'''
# AWS::ConnectCampaigns Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_connectcampaigns as connectcampaigns
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for ConnectCampaigns construct libraries](https://constructs.dev/search?q=connectcampaigns)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::ConnectCampaigns resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ConnectCampaigns.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::ConnectCampaigns](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ConnectCampaigns.html).

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
class CfnCampaign(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_connectcampaigns.CfnCampaign",
):
    '''Contains information about an outbound campaign.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connectcampaigns-campaign.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_connectcampaigns as connectcampaigns
        
        cfn_campaign = connectcampaigns.CfnCampaign(self, "MyCfnCampaign",
            connect_instance_arn="connectInstanceArn",
            dialer_config=connectcampaigns.CfnCampaign.DialerConfigProperty(
                predictive_dialer_config=connectcampaigns.CfnCampaign.PredictiveDialerConfigProperty(
                    bandwidth_allocation=123
                ),
                progressive_dialer_config=connectcampaigns.CfnCampaign.ProgressiveDialerConfigProperty(
                    bandwidth_allocation=123
                )
            ),
            name="name",
            outbound_call_config=connectcampaigns.CfnCampaign.OutboundCallConfigProperty(
                connect_contact_flow_arn="connectContactFlowArn",
                connect_queue_arn="connectQueueArn",
        
                # the properties below are optional
                answer_machine_detection_config=connectcampaigns.CfnCampaign.AnswerMachineDetectionConfigProperty(
                    enable_answer_machine_detection=False
                ),
                connect_source_phone_number="connectSourcePhoneNumber"
            ),
        
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
        connect_instance_arn: builtins.str,
        dialer_config: typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.DialerConfigProperty", typing.Dict[builtins.str, typing.Any]]],
        name: builtins.str,
        outbound_call_config: typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.OutboundCallConfigProperty", typing.Dict[builtins.str, typing.Any]]],
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param connect_instance_arn: The Amazon Resource Name (ARN) of the Amazon Connect instance.
        :param dialer_config: Contains information about the dialer configuration.
        :param name: The name of the campaign.
        :param outbound_call_config: Contains information about the outbound call configuration.
        :param tags: The tags used to organize, track, or control access for this resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68b9f8ac97e8f86d700174c96cda66f647fb30af60f6ffc32c9ccb2a582ee9a0)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCampaignProps(
            connect_instance_arn=connect_instance_arn,
            dialer_config=dialer_config,
            name=name,
            outbound_call_config=outbound_call_config,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39c44d7ae2657f370c3369a7f586c71388393c54da2c114ac1e1c77d3622e226)
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
            type_hints = typing.get_type_hints(_typecheckingstub__62912ab1ca5ea937290b5c4b8df2bf3cbf48646798a3ffe4817e823fbcee00dd)
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
        '''The Amazon Resource Name (ARN) of the high-volume outbound campaign.

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
    @jsii.member(jsii_name="connectInstanceArn")
    def connect_instance_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the Amazon Connect instance.'''
        return typing.cast(builtins.str, jsii.get(self, "connectInstanceArn"))

    @connect_instance_arn.setter
    def connect_instance_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe29864d67b82be24e959cf62a974af0c74a7c193aec5dba50b8d29d34299660)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectInstanceArn", value)

    @builtins.property
    @jsii.member(jsii_name="dialerConfig")
    def dialer_config(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnCampaign.DialerConfigProperty"]:
        '''Contains information about the dialer configuration.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnCampaign.DialerConfigProperty"], jsii.get(self, "dialerConfig"))

    @dialer_config.setter
    def dialer_config(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnCampaign.DialerConfigProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05eabb5a0a6a496245f76aa9920497833d53b1213ccff6ad494e498a46c47a14)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dialerConfig", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the campaign.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad25aa27ecc92a37957bdba0e157baf267f271fe29d85d5a56df337e3fcea244)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="outboundCallConfig")
    def outbound_call_config(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnCampaign.OutboundCallConfigProperty"]:
        '''Contains information about the outbound call configuration.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnCampaign.OutboundCallConfigProperty"], jsii.get(self, "outboundCallConfig"))

    @outbound_call_config.setter
    def outbound_call_config(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnCampaign.OutboundCallConfigProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4ee8145c90e26f199a53bd3fd72ca4d855169b8677380927010a8d6804bcf36)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "outboundCallConfig", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64d80d4084c307fbea620c4f9e9d0b1c2cfa515ad7d021df43d430bf87d42b6b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connectcampaigns.CfnCampaign.AnswerMachineDetectionConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "enable_answer_machine_detection": "enableAnswerMachineDetection",
        },
    )
    class AnswerMachineDetectionConfigProperty:
        def __init__(
            self,
            *,
            enable_answer_machine_detection: typing.Union[builtins.bool, _IResolvable_da3f097b],
        ) -> None:
            '''The configuration used for answering machine detection during outbound calls.

            :param enable_answer_machine_detection: Flag to decided whether outbound calls should have answering machine detection enabled or not.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaigns-campaign-answermachinedetectionconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connectcampaigns as connectcampaigns
                
                answer_machine_detection_config_property = connectcampaigns.CfnCampaign.AnswerMachineDetectionConfigProperty(
                    enable_answer_machine_detection=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__17ddf057c50900b164cfd172d5d737d25a962fc39676bd1cbafcac6a1d8d60b3)
                check_type(argname="argument enable_answer_machine_detection", value=enable_answer_machine_detection, expected_type=type_hints["enable_answer_machine_detection"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "enable_answer_machine_detection": enable_answer_machine_detection,
            }

        @builtins.property
        def enable_answer_machine_detection(
            self,
        ) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''Flag to decided whether outbound calls should have answering machine detection enabled or not.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaigns-campaign-answermachinedetectionconfig.html#cfn-connectcampaigns-campaign-answermachinedetectionconfig-enableanswermachinedetection
            '''
            result = self._values.get("enable_answer_machine_detection")
            assert result is not None, "Required property 'enable_answer_machine_detection' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AnswerMachineDetectionConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connectcampaigns.CfnCampaign.DialerConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "predictive_dialer_config": "predictiveDialerConfig",
            "progressive_dialer_config": "progressiveDialerConfig",
        },
    )
    class DialerConfigProperty:
        def __init__(
            self,
            *,
            predictive_dialer_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.PredictiveDialerConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            progressive_dialer_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.ProgressiveDialerConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Contains dialer configuration for an outbound campaign.

            :param predictive_dialer_config: The configuration of the predictive dialer.
            :param progressive_dialer_config: The configuration of the progressive dialer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaigns-campaign-dialerconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connectcampaigns as connectcampaigns
                
                dialer_config_property = connectcampaigns.CfnCampaign.DialerConfigProperty(
                    predictive_dialer_config=connectcampaigns.CfnCampaign.PredictiveDialerConfigProperty(
                        bandwidth_allocation=123
                    ),
                    progressive_dialer_config=connectcampaigns.CfnCampaign.ProgressiveDialerConfigProperty(
                        bandwidth_allocation=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e897edcd7676c3bd3118030c1566c77bbb71b144de6d6d57265efe4b287d257c)
                check_type(argname="argument predictive_dialer_config", value=predictive_dialer_config, expected_type=type_hints["predictive_dialer_config"])
                check_type(argname="argument progressive_dialer_config", value=progressive_dialer_config, expected_type=type_hints["progressive_dialer_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if predictive_dialer_config is not None:
                self._values["predictive_dialer_config"] = predictive_dialer_config
            if progressive_dialer_config is not None:
                self._values["progressive_dialer_config"] = progressive_dialer_config

        @builtins.property
        def predictive_dialer_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.PredictiveDialerConfigProperty"]]:
            '''The configuration of the predictive dialer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaigns-campaign-dialerconfig.html#cfn-connectcampaigns-campaign-dialerconfig-predictivedialerconfig
            '''
            result = self._values.get("predictive_dialer_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.PredictiveDialerConfigProperty"]], result)

        @builtins.property
        def progressive_dialer_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.ProgressiveDialerConfigProperty"]]:
            '''The configuration of the progressive dialer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaigns-campaign-dialerconfig.html#cfn-connectcampaigns-campaign-dialerconfig-progressivedialerconfig
            '''
            result = self._values.get("progressive_dialer_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.ProgressiveDialerConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DialerConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connectcampaigns.CfnCampaign.OutboundCallConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "connect_contact_flow_arn": "connectContactFlowArn",
            "connect_queue_arn": "connectQueueArn",
            "answer_machine_detection_config": "answerMachineDetectionConfig",
            "connect_source_phone_number": "connectSourcePhoneNumber",
        },
    )
    class OutboundCallConfigProperty:
        def __init__(
            self,
            *,
            connect_contact_flow_arn: builtins.str,
            connect_queue_arn: builtins.str,
            answer_machine_detection_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.AnswerMachineDetectionConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            connect_source_phone_number: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Contains outbound call configuration for an outbound campaign.

            :param connect_contact_flow_arn: The Amazon Resource Name (ARN) of the flow.
            :param connect_queue_arn: The Amazon Resource Name (ARN) of the queue.
            :param answer_machine_detection_config: The configuration used for answering machine detection during outbound calls.
            :param connect_source_phone_number: The phone number associated with the outbound call. This is the caller ID that is displayed to customers when an agent calls them.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaigns-campaign-outboundcallconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connectcampaigns as connectcampaigns
                
                outbound_call_config_property = connectcampaigns.CfnCampaign.OutboundCallConfigProperty(
                    connect_contact_flow_arn="connectContactFlowArn",
                    connect_queue_arn="connectQueueArn",
                
                    # the properties below are optional
                    answer_machine_detection_config=connectcampaigns.CfnCampaign.AnswerMachineDetectionConfigProperty(
                        enable_answer_machine_detection=False
                    ),
                    connect_source_phone_number="connectSourcePhoneNumber"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b8cee2b14e882c5a034ae8d95b67ff1d2e709e6be191f570e955d736616d6eb1)
                check_type(argname="argument connect_contact_flow_arn", value=connect_contact_flow_arn, expected_type=type_hints["connect_contact_flow_arn"])
                check_type(argname="argument connect_queue_arn", value=connect_queue_arn, expected_type=type_hints["connect_queue_arn"])
                check_type(argname="argument answer_machine_detection_config", value=answer_machine_detection_config, expected_type=type_hints["answer_machine_detection_config"])
                check_type(argname="argument connect_source_phone_number", value=connect_source_phone_number, expected_type=type_hints["connect_source_phone_number"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "connect_contact_flow_arn": connect_contact_flow_arn,
                "connect_queue_arn": connect_queue_arn,
            }
            if answer_machine_detection_config is not None:
                self._values["answer_machine_detection_config"] = answer_machine_detection_config
            if connect_source_phone_number is not None:
                self._values["connect_source_phone_number"] = connect_source_phone_number

        @builtins.property
        def connect_contact_flow_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the flow.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaigns-campaign-outboundcallconfig.html#cfn-connectcampaigns-campaign-outboundcallconfig-connectcontactflowarn
            '''
            result = self._values.get("connect_contact_flow_arn")
            assert result is not None, "Required property 'connect_contact_flow_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def connect_queue_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the queue.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaigns-campaign-outboundcallconfig.html#cfn-connectcampaigns-campaign-outboundcallconfig-connectqueuearn
            '''
            result = self._values.get("connect_queue_arn")
            assert result is not None, "Required property 'connect_queue_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def answer_machine_detection_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.AnswerMachineDetectionConfigProperty"]]:
            '''The configuration used for answering machine detection during outbound calls.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaigns-campaign-outboundcallconfig.html#cfn-connectcampaigns-campaign-outboundcallconfig-answermachinedetectionconfig
            '''
            result = self._values.get("answer_machine_detection_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.AnswerMachineDetectionConfigProperty"]], result)

        @builtins.property
        def connect_source_phone_number(self) -> typing.Optional[builtins.str]:
            '''The phone number associated with the outbound call.

            This is the caller ID that is displayed to customers when an agent calls them.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaigns-campaign-outboundcallconfig.html#cfn-connectcampaigns-campaign-outboundcallconfig-connectsourcephonenumber
            '''
            result = self._values.get("connect_source_phone_number")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OutboundCallConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connectcampaigns.CfnCampaign.PredictiveDialerConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"bandwidth_allocation": "bandwidthAllocation"},
    )
    class PredictiveDialerConfigProperty:
        def __init__(self, *, bandwidth_allocation: jsii.Number) -> None:
            '''Contains predictive dialer configuration for an outbound campaign.

            :param bandwidth_allocation: Bandwidth allocation for the predictive dialer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaigns-campaign-predictivedialerconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connectcampaigns as connectcampaigns
                
                predictive_dialer_config_property = connectcampaigns.CfnCampaign.PredictiveDialerConfigProperty(
                    bandwidth_allocation=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c724c0f74af1f9984fbf7dfe87a74dec49da182fbf7872ed0f38d38f71340f1c)
                check_type(argname="argument bandwidth_allocation", value=bandwidth_allocation, expected_type=type_hints["bandwidth_allocation"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bandwidth_allocation": bandwidth_allocation,
            }

        @builtins.property
        def bandwidth_allocation(self) -> jsii.Number:
            '''Bandwidth allocation for the predictive dialer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaigns-campaign-predictivedialerconfig.html#cfn-connectcampaigns-campaign-predictivedialerconfig-bandwidthallocation
            '''
            result = self._values.get("bandwidth_allocation")
            assert result is not None, "Required property 'bandwidth_allocation' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PredictiveDialerConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connectcampaigns.CfnCampaign.ProgressiveDialerConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"bandwidth_allocation": "bandwidthAllocation"},
    )
    class ProgressiveDialerConfigProperty:
        def __init__(self, *, bandwidth_allocation: jsii.Number) -> None:
            '''Contains progressive dialer configuration for an outbound campaign.

            :param bandwidth_allocation: Bandwidth allocation for the progressive dialer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaigns-campaign-progressivedialerconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connectcampaigns as connectcampaigns
                
                progressive_dialer_config_property = connectcampaigns.CfnCampaign.ProgressiveDialerConfigProperty(
                    bandwidth_allocation=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2caead7a21c70720675b949fc77715602dacb36c26a48d0f8d60fbd06a51c69d)
                check_type(argname="argument bandwidth_allocation", value=bandwidth_allocation, expected_type=type_hints["bandwidth_allocation"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bandwidth_allocation": bandwidth_allocation,
            }

        @builtins.property
        def bandwidth_allocation(self) -> jsii.Number:
            '''Bandwidth allocation for the progressive dialer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaigns-campaign-progressivedialerconfig.html#cfn-connectcampaigns-campaign-progressivedialerconfig-bandwidthallocation
            '''
            result = self._values.get("bandwidth_allocation")
            assert result is not None, "Required property 'bandwidth_allocation' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ProgressiveDialerConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_connectcampaigns.CfnCampaignProps",
    jsii_struct_bases=[],
    name_mapping={
        "connect_instance_arn": "connectInstanceArn",
        "dialer_config": "dialerConfig",
        "name": "name",
        "outbound_call_config": "outboundCallConfig",
        "tags": "tags",
    },
)
class CfnCampaignProps:
    def __init__(
        self,
        *,
        connect_instance_arn: builtins.str,
        dialer_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.DialerConfigProperty, typing.Dict[builtins.str, typing.Any]]],
        name: builtins.str,
        outbound_call_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.OutboundCallConfigProperty, typing.Dict[builtins.str, typing.Any]]],
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnCampaign``.

        :param connect_instance_arn: The Amazon Resource Name (ARN) of the Amazon Connect instance.
        :param dialer_config: Contains information about the dialer configuration.
        :param name: The name of the campaign.
        :param outbound_call_config: Contains information about the outbound call configuration.
        :param tags: The tags used to organize, track, or control access for this resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connectcampaigns-campaign.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_connectcampaigns as connectcampaigns
            
            cfn_campaign_props = connectcampaigns.CfnCampaignProps(
                connect_instance_arn="connectInstanceArn",
                dialer_config=connectcampaigns.CfnCampaign.DialerConfigProperty(
                    predictive_dialer_config=connectcampaigns.CfnCampaign.PredictiveDialerConfigProperty(
                        bandwidth_allocation=123
                    ),
                    progressive_dialer_config=connectcampaigns.CfnCampaign.ProgressiveDialerConfigProperty(
                        bandwidth_allocation=123
                    )
                ),
                name="name",
                outbound_call_config=connectcampaigns.CfnCampaign.OutboundCallConfigProperty(
                    connect_contact_flow_arn="connectContactFlowArn",
                    connect_queue_arn="connectQueueArn",
            
                    # the properties below are optional
                    answer_machine_detection_config=connectcampaigns.CfnCampaign.AnswerMachineDetectionConfigProperty(
                        enable_answer_machine_detection=False
                    ),
                    connect_source_phone_number="connectSourcePhoneNumber"
                ),
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__748694bd997b98d4b10bb548a20e78ee9ae49587c645d81ccb2e226ae08399ad)
            check_type(argname="argument connect_instance_arn", value=connect_instance_arn, expected_type=type_hints["connect_instance_arn"])
            check_type(argname="argument dialer_config", value=dialer_config, expected_type=type_hints["dialer_config"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument outbound_call_config", value=outbound_call_config, expected_type=type_hints["outbound_call_config"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "connect_instance_arn": connect_instance_arn,
            "dialer_config": dialer_config,
            "name": name,
            "outbound_call_config": outbound_call_config,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def connect_instance_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the Amazon Connect instance.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connectcampaigns-campaign.html#cfn-connectcampaigns-campaign-connectinstancearn
        '''
        result = self._values.get("connect_instance_arn")
        assert result is not None, "Required property 'connect_instance_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dialer_config(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnCampaign.DialerConfigProperty]:
        '''Contains information about the dialer configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connectcampaigns-campaign.html#cfn-connectcampaigns-campaign-dialerconfig
        '''
        result = self._values.get("dialer_config")
        assert result is not None, "Required property 'dialer_config' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnCampaign.DialerConfigProperty], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the campaign.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connectcampaigns-campaign.html#cfn-connectcampaigns-campaign-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def outbound_call_config(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnCampaign.OutboundCallConfigProperty]:
        '''Contains information about the outbound call configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connectcampaigns-campaign.html#cfn-connectcampaigns-campaign-outboundcallconfig
        '''
        result = self._values.get("outbound_call_config")
        assert result is not None, "Required property 'outbound_call_config' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnCampaign.OutboundCallConfigProperty], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for this resource.

        For example, { "tags": {"key1":"value1", "key2":"value2"} }.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connectcampaigns-campaign.html#cfn-connectcampaigns-campaign-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCampaignProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnCampaign",
    "CfnCampaignProps",
]

publication.publish()

def _typecheckingstub__68b9f8ac97e8f86d700174c96cda66f647fb30af60f6ffc32c9ccb2a582ee9a0(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    connect_instance_arn: builtins.str,
    dialer_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.DialerConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    name: builtins.str,
    outbound_call_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.OutboundCallConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39c44d7ae2657f370c3369a7f586c71388393c54da2c114ac1e1c77d3622e226(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62912ab1ca5ea937290b5c4b8df2bf3cbf48646798a3ffe4817e823fbcee00dd(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe29864d67b82be24e959cf62a974af0c74a7c193aec5dba50b8d29d34299660(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05eabb5a0a6a496245f76aa9920497833d53b1213ccff6ad494e498a46c47a14(
    value: typing.Union[_IResolvable_da3f097b, CfnCampaign.DialerConfigProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad25aa27ecc92a37957bdba0e157baf267f271fe29d85d5a56df337e3fcea244(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4ee8145c90e26f199a53bd3fd72ca4d855169b8677380927010a8d6804bcf36(
    value: typing.Union[_IResolvable_da3f097b, CfnCampaign.OutboundCallConfigProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64d80d4084c307fbea620c4f9e9d0b1c2cfa515ad7d021df43d430bf87d42b6b(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17ddf057c50900b164cfd172d5d737d25a962fc39676bd1cbafcac6a1d8d60b3(
    *,
    enable_answer_machine_detection: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e897edcd7676c3bd3118030c1566c77bbb71b144de6d6d57265efe4b287d257c(
    *,
    predictive_dialer_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.PredictiveDialerConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    progressive_dialer_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.ProgressiveDialerConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8cee2b14e882c5a034ae8d95b67ff1d2e709e6be191f570e955d736616d6eb1(
    *,
    connect_contact_flow_arn: builtins.str,
    connect_queue_arn: builtins.str,
    answer_machine_detection_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.AnswerMachineDetectionConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    connect_source_phone_number: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c724c0f74af1f9984fbf7dfe87a74dec49da182fbf7872ed0f38d38f71340f1c(
    *,
    bandwidth_allocation: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2caead7a21c70720675b949fc77715602dacb36c26a48d0f8d60fbd06a51c69d(
    *,
    bandwidth_allocation: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__748694bd997b98d4b10bb548a20e78ee9ae49587c645d81ccb2e226ae08399ad(
    *,
    connect_instance_arn: builtins.str,
    dialer_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.DialerConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    name: builtins.str,
    outbound_call_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.OutboundCallConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
