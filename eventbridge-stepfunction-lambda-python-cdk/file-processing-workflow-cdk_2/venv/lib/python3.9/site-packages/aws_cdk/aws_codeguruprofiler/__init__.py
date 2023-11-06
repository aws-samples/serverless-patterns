'''
# AWS::CodeGuruProfiler Construct Library

Amazon CodeGuru Profiler collects runtime performance data from your live applications, and provides recommendations that can help you fine-tune your application performance.

## Installation

Import to your project:

```python
import aws_cdk.aws_codeguruprofiler as codeguruprofiler
```

## Basic usage

Here's how to setup a profiling group and give your compute role permissions to publish to the profiling group to the profiling agent can publish profiling information:

```python
# The execution role of your application that publishes to the ProfilingGroup via CodeGuru Profiler Profiling Agent. (the following is merely an example)
publish_app_role = iam.Role(self, "PublishAppRole",
    assumed_by=iam.AccountRootPrincipal()
)

profiling_group = codeguruprofiler.ProfilingGroup(self, "MyProfilingGroup")
profiling_group.grant_publish(publish_app_role)
```

## Compute Platform configuration

Code Guru Profiler supports multiple compute environments.
They can be configured when creating a Profiling Group by using the `computePlatform` property:

```python
profiling_group = codeguruprofiler.ProfilingGroup(self, "MyProfilingGroup",
    compute_platform=codeguruprofiler.ComputePlatform.AWS_LAMBDA
)
```
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
    IResource as _IResource_c80c4260,
    ITaggable as _ITaggable_36806126,
    Resource as _Resource_45bc6135,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)
from ..aws_iam import Grant as _Grant_a7ae64f8, IGrantable as _IGrantable_71c4f5de


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnProfilingGroup(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_codeguruprofiler.CfnProfilingGroup",
):
    '''Creates a profiling group.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeguruprofiler-profilinggroup.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_codeguruprofiler as codeguruprofiler
        
        # agent_permissions: Any
        
        cfn_profiling_group = codeguruprofiler.CfnProfilingGroup(self, "MyCfnProfilingGroup",
            profiling_group_name="profilingGroupName",
        
            # the properties below are optional
            agent_permissions=agent_permissions,
            anomaly_detection_notification_configuration=[codeguruprofiler.CfnProfilingGroup.ChannelProperty(
                channel_uri="channelUri",
        
                # the properties below are optional
                channel_id="channelId"
            )],
            compute_platform="computePlatform",
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
        profiling_group_name: builtins.str,
        agent_permissions: typing.Any = None,
        anomaly_detection_notification_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnProfilingGroup.ChannelProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        compute_platform: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param profiling_group_name: The name of the profiling group.
        :param agent_permissions: The agent permissions attached to this profiling group. This action group grants ``ConfigureAgent`` and ``PostAgentProfile`` permissions to perform actions required by the profiling agent. The Json consists of key ``Principals`` . *Principals* : A list of string ARNs for the roles and users you want to grant access to the profiling group. Wildcards are not supported in the ARNs. You are allowed to provide up to 50 ARNs. An empty list is not permitted. This is a required key. For more information, see `Resource-based policies in CodeGuru Profiler <https://docs.aws.amazon.com/codeguru/latest/profiler-ug/resource-based-policies.html>`_ in the *Amazon CodeGuru Profiler user guide* , `ConfigureAgent <https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ConfigureAgent.html>`_ , and `PostAgentProfile <https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_PostAgentProfile.html>`_ .
        :param anomaly_detection_notification_configuration: Adds anomaly notifications for a profiling group.
        :param compute_platform: The compute platform of the profiling group. Use ``AWSLambda`` if your application runs on AWS Lambda. Use ``Default`` if your application runs on a compute platform that is not AWS Lambda , such an Amazon EC2 instance, an on-premises server, or a different platform. If not specified, ``Default`` is used. This property is immutable.
        :param tags: A list of tags to add to the created profiling group.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9aa0abb6bab44bc6d99509172735702ee5d874bf3f43241d8a04bc9b239b8bf)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnProfilingGroupProps(
            profiling_group_name=profiling_group_name,
            agent_permissions=agent_permissions,
            anomaly_detection_notification_configuration=anomaly_detection_notification_configuration,
            compute_platform=compute_platform,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24a556687187f3fa5c9bf014559a3a117b65e51abfce2431cb066434dd4eaa44)
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
            type_hints = typing.get_type_hints(_typecheckingstub__fafc590c253689aa6dbe3ece2a14715971b41a0287ac3abea2185200d7448965)
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
        '''The full Amazon Resource Name (ARN) for that profiling group.

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
    @jsii.member(jsii_name="profilingGroupName")
    def profiling_group_name(self) -> builtins.str:
        '''The name of the profiling group.'''
        return typing.cast(builtins.str, jsii.get(self, "profilingGroupName"))

    @profiling_group_name.setter
    def profiling_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5573a5208adffdf4734f691eb4ff7539202b1db0e5b1ca78bff1b5df9d85c73)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "profilingGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="agentPermissions")
    def agent_permissions(self) -> typing.Any:
        '''The agent permissions attached to this profiling group.'''
        return typing.cast(typing.Any, jsii.get(self, "agentPermissions"))

    @agent_permissions.setter
    def agent_permissions(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17d718bda323291cfa3fcddd8a1a5bb1086c9c8fc294cbc26895b278f35c89d1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "agentPermissions", value)

    @builtins.property
    @jsii.member(jsii_name="anomalyDetectionNotificationConfiguration")
    def anomaly_detection_notification_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnProfilingGroup.ChannelProperty"]]]]:
        '''Adds anomaly notifications for a profiling group.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnProfilingGroup.ChannelProperty"]]]], jsii.get(self, "anomalyDetectionNotificationConfiguration"))

    @anomaly_detection_notification_configuration.setter
    def anomaly_detection_notification_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnProfilingGroup.ChannelProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__316c247cfa3a39c676bf4ce8b50310a7688cf6084a673ebde8f3462cb4464ee6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "anomalyDetectionNotificationConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="computePlatform")
    def compute_platform(self) -> typing.Optional[builtins.str]:
        '''The compute platform of the profiling group.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "computePlatform"))

    @compute_platform.setter
    def compute_platform(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb128be2e7cd15970dee2ea394d635c967fffc05335b5468f285d71eb7972df8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "computePlatform", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of tags to add to the created profiling group.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cda9ac694cf4a0730ba8c58dcc623c74646a296072486d91f42a1051fefcfef7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_codeguruprofiler.CfnProfilingGroup.AgentPermissionsProperty",
        jsii_struct_bases=[],
        name_mapping={"principals": "principals"},
    )
    class AgentPermissionsProperty:
        def __init__(self, *, principals: typing.Sequence[builtins.str]) -> None:
            '''The agent permissions attached to this profiling group.

            :param principals: The principals for the agent permissions.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codeguruprofiler-profilinggroup-agentpermissions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_codeguruprofiler as codeguruprofiler
                
                agent_permissions_property = codeguruprofiler.CfnProfilingGroup.AgentPermissionsProperty(
                    principals=["principals"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__811cebbf9ff71c6cdc0a3e6f6073b243f3749069770de9b6715845db6a859300)
                check_type(argname="argument principals", value=principals, expected_type=type_hints["principals"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "principals": principals,
            }

        @builtins.property
        def principals(self) -> typing.List[builtins.str]:
            '''The principals for the agent permissions.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codeguruprofiler-profilinggroup-agentpermissions.html#cfn-codeguruprofiler-profilinggroup-agentpermissions-principals
            '''
            result = self._values.get("principals")
            assert result is not None, "Required property 'principals' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AgentPermissionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_codeguruprofiler.CfnProfilingGroup.ChannelProperty",
        jsii_struct_bases=[],
        name_mapping={"channel_uri": "channelUri", "channel_id": "channelId"},
    )
    class ChannelProperty:
        def __init__(
            self,
            *,
            channel_uri: builtins.str,
            channel_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Notification medium for users to get alerted for events that occur in application profile.

            We support SNS topic as a notification channel.

            :param channel_uri: The channel URI.
            :param channel_id: The channel ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codeguruprofiler-profilinggroup-channel.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_codeguruprofiler as codeguruprofiler
                
                channel_property = codeguruprofiler.CfnProfilingGroup.ChannelProperty(
                    channel_uri="channelUri",
                
                    # the properties below are optional
                    channel_id="channelId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__897f8a8de60bab360ab0a19378aece0020e93e34fe48060c6e6eca85b77617e3)
                check_type(argname="argument channel_uri", value=channel_uri, expected_type=type_hints["channel_uri"])
                check_type(argname="argument channel_id", value=channel_id, expected_type=type_hints["channel_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "channel_uri": channel_uri,
            }
            if channel_id is not None:
                self._values["channel_id"] = channel_id

        @builtins.property
        def channel_uri(self) -> builtins.str:
            '''The channel URI.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codeguruprofiler-profilinggroup-channel.html#cfn-codeguruprofiler-profilinggroup-channel-channeluri
            '''
            result = self._values.get("channel_uri")
            assert result is not None, "Required property 'channel_uri' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def channel_id(self) -> typing.Optional[builtins.str]:
            '''The channel ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codeguruprofiler-profilinggroup-channel.html#cfn-codeguruprofiler-profilinggroup-channel-channelid
            '''
            result = self._values.get("channel_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ChannelProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codeguruprofiler.CfnProfilingGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "profiling_group_name": "profilingGroupName",
        "agent_permissions": "agentPermissions",
        "anomaly_detection_notification_configuration": "anomalyDetectionNotificationConfiguration",
        "compute_platform": "computePlatform",
        "tags": "tags",
    },
)
class CfnProfilingGroupProps:
    def __init__(
        self,
        *,
        profiling_group_name: builtins.str,
        agent_permissions: typing.Any = None,
        anomaly_detection_notification_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnProfilingGroup.ChannelProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        compute_platform: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnProfilingGroup``.

        :param profiling_group_name: The name of the profiling group.
        :param agent_permissions: The agent permissions attached to this profiling group. This action group grants ``ConfigureAgent`` and ``PostAgentProfile`` permissions to perform actions required by the profiling agent. The Json consists of key ``Principals`` . *Principals* : A list of string ARNs for the roles and users you want to grant access to the profiling group. Wildcards are not supported in the ARNs. You are allowed to provide up to 50 ARNs. An empty list is not permitted. This is a required key. For more information, see `Resource-based policies in CodeGuru Profiler <https://docs.aws.amazon.com/codeguru/latest/profiler-ug/resource-based-policies.html>`_ in the *Amazon CodeGuru Profiler user guide* , `ConfigureAgent <https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ConfigureAgent.html>`_ , and `PostAgentProfile <https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_PostAgentProfile.html>`_ .
        :param anomaly_detection_notification_configuration: Adds anomaly notifications for a profiling group.
        :param compute_platform: The compute platform of the profiling group. Use ``AWSLambda`` if your application runs on AWS Lambda. Use ``Default`` if your application runs on a compute platform that is not AWS Lambda , such an Amazon EC2 instance, an on-premises server, or a different platform. If not specified, ``Default`` is used. This property is immutable.
        :param tags: A list of tags to add to the created profiling group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeguruprofiler-profilinggroup.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_codeguruprofiler as codeguruprofiler
            
            # agent_permissions: Any
            
            cfn_profiling_group_props = codeguruprofiler.CfnProfilingGroupProps(
                profiling_group_name="profilingGroupName",
            
                # the properties below are optional
                agent_permissions=agent_permissions,
                anomaly_detection_notification_configuration=[codeguruprofiler.CfnProfilingGroup.ChannelProperty(
                    channel_uri="channelUri",
            
                    # the properties below are optional
                    channel_id="channelId"
                )],
                compute_platform="computePlatform",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0311e48a474ca90384078ca3a0759f5a58ab45163d3da706301f20c5207756e)
            check_type(argname="argument profiling_group_name", value=profiling_group_name, expected_type=type_hints["profiling_group_name"])
            check_type(argname="argument agent_permissions", value=agent_permissions, expected_type=type_hints["agent_permissions"])
            check_type(argname="argument anomaly_detection_notification_configuration", value=anomaly_detection_notification_configuration, expected_type=type_hints["anomaly_detection_notification_configuration"])
            check_type(argname="argument compute_platform", value=compute_platform, expected_type=type_hints["compute_platform"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "profiling_group_name": profiling_group_name,
        }
        if agent_permissions is not None:
            self._values["agent_permissions"] = agent_permissions
        if anomaly_detection_notification_configuration is not None:
            self._values["anomaly_detection_notification_configuration"] = anomaly_detection_notification_configuration
        if compute_platform is not None:
            self._values["compute_platform"] = compute_platform
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def profiling_group_name(self) -> builtins.str:
        '''The name of the profiling group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeguruprofiler-profilinggroup.html#cfn-codeguruprofiler-profilinggroup-profilinggroupname
        '''
        result = self._values.get("profiling_group_name")
        assert result is not None, "Required property 'profiling_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def agent_permissions(self) -> typing.Any:
        '''The agent permissions attached to this profiling group.

        This action group grants ``ConfigureAgent`` and ``PostAgentProfile`` permissions to perform actions required by the profiling agent. The Json consists of key ``Principals`` .

        *Principals* : A list of string ARNs for the roles and users you want to grant access to the profiling group. Wildcards are not supported in the ARNs. You are allowed to provide up to 50 ARNs. An empty list is not permitted. This is a required key.

        For more information, see `Resource-based policies in CodeGuru Profiler <https://docs.aws.amazon.com/codeguru/latest/profiler-ug/resource-based-policies.html>`_ in the *Amazon CodeGuru Profiler user guide* , `ConfigureAgent <https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ConfigureAgent.html>`_ , and `PostAgentProfile <https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_PostAgentProfile.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeguruprofiler-profilinggroup.html#cfn-codeguruprofiler-profilinggroup-agentpermissions
        '''
        result = self._values.get("agent_permissions")
        return typing.cast(typing.Any, result)

    @builtins.property
    def anomaly_detection_notification_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnProfilingGroup.ChannelProperty]]]]:
        '''Adds anomaly notifications for a profiling group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeguruprofiler-profilinggroup.html#cfn-codeguruprofiler-profilinggroup-anomalydetectionnotificationconfiguration
        '''
        result = self._values.get("anomaly_detection_notification_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnProfilingGroup.ChannelProperty]]]], result)

    @builtins.property
    def compute_platform(self) -> typing.Optional[builtins.str]:
        '''The compute platform of the profiling group.

        Use ``AWSLambda`` if your application runs on AWS Lambda. Use ``Default`` if your application runs on a compute platform that is not AWS Lambda , such an Amazon EC2 instance, an on-premises server, or a different platform. If not specified, ``Default`` is used. This property is immutable.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeguruprofiler-profilinggroup.html#cfn-codeguruprofiler-profilinggroup-computeplatform
        '''
        result = self._values.get("compute_platform")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of tags to add to the created profiling group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeguruprofiler-profilinggroup.html#cfn-codeguruprofiler-profilinggroup-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnProfilingGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_codeguruprofiler.ComputePlatform")
class ComputePlatform(enum.Enum):
    '''The compute platform of the profiling group.

    :exampleMetadata: infused

    Example::

        profiling_group = codeguruprofiler.ProfilingGroup(self, "MyProfilingGroup",
            compute_platform=codeguruprofiler.ComputePlatform.AWS_LAMBDA
        )
    '''

    AWS_LAMBDA = "AWS_LAMBDA"
    '''Use AWS_LAMBDA if your application runs on AWS Lambda.'''
    DEFAULT = "DEFAULT"
    '''Use Default if your application runs on a compute platform that is not AWS Lambda, such an Amazon EC2 instance, an on-premises server, or a different platform.'''


@jsii.interface(jsii_type="aws-cdk-lib.aws_codeguruprofiler.IProfilingGroup")
class IProfilingGroup(_IResource_c80c4260, typing_extensions.Protocol):
    '''IResource represents a Profiling Group.'''

    @builtins.property
    @jsii.member(jsii_name="profilingGroupArn")
    def profiling_group_arn(self) -> builtins.str:
        '''The ARN of the profiling group.

        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="profilingGroupName")
    def profiling_group_name(self) -> builtins.str:
        '''The name of the profiling group.

        :attribute: true
        '''
        ...

    @jsii.member(jsii_name="grantPublish")
    def grant_publish(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant access to publish profiling information to the Profiling Group to the given identity.

        This will grant the following permissions:

        - codeguru-profiler:ConfigureAgent
        - codeguru-profiler:PostAgentProfile

        :param grantee: Principal to grant publish rights to.
        '''
        ...

    @jsii.member(jsii_name="grantRead")
    def grant_read(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant access to read profiling information from the Profiling Group to the given identity.

        This will grant the following permissions:

        - codeguru-profiler:GetProfile
        - codeguru-profiler:DescribeProfilingGroup

        :param grantee: Principal to grant read rights to.
        '''
        ...


class _IProfilingGroupProxy(
    jsii.proxy_for(_IResource_c80c4260), # type: ignore[misc]
):
    '''IResource represents a Profiling Group.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_codeguruprofiler.IProfilingGroup"

    @builtins.property
    @jsii.member(jsii_name="profilingGroupArn")
    def profiling_group_arn(self) -> builtins.str:
        '''The ARN of the profiling group.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "profilingGroupArn"))

    @builtins.property
    @jsii.member(jsii_name="profilingGroupName")
    def profiling_group_name(self) -> builtins.str:
        '''The name of the profiling group.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "profilingGroupName"))

    @jsii.member(jsii_name="grantPublish")
    def grant_publish(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant access to publish profiling information to the Profiling Group to the given identity.

        This will grant the following permissions:

        - codeguru-profiler:ConfigureAgent
        - codeguru-profiler:PostAgentProfile

        :param grantee: Principal to grant publish rights to.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8eef65bccc91bd6f83597064fade053f490648802b0350f9227188dc1487b758)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantPublish", [grantee]))

    @jsii.member(jsii_name="grantRead")
    def grant_read(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant access to read profiling information from the Profiling Group to the given identity.

        This will grant the following permissions:

        - codeguru-profiler:GetProfile
        - codeguru-profiler:DescribeProfilingGroup

        :param grantee: Principal to grant read rights to.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fad88677a83439824b5289f835fd0b41a038abaadbb21252ece4a01a245e1033)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantRead", [grantee]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IProfilingGroup).__jsii_proxy_class__ = lambda : _IProfilingGroupProxy


@jsii.implements(IProfilingGroup)
class ProfilingGroup(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_codeguruprofiler.ProfilingGroup",
):
    '''A new Profiling Group.

    :exampleMetadata: infused

    Example::

        # The execution role of your application that publishes to the ProfilingGroup via CodeGuru Profiler Profiling Agent. (the following is merely an example)
        publish_app_role = iam.Role(self, "PublishAppRole",
            assumed_by=iam.AccountRootPrincipal()
        )
        
        profiling_group = codeguruprofiler.ProfilingGroup(self, "MyProfilingGroup")
        profiling_group.grant_publish(publish_app_role)
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        compute_platform: typing.Optional[ComputePlatform] = None,
        profiling_group_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param compute_platform: The compute platform of the profiling group. Default: ComputePlatform.DEFAULT
        :param profiling_group_name: A name for the profiling group. Default: - automatically generated name.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__455d9f8e0fda8271257c6c1025ea87ea065d36bfefe7d63f702c45b526cc1976)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ProfilingGroupProps(
            compute_platform=compute_platform,
            profiling_group_name=profiling_group_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromProfilingGroupArn")
    @builtins.classmethod
    def from_profiling_group_arn(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        profiling_group_arn: builtins.str,
    ) -> IProfilingGroup:
        '''Import an existing Profiling Group provided an ARN.

        :param scope: The parent creating construct.
        :param id: The construct's name.
        :param profiling_group_arn: Profiling Group ARN.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b91b6e9dff0c314a77924dad57869cdc71781e124518a42fbbb57612c6f29d4b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument profiling_group_arn", value=profiling_group_arn, expected_type=type_hints["profiling_group_arn"])
        return typing.cast(IProfilingGroup, jsii.sinvoke(cls, "fromProfilingGroupArn", [scope, id, profiling_group_arn]))

    @jsii.member(jsii_name="fromProfilingGroupName")
    @builtins.classmethod
    def from_profiling_group_name(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        profiling_group_name: builtins.str,
    ) -> IProfilingGroup:
        '''Import an existing Profiling Group provided a Profiling Group Name.

        :param scope: The parent creating construct.
        :param id: The construct's name.
        :param profiling_group_name: Profiling Group Name.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__833a9e7894a97394ac1565daa3d417cd81e363776254c84ac034b459e478c491)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument profiling_group_name", value=profiling_group_name, expected_type=type_hints["profiling_group_name"])
        return typing.cast(IProfilingGroup, jsii.sinvoke(cls, "fromProfilingGroupName", [scope, id, profiling_group_name]))

    @jsii.member(jsii_name="grantPublish")
    def grant_publish(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant access to publish profiling information to the Profiling Group to the given identity.

        This will grant the following permissions:

        - codeguru-profiler:ConfigureAgent
        - codeguru-profiler:PostAgentProfile

        :param grantee: Principal to grant publish rights to.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18fa54053affb91d59e1ada2098754620fc3f0b31a3be3a82e08a29b665655f4)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantPublish", [grantee]))

    @jsii.member(jsii_name="grantRead")
    def grant_read(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant access to read profiling information from the Profiling Group to the given identity.

        This will grant the following permissions:

        - codeguru-profiler:GetProfile
        - codeguru-profiler:DescribeProfilingGroup

        :param grantee: Principal to grant read rights to.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23cf99a24a4b56d46b427eae23b846bdf8f4365553fa7bd0efc8267f78934894)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantRead", [grantee]))

    @builtins.property
    @jsii.member(jsii_name="profilingGroupArn")
    def profiling_group_arn(self) -> builtins.str:
        '''The ARN of the Profiling Group.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "profilingGroupArn"))

    @builtins.property
    @jsii.member(jsii_name="profilingGroupName")
    def profiling_group_name(self) -> builtins.str:
        '''The name of the Profiling Group.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "profilingGroupName"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codeguruprofiler.ProfilingGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "compute_platform": "computePlatform",
        "profiling_group_name": "profilingGroupName",
    },
)
class ProfilingGroupProps:
    def __init__(
        self,
        *,
        compute_platform: typing.Optional[ComputePlatform] = None,
        profiling_group_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for creating a new Profiling Group.

        :param compute_platform: The compute platform of the profiling group. Default: ComputePlatform.DEFAULT
        :param profiling_group_name: A name for the profiling group. Default: - automatically generated name.

        :exampleMetadata: infused

        Example::

            profiling_group = codeguruprofiler.ProfilingGroup(self, "MyProfilingGroup",
                compute_platform=codeguruprofiler.ComputePlatform.AWS_LAMBDA
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4843108164af294aabe875088a5b93297a7983cba8b4e8af4a9bcae0fb6659c)
            check_type(argname="argument compute_platform", value=compute_platform, expected_type=type_hints["compute_platform"])
            check_type(argname="argument profiling_group_name", value=profiling_group_name, expected_type=type_hints["profiling_group_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if compute_platform is not None:
            self._values["compute_platform"] = compute_platform
        if profiling_group_name is not None:
            self._values["profiling_group_name"] = profiling_group_name

    @builtins.property
    def compute_platform(self) -> typing.Optional[ComputePlatform]:
        '''The compute platform of the profiling group.

        :default: ComputePlatform.DEFAULT
        '''
        result = self._values.get("compute_platform")
        return typing.cast(typing.Optional[ComputePlatform], result)

    @builtins.property
    def profiling_group_name(self) -> typing.Optional[builtins.str]:
        '''A name for the profiling group.

        :default: - automatically generated name.
        '''
        result = self._values.get("profiling_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProfilingGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnProfilingGroup",
    "CfnProfilingGroupProps",
    "ComputePlatform",
    "IProfilingGroup",
    "ProfilingGroup",
    "ProfilingGroupProps",
]

publication.publish()

def _typecheckingstub__c9aa0abb6bab44bc6d99509172735702ee5d874bf3f43241d8a04bc9b239b8bf(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    profiling_group_name: builtins.str,
    agent_permissions: typing.Any = None,
    anomaly_detection_notification_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnProfilingGroup.ChannelProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    compute_platform: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24a556687187f3fa5c9bf014559a3a117b65e51abfce2431cb066434dd4eaa44(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fafc590c253689aa6dbe3ece2a14715971b41a0287ac3abea2185200d7448965(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5573a5208adffdf4734f691eb4ff7539202b1db0e5b1ca78bff1b5df9d85c73(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17d718bda323291cfa3fcddd8a1a5bb1086c9c8fc294cbc26895b278f35c89d1(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__316c247cfa3a39c676bf4ce8b50310a7688cf6084a673ebde8f3462cb4464ee6(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnProfilingGroup.ChannelProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb128be2e7cd15970dee2ea394d635c967fffc05335b5468f285d71eb7972df8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cda9ac694cf4a0730ba8c58dcc623c74646a296072486d91f42a1051fefcfef7(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__811cebbf9ff71c6cdc0a3e6f6073b243f3749069770de9b6715845db6a859300(
    *,
    principals: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__897f8a8de60bab360ab0a19378aece0020e93e34fe48060c6e6eca85b77617e3(
    *,
    channel_uri: builtins.str,
    channel_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0311e48a474ca90384078ca3a0759f5a58ab45163d3da706301f20c5207756e(
    *,
    profiling_group_name: builtins.str,
    agent_permissions: typing.Any = None,
    anomaly_detection_notification_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnProfilingGroup.ChannelProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    compute_platform: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8eef65bccc91bd6f83597064fade053f490648802b0350f9227188dc1487b758(
    grantee: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fad88677a83439824b5289f835fd0b41a038abaadbb21252ece4a01a245e1033(
    grantee: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__455d9f8e0fda8271257c6c1025ea87ea065d36bfefe7d63f702c45b526cc1976(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    compute_platform: typing.Optional[ComputePlatform] = None,
    profiling_group_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b91b6e9dff0c314a77924dad57869cdc71781e124518a42fbbb57612c6f29d4b(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    profiling_group_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__833a9e7894a97394ac1565daa3d417cd81e363776254c84ac034b459e478c491(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    profiling_group_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18fa54053affb91d59e1ada2098754620fc3f0b31a3be3a82e08a29b665655f4(
    grantee: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23cf99a24a4b56d46b427eae23b846bdf8f4365553fa7bd0efc8267f78934894(
    grantee: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4843108164af294aabe875088a5b93297a7983cba8b4e8af4a9bcae0fb6659c(
    *,
    compute_platform: typing.Optional[ComputePlatform] = None,
    profiling_group_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
