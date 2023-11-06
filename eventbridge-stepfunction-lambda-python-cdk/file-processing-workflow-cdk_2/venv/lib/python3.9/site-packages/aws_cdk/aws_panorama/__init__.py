'''
# AWS::Panorama Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_panorama as panorama
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for Panorama construct libraries](https://constructs.dev/search?q=panorama)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::Panorama resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Panorama.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::Panorama](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Panorama.html).

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
class CfnApplicationInstance(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_panorama.CfnApplicationInstance",
):
    '''Creates an application instance and deploys it to a device.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-applicationinstance.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_panorama as panorama
        
        cfn_application_instance = panorama.CfnApplicationInstance(self, "MyCfnApplicationInstance",
            default_runtime_context_device="defaultRuntimeContextDevice",
            manifest_payload=panorama.CfnApplicationInstance.ManifestPayloadProperty(
                payload_data="payloadData"
            ),
        
            # the properties below are optional
            application_instance_id_to_replace="applicationInstanceIdToReplace",
            description="description",
            manifest_overrides_payload=panorama.CfnApplicationInstance.ManifestOverridesPayloadProperty(
                payload_data="payloadData"
            ),
            name="name",
            runtime_role_arn="runtimeRoleArn",
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
        default_runtime_context_device: builtins.str,
        manifest_payload: typing.Union[_IResolvable_da3f097b, typing.Union["CfnApplicationInstance.ManifestPayloadProperty", typing.Dict[builtins.str, typing.Any]]],
        application_instance_id_to_replace: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        manifest_overrides_payload: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnApplicationInstance.ManifestOverridesPayloadProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        name: typing.Optional[builtins.str] = None,
        runtime_role_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param default_runtime_context_device: The device's ID.
        :param manifest_payload: The application's manifest document.
        :param application_instance_id_to_replace: The ID of an application instance to replace with the new instance.
        :param description: A description for the application instance.
        :param manifest_overrides_payload: Setting overrides for the application manifest.
        :param name: A name for the application instance.
        :param runtime_role_arn: The ARN of a runtime role for the application instance.
        :param tags: Tags for the application instance.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__efd0ba4cd6c0b4ee9023df6f956444617b610a622dce5eb667859d9d33cce0e1)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnApplicationInstanceProps(
            default_runtime_context_device=default_runtime_context_device,
            manifest_payload=manifest_payload,
            application_instance_id_to_replace=application_instance_id_to_replace,
            description=description,
            manifest_overrides_payload=manifest_overrides_payload,
            name=name,
            runtime_role_arn=runtime_role_arn,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f02c8fd6f1a71465462afea3d559ebb5b8ea0af1bc67afc99474bf782789ec30)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2d44dcdd2cf32e2db61481304b462fc2d18dd54bdc640c02d315dde2bc1bd73a)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrApplicationInstanceId")
    def attr_application_instance_id(self) -> builtins.str:
        '''The application instance's ID.

        :cloudformationAttribute: ApplicationInstanceId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrApplicationInstanceId"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''The application instance's ARN.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedTime")
    def attr_created_time(self) -> jsii.Number:
        '''The application instance's created time.

        :cloudformationAttribute: CreatedTime
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrCreatedTime"))

    @builtins.property
    @jsii.member(jsii_name="attrDefaultRuntimeContextDeviceName")
    def attr_default_runtime_context_device_name(self) -> builtins.str:
        '''The application instance's default runtime context device name.

        :cloudformationAttribute: DefaultRuntimeContextDeviceName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDefaultRuntimeContextDeviceName"))

    @builtins.property
    @jsii.member(jsii_name="attrHealthStatus")
    def attr_health_status(self) -> builtins.str:
        '''The application instance's health status.

        :cloudformationAttribute: HealthStatus
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrHealthStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrLastUpdatedTime")
    def attr_last_updated_time(self) -> jsii.Number:
        '''The application instance's last updated time.

        :cloudformationAttribute: LastUpdatedTime
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrLastUpdatedTime"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The application instance's status.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrStatusDescription")
    def attr_status_description(self) -> builtins.str:
        '''The application instance's status description.

        :cloudformationAttribute: StatusDescription
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatusDescription"))

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
    @jsii.member(jsii_name="defaultRuntimeContextDevice")
    def default_runtime_context_device(self) -> builtins.str:
        '''The device's ID.'''
        return typing.cast(builtins.str, jsii.get(self, "defaultRuntimeContextDevice"))

    @default_runtime_context_device.setter
    def default_runtime_context_device(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14dead437397488d87688e488f5b030e1acddee3c13863a0646a40942ead7dcc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultRuntimeContextDevice", value)

    @builtins.property
    @jsii.member(jsii_name="manifestPayload")
    def manifest_payload(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnApplicationInstance.ManifestPayloadProperty"]:
        '''The application's manifest document.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnApplicationInstance.ManifestPayloadProperty"], jsii.get(self, "manifestPayload"))

    @manifest_payload.setter
    def manifest_payload(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnApplicationInstance.ManifestPayloadProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4633be9adb22fb14ee3ed09114e5a580f0c1d44702407ccc944dc6786365f444)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "manifestPayload", value)

    @builtins.property
    @jsii.member(jsii_name="applicationInstanceIdToReplace")
    def application_instance_id_to_replace(self) -> typing.Optional[builtins.str]:
        '''The ID of an application instance to replace with the new instance.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "applicationInstanceIdToReplace"))

    @application_instance_id_to_replace.setter
    def application_instance_id_to_replace(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc7fbdde1d1b5abfbac0e504f36299a0ab3fa68bd2515240ccaa5b9aabb83f1e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationInstanceIdToReplace", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description for the application instance.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cdeccdf678155b692097126aa0b03f3329319b06cff4466ea53ac802efde82e3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="manifestOverridesPayload")
    def manifest_overrides_payload(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApplicationInstance.ManifestOverridesPayloadProperty"]]:
        '''Setting overrides for the application manifest.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApplicationInstance.ManifestOverridesPayloadProperty"]], jsii.get(self, "manifestOverridesPayload"))

    @manifest_overrides_payload.setter
    def manifest_overrides_payload(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApplicationInstance.ManifestOverridesPayloadProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b7471c650c5b47abc295c3f3540f494f924a6e4a67d4808e09a0c61dbfb5a40)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "manifestOverridesPayload", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''A name for the application instance.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1027678dff7d52641b35cc229158e34a793da6439b3b9c3a28f73f152ddba197)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="runtimeRoleArn")
    def runtime_role_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of a runtime role for the application instance.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "runtimeRoleArn"))

    @runtime_role_arn.setter
    def runtime_role_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4d8d9b27616402bbf99ce9903965d42b5395de944eb23c215804147caba15f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "runtimeRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Tags for the application instance.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc3bba124186482968d9b6204289729da05b6e7cb68d9a998bbd4aef3a949112)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_panorama.CfnApplicationInstance.ManifestOverridesPayloadProperty",
        jsii_struct_bases=[],
        name_mapping={"payload_data": "payloadData"},
    )
    class ManifestOverridesPayloadProperty:
        def __init__(
            self,
            *,
            payload_data: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Parameter overrides for an application instance.

            This is a JSON document that has a single key ( ``PayloadData`` ) where the value is an escaped string representation of the overrides document.

            :param payload_data: The overrides document.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-panorama-applicationinstance-manifestoverridespayload.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_panorama as panorama
                
                manifest_overrides_payload_property = panorama.CfnApplicationInstance.ManifestOverridesPayloadProperty(
                    payload_data="payloadData"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__def90730e19f581db1876aa8bbcc31c35d6dedb67b9cf6ad9012b0e71917b4ef)
                check_type(argname="argument payload_data", value=payload_data, expected_type=type_hints["payload_data"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if payload_data is not None:
                self._values["payload_data"] = payload_data

        @builtins.property
        def payload_data(self) -> typing.Optional[builtins.str]:
            '''The overrides document.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-panorama-applicationinstance-manifestoverridespayload.html#cfn-panorama-applicationinstance-manifestoverridespayload-payloaddata
            '''
            result = self._values.get("payload_data")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ManifestOverridesPayloadProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_panorama.CfnApplicationInstance.ManifestPayloadProperty",
        jsii_struct_bases=[],
        name_mapping={"payload_data": "payloadData"},
    )
    class ManifestPayloadProperty:
        def __init__(
            self,
            *,
            payload_data: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A application verion's manifest file.

            This is a JSON document that has a single key ( ``PayloadData`` ) where the value is an escaped string representation of the application manifest ( ``graph.json`` ). This file is located in the ``graphs`` folder in your application source.

            :param payload_data: The application manifest.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-panorama-applicationinstance-manifestpayload.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_panorama as panorama
                
                manifest_payload_property = panorama.CfnApplicationInstance.ManifestPayloadProperty(
                    payload_data="payloadData"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a5d7cb2c1d20afe24346d68fd8c261ab008166cc9e17ce83f5e21e6c3e1d3677)
                check_type(argname="argument payload_data", value=payload_data, expected_type=type_hints["payload_data"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if payload_data is not None:
                self._values["payload_data"] = payload_data

        @builtins.property
        def payload_data(self) -> typing.Optional[builtins.str]:
            '''The application manifest.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-panorama-applicationinstance-manifestpayload.html#cfn-panorama-applicationinstance-manifestpayload-payloaddata
            '''
            result = self._values.get("payload_data")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ManifestPayloadProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_panorama.CfnApplicationInstanceProps",
    jsii_struct_bases=[],
    name_mapping={
        "default_runtime_context_device": "defaultRuntimeContextDevice",
        "manifest_payload": "manifestPayload",
        "application_instance_id_to_replace": "applicationInstanceIdToReplace",
        "description": "description",
        "manifest_overrides_payload": "manifestOverridesPayload",
        "name": "name",
        "runtime_role_arn": "runtimeRoleArn",
        "tags": "tags",
    },
)
class CfnApplicationInstanceProps:
    def __init__(
        self,
        *,
        default_runtime_context_device: builtins.str,
        manifest_payload: typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplicationInstance.ManifestPayloadProperty, typing.Dict[builtins.str, typing.Any]]],
        application_instance_id_to_replace: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        manifest_overrides_payload: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplicationInstance.ManifestOverridesPayloadProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        name: typing.Optional[builtins.str] = None,
        runtime_role_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnApplicationInstance``.

        :param default_runtime_context_device: The device's ID.
        :param manifest_payload: The application's manifest document.
        :param application_instance_id_to_replace: The ID of an application instance to replace with the new instance.
        :param description: A description for the application instance.
        :param manifest_overrides_payload: Setting overrides for the application manifest.
        :param name: A name for the application instance.
        :param runtime_role_arn: The ARN of a runtime role for the application instance.
        :param tags: Tags for the application instance.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-applicationinstance.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_panorama as panorama
            
            cfn_application_instance_props = panorama.CfnApplicationInstanceProps(
                default_runtime_context_device="defaultRuntimeContextDevice",
                manifest_payload=panorama.CfnApplicationInstance.ManifestPayloadProperty(
                    payload_data="payloadData"
                ),
            
                # the properties below are optional
                application_instance_id_to_replace="applicationInstanceIdToReplace",
                description="description",
                manifest_overrides_payload=panorama.CfnApplicationInstance.ManifestOverridesPayloadProperty(
                    payload_data="payloadData"
                ),
                name="name",
                runtime_role_arn="runtimeRoleArn",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86e1bdf3f249b2bc0c09d79eca2507b458b360a5856626b251d3b11a03bcb807)
            check_type(argname="argument default_runtime_context_device", value=default_runtime_context_device, expected_type=type_hints["default_runtime_context_device"])
            check_type(argname="argument manifest_payload", value=manifest_payload, expected_type=type_hints["manifest_payload"])
            check_type(argname="argument application_instance_id_to_replace", value=application_instance_id_to_replace, expected_type=type_hints["application_instance_id_to_replace"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument manifest_overrides_payload", value=manifest_overrides_payload, expected_type=type_hints["manifest_overrides_payload"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument runtime_role_arn", value=runtime_role_arn, expected_type=type_hints["runtime_role_arn"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "default_runtime_context_device": default_runtime_context_device,
            "manifest_payload": manifest_payload,
        }
        if application_instance_id_to_replace is not None:
            self._values["application_instance_id_to_replace"] = application_instance_id_to_replace
        if description is not None:
            self._values["description"] = description
        if manifest_overrides_payload is not None:
            self._values["manifest_overrides_payload"] = manifest_overrides_payload
        if name is not None:
            self._values["name"] = name
        if runtime_role_arn is not None:
            self._values["runtime_role_arn"] = runtime_role_arn
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def default_runtime_context_device(self) -> builtins.str:
        '''The device's ID.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-applicationinstance.html#cfn-panorama-applicationinstance-defaultruntimecontextdevice
        '''
        result = self._values.get("default_runtime_context_device")
        assert result is not None, "Required property 'default_runtime_context_device' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def manifest_payload(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnApplicationInstance.ManifestPayloadProperty]:
        '''The application's manifest document.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-applicationinstance.html#cfn-panorama-applicationinstance-manifestpayload
        '''
        result = self._values.get("manifest_payload")
        assert result is not None, "Required property 'manifest_payload' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnApplicationInstance.ManifestPayloadProperty], result)

    @builtins.property
    def application_instance_id_to_replace(self) -> typing.Optional[builtins.str]:
        '''The ID of an application instance to replace with the new instance.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-applicationinstance.html#cfn-panorama-applicationinstance-applicationinstanceidtoreplace
        '''
        result = self._values.get("application_instance_id_to_replace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description for the application instance.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-applicationinstance.html#cfn-panorama-applicationinstance-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def manifest_overrides_payload(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApplicationInstance.ManifestOverridesPayloadProperty]]:
        '''Setting overrides for the application manifest.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-applicationinstance.html#cfn-panorama-applicationinstance-manifestoverridespayload
        '''
        result = self._values.get("manifest_overrides_payload")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApplicationInstance.ManifestOverridesPayloadProperty]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''A name for the application instance.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-applicationinstance.html#cfn-panorama-applicationinstance-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def runtime_role_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of a runtime role for the application instance.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-applicationinstance.html#cfn-panorama-applicationinstance-runtimerolearn
        '''
        result = self._values.get("runtime_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Tags for the application instance.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-applicationinstance.html#cfn-panorama-applicationinstance-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApplicationInstanceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnPackage(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_panorama.CfnPackage",
):
    '''Creates a package and storage location in an Amazon S3 access point.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-package.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_panorama as panorama
        
        cfn_package = panorama.CfnPackage(self, "MyCfnPackage",
            package_name="packageName",
        
            # the properties below are optional
            storage_location=panorama.CfnPackage.StorageLocationProperty(
                binary_prefix_location="binaryPrefixLocation",
                bucket="bucket",
                generated_prefix_location="generatedPrefixLocation",
                manifest_prefix_location="manifestPrefixLocation",
                repo_prefix_location="repoPrefixLocation"
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
        package_name: builtins.str,
        storage_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPackage.StorageLocationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param package_name: A name for the package.
        :param storage_location: 
        :param tags: Tags for the package.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__014b23b28acc37a82edebe15e1628f0ee03393a0354f498b25ce8519a95771ba)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPackageProps(
            package_name=package_name, storage_location=storage_location, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d571cb582323b52428cb462f12dd0ba0765010a338ed79ea157b3fc920aa535a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__48b633691fd3e7cd1d578298776aa8c23b15613ce9ad1613972a3229dd859eb0)
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
        '''The package's ARN.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedTime")
    def attr_created_time(self) -> jsii.Number:
        '''The item's created time.

        :cloudformationAttribute: CreatedTime
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrCreatedTime"))

    @builtins.property
    @jsii.member(jsii_name="attrPackageId")
    def attr_package_id(self) -> builtins.str:
        '''The package's ID.

        :cloudformationAttribute: PackageId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPackageId"))

    @builtins.property
    @jsii.member(jsii_name="attrStorageLocationBinaryPrefixLocation")
    def attr_storage_location_binary_prefix_location(self) -> builtins.str:
        '''
        :cloudformationAttribute: StorageLocation.BinaryPrefixLocation
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStorageLocationBinaryPrefixLocation"))

    @builtins.property
    @jsii.member(jsii_name="attrStorageLocationBucket")
    def attr_storage_location_bucket(self) -> builtins.str:
        '''
        :cloudformationAttribute: StorageLocation.Bucket
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStorageLocationBucket"))

    @builtins.property
    @jsii.member(jsii_name="attrStorageLocationGeneratedPrefixLocation")
    def attr_storage_location_generated_prefix_location(self) -> builtins.str:
        '''
        :cloudformationAttribute: StorageLocation.GeneratedPrefixLocation
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStorageLocationGeneratedPrefixLocation"))

    @builtins.property
    @jsii.member(jsii_name="attrStorageLocationManifestPrefixLocation")
    def attr_storage_location_manifest_prefix_location(self) -> builtins.str:
        '''
        :cloudformationAttribute: StorageLocation.ManifestPrefixLocation
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStorageLocationManifestPrefixLocation"))

    @builtins.property
    @jsii.member(jsii_name="attrStorageLocationRepoPrefixLocation")
    def attr_storage_location_repo_prefix_location(self) -> builtins.str:
        '''
        :cloudformationAttribute: StorageLocation.RepoPrefixLocation
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStorageLocationRepoPrefixLocation"))

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
    @jsii.member(jsii_name="packageName")
    def package_name(self) -> builtins.str:
        '''A name for the package.'''
        return typing.cast(builtins.str, jsii.get(self, "packageName"))

    @package_name.setter
    def package_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a932afc5efe9051f5c2e446dd907c22ad3ee75863d1133e888d379318105226b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "packageName", value)

    @builtins.property
    @jsii.member(jsii_name="storageLocation")
    def storage_location(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPackage.StorageLocationProperty"]]:
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPackage.StorageLocationProperty"]], jsii.get(self, "storageLocation"))

    @storage_location.setter
    def storage_location(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPackage.StorageLocationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1eaa635a573937e0a68237889912d86f74cf48c8584d1f51e6c4d9cc116ee909)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageLocation", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Tags for the package.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d23cf48bb2587552001b9c9c1738689c65ba3fb8070925cb3522000952eddac5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_panorama.CfnPackage.StorageLocationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "binary_prefix_location": "binaryPrefixLocation",
            "bucket": "bucket",
            "generated_prefix_location": "generatedPrefixLocation",
            "manifest_prefix_location": "manifestPrefixLocation",
            "repo_prefix_location": "repoPrefixLocation",
        },
    )
    class StorageLocationProperty:
        def __init__(
            self,
            *,
            binary_prefix_location: typing.Optional[builtins.str] = None,
            bucket: typing.Optional[builtins.str] = None,
            generated_prefix_location: typing.Optional[builtins.str] = None,
            manifest_prefix_location: typing.Optional[builtins.str] = None,
            repo_prefix_location: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param binary_prefix_location: 
            :param bucket: 
            :param generated_prefix_location: 
            :param manifest_prefix_location: 
            :param repo_prefix_location: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-panorama-package-storagelocation.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_panorama as panorama
                
                storage_location_property = panorama.CfnPackage.StorageLocationProperty(
                    binary_prefix_location="binaryPrefixLocation",
                    bucket="bucket",
                    generated_prefix_location="generatedPrefixLocation",
                    manifest_prefix_location="manifestPrefixLocation",
                    repo_prefix_location="repoPrefixLocation"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2c474d68f6b2f0c2e6021bd9cf93a01c9cb04e35b4b763184a117165d542c60f)
                check_type(argname="argument binary_prefix_location", value=binary_prefix_location, expected_type=type_hints["binary_prefix_location"])
                check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
                check_type(argname="argument generated_prefix_location", value=generated_prefix_location, expected_type=type_hints["generated_prefix_location"])
                check_type(argname="argument manifest_prefix_location", value=manifest_prefix_location, expected_type=type_hints["manifest_prefix_location"])
                check_type(argname="argument repo_prefix_location", value=repo_prefix_location, expected_type=type_hints["repo_prefix_location"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if binary_prefix_location is not None:
                self._values["binary_prefix_location"] = binary_prefix_location
            if bucket is not None:
                self._values["bucket"] = bucket
            if generated_prefix_location is not None:
                self._values["generated_prefix_location"] = generated_prefix_location
            if manifest_prefix_location is not None:
                self._values["manifest_prefix_location"] = manifest_prefix_location
            if repo_prefix_location is not None:
                self._values["repo_prefix_location"] = repo_prefix_location

        @builtins.property
        def binary_prefix_location(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-panorama-package-storagelocation.html#cfn-panorama-package-storagelocation-binaryprefixlocation
            '''
            result = self._values.get("binary_prefix_location")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def bucket(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-panorama-package-storagelocation.html#cfn-panorama-package-storagelocation-bucket
            '''
            result = self._values.get("bucket")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def generated_prefix_location(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-panorama-package-storagelocation.html#cfn-panorama-package-storagelocation-generatedprefixlocation
            '''
            result = self._values.get("generated_prefix_location")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def manifest_prefix_location(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-panorama-package-storagelocation.html#cfn-panorama-package-storagelocation-manifestprefixlocation
            '''
            result = self._values.get("manifest_prefix_location")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def repo_prefix_location(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-panorama-package-storagelocation.html#cfn-panorama-package-storagelocation-repoprefixlocation
            '''
            result = self._values.get("repo_prefix_location")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StorageLocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_panorama.CfnPackageProps",
    jsii_struct_bases=[],
    name_mapping={
        "package_name": "packageName",
        "storage_location": "storageLocation",
        "tags": "tags",
    },
)
class CfnPackageProps:
    def __init__(
        self,
        *,
        package_name: builtins.str,
        storage_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPackage.StorageLocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnPackage``.

        :param package_name: A name for the package.
        :param storage_location: 
        :param tags: Tags for the package.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-package.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_panorama as panorama
            
            cfn_package_props = panorama.CfnPackageProps(
                package_name="packageName",
            
                # the properties below are optional
                storage_location=panorama.CfnPackage.StorageLocationProperty(
                    binary_prefix_location="binaryPrefixLocation",
                    bucket="bucket",
                    generated_prefix_location="generatedPrefixLocation",
                    manifest_prefix_location="manifestPrefixLocation",
                    repo_prefix_location="repoPrefixLocation"
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1b52b8a916ab2fd0db4662da21b8aba3f3a0bd1b465b93c901724b70fe754a8)
            check_type(argname="argument package_name", value=package_name, expected_type=type_hints["package_name"])
            check_type(argname="argument storage_location", value=storage_location, expected_type=type_hints["storage_location"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "package_name": package_name,
        }
        if storage_location is not None:
            self._values["storage_location"] = storage_location
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def package_name(self) -> builtins.str:
        '''A name for the package.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-package.html#cfn-panorama-package-packagename
        '''
        result = self._values.get("package_name")
        assert result is not None, "Required property 'package_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def storage_location(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPackage.StorageLocationProperty]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-package.html#cfn-panorama-package-storagelocation
        '''
        result = self._values.get("storage_location")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPackage.StorageLocationProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Tags for the package.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-package.html#cfn-panorama-package-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPackageProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnPackageVersion(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_panorama.CfnPackageVersion",
):
    '''Registers a package version.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-packageversion.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_panorama as panorama
        
        cfn_package_version = panorama.CfnPackageVersion(self, "MyCfnPackageVersion",
            package_id="packageId",
            package_version="packageVersion",
            patch_version="patchVersion",
        
            # the properties below are optional
            mark_latest=False,
            owner_account="ownerAccount",
            updated_latest_patch_version="updatedLatestPatchVersion"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        package_id: builtins.str,
        package_version: builtins.str,
        patch_version: builtins.str,
        mark_latest: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        owner_account: typing.Optional[builtins.str] = None,
        updated_latest_patch_version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param package_id: A package ID.
        :param package_version: A package version.
        :param patch_version: A patch version.
        :param mark_latest: Whether to mark the new version as the latest version.
        :param owner_account: An owner account.
        :param updated_latest_patch_version: If the version was marked latest, the new version to maker as latest.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13ea96f0334a230d99017463d74c935661d9ebbe5ba26311c01f75163ae86682)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPackageVersionProps(
            package_id=package_id,
            package_version=package_version,
            patch_version=patch_version,
            mark_latest=mark_latest,
            owner_account=owner_account,
            updated_latest_patch_version=updated_latest_patch_version,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b79fc517c8a77d42c17a94e90d22d67539a81f6b46ac88ee957d355be61e6070)
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
            type_hints = typing.get_type_hints(_typecheckingstub__730fbb169a1c450a3e6ac869670128abfd32dd0fcaa827f1a07aba8adf06ab1c)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrIsLatestPatch")
    def attr_is_latest_patch(self) -> _IResolvable_da3f097b:
        '''Whether the package version is the latest version.

        :cloudformationAttribute: IsLatestPatch
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrIsLatestPatch"))

    @builtins.property
    @jsii.member(jsii_name="attrPackageArn")
    def attr_package_arn(self) -> builtins.str:
        '''The package version's ARN.

        :cloudformationAttribute: PackageArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPackageArn"))

    @builtins.property
    @jsii.member(jsii_name="attrPackageName")
    def attr_package_name(self) -> builtins.str:
        '''The package version's name.

        :cloudformationAttribute: PackageName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPackageName"))

    @builtins.property
    @jsii.member(jsii_name="attrRegisteredTime")
    def attr_registered_time(self) -> jsii.Number:
        '''The package version's registered time.

        :cloudformationAttribute: RegisteredTime
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrRegisteredTime"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The package version's status.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrStatusDescription")
    def attr_status_description(self) -> builtins.str:
        '''The package version's status description.

        :cloudformationAttribute: StatusDescription
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatusDescription"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="packageId")
    def package_id(self) -> builtins.str:
        '''A package ID.'''
        return typing.cast(builtins.str, jsii.get(self, "packageId"))

    @package_id.setter
    def package_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fbce3779996f3b0ac4831b659f592ca4a65199309309cb43bc7ddb5f9c16c597)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "packageId", value)

    @builtins.property
    @jsii.member(jsii_name="packageVersion")
    def package_version(self) -> builtins.str:
        '''A package version.'''
        return typing.cast(builtins.str, jsii.get(self, "packageVersion"))

    @package_version.setter
    def package_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee61c5c4023cba8ce285236309a3782afdc1c31e1bc0c75a1b70011d141b5328)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "packageVersion", value)

    @builtins.property
    @jsii.member(jsii_name="patchVersion")
    def patch_version(self) -> builtins.str:
        '''A patch version.'''
        return typing.cast(builtins.str, jsii.get(self, "patchVersion"))

    @patch_version.setter
    def patch_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7a55a07b0a31f8dcc3c95902dfb0b4cb99db0159f57f4b31666445a11a50a9a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "patchVersion", value)

    @builtins.property
    @jsii.member(jsii_name="markLatest")
    def mark_latest(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Whether to mark the new version as the latest version.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "markLatest"))

    @mark_latest.setter
    def mark_latest(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__feaca7cbbeb3ea13ff355cd5c7ca768921046c2e7bfcbbe8f2380c53bcbe38b7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "markLatest", value)

    @builtins.property
    @jsii.member(jsii_name="ownerAccount")
    def owner_account(self) -> typing.Optional[builtins.str]:
        '''An owner account.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ownerAccount"))

    @owner_account.setter
    def owner_account(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4a02ccb498f6e627400881f12832f7791d330ce6cf68e4fba78b66beb3b04a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ownerAccount", value)

    @builtins.property
    @jsii.member(jsii_name="updatedLatestPatchVersion")
    def updated_latest_patch_version(self) -> typing.Optional[builtins.str]:
        '''If the version was marked latest, the new version to maker as latest.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "updatedLatestPatchVersion"))

    @updated_latest_patch_version.setter
    def updated_latest_patch_version(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67beb15f93d101823e57a760b1affa4d22f8ec0110bd2f5fe3c329c87f8b56c3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "updatedLatestPatchVersion", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_panorama.CfnPackageVersionProps",
    jsii_struct_bases=[],
    name_mapping={
        "package_id": "packageId",
        "package_version": "packageVersion",
        "patch_version": "patchVersion",
        "mark_latest": "markLatest",
        "owner_account": "ownerAccount",
        "updated_latest_patch_version": "updatedLatestPatchVersion",
    },
)
class CfnPackageVersionProps:
    def __init__(
        self,
        *,
        package_id: builtins.str,
        package_version: builtins.str,
        patch_version: builtins.str,
        mark_latest: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        owner_account: typing.Optional[builtins.str] = None,
        updated_latest_patch_version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnPackageVersion``.

        :param package_id: A package ID.
        :param package_version: A package version.
        :param patch_version: A patch version.
        :param mark_latest: Whether to mark the new version as the latest version.
        :param owner_account: An owner account.
        :param updated_latest_patch_version: If the version was marked latest, the new version to maker as latest.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-packageversion.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_panorama as panorama
            
            cfn_package_version_props = panorama.CfnPackageVersionProps(
                package_id="packageId",
                package_version="packageVersion",
                patch_version="patchVersion",
            
                # the properties below are optional
                mark_latest=False,
                owner_account="ownerAccount",
                updated_latest_patch_version="updatedLatestPatchVersion"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a64dc269b0bd6d71d3221fbd05486743bcd745dd462213003c3e1bdcc512b47)
            check_type(argname="argument package_id", value=package_id, expected_type=type_hints["package_id"])
            check_type(argname="argument package_version", value=package_version, expected_type=type_hints["package_version"])
            check_type(argname="argument patch_version", value=patch_version, expected_type=type_hints["patch_version"])
            check_type(argname="argument mark_latest", value=mark_latest, expected_type=type_hints["mark_latest"])
            check_type(argname="argument owner_account", value=owner_account, expected_type=type_hints["owner_account"])
            check_type(argname="argument updated_latest_patch_version", value=updated_latest_patch_version, expected_type=type_hints["updated_latest_patch_version"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "package_id": package_id,
            "package_version": package_version,
            "patch_version": patch_version,
        }
        if mark_latest is not None:
            self._values["mark_latest"] = mark_latest
        if owner_account is not None:
            self._values["owner_account"] = owner_account
        if updated_latest_patch_version is not None:
            self._values["updated_latest_patch_version"] = updated_latest_patch_version

    @builtins.property
    def package_id(self) -> builtins.str:
        '''A package ID.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-packageversion.html#cfn-panorama-packageversion-packageid
        '''
        result = self._values.get("package_id")
        assert result is not None, "Required property 'package_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def package_version(self) -> builtins.str:
        '''A package version.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-packageversion.html#cfn-panorama-packageversion-packageversion
        '''
        result = self._values.get("package_version")
        assert result is not None, "Required property 'package_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def patch_version(self) -> builtins.str:
        '''A patch version.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-packageversion.html#cfn-panorama-packageversion-patchversion
        '''
        result = self._values.get("patch_version")
        assert result is not None, "Required property 'patch_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def mark_latest(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Whether to mark the new version as the latest version.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-packageversion.html#cfn-panorama-packageversion-marklatest
        '''
        result = self._values.get("mark_latest")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def owner_account(self) -> typing.Optional[builtins.str]:
        '''An owner account.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-packageversion.html#cfn-panorama-packageversion-owneraccount
        '''
        result = self._values.get("owner_account")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def updated_latest_patch_version(self) -> typing.Optional[builtins.str]:
        '''If the version was marked latest, the new version to maker as latest.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-packageversion.html#cfn-panorama-packageversion-updatedlatestpatchversion
        '''
        result = self._values.get("updated_latest_patch_version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPackageVersionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnApplicationInstance",
    "CfnApplicationInstanceProps",
    "CfnPackage",
    "CfnPackageProps",
    "CfnPackageVersion",
    "CfnPackageVersionProps",
]

publication.publish()

def _typecheckingstub__efd0ba4cd6c0b4ee9023df6f956444617b610a622dce5eb667859d9d33cce0e1(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    default_runtime_context_device: builtins.str,
    manifest_payload: typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplicationInstance.ManifestPayloadProperty, typing.Dict[builtins.str, typing.Any]]],
    application_instance_id_to_replace: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    manifest_overrides_payload: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplicationInstance.ManifestOverridesPayloadProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    runtime_role_arn: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f02c8fd6f1a71465462afea3d559ebb5b8ea0af1bc67afc99474bf782789ec30(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d44dcdd2cf32e2db61481304b462fc2d18dd54bdc640c02d315dde2bc1bd73a(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14dead437397488d87688e488f5b030e1acddee3c13863a0646a40942ead7dcc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4633be9adb22fb14ee3ed09114e5a580f0c1d44702407ccc944dc6786365f444(
    value: typing.Union[_IResolvable_da3f097b, CfnApplicationInstance.ManifestPayloadProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc7fbdde1d1b5abfbac0e504f36299a0ab3fa68bd2515240ccaa5b9aabb83f1e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cdeccdf678155b692097126aa0b03f3329319b06cff4466ea53ac802efde82e3(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b7471c650c5b47abc295c3f3540f494f924a6e4a67d4808e09a0c61dbfb5a40(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApplicationInstance.ManifestOverridesPayloadProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1027678dff7d52641b35cc229158e34a793da6439b3b9c3a28f73f152ddba197(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4d8d9b27616402bbf99ce9903965d42b5395de944eb23c215804147caba15f7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc3bba124186482968d9b6204289729da05b6e7cb68d9a998bbd4aef3a949112(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__def90730e19f581db1876aa8bbcc31c35d6dedb67b9cf6ad9012b0e71917b4ef(
    *,
    payload_data: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5d7cb2c1d20afe24346d68fd8c261ab008166cc9e17ce83f5e21e6c3e1d3677(
    *,
    payload_data: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86e1bdf3f249b2bc0c09d79eca2507b458b360a5856626b251d3b11a03bcb807(
    *,
    default_runtime_context_device: builtins.str,
    manifest_payload: typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplicationInstance.ManifestPayloadProperty, typing.Dict[builtins.str, typing.Any]]],
    application_instance_id_to_replace: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    manifest_overrides_payload: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplicationInstance.ManifestOverridesPayloadProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    runtime_role_arn: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__014b23b28acc37a82edebe15e1628f0ee03393a0354f498b25ce8519a95771ba(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    package_name: builtins.str,
    storage_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPackage.StorageLocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d571cb582323b52428cb462f12dd0ba0765010a338ed79ea157b3fc920aa535a(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48b633691fd3e7cd1d578298776aa8c23b15613ce9ad1613972a3229dd859eb0(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a932afc5efe9051f5c2e446dd907c22ad3ee75863d1133e888d379318105226b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1eaa635a573937e0a68237889912d86f74cf48c8584d1f51e6c4d9cc116ee909(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPackage.StorageLocationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d23cf48bb2587552001b9c9c1738689c65ba3fb8070925cb3522000952eddac5(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c474d68f6b2f0c2e6021bd9cf93a01c9cb04e35b4b763184a117165d542c60f(
    *,
    binary_prefix_location: typing.Optional[builtins.str] = None,
    bucket: typing.Optional[builtins.str] = None,
    generated_prefix_location: typing.Optional[builtins.str] = None,
    manifest_prefix_location: typing.Optional[builtins.str] = None,
    repo_prefix_location: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1b52b8a916ab2fd0db4662da21b8aba3f3a0bd1b465b93c901724b70fe754a8(
    *,
    package_name: builtins.str,
    storage_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPackage.StorageLocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13ea96f0334a230d99017463d74c935661d9ebbe5ba26311c01f75163ae86682(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    package_id: builtins.str,
    package_version: builtins.str,
    patch_version: builtins.str,
    mark_latest: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    owner_account: typing.Optional[builtins.str] = None,
    updated_latest_patch_version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b79fc517c8a77d42c17a94e90d22d67539a81f6b46ac88ee957d355be61e6070(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__730fbb169a1c450a3e6ac869670128abfd32dd0fcaa827f1a07aba8adf06ab1c(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fbce3779996f3b0ac4831b659f592ca4a65199309309cb43bc7ddb5f9c16c597(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee61c5c4023cba8ce285236309a3782afdc1c31e1bc0c75a1b70011d141b5328(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7a55a07b0a31f8dcc3c95902dfb0b4cb99db0159f57f4b31666445a11a50a9a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__feaca7cbbeb3ea13ff355cd5c7ca768921046c2e7bfcbbe8f2380c53bcbe38b7(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4a02ccb498f6e627400881f12832f7791d330ce6cf68e4fba78b66beb3b04a0(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67beb15f93d101823e57a760b1affa4d22f8ec0110bd2f5fe3c329c87f8b56c3(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a64dc269b0bd6d71d3221fbd05486743bcd745dd462213003c3e1bdcc512b47(
    *,
    package_id: builtins.str,
    package_version: builtins.str,
    patch_version: builtins.str,
    mark_latest: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    owner_account: typing.Optional[builtins.str] = None,
    updated_latest_patch_version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
