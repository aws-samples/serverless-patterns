'''
# AWS::MediaConvert Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_mediaconvert as mediaconvert
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for MediaConvert construct libraries](https://constructs.dev/search?q=mediaconvert)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::MediaConvert resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_MediaConvert.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::MediaConvert](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_MediaConvert.html).

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
class CfnJobTemplate(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_mediaconvert.CfnJobTemplate",
):
    '''The AWS::MediaConvert::JobTemplate resource is an AWS Elemental MediaConvert resource type that you can use to generate transcoding jobs.

    When you declare this entity in your AWS CloudFormation template, you pass in your transcoding job settings in JSON or YAML format. This settings specification must be formed in a particular way that conforms to AWS Elemental MediaConvert job validation. For more information about creating a job template model for the ``SettingsJson`` property, see the Remarks section later in this topic.

    For information about job templates, see `Working with AWS Elemental MediaConvert Job Templates <https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-job-templates.html>`_ in the ** .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-jobtemplate.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_mediaconvert as mediaconvert
        
        # settings_json: Any
        # tags: Any
        
        cfn_job_template = mediaconvert.CfnJobTemplate(self, "MyCfnJobTemplate",
            settings_json=settings_json,
        
            # the properties below are optional
            acceleration_settings=mediaconvert.CfnJobTemplate.AccelerationSettingsProperty(
                mode="mode"
            ),
            category="category",
            description="description",
            hop_destinations=[mediaconvert.CfnJobTemplate.HopDestinationProperty(
                priority=123,
                queue="queue",
                wait_minutes=123
            )],
            name="name",
            priority=123,
            queue="queue",
            status_update_interval="statusUpdateInterval",
            tags=tags
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        settings_json: typing.Any,
        acceleration_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnJobTemplate.AccelerationSettingsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        category: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        hop_destinations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnJobTemplate.HopDestinationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        name: typing.Optional[builtins.str] = None,
        priority: typing.Optional[jsii.Number] = None,
        queue: typing.Optional[builtins.str] = None,
        status_update_interval: typing.Optional[builtins.str] = None,
        tags: typing.Any = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param settings_json: Specify, in JSON format, the transcoding job settings for this job template. This specification must conform to the AWS Elemental MediaConvert job validation. For information about forming this specification, see the Remarks section later in this topic. For more information about MediaConvert job templates, see `Working with AWS Elemental MediaConvert Job Templates <https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-job-templates.html>`_ in the ** .
        :param acceleration_settings: Accelerated transcoding can significantly speed up jobs with long, visually complex content. Outputs that use this feature incur pro-tier pricing. For information about feature limitations, For more information, see `Job Limitations for Accelerated Transcoding in AWS Elemental MediaConvert <https://docs.aws.amazon.com/mediaconvert/latest/ug/job-requirements.html>`_ in the *AWS Elemental MediaConvert User Guide* .
        :param category: Optional. A category for the job template you are creating
        :param description: Optional. A description of the job template you are creating.
        :param hop_destinations: Optional. Configuration for a destination queue to which the job can hop once a customer-defined minimum wait time has passed. For more information, see `Setting Up Queue Hopping to Avoid Long Waits <https://docs.aws.amazon.com/mediaconvert/latest/ug/setting-up-queue-hopping-to-avoid-long-waits.html>`_ in the *AWS Elemental MediaConvert User Guide* .
        :param name: The name of the job template you are creating.
        :param priority: Specify the relative priority for this job. In any given queue, the service begins processing the job with the highest value first. When more than one job has the same priority, the service begins processing the job that you submitted first. If you don't specify a priority, the service uses the default value 0. Minimum: -50 Maximum: 50
        :param queue: Optional. The queue that jobs created from this template are assigned to. Specify the Amazon Resource Name (ARN) of the queue. For example, arn:aws:mediaconvert:us-west-2:505474453218:queues/Default. If you don't specify this, jobs will go to the default queue.
        :param status_update_interval: Specify how often MediaConvert sends STATUS_UPDATE events to Amazon CloudWatch Events. Set the interval, in seconds, between status updates. MediaConvert sends an update at this interval from the time the service begins processing your job to the time it completes the transcode or encounters an error. Specify one of the following enums: SECONDS_10 SECONDS_12 SECONDS_15 SECONDS_20 SECONDS_30 SECONDS_60 SECONDS_120 SECONDS_180 SECONDS_240 SECONDS_300 SECONDS_360 SECONDS_420 SECONDS_480 SECONDS_540 SECONDS_600
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6069a4448c0af7d940ed2037ac3ca32f293c46dc85314fc300ccf64aa573c06e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnJobTemplateProps(
            settings_json=settings_json,
            acceleration_settings=acceleration_settings,
            category=category,
            description=description,
            hop_destinations=hop_destinations,
            name=name,
            priority=priority,
            queue=queue,
            status_update_interval=status_update_interval,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8f5895955d49b09751b4fb43700086c0c6f207fe9b5fcb5d23033da6657c979)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1ad73f75b8da14e8668b904177606346b0c9ece117fa65fbe3945c2e37323559)
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
        '''The Amazon Resource Name (ARN) of the job template, such as ``arn:aws:mediaconvert:us-west-2:123456789012`` .

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
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> builtins.str:
        '''The name of the job template, such as ``Streaming stack DASH`` .

        :cloudformationAttribute: Name
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrName"))

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
    @jsii.member(jsii_name="settingsJson")
    def settings_json(self) -> typing.Any:
        '''Specify, in JSON format, the transcoding job settings for this job template.'''
        return typing.cast(typing.Any, jsii.get(self, "settingsJson"))

    @settings_json.setter
    def settings_json(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e6db6646d87945ef34e2e03c7b1efcd1666e1928a1f124f94694a92e717301e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "settingsJson", value)

    @builtins.property
    @jsii.member(jsii_name="accelerationSettings")
    def acceleration_settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnJobTemplate.AccelerationSettingsProperty"]]:
        '''Accelerated transcoding can significantly speed up jobs with long, visually complex content.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnJobTemplate.AccelerationSettingsProperty"]], jsii.get(self, "accelerationSettings"))

    @acceleration_settings.setter
    def acceleration_settings(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnJobTemplate.AccelerationSettingsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__296e89e4fb7eab6d9c3e9ffb503c8e7d494b915aaf6ffbeb356846e5b1550dce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accelerationSettings", value)

    @builtins.property
    @jsii.member(jsii_name="category")
    def category(self) -> typing.Optional[builtins.str]:
        '''Optional.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "category"))

    @category.setter
    def category(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6095b41f6b841d7de23758c4cfbb980b07b9f13c80a19eaba6ce4cb684801138)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "category", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''Optional.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad608e45172465d082cca6fda5cb45f46b8e4c24a10cc48ce5e66f5cdf31de04)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="hopDestinations")
    def hop_destinations(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnJobTemplate.HopDestinationProperty"]]]]:
        '''Optional.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnJobTemplate.HopDestinationProperty"]]]], jsii.get(self, "hopDestinations"))

    @hop_destinations.setter
    def hop_destinations(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnJobTemplate.HopDestinationProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d0fbb738f4409f521b0e8bc0586e0749bf26afe3de32a968ad27dd11e7b4fbf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hopDestinations", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the job template you are creating.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1fc4f350531fbb055c67bb24d69f0b90cf0af1a38ab15fc697b8366b45b11cd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> typing.Optional[jsii.Number]:
        '''Specify the relative priority for this job.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3857d89372a6fa395bbb9853843690578b7b6cae11814baed484c6fc8ad08938)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="queue")
    def queue(self) -> typing.Optional[builtins.str]:
        '''Optional.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queue"))

    @queue.setter
    def queue(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38320802a437cf0443d85acae426f6340d11d937df74fc400e5b5c7ed14b4d29)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queue", value)

    @builtins.property
    @jsii.member(jsii_name="statusUpdateInterval")
    def status_update_interval(self) -> typing.Optional[builtins.str]:
        '''Specify how often MediaConvert sends STATUS_UPDATE events to Amazon CloudWatch Events.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statusUpdateInterval"))

    @status_update_interval.setter
    def status_update_interval(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7ec7ad96104e4f7c1074d1d53806893f862c74346b89d72958e599f9b3bf47c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "statusUpdateInterval", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Any:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Any, jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e9ca8d435904ee086f90ed7c439c2d0e200a1d4d453bc42112e7fd9ef7aeff2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconvert.CfnJobTemplate.AccelerationSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"mode": "mode"},
    )
    class AccelerationSettingsProperty:
        def __init__(self, *, mode: builtins.str) -> None:
            '''Accelerated transcoding can significantly speed up jobs with long, visually complex content.

            Outputs that use this feature incur pro-tier pricing. For information about feature limitations, For more information, see `Job Limitations for Accelerated Transcoding in AWS Elemental MediaConvert <https://docs.aws.amazon.com/mediaconvert/latest/ug/job-requirements.html>`_ in the *AWS Elemental MediaConvert User Guide* .

            :param mode: Specify the conditions when the service will run your job with accelerated transcoding.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconvert-jobtemplate-accelerationsettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconvert as mediaconvert
                
                acceleration_settings_property = mediaconvert.CfnJobTemplate.AccelerationSettingsProperty(
                    mode="mode"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8f54269f0b30388de6a173382a5295a5105a846a1d29caf99299d166e2d8d450)
                check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "mode": mode,
            }

        @builtins.property
        def mode(self) -> builtins.str:
            '''Specify the conditions when the service will run your job with accelerated transcoding.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconvert-jobtemplate-accelerationsettings.html#cfn-mediaconvert-jobtemplate-accelerationsettings-mode
            '''
            result = self._values.get("mode")
            assert result is not None, "Required property 'mode' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AccelerationSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconvert.CfnJobTemplate.HopDestinationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "priority": "priority",
            "queue": "queue",
            "wait_minutes": "waitMinutes",
        },
    )
    class HopDestinationProperty:
        def __init__(
            self,
            *,
            priority: typing.Optional[jsii.Number] = None,
            queue: typing.Optional[builtins.str] = None,
            wait_minutes: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Optional.

            Configuration for a destination queue to which the job can hop once a customer-defined minimum wait time has passed. For more information, see `Setting Up Queue Hopping to Avoid Long Waits <https://docs.aws.amazon.com/mediaconvert/latest/ug/setting-up-queue-hopping-to-avoid-long-waits.html>`_ in the *AWS Elemental MediaConvert User Guide* .

            :param priority: Optional. When you set up a job to use queue hopping, you can specify a different relative priority for the job in the destination queue. If you don't specify, the relative priority will remain the same as in the previous queue.
            :param queue: Optional unless the job is submitted on the default queue. When you set up a job to use queue hopping, you can specify a destination queue. This queue cannot be the original queue to which the job is submitted. If the original queue isn't the default queue and you don't specify the destination queue, the job will move to the default queue.
            :param wait_minutes: Required for setting up a job to use queue hopping. Minimum wait time in minutes until the job can hop to the destination queue. Valid range is 1 to 4320 minutes, inclusive.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconvert-jobtemplate-hopdestination.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconvert as mediaconvert
                
                hop_destination_property = mediaconvert.CfnJobTemplate.HopDestinationProperty(
                    priority=123,
                    queue="queue",
                    wait_minutes=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__846cbb381389bc2995682d6266fbd2025526247b0442dfab6d6624ea1dedcad1)
                check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
                check_type(argname="argument queue", value=queue, expected_type=type_hints["queue"])
                check_type(argname="argument wait_minutes", value=wait_minutes, expected_type=type_hints["wait_minutes"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if priority is not None:
                self._values["priority"] = priority
            if queue is not None:
                self._values["queue"] = queue
            if wait_minutes is not None:
                self._values["wait_minutes"] = wait_minutes

        @builtins.property
        def priority(self) -> typing.Optional[jsii.Number]:
            '''Optional.

            When you set up a job to use queue hopping, you can specify a different relative priority for the job in the destination queue. If you don't specify, the relative priority will remain the same as in the previous queue.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconvert-jobtemplate-hopdestination.html#cfn-mediaconvert-jobtemplate-hopdestination-priority
            '''
            result = self._values.get("priority")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def queue(self) -> typing.Optional[builtins.str]:
            '''Optional unless the job is submitted on the default queue.

            When you set up a job to use queue hopping, you can specify a destination queue. This queue cannot be the original queue to which the job is submitted. If the original queue isn't the default queue and you don't specify the destination queue, the job will move to the default queue.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconvert-jobtemplate-hopdestination.html#cfn-mediaconvert-jobtemplate-hopdestination-queue
            '''
            result = self._values.get("queue")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def wait_minutes(self) -> typing.Optional[jsii.Number]:
            '''Required for setting up a job to use queue hopping.

            Minimum wait time in minutes until the job can hop to the destination queue. Valid range is 1 to 4320 minutes, inclusive.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconvert-jobtemplate-hopdestination.html#cfn-mediaconvert-jobtemplate-hopdestination-waitminutes
            '''
            result = self._values.get("wait_minutes")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HopDestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_mediaconvert.CfnJobTemplateProps",
    jsii_struct_bases=[],
    name_mapping={
        "settings_json": "settingsJson",
        "acceleration_settings": "accelerationSettings",
        "category": "category",
        "description": "description",
        "hop_destinations": "hopDestinations",
        "name": "name",
        "priority": "priority",
        "queue": "queue",
        "status_update_interval": "statusUpdateInterval",
        "tags": "tags",
    },
)
class CfnJobTemplateProps:
    def __init__(
        self,
        *,
        settings_json: typing.Any,
        acceleration_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnJobTemplate.AccelerationSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        category: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        hop_destinations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnJobTemplate.HopDestinationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        name: typing.Optional[builtins.str] = None,
        priority: typing.Optional[jsii.Number] = None,
        queue: typing.Optional[builtins.str] = None,
        status_update_interval: typing.Optional[builtins.str] = None,
        tags: typing.Any = None,
    ) -> None:
        '''Properties for defining a ``CfnJobTemplate``.

        :param settings_json: Specify, in JSON format, the transcoding job settings for this job template. This specification must conform to the AWS Elemental MediaConvert job validation. For information about forming this specification, see the Remarks section later in this topic. For more information about MediaConvert job templates, see `Working with AWS Elemental MediaConvert Job Templates <https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-job-templates.html>`_ in the ** .
        :param acceleration_settings: Accelerated transcoding can significantly speed up jobs with long, visually complex content. Outputs that use this feature incur pro-tier pricing. For information about feature limitations, For more information, see `Job Limitations for Accelerated Transcoding in AWS Elemental MediaConvert <https://docs.aws.amazon.com/mediaconvert/latest/ug/job-requirements.html>`_ in the *AWS Elemental MediaConvert User Guide* .
        :param category: Optional. A category for the job template you are creating
        :param description: Optional. A description of the job template you are creating.
        :param hop_destinations: Optional. Configuration for a destination queue to which the job can hop once a customer-defined minimum wait time has passed. For more information, see `Setting Up Queue Hopping to Avoid Long Waits <https://docs.aws.amazon.com/mediaconvert/latest/ug/setting-up-queue-hopping-to-avoid-long-waits.html>`_ in the *AWS Elemental MediaConvert User Guide* .
        :param name: The name of the job template you are creating.
        :param priority: Specify the relative priority for this job. In any given queue, the service begins processing the job with the highest value first. When more than one job has the same priority, the service begins processing the job that you submitted first. If you don't specify a priority, the service uses the default value 0. Minimum: -50 Maximum: 50
        :param queue: Optional. The queue that jobs created from this template are assigned to. Specify the Amazon Resource Name (ARN) of the queue. For example, arn:aws:mediaconvert:us-west-2:505474453218:queues/Default. If you don't specify this, jobs will go to the default queue.
        :param status_update_interval: Specify how often MediaConvert sends STATUS_UPDATE events to Amazon CloudWatch Events. Set the interval, in seconds, between status updates. MediaConvert sends an update at this interval from the time the service begins processing your job to the time it completes the transcode or encounters an error. Specify one of the following enums: SECONDS_10 SECONDS_12 SECONDS_15 SECONDS_20 SECONDS_30 SECONDS_60 SECONDS_120 SECONDS_180 SECONDS_240 SECONDS_300 SECONDS_360 SECONDS_420 SECONDS_480 SECONDS_540 SECONDS_600
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-jobtemplate.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_mediaconvert as mediaconvert
            
            # settings_json: Any
            # tags: Any
            
            cfn_job_template_props = mediaconvert.CfnJobTemplateProps(
                settings_json=settings_json,
            
                # the properties below are optional
                acceleration_settings=mediaconvert.CfnJobTemplate.AccelerationSettingsProperty(
                    mode="mode"
                ),
                category="category",
                description="description",
                hop_destinations=[mediaconvert.CfnJobTemplate.HopDestinationProperty(
                    priority=123,
                    queue="queue",
                    wait_minutes=123
                )],
                name="name",
                priority=123,
                queue="queue",
                status_update_interval="statusUpdateInterval",
                tags=tags
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2efc4500b40d93a1910ad093dd5e6c1a674296bd8209fe51b39cf44ca3625a9)
            check_type(argname="argument settings_json", value=settings_json, expected_type=type_hints["settings_json"])
            check_type(argname="argument acceleration_settings", value=acceleration_settings, expected_type=type_hints["acceleration_settings"])
            check_type(argname="argument category", value=category, expected_type=type_hints["category"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument hop_destinations", value=hop_destinations, expected_type=type_hints["hop_destinations"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument queue", value=queue, expected_type=type_hints["queue"])
            check_type(argname="argument status_update_interval", value=status_update_interval, expected_type=type_hints["status_update_interval"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "settings_json": settings_json,
        }
        if acceleration_settings is not None:
            self._values["acceleration_settings"] = acceleration_settings
        if category is not None:
            self._values["category"] = category
        if description is not None:
            self._values["description"] = description
        if hop_destinations is not None:
            self._values["hop_destinations"] = hop_destinations
        if name is not None:
            self._values["name"] = name
        if priority is not None:
            self._values["priority"] = priority
        if queue is not None:
            self._values["queue"] = queue
        if status_update_interval is not None:
            self._values["status_update_interval"] = status_update_interval
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def settings_json(self) -> typing.Any:
        '''Specify, in JSON format, the transcoding job settings for this job template.

        This specification must conform to the AWS Elemental MediaConvert job validation. For information about forming this specification, see the Remarks section later in this topic.

        For more information about MediaConvert job templates, see `Working with AWS Elemental MediaConvert Job Templates <https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-job-templates.html>`_ in the ** .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-jobtemplate.html#cfn-mediaconvert-jobtemplate-settingsjson
        '''
        result = self._values.get("settings_json")
        assert result is not None, "Required property 'settings_json' is missing"
        return typing.cast(typing.Any, result)

    @builtins.property
    def acceleration_settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnJobTemplate.AccelerationSettingsProperty]]:
        '''Accelerated transcoding can significantly speed up jobs with long, visually complex content.

        Outputs that use this feature incur pro-tier pricing. For information about feature limitations, For more information, see `Job Limitations for Accelerated Transcoding in AWS Elemental MediaConvert <https://docs.aws.amazon.com/mediaconvert/latest/ug/job-requirements.html>`_ in the *AWS Elemental MediaConvert User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-jobtemplate.html#cfn-mediaconvert-jobtemplate-accelerationsettings
        '''
        result = self._values.get("acceleration_settings")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnJobTemplate.AccelerationSettingsProperty]], result)

    @builtins.property
    def category(self) -> typing.Optional[builtins.str]:
        '''Optional.

        A category for the job template you are creating

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-jobtemplate.html#cfn-mediaconvert-jobtemplate-category
        '''
        result = self._values.get("category")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Optional.

        A description of the job template you are creating.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-jobtemplate.html#cfn-mediaconvert-jobtemplate-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def hop_destinations(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnJobTemplate.HopDestinationProperty]]]]:
        '''Optional.

        Configuration for a destination queue to which the job can hop once a customer-defined minimum wait time has passed. For more information, see `Setting Up Queue Hopping to Avoid Long Waits <https://docs.aws.amazon.com/mediaconvert/latest/ug/setting-up-queue-hopping-to-avoid-long-waits.html>`_ in the *AWS Elemental MediaConvert User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-jobtemplate.html#cfn-mediaconvert-jobtemplate-hopdestinations
        '''
        result = self._values.get("hop_destinations")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnJobTemplate.HopDestinationProperty]]]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the job template you are creating.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-jobtemplate.html#cfn-mediaconvert-jobtemplate-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def priority(self) -> typing.Optional[jsii.Number]:
        '''Specify the relative priority for this job.

        In any given queue, the service begins processing the job with the highest value first. When more than one job has the same priority, the service begins processing the job that you submitted first. If you don't specify a priority, the service uses the default value 0. Minimum: -50 Maximum: 50

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-jobtemplate.html#cfn-mediaconvert-jobtemplate-priority
        '''
        result = self._values.get("priority")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def queue(self) -> typing.Optional[builtins.str]:
        '''Optional.

        The queue that jobs created from this template are assigned to. Specify the Amazon Resource Name (ARN) of the queue. For example, arn:aws:mediaconvert:us-west-2:505474453218:queues/Default. If you don't specify this, jobs will go to the default queue.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-jobtemplate.html#cfn-mediaconvert-jobtemplate-queue
        '''
        result = self._values.get("queue")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status_update_interval(self) -> typing.Optional[builtins.str]:
        '''Specify how often MediaConvert sends STATUS_UPDATE events to Amazon CloudWatch Events.

        Set the interval, in seconds, between status updates. MediaConvert sends an update at this interval from the time the service begins processing your job to the time it completes the transcode or encounters an error.

        Specify one of the following enums:

        SECONDS_10

        SECONDS_12

        SECONDS_15

        SECONDS_20

        SECONDS_30

        SECONDS_60

        SECONDS_120

        SECONDS_180

        SECONDS_240

        SECONDS_300

        SECONDS_360

        SECONDS_420

        SECONDS_480

        SECONDS_540

        SECONDS_600

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-jobtemplate.html#cfn-mediaconvert-jobtemplate-statusupdateinterval
        '''
        result = self._values.get("status_update_interval")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Any:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-jobtemplate.html#cfn-mediaconvert-jobtemplate-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnJobTemplateProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnPreset(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_mediaconvert.CfnPreset",
):
    '''The AWS::MediaConvert::Preset resource is an AWS Elemental MediaConvert resource type that you can use to specify encoding settings for a single output in a transcoding job.

    When you declare this entity in your AWS CloudFormation template, you pass in your transcoding job settings in JSON or YAML format. This settings specification must be formed in a particular way that conforms to AWS Elemental MediaConvert job validation. For more information about creating an output preset model for the ``SettingsJson`` property, see the Remarks section later in this topic.

    For more information about output MediaConvert presets, see `Working with AWS Elemental MediaConvert Output Presets <https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-presets.html>`_ in the ** .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-preset.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_mediaconvert as mediaconvert
        
        # settings_json: Any
        # tags: Any
        
        cfn_preset = mediaconvert.CfnPreset(self, "MyCfnPreset",
            settings_json=settings_json,
        
            # the properties below are optional
            category="category",
            description="description",
            name="name",
            tags=tags
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        settings_json: typing.Any,
        category: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Any = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param settings_json: Specify, in JSON format, the transcoding job settings for this output preset. This specification must conform to the AWS Elemental MediaConvert job validation. For information about forming this specification, see the Remarks section later in this topic. For more information about MediaConvert output presets, see `Working with AWS Elemental MediaConvert Output Presets <https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-presets.html>`_ in the ** .
        :param category: The new category for the preset, if you are changing it.
        :param description: The new description for the preset, if you are changing it.
        :param name: The name of the preset that you are modifying.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7e9a02a55f71ce4dc1d1bd91234e42ae8b4f331a5204d9de2337abf478f6742)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPresetProps(
            settings_json=settings_json,
            category=category,
            description=description,
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
            type_hints = typing.get_type_hints(_typecheckingstub__cfdd12e2c70eaa4ee51ce8c0175f9e9a23741111e6220d5d757029b1f4107fa5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__29f0f92cec59e5e0767a2d876973de8cdf8e0c2615c8ffe28a990ecf9773cac0)
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
        '''The Amazon Resource Name (ARN) of the output preset, such as ``arn:aws:mediaconvert:us-west-2:123456789012`` .

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
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> builtins.str:
        '''The name of the output preset, such as ``HEVC high res`` .

        :cloudformationAttribute: Name
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrName"))

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
    @jsii.member(jsii_name="settingsJson")
    def settings_json(self) -> typing.Any:
        '''Specify, in JSON format, the transcoding job settings for this output preset.'''
        return typing.cast(typing.Any, jsii.get(self, "settingsJson"))

    @settings_json.setter
    def settings_json(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__896f46fb2b42116c3b9470123dec62b22cfd06c04c5bcbb998592a5d3a201e15)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "settingsJson", value)

    @builtins.property
    @jsii.member(jsii_name="category")
    def category(self) -> typing.Optional[builtins.str]:
        '''The new category for the preset, if you are changing it.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "category"))

    @category.setter
    def category(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7416b46e5f0f9cea5c961f17373253f1be2553f7983af31716026cb07ec40daa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "category", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The new description for the preset, if you are changing it.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6edaf93908a0193523b483e749d20ba3928b5255280ab8214729a4e86b108a04)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the preset that you are modifying.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f5cfa13481ef470c412166b972128fb907f80e1f74bfc400f30cd3339e066f4a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Any:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Any, jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f864101d79755967bf3e44fcc09e5237c08ff95f64c10eba5fa4da31c26dbe0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_mediaconvert.CfnPresetProps",
    jsii_struct_bases=[],
    name_mapping={
        "settings_json": "settingsJson",
        "category": "category",
        "description": "description",
        "name": "name",
        "tags": "tags",
    },
)
class CfnPresetProps:
    def __init__(
        self,
        *,
        settings_json: typing.Any,
        category: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Any = None,
    ) -> None:
        '''Properties for defining a ``CfnPreset``.

        :param settings_json: Specify, in JSON format, the transcoding job settings for this output preset. This specification must conform to the AWS Elemental MediaConvert job validation. For information about forming this specification, see the Remarks section later in this topic. For more information about MediaConvert output presets, see `Working with AWS Elemental MediaConvert Output Presets <https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-presets.html>`_ in the ** .
        :param category: The new category for the preset, if you are changing it.
        :param description: The new description for the preset, if you are changing it.
        :param name: The name of the preset that you are modifying.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-preset.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_mediaconvert as mediaconvert
            
            # settings_json: Any
            # tags: Any
            
            cfn_preset_props = mediaconvert.CfnPresetProps(
                settings_json=settings_json,
            
                # the properties below are optional
                category="category",
                description="description",
                name="name",
                tags=tags
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b4217f886c99598fd3f7185ab1fa9e56680b21929b9e706d0add6a1a13efe28)
            check_type(argname="argument settings_json", value=settings_json, expected_type=type_hints["settings_json"])
            check_type(argname="argument category", value=category, expected_type=type_hints["category"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "settings_json": settings_json,
        }
        if category is not None:
            self._values["category"] = category
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def settings_json(self) -> typing.Any:
        '''Specify, in JSON format, the transcoding job settings for this output preset.

        This specification must conform to the AWS Elemental MediaConvert job validation. For information about forming this specification, see the Remarks section later in this topic.

        For more information about MediaConvert output presets, see `Working with AWS Elemental MediaConvert Output Presets <https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-presets.html>`_ in the ** .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-preset.html#cfn-mediaconvert-preset-settingsjson
        '''
        result = self._values.get("settings_json")
        assert result is not None, "Required property 'settings_json' is missing"
        return typing.cast(typing.Any, result)

    @builtins.property
    def category(self) -> typing.Optional[builtins.str]:
        '''The new category for the preset, if you are changing it.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-preset.html#cfn-mediaconvert-preset-category
        '''
        result = self._values.get("category")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The new description for the preset, if you are changing it.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-preset.html#cfn-mediaconvert-preset-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the preset that you are modifying.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-preset.html#cfn-mediaconvert-preset-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Any:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-preset.html#cfn-mediaconvert-preset-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPresetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnQueue(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_mediaconvert.CfnQueue",
):
    '''The AWS::MediaConvert::Queue resource is an AWS Elemental MediaConvert resource type that you can use to manage the resources that are available to your account for parallel processing of jobs.

    For more information about queues, see `Working with AWS Elemental MediaConvert Queues <https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-queues.html>`_ in the ** .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-queue.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_mediaconvert as mediaconvert
        
        # tags: Any
        
        cfn_queue = mediaconvert.CfnQueue(self, "MyCfnQueue",
            description="description",
            name="name",
            pricing_plan="pricingPlan",
            status="status",
            tags=tags
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        pricing_plan: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
        tags: typing.Any = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param description: Optional. A description of the queue that you are creating.
        :param name: The name of the queue that you are creating.
        :param pricing_plan: When you use AWS CloudFormation , you can create only on-demand queues. Therefore, always set ``PricingPlan`` to the value "ON_DEMAND" when declaring an AWS::MediaConvert::Queue in your AWS CloudFormation template. To create a reserved queue, use the AWS Elemental MediaConvert console at https://console.aws.amazon.com/mediaconvert to set up a contract. For more information, see `Working with AWS Elemental MediaConvert Queues <https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-queues.html>`_ in the ** .
        :param status: Initial state of the queue. Queues can be either ACTIVE or PAUSED. If you create a paused queue, then jobs that you send to that queue won't begin.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce85d095c93254b82e67ee70a5cae96a78ca7b1fbb86f6494f48602d8a586d98)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnQueueProps(
            description=description,
            name=name,
            pricing_plan=pricing_plan,
            status=status,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44bf2af7e922fe606b4e888de0517c75f280a99541185e941a3e92f997fc97e8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__35c318d1b3afa3029c00b3041ce2990e84ecd612460683bdfc3995e4ff1f1397)
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
        '''The Amazon Resource Name (ARN) of the queue, such as ``arn:aws:mediaconvert:us-west-2:123456789012`` .

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
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> builtins.str:
        '''The name of the queue, such as ``Queue 2`` .

        :cloudformationAttribute: Name
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrName"))

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
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''Optional.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e85c7cbaa4ed5f47efbb96c65b1b5f493c2811227a36b5f2af1c323b91af1598)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the queue that you are creating.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd8d8c3dde443d166f24457acfce6e106f213d1607655d8d767e1db9afc13094)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="pricingPlan")
    def pricing_plan(self) -> typing.Optional[builtins.str]:
        '''When you use AWS CloudFormation , you can create only on-demand queues.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pricingPlan"))

    @pricing_plan.setter
    def pricing_plan(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__544728ca404947ab22b89e6afbdd2fe9562a7e292914ea684ded3f462fd1a7d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pricingPlan", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> typing.Optional[builtins.str]:
        '''Initial state of the queue.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "status"))

    @status.setter
    def status(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85fd14d7b664ec173f54ec0449201dc6c6f6738e85506a3f02565bad2b42761b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Any:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Any, jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f40a2466cbcd54418fd8402f9b79ae297cbdc53819c461dd9bde5aa9f01859d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_mediaconvert.CfnQueueProps",
    jsii_struct_bases=[],
    name_mapping={
        "description": "description",
        "name": "name",
        "pricing_plan": "pricingPlan",
        "status": "status",
        "tags": "tags",
    },
)
class CfnQueueProps:
    def __init__(
        self,
        *,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        pricing_plan: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
        tags: typing.Any = None,
    ) -> None:
        '''Properties for defining a ``CfnQueue``.

        :param description: Optional. A description of the queue that you are creating.
        :param name: The name of the queue that you are creating.
        :param pricing_plan: When you use AWS CloudFormation , you can create only on-demand queues. Therefore, always set ``PricingPlan`` to the value "ON_DEMAND" when declaring an AWS::MediaConvert::Queue in your AWS CloudFormation template. To create a reserved queue, use the AWS Elemental MediaConvert console at https://console.aws.amazon.com/mediaconvert to set up a contract. For more information, see `Working with AWS Elemental MediaConvert Queues <https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-queues.html>`_ in the ** .
        :param status: Initial state of the queue. Queues can be either ACTIVE or PAUSED. If you create a paused queue, then jobs that you send to that queue won't begin.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-queue.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_mediaconvert as mediaconvert
            
            # tags: Any
            
            cfn_queue_props = mediaconvert.CfnQueueProps(
                description="description",
                name="name",
                pricing_plan="pricingPlan",
                status="status",
                tags=tags
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7730e4d3d27bc8cf5ac3d6866a9c8915fd8e55a6c574e02bd2a03f4318d68f05)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument pricing_plan", value=pricing_plan, expected_type=type_hints["pricing_plan"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name
        if pricing_plan is not None:
            self._values["pricing_plan"] = pricing_plan
        if status is not None:
            self._values["status"] = status
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Optional.

        A description of the queue that you are creating.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-queue.html#cfn-mediaconvert-queue-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the queue that you are creating.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-queue.html#cfn-mediaconvert-queue-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pricing_plan(self) -> typing.Optional[builtins.str]:
        '''When you use AWS CloudFormation , you can create only on-demand queues.

        Therefore, always set ``PricingPlan`` to the value "ON_DEMAND" when declaring an AWS::MediaConvert::Queue in your AWS CloudFormation template.

        To create a reserved queue, use the AWS Elemental MediaConvert console at https://console.aws.amazon.com/mediaconvert to set up a contract. For more information, see `Working with AWS Elemental MediaConvert Queues <https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-queues.html>`_ in the ** .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-queue.html#cfn-mediaconvert-queue-pricingplan
        '''
        result = self._values.get("pricing_plan")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''Initial state of the queue.

        Queues can be either ACTIVE or PAUSED. If you create a paused queue, then jobs that you send to that queue won't begin.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-queue.html#cfn-mediaconvert-queue-status
        '''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Any:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-queue.html#cfn-mediaconvert-queue-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQueueProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnJobTemplate",
    "CfnJobTemplateProps",
    "CfnPreset",
    "CfnPresetProps",
    "CfnQueue",
    "CfnQueueProps",
]

