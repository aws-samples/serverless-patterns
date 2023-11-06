'''
# AWS::IVS Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_ivs as ivs
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for IVS construct libraries](https://constructs.dev/search?q=ivs)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::IVS resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_IVS.html) directly.

> An experimental construct library for this service is available in preview. Since it is not stable yet, it is distributed
> as a separate package so that you can pin its version independently of the rest of the CDK. See the package:
>
> <span class="package-reference">@aws-cdk/aws-ivs-alpha</span>

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::IVS](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_IVS.html).

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
class CfnChannel(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ivs.CfnChannel",
):
    '''The ``AWS::IVS::Channel`` resource specifies an  channel.

    A channel stores configuration information related to your live stream. For more information, see `CreateChannel <https://docs.aws.amazon.com/ivs/latest/APIReference/API_CreateChannel.html>`_ in the *Amazon Interactive Video Service API Reference* .
    .. epigraph::

       By default, the IVS API CreateChannel endpoint creates a stream key in addition to a channel. The  Channel resource *does not* create a stream key; to create a stream key, use the StreamKey resource instead.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-channel.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ivs as ivs
        
        cfn_channel = ivs.CfnChannel(self, "MyCfnChannel",
            authorized=False,
            insecure_ingest=False,
            latency_mode="latencyMode",
            name="name",
            preset="preset",
            recording_configuration_arn="recordingConfigurationArn",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            type="type"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        authorized: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        insecure_ingest: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        latency_mode: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        preset: typing.Optional[builtins.str] = None,
        recording_configuration_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param authorized: Whether the channel is authorized. *Default* : ``false`` Default: - false
        :param insecure_ingest: Whether the channel allows insecure RTMP ingest. *Default* : ``false`` Default: - false
        :param latency_mode: Channel latency mode. Valid values:. - ``NORMAL`` : Use NORMAL to broadcast and deliver live video up to Full HD. - ``LOW`` : Use LOW for near real-time interactions with viewers. .. epigraph:: In the console, ``LOW`` and ``NORMAL`` correspond to ``Ultra-low`` and ``Standard`` , respectively. *Default* : ``LOW`` Default: - "LOW"
        :param name: Channel name. Default: - "-"
        :param preset: An optional transcode preset for the channel. This is selectable only for ``ADVANCED_HD`` and ``ADVANCED_SD`` channel types. For those channel types, the default preset is ``HIGHER_BANDWIDTH_DELIVERY`` . For other channel types ( ``BASIC`` and ``STANDARD`` ), ``preset`` is the empty string ("").
        :param recording_configuration_arn: The ARN of a RecordingConfiguration resource. An empty string indicates that recording is disabled for the channel. A RecordingConfiguration ARN indicates that recording is enabled using the specified recording configuration. See the `RecordingConfiguration <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-recordingconfiguration.html>`_ resource for more information and an example. *Default* : "" (empty string, recording is disabled) Default: - ""
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        :param type: The channel type, which determines the allowable resolution and bitrate. *If you exceed the allowable resolution or bitrate, the stream probably will disconnect immediately.* Valid values: - ``STANDARD`` : Video is transcoded: multiple qualities are generated from the original input to automatically give viewers the best experience for their devices and network conditions. Transcoding allows higher playback quality across a range of download speeds. Resolution can be up to 1080p and bitrate can be up to 8.5 Mbps. Audio is transcoded only for renditions 360p and below; above that, audio is passed through. - ``BASIC`` : Video is transmuxed: Amazon IVS delivers the original input to viewers. The viewer’s video-quality choice is limited to the original input. Resolution can be up to 1080p and bitrate can be up to 1.5 Mbps for 480p and up to 3.5 Mbps for resolutions between 480p and 1080p. - ``ADVANCED_SD`` : Video is transcoded; multiple qualities are generated from the original input, to automatically give viewers the best experience for their devices and network conditions. Input resolution can be up to 1080p and bitrate can be up to 8.5 Mbps; output is capped at SD quality (480p). You can select an optional transcode preset (see below). Audio for all renditions is transcoded, and an audio-only rendition is available. - ``ADVANCED_HD`` : Video is transcoded; multiple qualities are generated from the original input, to automatically give viewers the best experience for their devices and network conditions. Input resolution can be up to 1080p and bitrate can be up to 8.5 Mbps; output is capped at HD quality (720p). You can select an optional transcode preset (see below). Audio for all renditions is transcoded, and an audio-only rendition is available. Optional *transcode presets* (available for the ``ADVANCED`` types) allow you to trade off available download bandwidth and video quality, to optimize the viewing experience. There are two presets: - *Constrained bandwidth delivery* uses a lower bitrate for each quality level. Use it if you have low download bandwidth and/or simple video content (e.g., talking heads) - *Higher bandwidth delivery* uses a higher bitrate for each quality level. Use it if you have high download bandwidth and/or complex video content (e.g., flashes and quick scene changes). *Default* : ``STANDARD`` Default: - "STANDARD"
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__998485c6924ca07e096c10b7976e238a36e5cfb75264ee66a67de472363369d6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnChannelProps(
            authorized=authorized,
            insecure_ingest=insecure_ingest,
            latency_mode=latency_mode,
            name=name,
            preset=preset,
            recording_configuration_arn=recording_configuration_arn,
            tags=tags,
            type=type,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b2f270a2cc06d7958dc82935ff792ce64817de7fc16c4f4b5a7afa6f76cdd80)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0fa81ac5355ae77db888dc8d0fb4cbbff54f381372b1c5a191ceb5eb77a6442b)
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
        '''The channel ARN.

        For example: ``arn:aws:ivs:us-west-2:123456789012:channel/abcdABCDefgh``

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrIngestEndpoint")
    def attr_ingest_endpoint(self) -> builtins.str:
        '''Channel ingest endpoint, part of the definition of an ingest server, used when you set up streaming software.

        For example: ``a1b2c3d4e5f6.global-contribute.live-video.net``

        :cloudformationAttribute: IngestEndpoint
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIngestEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="attrPlaybackUrl")
    def attr_playback_url(self) -> builtins.str:
        '''Channel playback URL.

        For example: ``https://a1b2c3d4e5f6.us-west-2.playback.live-video.net/api/video/v1/us-west-2.123456789012.channel.abcdEFGH.m3u8``

        :cloudformationAttribute: PlaybackUrl
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPlaybackUrl"))

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
    @jsii.member(jsii_name="authorized")
    def authorized(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Whether the channel is authorized.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "authorized"))

    @authorized.setter
    def authorized(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e83b3a70b60de37a8aabc9c019b31db83c549e80f9c9c88a5b74fde72ecb20e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authorized", value)

    @builtins.property
    @jsii.member(jsii_name="insecureIngest")
    def insecure_ingest(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Whether the channel allows insecure RTMP ingest.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "insecureIngest"))

    @insecure_ingest.setter
    def insecure_ingest(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__734c5e1f9cdeabe74fb1ade992399b475d1594cbcdfd026823e8984eaa2d4eab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "insecureIngest", value)

    @builtins.property
    @jsii.member(jsii_name="latencyMode")
    def latency_mode(self) -> typing.Optional[builtins.str]:
        '''Channel latency mode.

        Valid values:.
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "latencyMode"))

    @latency_mode.setter
    def latency_mode(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd2cfeff050510b655ecd39d0e3b95c3c9e2af649e77e0903ad721d0f6428ab5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "latencyMode", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''Channel name.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15776afbbb29227b4807e807447939235926366be32ef5acc331c74f0acd9b41)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="preset")
    def preset(self) -> typing.Optional[builtins.str]:
        '''An optional transcode preset for the channel.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "preset"))

    @preset.setter
    def preset(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95e047ef543e7e26080292a0481b6ce40457143e76918ac4c1c2d13855ce22ee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preset", value)

    @builtins.property
    @jsii.member(jsii_name="recordingConfigurationArn")
    def recording_configuration_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of a RecordingConfiguration resource.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "recordingConfigurationArn"))

    @recording_configuration_arn.setter
    def recording_configuration_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0eb4132c8e5e803f734f8f894d72d2324ee00be84b0babafa7076d94d732c960)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recordingConfigurationArn", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da42cce1a703989106b1844fef6f10d0a57f43c733d171564b16f83c208e7196)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> typing.Optional[builtins.str]:
        '''The channel type, which determines the allowable resolution and bitrate.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "type"))

    @type.setter
    def type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0be9a3a6192cfd130520f4e6ecd8c9091b1a8b4312f716182989ea3feb88dc8b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ivs.CfnChannelProps",
    jsii_struct_bases=[],
    name_mapping={
        "authorized": "authorized",
        "insecure_ingest": "insecureIngest",
        "latency_mode": "latencyMode",
        "name": "name",
        "preset": "preset",
        "recording_configuration_arn": "recordingConfigurationArn",
        "tags": "tags",
        "type": "type",
    },
)
class CfnChannelProps:
    def __init__(
        self,
        *,
        authorized: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        insecure_ingest: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        latency_mode: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        preset: typing.Optional[builtins.str] = None,
        recording_configuration_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnChannel``.

        :param authorized: Whether the channel is authorized. *Default* : ``false`` Default: - false
        :param insecure_ingest: Whether the channel allows insecure RTMP ingest. *Default* : ``false`` Default: - false
        :param latency_mode: Channel latency mode. Valid values:. - ``NORMAL`` : Use NORMAL to broadcast and deliver live video up to Full HD. - ``LOW`` : Use LOW for near real-time interactions with viewers. .. epigraph:: In the console, ``LOW`` and ``NORMAL`` correspond to ``Ultra-low`` and ``Standard`` , respectively. *Default* : ``LOW`` Default: - "LOW"
        :param name: Channel name. Default: - "-"
        :param preset: An optional transcode preset for the channel. This is selectable only for ``ADVANCED_HD`` and ``ADVANCED_SD`` channel types. For those channel types, the default preset is ``HIGHER_BANDWIDTH_DELIVERY`` . For other channel types ( ``BASIC`` and ``STANDARD`` ), ``preset`` is the empty string ("").
        :param recording_configuration_arn: The ARN of a RecordingConfiguration resource. An empty string indicates that recording is disabled for the channel. A RecordingConfiguration ARN indicates that recording is enabled using the specified recording configuration. See the `RecordingConfiguration <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-recordingconfiguration.html>`_ resource for more information and an example. *Default* : "" (empty string, recording is disabled) Default: - ""
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        :param type: The channel type, which determines the allowable resolution and bitrate. *If you exceed the allowable resolution or bitrate, the stream probably will disconnect immediately.* Valid values: - ``STANDARD`` : Video is transcoded: multiple qualities are generated from the original input to automatically give viewers the best experience for their devices and network conditions. Transcoding allows higher playback quality across a range of download speeds. Resolution can be up to 1080p and bitrate can be up to 8.5 Mbps. Audio is transcoded only for renditions 360p and below; above that, audio is passed through. - ``BASIC`` : Video is transmuxed: Amazon IVS delivers the original input to viewers. The viewer’s video-quality choice is limited to the original input. Resolution can be up to 1080p and bitrate can be up to 1.5 Mbps for 480p and up to 3.5 Mbps for resolutions between 480p and 1080p. - ``ADVANCED_SD`` : Video is transcoded; multiple qualities are generated from the original input, to automatically give viewers the best experience for their devices and network conditions. Input resolution can be up to 1080p and bitrate can be up to 8.5 Mbps; output is capped at SD quality (480p). You can select an optional transcode preset (see below). Audio for all renditions is transcoded, and an audio-only rendition is available. - ``ADVANCED_HD`` : Video is transcoded; multiple qualities are generated from the original input, to automatically give viewers the best experience for their devices and network conditions. Input resolution can be up to 1080p and bitrate can be up to 8.5 Mbps; output is capped at HD quality (720p). You can select an optional transcode preset (see below). Audio for all renditions is transcoded, and an audio-only rendition is available. Optional *transcode presets* (available for the ``ADVANCED`` types) allow you to trade off available download bandwidth and video quality, to optimize the viewing experience. There are two presets: - *Constrained bandwidth delivery* uses a lower bitrate for each quality level. Use it if you have low download bandwidth and/or simple video content (e.g., talking heads) - *Higher bandwidth delivery* uses a higher bitrate for each quality level. Use it if you have high download bandwidth and/or complex video content (e.g., flashes and quick scene changes). *Default* : ``STANDARD`` Default: - "STANDARD"

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-channel.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ivs as ivs
            
            cfn_channel_props = ivs.CfnChannelProps(
                authorized=False,
                insecure_ingest=False,
                latency_mode="latencyMode",
                name="name",
                preset="preset",
                recording_configuration_arn="recordingConfigurationArn",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                type="type"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61646017dba4df4ec5b97fde61911670aebc6b8151847b927754a4e9c110979d)
            check_type(argname="argument authorized", value=authorized, expected_type=type_hints["authorized"])
            check_type(argname="argument insecure_ingest", value=insecure_ingest, expected_type=type_hints["insecure_ingest"])
            check_type(argname="argument latency_mode", value=latency_mode, expected_type=type_hints["latency_mode"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument preset", value=preset, expected_type=type_hints["preset"])
            check_type(argname="argument recording_configuration_arn", value=recording_configuration_arn, expected_type=type_hints["recording_configuration_arn"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if authorized is not None:
            self._values["authorized"] = authorized
        if insecure_ingest is not None:
            self._values["insecure_ingest"] = insecure_ingest
        if latency_mode is not None:
            self._values["latency_mode"] = latency_mode
        if name is not None:
            self._values["name"] = name
        if preset is not None:
            self._values["preset"] = preset
        if recording_configuration_arn is not None:
            self._values["recording_configuration_arn"] = recording_configuration_arn
        if tags is not None:
            self._values["tags"] = tags
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def authorized(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Whether the channel is authorized.

        *Default* : ``false``

        :default: - false

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-channel.html#cfn-ivs-channel-authorized
        '''
        result = self._values.get("authorized")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def insecure_ingest(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Whether the channel allows insecure RTMP ingest.

        *Default* : ``false``

        :default: - false

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-channel.html#cfn-ivs-channel-insecureingest
        '''
        result = self._values.get("insecure_ingest")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def latency_mode(self) -> typing.Optional[builtins.str]:
        '''Channel latency mode. Valid values:.

        - ``NORMAL`` : Use NORMAL to broadcast and deliver live video up to Full HD.
        - ``LOW`` : Use LOW for near real-time interactions with viewers.

        .. epigraph::

           In the  console, ``LOW`` and ``NORMAL`` correspond to ``Ultra-low`` and ``Standard`` , respectively.

        *Default* : ``LOW``

        :default: - "LOW"

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-channel.html#cfn-ivs-channel-latencymode
        '''
        result = self._values.get("latency_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Channel name.

        :default: - "-"

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-channel.html#cfn-ivs-channel-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def preset(self) -> typing.Optional[builtins.str]:
        '''An optional transcode preset for the channel.

        This is selectable only for ``ADVANCED_HD`` and ``ADVANCED_SD`` channel types. For those channel types, the default preset is ``HIGHER_BANDWIDTH_DELIVERY`` . For other channel types ( ``BASIC`` and ``STANDARD`` ), ``preset`` is the empty string ("").

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-channel.html#cfn-ivs-channel-preset
        '''
        result = self._values.get("preset")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def recording_configuration_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of a RecordingConfiguration resource.

        An empty string indicates that recording is disabled for the channel. A RecordingConfiguration ARN indicates that recording is enabled using the specified recording configuration. See the `RecordingConfiguration <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-recordingconfiguration.html>`_ resource for more information and an example.

        *Default* : "" (empty string, recording is disabled)

        :default: - ""

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-channel.html#cfn-ivs-channel-recordingconfigurationarn
        '''
        result = self._values.get("recording_configuration_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-channel.html#cfn-ivs-channel-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''The channel type, which determines the allowable resolution and bitrate.

        *If you exceed the allowable resolution or bitrate, the stream probably will disconnect immediately.* Valid values:

        - ``STANDARD`` : Video is transcoded: multiple qualities are generated from the original input to automatically give viewers the best experience for their devices and network conditions. Transcoding allows higher playback quality across a range of download speeds. Resolution can be up to 1080p and bitrate can be up to 8.5 Mbps. Audio is transcoded only for renditions 360p and below; above that, audio is passed through.
        - ``BASIC`` : Video is transmuxed: Amazon IVS delivers the original input to viewers. The viewer’s video-quality choice is limited to the original input. Resolution can be up to 1080p and bitrate can be up to 1.5 Mbps for 480p and up to 3.5 Mbps for resolutions between 480p and 1080p.
        - ``ADVANCED_SD`` : Video is transcoded; multiple qualities are generated from the original input, to automatically give viewers the best experience for their devices and network conditions. Input resolution can be up to 1080p and bitrate can be up to 8.5 Mbps; output is capped at SD quality (480p). You can select an optional transcode preset (see below). Audio for all renditions is transcoded, and an audio-only rendition is available.
        - ``ADVANCED_HD`` : Video is transcoded; multiple qualities are generated from the original input, to automatically give viewers the best experience for their devices and network conditions. Input resolution can be up to 1080p and bitrate can be up to 8.5 Mbps; output is capped at HD quality (720p). You can select an optional transcode preset (see below). Audio for all renditions is transcoded, and an audio-only rendition is available.

        Optional *transcode presets* (available for the ``ADVANCED`` types) allow you to trade off available download bandwidth and video quality, to optimize the viewing experience. There are two presets:

        - *Constrained bandwidth delivery* uses a lower bitrate for each quality level. Use it if you have low download bandwidth and/or simple video content (e.g., talking heads)
        - *Higher bandwidth delivery* uses a higher bitrate for each quality level. Use it if you have high download bandwidth and/or complex video content (e.g., flashes and quick scene changes).

        *Default* : ``STANDARD``

        :default: - "STANDARD"

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-channel.html#cfn-ivs-channel-type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnChannelProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnPlaybackKeyPair(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ivs.CfnPlaybackKeyPair",
):
    '''The ``AWS::IVS::PlaybackKeyPair`` resource specifies an  playback key pair.

    uses a public playback key to validate playback tokens that have been signed with the corresponding private key. For more information, see `Setting Up Private Channels <https://docs.aws.amazon.com/ivs/latest/userguide/private-channels.html>`_ in the *Amazon Interactive Video Service User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-playbackkeypair.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ivs as ivs
        
        cfn_playback_key_pair = ivs.CfnPlaybackKeyPair(self, "MyCfnPlaybackKeyPair",
            name="name",
            public_key_material="publicKeyMaterial",
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
        name: typing.Optional[builtins.str] = None,
        public_key_material: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: Playback-key-pair name. The value does not need to be unique.
        :param public_key_material: The public portion of a customer-generated key pair.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8c9299641f93177a19cfd84cad783d859723e15238afc5b2487f08100163f85)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPlaybackKeyPairProps(
            name=name, public_key_material=public_key_material, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34197af23f293afc0148baab246f15cd2fe54b95571370449978a5aeca67fa11)
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
            type_hints = typing.get_type_hints(_typecheckingstub__032f36985f3069b4c60d8aea57dfc3994cc6fa0fc29cbdac055ac20e5f4aca7c)
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
        '''Key-pair ARN.

        For example: ``arn:aws:ivs:us-west-2:693991300569:playback-key/f99cde61-c2b0-4df3-8941-ca7d38acca1a``

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrFingerprint")
    def attr_fingerprint(self) -> builtins.str:
        '''Key-pair identifier.

        For example: ``98:0d:1a:a0:19:96:1e:ea:0a:0a:2c:9a:42:19:2b:e7``

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
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''Playback-key-pair name.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ec5d532530f73a41d36dd7016f4d18021d800813e68dbfa6f703cceca701478)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="publicKeyMaterial")
    def public_key_material(self) -> typing.Optional[builtins.str]:
        '''The public portion of a customer-generated key pair.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "publicKeyMaterial"))

    @public_key_material.setter
    def public_key_material(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4f35a09db8d81cf5fc7e7a397ca8172e49d613e64494c5a29798609a388e294)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicKeyMaterial", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74338171e55e9802fbeae4e8f45a4f31375c3a5730c487b0609b721a4660ce32)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ivs.CfnPlaybackKeyPairProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "public_key_material": "publicKeyMaterial",
        "tags": "tags",
    },
)
class CfnPlaybackKeyPairProps:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        public_key_material: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnPlaybackKeyPair``.

        :param name: Playback-key-pair name. The value does not need to be unique.
        :param public_key_material: The public portion of a customer-generated key pair.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-playbackkeypair.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ivs as ivs
            
            cfn_playback_key_pair_props = ivs.CfnPlaybackKeyPairProps(
                name="name",
                public_key_material="publicKeyMaterial",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a8be2c5b1653b9a20f33850cbab1a9c21d6b30034b5c68883e658d0e145e6a3)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument public_key_material", value=public_key_material, expected_type=type_hints["public_key_material"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if public_key_material is not None:
            self._values["public_key_material"] = public_key_material
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Playback-key-pair name.

        The value does not need to be unique.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-playbackkeypair.html#cfn-ivs-playbackkeypair-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def public_key_material(self) -> typing.Optional[builtins.str]:
        '''The public portion of a customer-generated key pair.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-playbackkeypair.html#cfn-ivs-playbackkeypair-publickeymaterial
        '''
        result = self._values.get("public_key_material")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-playbackkeypair.html#cfn-ivs-playbackkeypair-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPlaybackKeyPairProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnRecordingConfiguration(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ivs.CfnRecordingConfiguration",
):
    '''The ``AWS::IVS::RecordingConfiguration`` resource specifies an  recording configuration.

    A recording configuration enables the recording of a channel’s live streams to a data store. Multiple channels can reference the same recording configuration. For more information, see `RecordingConfiguration <https://docs.aws.amazon.com/ivs/latest/APIReference/API_RecordingConfiguration.html>`_ in the *Amazon Interactive Video Service API Reference* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-recordingconfiguration.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ivs as ivs
        
        cfn_recording_configuration = ivs.CfnRecordingConfiguration(self, "MyCfnRecordingConfiguration",
            destination_configuration=ivs.CfnRecordingConfiguration.DestinationConfigurationProperty(
                s3=ivs.CfnRecordingConfiguration.S3DestinationConfigurationProperty(
                    bucket_name="bucketName"
                )
            ),
        
            # the properties below are optional
            name="name",
            recording_reconnect_window_seconds=123,
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            thumbnail_configuration=ivs.CfnRecordingConfiguration.ThumbnailConfigurationProperty(
                recording_mode="recordingMode",
        
                # the properties below are optional
                target_interval_seconds=123
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        destination_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnRecordingConfiguration.DestinationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        name: typing.Optional[builtins.str] = None,
        recording_reconnect_window_seconds: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        thumbnail_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRecordingConfiguration.ThumbnailConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param destination_configuration: A destination configuration contains information about where recorded video will be stored. See the `DestinationConfiguration <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-recordingconfiguration-destinationconfiguration.html>`_ property type for more information.
        :param name: Recording-configuration name. The value does not need to be unique.
        :param recording_reconnect_window_seconds: If a broadcast disconnects and then reconnects within the specified interval, the multiple streams will be considered a single broadcast and merged together. *Default* : ``0`` Default: - 0
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        :param thumbnail_configuration: A thumbnail configuration enables/disables the recording of thumbnails for a live session and controls the interval at which thumbnails are generated for the live session. See the `ThumbnailConfiguration <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-recordingconfiguration-thunbnailconfiguration.html>`_ property type for more information.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__541cdf033047e5777646c5f067e03131707927e43c41e609fd3ac9ee776ae419)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnRecordingConfigurationProps(
            destination_configuration=destination_configuration,
            name=name,
            recording_reconnect_window_seconds=recording_reconnect_window_seconds,
            tags=tags,
            thumbnail_configuration=thumbnail_configuration,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d115d5ab74114a12edd8791ec11e4e4fd145cc6289d0579aac04f1c0c4089f8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3316cacec890424787de7224c6afcca2922a5899126aec97f005c3ea43409d1f)
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
        '''The recording configuration ARN.

        For example: ``arn:aws:ivs:us-west-2:123456789012:recording-configuration/abcdABCDefgh``

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrState")
    def attr_state(self) -> builtins.str:
        '''Indicates the current state of the recording configuration.

        When the state is ``ACTIVE`` , the configuration is ready to record a channel stream. Valid values: ``CREATING`` | ``CREATE_FAILED`` | ``ACTIVE`` .

        :cloudformationAttribute: State
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrState"))

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
    @jsii.member(jsii_name="destinationConfiguration")
    def destination_configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnRecordingConfiguration.DestinationConfigurationProperty"]:
        '''A destination configuration contains information about where recorded video will be stored.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnRecordingConfiguration.DestinationConfigurationProperty"], jsii.get(self, "destinationConfiguration"))

    @destination_configuration.setter
    def destination_configuration(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnRecordingConfiguration.DestinationConfigurationProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a98f37a00ab2b8c5a3413e54b7f022ac0bdf7ee44225243da737d75b9412595a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''Recording-configuration name.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6dd9b8dd365a2dac11937c93668ced572b553c203da9cbf1d9e0932d0e24faf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="recordingReconnectWindowSeconds")
    def recording_reconnect_window_seconds(self) -> typing.Optional[jsii.Number]:
        '''If a broadcast disconnects and then reconnects within the specified interval, the multiple streams will be considered a single broadcast and merged together.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "recordingReconnectWindowSeconds"))

    @recording_reconnect_window_seconds.setter
    def recording_reconnect_window_seconds(
        self,
        value: typing.Optional[jsii.Number],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38ff85ea7b2f1195ae4ae39514f42471c20d787399e92729b09aa86def8d11c4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recordingReconnectWindowSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__980f42185f1f8239b1f7d72b3f84be9a9c93c5d02f84695a71964c0630115230)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="thumbnailConfiguration")
    def thumbnail_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRecordingConfiguration.ThumbnailConfigurationProperty"]]:
        '''A thumbnail configuration enables/disables the recording of thumbnails for a live session and controls the interval at which thumbnails are generated for the live session.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRecordingConfiguration.ThumbnailConfigurationProperty"]], jsii.get(self, "thumbnailConfiguration"))

    @thumbnail_configuration.setter
    def thumbnail_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRecordingConfiguration.ThumbnailConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5cda01e5b9f5edb6a6ec7c5dce6ad1cecc2b7ce8727dd09a38d4b2b04befd3c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "thumbnailConfiguration", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ivs.CfnRecordingConfiguration.DestinationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"s3": "s3"},
    )
    class DestinationConfigurationProperty:
        def __init__(
            self,
            *,
            s3: typing.Union[_IResolvable_da3f097b, typing.Union["CfnRecordingConfiguration.S3DestinationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''The DestinationConfiguration property type describes the location where recorded videos will be stored.

            Each member represents a type of destination configuration. For recording, you define one and only one type of destination configuration.

            :param s3: An S3 destination configuration where recorded videos will be stored. See the `S3DestinationConfiguration <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-recordingconfiguration-s3destinationconfiguration.html>`_ property type for more information.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-recordingconfiguration-destinationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ivs as ivs
                
                destination_configuration_property = ivs.CfnRecordingConfiguration.DestinationConfigurationProperty(
                    s3=ivs.CfnRecordingConfiguration.S3DestinationConfigurationProperty(
                        bucket_name="bucketName"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__74552278e1b145c98ed786a3d8f29802876ef78e57a458c3030b125a545b6a0f)
                check_type(argname="argument s3", value=s3, expected_type=type_hints["s3"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "s3": s3,
            }

        @builtins.property
        def s3(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnRecordingConfiguration.S3DestinationConfigurationProperty"]:
            '''An S3 destination configuration where recorded videos will be stored.

            See the `S3DestinationConfiguration <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-recordingconfiguration-s3destinationconfiguration.html>`_ property type for more information.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-recordingconfiguration-destinationconfiguration.html#cfn-ivs-recordingconfiguration-destinationconfiguration-s3
            '''
            result = self._values.get("s3")
            assert result is not None, "Required property 's3' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnRecordingConfiguration.S3DestinationConfigurationProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DestinationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ivs.CfnRecordingConfiguration.S3DestinationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"bucket_name": "bucketName"},
    )
    class S3DestinationConfigurationProperty:
        def __init__(self, *, bucket_name: builtins.str) -> None:
            '''The S3DestinationConfiguration property type describes an S3 location where recorded videos will be stored.

            :param bucket_name: Location (S3 bucket name) where recorded videos will be stored.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-recordingconfiguration-s3destinationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ivs as ivs
                
                s3_destination_configuration_property = ivs.CfnRecordingConfiguration.S3DestinationConfigurationProperty(
                    bucket_name="bucketName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c973ee3e6df5393489017eab5a2edc4f798c18919ab571067170163085c0d659)
                check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bucket_name": bucket_name,
            }

        @builtins.property
        def bucket_name(self) -> builtins.str:
            '''Location (S3 bucket name) where recorded videos will be stored.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-recordingconfiguration-s3destinationconfiguration.html#cfn-ivs-recordingconfiguration-s3destinationconfiguration-bucketname
            '''
            result = self._values.get("bucket_name")
            assert result is not None, "Required property 'bucket_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3DestinationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ivs.CfnRecordingConfiguration.ThumbnailConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "recording_mode": "recordingMode",
            "target_interval_seconds": "targetIntervalSeconds",
        },
    )
    class ThumbnailConfigurationProperty:
        def __init__(
            self,
            *,
            recording_mode: builtins.str,
            target_interval_seconds: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''The ThumbnailConfiguration property type describes a configuration of thumbnails for recorded video.

            :param recording_mode: Thumbnail recording mode. Valid values:. - ``DISABLED`` : Use DISABLED to disable the generation of thumbnails for recorded video. - ``INTERVAL`` : Use INTERVAL to enable the generation of thumbnails for recorded video at a time interval controlled by the `TargetIntervalSeconds <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-recordingconfiguration-thumbnailconfiguration.html#cfn-ivs-recordingconfiguration-thumbnailconfiguration-targetintervalseconds>`_ property. *Default* : ``INTERVAL``
            :param target_interval_seconds: The targeted thumbnail-generation interval in seconds. This is configurable (and required) only if `RecordingMode <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-recordingconfiguration-thumbnailconfiguration.html#cfn-ivs-recordingconfiguration-thumbnailconfiguration-recordingmode>`_ is ``INTERVAL`` . .. epigraph:: Setting a value for ``TargetIntervalSeconds`` does not guarantee that thumbnails are generated at the specified interval. For thumbnails to be generated at the ``TargetIntervalSeconds`` interval, the ``IDR/Keyframe`` value for the input video must be less than the ``TargetIntervalSeconds`` value. See `Amazon IVS Streaming Configuration <https://docs.aws.amazon.com/ivs/latest/userguide/streaming-config.html>`_ for information on setting ``IDR/Keyframe`` to the recommended value in video-encoder settings. *Default* : 60 *Valid Range* : Minumum value of 5. Maximum value of 60.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-recordingconfiguration-thumbnailconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ivs as ivs
                
                thumbnail_configuration_property = ivs.CfnRecordingConfiguration.ThumbnailConfigurationProperty(
                    recording_mode="recordingMode",
                
                    # the properties below are optional
                    target_interval_seconds=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a4ff2be02860d22b7736feaee29733579c28da4de38d0a44a511a67d6659e786)
                check_type(argname="argument recording_mode", value=recording_mode, expected_type=type_hints["recording_mode"])
                check_type(argname="argument target_interval_seconds", value=target_interval_seconds, expected_type=type_hints["target_interval_seconds"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "recording_mode": recording_mode,
            }
            if target_interval_seconds is not None:
                self._values["target_interval_seconds"] = target_interval_seconds

        @builtins.property
        def recording_mode(self) -> builtins.str:
            '''Thumbnail recording mode. Valid values:.

            - ``DISABLED`` : Use DISABLED to disable the generation of thumbnails for recorded video.
            - ``INTERVAL`` : Use INTERVAL to enable the generation of thumbnails for recorded video at a time interval controlled by the `TargetIntervalSeconds <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-recordingconfiguration-thumbnailconfiguration.html#cfn-ivs-recordingconfiguration-thumbnailconfiguration-targetintervalseconds>`_ property.

            *Default* : ``INTERVAL``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-recordingconfiguration-thumbnailconfiguration.html#cfn-ivs-recordingconfiguration-thumbnailconfiguration-recordingmode
            '''
            result = self._values.get("recording_mode")
            assert result is not None, "Required property 'recording_mode' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def target_interval_seconds(self) -> typing.Optional[jsii.Number]:
            '''The targeted thumbnail-generation interval in seconds. This is configurable (and required) only if `RecordingMode <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-recordingconfiguration-thumbnailconfiguration.html#cfn-ivs-recordingconfiguration-thumbnailconfiguration-recordingmode>`_ is ``INTERVAL`` .

            .. epigraph::

               Setting a value for ``TargetIntervalSeconds`` does not guarantee that thumbnails are generated at the specified interval. For thumbnails to be generated at the ``TargetIntervalSeconds`` interval, the ``IDR/Keyframe`` value for the input video must be less than the ``TargetIntervalSeconds`` value. See `Amazon IVS Streaming Configuration <https://docs.aws.amazon.com/ivs/latest/userguide/streaming-config.html>`_ for information on setting ``IDR/Keyframe`` to the recommended value in video-encoder settings.

            *Default* : 60

            *Valid Range* : Minumum value of 5. Maximum value of 60.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-recordingconfiguration-thumbnailconfiguration.html#cfn-ivs-recordingconfiguration-thumbnailconfiguration-targetintervalseconds
            '''
            result = self._values.get("target_interval_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ThumbnailConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ivs.CfnRecordingConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={
        "destination_configuration": "destinationConfiguration",
        "name": "name",
        "recording_reconnect_window_seconds": "recordingReconnectWindowSeconds",
        "tags": "tags",
        "thumbnail_configuration": "thumbnailConfiguration",
    },
)
class CfnRecordingConfigurationProps:
    def __init__(
        self,
        *,
        destination_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRecordingConfiguration.DestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
        name: typing.Optional[builtins.str] = None,
        recording_reconnect_window_seconds: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        thumbnail_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRecordingConfiguration.ThumbnailConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnRecordingConfiguration``.

        :param destination_configuration: A destination configuration contains information about where recorded video will be stored. See the `DestinationConfiguration <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-recordingconfiguration-destinationconfiguration.html>`_ property type for more information.
        :param name: Recording-configuration name. The value does not need to be unique.
        :param recording_reconnect_window_seconds: If a broadcast disconnects and then reconnects within the specified interval, the multiple streams will be considered a single broadcast and merged together. *Default* : ``0`` Default: - 0
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        :param thumbnail_configuration: A thumbnail configuration enables/disables the recording of thumbnails for a live session and controls the interval at which thumbnails are generated for the live session. See the `ThumbnailConfiguration <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-recordingconfiguration-thunbnailconfiguration.html>`_ property type for more information.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-recordingconfiguration.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ivs as ivs
            
            cfn_recording_configuration_props = ivs.CfnRecordingConfigurationProps(
                destination_configuration=ivs.CfnRecordingConfiguration.DestinationConfigurationProperty(
                    s3=ivs.CfnRecordingConfiguration.S3DestinationConfigurationProperty(
                        bucket_name="bucketName"
                    )
                ),
            
                # the properties below are optional
                name="name",
                recording_reconnect_window_seconds=123,
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                thumbnail_configuration=ivs.CfnRecordingConfiguration.ThumbnailConfigurationProperty(
                    recording_mode="recordingMode",
            
                    # the properties below are optional
                    target_interval_seconds=123
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba7ddd4570fd05b5ededda48336345665e566391438dd61208aea34c865f91c1)
            check_type(argname="argument destination_configuration", value=destination_configuration, expected_type=type_hints["destination_configuration"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument recording_reconnect_window_seconds", value=recording_reconnect_window_seconds, expected_type=type_hints["recording_reconnect_window_seconds"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument thumbnail_configuration", value=thumbnail_configuration, expected_type=type_hints["thumbnail_configuration"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "destination_configuration": destination_configuration,
        }
        if name is not None:
            self._values["name"] = name
        if recording_reconnect_window_seconds is not None:
            self._values["recording_reconnect_window_seconds"] = recording_reconnect_window_seconds
        if tags is not None:
            self._values["tags"] = tags
        if thumbnail_configuration is not None:
            self._values["thumbnail_configuration"] = thumbnail_configuration

    @builtins.property
    def destination_configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnRecordingConfiguration.DestinationConfigurationProperty]:
        '''A destination configuration contains information about where recorded video will be stored.

        See the `DestinationConfiguration <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-recordingconfiguration-destinationconfiguration.html>`_ property type for more information.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-recordingconfiguration.html#cfn-ivs-recordingconfiguration-destinationconfiguration
        '''
        result = self._values.get("destination_configuration")
        assert result is not None, "Required property 'destination_configuration' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnRecordingConfiguration.DestinationConfigurationProperty], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Recording-configuration name.

        The value does not need to be unique.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-recordingconfiguration.html#cfn-ivs-recordingconfiguration-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def recording_reconnect_window_seconds(self) -> typing.Optional[jsii.Number]:
        '''If a broadcast disconnects and then reconnects within the specified interval, the multiple streams will be considered a single broadcast and merged together.

        *Default* : ``0``

        :default: - 0

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-recordingconfiguration.html#cfn-ivs-recordingconfiguration-recordingreconnectwindowseconds
        '''
        result = self._values.get("recording_reconnect_window_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-recordingconfiguration.html#cfn-ivs-recordingconfiguration-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def thumbnail_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnRecordingConfiguration.ThumbnailConfigurationProperty]]:
        '''A thumbnail configuration enables/disables the recording of thumbnails for a live session and controls the interval at which thumbnails are generated for the live session.

        See the `ThumbnailConfiguration <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-recordingconfiguration-thunbnailconfiguration.html>`_ property type for more information.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-recordingconfiguration.html#cfn-ivs-recordingconfiguration-thumbnailconfiguration
        '''
        result = self._values.get("thumbnail_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnRecordingConfiguration.ThumbnailConfigurationProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRecordingConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnStreamKey(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ivs.CfnStreamKey",
):
    '''The ``AWS::IVS::StreamKey`` resource specifies an  stream key associated with the referenced channel.

    Use a stream key to initiate a live stream.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-streamkey.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ivs as ivs
        
        cfn_stream_key = ivs.CfnStreamKey(self, "MyCfnStreamKey",
            channel_arn="channelArn",
        
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
        channel_arn: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param channel_arn: Channel ARN for the stream.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c508febc00a5b76d50ae6b38407e9fa4357bcef12dfb4180bbc821ced1e89112)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnStreamKeyProps(channel_arn=channel_arn, tags=tags)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c99a5ab18db8efd571b038c0d95c39758a584cec29efba661700074d2cf30bde)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ace437399547bc58926abe652ff0b6b8e00340a20eb309b99e2b5335ded44a08)
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
        '''The stream-key ARN.

        For example: ``arn:aws:ivs:us-west-2:123456789012:stream-key/g1H2I3j4k5L6``

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrValue")
    def attr_value(self) -> builtins.str:
        '''The stream-key value.

        For example: ``sk_us-west-2_abcdABCDefgh_567890abcdef``

        :cloudformationAttribute: Value
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrValue"))

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
    @jsii.member(jsii_name="channelArn")
    def channel_arn(self) -> builtins.str:
        '''Channel ARN for the stream.'''
        return typing.cast(builtins.str, jsii.get(self, "channelArn"))

    @channel_arn.setter
    def channel_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9fd7a730586bf4c02632ce69c6183339889a337f21e75e7368edd67dd583ea34)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "channelArn", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b966c0532d39deb26a3bd43a45365e1ee3edf5d3158d0a479134abca9f6f9d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ivs.CfnStreamKeyProps",
    jsii_struct_bases=[],
    name_mapping={"channel_arn": "channelArn", "tags": "tags"},
)
class CfnStreamKeyProps:
    def __init__(
        self,
        *,
        channel_arn: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnStreamKey``.

        :param channel_arn: Channel ARN for the stream.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-streamkey.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ivs as ivs
            
            cfn_stream_key_props = ivs.CfnStreamKeyProps(
                channel_arn="channelArn",
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a1d6f99b4c86a24198701caf819ea7b5d402ec68c7406b7aff6a02facc7e7c0)
            check_type(argname="argument channel_arn", value=channel_arn, expected_type=type_hints["channel_arn"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "channel_arn": channel_arn,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def channel_arn(self) -> builtins.str:
        '''Channel ARN for the stream.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-streamkey.html#cfn-ivs-streamkey-channelarn
        '''
        result = self._values.get("channel_arn")
        assert result is not None, "Required property 'channel_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-streamkey.html#cfn-ivs-streamkey-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnStreamKeyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnChannel",
    "CfnChannelProps",
    "CfnPlaybackKeyPair",
    "CfnPlaybackKeyPairProps",
    "CfnRecordingConfiguration",
    "CfnRecordingConfigurationProps",
    "CfnStreamKey",
    "CfnStreamKeyProps",
]

publication.publish()

def _typecheckingstub__998485c6924ca07e096c10b7976e238a36e5cfb75264ee66a67de472363369d6(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    authorized: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    insecure_ingest: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    latency_mode: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    preset: typing.Optional[builtins.str] = None,
    recording_configuration_arn: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b2f270a2cc06d7958dc82935ff792ce64817de7fc16c4f4b5a7afa6f76cdd80(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0fa81ac5355ae77db888dc8d0fb4cbbff54f381372b1c5a191ceb5eb77a6442b(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e83b3a70b60de37a8aabc9c019b31db83c549e80f9c9c88a5b74fde72ecb20e(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__734c5e1f9cdeabe74fb1ade992399b475d1594cbcdfd026823e8984eaa2d4eab(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd2cfeff050510b655ecd39d0e3b95c3c9e2af649e77e0903ad721d0f6428ab5(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15776afbbb29227b4807e807447939235926366be32ef5acc331c74f0acd9b41(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95e047ef543e7e26080292a0481b6ce40457143e76918ac4c1c2d13855ce22ee(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0eb4132c8e5e803f734f8f894d72d2324ee00be84b0babafa7076d94d732c960(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da42cce1a703989106b1844fef6f10d0a57f43c733d171564b16f83c208e7196(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0be9a3a6192cfd130520f4e6ecd8c9091b1a8b4312f716182989ea3feb88dc8b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61646017dba4df4ec5b97fde61911670aebc6b8151847b927754a4e9c110979d(
    *,
    authorized: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    insecure_ingest: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    latency_mode: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    preset: typing.Optional[builtins.str] = None,
    recording_configuration_arn: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8c9299641f93177a19cfd84cad783d859723e15238afc5b2487f08100163f85(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: typing.Optional[builtins.str] = None,
    public_key_material: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34197af23f293afc0148baab246f15cd2fe54b95571370449978a5aeca67fa11(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__032f36985f3069b4c60d8aea57dfc3994cc6fa0fc29cbdac055ac20e5f4aca7c(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ec5d532530f73a41d36dd7016f4d18021d800813e68dbfa6f703cceca701478(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4f35a09db8d81cf5fc7e7a397ca8172e49d613e64494c5a29798609a388e294(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74338171e55e9802fbeae4e8f45a4f31375c3a5730c487b0609b721a4660ce32(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a8be2c5b1653b9a20f33850cbab1a9c21d6b30034b5c68883e658d0e145e6a3(
    *,
    name: typing.Optional[builtins.str] = None,
    public_key_material: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__541cdf033047e5777646c5f067e03131707927e43c41e609fd3ac9ee776ae419(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    destination_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRecordingConfiguration.DestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    name: typing.Optional[builtins.str] = None,
    recording_reconnect_window_seconds: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    thumbnail_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRecordingConfiguration.ThumbnailConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d115d5ab74114a12edd8791ec11e4e4fd145cc6289d0579aac04f1c0c4089f8(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3316cacec890424787de7224c6afcca2922a5899126aec97f005c3ea43409d1f(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a98f37a00ab2b8c5a3413e54b7f022ac0bdf7ee44225243da737d75b9412595a(
    value: typing.Union[_IResolvable_da3f097b, CfnRecordingConfiguration.DestinationConfigurationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6dd9b8dd365a2dac11937c93668ced572b553c203da9cbf1d9e0932d0e24faf(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38ff85ea7b2f1195ae4ae39514f42471c20d787399e92729b09aa86def8d11c4(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__980f42185f1f8239b1f7d72b3f84be9a9c93c5d02f84695a71964c0630115230(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5cda01e5b9f5edb6a6ec7c5dce6ad1cecc2b7ce8727dd09a38d4b2b04befd3c(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnRecordingConfiguration.ThumbnailConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74552278e1b145c98ed786a3d8f29802876ef78e57a458c3030b125a545b6a0f(
    *,
    s3: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRecordingConfiguration.S3DestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c973ee3e6df5393489017eab5a2edc4f798c18919ab571067170163085c0d659(
    *,
    bucket_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4ff2be02860d22b7736feaee29733579c28da4de38d0a44a511a67d6659e786(
    *,
    recording_mode: builtins.str,
    target_interval_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba7ddd4570fd05b5ededda48336345665e566391438dd61208aea34c865f91c1(
    *,
    destination_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRecordingConfiguration.DestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    name: typing.Optional[builtins.str] = None,
    recording_reconnect_window_seconds: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    thumbnail_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRecordingConfiguration.ThumbnailConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c508febc00a5b76d50ae6b38407e9fa4357bcef12dfb4180bbc821ced1e89112(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    channel_arn: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c99a5ab18db8efd571b038c0d95c39758a584cec29efba661700074d2cf30bde(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ace437399547bc58926abe652ff0b6b8e00340a20eb309b99e2b5335ded44a08(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9fd7a730586bf4c02632ce69c6183339889a337f21e75e7368edd67dd583ea34(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b966c0532d39deb26a3bd43a45365e1ee3edf5d3158d0a479134abca9f6f9d2(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a1d6f99b4c86a24198701caf819ea7b5d402ec68c7406b7aff6a02facc7e7c0(
    *,
    channel_arn: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
