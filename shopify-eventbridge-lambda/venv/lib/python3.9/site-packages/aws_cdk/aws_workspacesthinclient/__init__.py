'''
# AWS::WorkSpacesThinClient Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_workspacesthinclient as workspacesthinclient
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for WorkSpacesThinClient construct libraries](https://constructs.dev/search?q=workspacesthinclient)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::WorkSpacesThinClient resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_WorkSpacesThinClient.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::WorkSpacesThinClient](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_WorkSpacesThinClient.html).

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
    ITaggableV2 as _ITaggableV2_4e6798f8,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnEnvironment(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_workspacesthinclient.CfnEnvironment",
):
    '''Describes an environment.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesthinclient-environment.html
    :cloudformationResource: AWS::WorkSpacesThinClient::Environment
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_workspacesthinclient as workspacesthinclient
        
        cfn_environment = workspacesthinclient.CfnEnvironment(self, "MyCfnEnvironment",
            desktop_arn="desktopArn",
        
            # the properties below are optional
            desired_software_set_id="desiredSoftwareSetId",
            desktop_endpoint="desktopEndpoint",
            kms_key_arn="kmsKeyArn",
            maintenance_window=workspacesthinclient.CfnEnvironment.MaintenanceWindowProperty(
                type="type",
        
                # the properties below are optional
                apply_time_of="applyTimeOf",
                days_of_the_week=["daysOfTheWeek"],
                end_time_hour=123,
                end_time_minute=123,
                start_time_hour=123,
                start_time_minute=123
            ),
            name="name",
            software_set_update_mode="softwareSetUpdateMode",
            software_set_update_schedule="softwareSetUpdateSchedule",
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
        desktop_arn: builtins.str,
        desired_software_set_id: typing.Optional[builtins.str] = None,
        desktop_endpoint: typing.Optional[builtins.str] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        maintenance_window: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEnvironment.MaintenanceWindowProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        name: typing.Optional[builtins.str] = None,
        software_set_update_mode: typing.Optional[builtins.str] = None,
        software_set_update_schedule: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param desktop_arn: The Amazon Resource Name (ARN) of the desktop to stream from Amazon WorkSpaces, WorkSpaces Web, or AppStream 2.0.
        :param desired_software_set_id: The ID of the software set to apply.
        :param desktop_endpoint: The URL for the identity provider login (only for environments that use AppStream 2.0).
        :param kms_key_arn: The Amazon Resource Name (ARN) of the AWS Key Management Service key used to encrypt the environment.
        :param maintenance_window: A specification for a time window to apply software updates.
        :param name: The name of the environment.
        :param software_set_update_mode: An option to define which software updates to apply.
        :param software_set_update_schedule: An option to define if software updates should be applied within a maintenance window.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71de71c28d2a60cf68cffac5043975f99ea7f8d1359578b88902be0ceae59226)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnEnvironmentProps(
            desktop_arn=desktop_arn,
            desired_software_set_id=desired_software_set_id,
            desktop_endpoint=desktop_endpoint,
            kms_key_arn=kms_key_arn,
            maintenance_window=maintenance_window,
            name=name,
            software_set_update_mode=software_set_update_mode,
            software_set_update_schedule=software_set_update_schedule,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26fe79e63248e30588683f3e2be498f330e45668d4f430c9bab51ff32e3819af)
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
            type_hints = typing.get_type_hints(_typecheckingstub__23afcca05e2873dbbc5ba274641ea1fbace611682394d037d4ba7b21a9728a73)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrActivationCode")
    def attr_activation_code(self) -> builtins.str:
        '''The activation code to register a device to the environment.

        :cloudformationAttribute: ActivationCode
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrActivationCode"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the environment.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The timestamp of when the environment was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrDesktopType")
    def attr_desktop_type(self) -> builtins.str:
        '''The type of streaming desktop for the environment.

        :cloudformationAttribute: DesktopType
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDesktopType"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''Unique identifier of the environment.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrPendingSoftwareSetId")
    def attr_pending_software_set_id(self) -> builtins.str:
        '''The ID of the software set that is pending to be installed.

        :cloudformationAttribute: PendingSoftwareSetId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPendingSoftwareSetId"))

    @builtins.property
    @jsii.member(jsii_name="attrPendingSoftwareSetVersion")
    def attr_pending_software_set_version(self) -> builtins.str:
        '''The version of the software set that is pending to be installed.

        :cloudformationAttribute: PendingSoftwareSetVersion
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPendingSoftwareSetVersion"))

    @builtins.property
    @jsii.member(jsii_name="attrRegisteredDevicesCount")
    def attr_registered_devices_count(self) -> jsii.Number:
        '''The number of devices registered to the environment.

        :cloudformationAttribute: RegisteredDevicesCount
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrRegisteredDevicesCount"))

    @builtins.property
    @jsii.member(jsii_name="attrSoftwareSetComplianceStatus")
    def attr_software_set_compliance_status(self) -> builtins.str:
        '''Describes if the software currently installed on all devices in the environment is a supported version.

        :cloudformationAttribute: SoftwareSetComplianceStatus
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSoftwareSetComplianceStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdatedAt")
    def attr_updated_at(self) -> builtins.str:
        '''The timestamp of when the device was updated.

        :cloudformationAttribute: UpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdatedAt"))

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
    @jsii.member(jsii_name="desktopArn")
    def desktop_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the desktop to stream from Amazon WorkSpaces, WorkSpaces Web, or AppStream 2.0.'''
        return typing.cast(builtins.str, jsii.get(self, "desktopArn"))

    @desktop_arn.setter
    def desktop_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3e78b8edaf64495b4cbfe5aebcac6adc52a26a4ce11d20899c252e79e244206)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "desktopArn", value)

    @builtins.property
    @jsii.member(jsii_name="desiredSoftwareSetId")
    def desired_software_set_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the software set to apply.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "desiredSoftwareSetId"))

    @desired_software_set_id.setter
    def desired_software_set_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4c2ed95db27be33e3e87a02e5be888ffbd88c1858352eb59579f9982d0b49c4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "desiredSoftwareSetId", value)

    @builtins.property
    @jsii.member(jsii_name="desktopEndpoint")
    def desktop_endpoint(self) -> typing.Optional[builtins.str]:
        '''The URL for the identity provider login (only for environments that use AppStream 2.0).'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "desktopEndpoint"))

    @desktop_endpoint.setter
    def desktop_endpoint(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2010c2730a9883ccf9f06acb0b4a9053fdfc7f663d75f04c3541325dfde780de)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "desktopEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArn")
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the AWS Key Management Service key used to encrypt the environment.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyArn"))

    @kms_key_arn.setter
    def kms_key_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a24926b91b3bb51316eea9ee2d4402ec7f3406b7e104cbbe3be155f02445d2f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyArn", value)

    @builtins.property
    @jsii.member(jsii_name="maintenanceWindow")
    def maintenance_window(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEnvironment.MaintenanceWindowProperty"]]:
        '''A specification for a time window to apply software updates.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEnvironment.MaintenanceWindowProperty"]], jsii.get(self, "maintenanceWindow"))

    @maintenance_window.setter
    def maintenance_window(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEnvironment.MaintenanceWindowProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c024c54088873ac76991013b9257c5932410af2555e0e9f9fc47e5c1ae21e57)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maintenanceWindow", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the environment.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6fcadafc2cbcc71c5e3164f5e903a7a7ecaded42b442bf9cf4c254d4b48d7d81)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="softwareSetUpdateMode")
    def software_set_update_mode(self) -> typing.Optional[builtins.str]:
        '''An option to define which software updates to apply.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "softwareSetUpdateMode"))

    @software_set_update_mode.setter
    def software_set_update_mode(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__634183bf8790de645bea99a416b64f052c207d6aa181b57679c8929b24366ca6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "softwareSetUpdateMode", value)

    @builtins.property
    @jsii.member(jsii_name="softwareSetUpdateSchedule")
    def software_set_update_schedule(self) -> typing.Optional[builtins.str]:
        '''An option to define if software updates should be applied within a maintenance window.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "softwareSetUpdateSchedule"))

    @software_set_update_schedule.setter
    def software_set_update_schedule(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c745e69d677c6272e5f655e543ca77d28470467bcc0d05a9fdd1e3ec9490f3f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "softwareSetUpdateSchedule", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9a06cd7a626e651ef6d755e20fc0f4ae84020634911fc131aedefc4b786d8e4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_workspacesthinclient.CfnEnvironment.MaintenanceWindowProperty",
        jsii_struct_bases=[],
        name_mapping={
            "type": "type",
            "apply_time_of": "applyTimeOf",
            "days_of_the_week": "daysOfTheWeek",
            "end_time_hour": "endTimeHour",
            "end_time_minute": "endTimeMinute",
            "start_time_hour": "startTimeHour",
            "start_time_minute": "startTimeMinute",
        },
    )
    class MaintenanceWindowProperty:
        def __init__(
            self,
            *,
            type: builtins.str,
            apply_time_of: typing.Optional[builtins.str] = None,
            days_of_the_week: typing.Optional[typing.Sequence[builtins.str]] = None,
            end_time_hour: typing.Optional[jsii.Number] = None,
            end_time_minute: typing.Optional[jsii.Number] = None,
            start_time_hour: typing.Optional[jsii.Number] = None,
            start_time_minute: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Describes the maintenance window for a thin client device.

            :param type: An option to select the default or custom maintenance window.
            :param apply_time_of: The option to set the maintenance window during the device local time or Universal Coordinated Time (UTC).
            :param days_of_the_week: The days of the week during which the maintenance window is open.
            :param end_time_hour: The hour for the maintenance window end ( ``00`` - ``23`` ).
            :param end_time_minute: The minutes for the maintenance window end ( ``00`` - ``59`` ).
            :param start_time_hour: The hour for the maintenance window start ( ``00`` - ``23`` ).
            :param start_time_minute: The minutes past the hour for the maintenance window start ( ``00`` - ``59`` ).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesthinclient-environment-maintenancewindow.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_workspacesthinclient as workspacesthinclient
                
                maintenance_window_property = workspacesthinclient.CfnEnvironment.MaintenanceWindowProperty(
                    type="type",
                
                    # the properties below are optional
                    apply_time_of="applyTimeOf",
                    days_of_the_week=["daysOfTheWeek"],
                    end_time_hour=123,
                    end_time_minute=123,
                    start_time_hour=123,
                    start_time_minute=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fdddfb66c374577593a886bb5769e5d1bf823db9017d1cedea143c7da6ecd514)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument apply_time_of", value=apply_time_of, expected_type=type_hints["apply_time_of"])
                check_type(argname="argument days_of_the_week", value=days_of_the_week, expected_type=type_hints["days_of_the_week"])
                check_type(argname="argument end_time_hour", value=end_time_hour, expected_type=type_hints["end_time_hour"])
                check_type(argname="argument end_time_minute", value=end_time_minute, expected_type=type_hints["end_time_minute"])
                check_type(argname="argument start_time_hour", value=start_time_hour, expected_type=type_hints["start_time_hour"])
                check_type(argname="argument start_time_minute", value=start_time_minute, expected_type=type_hints["start_time_minute"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "type": type,
            }
            if apply_time_of is not None:
                self._values["apply_time_of"] = apply_time_of
            if days_of_the_week is not None:
                self._values["days_of_the_week"] = days_of_the_week
            if end_time_hour is not None:
                self._values["end_time_hour"] = end_time_hour
            if end_time_minute is not None:
                self._values["end_time_minute"] = end_time_minute
            if start_time_hour is not None:
                self._values["start_time_hour"] = start_time_hour
            if start_time_minute is not None:
                self._values["start_time_minute"] = start_time_minute

        @builtins.property
        def type(self) -> builtins.str:
            '''An option to select the default or custom maintenance window.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesthinclient-environment-maintenancewindow.html#cfn-workspacesthinclient-environment-maintenancewindow-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def apply_time_of(self) -> typing.Optional[builtins.str]:
            '''The option to set the maintenance window during the device local time or Universal Coordinated Time (UTC).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesthinclient-environment-maintenancewindow.html#cfn-workspacesthinclient-environment-maintenancewindow-applytimeof
            '''
            result = self._values.get("apply_time_of")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def days_of_the_week(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The days of the week during which the maintenance window is open.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesthinclient-environment-maintenancewindow.html#cfn-workspacesthinclient-environment-maintenancewindow-daysoftheweek
            '''
            result = self._values.get("days_of_the_week")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def end_time_hour(self) -> typing.Optional[jsii.Number]:
            '''The hour for the maintenance window end ( ``00`` - ``23`` ).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesthinclient-environment-maintenancewindow.html#cfn-workspacesthinclient-environment-maintenancewindow-endtimehour
            '''
            result = self._values.get("end_time_hour")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def end_time_minute(self) -> typing.Optional[jsii.Number]:
            '''The minutes for the maintenance window end ( ``00`` - ``59`` ).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesthinclient-environment-maintenancewindow.html#cfn-workspacesthinclient-environment-maintenancewindow-endtimeminute
            '''
            result = self._values.get("end_time_minute")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def start_time_hour(self) -> typing.Optional[jsii.Number]:
            '''The hour for the maintenance window start ( ``00`` - ``23`` ).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesthinclient-environment-maintenancewindow.html#cfn-workspacesthinclient-environment-maintenancewindow-starttimehour
            '''
            result = self._values.get("start_time_hour")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def start_time_minute(self) -> typing.Optional[jsii.Number]:
            '''The minutes past the hour for the maintenance window start ( ``00`` - ``59`` ).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesthinclient-environment-maintenancewindow.html#cfn-workspacesthinclient-environment-maintenancewindow-starttimeminute
            '''
            result = self._values.get("start_time_minute")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MaintenanceWindowProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_workspacesthinclient.CfnEnvironmentProps",
    jsii_struct_bases=[],
    name_mapping={
        "desktop_arn": "desktopArn",
        "desired_software_set_id": "desiredSoftwareSetId",
        "desktop_endpoint": "desktopEndpoint",
        "kms_key_arn": "kmsKeyArn",
        "maintenance_window": "maintenanceWindow",
        "name": "name",
        "software_set_update_mode": "softwareSetUpdateMode",
        "software_set_update_schedule": "softwareSetUpdateSchedule",
        "tags": "tags",
    },
)
class CfnEnvironmentProps:
    def __init__(
        self,
        *,
        desktop_arn: builtins.str,
        desired_software_set_id: typing.Optional[builtins.str] = None,
        desktop_endpoint: typing.Optional[builtins.str] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        maintenance_window: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.MaintenanceWindowProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        name: typing.Optional[builtins.str] = None,
        software_set_update_mode: typing.Optional[builtins.str] = None,
        software_set_update_schedule: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnEnvironment``.

        :param desktop_arn: The Amazon Resource Name (ARN) of the desktop to stream from Amazon WorkSpaces, WorkSpaces Web, or AppStream 2.0.
        :param desired_software_set_id: The ID of the software set to apply.
        :param desktop_endpoint: The URL for the identity provider login (only for environments that use AppStream 2.0).
        :param kms_key_arn: The Amazon Resource Name (ARN) of the AWS Key Management Service key used to encrypt the environment.
        :param maintenance_window: A specification for a time window to apply software updates.
        :param name: The name of the environment.
        :param software_set_update_mode: An option to define which software updates to apply.
        :param software_set_update_schedule: An option to define if software updates should be applied within a maintenance window.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesthinclient-environment.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_workspacesthinclient as workspacesthinclient
            
            cfn_environment_props = workspacesthinclient.CfnEnvironmentProps(
                desktop_arn="desktopArn",
            
                # the properties below are optional
                desired_software_set_id="desiredSoftwareSetId",
                desktop_endpoint="desktopEndpoint",
                kms_key_arn="kmsKeyArn",
                maintenance_window=workspacesthinclient.CfnEnvironment.MaintenanceWindowProperty(
                    type="type",
            
                    # the properties below are optional
                    apply_time_of="applyTimeOf",
                    days_of_the_week=["daysOfTheWeek"],
                    end_time_hour=123,
                    end_time_minute=123,
                    start_time_hour=123,
                    start_time_minute=123
                ),
                name="name",
                software_set_update_mode="softwareSetUpdateMode",
                software_set_update_schedule="softwareSetUpdateSchedule",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5ade8c81bf6b62d21c53769263cd25b48d66d29f3ae96ec22ac8fb14f2e4d33)
            check_type(argname="argument desktop_arn", value=desktop_arn, expected_type=type_hints["desktop_arn"])
            check_type(argname="argument desired_software_set_id", value=desired_software_set_id, expected_type=type_hints["desired_software_set_id"])
            check_type(argname="argument desktop_endpoint", value=desktop_endpoint, expected_type=type_hints["desktop_endpoint"])
            check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
            check_type(argname="argument maintenance_window", value=maintenance_window, expected_type=type_hints["maintenance_window"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument software_set_update_mode", value=software_set_update_mode, expected_type=type_hints["software_set_update_mode"])
            check_type(argname="argument software_set_update_schedule", value=software_set_update_schedule, expected_type=type_hints["software_set_update_schedule"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "desktop_arn": desktop_arn,
        }
        if desired_software_set_id is not None:
            self._values["desired_software_set_id"] = desired_software_set_id
        if desktop_endpoint is not None:
            self._values["desktop_endpoint"] = desktop_endpoint
        if kms_key_arn is not None:
            self._values["kms_key_arn"] = kms_key_arn
        if maintenance_window is not None:
            self._values["maintenance_window"] = maintenance_window
        if name is not None:
            self._values["name"] = name
        if software_set_update_mode is not None:
            self._values["software_set_update_mode"] = software_set_update_mode
        if software_set_update_schedule is not None:
            self._values["software_set_update_schedule"] = software_set_update_schedule
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def desktop_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the desktop to stream from Amazon WorkSpaces, WorkSpaces Web, or AppStream 2.0.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesthinclient-environment.html#cfn-workspacesthinclient-environment-desktoparn
        '''
        result = self._values.get("desktop_arn")
        assert result is not None, "Required property 'desktop_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def desired_software_set_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the software set to apply.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesthinclient-environment.html#cfn-workspacesthinclient-environment-desiredsoftwaresetid
        '''
        result = self._values.get("desired_software_set_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def desktop_endpoint(self) -> typing.Optional[builtins.str]:
        '''The URL for the identity provider login (only for environments that use AppStream 2.0).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesthinclient-environment.html#cfn-workspacesthinclient-environment-desktopendpoint
        '''
        result = self._values.get("desktop_endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the AWS Key Management Service key used to encrypt the environment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesthinclient-environment.html#cfn-workspacesthinclient-environment-kmskeyarn
        '''
        result = self._values.get("kms_key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def maintenance_window(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEnvironment.MaintenanceWindowProperty]]:
        '''A specification for a time window to apply software updates.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesthinclient-environment.html#cfn-workspacesthinclient-environment-maintenancewindow
        '''
        result = self._values.get("maintenance_window")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEnvironment.MaintenanceWindowProperty]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the environment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesthinclient-environment.html#cfn-workspacesthinclient-environment-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def software_set_update_mode(self) -> typing.Optional[builtins.str]:
        '''An option to define which software updates to apply.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesthinclient-environment.html#cfn-workspacesthinclient-environment-softwaresetupdatemode
        '''
        result = self._values.get("software_set_update_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def software_set_update_schedule(self) -> typing.Optional[builtins.str]:
        '''An option to define if software updates should be applied within a maintenance window.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesthinclient-environment.html#cfn-workspacesthinclient-environment-softwaresetupdateschedule
        '''
        result = self._values.get("software_set_update_schedule")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesthinclient-environment.html#cfn-workspacesthinclient-environment-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEnvironmentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnEnvironment",
    "CfnEnvironmentProps",
]

publication.publish()

def _typecheckingstub__71de71c28d2a60cf68cffac5043975f99ea7f8d1359578b88902be0ceae59226(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    desktop_arn: builtins.str,
    desired_software_set_id: typing.Optional[builtins.str] = None,
    desktop_endpoint: typing.Optional[builtins.str] = None,
    kms_key_arn: typing.Optional[builtins.str] = None,
    maintenance_window: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.MaintenanceWindowProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    software_set_update_mode: typing.Optional[builtins.str] = None,
    software_set_update_schedule: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26fe79e63248e30588683f3e2be498f330e45668d4f430c9bab51ff32e3819af(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23afcca05e2873dbbc5ba274641ea1fbace611682394d037d4ba7b21a9728a73(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3e78b8edaf64495b4cbfe5aebcac6adc52a26a4ce11d20899c252e79e244206(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4c2ed95db27be33e3e87a02e5be888ffbd88c1858352eb59579f9982d0b49c4(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2010c2730a9883ccf9f06acb0b4a9053fdfc7f663d75f04c3541325dfde780de(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a24926b91b3bb51316eea9ee2d4402ec7f3406b7e104cbbe3be155f02445d2f1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c024c54088873ac76991013b9257c5932410af2555e0e9f9fc47e5c1ae21e57(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEnvironment.MaintenanceWindowProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6fcadafc2cbcc71c5e3164f5e903a7a7ecaded42b442bf9cf4c254d4b48d7d81(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__634183bf8790de645bea99a416b64f052c207d6aa181b57679c8929b24366ca6(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c745e69d677c6272e5f655e543ca77d28470467bcc0d05a9fdd1e3ec9490f3f8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9a06cd7a626e651ef6d755e20fc0f4ae84020634911fc131aedefc4b786d8e4(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fdddfb66c374577593a886bb5769e5d1bf823db9017d1cedea143c7da6ecd514(
    *,
    type: builtins.str,
    apply_time_of: typing.Optional[builtins.str] = None,
    days_of_the_week: typing.Optional[typing.Sequence[builtins.str]] = None,
    end_time_hour: typing.Optional[jsii.Number] = None,
    end_time_minute: typing.Optional[jsii.Number] = None,
    start_time_hour: typing.Optional[jsii.Number] = None,
    start_time_minute: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5ade8c81bf6b62d21c53769263cd25b48d66d29f3ae96ec22ac8fb14f2e4d33(
    *,
    desktop_arn: builtins.str,
    desired_software_set_id: typing.Optional[builtins.str] = None,
    desktop_endpoint: typing.Optional[builtins.str] = None,
    kms_key_arn: typing.Optional[builtins.str] = None,
    maintenance_window: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.MaintenanceWindowProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    software_set_update_mode: typing.Optional[builtins.str] = None,
    software_set_update_schedule: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