publication.publish()

def _typecheckingstub__6069a4448c0af7d940ed2037ac3ca32f293c46dc85314fc300ccf64aa573c06e(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    settings_json: typing.Any,
    acceleration_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnJobTemplate.AccelerationSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    category: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    hop_destinations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnJobTemplate.HopDestinationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    name: typing.Optional[builtins.str] = None,
    priority: typing.Optional[jsii.Number] = None,
    queue: typing.Optional[builtins.str] = None,
    status_update_interval: typing.Optional[builtins.str] = None,
    tags: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8f5895955d49b09751b4fb43700086c0c6f207fe9b5fcb5d23033da6657c979(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ad73f75b8da14e8668b904177606346b0c9ece117fa65fbe3945c2e37323559(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e6db6646d87945ef34e2e03c7b1efcd1666e1928a1f124f94694a92e717301e(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__296e89e4fb7eab6d9c3e9ffb503c8e7d494b915aaf6ffbeb356846e5b1550dce(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnJobTemplate.AccelerationSettingsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6095b41f6b841d7de23758c4cfbb980b07b9f13c80a19eaba6ce4cb684801138(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad608e45172465d082cca6fda5cb45f46b8e4c24a10cc48ce5e66f5cdf31de04(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d0fbb738f4409f521b0e8bc0586e0749bf26afe3de32a968ad27dd11e7b4fbf(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnJobTemplate.HopDestinationProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1fc4f350531fbb055c67bb24d69f0b90cf0af1a38ab15fc697b8366b45b11cd(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3857d89372a6fa395bbb9853843690578b7b6cae11814baed484c6fc8ad08938(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38320802a437cf0443d85acae426f6340d11d937df74fc400e5b5c7ed14b4d29(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7ec7ad96104e4f7c1074d1d53806893f862c74346b89d72958e599f9b3bf47c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e9ca8d435904ee086f90ed7c439c2d0e200a1d4d453bc42112e7fd9ef7aeff2(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f54269f0b30388de6a173382a5295a5105a846a1d29caf99299d166e2d8d450(
    *,
    mode: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__846cbb381389bc2995682d6266fbd2025526247b0442dfab6d6624ea1dedcad1(
    *,
    priority: typing.Optional[jsii.Number] = None,
    queue: typing.Optional[builtins.str] = None,
    wait_minutes: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2efc4500b40d93a1910ad093dd5e6c1a674296bd8209fe51b39cf44ca3625a9(
    *,
    settings_json: typing.Any,
    acceleration_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnJobTemplate.AccelerationSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    category: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    hop_destinations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnJobTemplate.HopDestinationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    name: typing.Optional[builtins.str] = None,
    priority: typing.Optional[jsii.Number] = None,
    queue: typing.Optional[builtins.str] = None,
    status_update_interval: typing.Optional[builtins.str] = None,
    tags: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7e9a02a55f71ce4dc1d1bd91234e42ae8b4f331a5204d9de2337abf478f6742(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    settings_json: typing.Any,
    category: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfdd12e2c70eaa4ee51ce8c0175f9e9a23741111e6220d5d757029b1f4107fa5(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29f0f92cec59e5e0767a2d876973de8cdf8e0c2615c8ffe28a990ecf9773cac0(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__896f46fb2b42116c3b9470123dec62b22cfd06c04c5bcbb998592a5d3a201e15(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7416b46e5f0f9cea5c961f17373253f1be2553f7983af31716026cb07ec40daa(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6edaf93908a0193523b483e749d20ba3928b5255280ab8214729a4e86b108a04(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5cfa13481ef470c412166b972128fb907f80e1f74bfc400f30cd3339e066f4a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f864101d79755967bf3e44fcc09e5237c08ff95f64c10eba5fa4da31c26dbe0(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b4217f886c99598fd3f7185ab1fa9e56680b21929b9e706d0add6a1a13efe28(
    *,
    settings_json: typing.Any,
    category: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce85d095c93254b82e67ee70a5cae96a78ca7b1fbb86f6494f48602d8a586d98(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    pricing_plan: typing.Optional[builtins.str] = None,
    status: typing.Optional[builtins.str] = None,
    tags: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44bf2af7e922fe606b4e888de0517c75f280a99541185e941a3e92f997fc97e8(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35c318d1b3afa3029c00b3041ce2990e84ecd612460683bdfc3995e4ff1f1397(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e85c7cbaa4ed5f47efbb96c65b1b5f493c2811227a36b5f2af1c323b91af1598(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd8d8c3dde443d166f24457acfce6e106f213d1607655d8d767e1db9afc13094(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__544728ca404947ab22b89e6afbdd2fe9562a7e292914ea684ded3f462fd1a7d0(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85fd14d7b664ec173f54ec0449201dc6c6f6738e85506a3f02565bad2b42761b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f40a2466cbcd54418fd8402f9b79ae297cbdc53819c461dd9bde5aa9f01859d(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7730e4d3d27bc8cf5ac3d6866a9c8915fd8e55a6c574e02bd2a03f4318d68f05(
    *,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    pricing_plan: typing.Optional[builtins.str] = None,
    status: typing.Optional[builtins.str] = None,
    tags: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass
