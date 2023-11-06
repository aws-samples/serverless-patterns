'''
# AWS::SSMContacts Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_ssmcontacts as ssmcontacts
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for SSMContacts construct libraries](https://constructs.dev/search?q=ssmcontacts)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::SSMContacts resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_SSMContacts.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::SSMContacts](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_SSMContacts.html).

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


@jsii.implements(_IInspectable_c2943556)
class CfnContact(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ssmcontacts.CfnContact",
):
    '''The ``AWS::SSMContacts::Contact`` resource specifies a contact or escalation plan.

    Incident Manager contacts are a subset of actions and data types that you can use for managing responder engagement and interaction.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-contact.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ssmcontacts as ssmcontacts
        
        cfn_contact = ssmcontacts.CfnContact(self, "MyCfnContact",
            alias="alias",
            display_name="displayName",
            type="type",
        
            # the properties below are optional
            plan=[ssmcontacts.CfnContact.StageProperty(
                duration_in_minutes=123,
                rotation_ids=["rotationIds"],
                targets=[ssmcontacts.CfnContact.TargetsProperty(
                    channel_target_info=ssmcontacts.CfnContact.ChannelTargetInfoProperty(
                        channel_id="channelId",
                        retry_interval_in_minutes=123
                    ),
                    contact_target_info=ssmcontacts.CfnContact.ContactTargetInfoProperty(
                        contact_id="contactId",
                        is_essential=False
                    )
                )]
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        alias: builtins.str,
        display_name: builtins.str,
        type: builtins.str,
        plan: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnContact.StageProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param alias: The unique and identifiable alias of the contact or escalation plan.
        :param display_name: The full name of the contact or escalation plan.
        :param type: Refers to the type of contact:. - ``PERSONAL`` : A single, individual contact. - ``ESCALATION`` : An escalation plan. - ``ONCALL_SCHEDULE`` : An on-call schedule.
        :param plan: A list of stages. A contact has an engagement plan with stages that contact specified contact channels. An escalation plan uses stages that contact specified contacts.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96185056d36e15643884f48a931b8d7005ac84a62576223bb952c88328d7d90c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnContactProps(
            alias=alias, display_name=display_name, type=type, plan=plan
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d145b029ad2942410a46b8ef97eda343598f927706f2322d3e0ecae3a114269c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2b081f8848b9d4742d3d4a3b6aa1dbb241d062469b6ef8e173e25b21525f7a27)
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
        '''The Amazon Resource Name (ARN) of the ``Contact`` resource, such as ``arn:aws:ssm-contacts:us-west-2:123456789012:contact/contactalias`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="alias")
    def alias(self) -> builtins.str:
        '''The unique and identifiable alias of the contact or escalation plan.'''
        return typing.cast(builtins.str, jsii.get(self, "alias"))

    @alias.setter
    def alias(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4bba8290dd4eb067f8393c42927f143c8caf24ad18958b81d84a3b8407981a2c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alias", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        '''The full name of the contact or escalation plan.'''
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__55de424a70da49fdee77dff632e72d116d463a39a20c87708b14539025047922)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''Refers to the type of contact:.'''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa02d91e10d2171d1f6f9fba4357f22de345c2007b02d0535df28e85a09c5c89)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="plan")
    def plan(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnContact.StageProperty"]]]]:
        '''A list of stages.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnContact.StageProperty"]]]], jsii.get(self, "plan"))

    @plan.setter
    def plan(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnContact.StageProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b53265c2630d58664ca7f46c1ce619caeab6eec0dc5682af154a1d6e5fadc5b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "plan", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssmcontacts.CfnContact.ChannelTargetInfoProperty",
        jsii_struct_bases=[],
        name_mapping={
            "channel_id": "channelId",
            "retry_interval_in_minutes": "retryIntervalInMinutes",
        },
    )
    class ChannelTargetInfoProperty:
        def __init__(
            self,
            *,
            channel_id: builtins.str,
            retry_interval_in_minutes: jsii.Number,
        ) -> None:
            '''Information about the contact channel that Incident Manager uses to engage the contact.

            :param channel_id: The Amazon Resource Name (ARN) of the contact channel.
            :param retry_interval_in_minutes: The number of minutes to wait before retrying to send engagement if the engagement initially failed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-contact-channeltargetinfo.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssmcontacts as ssmcontacts
                
                channel_target_info_property = ssmcontacts.CfnContact.ChannelTargetInfoProperty(
                    channel_id="channelId",
                    retry_interval_in_minutes=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d9859de101893bc6eb79fa20a2bb897c167951655effac5d46a65e9ddbe0e527)
                check_type(argname="argument channel_id", value=channel_id, expected_type=type_hints["channel_id"])
                check_type(argname="argument retry_interval_in_minutes", value=retry_interval_in_minutes, expected_type=type_hints["retry_interval_in_minutes"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "channel_id": channel_id,
                "retry_interval_in_minutes": retry_interval_in_minutes,
            }

        @builtins.property
        def channel_id(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the contact channel.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-contact-channeltargetinfo.html#cfn-ssmcontacts-contact-channeltargetinfo-channelid
            '''
            result = self._values.get("channel_id")
            assert result is not None, "Required property 'channel_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def retry_interval_in_minutes(self) -> jsii.Number:
            '''The number of minutes to wait before retrying to send engagement if the engagement initially failed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-contact-channeltargetinfo.html#cfn-ssmcontacts-contact-channeltargetinfo-retryintervalinminutes
            '''
            result = self._values.get("retry_interval_in_minutes")
            assert result is not None, "Required property 'retry_interval_in_minutes' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ChannelTargetInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssmcontacts.CfnContact.ContactTargetInfoProperty",
        jsii_struct_bases=[],
        name_mapping={"contact_id": "contactId", "is_essential": "isEssential"},
    )
    class ContactTargetInfoProperty:
        def __init__(
            self,
            *,
            contact_id: builtins.str,
            is_essential: typing.Union[builtins.bool, _IResolvable_da3f097b],
        ) -> None:
            '''The contact that Incident Manager is engaging during an incident.

            :param contact_id: The Amazon Resource Name (ARN) of the contact.
            :param is_essential: A Boolean value determining if the contact's acknowledgement stops the progress of stages in the plan.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-contact-contacttargetinfo.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssmcontacts as ssmcontacts
                
                contact_target_info_property = ssmcontacts.CfnContact.ContactTargetInfoProperty(
                    contact_id="contactId",
                    is_essential=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d65e32e1631ab40569f09ec16aaa5d8215a382cf1eb5593a2f809b42ba4936ad)
                check_type(argname="argument contact_id", value=contact_id, expected_type=type_hints["contact_id"])
                check_type(argname="argument is_essential", value=is_essential, expected_type=type_hints["is_essential"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "contact_id": contact_id,
                "is_essential": is_essential,
            }

        @builtins.property
        def contact_id(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the contact.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-contact-contacttargetinfo.html#cfn-ssmcontacts-contact-contacttargetinfo-contactid
            '''
            result = self._values.get("contact_id")
            assert result is not None, "Required property 'contact_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def is_essential(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''A Boolean value determining if the contact's acknowledgement stops the progress of stages in the plan.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-contact-contacttargetinfo.html#cfn-ssmcontacts-contact-contacttargetinfo-isessential
            '''
            result = self._values.get("is_essential")
            assert result is not None, "Required property 'is_essential' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ContactTargetInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssmcontacts.CfnContact.StageProperty",
        jsii_struct_bases=[],
        name_mapping={
            "duration_in_minutes": "durationInMinutes",
            "rotation_ids": "rotationIds",
            "targets": "targets",
        },
    )
    class StageProperty:
        def __init__(
            self,
            *,
            duration_in_minutes: typing.Optional[jsii.Number] = None,
            rotation_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
            targets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnContact.TargetsProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''The ``Stage`` property type specifies a set amount of time that an escalation plan or engagement plan engages the specified contacts or contact methods.

            :param duration_in_minutes: The time to wait until beginning the next stage. The duration can only be set to 0 if a target is specified.
            :param rotation_ids: The Amazon Resource Names (ARNs) of the on-call rotations associated with the plan.
            :param targets: The contacts or contact methods that the escalation plan or engagement plan is engaging.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-contact-stage.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssmcontacts as ssmcontacts
                
                stage_property = ssmcontacts.CfnContact.StageProperty(
                    duration_in_minutes=123,
                    rotation_ids=["rotationIds"],
                    targets=[ssmcontacts.CfnContact.TargetsProperty(
                        channel_target_info=ssmcontacts.CfnContact.ChannelTargetInfoProperty(
                            channel_id="channelId",
                            retry_interval_in_minutes=123
                        ),
                        contact_target_info=ssmcontacts.CfnContact.ContactTargetInfoProperty(
                            contact_id="contactId",
                            is_essential=False
                        )
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8f305b28534efe8d339e08837352556855e9044627d7362d0ef784e32e9b4e6e)
                check_type(argname="argument duration_in_minutes", value=duration_in_minutes, expected_type=type_hints["duration_in_minutes"])
                check_type(argname="argument rotation_ids", value=rotation_ids, expected_type=type_hints["rotation_ids"])
                check_type(argname="argument targets", value=targets, expected_type=type_hints["targets"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if duration_in_minutes is not None:
                self._values["duration_in_minutes"] = duration_in_minutes
            if rotation_ids is not None:
                self._values["rotation_ids"] = rotation_ids
            if targets is not None:
                self._values["targets"] = targets

        @builtins.property
        def duration_in_minutes(self) -> typing.Optional[jsii.Number]:
            '''The time to wait until beginning the next stage.

            The duration can only be set to 0 if a target is specified.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-contact-stage.html#cfn-ssmcontacts-contact-stage-durationinminutes
            '''
            result = self._values.get("duration_in_minutes")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def rotation_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The Amazon Resource Names (ARNs) of the on-call rotations associated with the plan.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-contact-stage.html#cfn-ssmcontacts-contact-stage-rotationids
            '''
            result = self._values.get("rotation_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def targets(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnContact.TargetsProperty"]]]]:
            '''The contacts or contact methods that the escalation plan or engagement plan is engaging.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-contact-stage.html#cfn-ssmcontacts-contact-stage-targets
            '''
            result = self._values.get("targets")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnContact.TargetsProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StageProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssmcontacts.CfnContact.TargetsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "channel_target_info": "channelTargetInfo",
            "contact_target_info": "contactTargetInfo",
        },
    )
    class TargetsProperty:
        def __init__(
            self,
            *,
            channel_target_info: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnContact.ChannelTargetInfoProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            contact_target_info: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnContact.ContactTargetInfoProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The contact or contact channel that's being engaged.

            :param channel_target_info: Information about the contact channel that Incident Manager engages.
            :param contact_target_info: The contact that Incident Manager is engaging during an incident.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-contact-targets.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssmcontacts as ssmcontacts
                
                targets_property = ssmcontacts.CfnContact.TargetsProperty(
                    channel_target_info=ssmcontacts.CfnContact.ChannelTargetInfoProperty(
                        channel_id="channelId",
                        retry_interval_in_minutes=123
                    ),
                    contact_target_info=ssmcontacts.CfnContact.ContactTargetInfoProperty(
                        contact_id="contactId",
                        is_essential=False
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__55603f1f49aeead31e2b8475c5647006fc8de1390e7ca4158f8c5047373348e2)
                check_type(argname="argument channel_target_info", value=channel_target_info, expected_type=type_hints["channel_target_info"])
                check_type(argname="argument contact_target_info", value=contact_target_info, expected_type=type_hints["contact_target_info"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if channel_target_info is not None:
                self._values["channel_target_info"] = channel_target_info
            if contact_target_info is not None:
                self._values["contact_target_info"] = contact_target_info

        @builtins.property
        def channel_target_info(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnContact.ChannelTargetInfoProperty"]]:
            '''Information about the contact channel that Incident Manager engages.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-contact-targets.html#cfn-ssmcontacts-contact-targets-channeltargetinfo
            '''
            result = self._values.get("channel_target_info")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnContact.ChannelTargetInfoProperty"]], result)

        @builtins.property
        def contact_target_info(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnContact.ContactTargetInfoProperty"]]:
            '''The contact that Incident Manager is engaging during an incident.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-contact-targets.html#cfn-ssmcontacts-contact-targets-contacttargetinfo
            '''
            result = self._values.get("contact_target_info")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnContact.ContactTargetInfoProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TargetsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556)
class CfnContactChannel(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ssmcontacts.CfnContactChannel",
):
    '''The ``AWS::SSMContacts::ContactChannel`` resource specifies a contact channel as the method that Incident Manager uses to engage your contact.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-contactchannel.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ssmcontacts as ssmcontacts
        
        cfn_contact_channel = ssmcontacts.CfnContactChannel(self, "MyCfnContactChannel",
            channel_address="channelAddress",
            channel_name="channelName",
            channel_type="channelType",
            contact_id="contactId",
        
            # the properties below are optional
            defer_activation=False
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        channel_address: builtins.str,
        channel_name: builtins.str,
        channel_type: builtins.str,
        contact_id: builtins.str,
        defer_activation: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param channel_address: The details that Incident Manager uses when trying to engage the contact channel.
        :param channel_name: The name of the contact channel.
        :param channel_type: The type of the contact channel. Incident Manager supports three contact methods:. - SMS - VOICE - EMAIL
        :param contact_id: The Amazon Resource Name (ARN) of the contact you are adding the contact channel to.
        :param defer_activation: If you want to activate the channel at a later time, you can choose to defer activation. Incident Manager can't engage your contact channel until it has been activated.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1617a23866261103ffbfe512be7356fd9cfde9f098fbbb8abeafd44e741a1dea)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnContactChannelProps(
            channel_address=channel_address,
            channel_name=channel_name,
            channel_type=channel_type,
            contact_id=contact_id,
            defer_activation=defer_activation,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c79c2a0f8c2fcfce619e0d43bafe063c344e896341db65e50b14635676b3f64)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7c8a7d2ebe7d9a66479c5bec6bb0d272cd150e7d9b19dccb5e0f02eecc1f2f02)
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
        '''The Amazon Resource Name (ARN) of the ``ContactChannel`` resource.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="channelAddress")
    def channel_address(self) -> builtins.str:
        '''The details that Incident Manager uses when trying to engage the contact channel.'''
        return typing.cast(builtins.str, jsii.get(self, "channelAddress"))

    @channel_address.setter
    def channel_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a5a7089d37931a755aff5c986c6109960e59c48f9af4ed79a8953b93ca748ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "channelAddress", value)

    @builtins.property
    @jsii.member(jsii_name="channelName")
    def channel_name(self) -> builtins.str:
        '''The name of the contact channel.'''
        return typing.cast(builtins.str, jsii.get(self, "channelName"))

    @channel_name.setter
    def channel_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3bba3adfea78f0f5c6aec4ef81d3a19e05bcb6013d7d1557bd5d87a56b91406)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "channelName", value)

    @builtins.property
    @jsii.member(jsii_name="channelType")
    def channel_type(self) -> builtins.str:
        '''The type of the contact channel.

        Incident Manager supports three contact methods:.
        '''
        return typing.cast(builtins.str, jsii.get(self, "channelType"))

    @channel_type.setter
    def channel_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e76494fe71820cd79123d1c58f52f9734511b5f0e9ebc904568cc4a3614d236a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "channelType", value)

    @builtins.property
    @jsii.member(jsii_name="contactId")
    def contact_id(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the contact you are adding the contact channel to.'''
        return typing.cast(builtins.str, jsii.get(self, "contactId"))

    @contact_id.setter
    def contact_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82ab7a7941dcaf019ff883ded9ab61de82e25ca982f876491b992626ec103136)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contactId", value)

    @builtins.property
    @jsii.member(jsii_name="deferActivation")
    def defer_activation(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''If you want to activate the channel at a later time, you can choose to defer activation.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "deferActivation"))

    @defer_activation.setter
    def defer_activation(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99b9167dee5265e65d4f53f0abd17410ef25ee43a5aaa99fd33f989d172a3844)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deferActivation", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ssmcontacts.CfnContactChannelProps",
    jsii_struct_bases=[],
    name_mapping={
        "channel_address": "channelAddress",
        "channel_name": "channelName",
        "channel_type": "channelType",
        "contact_id": "contactId",
        "defer_activation": "deferActivation",
    },
)
class CfnContactChannelProps:
    def __init__(
        self,
        *,
        channel_address: builtins.str,
        channel_name: builtins.str,
        channel_type: builtins.str,
        contact_id: builtins.str,
        defer_activation: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    ) -> None:
        '''Properties for defining a ``CfnContactChannel``.

        :param channel_address: The details that Incident Manager uses when trying to engage the contact channel.
        :param channel_name: The name of the contact channel.
        :param channel_type: The type of the contact channel. Incident Manager supports three contact methods:. - SMS - VOICE - EMAIL
        :param contact_id: The Amazon Resource Name (ARN) of the contact you are adding the contact channel to.
        :param defer_activation: If you want to activate the channel at a later time, you can choose to defer activation. Incident Manager can't engage your contact channel until it has been activated.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-contactchannel.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ssmcontacts as ssmcontacts
            
            cfn_contact_channel_props = ssmcontacts.CfnContactChannelProps(
                channel_address="channelAddress",
                channel_name="channelName",
                channel_type="channelType",
                contact_id="contactId",
            
                # the properties below are optional
                defer_activation=False
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60153d8d82b752412e4b3852bb6bfda95115461ca88ac40d1598f699bd2681fd)
            check_type(argname="argument channel_address", value=channel_address, expected_type=type_hints["channel_address"])
            check_type(argname="argument channel_name", value=channel_name, expected_type=type_hints["channel_name"])
            check_type(argname="argument channel_type", value=channel_type, expected_type=type_hints["channel_type"])
            check_type(argname="argument contact_id", value=contact_id, expected_type=type_hints["contact_id"])
            check_type(argname="argument defer_activation", value=defer_activation, expected_type=type_hints["defer_activation"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "channel_address": channel_address,
            "channel_name": channel_name,
            "channel_type": channel_type,
            "contact_id": contact_id,
        }
        if defer_activation is not None:
            self._values["defer_activation"] = defer_activation

    @builtins.property
    def channel_address(self) -> builtins.str:
        '''The details that Incident Manager uses when trying to engage the contact channel.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-contactchannel.html#cfn-ssmcontacts-contactchannel-channeladdress
        '''
        result = self._values.get("channel_address")
        assert result is not None, "Required property 'channel_address' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def channel_name(self) -> builtins.str:
        '''The name of the contact channel.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-contactchannel.html#cfn-ssmcontacts-contactchannel-channelname
        '''
        result = self._values.get("channel_name")
        assert result is not None, "Required property 'channel_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def channel_type(self) -> builtins.str:
        '''The type of the contact channel. Incident Manager supports three contact methods:.

        - SMS
        - VOICE
        - EMAIL

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-contactchannel.html#cfn-ssmcontacts-contactchannel-channeltype
        '''
        result = self._values.get("channel_type")
        assert result is not None, "Required property 'channel_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def contact_id(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the contact you are adding the contact channel to.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-contactchannel.html#cfn-ssmcontacts-contactchannel-contactid
        '''
        result = self._values.get("contact_id")
        assert result is not None, "Required property 'contact_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def defer_activation(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''If you want to activate the channel at a later time, you can choose to defer activation.

        Incident Manager can't engage your contact channel until it has been activated.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-contactchannel.html#cfn-ssmcontacts-contactchannel-deferactivation
        '''
        result = self._values.get("defer_activation")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnContactChannelProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ssmcontacts.CfnContactProps",
    jsii_struct_bases=[],
    name_mapping={
        "alias": "alias",
        "display_name": "displayName",
        "type": "type",
        "plan": "plan",
    },
)
class CfnContactProps:
    def __init__(
        self,
        *,
        alias: builtins.str,
        display_name: builtins.str,
        type: builtins.str,
        plan: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContact.StageProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnContact``.

        :param alias: The unique and identifiable alias of the contact or escalation plan.
        :param display_name: The full name of the contact or escalation plan.
        :param type: Refers to the type of contact:. - ``PERSONAL`` : A single, individual contact. - ``ESCALATION`` : An escalation plan. - ``ONCALL_SCHEDULE`` : An on-call schedule.
        :param plan: A list of stages. A contact has an engagement plan with stages that contact specified contact channels. An escalation plan uses stages that contact specified contacts.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-contact.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ssmcontacts as ssmcontacts
            
            cfn_contact_props = ssmcontacts.CfnContactProps(
                alias="alias",
                display_name="displayName",
                type="type",
            
                # the properties below are optional
                plan=[ssmcontacts.CfnContact.StageProperty(
                    duration_in_minutes=123,
                    rotation_ids=["rotationIds"],
                    targets=[ssmcontacts.CfnContact.TargetsProperty(
                        channel_target_info=ssmcontacts.CfnContact.ChannelTargetInfoProperty(
                            channel_id="channelId",
                            retry_interval_in_minutes=123
                        ),
                        contact_target_info=ssmcontacts.CfnContact.ContactTargetInfoProperty(
                            contact_id="contactId",
                            is_essential=False
                        )
                    )]
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f741949260f507a90eb76a4ec5f8c03a5b8eeee237bc39b33a8add5cdc74d026)
            check_type(argname="argument alias", value=alias, expected_type=type_hints["alias"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument plan", value=plan, expected_type=type_hints["plan"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "alias": alias,
            "display_name": display_name,
            "type": type,
        }
        if plan is not None:
            self._values["plan"] = plan

    @builtins.property
    def alias(self) -> builtins.str:
        '''The unique and identifiable alias of the contact or escalation plan.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-contact.html#cfn-ssmcontacts-contact-alias
        '''
        result = self._values.get("alias")
        assert result is not None, "Required property 'alias' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def display_name(self) -> builtins.str:
        '''The full name of the contact or escalation plan.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-contact.html#cfn-ssmcontacts-contact-displayname
        '''
        result = self._values.get("display_name")
        assert result is not None, "Required property 'display_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Refers to the type of contact:.

        - ``PERSONAL`` : A single, individual contact.
        - ``ESCALATION`` : An escalation plan.
        - ``ONCALL_SCHEDULE`` : An on-call schedule.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-contact.html#cfn-ssmcontacts-contact-type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def plan(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnContact.StageProperty]]]]:
        '''A list of stages.

        A contact has an engagement plan with stages that contact specified contact channels. An escalation plan uses stages that contact specified contacts.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-contact.html#cfn-ssmcontacts-contact-plan
        '''
        result = self._values.get("plan")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnContact.StageProperty]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnContactProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnPlan(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ssmcontacts.CfnPlan",
):
    '''Information about the stages and on-call rotation teams associated with an escalation plan or engagement plan.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-plan.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ssmcontacts as ssmcontacts
        
        cfn_plan = ssmcontacts.CfnPlan(self, "MyCfnPlan",
            contact_id="contactId",
        
            # the properties below are optional
            rotation_ids=["rotationIds"],
            stages=[ssmcontacts.CfnPlan.StageProperty(
                duration_in_minutes=123,
        
                # the properties below are optional
                targets=[ssmcontacts.CfnPlan.TargetsProperty(
                    channel_target_info=ssmcontacts.CfnPlan.ChannelTargetInfoProperty(
                        channel_id="channelId",
                        retry_interval_in_minutes=123
                    ),
                    contact_target_info=ssmcontacts.CfnPlan.ContactTargetInfoProperty(
                        contact_id="contactId",
                        is_essential=False
                    )
                )]
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        contact_id: builtins.str,
        rotation_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        stages: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPlan.StageProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param contact_id: The Amazon Resource Name (ARN) of the contact.
        :param rotation_ids: The Amazon Resource Names (ARNs) of the on-call rotations associated with the plan.
        :param stages: A list of stages that the escalation plan or engagement plan uses to engage contacts and contact methods.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6e0c22680f733d3f22f01f5aa4b1401c09fcbf33bd52ea8ce6e156657761291)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPlanProps(
            contact_id=contact_id, rotation_ids=rotation_ids, stages=stages
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__137ec9788a7a67aa1b51d2a0c7a6b9ed547385e0bf491539d328f6f2be03fcfe)
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
            type_hints = typing.get_type_hints(_typecheckingstub__32b96bebac55eb6729cb601463e9b625faf9ce4e9fbabd3b393117d992fd302b)
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
        '''The Amazon Resource Name (ARN) of the ``Plan`` resource.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="contactId")
    def contact_id(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the contact.'''
        return typing.cast(builtins.str, jsii.get(self, "contactId"))

    @contact_id.setter
    def contact_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59045e1db75e26927310a75a7663c8e46347a898fd847f92c5322b25b3166292)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contactId", value)

    @builtins.property
    @jsii.member(jsii_name="rotationIds")
    def rotation_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The Amazon Resource Names (ARNs) of the on-call rotations associated with the plan.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "rotationIds"))

    @rotation_ids.setter
    def rotation_ids(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7f8dbf20ba74a1032313ecba1522fc91898adade9f71310759089010f26013d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rotationIds", value)

    @builtins.property
    @jsii.member(jsii_name="stages")
    def stages(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPlan.StageProperty"]]]]:
        '''A list of stages that the escalation plan or engagement plan uses to engage contacts and contact methods.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPlan.StageProperty"]]]], jsii.get(self, "stages"))

    @stages.setter
    def stages(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPlan.StageProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98071cbe25b9c5fdcd471387b967afcc5792d313a75945efade94d8eb76ca785)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stages", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssmcontacts.CfnPlan.ChannelTargetInfoProperty",
        jsii_struct_bases=[],
        name_mapping={
            "channel_id": "channelId",
            "retry_interval_in_minutes": "retryIntervalInMinutes",
        },
    )
    class ChannelTargetInfoProperty:
        def __init__(
            self,
            *,
            channel_id: builtins.str,
            retry_interval_in_minutes: jsii.Number,
        ) -> None:
            '''Information about the contact channel that Incident Manager uses to engage the contact.

            :param channel_id: The Amazon Resource Name (ARN) of the contact channel.
            :param retry_interval_in_minutes: The number of minutes to wait before retrying to send engagement if the engagement initially failed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-plan-channeltargetinfo.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssmcontacts as ssmcontacts
                
                channel_target_info_property = ssmcontacts.CfnPlan.ChannelTargetInfoProperty(
                    channel_id="channelId",
                    retry_interval_in_minutes=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__84e76848537282e977dcde0f14f8ddb961f9ff06debd5fe09940f053ebe3cf2a)
                check_type(argname="argument channel_id", value=channel_id, expected_type=type_hints["channel_id"])
                check_type(argname="argument retry_interval_in_minutes", value=retry_interval_in_minutes, expected_type=type_hints["retry_interval_in_minutes"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "channel_id": channel_id,
                "retry_interval_in_minutes": retry_interval_in_minutes,
            }

        @builtins.property
        def channel_id(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the contact channel.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-plan-channeltargetinfo.html#cfn-ssmcontacts-plan-channeltargetinfo-channelid
            '''
            result = self._values.get("channel_id")
            assert result is not None, "Required property 'channel_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def retry_interval_in_minutes(self) -> jsii.Number:
            '''The number of minutes to wait before retrying to send engagement if the engagement initially failed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-plan-channeltargetinfo.html#cfn-ssmcontacts-plan-channeltargetinfo-retryintervalinminutes
            '''
            result = self._values.get("retry_interval_in_minutes")
            assert result is not None, "Required property 'retry_interval_in_minutes' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ChannelTargetInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssmcontacts.CfnPlan.ContactTargetInfoProperty",
        jsii_struct_bases=[],
        name_mapping={"contact_id": "contactId", "is_essential": "isEssential"},
    )
    class ContactTargetInfoProperty:
        def __init__(
            self,
            *,
            contact_id: builtins.str,
            is_essential: typing.Union[builtins.bool, _IResolvable_da3f097b],
        ) -> None:
            '''The contact that Incident Manager is engaging during an incident.

            :param contact_id: The Amazon Resource Name (ARN) of the contact.
            :param is_essential: A Boolean value determining if the contact's acknowledgement stops the progress of stages in the plan.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-plan-contacttargetinfo.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssmcontacts as ssmcontacts
                
                contact_target_info_property = ssmcontacts.CfnPlan.ContactTargetInfoProperty(
                    contact_id="contactId",
                    is_essential=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__610765f953ad183b666776caf683f78dbb8fa01e0c136d028fb058346bfde1ff)
                check_type(argname="argument contact_id", value=contact_id, expected_type=type_hints["contact_id"])
                check_type(argname="argument is_essential", value=is_essential, expected_type=type_hints["is_essential"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "contact_id": contact_id,
                "is_essential": is_essential,
            }

        @builtins.property
        def contact_id(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the contact.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-plan-contacttargetinfo.html#cfn-ssmcontacts-plan-contacttargetinfo-contactid
            '''
            result = self._values.get("contact_id")
            assert result is not None, "Required property 'contact_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def is_essential(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''A Boolean value determining if the contact's acknowledgement stops the progress of stages in the plan.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-plan-contacttargetinfo.html#cfn-ssmcontacts-plan-contacttargetinfo-isessential
            '''
            result = self._values.get("is_essential")
            assert result is not None, "Required property 'is_essential' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ContactTargetInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssmcontacts.CfnPlan.StageProperty",
        jsii_struct_bases=[],
        name_mapping={
            "duration_in_minutes": "durationInMinutes",
            "targets": "targets",
        },
    )
    class StageProperty:
        def __init__(
            self,
            *,
            duration_in_minutes: jsii.Number,
            targets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPlan.TargetsProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''A set amount of time that an escalation plan or engagement plan engages the specified contacts or contact methods.

            :param duration_in_minutes: The time to wait until beginning the next stage. The duration can only be set to 0 if a target is specified.
            :param targets: The contacts or contact methods that the escalation plan or engagement plan is engaging.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-plan-stage.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssmcontacts as ssmcontacts
                
                stage_property = ssmcontacts.CfnPlan.StageProperty(
                    duration_in_minutes=123,
                
                    # the properties below are optional
                    targets=[ssmcontacts.CfnPlan.TargetsProperty(
                        channel_target_info=ssmcontacts.CfnPlan.ChannelTargetInfoProperty(
                            channel_id="channelId",
                            retry_interval_in_minutes=123
                        ),
                        contact_target_info=ssmcontacts.CfnPlan.ContactTargetInfoProperty(
                            contact_id="contactId",
                            is_essential=False
                        )
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__23656d44cd1599e50fb9a1834c8723f0417861b7725022518d862812e406042b)
                check_type(argname="argument duration_in_minutes", value=duration_in_minutes, expected_type=type_hints["duration_in_minutes"])
                check_type(argname="argument targets", value=targets, expected_type=type_hints["targets"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "duration_in_minutes": duration_in_minutes,
            }
            if targets is not None:
                self._values["targets"] = targets

        @builtins.property
        def duration_in_minutes(self) -> jsii.Number:
            '''The time to wait until beginning the next stage.

            The duration can only be set to 0 if a target is specified.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-plan-stage.html#cfn-ssmcontacts-plan-stage-durationinminutes
            '''
            result = self._values.get("duration_in_minutes")
            assert result is not None, "Required property 'duration_in_minutes' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def targets(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPlan.TargetsProperty"]]]]:
            '''The contacts or contact methods that the escalation plan or engagement plan is engaging.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-plan-stage.html#cfn-ssmcontacts-plan-stage-targets
            '''
            result = self._values.get("targets")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPlan.TargetsProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StageProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssmcontacts.CfnPlan.TargetsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "channel_target_info": "channelTargetInfo",
            "contact_target_info": "contactTargetInfo",
        },
    )
    class TargetsProperty:
        def __init__(
            self,
            *,
            channel_target_info: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPlan.ChannelTargetInfoProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            contact_target_info: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPlan.ContactTargetInfoProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The contact or contact channel that's being engaged.

            :param channel_target_info: Information about the contact channel that Incident Manager engages.
            :param contact_target_info: Information about the contact that Incident Manager engages.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-plan-targets.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssmcontacts as ssmcontacts
                
                targets_property = ssmcontacts.CfnPlan.TargetsProperty(
                    channel_target_info=ssmcontacts.CfnPlan.ChannelTargetInfoProperty(
                        channel_id="channelId",
                        retry_interval_in_minutes=123
                    ),
                    contact_target_info=ssmcontacts.CfnPlan.ContactTargetInfoProperty(
                        contact_id="contactId",
                        is_essential=False
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6975d159f87be06849c92d03bb48f0cd4d1b06bb5e3f9555822c686d405c5e4e)
                check_type(argname="argument channel_target_info", value=channel_target_info, expected_type=type_hints["channel_target_info"])
                check_type(argname="argument contact_target_info", value=contact_target_info, expected_type=type_hints["contact_target_info"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if channel_target_info is not None:
                self._values["channel_target_info"] = channel_target_info
            if contact_target_info is not None:
                self._values["contact_target_info"] = contact_target_info

        @builtins.property
        def channel_target_info(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPlan.ChannelTargetInfoProperty"]]:
            '''Information about the contact channel that Incident Manager engages.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-plan-targets.html#cfn-ssmcontacts-plan-targets-channeltargetinfo
            '''
            result = self._values.get("channel_target_info")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPlan.ChannelTargetInfoProperty"]], result)

        @builtins.property
        def contact_target_info(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPlan.ContactTargetInfoProperty"]]:
            '''Information about the contact that Incident Manager engages.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-plan-targets.html#cfn-ssmcontacts-plan-targets-contacttargetinfo
            '''
            result = self._values.get("contact_target_info")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPlan.ContactTargetInfoProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TargetsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ssmcontacts.CfnPlanProps",
    jsii_struct_bases=[],
    name_mapping={
        "contact_id": "contactId",
        "rotation_ids": "rotationIds",
        "stages": "stages",
    },
)
class CfnPlanProps:
    def __init__(
        self,
        *,
        contact_id: builtins.str,
        rotation_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        stages: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPlan.StageProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnPlan``.

        :param contact_id: The Amazon Resource Name (ARN) of the contact.
        :param rotation_ids: The Amazon Resource Names (ARNs) of the on-call rotations associated with the plan.
        :param stages: A list of stages that the escalation plan or engagement plan uses to engage contacts and contact methods.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-plan.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ssmcontacts as ssmcontacts
            
            cfn_plan_props = ssmcontacts.CfnPlanProps(
                contact_id="contactId",
            
                # the properties below are optional
                rotation_ids=["rotationIds"],
                stages=[ssmcontacts.CfnPlan.StageProperty(
                    duration_in_minutes=123,
            
                    # the properties below are optional
                    targets=[ssmcontacts.CfnPlan.TargetsProperty(
                        channel_target_info=ssmcontacts.CfnPlan.ChannelTargetInfoProperty(
                            channel_id="channelId",
                            retry_interval_in_minutes=123
                        ),
                        contact_target_info=ssmcontacts.CfnPlan.ContactTargetInfoProperty(
                            contact_id="contactId",
                            is_essential=False
                        )
                    )]
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8efc2cb087519575d349f15e5f11bf8abf775e3bdb2501c2d28a6f2690c8f17f)
            check_type(argname="argument contact_id", value=contact_id, expected_type=type_hints["contact_id"])
            check_type(argname="argument rotation_ids", value=rotation_ids, expected_type=type_hints["rotation_ids"])
            check_type(argname="argument stages", value=stages, expected_type=type_hints["stages"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "contact_id": contact_id,
        }
        if rotation_ids is not None:
            self._values["rotation_ids"] = rotation_ids
        if stages is not None:
            self._values["stages"] = stages

    @builtins.property
    def contact_id(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the contact.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-plan.html#cfn-ssmcontacts-plan-contactid
        '''
        result = self._values.get("contact_id")
        assert result is not None, "Required property 'contact_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rotation_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The Amazon Resource Names (ARNs) of the on-call rotations associated with the plan.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-plan.html#cfn-ssmcontacts-plan-rotationids
        '''
        result = self._values.get("rotation_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def stages(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnPlan.StageProperty]]]]:
        '''A list of stages that the escalation plan or engagement plan uses to engage contacts and contact methods.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-plan.html#cfn-ssmcontacts-plan-stages
        '''
        result = self._values.get("stages")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnPlan.StageProperty]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPlanProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnRotation(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ssmcontacts.CfnRotation",
):
    '''Specifies a rotation in an on-call schedule.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-rotation.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ssmcontacts as ssmcontacts
        
        cfn_rotation = ssmcontacts.CfnRotation(self, "MyCfnRotation",
            contact_ids=["contactIds"],
            name="name",
            recurrence=ssmcontacts.CfnRotation.RecurrenceSettingsProperty(
                number_of_on_calls=123,
                recurrence_multiplier=123,
        
                # the properties below are optional
                daily_settings=["dailySettings"],
                monthly_settings=[ssmcontacts.CfnRotation.MonthlySettingProperty(
                    day_of_month=123,
                    hand_off_time="handOffTime"
                )],
                shift_coverages=[ssmcontacts.CfnRotation.ShiftCoverageProperty(
                    coverage_times=[ssmcontacts.CfnRotation.CoverageTimeProperty(
                        end_time="endTime",
                        start_time="startTime"
                    )],
                    day_of_week="dayOfWeek"
                )],
                weekly_settings=[ssmcontacts.CfnRotation.WeeklySettingProperty(
                    day_of_week="dayOfWeek",
                    hand_off_time="handOffTime"
                )]
            ),
            start_time="startTime",
            time_zone_id="timeZoneId",
        
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
        contact_ids: typing.Sequence[builtins.str],
        name: builtins.str,
        recurrence: typing.Union[_IResolvable_da3f097b, typing.Union["CfnRotation.RecurrenceSettingsProperty", typing.Dict[builtins.str, typing.Any]]],
        start_time: builtins.str,
        time_zone_id: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param contact_ids: The Amazon Resource Names (ARNs) of the contacts to add to the rotation. The order in which you list the contacts is their shift order in the rotation schedule.
        :param name: The name for the rotation.
        :param recurrence: Information about the rule that specifies when shift team members rotate.
        :param start_time: The date and time the rotation goes into effect.
        :param time_zone_id: The time zone to base the rotation’s activity on, in Internet Assigned Numbers Authority (IANA) format. For example: "America/Los_Angeles", "UTC", or "Asia/Seoul". For more information, see the `Time Zone Database <https://docs.aws.amazon.com/https://www.iana.org/time-zones>`_ on the IANA website.
        :param tags: Optional metadata to assign to the rotation. Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment. For more information, see `Tagging Incident Manager resources <https://docs.aws.amazon.com/incident-manager/latest/userguide/tagging.html>`_ in the *Incident Manager User Guide* .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26eef7672fdd8123b01e699b8130ced5537ce3c542ab77ee1c6c06cb09cbf930)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnRotationProps(
            contact_ids=contact_ids,
            name=name,
            recurrence=recurrence,
            start_time=start_time,
            time_zone_id=time_zone_id,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__737a3930064adb508425fd82524f603fb39f45e289da49869aa4d8d4df27b36a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b88c043eeb8e592d641499ebecdca207c839d7d68a19e163641d132e62530a4b)
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
        '''The Amazon Resource Name (ARN) of the ``Rotation`` resource.

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
    @jsii.member(jsii_name="contactIds")
    def contact_ids(self) -> typing.List[builtins.str]:
        '''The Amazon Resource Names (ARNs) of the contacts to add to the rotation.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "contactIds"))

    @contact_ids.setter
    def contact_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1cbd1cbfab002f07a6d2bffee561f6c31760fc539bfe7a1e613f37f4e07fb206)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contactIds", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name for the rotation.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__947d78575ed0d1c185f504ba957c2e81b4696b00927ea2c6c79d4dc7a169dd19)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="recurrence")
    def recurrence(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnRotation.RecurrenceSettingsProperty"]:
        '''Information about the rule that specifies when shift team members rotate.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnRotation.RecurrenceSettingsProperty"], jsii.get(self, "recurrence"))

    @recurrence.setter
    def recurrence(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnRotation.RecurrenceSettingsProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15da7772d8591fe2320b8ab1b99e597707b586730055c9d05111aeb272ccd4e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recurrence", value)

    @builtins.property
    @jsii.member(jsii_name="startTime")
    def start_time(self) -> builtins.str:
        '''The date and time the rotation goes into effect.'''
        return typing.cast(builtins.str, jsii.get(self, "startTime"))

    @start_time.setter
    def start_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c73526f3a03d5d0c27d0420ed51553cfdf3eb29e824bdee17839275d7c957cd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startTime", value)

    @builtins.property
    @jsii.member(jsii_name="timeZoneId")
    def time_zone_id(self) -> builtins.str:
        '''The time zone to base the rotation’s activity on, in Internet Assigned Numbers Authority (IANA) format.'''
        return typing.cast(builtins.str, jsii.get(self, "timeZoneId"))

    @time_zone_id.setter
    def time_zone_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e822e7f1d29cbe95f2fb771175a652c3ae4e0cba9709976aee85050382d94b1c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeZoneId", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Optional metadata to assign to the rotation.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a05c65df6e2e0154dd878cf7783bed608ad778e57fdc781109dc1f9297a2ff64)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssmcontacts.CfnRotation.CoverageTimeProperty",
        jsii_struct_bases=[],
        name_mapping={"end_time": "endTime", "start_time": "startTime"},
    )
    class CoverageTimeProperty:
        def __init__(self, *, end_time: builtins.str, start_time: builtins.str) -> None:
            '''Information about when an on-call shift begins and ends.

            :param end_time: Information about when an on-call rotation shift ends.
            :param start_time: Information about when an on-call rotation shift begins.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-rotation-coveragetime.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssmcontacts as ssmcontacts
                
                coverage_time_property = ssmcontacts.CfnRotation.CoverageTimeProperty(
                    end_time="endTime",
                    start_time="startTime"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5471c5c00a3ee14c4782530651c75ea7604939ef0fa51223f6a883ed7864ef9e)
                check_type(argname="argument end_time", value=end_time, expected_type=type_hints["end_time"])
                check_type(argname="argument start_time", value=start_time, expected_type=type_hints["start_time"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "end_time": end_time,
                "start_time": start_time,
            }

        @builtins.property
        def end_time(self) -> builtins.str:
            '''Information about when an on-call rotation shift ends.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-rotation-coveragetime.html#cfn-ssmcontacts-rotation-coveragetime-endtime
            '''
            result = self._values.get("end_time")
            assert result is not None, "Required property 'end_time' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def start_time(self) -> builtins.str:
            '''Information about when an on-call rotation shift begins.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-rotation-coveragetime.html#cfn-ssmcontacts-rotation-coveragetime-starttime
            '''
            result = self._values.get("start_time")
            assert result is not None, "Required property 'start_time' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CoverageTimeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssmcontacts.CfnRotation.MonthlySettingProperty",
        jsii_struct_bases=[],
        name_mapping={"day_of_month": "dayOfMonth", "hand_off_time": "handOffTime"},
    )
    class MonthlySettingProperty:
        def __init__(
            self,
            *,
            day_of_month: jsii.Number,
            hand_off_time: builtins.str,
        ) -> None:
            '''Information about on-call rotations that recur monthly.

            :param day_of_month: The day of the month when monthly recurring on-call rotations begin.
            :param hand_off_time: The time of day when a monthly recurring on-call shift rotation begins.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-rotation-monthlysetting.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssmcontacts as ssmcontacts
                
                monthly_setting_property = ssmcontacts.CfnRotation.MonthlySettingProperty(
                    day_of_month=123,
                    hand_off_time="handOffTime"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4acc5d36b459ef219c0d9e8696ba8d79a8dc692c3d46f15b8f7590249f318c89)
                check_type(argname="argument day_of_month", value=day_of_month, expected_type=type_hints["day_of_month"])
                check_type(argname="argument hand_off_time", value=hand_off_time, expected_type=type_hints["hand_off_time"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "day_of_month": day_of_month,
                "hand_off_time": hand_off_time,
            }

        @builtins.property
        def day_of_month(self) -> jsii.Number:
            '''The day of the month when monthly recurring on-call rotations begin.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-rotation-monthlysetting.html#cfn-ssmcontacts-rotation-monthlysetting-dayofmonth
            '''
            result = self._values.get("day_of_month")
            assert result is not None, "Required property 'day_of_month' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def hand_off_time(self) -> builtins.str:
            '''The time of day when a monthly recurring on-call shift rotation begins.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-rotation-monthlysetting.html#cfn-ssmcontacts-rotation-monthlysetting-handofftime
            '''
            result = self._values.get("hand_off_time")
            assert result is not None, "Required property 'hand_off_time' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonthlySettingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssmcontacts.CfnRotation.RecurrenceSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "number_of_on_calls": "numberOfOnCalls",
            "recurrence_multiplier": "recurrenceMultiplier",
            "daily_settings": "dailySettings",
            "monthly_settings": "monthlySettings",
            "shift_coverages": "shiftCoverages",
            "weekly_settings": "weeklySettings",
        },
    )
    class RecurrenceSettingsProperty:
        def __init__(
            self,
            *,
            number_of_on_calls: jsii.Number,
            recurrence_multiplier: jsii.Number,
            daily_settings: typing.Optional[typing.Sequence[builtins.str]] = None,
            monthly_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRotation.MonthlySettingProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            shift_coverages: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRotation.ShiftCoverageProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            weekly_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRotation.WeeklySettingProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Information about when an on-call rotation is in effect and how long the rotation period lasts.

            :param number_of_on_calls: The number of contacts, or shift team members designated to be on call concurrently during a shift. For example, in an on-call schedule that contains ten contacts, a value of ``2`` designates that two of them are on call at any given time.
            :param recurrence_multiplier: The number of days, weeks, or months a single rotation lasts.
            :param daily_settings: Information about on-call rotations that recur daily.
            :param monthly_settings: Information about on-call rotations that recur monthly.
            :param shift_coverages: Information about the days of the week included in on-call rotation coverage.
            :param weekly_settings: Information about on-call rotations that recur weekly.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-rotation-recurrencesettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssmcontacts as ssmcontacts
                
                recurrence_settings_property = ssmcontacts.CfnRotation.RecurrenceSettingsProperty(
                    number_of_on_calls=123,
                    recurrence_multiplier=123,
                
                    # the properties below are optional
                    daily_settings=["dailySettings"],
                    monthly_settings=[ssmcontacts.CfnRotation.MonthlySettingProperty(
                        day_of_month=123,
                        hand_off_time="handOffTime"
                    )],
                    shift_coverages=[ssmcontacts.CfnRotation.ShiftCoverageProperty(
                        coverage_times=[ssmcontacts.CfnRotation.CoverageTimeProperty(
                            end_time="endTime",
                            start_time="startTime"
                        )],
                        day_of_week="dayOfWeek"
                    )],
                    weekly_settings=[ssmcontacts.CfnRotation.WeeklySettingProperty(
                        day_of_week="dayOfWeek",
                        hand_off_time="handOffTime"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1c7e912eafde708159eeee02d146481d7aad1c73b0a5b641a391970ddad57bbb)
                check_type(argname="argument number_of_on_calls", value=number_of_on_calls, expected_type=type_hints["number_of_on_calls"])
                check_type(argname="argument recurrence_multiplier", value=recurrence_multiplier, expected_type=type_hints["recurrence_multiplier"])
                check_type(argname="argument daily_settings", value=daily_settings, expected_type=type_hints["daily_settings"])
                check_type(argname="argument monthly_settings", value=monthly_settings, expected_type=type_hints["monthly_settings"])
                check_type(argname="argument shift_coverages", value=shift_coverages, expected_type=type_hints["shift_coverages"])
                check_type(argname="argument weekly_settings", value=weekly_settings, expected_type=type_hints["weekly_settings"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "number_of_on_calls": number_of_on_calls,
                "recurrence_multiplier": recurrence_multiplier,
            }
            if daily_settings is not None:
                self._values["daily_settings"] = daily_settings
            if monthly_settings is not None:
                self._values["monthly_settings"] = monthly_settings
            if shift_coverages is not None:
                self._values["shift_coverages"] = shift_coverages
            if weekly_settings is not None:
                self._values["weekly_settings"] = weekly_settings

        @builtins.property
        def number_of_on_calls(self) -> jsii.Number:
            '''The number of contacts, or shift team members designated to be on call concurrently during a shift.

            For example, in an on-call schedule that contains ten contacts, a value of ``2`` designates that two of them are on call at any given time.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-rotation-recurrencesettings.html#cfn-ssmcontacts-rotation-recurrencesettings-numberofoncalls
            '''
            result = self._values.get("number_of_on_calls")
            assert result is not None, "Required property 'number_of_on_calls' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def recurrence_multiplier(self) -> jsii.Number:
            '''The number of days, weeks, or months a single rotation lasts.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-rotation-recurrencesettings.html#cfn-ssmcontacts-rotation-recurrencesettings-recurrencemultiplier
            '''
            result = self._values.get("recurrence_multiplier")
            assert result is not None, "Required property 'recurrence_multiplier' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def daily_settings(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Information about on-call rotations that recur daily.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-rotation-recurrencesettings.html#cfn-ssmcontacts-rotation-recurrencesettings-dailysettings
            '''
            result = self._values.get("daily_settings")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def monthly_settings(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRotation.MonthlySettingProperty"]]]]:
            '''Information about on-call rotations that recur monthly.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-rotation-recurrencesettings.html#cfn-ssmcontacts-rotation-recurrencesettings-monthlysettings
            '''
            result = self._values.get("monthly_settings")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRotation.MonthlySettingProperty"]]]], result)

        @builtins.property
        def shift_coverages(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRotation.ShiftCoverageProperty"]]]]:
            '''Information about the days of the week included in on-call rotation coverage.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-rotation-recurrencesettings.html#cfn-ssmcontacts-rotation-recurrencesettings-shiftcoverages
            '''
            result = self._values.get("shift_coverages")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRotation.ShiftCoverageProperty"]]]], result)

        @builtins.property
        def weekly_settings(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRotation.WeeklySettingProperty"]]]]:
            '''Information about on-call rotations that recur weekly.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-rotation-recurrencesettings.html#cfn-ssmcontacts-rotation-recurrencesettings-weeklysettings
            '''
            result = self._values.get("weekly_settings")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRotation.WeeklySettingProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RecurrenceSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssmcontacts.CfnRotation.ShiftCoverageProperty",
        jsii_struct_bases=[],
        name_mapping={"coverage_times": "coverageTimes", "day_of_week": "dayOfWeek"},
    )
    class ShiftCoverageProperty:
        def __init__(
            self,
            *,
            coverage_times: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRotation.CoverageTimeProperty", typing.Dict[builtins.str, typing.Any]]]]],
            day_of_week: builtins.str,
        ) -> None:
            '''Information about the days of the week that the on-call rotation coverage includes.

            :param coverage_times: The start and end times of the shift.
            :param day_of_week: A list of days on which the schedule is active.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-rotation-shiftcoverage.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssmcontacts as ssmcontacts
                
                shift_coverage_property = ssmcontacts.CfnRotation.ShiftCoverageProperty(
                    coverage_times=[ssmcontacts.CfnRotation.CoverageTimeProperty(
                        end_time="endTime",
                        start_time="startTime"
                    )],
                    day_of_week="dayOfWeek"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9812f77378c4a6af9579759f5ec079ebc4b0cd0e6e34d34ad7898495e1e5ab2d)
                check_type(argname="argument coverage_times", value=coverage_times, expected_type=type_hints["coverage_times"])
                check_type(argname="argument day_of_week", value=day_of_week, expected_type=type_hints["day_of_week"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "coverage_times": coverage_times,
                "day_of_week": day_of_week,
            }

        @builtins.property
        def coverage_times(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRotation.CoverageTimeProperty"]]]:
            '''The start and end times of the shift.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-rotation-shiftcoverage.html#cfn-ssmcontacts-rotation-shiftcoverage-coveragetimes
            '''
            result = self._values.get("coverage_times")
            assert result is not None, "Required property 'coverage_times' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRotation.CoverageTimeProperty"]]], result)

        @builtins.property
        def day_of_week(self) -> builtins.str:
            '''A list of days on which the schedule is active.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-rotation-shiftcoverage.html#cfn-ssmcontacts-rotation-shiftcoverage-dayofweek
            '''
            result = self._values.get("day_of_week")
            assert result is not None, "Required property 'day_of_week' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ShiftCoverageProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssmcontacts.CfnRotation.WeeklySettingProperty",
        jsii_struct_bases=[],
        name_mapping={"day_of_week": "dayOfWeek", "hand_off_time": "handOffTime"},
    )
    class WeeklySettingProperty:
        def __init__(
            self,
            *,
            day_of_week: builtins.str,
            hand_off_time: builtins.str,
        ) -> None:
            '''Information about rotations that recur weekly.

            :param day_of_week: The day of the week when weekly recurring on-call shift rotations begins.
            :param hand_off_time: The time of day when a weekly recurring on-call shift rotation begins.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-rotation-weeklysetting.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssmcontacts as ssmcontacts
                
                weekly_setting_property = ssmcontacts.CfnRotation.WeeklySettingProperty(
                    day_of_week="dayOfWeek",
                    hand_off_time="handOffTime"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c14404de3c73953c4e847ede12a15215fcadf495c7dffd1cc41c93ec2cf26200)
                check_type(argname="argument day_of_week", value=day_of_week, expected_type=type_hints["day_of_week"])
                check_type(argname="argument hand_off_time", value=hand_off_time, expected_type=type_hints["hand_off_time"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "day_of_week": day_of_week,
                "hand_off_time": hand_off_time,
            }

        @builtins.property
        def day_of_week(self) -> builtins.str:
            '''The day of the week when weekly recurring on-call shift rotations begins.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-rotation-weeklysetting.html#cfn-ssmcontacts-rotation-weeklysetting-dayofweek
            '''
            result = self._values.get("day_of_week")
            assert result is not None, "Required property 'day_of_week' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def hand_off_time(self) -> builtins.str:
            '''The time of day when a weekly recurring on-call shift rotation begins.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmcontacts-rotation-weeklysetting.html#cfn-ssmcontacts-rotation-weeklysetting-handofftime
            '''
            result = self._values.get("hand_off_time")
            assert result is not None, "Required property 'hand_off_time' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WeeklySettingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ssmcontacts.CfnRotationProps",
    jsii_struct_bases=[],
    name_mapping={
        "contact_ids": "contactIds",
        "name": "name",
        "recurrence": "recurrence",
        "start_time": "startTime",
        "time_zone_id": "timeZoneId",
        "tags": "tags",
    },
)
class CfnRotationProps:
    def __init__(
        self,
        *,
        contact_ids: typing.Sequence[builtins.str],
        name: builtins.str,
        recurrence: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRotation.RecurrenceSettingsProperty, typing.Dict[builtins.str, typing.Any]]],
        start_time: builtins.str,
        time_zone_id: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnRotation``.

        :param contact_ids: The Amazon Resource Names (ARNs) of the contacts to add to the rotation. The order in which you list the contacts is their shift order in the rotation schedule.
        :param name: The name for the rotation.
        :param recurrence: Information about the rule that specifies when shift team members rotate.
        :param start_time: The date and time the rotation goes into effect.
        :param time_zone_id: The time zone to base the rotation’s activity on, in Internet Assigned Numbers Authority (IANA) format. For example: "America/Los_Angeles", "UTC", or "Asia/Seoul". For more information, see the `Time Zone Database <https://docs.aws.amazon.com/https://www.iana.org/time-zones>`_ on the IANA website.
        :param tags: Optional metadata to assign to the rotation. Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment. For more information, see `Tagging Incident Manager resources <https://docs.aws.amazon.com/incident-manager/latest/userguide/tagging.html>`_ in the *Incident Manager User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-rotation.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ssmcontacts as ssmcontacts
            
            cfn_rotation_props = ssmcontacts.CfnRotationProps(
                contact_ids=["contactIds"],
                name="name",
                recurrence=ssmcontacts.CfnRotation.RecurrenceSettingsProperty(
                    number_of_on_calls=123,
                    recurrence_multiplier=123,
            
                    # the properties below are optional
                    daily_settings=["dailySettings"],
                    monthly_settings=[ssmcontacts.CfnRotation.MonthlySettingProperty(
                        day_of_month=123,
                        hand_off_time="handOffTime"
                    )],
                    shift_coverages=[ssmcontacts.CfnRotation.ShiftCoverageProperty(
                        coverage_times=[ssmcontacts.CfnRotation.CoverageTimeProperty(
                            end_time="endTime",
                            start_time="startTime"
                        )],
                        day_of_week="dayOfWeek"
                    )],
                    weekly_settings=[ssmcontacts.CfnRotation.WeeklySettingProperty(
                        day_of_week="dayOfWeek",
                        hand_off_time="handOffTime"
                    )]
                ),
                start_time="startTime",
                time_zone_id="timeZoneId",
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f29cf5a650f09297dec7b1ce2f14bd8b674754ea6d93bd8481ddf8a4ec8375f)
            check_type(argname="argument contact_ids", value=contact_ids, expected_type=type_hints["contact_ids"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument recurrence", value=recurrence, expected_type=type_hints["recurrence"])
            check_type(argname="argument start_time", value=start_time, expected_type=type_hints["start_time"])
            check_type(argname="argument time_zone_id", value=time_zone_id, expected_type=type_hints["time_zone_id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "contact_ids": contact_ids,
            "name": name,
            "recurrence": recurrence,
            "start_time": start_time,
            "time_zone_id": time_zone_id,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def contact_ids(self) -> typing.List[builtins.str]:
        '''The Amazon Resource Names (ARNs) of the contacts to add to the rotation.

        The order in which you list the contacts is their shift order in the rotation schedule.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-rotation.html#cfn-ssmcontacts-rotation-contactids
        '''
        result = self._values.get("contact_ids")
        assert result is not None, "Required property 'contact_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name for the rotation.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-rotation.html#cfn-ssmcontacts-rotation-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def recurrence(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnRotation.RecurrenceSettingsProperty]:
        '''Information about the rule that specifies when shift team members rotate.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-rotation.html#cfn-ssmcontacts-rotation-recurrence
        '''
        result = self._values.get("recurrence")
        assert result is not None, "Required property 'recurrence' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnRotation.RecurrenceSettingsProperty], result)

    @builtins.property
    def start_time(self) -> builtins.str:
        '''The date and time the rotation goes into effect.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-rotation.html#cfn-ssmcontacts-rotation-starttime
        '''
        result = self._values.get("start_time")
        assert result is not None, "Required property 'start_time' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def time_zone_id(self) -> builtins.str:
        '''The time zone to base the rotation’s activity on, in Internet Assigned Numbers Authority (IANA) format.

        For example: "America/Los_Angeles", "UTC", or "Asia/Seoul". For more information, see the `Time Zone Database <https://docs.aws.amazon.com/https://www.iana.org/time-zones>`_ on the IANA website.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-rotation.html#cfn-ssmcontacts-rotation-timezoneid
        '''
        result = self._values.get("time_zone_id")
        assert result is not None, "Required property 'time_zone_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Optional metadata to assign to the rotation.

        Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment. For more information, see `Tagging Incident Manager resources <https://docs.aws.amazon.com/incident-manager/latest/userguide/tagging.html>`_ in the *Incident Manager User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-rotation.html#cfn-ssmcontacts-rotation-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRotationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnContact",
    "CfnContactChannel",
    "CfnContactChannelProps",
    "CfnContactProps",
    "CfnPlan",
    "CfnPlanProps",
    "CfnRotation",
    "CfnRotationProps",
]

publication.publish()

def _typecheckingstub__96185056d36e15643884f48a931b8d7005ac84a62576223bb952c88328d7d90c(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    alias: builtins.str,
    display_name: builtins.str,
    type: builtins.str,
    plan: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContact.StageProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d145b029ad2942410a46b8ef97eda343598f927706f2322d3e0ecae3a114269c(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b081f8848b9d4742d3d4a3b6aa1dbb241d062469b6ef8e173e25b21525f7a27(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bba8290dd4eb067f8393c42927f143c8caf24ad18958b81d84a3b8407981a2c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55de424a70da49fdee77dff632e72d116d463a39a20c87708b14539025047922(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa02d91e10d2171d1f6f9fba4357f22de345c2007b02d0535df28e85a09c5c89(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b53265c2630d58664ca7f46c1ce619caeab6eec0dc5682af154a1d6e5fadc5b(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnContact.StageProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9859de101893bc6eb79fa20a2bb897c167951655effac5d46a65e9ddbe0e527(
    *,
    channel_id: builtins.str,
    retry_interval_in_minutes: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d65e32e1631ab40569f09ec16aaa5d8215a382cf1eb5593a2f809b42ba4936ad(
    *,
    contact_id: builtins.str,
    is_essential: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f305b28534efe8d339e08837352556855e9044627d7362d0ef784e32e9b4e6e(
    *,
    duration_in_minutes: typing.Optional[jsii.Number] = None,
    rotation_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    targets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContact.TargetsProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55603f1f49aeead31e2b8475c5647006fc8de1390e7ca4158f8c5047373348e2(
    *,
    channel_target_info: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContact.ChannelTargetInfoProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    contact_target_info: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContact.ContactTargetInfoProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1617a23866261103ffbfe512be7356fd9cfde9f098fbbb8abeafd44e741a1dea(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    channel_address: builtins.str,
    channel_name: builtins.str,
    channel_type: builtins.str,
    contact_id: builtins.str,
    defer_activation: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c79c2a0f8c2fcfce619e0d43bafe063c344e896341db65e50b14635676b3f64(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c8a7d2ebe7d9a66479c5bec6bb0d272cd150e7d9b19dccb5e0f02eecc1f2f02(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a5a7089d37931a755aff5c986c6109960e59c48f9af4ed79a8953b93ca748ec(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3bba3adfea78f0f5c6aec4ef81d3a19e05bcb6013d7d1557bd5d87a56b91406(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e76494fe71820cd79123d1c58f52f9734511b5f0e9ebc904568cc4a3614d236a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82ab7a7941dcaf019ff883ded9ab61de82e25ca982f876491b992626ec103136(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99b9167dee5265e65d4f53f0abd17410ef25ee43a5aaa99fd33f989d172a3844(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60153d8d82b752412e4b3852bb6bfda95115461ca88ac40d1598f699bd2681fd(
    *,
    channel_address: builtins.str,
    channel_name: builtins.str,
    channel_type: builtins.str,
    contact_id: builtins.str,
    defer_activation: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f741949260f507a90eb76a4ec5f8c03a5b8eeee237bc39b33a8add5cdc74d026(
    *,
    alias: builtins.str,
    display_name: builtins.str,
    type: builtins.str,
    plan: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContact.StageProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6e0c22680f733d3f22f01f5aa4b1401c09fcbf33bd52ea8ce6e156657761291(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    contact_id: builtins.str,
    rotation_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    stages: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPlan.StageProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__137ec9788a7a67aa1b51d2a0c7a6b9ed547385e0bf491539d328f6f2be03fcfe(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32b96bebac55eb6729cb601463e9b625faf9ce4e9fbabd3b393117d992fd302b(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59045e1db75e26927310a75a7663c8e46347a898fd847f92c5322b25b3166292(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7f8dbf20ba74a1032313ecba1522fc91898adade9f71310759089010f26013d(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98071cbe25b9c5fdcd471387b967afcc5792d313a75945efade94d8eb76ca785(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnPlan.StageProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84e76848537282e977dcde0f14f8ddb961f9ff06debd5fe09940f053ebe3cf2a(
    *,
    channel_id: builtins.str,
    retry_interval_in_minutes: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__610765f953ad183b666776caf683f78dbb8fa01e0c136d028fb058346bfde1ff(
    *,
    contact_id: builtins.str,
    is_essential: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23656d44cd1599e50fb9a1834c8723f0417861b7725022518d862812e406042b(
    *,
    duration_in_minutes: jsii.Number,
    targets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPlan.TargetsProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6975d159f87be06849c92d03bb48f0cd4d1b06bb5e3f9555822c686d405c5e4e(
    *,
    channel_target_info: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPlan.ChannelTargetInfoProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    contact_target_info: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPlan.ContactTargetInfoProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8efc2cb087519575d349f15e5f11bf8abf775e3bdb2501c2d28a6f2690c8f17f(
    *,
    contact_id: builtins.str,
    rotation_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    stages: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPlan.StageProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26eef7672fdd8123b01e699b8130ced5537ce3c542ab77ee1c6c06cb09cbf930(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    contact_ids: typing.Sequence[builtins.str],
    name: builtins.str,
    recurrence: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRotation.RecurrenceSettingsProperty, typing.Dict[builtins.str, typing.Any]]],
    start_time: builtins.str,
    time_zone_id: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__737a3930064adb508425fd82524f603fb39f45e289da49869aa4d8d4df27b36a(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b88c043eeb8e592d641499ebecdca207c839d7d68a19e163641d132e62530a4b(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1cbd1cbfab002f07a6d2bffee561f6c31760fc539bfe7a1e613f37f4e07fb206(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__947d78575ed0d1c185f504ba957c2e81b4696b00927ea2c6c79d4dc7a169dd19(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15da7772d8591fe2320b8ab1b99e597707b586730055c9d05111aeb272ccd4e9(
    value: typing.Union[_IResolvable_da3f097b, CfnRotation.RecurrenceSettingsProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c73526f3a03d5d0c27d0420ed51553cfdf3eb29e824bdee17839275d7c957cd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e822e7f1d29cbe95f2fb771175a652c3ae4e0cba9709976aee85050382d94b1c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a05c65df6e2e0154dd878cf7783bed608ad778e57fdc781109dc1f9297a2ff64(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5471c5c00a3ee14c4782530651c75ea7604939ef0fa51223f6a883ed7864ef9e(
    *,
    end_time: builtins.str,
    start_time: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4acc5d36b459ef219c0d9e8696ba8d79a8dc692c3d46f15b8f7590249f318c89(
    *,
    day_of_month: jsii.Number,
    hand_off_time: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c7e912eafde708159eeee02d146481d7aad1c73b0a5b641a391970ddad57bbb(
    *,
    number_of_on_calls: jsii.Number,
    recurrence_multiplier: jsii.Number,
    daily_settings: typing.Optional[typing.Sequence[builtins.str]] = None,
    monthly_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRotation.MonthlySettingProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    shift_coverages: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRotation.ShiftCoverageProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    weekly_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRotation.WeeklySettingProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9812f77378c4a6af9579759f5ec079ebc4b0cd0e6e34d34ad7898495e1e5ab2d(
    *,
    coverage_times: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRotation.CoverageTimeProperty, typing.Dict[builtins.str, typing.Any]]]]],
    day_of_week: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c14404de3c73953c4e847ede12a15215fcadf495c7dffd1cc41c93ec2cf26200(
    *,
    day_of_week: builtins.str,
    hand_off_time: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f29cf5a650f09297dec7b1ce2f14bd8b674754ea6d93bd8481ddf8a4ec8375f(
    *,
    contact_ids: typing.Sequence[builtins.str],
    name: builtins.str,
    recurrence: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRotation.RecurrenceSettingsProperty, typing.Dict[builtins.str, typing.Any]]],
    start_time: builtins.str,
    time_zone_id: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
