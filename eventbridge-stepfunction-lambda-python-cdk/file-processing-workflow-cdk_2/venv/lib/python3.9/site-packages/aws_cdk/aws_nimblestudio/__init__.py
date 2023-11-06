'''
# AWS::NimbleStudio Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_nimblestudio as nimblestudio
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for NimbleStudio construct libraries](https://constructs.dev/search?q=nimblestudio)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::NimbleStudio resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_NimbleStudio.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::NimbleStudio](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_NimbleStudio.html).

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
    ITaggable as _ITaggable_36806126,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnLaunchProfile(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_nimblestudio.CfnLaunchProfile",
):
    '''The ``AWS::NimbleStudio::LaunchProfile`` resource represents access permissions for a set of studio components, including types of workstations, render farms, and shared file systems.

    Launch profiles are shared with studio users to give them access to the set of studio components.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-launchprofile.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_nimblestudio as nimblestudio
        
        cfn_launch_profile = nimblestudio.CfnLaunchProfile(self, "MyCfnLaunchProfile",
            ec2_subnet_ids=["ec2SubnetIds"],
            launch_profile_protocol_versions=["launchProfileProtocolVersions"],
            name="name",
            stream_configuration=nimblestudio.CfnLaunchProfile.StreamConfigurationProperty(
                clipboard_mode="clipboardMode",
                ec2_instance_types=["ec2InstanceTypes"],
                streaming_image_ids=["streamingImageIds"],
        
                # the properties below are optional
                automatic_termination_mode="automaticTerminationMode",
                max_session_length_in_minutes=123,
                max_stopped_session_length_in_minutes=123,
                session_backup=nimblestudio.CfnLaunchProfile.StreamConfigurationSessionBackupProperty(
                    max_backups_to_retain=123,
                    mode="mode"
                ),
                session_persistence_mode="sessionPersistenceMode",
                session_storage=nimblestudio.CfnLaunchProfile.StreamConfigurationSessionStorageProperty(
                    mode=["mode"],
        
                    # the properties below are optional
                    root=nimblestudio.CfnLaunchProfile.StreamingSessionStorageRootProperty(
                        linux="linux",
                        windows="windows"
                    )
                ),
                volume_configuration=nimblestudio.CfnLaunchProfile.VolumeConfigurationProperty(
                    iops=123,
                    size=123,
                    throughput=123
                )
            ),
            studio_component_ids=["studioComponentIds"],
            studio_id="studioId",
        
            # the properties below are optional
            description="description",
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
        ec2_subnet_ids: typing.Sequence[builtins.str],
        launch_profile_protocol_versions: typing.Sequence[builtins.str],
        name: builtins.str,
        stream_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnLaunchProfile.StreamConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        studio_component_ids: typing.Sequence[builtins.str],
        studio_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param ec2_subnet_ids: Unique identifiers for a collection of EC2 subnets.
        :param launch_profile_protocol_versions: The version number of the protocol that is used by the launch profile. The only valid version is "2021-03-31".
        :param name: A friendly name for the launch profile.
        :param stream_configuration: A configuration for a streaming session.
        :param studio_component_ids: Unique identifiers for a collection of studio components that can be used with this launch profile.
        :param studio_id: The unique identifier for a studio resource. In Nimble Studio , all other resources are contained in a studio resource.
        :param description: A human-readable description of the launch profile.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73431936cbffacfb1263654979458319433048ccdba564211a0c846e43353e93)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnLaunchProfileProps(
            ec2_subnet_ids=ec2_subnet_ids,
            launch_profile_protocol_versions=launch_profile_protocol_versions,
            name=name,
            stream_configuration=stream_configuration,
            studio_component_ids=studio_component_ids,
            studio_id=studio_id,
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
            type_hints = typing.get_type_hints(_typecheckingstub__520cd2385901941c1e07bafe0b30dccdcf30981fdd1174c5151396c07cc1b66a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a4b697644b6941637bdcf63cd1dc5040bfc2f102b30b506e95b4f0952bee5c51)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrLaunchProfileId")
    def attr_launch_profile_id(self) -> builtins.str:
        '''The unique identifier for the launch profile resource.

        :cloudformationAttribute: LaunchProfileId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLaunchProfileId"))

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
    @jsii.member(jsii_name="ec2SubnetIds")
    def ec2_subnet_ids(self) -> typing.List[builtins.str]:
        '''Unique identifiers for a collection of EC2 subnets.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "ec2SubnetIds"))

    @ec2_subnet_ids.setter
    def ec2_subnet_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8eab63a068a36016ac93250f9b0a34c6df138ede870e6e7dd6c24f14f8e88e4a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ec2SubnetIds", value)

    @builtins.property
    @jsii.member(jsii_name="launchProfileProtocolVersions")
    def launch_profile_protocol_versions(self) -> typing.List[builtins.str]:
        '''The version number of the protocol that is used by the launch profile.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "launchProfileProtocolVersions"))

    @launch_profile_protocol_versions.setter
    def launch_profile_protocol_versions(
        self,
        value: typing.List[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__244782d1faf0571974ba6a1c12750af38ed7612b5c1d97fa7e01b48cc08793ad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "launchProfileProtocolVersions", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''A friendly name for the launch profile.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__549cc7f1cd83b0d6b509f02a91f45eeaec2f37fb1c8b7eb6bb233fed9c2d1241)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="streamConfiguration")
    def stream_configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnLaunchProfile.StreamConfigurationProperty"]:
        '''A configuration for a streaming session.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnLaunchProfile.StreamConfigurationProperty"], jsii.get(self, "streamConfiguration"))

    @stream_configuration.setter
    def stream_configuration(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnLaunchProfile.StreamConfigurationProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d4c944f3608c457b83c69dac5a4b0dd866e36dd1e2861d2eda291179f914ed8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "streamConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="studioComponentIds")
    def studio_component_ids(self) -> typing.List[builtins.str]:
        '''Unique identifiers for a collection of studio components that can be used with this launch profile.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "studioComponentIds"))

    @studio_component_ids.setter
    def studio_component_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b26ebbd02c5570a7f87ceb260d4d0a26bf024848979ffbad2cac045053fdee6f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "studioComponentIds", value)

    @builtins.property
    @jsii.member(jsii_name="studioId")
    def studio_id(self) -> builtins.str:
        '''The unique identifier for a studio resource.'''
        return typing.cast(builtins.str, jsii.get(self, "studioId"))

    @studio_id.setter
    def studio_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d1edb30e700b6e7289aa48d4088a1eb6a71cc6ce4437c1b3f3acc67a5056c5b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "studioId", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A human-readable description of the launch profile.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1daf19be5a17af43fb390f37aac4fbae48bb61c1d3437067e5a69761552656c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a7ed277becd75aaa152fa2cdcf16874239db41e9e5f5cb9cfe9640e984da3ff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_nimblestudio.CfnLaunchProfile.StreamConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "clipboard_mode": "clipboardMode",
            "ec2_instance_types": "ec2InstanceTypes",
            "streaming_image_ids": "streamingImageIds",
            "automatic_termination_mode": "automaticTerminationMode",
            "max_session_length_in_minutes": "maxSessionLengthInMinutes",
            "max_stopped_session_length_in_minutes": "maxStoppedSessionLengthInMinutes",
            "session_backup": "sessionBackup",
            "session_persistence_mode": "sessionPersistenceMode",
            "session_storage": "sessionStorage",
            "volume_configuration": "volumeConfiguration",
        },
    )
    class StreamConfigurationProperty:
        def __init__(
            self,
            *,
            clipboard_mode: builtins.str,
            ec2_instance_types: typing.Sequence[builtins.str],
            streaming_image_ids: typing.Sequence[builtins.str],
            automatic_termination_mode: typing.Optional[builtins.str] = None,
            max_session_length_in_minutes: typing.Optional[jsii.Number] = None,
            max_stopped_session_length_in_minutes: typing.Optional[jsii.Number] = None,
            session_backup: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnLaunchProfile.StreamConfigurationSessionBackupProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            session_persistence_mode: typing.Optional[builtins.str] = None,
            session_storage: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnLaunchProfile.StreamConfigurationSessionStorageProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            volume_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnLaunchProfile.VolumeConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''A configuration for a streaming session.

            :param clipboard_mode: Allows or deactivates the use of the system clipboard to copy and paste between the streaming session and streaming client.
            :param ec2_instance_types: The EC2 instance types that users can select from when launching a streaming session with this launch profile.
            :param streaming_image_ids: The streaming images that users can select from when launching a streaming session with this launch profile.
            :param automatic_termination_mode: 
            :param max_session_length_in_minutes: The length of time, in minutes, that a streaming session can be active before it is stopped or terminated. After this point, Nimble Studio automatically terminates or stops the session. The default length of time is 690 minutes, and the maximum length of time is 30 days. Default: - 690
            :param max_stopped_session_length_in_minutes: Integer that determines if you can start and stop your sessions and how long a session can stay in the ``STOPPED`` state. The default value is 0. The maximum value is 5760. This field is allowed only when ``sessionPersistenceMode`` is ``ACTIVATED`` and ``automaticTerminationMode`` is ``ACTIVATED`` . If the value is set to 0, your sessions can’t be ``STOPPED`` . If you then call ``StopStreamingSession`` , the session fails. If the time that a session stays in the ``READY`` state exceeds the ``maxSessionLengthInMinutes`` value, the session will automatically be terminated (instead of ``STOPPED`` ). If the value is set to a positive number, the session can be stopped. You can call ``StopStreamingSession`` to stop sessions in the ``READY`` state. If the time that a session stays in the ``READY`` state exceeds the ``maxSessionLengthInMinutes`` value, the session will automatically be stopped (instead of terminated). Default: - 0
            :param session_backup: 
            :param session_persistence_mode: 
            :param session_storage: The upload storage for a streaming session.
            :param volume_configuration: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-launchprofile-streamconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_nimblestudio as nimblestudio
                
                stream_configuration_property = nimblestudio.CfnLaunchProfile.StreamConfigurationProperty(
                    clipboard_mode="clipboardMode",
                    ec2_instance_types=["ec2InstanceTypes"],
                    streaming_image_ids=["streamingImageIds"],
                
                    # the properties below are optional
                    automatic_termination_mode="automaticTerminationMode",
                    max_session_length_in_minutes=123,
                    max_stopped_session_length_in_minutes=123,
                    session_backup=nimblestudio.CfnLaunchProfile.StreamConfigurationSessionBackupProperty(
                        max_backups_to_retain=123,
                        mode="mode"
                    ),
                    session_persistence_mode="sessionPersistenceMode",
                    session_storage=nimblestudio.CfnLaunchProfile.StreamConfigurationSessionStorageProperty(
                        mode=["mode"],
                
                        # the properties below are optional
                        root=nimblestudio.CfnLaunchProfile.StreamingSessionStorageRootProperty(
                            linux="linux",
                            windows="windows"
                        )
                    ),
                    volume_configuration=nimblestudio.CfnLaunchProfile.VolumeConfigurationProperty(
                        iops=123,
                        size=123,
                        throughput=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a37dd49325f1b1d692fa7ce1b7127ade8de959831704fc817da9eefdabf229d9)
                check_type(argname="argument clipboard_mode", value=clipboard_mode, expected_type=type_hints["clipboard_mode"])
                check_type(argname="argument ec2_instance_types", value=ec2_instance_types, expected_type=type_hints["ec2_instance_types"])
                check_type(argname="argument streaming_image_ids", value=streaming_image_ids, expected_type=type_hints["streaming_image_ids"])
                check_type(argname="argument automatic_termination_mode", value=automatic_termination_mode, expected_type=type_hints["automatic_termination_mode"])
                check_type(argname="argument max_session_length_in_minutes", value=max_session_length_in_minutes, expected_type=type_hints["max_session_length_in_minutes"])
                check_type(argname="argument max_stopped_session_length_in_minutes", value=max_stopped_session_length_in_minutes, expected_type=type_hints["max_stopped_session_length_in_minutes"])
                check_type(argname="argument session_backup", value=session_backup, expected_type=type_hints["session_backup"])
                check_type(argname="argument session_persistence_mode", value=session_persistence_mode, expected_type=type_hints["session_persistence_mode"])
                check_type(argname="argument session_storage", value=session_storage, expected_type=type_hints["session_storage"])
                check_type(argname="argument volume_configuration", value=volume_configuration, expected_type=type_hints["volume_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "clipboard_mode": clipboard_mode,
                "ec2_instance_types": ec2_instance_types,
                "streaming_image_ids": streaming_image_ids,
            }
            if automatic_termination_mode is not None:
                self._values["automatic_termination_mode"] = automatic_termination_mode
            if max_session_length_in_minutes is not None:
                self._values["max_session_length_in_minutes"] = max_session_length_in_minutes
            if max_stopped_session_length_in_minutes is not None:
                self._values["max_stopped_session_length_in_minutes"] = max_stopped_session_length_in_minutes
            if session_backup is not None:
                self._values["session_backup"] = session_backup
            if session_persistence_mode is not None:
                self._values["session_persistence_mode"] = session_persistence_mode
            if session_storage is not None:
                self._values["session_storage"] = session_storage
            if volume_configuration is not None:
                self._values["volume_configuration"] = volume_configuration

        @builtins.property
        def clipboard_mode(self) -> builtins.str:
            '''Allows or deactivates the use of the system clipboard to copy and paste between the streaming session and streaming client.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-launchprofile-streamconfiguration.html#cfn-nimblestudio-launchprofile-streamconfiguration-clipboardmode
            '''
            result = self._values.get("clipboard_mode")
            assert result is not None, "Required property 'clipboard_mode' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def ec2_instance_types(self) -> typing.List[builtins.str]:
            '''The EC2 instance types that users can select from when launching a streaming session with this launch profile.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-launchprofile-streamconfiguration.html#cfn-nimblestudio-launchprofile-streamconfiguration-ec2instancetypes
            '''
            result = self._values.get("ec2_instance_types")
            assert result is not None, "Required property 'ec2_instance_types' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def streaming_image_ids(self) -> typing.List[builtins.str]:
            '''The streaming images that users can select from when launching a streaming session with this launch profile.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-launchprofile-streamconfiguration.html#cfn-nimblestudio-launchprofile-streamconfiguration-streamingimageids
            '''
            result = self._values.get("streaming_image_ids")
            assert result is not None, "Required property 'streaming_image_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def automatic_termination_mode(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-launchprofile-streamconfiguration.html#cfn-nimblestudio-launchprofile-streamconfiguration-automaticterminationmode
            '''
            result = self._values.get("automatic_termination_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def max_session_length_in_minutes(self) -> typing.Optional[jsii.Number]:
            '''The length of time, in minutes, that a streaming session can be active before it is stopped or terminated.

            After this point, Nimble Studio automatically terminates or stops the session. The default length of time is 690 minutes, and the maximum length of time is 30 days.

            :default: - 690

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-launchprofile-streamconfiguration.html#cfn-nimblestudio-launchprofile-streamconfiguration-maxsessionlengthinminutes
            '''
            result = self._values.get("max_session_length_in_minutes")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def max_stopped_session_length_in_minutes(self) -> typing.Optional[jsii.Number]:
            '''Integer that determines if you can start and stop your sessions and how long a session can stay in the ``STOPPED`` state.

            The default value is 0. The maximum value is 5760.

            This field is allowed only when ``sessionPersistenceMode`` is ``ACTIVATED`` and ``automaticTerminationMode`` is ``ACTIVATED`` .

            If the value is set to 0, your sessions can’t be ``STOPPED`` . If you then call ``StopStreamingSession`` , the session fails. If the time that a session stays in the ``READY`` state exceeds the ``maxSessionLengthInMinutes`` value, the session will automatically be terminated (instead of ``STOPPED`` ).

            If the value is set to a positive number, the session can be stopped. You can call ``StopStreamingSession`` to stop sessions in the ``READY`` state. If the time that a session stays in the ``READY`` state exceeds the ``maxSessionLengthInMinutes`` value, the session will automatically be stopped (instead of terminated).

            :default: - 0

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-launchprofile-streamconfiguration.html#cfn-nimblestudio-launchprofile-streamconfiguration-maxstoppedsessionlengthinminutes
            '''
            result = self._values.get("max_stopped_session_length_in_minutes")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def session_backup(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLaunchProfile.StreamConfigurationSessionBackupProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-launchprofile-streamconfiguration.html#cfn-nimblestudio-launchprofile-streamconfiguration-sessionbackup
            '''
            result = self._values.get("session_backup")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLaunchProfile.StreamConfigurationSessionBackupProperty"]], result)

        @builtins.property
        def session_persistence_mode(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-launchprofile-streamconfiguration.html#cfn-nimblestudio-launchprofile-streamconfiguration-sessionpersistencemode
            '''
            result = self._values.get("session_persistence_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def session_storage(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLaunchProfile.StreamConfigurationSessionStorageProperty"]]:
            '''The upload storage for a streaming session.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-launchprofile-streamconfiguration.html#cfn-nimblestudio-launchprofile-streamconfiguration-sessionstorage
            '''
            result = self._values.get("session_storage")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLaunchProfile.StreamConfigurationSessionStorageProperty"]], result)

        @builtins.property
        def volume_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLaunchProfile.VolumeConfigurationProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-launchprofile-streamconfiguration.html#cfn-nimblestudio-launchprofile-streamconfiguration-volumeconfiguration
            '''
            result = self._values.get("volume_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLaunchProfile.VolumeConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StreamConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_nimblestudio.CfnLaunchProfile.StreamConfigurationSessionBackupProperty",
        jsii_struct_bases=[],
        name_mapping={"max_backups_to_retain": "maxBackupsToRetain", "mode": "mode"},
    )
    class StreamConfigurationSessionBackupProperty:
        def __init__(
            self,
            *,
            max_backups_to_retain: typing.Optional[jsii.Number] = None,
            mode: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param max_backups_to_retain:  Default: - 0
            :param mode: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-launchprofile-streamconfigurationsessionbackup.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_nimblestudio as nimblestudio
                
                stream_configuration_session_backup_property = nimblestudio.CfnLaunchProfile.StreamConfigurationSessionBackupProperty(
                    max_backups_to_retain=123,
                    mode="mode"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__35eeaf35b6b7c2ee9db6ce9cf7e5a534d316270e0d4408c94083618daf7e76e6)
                check_type(argname="argument max_backups_to_retain", value=max_backups_to_retain, expected_type=type_hints["max_backups_to_retain"])
                check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if max_backups_to_retain is not None:
                self._values["max_backups_to_retain"] = max_backups_to_retain
            if mode is not None:
                self._values["mode"] = mode

        @builtins.property
        def max_backups_to_retain(self) -> typing.Optional[jsii.Number]:
            '''
            :default: - 0

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-launchprofile-streamconfigurationsessionbackup.html#cfn-nimblestudio-launchprofile-streamconfigurationsessionbackup-maxbackupstoretain
            '''
            result = self._values.get("max_backups_to_retain")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def mode(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-launchprofile-streamconfigurationsessionbackup.html#cfn-nimblestudio-launchprofile-streamconfigurationsessionbackup-mode
            '''
            result = self._values.get("mode")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StreamConfigurationSessionBackupProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_nimblestudio.CfnLaunchProfile.StreamConfigurationSessionStorageProperty",
        jsii_struct_bases=[],
        name_mapping={"mode": "mode", "root": "root"},
    )
    class StreamConfigurationSessionStorageProperty:
        def __init__(
            self,
            *,
            mode: typing.Sequence[builtins.str],
            root: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnLaunchProfile.StreamingSessionStorageRootProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The configuration for a streaming session’s upload storage.

            :param mode: Allows artists to upload files to their workstations. The only valid option is ``UPLOAD`` .
            :param root: The configuration for the upload storage root of the streaming session.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-launchprofile-streamconfigurationsessionstorage.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_nimblestudio as nimblestudio
                
                stream_configuration_session_storage_property = nimblestudio.CfnLaunchProfile.StreamConfigurationSessionStorageProperty(
                    mode=["mode"],
                
                    # the properties below are optional
                    root=nimblestudio.CfnLaunchProfile.StreamingSessionStorageRootProperty(
                        linux="linux",
                        windows="windows"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ad7a7e42a6c8c153c4a98ea3d0444cf07fa8b818f3f9ce1c57147f269d974fc3)
                check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
                check_type(argname="argument root", value=root, expected_type=type_hints["root"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "mode": mode,
            }
            if root is not None:
                self._values["root"] = root

        @builtins.property
        def mode(self) -> typing.List[builtins.str]:
            '''Allows artists to upload files to their workstations.

            The only valid option is ``UPLOAD`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-launchprofile-streamconfigurationsessionstorage.html#cfn-nimblestudio-launchprofile-streamconfigurationsessionstorage-mode
            '''
            result = self._values.get("mode")
            assert result is not None, "Required property 'mode' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def root(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLaunchProfile.StreamingSessionStorageRootProperty"]]:
            '''The configuration for the upload storage root of the streaming session.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-launchprofile-streamconfigurationsessionstorage.html#cfn-nimblestudio-launchprofile-streamconfigurationsessionstorage-root
            '''
            result = self._values.get("root")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLaunchProfile.StreamingSessionStorageRootProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StreamConfigurationSessionStorageProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_nimblestudio.CfnLaunchProfile.StreamingSessionStorageRootProperty",
        jsii_struct_bases=[],
        name_mapping={"linux": "linux", "windows": "windows"},
    )
    class StreamingSessionStorageRootProperty:
        def __init__(
            self,
            *,
            linux: typing.Optional[builtins.str] = None,
            windows: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The upload storage root location (folder) on streaming workstations where files are uploaded.

            :param linux: The folder path in Linux workstations where files are uploaded.
            :param windows: The folder path in Windows workstations where files are uploaded.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-launchprofile-streamingsessionstorageroot.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_nimblestudio as nimblestudio
                
                streaming_session_storage_root_property = nimblestudio.CfnLaunchProfile.StreamingSessionStorageRootProperty(
                    linux="linux",
                    windows="windows"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__dbef4d124e5ccc904925563702d809634edaf7f07229849540fc27bb89e29512)
                check_type(argname="argument linux", value=linux, expected_type=type_hints["linux"])
                check_type(argname="argument windows", value=windows, expected_type=type_hints["windows"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if linux is not None:
                self._values["linux"] = linux
            if windows is not None:
                self._values["windows"] = windows

        @builtins.property
        def linux(self) -> typing.Optional[builtins.str]:
            '''The folder path in Linux workstations where files are uploaded.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-launchprofile-streamingsessionstorageroot.html#cfn-nimblestudio-launchprofile-streamingsessionstorageroot-linux
            '''
            result = self._values.get("linux")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def windows(self) -> typing.Optional[builtins.str]:
            '''The folder path in Windows workstations where files are uploaded.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-launchprofile-streamingsessionstorageroot.html#cfn-nimblestudio-launchprofile-streamingsessionstorageroot-windows
            '''
            result = self._values.get("windows")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StreamingSessionStorageRootProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_nimblestudio.CfnLaunchProfile.VolumeConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"iops": "iops", "size": "size", "throughput": "throughput"},
    )
    class VolumeConfigurationProperty:
        def __init__(
            self,
            *,
            iops: typing.Optional[jsii.Number] = None,
            size: typing.Optional[jsii.Number] = None,
            throughput: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param iops:  Default: - 3000
            :param size:  The root volume size is measured in GiBs. Default: - 500
            :param throughput:  The throughput is measured in MiB/s. Default: - 125

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-launchprofile-volumeconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_nimblestudio as nimblestudio
                
                volume_configuration_property = nimblestudio.CfnLaunchProfile.VolumeConfigurationProperty(
                    iops=123,
                    size=123,
                    throughput=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2b5a387bc8ff36612169915fabbc675a7dc7b970403a52c9b4bbc3ec072c6615)
                check_type(argname="argument iops", value=iops, expected_type=type_hints["iops"])
                check_type(argname="argument size", value=size, expected_type=type_hints["size"])
                check_type(argname="argument throughput", value=throughput, expected_type=type_hints["throughput"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if iops is not None:
                self._values["iops"] = iops
            if size is not None:
                self._values["size"] = size
            if throughput is not None:
                self._values["throughput"] = throughput

        @builtins.property
        def iops(self) -> typing.Optional[jsii.Number]:
            '''
            :default: - 3000

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-launchprofile-volumeconfiguration.html#cfn-nimblestudio-launchprofile-volumeconfiguration-iops
            '''
            result = self._values.get("iops")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def size(self) -> typing.Optional[jsii.Number]:
            '''
            The root volume
            size is measured in GiBs.

            :default: - 500

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-launchprofile-volumeconfiguration.html#cfn-nimblestudio-launchprofile-volumeconfiguration-size
            '''
            result = self._values.get("size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def throughput(self) -> typing.Optional[jsii.Number]:
            '''
            The throughput is measured in MiB/s.

            :default: - 125

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-launchprofile-volumeconfiguration.html#cfn-nimblestudio-launchprofile-volumeconfiguration-throughput
            '''
            result = self._values.get("throughput")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VolumeConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_nimblestudio.CfnLaunchProfileProps",
    jsii_struct_bases=[],
    name_mapping={
        "ec2_subnet_ids": "ec2SubnetIds",
        "launch_profile_protocol_versions": "launchProfileProtocolVersions",
        "name": "name",
        "stream_configuration": "streamConfiguration",
        "studio_component_ids": "studioComponentIds",
        "studio_id": "studioId",
        "description": "description",
        "tags": "tags",
    },
)
class CfnLaunchProfileProps:
    def __init__(
        self,
        *,
        ec2_subnet_ids: typing.Sequence[builtins.str],
        launch_profile_protocol_versions: typing.Sequence[builtins.str],
        name: builtins.str,
        stream_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnLaunchProfile.StreamConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
        studio_component_ids: typing.Sequence[builtins.str],
        studio_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnLaunchProfile``.

        :param ec2_subnet_ids: Unique identifiers for a collection of EC2 subnets.
        :param launch_profile_protocol_versions: The version number of the protocol that is used by the launch profile. The only valid version is "2021-03-31".
        :param name: A friendly name for the launch profile.
        :param stream_configuration: A configuration for a streaming session.
        :param studio_component_ids: Unique identifiers for a collection of studio components that can be used with this launch profile.
        :param studio_id: The unique identifier for a studio resource. In Nimble Studio , all other resources are contained in a studio resource.
        :param description: A human-readable description of the launch profile.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-launchprofile.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_nimblestudio as nimblestudio
            
            cfn_launch_profile_props = nimblestudio.CfnLaunchProfileProps(
                ec2_subnet_ids=["ec2SubnetIds"],
                launch_profile_protocol_versions=["launchProfileProtocolVersions"],
                name="name",
                stream_configuration=nimblestudio.CfnLaunchProfile.StreamConfigurationProperty(
                    clipboard_mode="clipboardMode",
                    ec2_instance_types=["ec2InstanceTypes"],
                    streaming_image_ids=["streamingImageIds"],
            
                    # the properties below are optional
                    automatic_termination_mode="automaticTerminationMode",
                    max_session_length_in_minutes=123,
                    max_stopped_session_length_in_minutes=123,
                    session_backup=nimblestudio.CfnLaunchProfile.StreamConfigurationSessionBackupProperty(
                        max_backups_to_retain=123,
                        mode="mode"
                    ),
                    session_persistence_mode="sessionPersistenceMode",
                    session_storage=nimblestudio.CfnLaunchProfile.StreamConfigurationSessionStorageProperty(
                        mode=["mode"],
            
                        # the properties below are optional
                        root=nimblestudio.CfnLaunchProfile.StreamingSessionStorageRootProperty(
                            linux="linux",
                            windows="windows"
                        )
                    ),
                    volume_configuration=nimblestudio.CfnLaunchProfile.VolumeConfigurationProperty(
                        iops=123,
                        size=123,
                        throughput=123
                    )
                ),
                studio_component_ids=["studioComponentIds"],
                studio_id="studioId",
            
                # the properties below are optional
                description="description",
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b43819be936b43afea9ec331a5d4d93db811f04b73c74189dfabbb03a021968)
            check_type(argname="argument ec2_subnet_ids", value=ec2_subnet_ids, expected_type=type_hints["ec2_subnet_ids"])
            check_type(argname="argument launch_profile_protocol_versions", value=launch_profile_protocol_versions, expected_type=type_hints["launch_profile_protocol_versions"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument stream_configuration", value=stream_configuration, expected_type=type_hints["stream_configuration"])
            check_type(argname="argument studio_component_ids", value=studio_component_ids, expected_type=type_hints["studio_component_ids"])
            check_type(argname="argument studio_id", value=studio_id, expected_type=type_hints["studio_id"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "ec2_subnet_ids": ec2_subnet_ids,
            "launch_profile_protocol_versions": launch_profile_protocol_versions,
            "name": name,
            "stream_configuration": stream_configuration,
            "studio_component_ids": studio_component_ids,
            "studio_id": studio_id,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def ec2_subnet_ids(self) -> typing.List[builtins.str]:
        '''Unique identifiers for a collection of EC2 subnets.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-launchprofile.html#cfn-nimblestudio-launchprofile-ec2subnetids
        '''
        result = self._values.get("ec2_subnet_ids")
        assert result is not None, "Required property 'ec2_subnet_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def launch_profile_protocol_versions(self) -> typing.List[builtins.str]:
        '''The version number of the protocol that is used by the launch profile.

        The only valid version is "2021-03-31".

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-launchprofile.html#cfn-nimblestudio-launchprofile-launchprofileprotocolversions
        '''
        result = self._values.get("launch_profile_protocol_versions")
        assert result is not None, "Required property 'launch_profile_protocol_versions' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''A friendly name for the launch profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-launchprofile.html#cfn-nimblestudio-launchprofile-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def stream_configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnLaunchProfile.StreamConfigurationProperty]:
        '''A configuration for a streaming session.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-launchprofile.html#cfn-nimblestudio-launchprofile-streamconfiguration
        '''
        result = self._values.get("stream_configuration")
        assert result is not None, "Required property 'stream_configuration' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnLaunchProfile.StreamConfigurationProperty], result)

    @builtins.property
    def studio_component_ids(self) -> typing.List[builtins.str]:
        '''Unique identifiers for a collection of studio components that can be used with this launch profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-launchprofile.html#cfn-nimblestudio-launchprofile-studiocomponentids
        '''
        result = self._values.get("studio_component_ids")
        assert result is not None, "Required property 'studio_component_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def studio_id(self) -> builtins.str:
        '''The unique identifier for a studio resource.

        In Nimble Studio , all other resources are contained in a studio resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-launchprofile.html#cfn-nimblestudio-launchprofile-studioid
        '''
        result = self._values.get("studio_id")
        assert result is not None, "Required property 'studio_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A human-readable description of the launch profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-launchprofile.html#cfn-nimblestudio-launchprofile-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-launchprofile.html#cfn-nimblestudio-launchprofile-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLaunchProfileProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnStreamingImage(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_nimblestudio.CfnStreamingImage",
):
    '''The ``AWS::NimbleStudio::StreamingImage`` resource creates a streaming image in a studio.

    A streaming image defines the operating system and software to be used in an  streaming session.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-streamingimage.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_nimblestudio as nimblestudio
        
        cfn_streaming_image = nimblestudio.CfnStreamingImage(self, "MyCfnStreamingImage",
            ec2_image_id="ec2ImageId",
            name="name",
            studio_id="studioId",
        
            # the properties below are optional
            description="description",
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
        ec2_image_id: builtins.str,
        name: builtins.str,
        studio_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param ec2_image_id: The ID of an EC2 machine image with which to create the streaming image.
        :param name: A friendly name for a streaming image resource.
        :param studio_id: The unique identifier for a studio resource. In Nimble Studio , all other resources are contained in a studio resource.
        :param description: A human-readable description of the streaming image.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71d825f7da9831b1c19a5c5c864573313899a2423aac6b5af05a411a54526743)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnStreamingImageProps(
            ec2_image_id=ec2_image_id,
            name=name,
            studio_id=studio_id,
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
            type_hints = typing.get_type_hints(_typecheckingstub__401199e97fd635eab46a6fe194df913d1300b94756f7fbccce0959a5e942144d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f0c5b299b247b9175cf16c768182404133746cb763acf8fdf6025f9879f1d12b)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrEncryptionConfiguration")
    def attr_encryption_configuration(self) -> _IResolvable_da3f097b:
        '''
        :cloudformationAttribute: EncryptionConfiguration
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrEncryptionConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="attrEncryptionConfigurationKeyArn")
    def attr_encryption_configuration_key_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: EncryptionConfiguration.KeyArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEncryptionConfigurationKeyArn"))

    @builtins.property
    @jsii.member(jsii_name="attrEncryptionConfigurationKeyType")
    def attr_encryption_configuration_key_type(self) -> builtins.str:
        '''
        :cloudformationAttribute: EncryptionConfiguration.KeyType
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEncryptionConfigurationKeyType"))

    @builtins.property
    @jsii.member(jsii_name="attrEulaIds")
    def attr_eula_ids(self) -> typing.List[builtins.str]:
        '''The list of IDs of EULAs that must be accepted before a streaming session can be started using this streaming image.

        :cloudformationAttribute: EulaIds
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrEulaIds"))

    @builtins.property
    @jsii.member(jsii_name="attrOwner")
    def attr_owner(self) -> builtins.str:
        '''The owner of the streaming image, either the studioId that contains the streaming image or 'amazon' for images that are provided by  .

        :cloudformationAttribute: Owner
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrOwner"))

    @builtins.property
    @jsii.member(jsii_name="attrPlatform")
    def attr_platform(self) -> builtins.str:
        '''The platform of the streaming image, either WINDOWS or LINUX.

        :cloudformationAttribute: Platform
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPlatform"))

    @builtins.property
    @jsii.member(jsii_name="attrStreamingImageId")
    def attr_streaming_image_id(self) -> builtins.str:
        '''The unique identifier for the streaming image resource.

        :cloudformationAttribute: StreamingImageId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStreamingImageId"))

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
    @jsii.member(jsii_name="ec2ImageId")
    def ec2_image_id(self) -> builtins.str:
        '''The ID of an EC2 machine image with which to create the streaming image.'''
        return typing.cast(builtins.str, jsii.get(self, "ec2ImageId"))

    @ec2_image_id.setter
    def ec2_image_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e288fe1c9afd779c805cdf86daf8c368566816ac637a20639c48dd52a91e1edf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ec2ImageId", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''A friendly name for a streaming image resource.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f45937e5e70c9f94fdab81bc9a82676c2e4be3245ab692680328a311c28cdf45)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="studioId")
    def studio_id(self) -> builtins.str:
        '''The unique identifier for a studio resource.'''
        return typing.cast(builtins.str, jsii.get(self, "studioId"))

    @studio_id.setter
    def studio_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__457f906bcebf6cadc64c88ad0022be38965d66119e246c12deb74de88404a0aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "studioId", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A human-readable description of the streaming image.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ad786d753c89334f55d3c9f271ffb856894dd8b2ebbe4e82cf60051ba58e881)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca0d63091de8d88c09bdab08615b7f8db92f3b45649c5965ea4473a43b3c4e7d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_nimblestudio.CfnStreamingImage.StreamingImageEncryptionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"key_type": "keyType", "key_arn": "keyArn"},
    )
    class StreamingImageEncryptionConfigurationProperty:
        def __init__(
            self,
            *,
            key_type: builtins.str,
            key_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param key_type: 
            :param key_arn: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-streamingimage-streamingimageencryptionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_nimblestudio as nimblestudio
                
                streaming_image_encryption_configuration_property = nimblestudio.CfnStreamingImage.StreamingImageEncryptionConfigurationProperty(
                    key_type="keyType",
                
                    # the properties below are optional
                    key_arn="keyArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f47af9fbd3a5b2893cc6cec73ff563dc9e73becb5481ed7ca2e1751c634d053d)
                check_type(argname="argument key_type", value=key_type, expected_type=type_hints["key_type"])
                check_type(argname="argument key_arn", value=key_arn, expected_type=type_hints["key_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "key_type": key_type,
            }
            if key_arn is not None:
                self._values["key_arn"] = key_arn

        @builtins.property
        def key_type(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-streamingimage-streamingimageencryptionconfiguration.html#cfn-nimblestudio-streamingimage-streamingimageencryptionconfiguration-keytype
            '''
            result = self._values.get("key_type")
            assert result is not None, "Required property 'key_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def key_arn(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-streamingimage-streamingimageencryptionconfiguration.html#cfn-nimblestudio-streamingimage-streamingimageencryptionconfiguration-keyarn
            '''
            result = self._values.get("key_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StreamingImageEncryptionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_nimblestudio.CfnStreamingImageProps",
    jsii_struct_bases=[],
    name_mapping={
        "ec2_image_id": "ec2ImageId",
        "name": "name",
        "studio_id": "studioId",
        "description": "description",
        "tags": "tags",
    },
)
class CfnStreamingImageProps:
    def __init__(
        self,
        *,
        ec2_image_id: builtins.str,
        name: builtins.str,
        studio_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnStreamingImage``.

        :param ec2_image_id: The ID of an EC2 machine image with which to create the streaming image.
        :param name: A friendly name for a streaming image resource.
        :param studio_id: The unique identifier for a studio resource. In Nimble Studio , all other resources are contained in a studio resource.
        :param description: A human-readable description of the streaming image.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-streamingimage.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_nimblestudio as nimblestudio
            
            cfn_streaming_image_props = nimblestudio.CfnStreamingImageProps(
                ec2_image_id="ec2ImageId",
                name="name",
                studio_id="studioId",
            
                # the properties below are optional
                description="description",
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5639283dde9f5507e33ed3b0cc8e4bb11678e400c6ec36786bc8e646353a366d)
            check_type(argname="argument ec2_image_id", value=ec2_image_id, expected_type=type_hints["ec2_image_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument studio_id", value=studio_id, expected_type=type_hints["studio_id"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "ec2_image_id": ec2_image_id,
            "name": name,
            "studio_id": studio_id,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def ec2_image_id(self) -> builtins.str:
        '''The ID of an EC2 machine image with which to create the streaming image.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-streamingimage.html#cfn-nimblestudio-streamingimage-ec2imageid
        '''
        result = self._values.get("ec2_image_id")
        assert result is not None, "Required property 'ec2_image_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''A friendly name for a streaming image resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-streamingimage.html#cfn-nimblestudio-streamingimage-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def studio_id(self) -> builtins.str:
        '''The unique identifier for a studio resource.

        In Nimble Studio , all other resources are contained in a studio resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-streamingimage.html#cfn-nimblestudio-streamingimage-studioid
        '''
        result = self._values.get("studio_id")
        assert result is not None, "Required property 'studio_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A human-readable description of the streaming image.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-streamingimage.html#cfn-nimblestudio-streamingimage-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-streamingimage.html#cfn-nimblestudio-streamingimage-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnStreamingImageProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnStudio(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_nimblestudio.CfnStudio",
):
    '''The ``AWS::NimbleStudio::Studio`` resource creates a new studio resource. In  , all other resources are contained in a studio.

    When creating a studio, two IAM roles must be provided: the admin role and the user role. These roles are assumed by your users when they log in to the  portal. The user role must have the AmazonNimbleStudio-StudioUser managed policy attached for the portal to function properly. The Admin Role must have the AmazonNimbleStudio-StudioAdmin managed policy attached for the portal to function properly.

    You can optionally specify an AWS Key Management Service key in the StudioEncryptionConfiguration. In Nimble Studio, resource names, descriptions, initialization scripts, and other data you provide are always encrypted at rest using an AWS Key Management Service key. By default, this key is owned by AWS and managed on your behalf. You may provide your own AWS Key Management Service key when calling CreateStudio to encrypt this data using a key that you own and manage. When providing an AWS Key Management Service key during studio creation,  creates AWS Key Management Service grants in your account to provide your studio user and admin roles access to these AWS Key Management Service keys. If you delete this grant, the studio will no longer be accessible to your portal users. If you delete the studio AWS Key Management Service key, your studio will no longer be accessible.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studio.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_nimblestudio as nimblestudio
        
        cfn_studio = nimblestudio.CfnStudio(self, "MyCfnStudio",
            admin_role_arn="adminRoleArn",
            display_name="displayName",
            studio_name="studioName",
            user_role_arn="userRoleArn",
        
            # the properties below are optional
            studio_encryption_configuration=nimblestudio.CfnStudio.StudioEncryptionConfigurationProperty(
                key_type="keyType",
        
                # the properties below are optional
                key_arn="keyArn"
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
        admin_role_arn: builtins.str,
        display_name: builtins.str,
        studio_name: builtins.str,
        user_role_arn: builtins.str,
        studio_encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnStudio.StudioEncryptionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param admin_role_arn: The IAM role that studio admins assume when logging in to the Nimble Studio portal.
        :param display_name: A friendly name for the studio.
        :param studio_name: The name of the studio, as included in the URL when accessing it in the Nimble Studio portal.
        :param user_role_arn: The IAM role that studio users assume when logging in to the Nimble Studio portal.
        :param studio_encryption_configuration: Configuration of the encryption method that is used for the studio.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45420baa577c3a8eb786b8d20404bcbc5573494502885eb1f55a897024f77af2)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnStudioProps(
            admin_role_arn=admin_role_arn,
            display_name=display_name,
            studio_name=studio_name,
            user_role_arn=user_role_arn,
            studio_encryption_configuration=studio_encryption_configuration,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a95feb38c2ffd266287aa8d0e3539b938c3d8fffe708542e910fcb088e43f36e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__da47c57120b2198c73e780d3fa294b1027942e0731f09a0ebe537b607edbc75c)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrHomeRegion")
    def attr_home_region(self) -> builtins.str:
        '''The AWS Region where the studio resource is located.

        For example, ``us-west-2`` .

        :cloudformationAttribute: HomeRegion
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrHomeRegion"))

    @builtins.property
    @jsii.member(jsii_name="attrSsoClientId")
    def attr_sso_client_id(self) -> builtins.str:
        '''The IAM Identity Center application client ID that is used to integrate with IAM Identity Center , which enables IAM Identity Center users to log into the  portal.

        :cloudformationAttribute: SsoClientId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSsoClientId"))

    @builtins.property
    @jsii.member(jsii_name="attrStudioId")
    def attr_studio_id(self) -> builtins.str:
        '''The unique identifier for the studio resource.

        :cloudformationAttribute: StudioId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStudioId"))

    @builtins.property
    @jsii.member(jsii_name="attrStudioUrl")
    def attr_studio_url(self) -> builtins.str:
        '''The unique identifier for the studio resource.

        :cloudformationAttribute: StudioUrl
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStudioUrl"))

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
    @jsii.member(jsii_name="adminRoleArn")
    def admin_role_arn(self) -> builtins.str:
        '''The IAM role that studio admins assume when logging in to the Nimble Studio portal.'''
        return typing.cast(builtins.str, jsii.get(self, "adminRoleArn"))

    @admin_role_arn.setter
    def admin_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3d45ca698b0f9c73a5a815431dab2f63d7a25137f62fa1b04be4ce8b2f86a6b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adminRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        '''A friendly name for the studio.'''
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96b73f6d52ee20a9a22ee68f200107e5e34616b8607c05a9595b8eca6efb6ce6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="studioName")
    def studio_name(self) -> builtins.str:
        '''The name of the studio, as included in the URL when accessing it in the Nimble Studio portal.'''
        return typing.cast(builtins.str, jsii.get(self, "studioName"))

    @studio_name.setter
    def studio_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb1a59455ee690f34b227f1f8fa0736461134072dc0468cb376617813d739cbb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "studioName", value)

    @builtins.property
    @jsii.member(jsii_name="userRoleArn")
    def user_role_arn(self) -> builtins.str:
        '''The IAM role that studio users assume when logging in to the Nimble Studio portal.'''
        return typing.cast(builtins.str, jsii.get(self, "userRoleArn"))

    @user_role_arn.setter
    def user_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2ec224d834b90ef2e15d73b85c5c439aefad3adb2c0991d837a5f73239e44bd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="studioEncryptionConfiguration")
    def studio_encryption_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStudio.StudioEncryptionConfigurationProperty"]]:
        '''Configuration of the encryption method that is used for the studio.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStudio.StudioEncryptionConfigurationProperty"]], jsii.get(self, "studioEncryptionConfiguration"))

    @studio_encryption_configuration.setter
    def studio_encryption_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStudio.StudioEncryptionConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65e345613e83891827335ce5b32806fa57cf7c858954c9518f24f1ad182d23d8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "studioEncryptionConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9aa4bab5b1a32aba59dcf9d389dc561f499db9d284979f550aa02a5217890468)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_nimblestudio.CfnStudio.StudioEncryptionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"key_type": "keyType", "key_arn": "keyArn"},
    )
    class StudioEncryptionConfigurationProperty:
        def __init__(
            self,
            *,
            key_type: builtins.str,
            key_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Configuration of the encryption method that is used for the studio.

            :param key_type: The type of KMS key that is used to encrypt studio data.
            :param key_arn: The ARN for a KMS key that is used to encrypt studio data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studio-studioencryptionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_nimblestudio as nimblestudio
                
                studio_encryption_configuration_property = nimblestudio.CfnStudio.StudioEncryptionConfigurationProperty(
                    key_type="keyType",
                
                    # the properties below are optional
                    key_arn="keyArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f53b3db707074d7a01dfb0371454ff8800dfd75ba14d633662203acd10c08422)
                check_type(argname="argument key_type", value=key_type, expected_type=type_hints["key_type"])
                check_type(argname="argument key_arn", value=key_arn, expected_type=type_hints["key_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "key_type": key_type,
            }
            if key_arn is not None:
                self._values["key_arn"] = key_arn

        @builtins.property
        def key_type(self) -> builtins.str:
            '''The type of KMS key that is used to encrypt studio data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studio-studioencryptionconfiguration.html#cfn-nimblestudio-studio-studioencryptionconfiguration-keytype
            '''
            result = self._values.get("key_type")
            assert result is not None, "Required property 'key_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def key_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN for a KMS key that is used to encrypt studio data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studio-studioencryptionconfiguration.html#cfn-nimblestudio-studio-studioencryptionconfiguration-keyarn
            '''
            result = self._values.get("key_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StudioEncryptionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnStudioComponent(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_nimblestudio.CfnStudioComponent",
):
    '''The ``AWS::NimbleStudio::StudioComponent`` resource represents a network resource that is used by a studio's users and workflows.

    A typical studio contains studio components for the following: a render farm, an Active Directory, a licensing service, and a shared file system.

    Access to a studio component is managed by specifying security groups for the resource, as well as its endpoint.

    A studio component also has a set of initialization scripts, which are returned by ``GetLaunchProfileInitialization`` . These initialization scripts run on streaming sessions when they start. They provide users with flexibility in controlling how studio resources are configured on a streaming session.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studiocomponent.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_nimblestudio as nimblestudio
        
        cfn_studio_component = nimblestudio.CfnStudioComponent(self, "MyCfnStudioComponent",
            name="name",
            studio_id="studioId",
            type="type",
        
            # the properties below are optional
            configuration=nimblestudio.CfnStudioComponent.StudioComponentConfigurationProperty(
                active_directory_configuration=nimblestudio.CfnStudioComponent.ActiveDirectoryConfigurationProperty(
                    computer_attributes=[nimblestudio.CfnStudioComponent.ActiveDirectoryComputerAttributeProperty(
                        name="name",
                        value="value"
                    )],
                    directory_id="directoryId",
                    organizational_unit_distinguished_name="organizationalUnitDistinguishedName"
                ),
                compute_farm_configuration=nimblestudio.CfnStudioComponent.ComputeFarmConfigurationProperty(
                    active_directory_user="activeDirectoryUser",
                    endpoint="endpoint"
                ),
                license_service_configuration=nimblestudio.CfnStudioComponent.LicenseServiceConfigurationProperty(
                    endpoint="endpoint"
                ),
                shared_file_system_configuration=nimblestudio.CfnStudioComponent.SharedFileSystemConfigurationProperty(
                    endpoint="endpoint",
                    file_system_id="fileSystemId",
                    linux_mount_point="linuxMountPoint",
                    share_name="shareName",
                    windows_mount_drive="windowsMountDrive"
                )
            ),
            description="description",
            ec2_security_group_ids=["ec2SecurityGroupIds"],
            initialization_scripts=[nimblestudio.CfnStudioComponent.StudioComponentInitializationScriptProperty(
                launch_profile_protocol_version="launchProfileProtocolVersion",
                platform="platform",
                run_context="runContext",
                script="script"
            )],
            runtime_role_arn="runtimeRoleArn",
            script_parameters=[nimblestudio.CfnStudioComponent.ScriptParameterKeyValueProperty(
                key="key",
                value="value"
            )],
            secure_initialization_role_arn="secureInitializationRoleArn",
            subtype="subtype",
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
        name: builtins.str,
        studio_id: builtins.str,
        type: builtins.str,
        configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnStudioComponent.StudioComponentConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        ec2_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        initialization_scripts: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnStudioComponent.StudioComponentInitializationScriptProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        runtime_role_arn: typing.Optional[builtins.str] = None,
        script_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnStudioComponent.ScriptParameterKeyValueProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        secure_initialization_role_arn: typing.Optional[builtins.str] = None,
        subtype: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: A friendly name for the studio component resource.
        :param studio_id: The unique identifier for a studio resource. In Nimble Studio , all other resources are contained in a studio resource.
        :param type: The type of the studio component.
        :param configuration: The configuration of the studio component, based on component type.
        :param description: A human-readable description for the studio component resource.
        :param ec2_security_group_ids: The EC2 security groups that control access to the studio component.
        :param initialization_scripts: Initialization scripts for studio components.
        :param runtime_role_arn: 
        :param script_parameters: Parameters for the studio component scripts.
        :param secure_initialization_role_arn: 
        :param subtype: The specific subtype of a studio component.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c22fe0082d9b44d07e4ef368d5f042dd2864628399c458b780e181e7bd4c1351)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnStudioComponentProps(
            name=name,
            studio_id=studio_id,
            type=type,
            configuration=configuration,
            description=description,
            ec2_security_group_ids=ec2_security_group_ids,
            initialization_scripts=initialization_scripts,
            runtime_role_arn=runtime_role_arn,
            script_parameters=script_parameters,
            secure_initialization_role_arn=secure_initialization_role_arn,
            subtype=subtype,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f049b7949e547c2737240060a75c0d47daf4ed1153c80c61aef28d8fdfdf8996)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6e532f9647d932e10f936bfa9825f8ee410e52f51f7c149619ca29b5b4efc60c)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrStudioComponentId")
    def attr_studio_component_id(self) -> builtins.str:
        '''The unique identifier for the studio component resource.

        :cloudformationAttribute: StudioComponentId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStudioComponentId"))

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
        '''A friendly name for the studio component resource.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4f4c1afe096cb2f5c4ebd1c617301dfc41ef84987003077915c9f2a38ad2e61)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="studioId")
    def studio_id(self) -> builtins.str:
        '''The unique identifier for a studio resource.'''
        return typing.cast(builtins.str, jsii.get(self, "studioId"))

    @studio_id.setter
    def studio_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d199c64c8bc358279fb06fb2308e8de2838e907d3b3d9ee49b203ec3defe86d1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "studioId", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''The type of the studio component.'''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7516e9fe600c8968b99698223adac50887f80996b31ea7da47891ca3594f82dd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="configuration")
    def configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStudioComponent.StudioComponentConfigurationProperty"]]:
        '''The configuration of the studio component, based on component type.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStudioComponent.StudioComponentConfigurationProperty"]], jsii.get(self, "configuration"))

    @configuration.setter
    def configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStudioComponent.StudioComponentConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34572620ca2af0c513e1e746eb9c110d151b9bfdf8ec84a3e8d9b96f4a029f28)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configuration", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A human-readable description for the studio component resource.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4d435d976922da8bf26ca6560198803fd916e0a3be3e830c4be0919311c8179)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="ec2SecurityGroupIds")
    def ec2_security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The EC2 security groups that control access to the studio component.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "ec2SecurityGroupIds"))

    @ec2_security_group_ids.setter
    def ec2_security_group_ids(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6238eec10b0be6fb62a440a534f079d11883a8e84a6d4745fde07f70f507c406)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ec2SecurityGroupIds", value)

    @builtins.property
    @jsii.member(jsii_name="initializationScripts")
    def initialization_scripts(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnStudioComponent.StudioComponentInitializationScriptProperty"]]]]:
        '''Initialization scripts for studio components.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnStudioComponent.StudioComponentInitializationScriptProperty"]]]], jsii.get(self, "initializationScripts"))

    @initialization_scripts.setter
    def initialization_scripts(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnStudioComponent.StudioComponentInitializationScriptProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__659216de4760e25164d033c057bfa0fdf83af861fc798a0f08b86ff4d3a87b87)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "initializationScripts", value)

    @builtins.property
    @jsii.member(jsii_name="runtimeRoleArn")
    def runtime_role_arn(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "runtimeRoleArn"))

    @runtime_role_arn.setter
    def runtime_role_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b81da422d011c4a82640eb49baceab2f76b57ee93b27f43a10c611ad081a6e03)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "runtimeRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="scriptParameters")
    def script_parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnStudioComponent.ScriptParameterKeyValueProperty"]]]]:
        '''Parameters for the studio component scripts.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnStudioComponent.ScriptParameterKeyValueProperty"]]]], jsii.get(self, "scriptParameters"))

    @script_parameters.setter
    def script_parameters(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnStudioComponent.ScriptParameterKeyValueProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d03432e7064ac8ade176413120d4effe4df12f3c4c0ea0d5812102bd65db908)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scriptParameters", value)

    @builtins.property
    @jsii.member(jsii_name="secureInitializationRoleArn")
    def secure_initialization_role_arn(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secureInitializationRoleArn"))

    @secure_initialization_role_arn.setter
    def secure_initialization_role_arn(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed299be512003df10a0838a8f90e93c49ae8d9bf5993557d1fa9f773a302abc0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secureInitializationRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="subtype")
    def subtype(self) -> typing.Optional[builtins.str]:
        '''The specific subtype of a studio component.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subtype"))

    @subtype.setter
    def subtype(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83a7858d87ccc1b3698f54725ddcb72b48818d28bf2b6cf8b26640011e6028cd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subtype", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ec5b0a0223c7b24add9fca9d6614f1e0b4446ec4b4e800ac16d2ce120598396)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_nimblestudio.CfnStudioComponent.ActiveDirectoryComputerAttributeProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "value": "value"},
    )
    class ActiveDirectoryComputerAttributeProperty:
        def __init__(
            self,
            *,
            name: typing.Optional[builtins.str] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''An LDAP attribute of an Active Directory computer account, in the form of a name:value pair.

            :param name: The name for the LDAP attribute.
            :param value: The value for the LDAP attribute.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-activedirectorycomputerattribute.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_nimblestudio as nimblestudio
                
                active_directory_computer_attribute_property = nimblestudio.CfnStudioComponent.ActiveDirectoryComputerAttributeProperty(
                    name="name",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ec1aaef806df5703c5f025d35103a05e255a829199c9ea9ce1341d14abc7c9c3)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if name is not None:
                self._values["name"] = name
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name for the LDAP attribute.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-activedirectorycomputerattribute.html#cfn-nimblestudio-studiocomponent-activedirectorycomputerattribute-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''The value for the LDAP attribute.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-activedirectorycomputerattribute.html#cfn-nimblestudio-studiocomponent-activedirectorycomputerattribute-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ActiveDirectoryComputerAttributeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_nimblestudio.CfnStudioComponent.ActiveDirectoryConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "computer_attributes": "computerAttributes",
            "directory_id": "directoryId",
            "organizational_unit_distinguished_name": "organizationalUnitDistinguishedName",
        },
    )
    class ActiveDirectoryConfigurationProperty:
        def __init__(
            self,
            *,
            computer_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnStudioComponent.ActiveDirectoryComputerAttributeProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            directory_id: typing.Optional[builtins.str] = None,
            organizational_unit_distinguished_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The configuration for a AWS Directory Service for Microsoft Active Directory studio resource.

            :param computer_attributes: A collection of custom attributes for an Active Directory computer.
            :param directory_id: The directory ID of the AWS Directory Service for Microsoft Active Directory to access using this studio component.
            :param organizational_unit_distinguished_name: The distinguished name (DN) and organizational unit (OU) of an Active Directory computer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-activedirectoryconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_nimblestudio as nimblestudio
                
                active_directory_configuration_property = nimblestudio.CfnStudioComponent.ActiveDirectoryConfigurationProperty(
                    computer_attributes=[nimblestudio.CfnStudioComponent.ActiveDirectoryComputerAttributeProperty(
                        name="name",
                        value="value"
                    )],
                    directory_id="directoryId",
                    organizational_unit_distinguished_name="organizationalUnitDistinguishedName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cf520f76dfeb11fc4be8388e582d9b3637d9c0a88480f18777f5ec3ac9d4a1cd)
                check_type(argname="argument computer_attributes", value=computer_attributes, expected_type=type_hints["computer_attributes"])
                check_type(argname="argument directory_id", value=directory_id, expected_type=type_hints["directory_id"])
                check_type(argname="argument organizational_unit_distinguished_name", value=organizational_unit_distinguished_name, expected_type=type_hints["organizational_unit_distinguished_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if computer_attributes is not None:
                self._values["computer_attributes"] = computer_attributes
            if directory_id is not None:
                self._values["directory_id"] = directory_id
            if organizational_unit_distinguished_name is not None:
                self._values["organizational_unit_distinguished_name"] = organizational_unit_distinguished_name

        @builtins.property
        def computer_attributes(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnStudioComponent.ActiveDirectoryComputerAttributeProperty"]]]]:
            '''A collection of custom attributes for an Active Directory computer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-activedirectoryconfiguration.html#cfn-nimblestudio-studiocomponent-activedirectoryconfiguration-computerattributes
            '''
            result = self._values.get("computer_attributes")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnStudioComponent.ActiveDirectoryComputerAttributeProperty"]]]], result)

        @builtins.property
        def directory_id(self) -> typing.Optional[builtins.str]:
            '''The directory ID of the AWS Directory Service for Microsoft Active Directory to access using this studio component.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-activedirectoryconfiguration.html#cfn-nimblestudio-studiocomponent-activedirectoryconfiguration-directoryid
            '''
            result = self._values.get("directory_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def organizational_unit_distinguished_name(
            self,
        ) -> typing.Optional[builtins.str]:
            '''The distinguished name (DN) and organizational unit (OU) of an Active Directory computer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-activedirectoryconfiguration.html#cfn-nimblestudio-studiocomponent-activedirectoryconfiguration-organizationalunitdistinguishedname
            '''
            result = self._values.get("organizational_unit_distinguished_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ActiveDirectoryConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_nimblestudio.CfnStudioComponent.ComputeFarmConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "active_directory_user": "activeDirectoryUser",
            "endpoint": "endpoint",
        },
    )
    class ComputeFarmConfigurationProperty:
        def __init__(
            self,
            *,
            active_directory_user: typing.Optional[builtins.str] = None,
            endpoint: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The configuration for a render farm that is associated with a studio resource.

            :param active_directory_user: The name of an Active Directory user that is used on ComputeFarm worker instances.
            :param endpoint: The endpoint of the ComputeFarm that is accessed by the studio component resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-computefarmconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_nimblestudio as nimblestudio
                
                compute_farm_configuration_property = nimblestudio.CfnStudioComponent.ComputeFarmConfigurationProperty(
                    active_directory_user="activeDirectoryUser",
                    endpoint="endpoint"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__491f85d55bdecd3f05c710ad770b18aecaa5058e3ca815a3e8b49744098fe6d1)
                check_type(argname="argument active_directory_user", value=active_directory_user, expected_type=type_hints["active_directory_user"])
                check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if active_directory_user is not None:
                self._values["active_directory_user"] = active_directory_user
            if endpoint is not None:
                self._values["endpoint"] = endpoint

        @builtins.property
        def active_directory_user(self) -> typing.Optional[builtins.str]:
            '''The name of an Active Directory user that is used on ComputeFarm worker instances.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-computefarmconfiguration.html#cfn-nimblestudio-studiocomponent-computefarmconfiguration-activedirectoryuser
            '''
            result = self._values.get("active_directory_user")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def endpoint(self) -> typing.Optional[builtins.str]:
            '''The endpoint of the ComputeFarm that is accessed by the studio component resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-computefarmconfiguration.html#cfn-nimblestudio-studiocomponent-computefarmconfiguration-endpoint
            '''
            result = self._values.get("endpoint")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ComputeFarmConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_nimblestudio.CfnStudioComponent.LicenseServiceConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"endpoint": "endpoint"},
    )
    class LicenseServiceConfigurationProperty:
        def __init__(self, *, endpoint: typing.Optional[builtins.str] = None) -> None:
            '''The configuration for a license service that is associated with a studio resource.

            :param endpoint: The endpoint of the license service that is accessed by the studio component resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-licenseserviceconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_nimblestudio as nimblestudio
                
                license_service_configuration_property = nimblestudio.CfnStudioComponent.LicenseServiceConfigurationProperty(
                    endpoint="endpoint"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4663624ef288c2192b672ec1d0dadaad5734426a570ae1e8c211701185b3b2be)
                check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if endpoint is not None:
                self._values["endpoint"] = endpoint

        @builtins.property
        def endpoint(self) -> typing.Optional[builtins.str]:
            '''The endpoint of the license service that is accessed by the studio component resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-licenseserviceconfiguration.html#cfn-nimblestudio-studiocomponent-licenseserviceconfiguration-endpoint
            '''
            result = self._values.get("endpoint")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LicenseServiceConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_nimblestudio.CfnStudioComponent.ScriptParameterKeyValueProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class ScriptParameterKeyValueProperty:
        def __init__(
            self,
            *,
            key: typing.Optional[builtins.str] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A parameter for a studio component script, in the form of a key-value pair.

            :param key: A script parameter key.
            :param value: A script parameter value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-scriptparameterkeyvalue.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_nimblestudio as nimblestudio
                
                script_parameter_key_value_property = nimblestudio.CfnStudioComponent.ScriptParameterKeyValueProperty(
                    key="key",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b9e48ce368437101b8e71543180ff6f23509e1faf033d58da2be44a346c448fb)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if key is not None:
                self._values["key"] = key
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def key(self) -> typing.Optional[builtins.str]:
            '''A script parameter key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-scriptparameterkeyvalue.html#cfn-nimblestudio-studiocomponent-scriptparameterkeyvalue-key
            '''
            result = self._values.get("key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''A script parameter value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-scriptparameterkeyvalue.html#cfn-nimblestudio-studiocomponent-scriptparameterkeyvalue-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScriptParameterKeyValueProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_nimblestudio.CfnStudioComponent.SharedFileSystemConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "endpoint": "endpoint",
            "file_system_id": "fileSystemId",
            "linux_mount_point": "linuxMountPoint",
            "share_name": "shareName",
            "windows_mount_drive": "windowsMountDrive",
        },
    )
    class SharedFileSystemConfigurationProperty:
        def __init__(
            self,
            *,
            endpoint: typing.Optional[builtins.str] = None,
            file_system_id: typing.Optional[builtins.str] = None,
            linux_mount_point: typing.Optional[builtins.str] = None,
            share_name: typing.Optional[builtins.str] = None,
            windows_mount_drive: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The configuration for a shared file storage system that is associated with a studio resource.

            :param endpoint: The endpoint of the shared file system that is accessed by the studio component resource.
            :param file_system_id: The unique identifier for a file system.
            :param linux_mount_point: The mount location for a shared file system on a Linux virtual workstation.
            :param share_name: The name of the file share.
            :param windows_mount_drive: The mount location for a shared file system on a Windows virtual workstation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-sharedfilesystemconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_nimblestudio as nimblestudio
                
                shared_file_system_configuration_property = nimblestudio.CfnStudioComponent.SharedFileSystemConfigurationProperty(
                    endpoint="endpoint",
                    file_system_id="fileSystemId",
                    linux_mount_point="linuxMountPoint",
                    share_name="shareName",
                    windows_mount_drive="windowsMountDrive"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__beca9538aeae04fbce9fcadf9ddcba87da3b58665047ce413b7d7d2a5d118f67)
                check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
                check_type(argname="argument file_system_id", value=file_system_id, expected_type=type_hints["file_system_id"])
                check_type(argname="argument linux_mount_point", value=linux_mount_point, expected_type=type_hints["linux_mount_point"])
                check_type(argname="argument share_name", value=share_name, expected_type=type_hints["share_name"])
                check_type(argname="argument windows_mount_drive", value=windows_mount_drive, expected_type=type_hints["windows_mount_drive"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if endpoint is not None:
                self._values["endpoint"] = endpoint
            if file_system_id is not None:
                self._values["file_system_id"] = file_system_id
            if linux_mount_point is not None:
                self._values["linux_mount_point"] = linux_mount_point
            if share_name is not None:
                self._values["share_name"] = share_name
            if windows_mount_drive is not None:
                self._values["windows_mount_drive"] = windows_mount_drive

        @builtins.property
        def endpoint(self) -> typing.Optional[builtins.str]:
            '''The endpoint of the shared file system that is accessed by the studio component resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-sharedfilesystemconfiguration.html#cfn-nimblestudio-studiocomponent-sharedfilesystemconfiguration-endpoint
            '''
            result = self._values.get("endpoint")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def file_system_id(self) -> typing.Optional[builtins.str]:
            '''The unique identifier for a file system.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-sharedfilesystemconfiguration.html#cfn-nimblestudio-studiocomponent-sharedfilesystemconfiguration-filesystemid
            '''
            result = self._values.get("file_system_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def linux_mount_point(self) -> typing.Optional[builtins.str]:
            '''The mount location for a shared file system on a Linux virtual workstation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-sharedfilesystemconfiguration.html#cfn-nimblestudio-studiocomponent-sharedfilesystemconfiguration-linuxmountpoint
            '''
            result = self._values.get("linux_mount_point")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def share_name(self) -> typing.Optional[builtins.str]:
            '''The name of the file share.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-sharedfilesystemconfiguration.html#cfn-nimblestudio-studiocomponent-sharedfilesystemconfiguration-sharename
            '''
            result = self._values.get("share_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def windows_mount_drive(self) -> typing.Optional[builtins.str]:
            '''The mount location for a shared file system on a Windows virtual workstation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-sharedfilesystemconfiguration.html#cfn-nimblestudio-studiocomponent-sharedfilesystemconfiguration-windowsmountdrive
            '''
            result = self._values.get("windows_mount_drive")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SharedFileSystemConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_nimblestudio.CfnStudioComponent.StudioComponentConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "active_directory_configuration": "activeDirectoryConfiguration",
            "compute_farm_configuration": "computeFarmConfiguration",
            "license_service_configuration": "licenseServiceConfiguration",
            "shared_file_system_configuration": "sharedFileSystemConfiguration",
        },
    )
    class StudioComponentConfigurationProperty:
        def __init__(
            self,
            *,
            active_directory_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnStudioComponent.ActiveDirectoryConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            compute_farm_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnStudioComponent.ComputeFarmConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            license_service_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnStudioComponent.LicenseServiceConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            shared_file_system_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnStudioComponent.SharedFileSystemConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The configuration of the studio component, based on component type.

            :param active_directory_configuration: The configuration for a AWS Directory Service for Microsoft Active Directory studio resource.
            :param compute_farm_configuration: The configuration for a render farm that is associated with a studio resource.
            :param license_service_configuration: The configuration for a license service that is associated with a studio resource.
            :param shared_file_system_configuration: The configuration for a shared file storage system that is associated with a studio resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-studiocomponentconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_nimblestudio as nimblestudio
                
                studio_component_configuration_property = nimblestudio.CfnStudioComponent.StudioComponentConfigurationProperty(
                    active_directory_configuration=nimblestudio.CfnStudioComponent.ActiveDirectoryConfigurationProperty(
                        computer_attributes=[nimblestudio.CfnStudioComponent.ActiveDirectoryComputerAttributeProperty(
                            name="name",
                            value="value"
                        )],
                        directory_id="directoryId",
                        organizational_unit_distinguished_name="organizationalUnitDistinguishedName"
                    ),
                    compute_farm_configuration=nimblestudio.CfnStudioComponent.ComputeFarmConfigurationProperty(
                        active_directory_user="activeDirectoryUser",
                        endpoint="endpoint"
                    ),
                    license_service_configuration=nimblestudio.CfnStudioComponent.LicenseServiceConfigurationProperty(
                        endpoint="endpoint"
                    ),
                    shared_file_system_configuration=nimblestudio.CfnStudioComponent.SharedFileSystemConfigurationProperty(
                        endpoint="endpoint",
                        file_system_id="fileSystemId",
                        linux_mount_point="linuxMountPoint",
                        share_name="shareName",
                        windows_mount_drive="windowsMountDrive"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1d3ca279ff5b8ba3141eff89ae77e118d04ed28e85c1bf22486b3014d95103b6)
                check_type(argname="argument active_directory_configuration", value=active_directory_configuration, expected_type=type_hints["active_directory_configuration"])
                check_type(argname="argument compute_farm_configuration", value=compute_farm_configuration, expected_type=type_hints["compute_farm_configuration"])
                check_type(argname="argument license_service_configuration", value=license_service_configuration, expected_type=type_hints["license_service_configuration"])
                check_type(argname="argument shared_file_system_configuration", value=shared_file_system_configuration, expected_type=type_hints["shared_file_system_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if active_directory_configuration is not None:
                self._values["active_directory_configuration"] = active_directory_configuration
            if compute_farm_configuration is not None:
                self._values["compute_farm_configuration"] = compute_farm_configuration
            if license_service_configuration is not None:
                self._values["license_service_configuration"] = license_service_configuration
            if shared_file_system_configuration is not None:
                self._values["shared_file_system_configuration"] = shared_file_system_configuration

        @builtins.property
        def active_directory_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStudioComponent.ActiveDirectoryConfigurationProperty"]]:
            '''The configuration for a AWS Directory Service for Microsoft Active Directory studio resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-studiocomponentconfiguration.html#cfn-nimblestudio-studiocomponent-studiocomponentconfiguration-activedirectoryconfiguration
            '''
            result = self._values.get("active_directory_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStudioComponent.ActiveDirectoryConfigurationProperty"]], result)

        @builtins.property
        def compute_farm_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStudioComponent.ComputeFarmConfigurationProperty"]]:
            '''The configuration for a render farm that is associated with a studio resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-studiocomponentconfiguration.html#cfn-nimblestudio-studiocomponent-studiocomponentconfiguration-computefarmconfiguration
            '''
            result = self._values.get("compute_farm_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStudioComponent.ComputeFarmConfigurationProperty"]], result)

        @builtins.property
        def license_service_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStudioComponent.LicenseServiceConfigurationProperty"]]:
            '''The configuration for a license service that is associated with a studio resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-studiocomponentconfiguration.html#cfn-nimblestudio-studiocomponent-studiocomponentconfiguration-licenseserviceconfiguration
            '''
            result = self._values.get("license_service_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStudioComponent.LicenseServiceConfigurationProperty"]], result)

        @builtins.property
        def shared_file_system_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStudioComponent.SharedFileSystemConfigurationProperty"]]:
            '''The configuration for a shared file storage system that is associated with a studio resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-studiocomponentconfiguration.html#cfn-nimblestudio-studiocomponent-studiocomponentconfiguration-sharedfilesystemconfiguration
            '''
            result = self._values.get("shared_file_system_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStudioComponent.SharedFileSystemConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StudioComponentConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_nimblestudio.CfnStudioComponent.StudioComponentInitializationScriptProperty",
        jsii_struct_bases=[],
        name_mapping={
            "launch_profile_protocol_version": "launchProfileProtocolVersion",
            "platform": "platform",
            "run_context": "runContext",
            "script": "script",
        },
    )
    class StudioComponentInitializationScriptProperty:
        def __init__(
            self,
            *,
            launch_profile_protocol_version: typing.Optional[builtins.str] = None,
            platform: typing.Optional[builtins.str] = None,
            run_context: typing.Optional[builtins.str] = None,
            script: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Initialization scripts for studio components.

            :param launch_profile_protocol_version: The version number of the protocol that is used by the launch profile. The only valid version is "2021-03-31".
            :param platform: The platform of the initialization script, either Windows or Linux.
            :param run_context: The method to use when running the initialization script.
            :param script: The initialization script.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-studiocomponentinitializationscript.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_nimblestudio as nimblestudio
                
                studio_component_initialization_script_property = nimblestudio.CfnStudioComponent.StudioComponentInitializationScriptProperty(
                    launch_profile_protocol_version="launchProfileProtocolVersion",
                    platform="platform",
                    run_context="runContext",
                    script="script"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__81ae21ca54c86cd8aaeb2004583ec16f187a029ddafc8eeb7ab83f4afe67b39c)
                check_type(argname="argument launch_profile_protocol_version", value=launch_profile_protocol_version, expected_type=type_hints["launch_profile_protocol_version"])
                check_type(argname="argument platform", value=platform, expected_type=type_hints["platform"])
                check_type(argname="argument run_context", value=run_context, expected_type=type_hints["run_context"])
                check_type(argname="argument script", value=script, expected_type=type_hints["script"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if launch_profile_protocol_version is not None:
                self._values["launch_profile_protocol_version"] = launch_profile_protocol_version
            if platform is not None:
                self._values["platform"] = platform
            if run_context is not None:
                self._values["run_context"] = run_context
            if script is not None:
                self._values["script"] = script

        @builtins.property
        def launch_profile_protocol_version(self) -> typing.Optional[builtins.str]:
            '''The version number of the protocol that is used by the launch profile.

            The only valid version is "2021-03-31".

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-studiocomponentinitializationscript.html#cfn-nimblestudio-studiocomponent-studiocomponentinitializationscript-launchprofileprotocolversion
            '''
            result = self._values.get("launch_profile_protocol_version")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def platform(self) -> typing.Optional[builtins.str]:
            '''The platform of the initialization script, either Windows or Linux.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-studiocomponentinitializationscript.html#cfn-nimblestudio-studiocomponent-studiocomponentinitializationscript-platform
            '''
            result = self._values.get("platform")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def run_context(self) -> typing.Optional[builtins.str]:
            '''The method to use when running the initialization script.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-studiocomponentinitializationscript.html#cfn-nimblestudio-studiocomponent-studiocomponentinitializationscript-runcontext
            '''
            result = self._values.get("run_context")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def script(self) -> typing.Optional[builtins.str]:
            '''The initialization script.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-nimblestudio-studiocomponent-studiocomponentinitializationscript.html#cfn-nimblestudio-studiocomponent-studiocomponentinitializationscript-script
            '''
            result = self._values.get("script")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StudioComponentInitializationScriptProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_nimblestudio.CfnStudioComponentProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "studio_id": "studioId",
        "type": "type",
        "configuration": "configuration",
        "description": "description",
        "ec2_security_group_ids": "ec2SecurityGroupIds",
        "initialization_scripts": "initializationScripts",
        "runtime_role_arn": "runtimeRoleArn",
        "script_parameters": "scriptParameters",
        "secure_initialization_role_arn": "secureInitializationRoleArn",
        "subtype": "subtype",
        "tags": "tags",
    },
)
class CfnStudioComponentProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        studio_id: builtins.str,
        type: builtins.str,
        configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStudioComponent.StudioComponentConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        ec2_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        initialization_scripts: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStudioComponent.StudioComponentInitializationScriptProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        runtime_role_arn: typing.Optional[builtins.str] = None,
        script_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStudioComponent.ScriptParameterKeyValueProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        secure_initialization_role_arn: typing.Optional[builtins.str] = None,
        subtype: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnStudioComponent``.

        :param name: A friendly name for the studio component resource.
        :param studio_id: The unique identifier for a studio resource. In Nimble Studio , all other resources are contained in a studio resource.
        :param type: The type of the studio component.
        :param configuration: The configuration of the studio component, based on component type.
        :param description: A human-readable description for the studio component resource.
        :param ec2_security_group_ids: The EC2 security groups that control access to the studio component.
        :param initialization_scripts: Initialization scripts for studio components.
        :param runtime_role_arn: 
        :param script_parameters: Parameters for the studio component scripts.
        :param secure_initialization_role_arn: 
        :param subtype: The specific subtype of a studio component.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studiocomponent.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_nimblestudio as nimblestudio
            
            cfn_studio_component_props = nimblestudio.CfnStudioComponentProps(
                name="name",
                studio_id="studioId",
                type="type",
            
                # the properties below are optional
                configuration=nimblestudio.CfnStudioComponent.StudioComponentConfigurationProperty(
                    active_directory_configuration=nimblestudio.CfnStudioComponent.ActiveDirectoryConfigurationProperty(
                        computer_attributes=[nimblestudio.CfnStudioComponent.ActiveDirectoryComputerAttributeProperty(
                            name="name",
                            value="value"
                        )],
                        directory_id="directoryId",
                        organizational_unit_distinguished_name="organizationalUnitDistinguishedName"
                    ),
                    compute_farm_configuration=nimblestudio.CfnStudioComponent.ComputeFarmConfigurationProperty(
                        active_directory_user="activeDirectoryUser",
                        endpoint="endpoint"
                    ),
                    license_service_configuration=nimblestudio.CfnStudioComponent.LicenseServiceConfigurationProperty(
                        endpoint="endpoint"
                    ),
                    shared_file_system_configuration=nimblestudio.CfnStudioComponent.SharedFileSystemConfigurationProperty(
                        endpoint="endpoint",
                        file_system_id="fileSystemId",
                        linux_mount_point="linuxMountPoint",
                        share_name="shareName",
                        windows_mount_drive="windowsMountDrive"
                    )
                ),
                description="description",
                ec2_security_group_ids=["ec2SecurityGroupIds"],
                initialization_scripts=[nimblestudio.CfnStudioComponent.StudioComponentInitializationScriptProperty(
                    launch_profile_protocol_version="launchProfileProtocolVersion",
                    platform="platform",
                    run_context="runContext",
                    script="script"
                )],
                runtime_role_arn="runtimeRoleArn",
                script_parameters=[nimblestudio.CfnStudioComponent.ScriptParameterKeyValueProperty(
                    key="key",
                    value="value"
                )],
                secure_initialization_role_arn="secureInitializationRoleArn",
                subtype="subtype",
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__452974fbd84550efbe28df9f5e4cb6049d1527391e07a1544107fc2f0186e7dc)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument studio_id", value=studio_id, expected_type=type_hints["studio_id"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument configuration", value=configuration, expected_type=type_hints["configuration"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument ec2_security_group_ids", value=ec2_security_group_ids, expected_type=type_hints["ec2_security_group_ids"])
            check_type(argname="argument initialization_scripts", value=initialization_scripts, expected_type=type_hints["initialization_scripts"])
            check_type(argname="argument runtime_role_arn", value=runtime_role_arn, expected_type=type_hints["runtime_role_arn"])
            check_type(argname="argument script_parameters", value=script_parameters, expected_type=type_hints["script_parameters"])
            check_type(argname="argument secure_initialization_role_arn", value=secure_initialization_role_arn, expected_type=type_hints["secure_initialization_role_arn"])
            check_type(argname="argument subtype", value=subtype, expected_type=type_hints["subtype"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "studio_id": studio_id,
            "type": type,
        }
        if configuration is not None:
            self._values["configuration"] = configuration
        if description is not None:
            self._values["description"] = description
        if ec2_security_group_ids is not None:
            self._values["ec2_security_group_ids"] = ec2_security_group_ids
        if initialization_scripts is not None:
            self._values["initialization_scripts"] = initialization_scripts
        if runtime_role_arn is not None:
            self._values["runtime_role_arn"] = runtime_role_arn
        if script_parameters is not None:
            self._values["script_parameters"] = script_parameters
        if secure_initialization_role_arn is not None:
            self._values["secure_initialization_role_arn"] = secure_initialization_role_arn
        if subtype is not None:
            self._values["subtype"] = subtype
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''A friendly name for the studio component resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studiocomponent.html#cfn-nimblestudio-studiocomponent-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def studio_id(self) -> builtins.str:
        '''The unique identifier for a studio resource.

        In Nimble Studio , all other resources are contained in a studio resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studiocomponent.html#cfn-nimblestudio-studiocomponent-studioid
        '''
        result = self._values.get("studio_id")
        assert result is not None, "Required property 'studio_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The type of the studio component.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studiocomponent.html#cfn-nimblestudio-studiocomponent-type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStudioComponent.StudioComponentConfigurationProperty]]:
        '''The configuration of the studio component, based on component type.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studiocomponent.html#cfn-nimblestudio-studiocomponent-configuration
        '''
        result = self._values.get("configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStudioComponent.StudioComponentConfigurationProperty]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A human-readable description for the studio component resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studiocomponent.html#cfn-nimblestudio-studiocomponent-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ec2_security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The EC2 security groups that control access to the studio component.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studiocomponent.html#cfn-nimblestudio-studiocomponent-ec2securitygroupids
        '''
        result = self._values.get("ec2_security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def initialization_scripts(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnStudioComponent.StudioComponentInitializationScriptProperty]]]]:
        '''Initialization scripts for studio components.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studiocomponent.html#cfn-nimblestudio-studiocomponent-initializationscripts
        '''
        result = self._values.get("initialization_scripts")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnStudioComponent.StudioComponentInitializationScriptProperty]]]], result)

    @builtins.property
    def runtime_role_arn(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studiocomponent.html#cfn-nimblestudio-studiocomponent-runtimerolearn
        '''
        result = self._values.get("runtime_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def script_parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnStudioComponent.ScriptParameterKeyValueProperty]]]]:
        '''Parameters for the studio component scripts.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studiocomponent.html#cfn-nimblestudio-studiocomponent-scriptparameters
        '''
        result = self._values.get("script_parameters")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnStudioComponent.ScriptParameterKeyValueProperty]]]], result)

    @builtins.property
    def secure_initialization_role_arn(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studiocomponent.html#cfn-nimblestudio-studiocomponent-secureinitializationrolearn
        '''
        result = self._values.get("secure_initialization_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subtype(self) -> typing.Optional[builtins.str]:
        '''The specific subtype of a studio component.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studiocomponent.html#cfn-nimblestudio-studiocomponent-subtype
        '''
        result = self._values.get("subtype")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studiocomponent.html#cfn-nimblestudio-studiocomponent-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnStudioComponentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_nimblestudio.CfnStudioProps",
    jsii_struct_bases=[],
    name_mapping={
        "admin_role_arn": "adminRoleArn",
        "display_name": "displayName",
        "studio_name": "studioName",
        "user_role_arn": "userRoleArn",
        "studio_encryption_configuration": "studioEncryptionConfiguration",
        "tags": "tags",
    },
)
class CfnStudioProps:
    def __init__(
        self,
        *,
        admin_role_arn: builtins.str,
        display_name: builtins.str,
        studio_name: builtins.str,
        user_role_arn: builtins.str,
        studio_encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStudio.StudioEncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnStudio``.

        :param admin_role_arn: The IAM role that studio admins assume when logging in to the Nimble Studio portal.
        :param display_name: A friendly name for the studio.
        :param studio_name: The name of the studio, as included in the URL when accessing it in the Nimble Studio portal.
        :param user_role_arn: The IAM role that studio users assume when logging in to the Nimble Studio portal.
        :param studio_encryption_configuration: Configuration of the encryption method that is used for the studio.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studio.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_nimblestudio as nimblestudio
            
            cfn_studio_props = nimblestudio.CfnStudioProps(
                admin_role_arn="adminRoleArn",
                display_name="displayName",
                studio_name="studioName",
                user_role_arn="userRoleArn",
            
                # the properties below are optional
                studio_encryption_configuration=nimblestudio.CfnStudio.StudioEncryptionConfigurationProperty(
                    key_type="keyType",
            
                    # the properties below are optional
                    key_arn="keyArn"
                ),
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__adecf8657a6c6a9dbaea94911b353618ab8a0000478c99ec27d8a488e0e2469e)
            check_type(argname="argument admin_role_arn", value=admin_role_arn, expected_type=type_hints["admin_role_arn"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument studio_name", value=studio_name, expected_type=type_hints["studio_name"])
            check_type(argname="argument user_role_arn", value=user_role_arn, expected_type=type_hints["user_role_arn"])
            check_type(argname="argument studio_encryption_configuration", value=studio_encryption_configuration, expected_type=type_hints["studio_encryption_configuration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "admin_role_arn": admin_role_arn,
            "display_name": display_name,
            "studio_name": studio_name,
            "user_role_arn": user_role_arn,
        }
        if studio_encryption_configuration is not None:
            self._values["studio_encryption_configuration"] = studio_encryption_configuration
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def admin_role_arn(self) -> builtins.str:
        '''The IAM role that studio admins assume when logging in to the Nimble Studio portal.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studio.html#cfn-nimblestudio-studio-adminrolearn
        '''
        result = self._values.get("admin_role_arn")
        assert result is not None, "Required property 'admin_role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def display_name(self) -> builtins.str:
        '''A friendly name for the studio.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studio.html#cfn-nimblestudio-studio-displayname
        '''
        result = self._values.get("display_name")
        assert result is not None, "Required property 'display_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def studio_name(self) -> builtins.str:
        '''The name of the studio, as included in the URL when accessing it in the Nimble Studio portal.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studio.html#cfn-nimblestudio-studio-studioname
        '''
        result = self._values.get("studio_name")
        assert result is not None, "Required property 'studio_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_role_arn(self) -> builtins.str:
        '''The IAM role that studio users assume when logging in to the Nimble Studio portal.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studio.html#cfn-nimblestudio-studio-userrolearn
        '''
        result = self._values.get("user_role_arn")
        assert result is not None, "Required property 'user_role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def studio_encryption_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStudio.StudioEncryptionConfigurationProperty]]:
        '''Configuration of the encryption method that is used for the studio.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studio.html#cfn-nimblestudio-studio-studioencryptionconfiguration
        '''
        result = self._values.get("studio_encryption_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStudio.StudioEncryptionConfigurationProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-nimblestudio-studio.html#cfn-nimblestudio-studio-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnStudioProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnLaunchProfile",
    "CfnLaunchProfileProps",
    "CfnStreamingImage",
    "CfnStreamingImageProps",
    "CfnStudio",
    "CfnStudioComponent",
    "CfnStudioComponentProps",
    "CfnStudioProps",
]

publication.publish()

def _typecheckingstub__73431936cbffacfb1263654979458319433048ccdba564211a0c846e43353e93(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    ec2_subnet_ids: typing.Sequence[builtins.str],
    launch_profile_protocol_versions: typing.Sequence[builtins.str],
    name: builtins.str,
    stream_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnLaunchProfile.StreamConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    studio_component_ids: typing.Sequence[builtins.str],
    studio_id: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__520cd2385901941c1e07bafe0b30dccdcf30981fdd1174c5151396c07cc1b66a(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4b697644b6941637bdcf63cd1dc5040bfc2f102b30b506e95b4f0952bee5c51(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8eab63a068a36016ac93250f9b0a34c6df138ede870e6e7dd6c24f14f8e88e4a(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__244782d1faf0571974ba6a1c12750af38ed7612b5c1d97fa7e01b48cc08793ad(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__549cc7f1cd83b0d6b509f02a91f45eeaec2f37fb1c8b7eb6bb233fed9c2d1241(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d4c944f3608c457b83c69dac5a4b0dd866e36dd1e2861d2eda291179f914ed8(
    value: typing.Union[_IResolvable_da3f097b, CfnLaunchProfile.StreamConfigurationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b26ebbd02c5570a7f87ceb260d4d0a26bf024848979ffbad2cac045053fdee6f(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d1edb30e700b6e7289aa48d4088a1eb6a71cc6ce4437c1b3f3acc67a5056c5b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1daf19be5a17af43fb390f37aac4fbae48bb61c1d3437067e5a69761552656c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a7ed277becd75aaa152fa2cdcf16874239db41e9e5f5cb9cfe9640e984da3ff(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a37dd49325f1b1d692fa7ce1b7127ade8de959831704fc817da9eefdabf229d9(
    *,
    clipboard_mode: builtins.str,
    ec2_instance_types: typing.Sequence[builtins.str],
    streaming_image_ids: typing.Sequence[builtins.str],
    automatic_termination_mode: typing.Optional[builtins.str] = None,
    max_session_length_in_minutes: typing.Optional[jsii.Number] = None,
    max_stopped_session_length_in_minutes: typing.Optional[jsii.Number] = None,
    session_backup: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLaunchProfile.StreamConfigurationSessionBackupProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    session_persistence_mode: typing.Optional[builtins.str] = None,
    session_storage: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLaunchProfile.StreamConfigurationSessionStorageProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    volume_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLaunchProfile.VolumeConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35eeaf35b6b7c2ee9db6ce9cf7e5a534d316270e0d4408c94083618daf7e76e6(
    *,
    max_backups_to_retain: typing.Optional[jsii.Number] = None,
    mode: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad7a7e42a6c8c153c4a98ea3d0444cf07fa8b818f3f9ce1c57147f269d974fc3(
    *,
    mode: typing.Sequence[builtins.str],
    root: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLaunchProfile.StreamingSessionStorageRootProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dbef4d124e5ccc904925563702d809634edaf7f07229849540fc27bb89e29512(
    *,
    linux: typing.Optional[builtins.str] = None,
    windows: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b5a387bc8ff36612169915fabbc675a7dc7b970403a52c9b4bbc3ec072c6615(
    *,
    iops: typing.Optional[jsii.Number] = None,
    size: typing.Optional[jsii.Number] = None,
    throughput: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b43819be936b43afea9ec331a5d4d93db811f04b73c74189dfabbb03a021968(
    *,
    ec2_subnet_ids: typing.Sequence[builtins.str],
    launch_profile_protocol_versions: typing.Sequence[builtins.str],
    name: builtins.str,
    stream_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnLaunchProfile.StreamConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    studio_component_ids: typing.Sequence[builtins.str],
    studio_id: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71d825f7da9831b1c19a5c5c864573313899a2423aac6b5af05a411a54526743(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    ec2_image_id: builtins.str,
    name: builtins.str,
    studio_id: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__401199e97fd635eab46a6fe194df913d1300b94756f7fbccce0959a5e942144d(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0c5b299b247b9175cf16c768182404133746cb763acf8fdf6025f9879f1d12b(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e288fe1c9afd779c805cdf86daf8c368566816ac637a20639c48dd52a91e1edf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f45937e5e70c9f94fdab81bc9a82676c2e4be3245ab692680328a311c28cdf45(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__457f906bcebf6cadc64c88ad0022be38965d66119e246c12deb74de88404a0aa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ad786d753c89334f55d3c9f271ffb856894dd8b2ebbe4e82cf60051ba58e881(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca0d63091de8d88c09bdab08615b7f8db92f3b45649c5965ea4473a43b3c4e7d(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f47af9fbd3a5b2893cc6cec73ff563dc9e73becb5481ed7ca2e1751c634d053d(
    *,
    key_type: builtins.str,
    key_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5639283dde9f5507e33ed3b0cc8e4bb11678e400c6ec36786bc8e646353a366d(
    *,
    ec2_image_id: builtins.str,
    name: builtins.str,
    studio_id: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45420baa577c3a8eb786b8d20404bcbc5573494502885eb1f55a897024f77af2(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    admin_role_arn: builtins.str,
    display_name: builtins.str,
    studio_name: builtins.str,
    user_role_arn: builtins.str,
    studio_encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStudio.StudioEncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a95feb38c2ffd266287aa8d0e3539b938c3d8fffe708542e910fcb088e43f36e(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da47c57120b2198c73e780d3fa294b1027942e0731f09a0ebe537b607edbc75c(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3d45ca698b0f9c73a5a815431dab2f63d7a25137f62fa1b04be4ce8b2f86a6b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96b73f6d52ee20a9a22ee68f200107e5e34616b8607c05a9595b8eca6efb6ce6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb1a59455ee690f34b227f1f8fa0736461134072dc0468cb376617813d739cbb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2ec224d834b90ef2e15d73b85c5c439aefad3adb2c0991d837a5f73239e44bd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65e345613e83891827335ce5b32806fa57cf7c858954c9518f24f1ad182d23d8(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStudio.StudioEncryptionConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9aa4bab5b1a32aba59dcf9d389dc561f499db9d284979f550aa02a5217890468(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f53b3db707074d7a01dfb0371454ff8800dfd75ba14d633662203acd10c08422(
    *,
    key_type: builtins.str,
    key_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c22fe0082d9b44d07e4ef368d5f042dd2864628399c458b780e181e7bd4c1351(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    studio_id: builtins.str,
    type: builtins.str,
    configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStudioComponent.StudioComponentConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    ec2_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    initialization_scripts: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStudioComponent.StudioComponentInitializationScriptProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    runtime_role_arn: typing.Optional[builtins.str] = None,
    script_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStudioComponent.ScriptParameterKeyValueProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    secure_initialization_role_arn: typing.Optional[builtins.str] = None,
    subtype: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f049b7949e547c2737240060a75c0d47daf4ed1153c80c61aef28d8fdfdf8996(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e532f9647d932e10f936bfa9825f8ee410e52f51f7c149619ca29b5b4efc60c(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4f4c1afe096cb2f5c4ebd1c617301dfc41ef84987003077915c9f2a38ad2e61(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d199c64c8bc358279fb06fb2308e8de2838e907d3b3d9ee49b203ec3defe86d1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7516e9fe600c8968b99698223adac50887f80996b31ea7da47891ca3594f82dd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34572620ca2af0c513e1e746eb9c110d151b9bfdf8ec84a3e8d9b96f4a029f28(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStudioComponent.StudioComponentConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4d435d976922da8bf26ca6560198803fd916e0a3be3e830c4be0919311c8179(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6238eec10b0be6fb62a440a534f079d11883a8e84a6d4745fde07f70f507c406(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__659216de4760e25164d033c057bfa0fdf83af861fc798a0f08b86ff4d3a87b87(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnStudioComponent.StudioComponentInitializationScriptProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b81da422d011c4a82640eb49baceab2f76b57ee93b27f43a10c611ad081a6e03(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d03432e7064ac8ade176413120d4effe4df12f3c4c0ea0d5812102bd65db908(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnStudioComponent.ScriptParameterKeyValueProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed299be512003df10a0838a8f90e93c49ae8d9bf5993557d1fa9f773a302abc0(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83a7858d87ccc1b3698f54725ddcb72b48818d28bf2b6cf8b26640011e6028cd(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ec5b0a0223c7b24add9fca9d6614f1e0b4446ec4b4e800ac16d2ce120598396(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec1aaef806df5703c5f025d35103a05e255a829199c9ea9ce1341d14abc7c9c3(
    *,
    name: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf520f76dfeb11fc4be8388e582d9b3637d9c0a88480f18777f5ec3ac9d4a1cd(
    *,
    computer_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStudioComponent.ActiveDirectoryComputerAttributeProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    directory_id: typing.Optional[builtins.str] = None,
    organizational_unit_distinguished_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__491f85d55bdecd3f05c710ad770b18aecaa5058e3ca815a3e8b49744098fe6d1(
    *,
    active_directory_user: typing.Optional[builtins.str] = None,
    endpoint: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4663624ef288c2192b672ec1d0dadaad5734426a570ae1e8c211701185b3b2be(
    *,
    endpoint: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9e48ce368437101b8e71543180ff6f23509e1faf033d58da2be44a346c448fb(
    *,
    key: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__beca9538aeae04fbce9fcadf9ddcba87da3b58665047ce413b7d7d2a5d118f67(
    *,
    endpoint: typing.Optional[builtins.str] = None,
    file_system_id: typing.Optional[builtins.str] = None,
    linux_mount_point: typing.Optional[builtins.str] = None,
    share_name: typing.Optional[builtins.str] = None,
    windows_mount_drive: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d3ca279ff5b8ba3141eff89ae77e118d04ed28e85c1bf22486b3014d95103b6(
    *,
    active_directory_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStudioComponent.ActiveDirectoryConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    compute_farm_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStudioComponent.ComputeFarmConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    license_service_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStudioComponent.LicenseServiceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    shared_file_system_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStudioComponent.SharedFileSystemConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81ae21ca54c86cd8aaeb2004583ec16f187a029ddafc8eeb7ab83f4afe67b39c(
    *,
    launch_profile_protocol_version: typing.Optional[builtins.str] = None,
    platform: typing.Optional[builtins.str] = None,
    run_context: typing.Optional[builtins.str] = None,
    script: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__452974fbd84550efbe28df9f5e4cb6049d1527391e07a1544107fc2f0186e7dc(
    *,
    name: builtins.str,
    studio_id: builtins.str,
    type: builtins.str,
    configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStudioComponent.StudioComponentConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    ec2_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    initialization_scripts: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStudioComponent.StudioComponentInitializationScriptProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    runtime_role_arn: typing.Optional[builtins.str] = None,
    script_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStudioComponent.ScriptParameterKeyValueProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    secure_initialization_role_arn: typing.Optional[builtins.str] = None,
    subtype: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__adecf8657a6c6a9dbaea94911b353618ab8a0000478c99ec27d8a488e0e2469e(
    *,
    admin_role_arn: builtins.str,
    display_name: builtins.str,
    studio_name: builtins.str,
    user_role_arn: builtins.str,
    studio_encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStudio.StudioEncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass
