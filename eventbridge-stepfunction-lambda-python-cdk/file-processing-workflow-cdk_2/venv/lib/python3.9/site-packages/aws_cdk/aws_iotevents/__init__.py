'''
# AWS::IoTEvents Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_iotevents as iotevents
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for IoTEvents construct libraries](https://constructs.dev/search?q=iotevents)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::IoTEvents resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_IoTEvents.html) directly.

> An experimental construct library for this service is available in preview. Since it is not stable yet, it is distributed
> as a separate package so that you can pin its version independently of the rest of the CDK. See the package:
>
> <span class="package-reference">@aws-cdk/aws-iotevents-alpha</span>

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::IoTEvents](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_IoTEvents.html).

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
class CfnAlarmModel(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iotevents.CfnAlarmModel",
):
    '''Represents an alarm model to monitor an AWS IoT Events input attribute.

    You can use the alarm to get notified when the value is outside a specified range. For more information, see `Create an alarm model <https://docs.aws.amazon.com/iotevents/latest/developerguide/create-alarms.html>`_ in the *AWS IoT Events Developer Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-alarmmodel.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iotevents as iotevents
        
        cfn_alarm_model = iotevents.CfnAlarmModel(self, "MyCfnAlarmModel",
            alarm_rule=iotevents.CfnAlarmModel.AlarmRuleProperty(
                simple_rule=iotevents.CfnAlarmModel.SimpleRuleProperty(
                    comparison_operator="comparisonOperator",
                    input_property="inputProperty",
                    threshold="threshold"
                )
            ),
            role_arn="roleArn",
        
            # the properties below are optional
            alarm_capabilities=iotevents.CfnAlarmModel.AlarmCapabilitiesProperty(
                acknowledge_flow=iotevents.CfnAlarmModel.AcknowledgeFlowProperty(
                    enabled=False
                ),
                initialization_configuration=iotevents.CfnAlarmModel.InitializationConfigurationProperty(
                    disabled_on_initialization=False
                )
            ),
            alarm_event_actions=iotevents.CfnAlarmModel.AlarmEventActionsProperty(
                alarm_actions=[iotevents.CfnAlarmModel.AlarmActionProperty(
                    dynamo_db=iotevents.CfnAlarmModel.DynamoDBProperty(
                        hash_key_field="hashKeyField",
                        hash_key_value="hashKeyValue",
                        table_name="tableName",
        
                        # the properties below are optional
                        hash_key_type="hashKeyType",
                        operation="operation",
                        payload=iotevents.CfnAlarmModel.PayloadProperty(
                            content_expression="contentExpression",
                            type="type"
                        ),
                        payload_field="payloadField",
                        range_key_field="rangeKeyField",
                        range_key_type="rangeKeyType",
                        range_key_value="rangeKeyValue"
                    ),
                    dynamo_dBv2=iotevents.CfnAlarmModel.DynamoDBv2Property(
                        table_name="tableName",
        
                        # the properties below are optional
                        payload=iotevents.CfnAlarmModel.PayloadProperty(
                            content_expression="contentExpression",
                            type="type"
                        )
                    ),
                    firehose=iotevents.CfnAlarmModel.FirehoseProperty(
                        delivery_stream_name="deliveryStreamName",
        
                        # the properties below are optional
                        payload=iotevents.CfnAlarmModel.PayloadProperty(
                            content_expression="contentExpression",
                            type="type"
                        ),
                        separator="separator"
                    ),
                    iot_events=iotevents.CfnAlarmModel.IotEventsProperty(
                        input_name="inputName",
        
                        # the properties below are optional
                        payload=iotevents.CfnAlarmModel.PayloadProperty(
                            content_expression="contentExpression",
                            type="type"
                        )
                    ),
                    iot_site_wise=iotevents.CfnAlarmModel.IotSiteWiseProperty(
                        asset_id="assetId",
                        entry_id="entryId",
                        property_alias="propertyAlias",
                        property_id="propertyId",
                        property_value=iotevents.CfnAlarmModel.AssetPropertyValueProperty(
                            value=iotevents.CfnAlarmModel.AssetPropertyVariantProperty(
                                boolean_value="booleanValue",
                                double_value="doubleValue",
                                integer_value="integerValue",
                                string_value="stringValue"
                            ),
        
                            # the properties below are optional
                            quality="quality",
                            timestamp=iotevents.CfnAlarmModel.AssetPropertyTimestampProperty(
                                time_in_seconds="timeInSeconds",
        
                                # the properties below are optional
                                offset_in_nanos="offsetInNanos"
                            )
                        )
                    ),
                    iot_topic_publish=iotevents.CfnAlarmModel.IotTopicPublishProperty(
                        mqtt_topic="mqttTopic",
        
                        # the properties below are optional
                        payload=iotevents.CfnAlarmModel.PayloadProperty(
                            content_expression="contentExpression",
                            type="type"
                        )
                    ),
                    lambda_=iotevents.CfnAlarmModel.LambdaProperty(
                        function_arn="functionArn",
        
                        # the properties below are optional
                        payload=iotevents.CfnAlarmModel.PayloadProperty(
                            content_expression="contentExpression",
                            type="type"
                        )
                    ),
                    sns=iotevents.CfnAlarmModel.SnsProperty(
                        target_arn="targetArn",
        
                        # the properties below are optional
                        payload=iotevents.CfnAlarmModel.PayloadProperty(
                            content_expression="contentExpression",
                            type="type"
                        )
                    ),
                    sqs=iotevents.CfnAlarmModel.SqsProperty(
                        queue_url="queueUrl",
        
                        # the properties below are optional
                        payload=iotevents.CfnAlarmModel.PayloadProperty(
                            content_expression="contentExpression",
                            type="type"
                        ),
                        use_base64=False
                    )
                )]
            ),
            alarm_model_description="alarmModelDescription",
            alarm_model_name="alarmModelName",
            key="key",
            severity=123,
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
        alarm_rule: typing.Union[_IResolvable_da3f097b, typing.Union["CfnAlarmModel.AlarmRuleProperty", typing.Dict[builtins.str, typing.Any]]],
        role_arn: builtins.str,
        alarm_capabilities: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAlarmModel.AlarmCapabilitiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        alarm_event_actions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAlarmModel.AlarmEventActionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        alarm_model_description: typing.Optional[builtins.str] = None,
        alarm_model_name: typing.Optional[builtins.str] = None,
        key: typing.Optional[builtins.str] = None,
        severity: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param alarm_rule: Defines when your alarm is invoked.
        :param role_arn: The ARN of the IAM role that allows the alarm to perform actions and access AWS resources. For more information, see `Amazon Resource Names (ARNs) <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`_ in the *AWS General Reference* .
        :param alarm_capabilities: Contains the configuration information of alarm state changes.
        :param alarm_event_actions: Contains information about one or more alarm actions.
        :param alarm_model_description: The description of the alarm model.
        :param alarm_model_name: The name of the alarm model.
        :param key: An input attribute used as a key to create an alarm. AWS IoT Events routes `inputs <https://docs.aws.amazon.com/iotevents/latest/apireference/API_Input.html>`_ associated with this key to the alarm.
        :param severity: A non-negative integer that reflects the severity level of the alarm.
        :param tags: A list of key-value pairs that contain metadata for the alarm model. The tags help you manage the alarm model. For more information, see `Tagging your AWS IoT Events resources <https://docs.aws.amazon.com/iotevents/latest/developerguide/tagging-iotevents.html>`_ in the *AWS IoT Events Developer Guide* . You can create up to 50 tags for one alarm model.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef7f48b87ae58ab2d16bfb25fbcc61ae8753eb0c9a5b0016eec37a52e79b7a7d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAlarmModelProps(
            alarm_rule=alarm_rule,
            role_arn=role_arn,
            alarm_capabilities=alarm_capabilities,
            alarm_event_actions=alarm_event_actions,
            alarm_model_description=alarm_model_description,
            alarm_model_name=alarm_model_name,
            key=key,
            severity=severity,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29efb49b22ff313d9ee99306ea7ca4bf99648d4ec281ef880884544374a005e5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__05b98ff8d3be84f09516f43c45c6be0ea4a8c084c6b193e977f2739cd0e26d54)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

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
    @jsii.member(jsii_name="alarmRule")
    def alarm_rule(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnAlarmModel.AlarmRuleProperty"]:
        '''Defines when your alarm is invoked.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnAlarmModel.AlarmRuleProperty"], jsii.get(self, "alarmRule"))

    @alarm_rule.setter
    def alarm_rule(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnAlarmModel.AlarmRuleProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36c0e05874a966c4cf11e13423d2cf0b8945f4dafb03af1bb65b04fe1f904e1c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alarmRule", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''The ARN of the IAM role that allows the alarm to perform actions and access AWS resources.'''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__667c04eef9049300d49a54887f048621c4279fc765df4962bf383ab77e428d5c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="alarmCapabilities")
    def alarm_capabilities(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAlarmModel.AlarmCapabilitiesProperty"]]:
        '''Contains the configuration information of alarm state changes.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAlarmModel.AlarmCapabilitiesProperty"]], jsii.get(self, "alarmCapabilities"))

    @alarm_capabilities.setter
    def alarm_capabilities(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAlarmModel.AlarmCapabilitiesProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d85be71c4d51b50fc44306a17518e6e2409c133128f31c26dcdf967abb3e0ec7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alarmCapabilities", value)

    @builtins.property
    @jsii.member(jsii_name="alarmEventActions")
    def alarm_event_actions(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAlarmModel.AlarmEventActionsProperty"]]:
        '''Contains information about one or more alarm actions.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAlarmModel.AlarmEventActionsProperty"]], jsii.get(self, "alarmEventActions"))

    @alarm_event_actions.setter
    def alarm_event_actions(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAlarmModel.AlarmEventActionsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8227f73f350bd144d86be0ccf98762b44508b027f4ffb7aef8e68eeaafd91ecd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alarmEventActions", value)

    @builtins.property
    @jsii.member(jsii_name="alarmModelDescription")
    def alarm_model_description(self) -> typing.Optional[builtins.str]:
        '''The description of the alarm model.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alarmModelDescription"))

    @alarm_model_description.setter
    def alarm_model_description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b540895073c6ca51a688168fe27abe8c0bc5df06473c9a8e026f6b4a5c1881f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alarmModelDescription", value)

    @builtins.property
    @jsii.member(jsii_name="alarmModelName")
    def alarm_model_name(self) -> typing.Optional[builtins.str]:
        '''The name of the alarm model.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alarmModelName"))

    @alarm_model_name.setter
    def alarm_model_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2520aa074d1ed7d38b09cd7416997eb16982c8c7dc7a4340e5fd1178569cc01a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alarmModelName", value)

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> typing.Optional[builtins.str]:
        '''An input attribute used as a key to create an alarm.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "key"))

    @key.setter
    def key(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f86ab353b386a192172ab818d729e6584ca5b5df31c6e550f1e7986ea1ce3026)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="severity")
    def severity(self) -> typing.Optional[jsii.Number]:
        '''A non-negative integer that reflects the severity level of the alarm.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "severity"))

    @severity.setter
    def severity(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc04b5b9d376105aa5bf470e04873d2255ed6412dbf222f2dbc18a074c52ed49)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "severity", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of key-value pairs that contain metadata for the alarm model.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__877eb82e1ea1e65eaa71c65808ed46b8a70c4cbff438aa7f010439bd4b409dcb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotevents.CfnAlarmModel.AcknowledgeFlowProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled": "enabled"},
    )
    class AcknowledgeFlowProperty:
        def __init__(
            self,
            *,
            enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Specifies whether to get notified for alarm state changes.

            :param enabled: The value must be ``TRUE`` or ``FALSE`` . If ``TRUE`` , you receive a notification when the alarm state changes. You must choose to acknowledge the notification before the alarm state can return to ``NORMAL`` . If ``FALSE`` , you won't receive notifications. The alarm automatically changes to the ``NORMAL`` state when the input property value returns to the specified range.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-acknowledgeflow.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotevents as iotevents
                
                acknowledge_flow_property = iotevents.CfnAlarmModel.AcknowledgeFlowProperty(
                    enabled=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6cf300e297184ec092d4441ac920d284db156ae6cb1ff9f0dde90b454a739267)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if enabled is not None:
                self._values["enabled"] = enabled

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''The value must be ``TRUE`` or ``FALSE`` .

            If ``TRUE`` , you receive a notification when the alarm state changes. You must choose to acknowledge the notification before the alarm state can return to ``NORMAL`` . If ``FALSE`` , you won't receive notifications. The alarm automatically changes to the ``NORMAL`` state when the input property value returns to the specified range.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-acknowledgeflow.html#cfn-iotevents-alarmmodel-acknowledgeflow-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AcknowledgeFlowProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotevents.CfnAlarmModel.AlarmActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "dynamo_db": "dynamoDb",
            "dynamo_d_bv2": "dynamoDBv2",
            "firehose": "firehose",
            "iot_events": "iotEvents",
            "iot_site_wise": "iotSiteWise",
            "iot_topic_publish": "iotTopicPublish",
            "lambda_": "lambda",
            "sns": "sns",
            "sqs": "sqs",
        },
    )
    class AlarmActionProperty:
        def __init__(
            self,
            *,
            dynamo_db: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAlarmModel.DynamoDBProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            dynamo_d_bv2: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAlarmModel.DynamoDBv2Property", typing.Dict[builtins.str, typing.Any]]]] = None,
            firehose: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAlarmModel.FirehoseProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            iot_events: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAlarmModel.IotEventsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            iot_site_wise: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAlarmModel.IotSiteWiseProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            iot_topic_publish: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAlarmModel.IotTopicPublishProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            lambda_: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAlarmModel.LambdaProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            sns: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAlarmModel.SnsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            sqs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAlarmModel.SqsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Specifies one of the following actions to receive notifications when the alarm state changes.

            :param dynamo_db: Defines an action to write to the Amazon DynamoDB table that you created. The standard action payload contains all the information about the detector model instance and the event that triggered the action. You can customize the `payload <https://docs.aws.amazon.com/iotevents/latest/apireference/API_Payload.html>`_ . One column of the DynamoDB table receives all attribute-value pairs in the payload that you specify. You must use expressions for all parameters in ``DynamoDBAction`` . The expressions accept literals, operators, functions, references, and substitution templates. **Examples** - For literal values, the expressions must contain single quotes. For example, the value for the ``hashKeyType`` parameter can be ``'STRING'`` . - For references, you must specify either variables or input values. For example, the value for the ``hashKeyField`` parameter can be ``$input.GreenhouseInput.name`` . - For a substitution template, you must use ``${}`` , and the template must be in single quotes. A substitution template can also contain a combination of literals, operators, functions, references, and substitution templates. In the following example, the value for the ``hashKeyValue`` parameter uses a substitution template. ``'${$input.GreenhouseInput.temperature * 6 / 5 + 32} in Fahrenheit'`` - For a string concatenation, you must use ``+`` . A string concatenation can also contain a combination of literals, operators, functions, references, and substitution templates. In the following example, the value for the ``tableName`` parameter uses a string concatenation. ``'GreenhouseTemperatureTable ' + $input.GreenhouseInput.date`` For more information, see `Expressions <https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-expressions.html>`_ in the *AWS IoT Events Developer Guide* . If the defined payload type is a string, ``DynamoDBAction`` writes non-JSON data to the DynamoDB table as binary data. The DynamoDB console displays the data as Base64-encoded text. The value for the ``payloadField`` parameter is ``<payload-field>_raw`` .
            :param dynamo_d_bv2: Defines an action to write to the Amazon DynamoDB table that you created. The default action payload contains all the information about the detector model instance and the event that triggered the action. You can customize the `payload <https://docs.aws.amazon.com/iotevents/latest/apireference/API_Payload.html>`_ . A separate column of the DynamoDB table receives one attribute-value pair in the payload that you specify. You must use expressions for all parameters in ``DynamoDBv2Action`` . The expressions accept literals, operators, functions, references, and substitution templates. **Examples** - For literal values, the expressions must contain single quotes. For example, the value for the ``tableName`` parameter can be ``'GreenhouseTemperatureTable'`` . - For references, you must specify either variables or input values. For example, the value for the ``tableName`` parameter can be ``$variable.ddbtableName`` . - For a substitution template, you must use ``${}`` , and the template must be in single quotes. A substitution template can also contain a combination of literals, operators, functions, references, and substitution templates. In the following example, the value for the ``contentExpression`` parameter in ``Payload`` uses a substitution template. ``'{\\"sensorID\\": \\"${$input.GreenhouseInput.sensor_id}\\", \\"temperature\\": \\"${$input.GreenhouseInput.temperature * 9 / 5 + 32}\\"}'`` - For a string concatenation, you must use ``+`` . A string concatenation can also contain a combination of literals, operators, functions, references, and substitution templates. In the following example, the value for the ``tableName`` parameter uses a string concatenation. ``'GreenhouseTemperatureTable ' + $input.GreenhouseInput.date`` For more information, see `Expressions <https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-expressions.html>`_ in the *AWS IoT Events Developer Guide* . The value for the ``type`` parameter in ``Payload`` must be ``JSON`` .
            :param firehose: Sends information about the detector model instance and the event that triggered the action to an Amazon Kinesis Data Firehose delivery stream.
            :param iot_events: Sends an AWS IoT Events input, passing in information about the detector model instance and the event that triggered the action.
            :param iot_site_wise: Sends information about the detector model instance and the event that triggered the action to a specified asset property in AWS IoT SiteWise . You must use expressions for all parameters in ``IotSiteWiseAction`` . The expressions accept literals, operators, functions, references, and substitutions templates. **Examples** - For literal values, the expressions must contain single quotes. For example, the value for the ``propertyAlias`` parameter can be ``'/company/windfarm/3/turbine/7/temperature'`` . - For references, you must specify either variables or input values. For example, the value for the ``assetId`` parameter can be ``$input.TurbineInput.assetId1`` . - For a substitution template, you must use ``${}`` , and the template must be in single quotes. A substitution template can also contain a combination of literals, operators, functions, references, and substitution templates. In the following example, the value for the ``propertyAlias`` parameter uses a substitution template. ``'company/windfarm/${$input.TemperatureInput.sensorData.windfarmID}/turbine/ ${$input.TemperatureInput.sensorData.turbineID}/temperature'`` You must specify either ``propertyAlias`` or both ``assetId`` and ``propertyId`` to identify the target asset property in AWS IoT SiteWise . For more information, see `Expressions <https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-expressions.html>`_ in the *AWS IoT Events Developer Guide* .
            :param iot_topic_publish: Information required to publish the MQTT message through the AWS IoT message broker.
            :param lambda_: Calls a Lambda function, passing in information about the detector model instance and the event that triggered the action.
            :param sns: Information required to publish the Amazon SNS message.
            :param sqs: Sends information about the detector model instance and the event that triggered the action to an Amazon SQS queue.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-alarmaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotevents as iotevents
                
                alarm_action_property = iotevents.CfnAlarmModel.AlarmActionProperty(
                    dynamo_db=iotevents.CfnAlarmModel.DynamoDBProperty(
                        hash_key_field="hashKeyField",
                        hash_key_value="hashKeyValue",
                        table_name="tableName",
                
                        # the properties below are optional
                        hash_key_type="hashKeyType",
                        operation="operation",
                        payload=iotevents.CfnAlarmModel.PayloadProperty(
                            content_expression="contentExpression",
                            type="type"
                        ),
                        payload_field="payloadField",
                        range_key_field="rangeKeyField",
                        range_key_type="rangeKeyType",
                        range_key_value="rangeKeyValue"
                    ),
                    dynamo_dBv2=iotevents.CfnAlarmModel.DynamoDBv2Property(
                        table_name="tableName",
                
                        # the properties below are optional
                        payload=iotevents.CfnAlarmModel.PayloadProperty(
                            content_expression="contentExpression",
                            type="type"
                        )
                    ),
                    firehose=iotevents.CfnAlarmModel.FirehoseProperty(
                        delivery_stream_name="deliveryStreamName",
                
                        # the properties below are optional
                        payload=iotevents.CfnAlarmModel.PayloadProperty(
                            content_expression="contentExpression",
                            type="type"
                        ),
                        separator="separator"
                    ),
                    iot_events=iotevents.CfnAlarmModel.IotEventsProperty(
                        input_name="inputName",
                
                        # the properties below are optional
                        payload=iotevents.CfnAlarmModel.PayloadProperty(
                            content_expression="contentExpression",
                            type="type"
                        )
                    ),
                    iot_site_wise=iotevents.CfnAlarmModel.IotSiteWiseProperty(
                        asset_id="assetId",
                        entry_id="entryId",
                        property_alias="propertyAlias",
                        property_id="propertyId",
                        property_value=iotevents.CfnAlarmModel.AssetPropertyValueProperty(
                            value=iotevents.CfnAlarmModel.AssetPropertyVariantProperty(
                                boolean_value="booleanValue",
                                double_value="doubleValue",
                                integer_value="integerValue",
                                string_value="stringValue"
                            ),
                
                            # the properties below are optional
                            quality="quality",
                            timestamp=iotevents.CfnAlarmModel.AssetPropertyTimestampProperty(
                                time_in_seconds="timeInSeconds",
                
                                # the properties below are optional
                                offset_in_nanos="offsetInNanos"
                            )
                        )
                    ),
                    iot_topic_publish=iotevents.CfnAlarmModel.IotTopicPublishProperty(
                        mqtt_topic="mqttTopic",
                
                        # the properties below are optional
                        payload=iotevents.CfnAlarmModel.PayloadProperty(
                            content_expression="contentExpression",
                            type="type"
                        )
                    ),
                    lambda_=iotevents.CfnAlarmModel.LambdaProperty(
                        function_arn="functionArn",
                
                        # the properties below are optional
                        payload=iotevents.CfnAlarmModel.PayloadProperty(
                            content_expression="contentExpression",
                            type="type"
                        )
                    ),
                    sns=iotevents.CfnAlarmModel.SnsProperty(
                        target_arn="targetArn",
                
                        # the properties below are optional
                        payload=iotevents.CfnAlarmModel.PayloadProperty(
                            content_expression="contentExpression",
                            type="type"
                        )
                    ),
                    sqs=iotevents.CfnAlarmModel.SqsProperty(
                        queue_url="queueUrl",
                
                        # the properties below are optional
                        payload=iotevents.CfnAlarmModel.PayloadProperty(
                            content_expression="contentExpression",
                            type="type"
                        ),
                        use_base64=False
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ab691bc61d6c876d3c04cfc2eaaae2a144273102c7fd7065a4db407ff0bac487)
                check_type(argname="argument dynamo_db", value=dynamo_db, expected_type=type_hints["dynamo_db"])
                check_type(argname="argument dynamo_d_bv2", value=dynamo_d_bv2, expected_type=type_hints["dynamo_d_bv2"])
                check_type(argname="argument firehose", value=firehose, expected_type=type_hints["firehose"])
                check_type(argname="argument iot_events", value=iot_events, expected_type=type_hints["iot_events"])
                check_type(argname="argument iot_site_wise", value=iot_site_wise, expected_type=type_hints["iot_site_wise"])
                check_type(argname="argument iot_topic_publish", value=iot_topic_publish, expected_type=type_hints["iot_topic_publish"])
                check_type(argname="argument lambda_", value=lambda_, expected_type=type_hints["lambda_"])
                check_type(argname="argument sns", value=sns, expected_type=type_hints["sns"])
                check_type(argname="argument sqs", value=sqs, expected_type=type_hints["sqs"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if dynamo_db is not None:
                self._values["dynamo_db"] = dynamo_db
            if dynamo_d_bv2 is not None:
                self._values["dynamo_d_bv2"] = dynamo_d_bv2
            if firehose is not None:
                self._values["firehose"] = firehose
            if iot_events is not None:
                self._values["iot_events"] = iot_events
            if iot_site_wise is not None:
                self._values["iot_site_wise"] = iot_site_wise
            if iot_topic_publish is not None:
                self._values["iot_topic_publish"] = iot_topic_publish
            if lambda_ is not None:
                self._values["lambda_"] = lambda_
            if sns is not None:
                self._values["sns"] = sns
            if sqs is not None:
                self._values["sqs"] = sqs

        @builtins.property
        def dynamo_db(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAlarmModel.DynamoDBProperty"]]:
            '''Defines an action to write to the Amazon DynamoDB table that you created.

            The standard action payload contains all the information about the detector model instance and the event that triggered the action. You can customize the `payload <https://docs.aws.amazon.com/iotevents/latest/apireference/API_Payload.html>`_ . One column of the DynamoDB table receives all attribute-value pairs in the payload that you specify.

            You must use expressions for all parameters in ``DynamoDBAction`` . The expressions accept literals, operators, functions, references, and substitution templates.

            **Examples** - For literal values, the expressions must contain single quotes. For example, the value for the ``hashKeyType`` parameter can be ``'STRING'`` .

            - For references, you must specify either variables or input values. For example, the value for the ``hashKeyField`` parameter can be ``$input.GreenhouseInput.name`` .
            - For a substitution template, you must use ``${}`` , and the template must be in single quotes. A substitution template can also contain a combination of literals, operators, functions, references, and substitution templates.

            In the following example, the value for the ``hashKeyValue`` parameter uses a substitution template.

            ``'${$input.GreenhouseInput.temperature * 6 / 5 + 32} in Fahrenheit'``

            - For a string concatenation, you must use ``+`` . A string concatenation can also contain a combination of literals, operators, functions, references, and substitution templates.

            In the following example, the value for the ``tableName`` parameter uses a string concatenation.

            ``'GreenhouseTemperatureTable ' + $input.GreenhouseInput.date``

            For more information, see `Expressions <https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-expressions.html>`_ in the *AWS IoT Events Developer Guide* .

            If the defined payload type is a string, ``DynamoDBAction`` writes non-JSON data to the DynamoDB table as binary data. The DynamoDB console displays the data as Base64-encoded text. The value for the ``payloadField`` parameter is ``<payload-field>_raw`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-alarmaction.html#cfn-iotevents-alarmmodel-alarmaction-dynamodb
            '''
            result = self._values.get("dynamo_db")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAlarmModel.DynamoDBProperty"]], result)

        @builtins.property
        def dynamo_d_bv2(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAlarmModel.DynamoDBv2Property"]]:
            '''Defines an action to write to the Amazon DynamoDB table that you created.

            The default action payload contains all the information about the detector model instance and the event that triggered the action. You can customize the `payload <https://docs.aws.amazon.com/iotevents/latest/apireference/API_Payload.html>`_ . A separate column of the DynamoDB table receives one attribute-value pair in the payload that you specify.

            You must use expressions for all parameters in ``DynamoDBv2Action`` . The expressions accept literals, operators, functions, references, and substitution templates.

            **Examples** - For literal values, the expressions must contain single quotes. For example, the value for the ``tableName`` parameter can be ``'GreenhouseTemperatureTable'`` .

            - For references, you must specify either variables or input values. For example, the value for the ``tableName`` parameter can be ``$variable.ddbtableName`` .
            - For a substitution template, you must use ``${}`` , and the template must be in single quotes. A substitution template can also contain a combination of literals, operators, functions, references, and substitution templates.

            In the following example, the value for the ``contentExpression`` parameter in ``Payload`` uses a substitution template.

            ``'{\\"sensorID\\": \\"${$input.GreenhouseInput.sensor_id}\\", \\"temperature\\": \\"${$input.GreenhouseInput.temperature * 9 / 5 + 32}\\"}'``

            - For a string concatenation, you must use ``+`` . A string concatenation can also contain a combination of literals, operators, functions, references, and substitution templates.

            In the following example, the value for the ``tableName`` parameter uses a string concatenation.

            ``'GreenhouseTemperatureTable ' + $input.GreenhouseInput.date``

            For more information, see `Expressions <https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-expressions.html>`_ in the *AWS IoT Events Developer Guide* .

            The value for the ``type`` parameter in ``Payload`` must be ``JSON`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-alarmaction.html#cfn-iotevents-alarmmodel-alarmaction-dynamodbv2
            '''
            result = self._values.get("dynamo_d_bv2")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAlarmModel.DynamoDBv2Property"]], result)

        @builtins.property
        def firehose(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAlarmModel.FirehoseProperty"]]:
            '''Sends information about the detector model instance and the event that triggered the action to an Amazon Kinesis Data Firehose delivery stream.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-alarmaction.html#cfn-iotevents-alarmmodel-alarmaction-firehose
            '''
            result = self._values.get("firehose")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAlarmModel.FirehoseProperty"]], result)

        @builtins.property
        def iot_events(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAlarmModel.IotEventsProperty"]]:
            '''Sends an AWS IoT Events input, passing in information about the detector model instance and the event that triggered the action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-alarmaction.html#cfn-iotevents-alarmmodel-alarmaction-iotevents
            '''
            result = self._values.get("iot_events")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAlarmModel.IotEventsProperty"]], result)

        @builtins.property
        def iot_site_wise(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAlarmModel.IotSiteWiseProperty"]]:
            '''Sends information about the detector model instance and the event that triggered the action to a specified asset property in AWS IoT SiteWise .

            You must use expressions for all parameters in ``IotSiteWiseAction`` . The expressions accept literals, operators, functions, references, and substitutions templates.

            **Examples** - For literal values, the expressions must contain single quotes. For example, the value for the ``propertyAlias`` parameter can be ``'/company/windfarm/3/turbine/7/temperature'`` .

            - For references, you must specify either variables or input values. For example, the value for the ``assetId`` parameter can be ``$input.TurbineInput.assetId1`` .
            - For a substitution template, you must use ``${}`` , and the template must be in single quotes. A substitution template can also contain a combination of literals, operators, functions, references, and substitution templates.

            In the following example, the value for the ``propertyAlias`` parameter uses a substitution template.

            ``'company/windfarm/${$input.TemperatureInput.sensorData.windfarmID}/turbine/ ${$input.TemperatureInput.sensorData.turbineID}/temperature'``

            You must specify either ``propertyAlias`` or both ``assetId`` and ``propertyId`` to identify the target asset property in AWS IoT SiteWise .

            For more information, see `Expressions <https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-expressions.html>`_ in the *AWS IoT Events Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-alarmaction.html#cfn-iotevents-alarmmodel-alarmaction-iotsitewise
            '''
            result = self._values.get("iot_site_wise")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAlarmModel.IotSiteWiseProperty"]], result)

        @builtins.property
        def iot_topic_publish(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAlarmModel.IotTopicPublishProperty"]]:
            '''Information required to publish the MQTT message through the AWS IoT message broker.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-alarmaction.html#cfn-iotevents-alarmmodel-alarmaction-iottopicpublish
            '''
            result = self._values.get("iot_topic_publish")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAlarmModel.IotTopicPublishProperty"]], result)

        @builtins.property
        def lambda_(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAlarmModel.LambdaProperty"]]:
            '''Calls a Lambda function, passing in information about the detector model instance and the event that triggered the action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-alarmaction.html#cfn-iotevents-alarmmodel-alarmaction-lambda
            '''
            result = self._values.get("lambda_")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAlarmModel.LambdaProperty"]], result)

        @builtins.property
        def sns(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAlarmModel.SnsProperty"]]:
            '''Information required to publish the Amazon SNS message.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-alarmaction.html#cfn-iotevents-alarmmodel-alarmaction-sns
            '''
            result = self._values.get("sns")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAlarmModel.SnsProperty"]], result)

        @builtins.property
        def sqs(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAlarmModel.SqsProperty"]]:
            '''Sends information about the detector model instance and the event that triggered the action to an Amazon SQS queue.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-alarmaction.html#cfn-iotevents-alarmmodel-alarmaction-sqs
            '''
            result = self._values.get("sqs")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAlarmModel.SqsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AlarmActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotevents.CfnAlarmModel.AlarmCapabilitiesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "acknowledge_flow": "acknowledgeFlow",
            "initialization_configuration": "initializationConfiguration",
        },
    )
    class AlarmCapabilitiesProperty:
        def __init__(
            self,
            *,
            acknowledge_flow: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAlarmModel.AcknowledgeFlowProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            initialization_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAlarmModel.InitializationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Contains the configuration information of alarm state changes.

            :param acknowledge_flow: Specifies whether to get notified for alarm state changes.
            :param initialization_configuration: Specifies the default alarm state. The configuration applies to all alarms that were created based on this alarm model.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-alarmcapabilities.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotevents as iotevents
                
                alarm_capabilities_property = iotevents.CfnAlarmModel.AlarmCapabilitiesProperty(
                    acknowledge_flow=iotevents.CfnAlarmModel.AcknowledgeFlowProperty(
                        enabled=False
                    ),
                    initialization_configuration=iotevents.CfnAlarmModel.InitializationConfigurationProperty(
                        disabled_on_initialization=False
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8cfea2cb5d08826e83e6dc83754015780aeb22a1b8774e0f8e35b1d0931455b0)
                check_type(argname="argument acknowledge_flow", value=acknowledge_flow, expected_type=type_hints["acknowledge_flow"])
                check_type(argname="argument initialization_configuration", value=initialization_configuration, expected_type=type_hints["initialization_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if acknowledge_flow is not None:
                self._values["acknowledge_flow"] = acknowledge_flow
            if initialization_configuration is not None:
                self._values["initialization_configuration"] = initialization_configuration

        @builtins.property
        def acknowledge_flow(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAlarmModel.AcknowledgeFlowProperty"]]:
            '''Specifies whether to get notified for alarm state changes.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-alarmcapabilities.html#cfn-iotevents-alarmmodel-alarmcapabilities-acknowledgeflow
            '''
            result = self._values.get("acknowledge_flow")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAlarmModel.AcknowledgeFlowProperty"]], result)

        @builtins.property
        def initialization_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAlarmModel.InitializationConfigurationProperty"]]:
            '''Specifies the default alarm state.

            The configuration applies to all alarms that were created based on this alarm model.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-alarmcapabilities.html#cfn-iotevents-alarmmodel-alarmcapabilities-initializationconfiguration
            '''
            result = self._values.get("initialization_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAlarmModel.InitializationConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AlarmCapabilitiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotevents.CfnAlarmModel.AlarmEventActionsProperty",
        jsii_struct_bases=[],
        name_mapping={"alarm_actions": "alarmActions"},
    )
    class AlarmEventActionsProperty:
        def __init__(
            self,
            *,
            alarm_actions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAlarmModel.AlarmActionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Contains information about one or more alarm actions.

            :param alarm_actions: Specifies one or more supported actions to receive notifications when the alarm state changes.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-alarmeventactions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotevents as iotevents
                
                alarm_event_actions_property = iotevents.CfnAlarmModel.AlarmEventActionsProperty(
                    alarm_actions=[iotevents.CfnAlarmModel.AlarmActionProperty(
                        dynamo_db=iotevents.CfnAlarmModel.DynamoDBProperty(
                            hash_key_field="hashKeyField",
                            hash_key_value="hashKeyValue",
                            table_name="tableName",
                
                            # the properties below are optional
                            hash_key_type="hashKeyType",
                            operation="operation",
                            payload=iotevents.CfnAlarmModel.PayloadProperty(
                                content_expression="contentExpression",
                                type="type"
                            ),
                            payload_field="payloadField",
                            range_key_field="rangeKeyField",
                            range_key_type="rangeKeyType",
                            range_key_value="rangeKeyValue"
                        ),
                        dynamo_dBv2=iotevents.CfnAlarmModel.DynamoDBv2Property(
                            table_name="tableName",
                
                            # the properties below are optional
                            payload=iotevents.CfnAlarmModel.PayloadProperty(
                                content_expression="contentExpression",
                                type="type"
                            )
                        ),
                        firehose=iotevents.CfnAlarmModel.FirehoseProperty(
                            delivery_stream_name="deliveryStreamName",
                
                            # the properties below are optional
                            payload=iotevents.CfnAlarmModel.PayloadProperty(
                                content_expression="contentExpression",
                                type="type"
                            ),
                            separator="separator"
                        ),
                        iot_events=iotevents.CfnAlarmModel.IotEventsProperty(
                            input_name="inputName",
                
                            # the properties below are optional
                            payload=iotevents.CfnAlarmModel.PayloadProperty(
                                content_expression="contentExpression",
                                type="type"
                            )
                        ),
                        iot_site_wise=iotevents.CfnAlarmModel.IotSiteWiseProperty(
                            asset_id="assetId",
                            entry_id="entryId",
                            property_alias="propertyAlias",
                            property_id="propertyId",
                            property_value=iotevents.CfnAlarmModel.AssetPropertyValueProperty(
                                value=iotevents.CfnAlarmModel.AssetPropertyVariantProperty(
                                    boolean_value="booleanValue",
                                    double_value="doubleValue",
                                    integer_value="integerValue",
                                    string_value="stringValue"
                                ),
                
                                # the properties below are optional
                                quality="quality",
                                timestamp=iotevents.CfnAlarmModel.AssetPropertyTimestampProperty(
                                    time_in_seconds="timeInSeconds",
                
                                    # the properties below are optional
                                    offset_in_nanos="offsetInNanos"
                                )
                            )
                        ),
                        iot_topic_publish=iotevents.CfnAlarmModel.IotTopicPublishProperty(
                            mqtt_topic="mqttTopic",
                
                            # the properties below are optional
                            payload=iotevents.CfnAlarmModel.PayloadProperty(
                                content_expression="contentExpression",
                                type="type"
                            )
                        ),
                        lambda_=iotevents.CfnAlarmModel.LambdaProperty(
                            function_arn="functionArn",
                
                            # the properties below are optional
                            payload=iotevents.CfnAlarmModel.PayloadProperty(
                                content_expression="contentExpression",
                                type="type"
                            )
                        ),
                        sns=iotevents.CfnAlarmModel.SnsProperty(
                            target_arn="targetArn",
                
                            # the properties below are optional
                            payload=iotevents.CfnAlarmModel.PayloadProperty(
                                content_expression="contentExpression",
                                type="type"
                            )
                        ),
                        sqs=iotevents.CfnAlarmModel.SqsProperty(
                            queue_url="queueUrl",
                
                            # the properties below are optional
                            payload=iotevents.CfnAlarmModel.PayloadProperty(
                                content_expression="contentExpression",
                                type="type"
                            ),
                            use_base64=False
                        )
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a6ca07dd10460007b069e0fb33a778c8623f821779a57a99e1b7583f9708fb0b)
                check_type(argname="argument alarm_actions", value=alarm_actions, expected_type=type_hints["alarm_actions"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if alarm_actions is not None:
                self._values["alarm_actions"] = alarm_actions

        @builtins.property
        def alarm_actions(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAlarmModel.AlarmActionProperty"]]]]:
            '''Specifies one or more supported actions to receive notifications when the alarm state changes.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-alarmeventactions.html#cfn-iotevents-alarmmodel-alarmeventactions-alarmactions
            '''
            result = self._values.get("alarm_actions")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAlarmModel.AlarmActionProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AlarmEventActionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotevents.CfnAlarmModel.AlarmRuleProperty",
        jsii_struct_bases=[],
        name_mapping={"simple_rule": "simpleRule"},
    )
    class AlarmRuleProperty:
        def __init__(
            self,
            *,
            simple_rule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAlarmModel.SimpleRuleProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Defines when your alarm is invoked.

            :param simple_rule: A rule that compares an input property value to a threshold value with a comparison operator.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-alarmrule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotevents as iotevents
                
                alarm_rule_property = iotevents.CfnAlarmModel.AlarmRuleProperty(
                    simple_rule=iotevents.CfnAlarmModel.SimpleRuleProperty(
                        comparison_operator="comparisonOperator",
                        input_property="inputProperty",
                        threshold="threshold"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ecdb897257f52e6f2dc0b5e8aa04adf9936f47ba53e3a04c2de77b97b3007a0e)
                check_type(argname="argument simple_rule", value=simple_rule, expected_type=type_hints["simple_rule"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if simple_rule is not None:
                self._values["simple_rule"] = simple_rule

        @builtins.property
        def simple_rule(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAlarmModel.SimpleRuleProperty"]]:
            '''A rule that compares an input property value to a threshold value with a comparison operator.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-alarmrule.html#cfn-iotevents-alarmmodel-alarmrule-simplerule
            '''
            result = self._values.get("simple_rule")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAlarmModel.SimpleRuleProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AlarmRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotevents.CfnAlarmModel.AssetPropertyTimestampProperty",
        jsii_struct_bases=[],
        name_mapping={
            "time_in_seconds": "timeInSeconds",
            "offset_in_nanos": "offsetInNanos",
        },
    )
    class AssetPropertyTimestampProperty:
        def __init__(
            self,
            *,
            time_in_seconds: builtins.str,
            offset_in_nanos: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A structure that contains timestamp information. For more information, see `TimeInNanos <https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_TimeInNanos.html>`_ in the *AWS IoT SiteWise API Reference* .

            You must use expressions for all parameters in ``AssetPropertyTimestamp`` . The expressions accept literals, operators, functions, references, and substitution templates.

            **Examples** - For literal values, the expressions must contain single quotes. For example, the value for the ``timeInSeconds`` parameter can be ``'1586400675'`` .

            - For references, you must specify either variables or input values. For example, the value for the ``offsetInNanos`` parameter can be ``$variable.time`` .
            - For a substitution template, you must use ``${}`` , and the template must be in single quotes. A substitution template can also contain a combination of literals, operators, functions, references, and substitution templates.

            In the following example, the value for the ``timeInSeconds`` parameter uses a substitution template.

            ``'${$input.TemperatureInput.sensorData.timestamp / 1000}'``

            For more information, see `Expressions <https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-expressions.html>`_ in the *AWS IoT Events Developer Guide* .

            :param time_in_seconds: The timestamp, in seconds, in the Unix epoch format. The valid range is between 1-31556889864403199.
            :param offset_in_nanos: The nanosecond offset converted from ``timeInSeconds`` . The valid range is between 0-999999999.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-assetpropertytimestamp.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotevents as iotevents
                
                asset_property_timestamp_property = iotevents.CfnAlarmModel.AssetPropertyTimestampProperty(
                    time_in_seconds="timeInSeconds",
                
                    # the properties below are optional
                    offset_in_nanos="offsetInNanos"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d0faa4e9328819a8804a815994faf7d70d0f09054014c6e47dd3b002c546003d)
                check_type(argname="argument time_in_seconds", value=time_in_seconds, expected_type=type_hints["time_in_seconds"])
                check_type(argname="argument offset_in_nanos", value=offset_in_nanos, expected_type=type_hints["offset_in_nanos"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "time_in_seconds": time_in_seconds,
            }
            if offset_in_nanos is not None:
                self._values["offset_in_nanos"] = offset_in_nanos

        @builtins.property
        def time_in_seconds(self) -> builtins.str:
            '''The timestamp, in seconds, in the Unix epoch format.

            The valid range is between 1-31556889864403199.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-assetpropertytimestamp.html#cfn-iotevents-alarmmodel-assetpropertytimestamp-timeinseconds
            '''
            result = self._values.get("time_in_seconds")
            assert result is not None, "Required property 'time_in_seconds' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def offset_in_nanos(self) -> typing.Optional[builtins.str]:
            '''The nanosecond offset converted from ``timeInSeconds`` .

            The valid range is between 0-999999999.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-assetpropertytimestamp.html#cfn-iotevents-alarmmodel-assetpropertytimestamp-offsetinnanos
            '''
            result = self._values.get("offset_in_nanos")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AssetPropertyTimestampProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotevents.CfnAlarmModel.AssetPropertyValueProperty",
        jsii_struct_bases=[],
        name_mapping={
            "value": "value",
            "quality": "quality",
            "timestamp": "timestamp",
        },
    )
    class AssetPropertyValueProperty:
        def __init__(
            self,
            *,
            value: typing.Union[_IResolvable_da3f097b, typing.Union["CfnAlarmModel.AssetPropertyVariantProperty", typing.Dict[builtins.str, typing.Any]]],
            quality: typing.Optional[builtins.str] = None,
            timestamp: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAlarmModel.AssetPropertyTimestampProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''A structure that contains value information. For more information, see `AssetPropertyValue <https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_AssetPropertyValue.html>`_ in the *AWS IoT SiteWise API Reference* .

            You must use expressions for all parameters in ``AssetPropertyValue`` . The expressions accept literals, operators, functions, references, and substitution templates.

            **Examples** - For literal values, the expressions must contain single quotes. For example, the value for the ``quality`` parameter can be ``'GOOD'`` .

            - For references, you must specify either variables or input values. For example, the value for the ``quality`` parameter can be ``$input.TemperatureInput.sensorData.quality`` .

            For more information, see `Expressions <https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-expressions.html>`_ in the *AWS IoT Events Developer Guide* .

            :param value: The value to send to an asset property.
            :param quality: The quality of the asset property value. The value must be ``'GOOD'`` , ``'BAD'`` , or ``'UNCERTAIN'`` .
            :param timestamp: The timestamp associated with the asset property value. The default is the current event time.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-assetpropertyvalue.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotevents as iotevents
                
                asset_property_value_property = iotevents.CfnAlarmModel.AssetPropertyValueProperty(
                    value=iotevents.CfnAlarmModel.AssetPropertyVariantProperty(
                        boolean_value="booleanValue",
                        double_value="doubleValue",
                        integer_value="integerValue",
                        string_value="stringValue"
                    ),
                
                    # the properties below are optional
                    quality="quality",
                    timestamp=iotevents.CfnAlarmModel.AssetPropertyTimestampProperty(
                        time_in_seconds="timeInSeconds",
                
                        # the properties below are optional
                        offset_in_nanos="offsetInNanos"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__708234624899e9edfd2c801c216045db009dc0332806973b92a2972970d186a8)
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
                check_type(argname="argument quality", value=quality, expected_type=type_hints["quality"])
                check_type(argname="argument timestamp", value=timestamp, expected_type=type_hints["timestamp"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "value": value,
            }
            if quality is not None:
                self._values["quality"] = quality
            if timestamp is not None:
                self._values["timestamp"] = timestamp

        @builtins.property
        def value(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnAlarmModel.AssetPropertyVariantProperty"]:
            '''The value to send to an asset property.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-assetpropertyvalue.html#cfn-iotevents-alarmmodel-assetpropertyvalue-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnAlarmModel.AssetPropertyVariantProperty"], result)

        @builtins.property
        def quality(self) -> typing.Optional[builtins.str]:
            '''The quality of the asset property value.

            The value must be ``'GOOD'`` , ``'BAD'`` , or ``'UNCERTAIN'`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-assetpropertyvalue.html#cfn-iotevents-alarmmodel-assetpropertyvalue-quality
            '''
            result = self._values.get("quality")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def timestamp(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAlarmModel.AssetPropertyTimestampProperty"]]:
            '''The timestamp associated with the asset property value.

            The default is the current event time.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-assetpropertyvalue.html#cfn-iotevents-alarmmodel-assetpropertyvalue-timestamp
            '''
            result = self._values.get("timestamp")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAlarmModel.AssetPropertyTimestampProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AssetPropertyValueProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotevents.CfnAlarmModel.AssetPropertyVariantProperty",
        jsii_struct_bases=[],
        name_mapping={
            "boolean_value": "booleanValue",
            "double_value": "doubleValue",
            "integer_value": "integerValue",
            "string_value": "stringValue",
        },
    )
    class AssetPropertyVariantProperty:
        def __init__(
            self,
            *,
            boolean_value: typing.Optional[builtins.str] = None,
            double_value: typing.Optional[builtins.str] = None,
            integer_value: typing.Optional[builtins.str] = None,
            string_value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A structure that contains an asset property value.

            For more information, see `Variant <https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_Variant.html>`_ in the *AWS IoT SiteWise API Reference* .

            You must use expressions for all parameters in ``AssetPropertyVariant`` . The expressions accept literals, operators, functions, references, and substitution templates.

            **Examples** - For literal values, the expressions must contain single quotes. For example, the value for the ``integerValue`` parameter can be ``'100'`` .

            - For references, you must specify either variables or parameters. For example, the value for the ``booleanValue`` parameter can be ``$variable.offline`` .
            - For a substitution template, you must use ``${}`` , and the template must be in single quotes. A substitution template can also contain a combination of literals, operators, functions, references, and substitution templates.

            In the following example, the value for the ``doubleValue`` parameter uses a substitution template.

            ``'${$input.TemperatureInput.sensorData.temperature * 6 / 5 + 32}'``

            For more information, see `Expressions <https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-expressions.html>`_ in the *AWS IoT Events Developer Guide* .

            You must specify one of the following value types, depending on the ``dataType`` of the specified asset property. For more information, see `AssetProperty <https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_AssetProperty.html>`_ in the *AWS IoT SiteWise API Reference* .

            :param boolean_value: The asset property value is a Boolean value that must be ``'TRUE'`` or ``'FALSE'`` . You must use an expression, and the evaluated result should be a Boolean value.
            :param double_value: The asset property value is a double. You must use an expression, and the evaluated result should be a double.
            :param integer_value: The asset property value is an integer. You must use an expression, and the evaluated result should be an integer.
            :param string_value: The asset property value is a string. You must use an expression, and the evaluated result should be a string.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-assetpropertyvariant.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotevents as iotevents
                
                asset_property_variant_property = iotevents.CfnAlarmModel.AssetPropertyVariantProperty(
                    boolean_value="booleanValue",
                    double_value="doubleValue",
                    integer_value="integerValue",
                    string_value="stringValue"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4caad62d2d9efb76f9ed85eeb63e97b3d0a85ede80a6e1541ef55198968a2ed3)
                check_type(argname="argument boolean_value", value=boolean_value, expected_type=type_hints["boolean_value"])
                check_type(argname="argument double_value", value=double_value, expected_type=type_hints["double_value"])
                check_type(argname="argument integer_value", value=integer_value, expected_type=type_hints["integer_value"])
                check_type(argname="argument string_value", value=string_value, expected_type=type_hints["string_value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if boolean_value is not None:
                self._values["boolean_value"] = boolean_value
            if double_value is not None:
                self._values["double_value"] = double_value
            if integer_value is not None:
                self._values["integer_value"] = integer_value
            if string_value is not None:
                self._values["string_value"] = string_value

        @builtins.property
        def boolean_value(self) -> typing.Optional[builtins.str]:
            '''The asset property value is a Boolean value that must be ``'TRUE'`` or ``'FALSE'`` .

            You must use an expression, and the evaluated result should be a Boolean value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-assetpropertyvariant.html#cfn-iotevents-alarmmodel-assetpropertyvariant-booleanvalue
            '''
            result = self._values.get("boolean_value")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def double_value(self) -> typing.Optional[builtins.str]:
            '''The asset property value is a double.

            You must use an expression, and the evaluated result should be a double.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-assetpropertyvariant.html#cfn-iotevents-alarmmodel-assetpropertyvariant-doublevalue
            '''
            result = self._values.get("double_value")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def integer_value(self) -> typing.Optional[builtins.str]:
            '''The asset property value is an integer.

            You must use an expression, and the evaluated result should be an integer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-assetpropertyvariant.html#cfn-iotevents-alarmmodel-assetpropertyvariant-integervalue
            '''
            result = self._values.get("integer_value")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def string_value(self) -> typing.Optional[builtins.str]:
            '''The asset property value is a string.

            You must use an expression, and the evaluated result should be a string.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-assetpropertyvariant.html#cfn-iotevents-alarmmodel-assetpropertyvariant-stringvalue
            '''
            result = self._values.get("string_value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AssetPropertyVariantProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotevents.CfnAlarmModel.DynamoDBProperty",
        jsii_struct_bases=[],
        name_mapping={
            "hash_key_field": "hashKeyField",
            "hash_key_value": "hashKeyValue",
            "table_name": "tableName",
            "hash_key_type": "hashKeyType",
            "operation": "operation",
            "payload": "payload",
            "payload_field": "payloadField",
            "range_key_field": "rangeKeyField",
            "range_key_type": "rangeKeyType",
            "range_key_value": "rangeKeyValue",
        },
    )
    class DynamoDBProperty:
        def __init__(
            self,
            *,
            hash_key_field: builtins.str,
            hash_key_value: builtins.str,
            table_name: builtins.str,
            hash_key_type: typing.Optional[builtins.str] = None,
            operation: typing.Optional[builtins.str] = None,
            payload: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAlarmModel.PayloadProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            payload_field: typing.Optional[builtins.str] = None,
            range_key_field: typing.Optional[builtins.str] = None,
            range_key_type: typing.Optional[builtins.str] = None,
            range_key_value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Defines an action to write to the Amazon DynamoDB table that you created.

            The standard action payload contains all the information about the detector model instance and the event that triggered the action. You can customize the `payload <https://docs.aws.amazon.com/iotevents/latest/apireference/API_Payload.html>`_ . One column of the DynamoDB table receives all attribute-value pairs in the payload that you specify.

            You must use expressions for all parameters in ``DynamoDBAction`` . The expressions accept literals, operators, functions, references, and substitution templates.

            **Examples** - For literal values, the expressions must contain single quotes. For example, the value for the ``hashKeyType`` parameter can be ``'STRING'`` .

            - For references, you must specify either variables or input values. For example, the value for the ``hashKeyField`` parameter can be ``$input.GreenhouseInput.name`` .
            - For a substitution template, you must use ``${}`` , and the template must be in single quotes. A substitution template can also contain a combination of literals, operators, functions, references, and substitution templates.

            In the following example, the value for the ``hashKeyValue`` parameter uses a substitution template.

            ``'${$input.GreenhouseInput.temperature * 6 / 5 + 32} in Fahrenheit'``

            - For a string concatenation, you must use ``+`` . A string concatenation can also contain a combination of literals, operators, functions, references, and substitution templates.

            In the following example, the value for the ``tableName`` parameter uses a string concatenation.

            ``'GreenhouseTemperatureTable ' + $input.GreenhouseInput.date``

            For more information, see `Expressions <https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-expressions.html>`_ in the *AWS IoT Events Developer Guide* .

            If the defined payload type is a string, ``DynamoDBAction`` writes non-JSON data to the DynamoDB table as binary data. The DynamoDB console displays the data as Base64-encoded text. The value for the ``payloadField`` parameter is ``<payload-field>_raw`` .

            :param hash_key_field: The name of the hash key (also called the partition key). The ``hashKeyField`` value must match the partition key of the target DynamoDB table.
            :param hash_key_value: The value of the hash key (also called the partition key).
            :param table_name: The name of the DynamoDB table. The ``tableName`` value must match the table name of the target DynamoDB table.
            :param hash_key_type: The data type for the hash key (also called the partition key). You can specify the following values:. - ``'STRING'`` - The hash key is a string. - ``'NUMBER'`` - The hash key is a number. If you don't specify ``hashKeyType`` , the default value is ``'STRING'`` .
            :param operation: The type of operation to perform. You can specify the following values:. - ``'INSERT'`` - Insert data as a new item into the DynamoDB table. This item uses the specified hash key as a partition key. If you specified a range key, the item uses the range key as a sort key. - ``'UPDATE'`` - Update an existing item of the DynamoDB table with new data. This item's partition key must match the specified hash key. If you specified a range key, the range key must match the item's sort key. - ``'DELETE'`` - Delete an existing item of the DynamoDB table. This item's partition key must match the specified hash key. If you specified a range key, the range key must match the item's sort key. If you don't specify this parameter, AWS IoT Events triggers the ``'INSERT'`` operation.
            :param payload: Information needed to configure the payload. By default, AWS IoT Events generates a standard payload in JSON for any action. This action payload contains all attribute-value pairs that have the information about the detector model instance and the event triggered the action. To configure the action payload, you can use ``contentExpression`` .
            :param payload_field: The name of the DynamoDB column that receives the action payload. If you don't specify this parameter, the name of the DynamoDB column is ``payload`` .
            :param range_key_field: The name of the range key (also called the sort key). The ``rangeKeyField`` value must match the sort key of the target DynamoDB table.
            :param range_key_type: The data type for the range key (also called the sort key), You can specify the following values:. - ``'STRING'`` - The range key is a string. - ``'NUMBER'`` - The range key is number. If you don't specify ``rangeKeyField`` , the default value is ``'STRING'`` .
            :param range_key_value: The value of the range key (also called the sort key).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-dynamodb.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotevents as iotevents
                
                dynamo_dBProperty = iotevents.CfnAlarmModel.DynamoDBProperty(
                    hash_key_field="hashKeyField",
                    hash_key_value="hashKeyValue",
                    table_name="tableName",
                
                    # the properties below are optional
                    hash_key_type="hashKeyType",
                    operation="operation",
                    payload=iotevents.CfnAlarmModel.PayloadProperty(
                        content_expression="contentExpression",
                        type="type"
                    ),
                    payload_field="payloadField",
                    range_key_field="rangeKeyField",
                    range_key_type="rangeKeyType",
                    range_key_value="rangeKeyValue"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5817f24cc0ee11012a378de58760f08626fd63cf7b576191502d7ed8d10b2ddf)
                check_type(argname="argument hash_key_field", value=hash_key_field, expected_type=type_hints["hash_key_field"])
                check_type(argname="argument hash_key_value", value=hash_key_value, expected_type=type_hints["hash_key_value"])
                check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
                check_type(argname="argument hash_key_type", value=hash_key_type, expected_type=type_hints["hash_key_type"])
                check_type(argname="argument operation", value=operation, expected_type=type_hints["operation"])
                check_type(argname="argument payload", value=payload, expected_type=type_hints["payload"])
                check_type(argname="argument payload_field", value=payload_field, expected_type=type_hints["payload_field"])
                check_type(argname="argument range_key_field", value=range_key_field, expected_type=type_hints["range_key_field"])
                check_type(argname="argument range_key_type", value=range_key_type, expected_type=type_hints["range_key_type"])
                check_type(argname="argument range_key_value", value=range_key_value, expected_type=type_hints["range_key_value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "hash_key_field": hash_key_field,
                "hash_key_value": hash_key_value,
                "table_name": table_name,
            }
            if hash_key_type is not None:
                self._values["hash_key_type"] = hash_key_type
            if operation is not None:
                self._values["operation"] = operation
            if payload is not None:
                self._values["payload"] = payload
            if payload_field is not None:
                self._values["payload_field"] = payload_field
            if range_key_field is not None:
                self._values["range_key_field"] = range_key_field
            if range_key_type is not None:
                self._values["range_key_type"] = range_key_type
            if range_key_value is not None:
                self._values["range_key_value"] = range_key_value

        @builtins.property
        def hash_key_field(self) -> builtins.str:
            '''The name of the hash key (also called the partition key).

            The ``hashKeyField`` value must match the partition key of the target DynamoDB table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-dynamodb.html#cfn-iotevents-alarmmodel-dynamodb-hashkeyfield
            '''
            result = self._values.get("hash_key_field")
            assert result is not None, "Required property 'hash_key_field' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def hash_key_value(self) -> builtins.str:
            '''The value of the hash key (also called the partition key).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-dynamodb.html#cfn-iotevents-alarmmodel-dynamodb-hashkeyvalue
            '''
            result = self._values.get("hash_key_value")
            assert result is not None, "Required property 'hash_key_value' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def table_name(self) -> builtins.str:
            '''The name of the DynamoDB table.

            The ``tableName`` value must match the table name of the target DynamoDB table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-dynamodb.html#cfn-iotevents-alarmmodel-dynamodb-tablename
            '''
            result = self._values.get("table_name")
            assert result is not None, "Required property 'table_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def hash_key_type(self) -> typing.Optional[builtins.str]:
            '''The data type for the hash key (also called the partition key). You can specify the following values:.

            - ``'STRING'`` - The hash key is a string.
            - ``'NUMBER'`` - The hash key is a number.

            If you don't specify ``hashKeyType`` , the default value is ``'STRING'`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-dynamodb.html#cfn-iotevents-alarmmodel-dynamodb-hashkeytype
            '''
            result = self._values.get("hash_key_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def operation(self) -> typing.Optional[builtins.str]:
            '''The type of operation to perform. You can specify the following values:.

            - ``'INSERT'`` - Insert data as a new item into the DynamoDB table. This item uses the specified hash key as a partition key. If you specified a range key, the item uses the range key as a sort key.
            - ``'UPDATE'`` - Update an existing item of the DynamoDB table with new data. This item's partition key must match the specified hash key. If you specified a range key, the range key must match the item's sort key.
            - ``'DELETE'`` - Delete an existing item of the DynamoDB table. This item's partition key must match the specified hash key. If you specified a range key, the range key must match the item's sort key.

            If you don't specify this parameter, AWS IoT Events triggers the ``'INSERT'`` operation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-dynamodb.html#cfn-iotevents-alarmmodel-dynamodb-operation
            '''
            result = self._values.get("operation")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def payload(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAlarmModel.PayloadProperty"]]:
            '''Information needed to configure the payload.

            By default, AWS IoT Events generates a standard payload in JSON for any action. This action payload contains all attribute-value pairs that have the information about the detector model instance and the event triggered the action. To configure the action payload, you can use ``contentExpression`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-dynamodb.html#cfn-iotevents-alarmmodel-dynamodb-payload
            '''
            result = self._values.get("payload")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAlarmModel.PayloadProperty"]], result)

        @builtins.property
        def payload_field(self) -> typing.Optional[builtins.str]:
            '''The name of the DynamoDB column that receives the action payload.

            If you don't specify this parameter, the name of the DynamoDB column is ``payload`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-dynamodb.html#cfn-iotevents-alarmmodel-dynamodb-payloadfield
            '''
            result = self._values.get("payload_field")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def range_key_field(self) -> typing.Optional[builtins.str]:
            '''The name of the range key (also called the sort key).

            The ``rangeKeyField`` value must match the sort key of the target DynamoDB table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-dynamodb.html#cfn-iotevents-alarmmodel-dynamodb-rangekeyfield
            '''
            result = self._values.get("range_key_field")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def range_key_type(self) -> typing.Optional[builtins.str]:
            '''The data type for the range key (also called the sort key), You can specify the following values:.

            - ``'STRING'`` - The range key is a string.
            - ``'NUMBER'`` - The range key is number.

            If you don't specify ``rangeKeyField`` , the default value is ``'STRING'`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-dynamodb.html#cfn-iotevents-alarmmodel-dynamodb-rangekeytype
            '''
            result = self._values.get("range_key_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def range_key_value(self) -> typing.Optional[builtins.str]:
            '''The value of the range key (also called the sort key).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-dynamodb.html#cfn-iotevents-alarmmodel-dynamodb-rangekeyvalue
            '''
            result = self._values.get("range_key_value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DynamoDBProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotevents.CfnAlarmModel.DynamoDBv2Property",
        jsii_struct_bases=[],
        name_mapping={"table_name": "tableName", "payload": "payload"},
    )
    class DynamoDBv2Property:
        def __init__(
            self,
            *,
            table_name: builtins.str,
            payload: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAlarmModel.PayloadProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Defines an action to write to the Amazon DynamoDB table that you created.

            The default action payload contains all the information about the detector model instance and the event that triggered the action. You can customize the `payload <https://docs.aws.amazon.com/iotevents/latest/apireference/API_Payload.html>`_ . A separate column of the DynamoDB table receives one attribute-value pair in the payload that you specify.

            You must use expressions for all parameters in ``DynamoDBv2Action`` . The expressions accept literals, operators, functions, references, and substitution templates.

            **Examples** - For literal values, the expressions must contain single quotes. For example, the value for the ``tableName`` parameter can be ``'GreenhouseTemperatureTable'`` .

            - For references, you must specify either variables or input values. For example, the value for the ``tableName`` parameter can be ``$variable.ddbtableName`` .
            - For a substitution template, you must use ``${}`` , and the template must be in single quotes. A substitution template can also contain a combination of literals, operators, functions, references, and substitution templates.

            In the following example, the value for the ``contentExpression`` parameter in ``Payload`` uses a substitution template.

            ``'{\\"sensorID\\": \\"${$input.GreenhouseInput.sensor_id}\\", \\"temperature\\": \\"${$input.GreenhouseInput.temperature * 9 / 5 + 32}\\"}'``

            - For a string concatenation, you must use ``+`` . A string concatenation can also contain a combination of literals, operators, functions, references, and substitution templates.

            In the following example, the value for the ``tableName`` parameter uses a string concatenation.

            ``'GreenhouseTemperatureTable ' + $input.GreenhouseInput.date``

            For more information, see `Expressions <https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-expressions.html>`_ in the *AWS IoT Events Developer Guide* .

            The value for the ``type`` parameter in ``Payload`` must be ``JSON`` .

            :param table_name: The name of the DynamoDB table.
            :param payload: Information needed to configure the payload. By default, AWS IoT Events generates a standard payload in JSON for any action. This action payload contains all attribute-value pairs that have the information about the detector model instance and the event triggered the action. To configure the action payload, you can use ``contentExpression`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-dynamodbv2.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotevents as iotevents
                
                dynamo_dBv2_property = iotevents.CfnAlarmModel.DynamoDBv2Property(
                    table_name="tableName",
                
                    # the properties below are optional
                    payload=iotevents.CfnAlarmModel.PayloadProperty(
                        content_expression="contentExpression",
                        type="type"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__991f55661aeeabe2f112b3b55306f540afbaca55eac19af02f6046a1039bf0a0)
                check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
                check_type(argname="argument payload", value=payload, expected_type=type_hints["payload"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "table_name": table_name,
            }
            if payload is not None:
                self._values["payload"] = payload

        @builtins.property
        def table_name(self) -> builtins.str:
            '''The name of the DynamoDB table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-dynamodbv2.html#cfn-iotevents-alarmmodel-dynamodbv2-tablename
            '''
            result = self._values.get("table_name")
            assert result is not None, "Required property 'table_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def payload(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAlarmModel.PayloadProperty"]]:
            '''Information needed to configure the payload.

            By default, AWS IoT Events generates a standard payload in JSON for any action. This action payload contains all attribute-value pairs that have the information about the detector model instance and the event triggered the action. To configure the action payload, you can use ``contentExpression`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-dynamodbv2.html#cfn-iotevents-alarmmodel-dynamodbv2-payload
            '''
            result = self._values.get("payload")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAlarmModel.PayloadProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DynamoDBv2Property(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotevents.CfnAlarmModel.FirehoseProperty",
        jsii_struct_bases=[],
        name_mapping={
            "delivery_stream_name": "deliveryStreamName",
            "payload": "payload",
            "separator": "separator",
        },
    )
    class FirehoseProperty:
        def __init__(
            self,
            *,
            delivery_stream_name: builtins.str,
            payload: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAlarmModel.PayloadProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            separator: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Sends information about the detector model instance and the event that triggered the action to an Amazon Kinesis Data Firehose delivery stream.

            :param delivery_stream_name: The name of the Kinesis Data Firehose delivery stream where the data is written.
            :param payload: You can configure the action payload when you send a message to an Amazon Kinesis Data Firehose delivery stream.
            :param separator: A character separator that is used to separate records written to the Kinesis Data Firehose delivery stream. Valid values are: '\\n' (newline), '\\t' (tab), '\\r\\n' (Windows newline), ',' (comma).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-firehose.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotevents as iotevents
                
                firehose_property = iotevents.CfnAlarmModel.FirehoseProperty(
                    delivery_stream_name="deliveryStreamName",
                
                    # the properties below are optional
                    payload=iotevents.CfnAlarmModel.PayloadProperty(
                        content_expression="contentExpression",
                        type="type"
                    ),
                    separator="separator"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6aaead57fb4199647f0274fe275fcc660e36d121f8abbc3801a7154bd92c0923)
                check_type(argname="argument delivery_stream_name", value=delivery_stream_name, expected_type=type_hints["delivery_stream_name"])
                check_type(argname="argument payload", value=payload, expected_type=type_hints["payload"])
                check_type(argname="argument separator", value=separator, expected_type=type_hints["separator"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "delivery_stream_name": delivery_stream_name,
            }
            if payload is not None:
                self._values["payload"] = payload
            if separator is not None:
                self._values["separator"] = separator

        @builtins.property
        def delivery_stream_name(self) -> builtins.str:
            '''The name of the Kinesis Data Firehose delivery stream where the data is written.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-firehose.html#cfn-iotevents-alarmmodel-firehose-deliverystreamname
            '''
            result = self._values.get("delivery_stream_name")
            assert result is not None, "Required property 'delivery_stream_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def payload(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAlarmModel.PayloadProperty"]]:
            '''You can configure the action payload when you send a message to an Amazon Kinesis Data Firehose delivery stream.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-firehose.html#cfn-iotevents-alarmmodel-firehose-payload
            '''
            result = self._values.get("payload")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAlarmModel.PayloadProperty"]], result)

        @builtins.property
        def separator(self) -> typing.Optional[builtins.str]:
            '''A character separator that is used to separate records written to the Kinesis Data Firehose delivery stream.

            Valid values are: '\\n' (newline), '\\t' (tab), '\\r\\n' (Windows newline), ',' (comma).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-firehose.html#cfn-iotevents-alarmmodel-firehose-separator
            '''
            result = self._values.get("separator")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FirehoseProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotevents.CfnAlarmModel.InitializationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"disabled_on_initialization": "disabledOnInitialization"},
    )
    class InitializationConfigurationProperty:
        def __init__(
            self,
            *,
            disabled_on_initialization: typing.Union[builtins.bool, _IResolvable_da3f097b],
        ) -> None:
            '''Specifies the default alarm state.

            The configuration applies to all alarms that were created based on this alarm model.

            :param disabled_on_initialization: The value must be ``TRUE`` or ``FALSE`` . If ``FALSE`` , all alarm instances created based on the alarm model are activated. The default value is ``TRUE`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-initializationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotevents as iotevents
                
                initialization_configuration_property = iotevents.CfnAlarmModel.InitializationConfigurationProperty(
                    disabled_on_initialization=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f006a26469daccaeec8fbdc6b6b96590027aa831f6565f8f5bf0f295a81a2c95)
                check_type(argname="argument disabled_on_initialization", value=disabled_on_initialization, expected_type=type_hints["disabled_on_initialization"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "disabled_on_initialization": disabled_on_initialization,
            }

        @builtins.property
        def disabled_on_initialization(
            self,
        ) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''The value must be ``TRUE`` or ``FALSE`` .

            If ``FALSE`` , all alarm instances created based on the alarm model are activated. The default value is ``TRUE`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-initializationconfiguration.html#cfn-iotevents-alarmmodel-initializationconfiguration-disabledoninitialization
            '''
            result = self._values.get("disabled_on_initialization")
            assert result is not None, "Required property 'disabled_on_initialization' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InitializationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotevents.CfnAlarmModel.IotEventsProperty",
        jsii_struct_bases=[],
        name_mapping={"input_name": "inputName", "payload": "payload"},
    )
    class IotEventsProperty:
        def __init__(
            self,
            *,
            input_name: builtins.str,
            payload: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAlarmModel.PayloadProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Sends an AWS IoT Events input, passing in information about the detector model instance and the event that triggered the action.

            :param input_name: The name of the AWS IoT Events input where the data is sent.
            :param payload: You can configure the action payload when you send a message to an AWS IoT Events input.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-iotevents.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotevents as iotevents
                
                iot_events_property = iotevents.CfnAlarmModel.IotEventsProperty(
                    input_name="inputName",
                
                    # the properties below are optional
                    payload=iotevents.CfnAlarmModel.PayloadProperty(
                        content_expression="contentExpression",
                        type="type"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1159713658f7035984daf8d6dbfaf0175f9cab27b66825c395143c8befb7e719)
                check_type(argname="argument input_name", value=input_name, expected_type=type_hints["input_name"])
                check_type(argname="argument payload", value=payload, expected_type=type_hints["payload"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "input_name": input_name,
            }
            if payload is not None:
                self._values["payload"] = payload

        @builtins.property
        def input_name(self) -> builtins.str:
            '''The name of the AWS IoT Events input where the data is sent.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-iotevents.html#cfn-iotevents-alarmmodel-iotevents-inputname
            '''
            result = self._values.get("input_name")
            assert result is not None, "Required property 'input_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def payload(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAlarmModel.PayloadProperty"]]:
            '''You can configure the action payload when you send a message to an AWS IoT Events input.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-iotevents.html#cfn-iotevents-alarmmodel-iotevents-payload
            '''
            result = self._values.get("payload")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAlarmModel.PayloadProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IotEventsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotevents.CfnAlarmModel.IotSiteWiseProperty",
        jsii_struct_bases=[],
        name_mapping={
            "asset_id": "assetId",
            "entry_id": "entryId",
            "property_alias": "propertyAlias",
            "property_id": "propertyId",
            "property_value": "propertyValue",
        },
    )
    class IotSiteWiseProperty:
        def __init__(
            self,
            *,
            asset_id: typing.Optional[builtins.str] = None,
            entry_id: typing.Optional[builtins.str] = None,
            property_alias: typing.Optional[builtins.str] = None,
            property_id: typing.Optional[builtins.str] = None,
            property_value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAlarmModel.AssetPropertyValueProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Sends information about the detector model instance and the event that triggered the action to a specified asset property in AWS IoT SiteWise .

            You must use expressions for all parameters in ``IotSiteWiseAction`` . The expressions accept literals, operators, functions, references, and substitutions templates.

            **Examples** - For literal values, the expressions must contain single quotes. For example, the value for the ``propertyAlias`` parameter can be ``'/company/windfarm/3/turbine/7/temperature'`` .

            - For references, you must specify either variables or input values. For example, the value for the ``assetId`` parameter can be ``$input.TurbineInput.assetId1`` .
            - For a substitution template, you must use ``${}`` , and the template must be in single quotes. A substitution template can also contain a combination of literals, operators, functions, references, and substitution templates.

            In the following example, the value for the ``propertyAlias`` parameter uses a substitution template.

            ``'company/windfarm/${$input.TemperatureInput.sensorData.windfarmID}/turbine/ ${$input.TemperatureInput.sensorData.turbineID}/temperature'``

            You must specify either ``propertyAlias`` or both ``assetId`` and ``propertyId`` to identify the target asset property in AWS IoT SiteWise .

            For more information, see `Expressions <https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-expressions.html>`_ in the *AWS IoT Events Developer Guide* .

            :param asset_id: The ID of the asset that has the specified property.
            :param entry_id: A unique identifier for this entry. You can use the entry ID to track which data entry causes an error in case of failure. The default is a new unique identifier.
            :param property_alias: The alias of the asset property.
            :param property_id: The ID of the asset property.
            :param property_value: The value to send to the asset property. This value contains timestamp, quality, and value (TQV) information.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-iotsitewise.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotevents as iotevents
                
                iot_site_wise_property = iotevents.CfnAlarmModel.IotSiteWiseProperty(
                    asset_id="assetId",
                    entry_id="entryId",
                    property_alias="propertyAlias",
                    property_id="propertyId",
                    property_value=iotevents.CfnAlarmModel.AssetPropertyValueProperty(
                        value=iotevents.CfnAlarmModel.AssetPropertyVariantProperty(
                            boolean_value="booleanValue",
                            double_value="doubleValue",
                            integer_value="integerValue",
                            string_value="stringValue"
                        ),
                
                        # the properties below are optional
                        quality="quality",
                        timestamp=iotevents.CfnAlarmModel.AssetPropertyTimestampProperty(
                            time_in_seconds="timeInSeconds",
                
                            # the properties below are optional
                            offset_in_nanos="offsetInNanos"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__11694da853291108b198c9c98d58e346ab22cadc06b186dc6b980bb04d7751df)
                check_type(argname="argument asset_id", value=asset_id, expected_type=type_hints["asset_id"])
                check_type(argname="argument entry_id", value=entry_id, expected_type=type_hints["entry_id"])
                check_type(argname="argument property_alias", value=property_alias, expected_type=type_hints["property_alias"])
                check_type(argname="argument property_id", value=property_id, expected_type=type_hints["property_id"])
                check_type(argname="argument property_value", value=property_value, expected_type=type_hints["property_value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if asset_id is not None:
                self._values["asset_id"] = asset_id
            if entry_id is not None:
                self._values["entry_id"] = entry_id
            if property_alias is not None:
                self._values["property_alias"] = property_alias
            if property_id is not None:
                self._values["property_id"] = property_id
            if property_value is not None:
                self._values["property_value"] = property_value

        @builtins.property
        def asset_id(self) -> typing.Optional[builtins.str]:
            '''The ID of the asset that has the specified property.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-iotsitewise.html#cfn-iotevents-alarmmodel-iotsitewise-assetid
            '''
            result = self._values.get("asset_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def entry_id(self) -> typing.Optional[builtins.str]:
            '''A unique identifier for this entry.

            You can use the entry ID to track which data entry causes an error in case of failure. The default is a new unique identifier.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-iotsitewise.html#cfn-iotevents-alarmmodel-iotsitewise-entryid
            '''
            result = self._values.get("entry_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def property_alias(self) -> typing.Optional[builtins.str]:
            '''The alias of the asset property.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-iotsitewise.html#cfn-iotevents-alarmmodel-iotsitewise-propertyalias
            '''
            result = self._values.get("property_alias")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def property_id(self) -> typing.Optional[builtins.str]:
            '''The ID of the asset property.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-iotsitewise.html#cfn-iotevents-alarmmodel-iotsitewise-propertyid
            '''
            result = self._values.get("property_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def property_value(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAlarmModel.AssetPropertyValueProperty"]]:
            '''The value to send to the asset property.

            This value contains timestamp, quality, and value (TQV) information.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-iotsitewise.html#cfn-iotevents-alarmmodel-iotsitewise-propertyvalue
            '''
            result = self._values.get("property_value")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAlarmModel.AssetPropertyValueProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IotSiteWiseProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotevents.CfnAlarmModel.IotTopicPublishProperty",
        jsii_struct_bases=[],
        name_mapping={"mqtt_topic": "mqttTopic", "payload": "payload"},
    )
    class IotTopicPublishProperty:
        def __init__(
            self,
            *,
            mqtt_topic: builtins.str,
            payload: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAlarmModel.PayloadProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Information required to publish the MQTT message through the AWS IoT message broker.

            :param mqtt_topic: The MQTT topic of the message. You can use a string expression that includes variables ( ``$variable.<variable-name>`` ) and input values ( ``$input.<input-name>.<path-to-datum>`` ) as the topic string.
            :param payload: You can configure the action payload when you publish a message to an AWS IoT Core topic.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-iottopicpublish.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotevents as iotevents
                
                iot_topic_publish_property = iotevents.CfnAlarmModel.IotTopicPublishProperty(
                    mqtt_topic="mqttTopic",
                
                    # the properties below are optional
                    payload=iotevents.CfnAlarmModel.PayloadProperty(
                        content_expression="contentExpression",
                        type="type"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fd8797ce19f302d10090f97f9aa3b5045c89cb01d164ff9de6b87da2d7a6e25f)
                check_type(argname="argument mqtt_topic", value=mqtt_topic, expected_type=type_hints["mqtt_topic"])
                check_type(argname="argument payload", value=payload, expected_type=type_hints["payload"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "mqtt_topic": mqtt_topic,
            }
            if payload is not None:
                self._values["payload"] = payload

        @builtins.property
        def mqtt_topic(self) -> builtins.str:
            '''The MQTT topic of the message.

            You can use a string expression that includes variables ( ``$variable.<variable-name>`` ) and input values ( ``$input.<input-name>.<path-to-datum>`` ) as the topic string.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-iottopicpublish.html#cfn-iotevents-alarmmodel-iottopicpublish-mqtttopic
            '''
            result = self._values.get("mqtt_topic")
            assert result is not None, "Required property 'mqtt_topic' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def payload(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAlarmModel.PayloadProperty"]]:
            '''You can configure the action payload when you publish a message to an AWS IoT Core topic.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-iottopicpublish.html#cfn-iotevents-alarmmodel-iottopicpublish-payload
            '''
            result = self._values.get("payload")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAlarmModel.PayloadProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IotTopicPublishProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotevents.CfnAlarmModel.LambdaProperty",
        jsii_struct_bases=[],
        name_mapping={"function_arn": "functionArn", "payload": "payload"},
    )
    class LambdaProperty:
        def __init__(
            self,
            *,
            function_arn: builtins.str,
            payload: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAlarmModel.PayloadProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Calls a Lambda function, passing in information about the detector model instance and the event that triggered the action.

            :param function_arn: The ARN of the Lambda function that is executed.
            :param payload: You can configure the action payload when you send a message to a Lambda function.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-lambda.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotevents as iotevents
                
                lambda_property = iotevents.CfnAlarmModel.LambdaProperty(
                    function_arn="functionArn",
                
                    # the properties below are optional
                    payload=iotevents.CfnAlarmModel.PayloadProperty(
                        content_expression="contentExpression",
                        type="type"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a975c271127a1fe7c32f180fab5bb983fa81f890ee87d4cdd1dad0c6d4e60469)
                check_type(argname="argument function_arn", value=function_arn, expected_type=type_hints["function_arn"])
                check_type(argname="argument payload", value=payload, expected_type=type_hints["payload"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "function_arn": function_arn,
            }
            if payload is not None:
                self._values["payload"] = payload

        @builtins.property
        def function_arn(self) -> builtins.str:
            '''The ARN of the Lambda function that is executed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-lambda.html#cfn-iotevents-alarmmodel-lambda-functionarn
            '''
            result = self._values.get("function_arn")
            assert result is not None, "Required property 'function_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def payload(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAlarmModel.PayloadProperty"]]:
            '''You can configure the action payload when you send a message to a Lambda function.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-lambda.html#cfn-iotevents-alarmmodel-lambda-payload
            '''
            result = self._values.get("payload")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAlarmModel.PayloadProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LambdaProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotevents.CfnAlarmModel.PayloadProperty",
        jsii_struct_bases=[],
        name_mapping={"content_expression": "contentExpression", "type": "type"},
    )
    class PayloadProperty:
        def __init__(
            self,
            *,
            content_expression: builtins.str,
            type: builtins.str,
        ) -> None:
            '''Information needed to configure the payload.

            By default, AWS IoT Events generates a standard payload in JSON for any action. This action payload contains all attribute-value pairs that have the information about the detector model instance and the event triggered the action. To configure the action payload, you can use ``contentExpression`` .

            :param content_expression: The content of the payload. You can use a string expression that includes quoted strings ( ``'<string>'`` ), variables ( ``$variable.<variable-name>`` ), input values ( ``$input.<input-name>.<path-to-datum>`` ), string concatenations, and quoted strings that contain ``${}`` as the content. The recommended maximum size of a content expression is 1 KB.
            :param type: The value of the payload type can be either ``STRING`` or ``JSON`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-payload.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotevents as iotevents
                
                payload_property = iotevents.CfnAlarmModel.PayloadProperty(
                    content_expression="contentExpression",
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d18e90a4d474eeb87d607384857f4c582b60a985502109bd17120c0af558d368)
                check_type(argname="argument content_expression", value=content_expression, expected_type=type_hints["content_expression"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "content_expression": content_expression,
                "type": type,
            }

        @builtins.property
        def content_expression(self) -> builtins.str:
            '''The content of the payload.

            You can use a string expression that includes quoted strings ( ``'<string>'`` ), variables ( ``$variable.<variable-name>`` ), input values ( ``$input.<input-name>.<path-to-datum>`` ), string concatenations, and quoted strings that contain ``${}`` as the content. The recommended maximum size of a content expression is 1 KB.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-payload.html#cfn-iotevents-alarmmodel-payload-contentexpression
            '''
            result = self._values.get("content_expression")
            assert result is not None, "Required property 'content_expression' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def type(self) -> builtins.str:
            '''The value of the payload type can be either ``STRING`` or ``JSON`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-payload.html#cfn-iotevents-alarmmodel-payload-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PayloadProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotevents.CfnAlarmModel.SimpleRuleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "comparison_operator": "comparisonOperator",
            "input_property": "inputProperty",
            "threshold": "threshold",
        },
    )
    class SimpleRuleProperty:
        def __init__(
            self,
            *,
            comparison_operator: builtins.str,
            input_property: builtins.str,
            threshold: builtins.str,
        ) -> None:
            '''A rule that compares an input property value to a threshold value with a comparison operator.

            :param comparison_operator: The comparison operator.
            :param input_property: The value on the left side of the comparison operator. You can specify an AWS IoT Events input attribute as an input property.
            :param threshold: The value on the right side of the comparison operator. You can enter a number or specify an AWS IoT Events input attribute.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-simplerule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotevents as iotevents
                
                simple_rule_property = iotevents.CfnAlarmModel.SimpleRuleProperty(
                    comparison_operator="comparisonOperator",
                    input_property="inputProperty",
                    threshold="threshold"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__90136387b310cc21ca49a113bb812022359fee99174291ce490e1b433ef6b419)
                check_type(argname="argument comparison_operator", value=comparison_operator, expected_type=type_hints["comparison_operator"])
                check_type(argname="argument input_property", value=input_property, expected_type=type_hints["input_property"])
                check_type(argname="argument threshold", value=threshold, expected_type=type_hints["threshold"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "comparison_operator": comparison_operator,
                "input_property": input_property,
                "threshold": threshold,
            }

        @builtins.property
        def comparison_operator(self) -> builtins.str:
            '''The comparison operator.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-simplerule.html#cfn-iotevents-alarmmodel-simplerule-comparisonoperator
            '''
            result = self._values.get("comparison_operator")
            assert result is not None, "Required property 'comparison_operator' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def input_property(self) -> builtins.str:
            '''The value on the left side of the comparison operator.

            You can specify an AWS IoT Events input attribute as an input property.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-simplerule.html#cfn-iotevents-alarmmodel-simplerule-inputproperty
            '''
            result = self._values.get("input_property")
            assert result is not None, "Required property 'input_property' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def threshold(self) -> builtins.str:
            '''The value on the right side of the comparison operator.

            You can enter a number or specify an AWS IoT Events input attribute.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-simplerule.html#cfn-iotevents-alarmmodel-simplerule-threshold
            '''
            result = self._values.get("threshold")
            assert result is not None, "Required property 'threshold' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SimpleRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotevents.CfnAlarmModel.SnsProperty",
        jsii_struct_bases=[],
        name_mapping={"target_arn": "targetArn", "payload": "payload"},
    )
    class SnsProperty:
        def __init__(
            self,
            *,
            target_arn: builtins.str,
            payload: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAlarmModel.PayloadProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Information required to publish the Amazon SNS message.

            :param target_arn: The ARN of the Amazon SNS target where the message is sent.
            :param payload: You can configure the action payload when you send a message as an Amazon SNS push notification.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-sns.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotevents as iotevents
                
                sns_property = iotevents.CfnAlarmModel.SnsProperty(
                    target_arn="targetArn",
                
                    # the properties below are optional
                    payload=iotevents.CfnAlarmModel.PayloadProperty(
                        content_expression="contentExpression",
                        type="type"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ce9abb929fe2014828de206b11bb74d7efb0ce4f363c5b1fe4df056896e7de68)
                check_type(argname="argument target_arn", value=target_arn, expected_type=type_hints["target_arn"])
                check_type(argname="argument payload", value=payload, expected_type=type_hints["payload"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "target_arn": target_arn,
            }
            if payload is not None:
                self._values["payload"] = payload

        @builtins.property
        def target_arn(self) -> builtins.str:
            '''The ARN of the Amazon SNS target where the message is sent.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-sns.html#cfn-iotevents-alarmmodel-sns-targetarn
            '''
            result = self._values.get("target_arn")
            assert result is not None, "Required property 'target_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def payload(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAlarmModel.PayloadProperty"]]:
            '''You can configure the action payload when you send a message as an Amazon SNS push notification.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-sns.html#cfn-iotevents-alarmmodel-sns-payload
            '''
            result = self._values.get("payload")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAlarmModel.PayloadProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SnsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotevents.CfnAlarmModel.SqsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "queue_url": "queueUrl",
            "payload": "payload",
            "use_base64": "useBase64",
        },
    )
    class SqsProperty:
        def __init__(
            self,
            *,
            queue_url: builtins.str,
            payload: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAlarmModel.PayloadProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            use_base64: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Sends information about the detector model instance and the event that triggered the action to an Amazon SQS queue.

            :param queue_url: The URL of the SQS queue where the data is written.
            :param payload: You can configure the action payload when you send a message to an Amazon SQS queue.
            :param use_base64: Set this to TRUE if you want the data to be base-64 encoded before it is written to the queue. Otherwise, set this to FALSE.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-sqs.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotevents as iotevents
                
                sqs_property = iotevents.CfnAlarmModel.SqsProperty(
                    queue_url="queueUrl",
                
                    # the properties below are optional
                    payload=iotevents.CfnAlarmModel.PayloadProperty(
                        content_expression="contentExpression",
                        type="type"
                    ),
                    use_base64=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f53bd000fd0e8e8506df9f9b2dcacf36f61e120354ff39131baa459b8dfef188)
                check_type(argname="argument queue_url", value=queue_url, expected_type=type_hints["queue_url"])
                check_type(argname="argument payload", value=payload, expected_type=type_hints["payload"])
                check_type(argname="argument use_base64", value=use_base64, expected_type=type_hints["use_base64"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "queue_url": queue_url,
            }
            if payload is not None:
                self._values["payload"] = payload
            if use_base64 is not None:
                self._values["use_base64"] = use_base64

        @builtins.property
        def queue_url(self) -> builtins.str:
            '''The URL of the SQS queue where the data is written.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-sqs.html#cfn-iotevents-alarmmodel-sqs-queueurl
            '''
            result = self._values.get("queue_url")
            assert result is not None, "Required property 'queue_url' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def payload(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAlarmModel.PayloadProperty"]]:
            '''You can configure the action payload when you send a message to an Amazon SQS queue.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-sqs.html#cfn-iotevents-alarmmodel-sqs-payload
            '''
            result = self._values.get("payload")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAlarmModel.PayloadProperty"]], result)

        @builtins.property
        def use_base64(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Set this to TRUE if you want the data to be base-64 encoded before it is written to the queue.

            Otherwise, set this to FALSE.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-alarmmodel-sqs.html#cfn-iotevents-alarmmodel-sqs-usebase64
            '''
            result = self._values.get("use_base64")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SqsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iotevents.CfnAlarmModelProps",
    jsii_struct_bases=[],
    name_mapping={
        "alarm_rule": "alarmRule",
        "role_arn": "roleArn",
        "alarm_capabilities": "alarmCapabilities",
        "alarm_event_actions": "alarmEventActions",
        "alarm_model_description": "alarmModelDescription",
        "alarm_model_name": "alarmModelName",
        "key": "key",
        "severity": "severity",
        "tags": "tags",
    },
)
class CfnAlarmModelProps:
    def __init__(
        self,
        *,
        alarm_rule: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAlarmModel.AlarmRuleProperty, typing.Dict[builtins.str, typing.Any]]],
        role_arn: builtins.str,
        alarm_capabilities: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAlarmModel.AlarmCapabilitiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        alarm_event_actions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAlarmModel.AlarmEventActionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        alarm_model_description: typing.Optional[builtins.str] = None,
        alarm_model_name: typing.Optional[builtins.str] = None,
        key: typing.Optional[builtins.str] = None,
        severity: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnAlarmModel``.

        :param alarm_rule: Defines when your alarm is invoked.
        :param role_arn: The ARN of the IAM role that allows the alarm to perform actions and access AWS resources. For more information, see `Amazon Resource Names (ARNs) <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`_ in the *AWS General Reference* .
        :param alarm_capabilities: Contains the configuration information of alarm state changes.
        :param alarm_event_actions: Contains information about one or more alarm actions.
        :param alarm_model_description: The description of the alarm model.
        :param alarm_model_name: The name of the alarm model.
        :param key: An input attribute used as a key to create an alarm. AWS IoT Events routes `inputs <https://docs.aws.amazon.com/iotevents/latest/apireference/API_Input.html>`_ associated with this key to the alarm.
        :param severity: A non-negative integer that reflects the severity level of the alarm.
        :param tags: A list of key-value pairs that contain metadata for the alarm model. The tags help you manage the alarm model. For more information, see `Tagging your AWS IoT Events resources <https://docs.aws.amazon.com/iotevents/latest/developerguide/tagging-iotevents.html>`_ in the *AWS IoT Events Developer Guide* . You can create up to 50 tags for one alarm model.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-alarmmodel.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iotevents as iotevents
            
            cfn_alarm_model_props = iotevents.CfnAlarmModelProps(
                alarm_rule=iotevents.CfnAlarmModel.AlarmRuleProperty(
                    simple_rule=iotevents.CfnAlarmModel.SimpleRuleProperty(
                        comparison_operator="comparisonOperator",
                        input_property="inputProperty",
                        threshold="threshold"
                    )
                ),
                role_arn="roleArn",
            
                # the properties below are optional
                alarm_capabilities=iotevents.CfnAlarmModel.AlarmCapabilitiesProperty(
                    acknowledge_flow=iotevents.CfnAlarmModel.AcknowledgeFlowProperty(
                        enabled=False
                    ),
                    initialization_configuration=iotevents.CfnAlarmModel.InitializationConfigurationProperty(
                        disabled_on_initialization=False
                    )
                ),
                alarm_event_actions=iotevents.CfnAlarmModel.AlarmEventActionsProperty(
                    alarm_actions=[iotevents.CfnAlarmModel.AlarmActionProperty(
                        dynamo_db=iotevents.CfnAlarmModel.DynamoDBProperty(
                            hash_key_field="hashKeyField",
                            hash_key_value="hashKeyValue",
                            table_name="tableName",
            
                            # the properties below are optional
                            hash_key_type="hashKeyType",
                            operation="operation",
                            payload=iotevents.CfnAlarmModel.PayloadProperty(
                                content_expression="contentExpression",
                                type="type"
                            ),
                            payload_field="payloadField",
                            range_key_field="rangeKeyField",
                            range_key_type="rangeKeyType",
                            range_key_value="rangeKeyValue"
                        ),
                        dynamo_dBv2=iotevents.CfnAlarmModel.DynamoDBv2Property(
                            table_name="tableName",
            
                            # the properties below are optional
                            payload=iotevents.CfnAlarmModel.PayloadProperty(
                                content_expression="contentExpression",
                                type="type"
                            )
                        ),
                        firehose=iotevents.CfnAlarmModel.FirehoseProperty(
                            delivery_stream_name="deliveryStreamName",
            
                            # the properties below are optional
                            payload=iotevents.CfnAlarmModel.PayloadProperty(
                                content_expression="contentExpression",
                                type="type"
                            ),
                            separator="separator"
                        ),
                        iot_events=iotevents.CfnAlarmModel.IotEventsProperty(
                            input_name="inputName",
            
                            # the properties below are optional
                            payload=iotevents.CfnAlarmModel.PayloadProperty(
                                content_expression="contentExpression",
                                type="type"
                            )
                        ),
                        iot_site_wise=iotevents.CfnAlarmModel.IotSiteWiseProperty(
                            asset_id="assetId",
                            entry_id="entryId",
                            property_alias="propertyAlias",
                            property_id="propertyId",
                            property_value=iotevents.CfnAlarmModel.AssetPropertyValueProperty(
                                value=iotevents.CfnAlarmModel.AssetPropertyVariantProperty(
                                    boolean_value="booleanValue",
                                    double_value="doubleValue",
                                    integer_value="integerValue",
                                    string_value="stringValue"
                                ),
            
                                # the properties below are optional
                                quality="quality",
                                timestamp=iotevents.CfnAlarmModel.AssetPropertyTimestampProperty(
                                    time_in_seconds="timeInSeconds",
            
                                    # the properties below are optional
                                    offset_in_nanos="offsetInNanos"
                                )
                            )
                        ),
                        iot_topic_publish=iotevents.CfnAlarmModel.IotTopicPublishProperty(
                            mqtt_topic="mqttTopic",
            
                            # the properties below are optional
                            payload=iotevents.CfnAlarmModel.PayloadProperty(
                                content_expression="contentExpression",
                                type="type"
                            )
                        ),
                        lambda_=iotevents.CfnAlarmModel.LambdaProperty(
                            function_arn="functionArn",
            
                            # the properties below are optional
                            payload=iotevents.CfnAlarmModel.PayloadProperty(
                                content_expression="contentExpression",
                                type="type"
                            )
                        ),
                        sns=iotevents.CfnAlarmModel.SnsProperty(
                            target_arn="targetArn",
            
                            # the properties below are optional
                            payload=iotevents.CfnAlarmModel.PayloadProperty(
                                content_expression="contentExpression",
                                type="type"
                            )
                        ),
                        sqs=iotevents.CfnAlarmModel.SqsProperty(
                            queue_url="queueUrl",
            
                            # the properties below are optional
                            payload=iotevents.CfnAlarmModel.PayloadProperty(
                                content_expression="contentExpression",
                                type="type"
                            ),
                            use_base64=False
                        )
                    )]
                ),
                alarm_model_description="alarmModelDescription",
                alarm_model_name="alarmModelName",
                key="key",
                severity=123,
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20e728f3578307e805cd9079d426bae0a7ec729fb1c6704b7c6c04fd09cce9d8)
            check_type(argname="argument alarm_rule", value=alarm_rule, expected_type=type_hints["alarm_rule"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument alarm_capabilities", value=alarm_capabilities, expected_type=type_hints["alarm_capabilities"])
            check_type(argname="argument alarm_event_actions", value=alarm_event_actions, expected_type=type_hints["alarm_event_actions"])
            check_type(argname="argument alarm_model_description", value=alarm_model_description, expected_type=type_hints["alarm_model_description"])
            check_type(argname="argument alarm_model_name", value=alarm_model_name, expected_type=type_hints["alarm_model_name"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument severity", value=severity, expected_type=type_hints["severity"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "alarm_rule": alarm_rule,
            "role_arn": role_arn,
        }
        if alarm_capabilities is not None:
            self._values["alarm_capabilities"] = alarm_capabilities
        if alarm_event_actions is not None:
            self._values["alarm_event_actions"] = alarm_event_actions
        if alarm_model_description is not None:
            self._values["alarm_model_description"] = alarm_model_description
        if alarm_model_name is not None:
            self._values["alarm_model_name"] = alarm_model_name
        if key is not None:
            self._values["key"] = key
        if severity is not None:
            self._values["severity"] = severity
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def alarm_rule(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnAlarmModel.AlarmRuleProperty]:
        '''Defines when your alarm is invoked.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-alarmmodel.html#cfn-iotevents-alarmmodel-alarmrule
        '''
        result = self._values.get("alarm_rule")
        assert result is not None, "Required property 'alarm_rule' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnAlarmModel.AlarmRuleProperty], result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''The ARN of the IAM role that allows the alarm to perform actions and access AWS resources.

        For more information, see `Amazon Resource Names (ARNs) <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`_ in the *AWS General Reference* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-alarmmodel.html#cfn-iotevents-alarmmodel-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def alarm_capabilities(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAlarmModel.AlarmCapabilitiesProperty]]:
        '''Contains the configuration information of alarm state changes.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-alarmmodel.html#cfn-iotevents-alarmmodel-alarmcapabilities
        '''
        result = self._values.get("alarm_capabilities")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAlarmModel.AlarmCapabilitiesProperty]], result)

    @builtins.property
    def alarm_event_actions(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAlarmModel.AlarmEventActionsProperty]]:
        '''Contains information about one or more alarm actions.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-alarmmodel.html#cfn-iotevents-alarmmodel-alarmeventactions
        '''
        result = self._values.get("alarm_event_actions")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAlarmModel.AlarmEventActionsProperty]], result)

    @builtins.property
    def alarm_model_description(self) -> typing.Optional[builtins.str]:
        '''The description of the alarm model.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-alarmmodel.html#cfn-iotevents-alarmmodel-alarmmodeldescription
        '''
        result = self._values.get("alarm_model_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def alarm_model_name(self) -> typing.Optional[builtins.str]:
        '''The name of the alarm model.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-alarmmodel.html#cfn-iotevents-alarmmodel-alarmmodelname
        '''
        result = self._values.get("alarm_model_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''An input attribute used as a key to create an alarm.

        AWS IoT Events routes `inputs <https://docs.aws.amazon.com/iotevents/latest/apireference/API_Input.html>`_ associated with this key to the alarm.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-alarmmodel.html#cfn-iotevents-alarmmodel-key
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def severity(self) -> typing.Optional[jsii.Number]:
        '''A non-negative integer that reflects the severity level of the alarm.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-alarmmodel.html#cfn-iotevents-alarmmodel-severity
        '''
        result = self._values.get("severity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of key-value pairs that contain metadata for the alarm model.

        The tags help you manage the alarm model. For more information, see `Tagging your AWS IoT Events resources <https://docs.aws.amazon.com/iotevents/latest/developerguide/tagging-iotevents.html>`_ in the *AWS IoT Events Developer Guide* .

        You can create up to 50 tags for one alarm model.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-alarmmodel.html#cfn-iotevents-alarmmodel-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAlarmModelProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnDetectorModel(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iotevents.CfnDetectorModel",
):
    '''The AWS::IoTEvents::DetectorModel resource creates a detector model.

    You create a *detector model* (a model of your equipment or process) using *states* . For each state, you define conditional (Boolean) logic that evaluates the incoming inputs to detect significant events. When an event is detected, it can change the state or trigger custom-built or predefined actions using other AWS services. You can define additional events that trigger actions when entering or exiting a state and, optionally, when a condition is met. For more information, see `How to Use AWS IoT Events <https://docs.aws.amazon.com/iotevents/latest/developerguide/how-to-use-iotevents.html>`_ in the *AWS IoT Events Developer Guide* .
    .. epigraph::

       When you successfully update a detector model (using the AWS IoT Events console, AWS IoT Events API or CLI commands, or AWS CloudFormation ) all detector instances created by the model are reset to their initial states. (The detector's ``state`` , and the values of any variables and timers are reset.)

       When you successfully update a detector model (using the AWS IoT Events console, AWS IoT Events API or CLI commands, or AWS CloudFormation ) the version number of the detector model is incremented. (A detector model with version number 1 before the update has version number 2 after the update succeeds.)

       If you attempt to update a detector model using AWS CloudFormation and the update does not succeed, the system may, in some cases, restore the original detector model. When this occurs, the detector model's version is incremented twice (for example, from version 1 to version 3) and the detector instances are reset.

       Also, be aware that if you attempt to update several detector models at once using AWS CloudFormation , some updates may succeed and others fail. In this case, the effects on each detector model's detector instances and version number depend on whether the update succeeded or failed, with the results as stated.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-detectormodel.html
    :exampleMetadata: fixture=_generated

    Example::

        
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        detector_model_definition: typing.Union[_IResolvable_da3f097b, typing.Union["CfnDetectorModel.DetectorModelDefinitionProperty", typing.Dict[builtins.str, typing.Any]]],
        role_arn: builtins.str,
        detector_model_description: typing.Optional[builtins.str] = None,
        detector_model_name: typing.Optional[builtins.str] = None,
        evaluation_method: typing.Optional[builtins.str] = None,
        key: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param detector_model_definition: Information that defines how a detector operates.
        :param role_arn: The ARN of the role that grants permission to AWS IoT Events to perform its operations.
        :param detector_model_description: A brief description of the detector model.
        :param detector_model_name: The name of the detector model.
        :param evaluation_method: Information about the order in which events are evaluated and how actions are executed.
        :param key: The value used to identify a detector instance. When a device or system sends input, a new detector instance with a unique key value is created. AWS IoT Events can continue to route input to its corresponding detector instance based on this identifying information. This parameter uses a JSON-path expression to select the attribute-value pair in the message payload that is used for identification. To route the message to the correct detector instance, the device must send a message payload that contains the same attribute-value.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7801b6324e5f272a708fd3542c09e1cc61e7621f542ce11a4795b2717b8f7f3a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDetectorModelProps(
            detector_model_definition=detector_model_definition,
            role_arn=role_arn,
            detector_model_description=detector_model_description,
            detector_model_name=detector_model_name,
            evaluation_method=evaluation_method,
            key=key,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29f2e3393710755e327caeb1124191f98f1ffdfa48556729447af0457b842077)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9223278334ea0b572f1758d19c1e4bcc3469b9041fea558d47a8c0c09cdbf578)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

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
    @jsii.member(jsii_name="detectorModelDefinition")
    def detector_model_definition(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnDetectorModel.DetectorModelDefinitionProperty"]:
        '''Information that defines how a detector operates.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnDetectorModel.DetectorModelDefinitionProperty"], jsii.get(self, "detectorModelDefinition"))

    @detector_model_definition.setter
    def detector_model_definition(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnDetectorModel.DetectorModelDefinitionProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63791e6db81942e4097ff9f1b03dce0b5618f92376af9187df3403f25fe75d85)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "detectorModelDefinition", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''The ARN of the role that grants permission to AWS IoT Events to perform its operations.'''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea88e939b3cea49f4e92a8fa44670ef9976e22c5a0fb5fe78ac052fd14c5dab0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="detectorModelDescription")
    def detector_model_description(self) -> typing.Optional[builtins.str]:
        '''A brief description of the detector model.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "detectorModelDescription"))

    @detector_model_description.setter
    def detector_model_description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7eee7f26e62967552ad2a22246ac4aa020ed80878cef3e44ceb4849bba312eda)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "detectorModelDescription", value)

    @builtins.property
    @jsii.member(jsii_name="detectorModelName")
    def detector_model_name(self) -> typing.Optional[builtins.str]:
        '''The name of the detector model.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "detectorModelName"))

    @detector_model_name.setter
    def detector_model_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4faf59137fbafe31260e949107d4c02fc4239abc15c840bc619336d54bf866e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "detectorModelName", value)

    @builtins.property
    @jsii.member(jsii_name="evaluationMethod")
    def evaluation_method(self) -> typing.Optional[builtins.str]:
        '''Information about the order in which events are evaluated and how actions are executed.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "evaluationMethod"))

    @evaluation_method.setter
    def evaluation_method(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb0b24d2480d69d447d4a28a886f18008b5a68a52c7e66b5764230e251def06d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "evaluationMethod", value)

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> typing.Optional[builtins.str]:
        '''The value used to identify a detector instance.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "key"))

    @key.setter
    def key(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d0b60cb750a8707e4533e77383c39c786579957920ad5474c000e7a4565e4f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e0a32c9ce5c2628faeace1b70ec3577ac67b86fb20a6cdea89790127622b2feb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotevents.CfnDetectorModel.ActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "clear_timer": "clearTimer",
            "dynamo_db": "dynamoDb",
            "dynamo_d_bv2": "dynamoDBv2",
            "firehose": "firehose",
            "iot_events": "iotEvents",
            "iot_site_wise": "iotSiteWise",
            "iot_topic_publish": "iotTopicPublish",
            "lambda_": "lambda",
            "reset_timer": "resetTimer",
            "set_timer": "setTimer",
            "set_variable": "setVariable",
            "sns": "sns",
            "sqs": "sqs",
        },
    )
    class ActionProperty:
        def __init__(
            self,
            *,
            clear_timer: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDetectorModel.ClearTimerProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            dynamo_db: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDetectorModel.DynamoDBProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            dynamo_d_bv2: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDetectorModel.DynamoDBv2Property", typing.Dict[builtins.str, typing.Any]]]] = None,
            firehose: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDetectorModel.FirehoseProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            iot_events: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDetectorModel.IotEventsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            iot_site_wise: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDetectorModel.IotSiteWiseProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            iot_topic_publish: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDetectorModel.IotTopicPublishProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            lambda_: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDetectorModel.LambdaProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            reset_timer: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDetectorModel.ResetTimerProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            set_timer: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDetectorModel.SetTimerProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            set_variable: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDetectorModel.SetVariableProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            sns: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDetectorModel.SnsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            sqs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDetectorModel.SqsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''An action to be performed when the ``condition`` is TRUE.

            :param clear_timer: Information needed to clear the timer.
            :param dynamo_db: Writes to the DynamoDB table that you created. The default action payload contains all attribute-value pairs that have the information about the detector model instance and the event that triggered the action. You can customize the `payload <https://docs.aws.amazon.com/iotevents/latest/apireference/API_Payload.html>`_ . One column of the DynamoDB table receives all attribute-value pairs in the payload that you specify. For more information, see `Actions <https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-event-actions.html>`_ in *AWS IoT Events Developer Guide* .
            :param dynamo_d_bv2: Writes to the DynamoDB table that you created. The default action payload contains all attribute-value pairs that have the information about the detector model instance and the event that triggered the action. You can customize the `payload <https://docs.aws.amazon.com/iotevents/latest/apireference/API_Payload.html>`_ . A separate column of the DynamoDB table receives one attribute-value pair in the payload that you specify. For more information, see `Actions <https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-event-actions.html>`_ in *AWS IoT Events Developer Guide* .
            :param firehose: Sends information about the detector model instance and the event that triggered the action to an Amazon Kinesis Data Firehose delivery stream.
            :param iot_events: Sends AWS IoT Events input, which passes information about the detector model instance and the event that triggered the action.
            :param iot_site_wise: Sends information about the detector model instance and the event that triggered the action to an asset property in AWS IoT SiteWise .
            :param iot_topic_publish: Publishes an MQTT message with the given topic to the AWS IoT message broker.
            :param lambda_: Calls a Lambda function, passing in information about the detector model instance and the event that triggered the action.
            :param reset_timer: Information needed to reset the timer.
            :param set_timer: Information needed to set the timer.
            :param set_variable: Sets a variable to a specified value.
            :param sns: Sends an Amazon SNS message.
            :param sqs: Sends an Amazon SNS message.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-action.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotevents as iotevents
                
                action_property = iotevents.CfnDetectorModel.ActionProperty(
                    clear_timer=iotevents.CfnDetectorModel.ClearTimerProperty(
                        timer_name="timerName"
                    ),
                    dynamo_db=iotevents.CfnDetectorModel.DynamoDBProperty(
                        hash_key_field="hashKeyField",
                        hash_key_value="hashKeyValue",
                        table_name="tableName",
                
                        # the properties below are optional
                        hash_key_type="hashKeyType",
                        operation="operation",
                        payload=iotevents.CfnDetectorModel.PayloadProperty(
                            content_expression="contentExpression",
                            type="type"
                        ),
                        payload_field="payloadField",
                        range_key_field="rangeKeyField",
                        range_key_type="rangeKeyType",
                        range_key_value="rangeKeyValue"
                    ),
                    dynamo_dBv2=iotevents.CfnDetectorModel.DynamoDBv2Property(
                        table_name="tableName",
                
                        # the properties below are optional
                        payload=iotevents.CfnDetectorModel.PayloadProperty(
                            content_expression="contentExpression",
                            type="type"
                        )
                    ),
                    firehose=iotevents.CfnDetectorModel.FirehoseProperty(
                        delivery_stream_name="deliveryStreamName",
                
                        # the properties below are optional
                        payload=iotevents.CfnDetectorModel.PayloadProperty(
                            content_expression="contentExpression",
                            type="type"
                        ),
                        separator="separator"
                    ),
                    iot_events=iotevents.CfnDetectorModel.IotEventsProperty(
                        input_name="inputName",
                
                        # the properties below are optional
                        payload=iotevents.CfnDetectorModel.PayloadProperty(
                            content_expression="contentExpression",
                            type="type"
                        )
                    ),
                    iot_site_wise=iotevents.CfnDetectorModel.IotSiteWiseProperty(
                        property_value=iotevents.CfnDetectorModel.AssetPropertyValueProperty(
                            value=iotevents.CfnDetectorModel.AssetPropertyVariantProperty(
                                boolean_value="booleanValue",
                                double_value="doubleValue",
                                integer_value="integerValue",
                                string_value="stringValue"
                            ),
                
                            # the properties below are optional
                            quality="quality",
                            timestamp=iotevents.CfnDetectorModel.AssetPropertyTimestampProperty(
                                time_in_seconds="timeInSeconds",
                
                                # the properties below are optional
                                offset_in_nanos="offsetInNanos"
                            )
                        ),
                
                        # the properties below are optional
                        asset_id="assetId",
                        entry_id="entryId",
                        property_alias="propertyAlias",
                        property_id="propertyId"
                    ),
                    iot_topic_publish=iotevents.CfnDetectorModel.IotTopicPublishProperty(
                        mqtt_topic="mqttTopic",
                
                        # the properties below are optional
                        payload=iotevents.CfnDetectorModel.PayloadProperty(
                            content_expression="contentExpression",
                            type="type"
                        )
                    ),
                    lambda_=iotevents.CfnDetectorModel.LambdaProperty(
                        function_arn="functionArn",
                
                        # the properties below are optional
                        payload=iotevents.CfnDetectorModel.PayloadProperty(
                            content_expression="contentExpression",
                            type="type"
                        )
                    ),
                    reset_timer=iotevents.CfnDetectorModel.ResetTimerProperty(
                        timer_name="timerName"
                    ),
                    set_timer=iotevents.CfnDetectorModel.SetTimerProperty(
                        timer_name="timerName",
                
                        # the properties below are optional
                        duration_expression="durationExpression",
                        seconds=123
                    ),
                    set_variable=iotevents.CfnDetectorModel.SetVariableProperty(
                        value="value",
                        variable_name="variableName"
                    ),
                    sns=iotevents.CfnDetectorModel.SnsProperty(
                        target_arn="targetArn",
                
                        # the properties below are optional
                        payload=iotevents.CfnDetectorModel.PayloadProperty(
                            content_expression="contentExpression",
                            type="type"
                        )
                    ),
                    sqs=iotevents.CfnDetectorModel.SqsProperty(
                        queue_url="queueUrl",
                
                        # the properties below are optional
                        payload=iotevents.CfnDetectorModel.PayloadProperty(
                            content_expression="contentExpression",
                            type="type"
                        ),
                        use_base64=False
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__997f21492a6bca00169c7708a8d2827cc3198fda198345353c9092e56e7792c1)
                check_type(argname="argument clear_timer", value=clear_timer, expected_type=type_hints["clear_timer"])
                check_type(argname="argument dynamo_db", value=dynamo_db, expected_type=type_hints["dynamo_db"])
                check_type(argname="argument dynamo_d_bv2", value=dynamo_d_bv2, expected_type=type_hints["dynamo_d_bv2"])
                check_type(argname="argument firehose", value=firehose, expected_type=type_hints["firehose"])
                check_type(argname="argument iot_events", value=iot_events, expected_type=type_hints["iot_events"])
                check_type(argname="argument iot_site_wise", value=iot_site_wise, expected_type=type_hints["iot_site_wise"])
                check_type(argname="argument iot_topic_publish", value=iot_topic_publish, expected_type=type_hints["iot_topic_publish"])
                check_type(argname="argument lambda_", value=lambda_, expected_type=type_hints["lambda_"])
                check_type(argname="argument reset_timer", value=reset_timer, expected_type=type_hints["reset_timer"])
                check_type(argname="argument set_timer", value=set_timer, expected_type=type_hints["set_timer"])
                check_type(argname="argument set_variable", value=set_variable, expected_type=type_hints["set_variable"])
                check_type(argname="argument sns", value=sns, expected_type=type_hints["sns"])
                check_type(argname="argument sqs", value=sqs, expected_type=type_hints["sqs"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if clear_timer is not None:
                self._values["clear_timer"] = clear_timer
            if dynamo_db is not None:
                self._values["dynamo_db"] = dynamo_db
            if dynamo_d_bv2 is not None:
                self._values["dynamo_d_bv2"] = dynamo_d_bv2
            if firehose is not None:
                self._values["firehose"] = firehose
            if iot_events is not None:
                self._values["iot_events"] = iot_events
            if iot_site_wise is not None:
                self._values["iot_site_wise"] = iot_site_wise
            if iot_topic_publish is not None:
                self._values["iot_topic_publish"] = iot_topic_publish
            if lambda_ is not None:
                self._values["lambda_"] = lambda_
            if reset_timer is not None:
                self._values["reset_timer"] = reset_timer
            if set_timer is not None:
                self._values["set_timer"] = set_timer
            if set_variable is not None:
                self._values["set_variable"] = set_variable
            if sns is not None:
                self._values["sns"] = sns
            if sqs is not None:
                self._values["sqs"] = sqs

        @builtins.property
        def clear_timer(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDetectorModel.ClearTimerProperty"]]:
            '''Information needed to clear the timer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-action.html#cfn-iotevents-detectormodel-action-cleartimer
            '''
            result = self._values.get("clear_timer")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDetectorModel.ClearTimerProperty"]], result)

        @builtins.property
        def dynamo_db(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDetectorModel.DynamoDBProperty"]]:
            '''Writes to the DynamoDB table that you created.

            The default action payload contains all attribute-value pairs that have the information about the detector model instance and the event that triggered the action. You can customize the `payload <https://docs.aws.amazon.com/iotevents/latest/apireference/API_Payload.html>`_ . One column of the DynamoDB table receives all attribute-value pairs in the payload that you specify. For more information, see `Actions <https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-event-actions.html>`_ in *AWS IoT Events Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-action.html#cfn-iotevents-detectormodel-action-dynamodb
            '''
            result = self._values.get("dynamo_db")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDetectorModel.DynamoDBProperty"]], result)

        @builtins.property
        def dynamo_d_bv2(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDetectorModel.DynamoDBv2Property"]]:
            '''Writes to the DynamoDB table that you created.

            The default action payload contains all attribute-value pairs that have the information about the detector model instance and the event that triggered the action. You can customize the `payload <https://docs.aws.amazon.com/iotevents/latest/apireference/API_Payload.html>`_ . A separate column of the DynamoDB table receives one attribute-value pair in the payload that you specify. For more information, see `Actions <https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-event-actions.html>`_ in *AWS IoT Events Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-action.html#cfn-iotevents-detectormodel-action-dynamodbv2
            '''
            result = self._values.get("dynamo_d_bv2")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDetectorModel.DynamoDBv2Property"]], result)

        @builtins.property
        def firehose(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDetectorModel.FirehoseProperty"]]:
            '''Sends information about the detector model instance and the event that triggered the action to an Amazon Kinesis Data Firehose delivery stream.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-action.html#cfn-iotevents-detectormodel-action-firehose
            '''
            result = self._values.get("firehose")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDetectorModel.FirehoseProperty"]], result)

        @builtins.property
        def iot_events(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDetectorModel.IotEventsProperty"]]:
            '''Sends AWS IoT Events input, which passes information about the detector model instance and the event that triggered the action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-action.html#cfn-iotevents-detectormodel-action-iotevents
            '''
            result = self._values.get("iot_events")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDetectorModel.IotEventsProperty"]], result)

        @builtins.property
        def iot_site_wise(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDetectorModel.IotSiteWiseProperty"]]:
            '''Sends information about the detector model instance and the event that triggered the action to an asset property in AWS IoT SiteWise .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-action.html#cfn-iotevents-detectormodel-action-iotsitewise
            '''
            result = self._values.get("iot_site_wise")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDetectorModel.IotSiteWiseProperty"]], result)

        @builtins.property
        def iot_topic_publish(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDetectorModel.IotTopicPublishProperty"]]:
            '''Publishes an MQTT message with the given topic to the AWS IoT message broker.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-action.html#cfn-iotevents-detectormodel-action-iottopicpublish
            '''
            result = self._values.get("iot_topic_publish")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDetectorModel.IotTopicPublishProperty"]], result)

        @builtins.property
        def lambda_(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDetectorModel.LambdaProperty"]]:
            '''Calls a Lambda function, passing in information about the detector model instance and the event that triggered the action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-action.html#cfn-iotevents-detectormodel-action-lambda
            '''
            result = self._values.get("lambda_")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDetectorModel.LambdaProperty"]], result)

        @builtins.property
        def reset_timer(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDetectorModel.ResetTimerProperty"]]:
            '''Information needed to reset the timer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-action.html#cfn-iotevents-detectormodel-action-resettimer
            '''
            result = self._values.get("reset_timer")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDetectorModel.ResetTimerProperty"]], result)

        @builtins.property
        def set_timer(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDetectorModel.SetTimerProperty"]]:
            '''Information needed to set the timer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-action.html#cfn-iotevents-detectormodel-action-settimer
            '''
            result = self._values.get("set_timer")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDetectorModel.SetTimerProperty"]], result)

        @builtins.property
        def set_variable(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDetectorModel.SetVariableProperty"]]:
            '''Sets a variable to a specified value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-action.html#cfn-iotevents-detectormodel-action-setvariable
            '''
            result = self._values.get("set_variable")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDetectorModel.SetVariableProperty"]], result)

        @builtins.property
        def sns(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDetectorModel.SnsProperty"]]:
            '''Sends an Amazon SNS message.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-action.html#cfn-iotevents-detectormodel-action-sns
            '''
            result = self._values.get("sns")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDetectorModel.SnsProperty"]], result)

        @builtins.property
        def sqs(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDetectorModel.SqsProperty"]]:
            '''Sends an Amazon SNS message.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-action.html#cfn-iotevents-detectormodel-action-sqs
            '''
            result = self._values.get("sqs")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDetectorModel.SqsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotevents.CfnDetectorModel.AssetPropertyTimestampProperty",
        jsii_struct_bases=[],
        name_mapping={
            "time_in_seconds": "timeInSeconds",
            "offset_in_nanos": "offsetInNanos",
        },
    )
    class AssetPropertyTimestampProperty:
        def __init__(
            self,
            *,
            time_in_seconds: builtins.str,
            offset_in_nanos: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A structure that contains timestamp information. For more information, see `TimeInNanos <https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_TimeInNanos.html>`_ in the *AWS IoT SiteWise API Reference* .

            You must use expressions for all parameters in ``AssetPropertyTimestamp`` . The expressions accept literals, operators, functions, references, and substitution templates.

            **Examples** - For literal values, the expressions must contain single quotes. For example, the value for the ``timeInSeconds`` parameter can be ``'1586400675'`` .

            - For references, you must specify either variables or input values. For example, the value for the ``offsetInNanos`` parameter can be ``$variable.time`` .
            - For a substitution template, you must use ``${}`` , and the template must be in single quotes. A substitution template can also contain a combination of literals, operators, functions, references, and substitution templates.

            In the following example, the value for the ``timeInSeconds`` parameter uses a substitution template.

            ``'${$input.TemperatureInput.sensorData.timestamp / 1000}'``

            For more information, see `Expressions <https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-expressions.html>`_ in the *AWS IoT Events Developer Guide* .

            :param time_in_seconds: The timestamp, in seconds, in the Unix epoch format. The valid range is between 1-31556889864403199.
            :param offset_in_nanos: The nanosecond offset converted from ``timeInSeconds`` . The valid range is between 0-999999999.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-assetpropertytimestamp.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotevents as iotevents
                
                asset_property_timestamp_property = iotevents.CfnDetectorModel.AssetPropertyTimestampProperty(
                    time_in_seconds="timeInSeconds",
                
                    # the properties below are optional
                    offset_in_nanos="offsetInNanos"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d22f888073f939f0cd7ee06c54bc7d6cd951574ecee193dfed4f0e55492753e8)
                check_type(argname="argument time_in_seconds", value=time_in_seconds, expected_type=type_hints["time_in_seconds"])
                check_type(argname="argument offset_in_nanos", value=offset_in_nanos, expected_type=type_hints["offset_in_nanos"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "time_in_seconds": time_in_seconds,
            }
            if offset_in_nanos is not None:
                self._values["offset_in_nanos"] = offset_in_nanos

        @builtins.property
        def time_in_seconds(self) -> builtins.str:
            '''The timestamp, in seconds, in the Unix epoch format.

            The valid range is between 1-31556889864403199.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-assetpropertytimestamp.html#cfn-iotevents-detectormodel-assetpropertytimestamp-timeinseconds
            '''
            result = self._values.get("time_in_seconds")
            assert result is not None, "Required property 'time_in_seconds' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def offset_in_nanos(self) -> typing.Optional[builtins.str]:
            '''The nanosecond offset converted from ``timeInSeconds`` .

            The valid range is between 0-999999999.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-assetpropertytimestamp.html#cfn-iotevents-detectormodel-assetpropertytimestamp-offsetinnanos
            '''
            result = self._values.get("offset_in_nanos")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AssetPropertyTimestampProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotevents.CfnDetectorModel.AssetPropertyValueProperty",
        jsii_struct_bases=[],
        name_mapping={
            "value": "value",
            "quality": "quality",
            "timestamp": "timestamp",
        },
    )
    class AssetPropertyValueProperty:
        def __init__(
            self,
            *,
            value: typing.Union[_IResolvable_da3f097b, typing.Union["CfnDetectorModel.AssetPropertyVariantProperty", typing.Dict[builtins.str, typing.Any]]],
            quality: typing.Optional[builtins.str] = None,
            timestamp: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDetectorModel.AssetPropertyTimestampProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''A structure that contains value information. For more information, see `AssetPropertyValue <https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_AssetPropertyValue.html>`_ in the *AWS IoT SiteWise API Reference* .

            You must use expressions for all parameters in ``AssetPropertyValue`` . The expressions accept literals, operators, functions, references, and substitution templates.

            **Examples** - For literal values, the expressions must contain single quotes. For example, the value for the ``quality`` parameter can be ``'GOOD'`` .

            - For references, you must specify either variables or input values. For example, the value for the ``quality`` parameter can be ``$input.TemperatureInput.sensorData.quality`` .

            For more information, see `Expressions <https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-expressions.html>`_ in the *AWS IoT Events Developer Guide* .

            :param value: The value to send to an asset property.
            :param quality: The quality of the asset property value. The value must be ``'GOOD'`` , ``'BAD'`` , or ``'UNCERTAIN'`` .
            :param timestamp: The timestamp associated with the asset property value. The default is the current event time.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-assetpropertyvalue.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotevents as iotevents
                
                asset_property_value_property = iotevents.CfnDetectorModel.AssetPropertyValueProperty(
                    value=iotevents.CfnDetectorModel.AssetPropertyVariantProperty(
                        boolean_value="booleanValue",
                        double_value="doubleValue",
                        integer_value="integerValue",
                        string_value="stringValue"
                    ),
                
                    # the properties below are optional
                    quality="quality",
                    timestamp=iotevents.CfnDetectorModel.AssetPropertyTimestampProperty(
                        time_in_seconds="timeInSeconds",
                
                        # the properties below are optional
                        offset_in_nanos="offsetInNanos"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__49e6195d5246f0fc1891e1c7b239860858968a5d4b50a8581dcfcb07f3c93068)
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
                check_type(argname="argument quality", value=quality, expected_type=type_hints["quality"])
                check_type(argname="argument timestamp", value=timestamp, expected_type=type_hints["timestamp"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "value": value,
            }
            if quality is not None:
                self._values["quality"] = quality
            if timestamp is not None:
                self._values["timestamp"] = timestamp

        @builtins.property
        def value(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnDetectorModel.AssetPropertyVariantProperty"]:
            '''The value to send to an asset property.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-assetpropertyvalue.html#cfn-iotevents-detectormodel-assetpropertyvalue-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnDetectorModel.AssetPropertyVariantProperty"], result)

        @builtins.property
        def quality(self) -> typing.Optional[builtins.str]:
            '''The quality of the asset property value.

            The value must be ``'GOOD'`` , ``'BAD'`` , or ``'UNCERTAIN'`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-assetpropertyvalue.html#cfn-iotevents-detectormodel-assetpropertyvalue-quality
            '''
            result = self._values.get("quality")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def timestamp(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDetectorModel.AssetPropertyTimestampProperty"]]:
            '''The timestamp associated with the asset property value.

            The default is the current event time.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-assetpropertyvalue.html#cfn-iotevents-detectormodel-assetpropertyvalue-timestamp
            '''
            result = self._values.get("timestamp")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDetectorModel.AssetPropertyTimestampProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AssetPropertyValueProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotevents.CfnDetectorModel.AssetPropertyVariantProperty",
        jsii_struct_bases=[],
        name_mapping={
            "boolean_value": "booleanValue",
            "double_value": "doubleValue",
            "integer_value": "integerValue",
            "string_value": "stringValue",
        },
    )
    class AssetPropertyVariantProperty:
        def __init__(
            self,
            *,
            boolean_value: typing.Optional[builtins.str] = None,
            double_value: typing.Optional[builtins.str] = None,
            integer_value: typing.Optional[builtins.str] = None,
            string_value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A structure that contains an asset property value.

            For more information, see `Variant <https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_Variant.html>`_ in the *AWS IoT SiteWise API Reference* .

            You must use expressions for all parameters in ``AssetPropertyVariant`` . The expressions accept literals, operators, functions, references, and substitution templates.

            **Examples** - For literal values, the expressions must contain single quotes. For example, the value for the ``integerValue`` parameter can be ``'100'`` .

            - For references, you must specify either variables or parameters. For example, the value for the ``booleanValue`` parameter can be ``$variable.offline`` .
            - For a substitution template, you must use ``${}`` , and the template must be in single quotes. A substitution template can also contain a combination of literals, operators, functions, references, and substitution templates.

            In the following example, the value for the ``doubleValue`` parameter uses a substitution template.

            ``'${$input.TemperatureInput.sensorData.temperature * 6 / 5 + 32}'``

            For more information, see `Expressions <https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-expressions.html>`_ in the *AWS IoT Events Developer Guide* .

            You must specify one of the following value types, depending on the ``dataType`` of the specified asset property. For more information, see `AssetProperty <https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_AssetProperty.html>`_ in the *AWS IoT SiteWise API Reference* .

            :param boolean_value: The asset property value is a Boolean value that must be ``'TRUE'`` or ``'FALSE'`` . You must use an expression, and the evaluated result should be a Boolean value.
            :param double_value: The asset property value is a double. You must use an expression, and the evaluated result should be a double.
            :param integer_value: The asset property value is an integer. You must use an expression, and the evaluated result should be an integer.
            :param string_value: The asset property value is a string. You must use an expression, and the evaluated result should be a string.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-assetpropertyvariant.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotevents as iotevents
                
                asset_property_variant_property = iotevents.CfnDetectorModel.AssetPropertyVariantProperty(
                    boolean_value="booleanValue",
                    double_value="doubleValue",
                    integer_value="integerValue",
                    string_value="stringValue"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b8b56c1e6c67193acb9830ebc279e1835d5ff3fcd79e142ad47466b5a297929e)
                check_type(argname="argument boolean_value", value=boolean_value, expected_type=type_hints["boolean_value"])
                check_type(argname="argument double_value", value=double_value, expected_type=type_hints["double_value"])
                check_type(argname="argument integer_value", value=integer_value, expected_type=type_hints["integer_value"])
                check_type(argname="argument string_value", value=string_value, expected_type=type_hints["string_value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if boolean_value is not None:
                self._values["boolean_value"] = boolean_value
            if double_value is not None:
                self._values["double_value"] = double_value
            if integer_value is not None:
                self._values["integer_value"] = integer_value
            if string_value is not None:
                self._values["string_value"] = string_value

        @builtins.property
        def boolean_value(self) -> typing.Optional[builtins.str]:
            '''The asset property value is a Boolean value that must be ``'TRUE'`` or ``'FALSE'`` .

            You must use an expression, and the evaluated result should be a Boolean value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-assetpropertyvariant.html#cfn-iotevents-detectormodel-assetpropertyvariant-booleanvalue
            '''
            result = self._values.get("boolean_value")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def double_value(self) -> typing.Optional[builtins.str]:
            '''The asset property value is a double.

            You must use an expression, and the evaluated result should be a double.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-assetpropertyvariant.html#cfn-iotevents-detectormodel-assetpropertyvariant-doublevalue
            '''
            result = self._values.get("double_value")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def integer_value(self) -> typing.Optional[builtins.str]:
            '''The asset property value is an integer.

            You must use an expression, and the evaluated result should be an integer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-assetpropertyvariant.html#cfn-iotevents-detectormodel-assetpropertyvariant-integervalue
            '''
            result = self._values.get("integer_value")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def string_value(self) -> typing.Optional[builtins.str]:
            '''The asset property value is a string.

            You must use an expression, and the evaluated result should be a string.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-assetpropertyvariant.html#cfn-iotevents-detectormodel-assetpropertyvariant-stringvalue
            '''
            result = self._values.get("string_value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AssetPropertyVariantProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotevents.CfnDetectorModel.ClearTimerProperty",
        jsii_struct_bases=[],
        name_mapping={"timer_name": "timerName"},
    )
    class ClearTimerProperty:
        def __init__(self, *, timer_name: builtins.str) -> None:
            '''Information needed to clear the timer.

            :param timer_name: The name of the timer to clear.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-cleartimer.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotevents as iotevents
                
                clear_timer_property = iotevents.CfnDetectorModel.ClearTimerProperty(
                    timer_name="timerName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7875bb21ca70e3332dc63f20cd6808a6f0476f0bc6e28fd0b03d0a058575500b)
                check_type(argname="argument timer_name", value=timer_name, expected_type=type_hints["timer_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "timer_name": timer_name,
            }

        @builtins.property
        def timer_name(self) -> builtins.str:
            '''The name of the timer to clear.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-cleartimer.html#cfn-iotevents-detectormodel-cleartimer-timername
            '''
            result = self._values.get("timer_name")
            assert result is not None, "Required property 'timer_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ClearTimerProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotevents.CfnDetectorModel.DetectorModelDefinitionProperty",
        jsii_struct_bases=[],
        name_mapping={"initial_state_name": "initialStateName", "states": "states"},
    )
    class DetectorModelDefinitionProperty:
        def __init__(
            self,
            *,
            initial_state_name: builtins.str,
            states: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDetectorModel.StateProperty", typing.Dict[builtins.str, typing.Any]]]]],
        ) -> None:
            '''Information that defines how a detector operates.

            :param initial_state_name: The state that is entered at the creation of each detector (instance).
            :param states: Information about the states of the detector.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-detectormodeldefinition.html
            :exampleMetadata: fixture=_generated

            Example::

                
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6e1657c0e6d089d8b904914d9cdca2ff5841ab5284a6cbd6261e40e2c2fa9cb0)
                check_type(argname="argument initial_state_name", value=initial_state_name, expected_type=type_hints["initial_state_name"])
                check_type(argname="argument states", value=states, expected_type=type_hints["states"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "initial_state_name": initial_state_name,
                "states": states,
            }

        @builtins.property
        def initial_state_name(self) -> builtins.str:
            '''The state that is entered at the creation of each detector (instance).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-detectormodeldefinition.html#cfn-iotevents-detectormodel-detectormodeldefinition-initialstatename
            '''
            result = self._values.get("initial_state_name")
            assert result is not None, "Required property 'initial_state_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def states(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDetectorModel.StateProperty"]]]:
            '''Information about the states of the detector.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-detectormodeldefinition.html#cfn-iotevents-detectormodel-detectormodeldefinition-states
            '''
            result = self._values.get("states")
            assert result is not None, "Required property 'states' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDetectorModel.StateProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DetectorModelDefinitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotevents.CfnDetectorModel.DynamoDBProperty",
        jsii_struct_bases=[],
        name_mapping={
            "hash_key_field": "hashKeyField",
            "hash_key_value": "hashKeyValue",
            "table_name": "tableName",
            "hash_key_type": "hashKeyType",
            "operation": "operation",
            "payload": "payload",
            "payload_field": "payloadField",
            "range_key_field": "rangeKeyField",
            "range_key_type": "rangeKeyType",
            "range_key_value": "rangeKeyValue",
        },
    )
    class DynamoDBProperty:
        def __init__(
            self,
            *,
            hash_key_field: builtins.str,
            hash_key_value: builtins.str,
            table_name: builtins.str,
            hash_key_type: typing.Optional[builtins.str] = None,
            operation: typing.Optional[builtins.str] = None,
            payload: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDetectorModel.PayloadProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            payload_field: typing.Optional[builtins.str] = None,
            range_key_field: typing.Optional[builtins.str] = None,
            range_key_type: typing.Optional[builtins.str] = None,
            range_key_value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Defines an action to write to the Amazon DynamoDB table that you created.

            The standard action payload contains all the information about the detector model instance and the event that triggered the action. You can customize the `payload <https://docs.aws.amazon.com/iotevents/latest/apireference/API_Payload.html>`_ . One column of the DynamoDB table receives all attribute-value pairs in the payload that you specify.

            You must use expressions for all parameters in ``DynamoDBAction`` . The expressions accept literals, operators, functions, references, and substitution templates.

            **Examples** - For literal values, the expressions must contain single quotes. For example, the value for the ``hashKeyType`` parameter can be ``'STRING'`` .

            - For references, you must specify either variables or input values. For example, the value for the ``hashKeyField`` parameter can be ``$input.GreenhouseInput.name`` .
            - For a substitution template, you must use ``${}`` , and the template must be in single quotes. A substitution template can also contain a combination of literals, operators, functions, references, and substitution templates.

            In the following example, the value for the ``hashKeyValue`` parameter uses a substitution template.

            ``'${$input.GreenhouseInput.temperature * 6 / 5 + 32} in Fahrenheit'``

            - For a string concatenation, you must use ``+`` . A string concatenation can also contain a combination of literals, operators, functions, references, and substitution templates.

            In the following example, the value for the ``tableName`` parameter uses a string concatenation.

            ``'GreenhouseTemperatureTable ' + $input.GreenhouseInput.date``

            For more information, see `Expressions <https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-expressions.html>`_ in the *AWS IoT Events Developer Guide* .

            If the defined payload type is a string, ``DynamoDBAction`` writes non-JSON data to the DynamoDB table as binary data. The DynamoDB console displays the data as Base64-encoded text. The value for the ``payloadField`` parameter is ``<payload-field>_raw`` .

            :param hash_key_field: The name of the hash key (also called the partition key). The ``hashKeyField`` value must match the partition key of the target DynamoDB table.
            :param hash_key_value: The value of the hash key (also called the partition key).
            :param table_name: The name of the DynamoDB table. The ``tableName`` value must match the table name of the target DynamoDB table.
            :param hash_key_type: The data type for the hash key (also called the partition key). You can specify the following values:. - ``'STRING'`` - The hash key is a string. - ``'NUMBER'`` - The hash key is a number. If you don't specify ``hashKeyType`` , the default value is ``'STRING'`` .
            :param operation: The type of operation to perform. You can specify the following values:. - ``'INSERT'`` - Insert data as a new item into the DynamoDB table. This item uses the specified hash key as a partition key. If you specified a range key, the item uses the range key as a sort key. - ``'UPDATE'`` - Update an existing item of the DynamoDB table with new data. This item's partition key must match the specified hash key. If you specified a range key, the range key must match the item's sort key. - ``'DELETE'`` - Delete an existing item of the DynamoDB table. This item's partition key must match the specified hash key. If you specified a range key, the range key must match the item's sort key. If you don't specify this parameter, AWS IoT Events triggers the ``'INSERT'`` operation.
            :param payload: Information needed to configure the payload. By default, AWS IoT Events generates a standard payload in JSON for any action. This action payload contains all attribute-value pairs that have the information about the detector model instance and the event triggered the action. To configure the action payload, you can use ``contentExpression`` .
            :param payload_field: The name of the DynamoDB column that receives the action payload. If you don't specify this parameter, the name of the DynamoDB column is ``payload`` .
            :param range_key_field: The name of the range key (also called the sort key). The ``rangeKeyField`` value must match the sort key of the target DynamoDB table.
            :param range_key_type: The data type for the range key (also called the sort key), You can specify the following values:. - ``'STRING'`` - The range key is a string. - ``'NUMBER'`` - The range key is number. If you don't specify ``rangeKeyField`` , the default value is ``'STRING'`` .
            :param range_key_value: The value of the range key (also called the sort key).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-dynamodb.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotevents as iotevents
                
                dynamo_dBProperty = iotevents.CfnDetectorModel.DynamoDBProperty(
                    hash_key_field="hashKeyField",
                    hash_key_value="hashKeyValue",
                    table_name="tableName",
                
                    # the properties below are optional
                    hash_key_type="hashKeyType",
                    operation="operation",
                    payload=iotevents.CfnDetectorModel.PayloadProperty(
                        content_expression="contentExpression",
                        type="type"
                    ),
                    payload_field="payloadField",
                    range_key_field="rangeKeyField",
                    range_key_type="rangeKeyType",
                    range_key_value="rangeKeyValue"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8f20bd32cd2bf50da45c673c93066de3531126c3c989ecc1c664070a98ae2fde)
                check_type(argname="argument hash_key_field", value=hash_key_field, expected_type=type_hints["hash_key_field"])
                check_type(argname="argument hash_key_value", value=hash_key_value, expected_type=type_hints["hash_key_value"])
                check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
                check_type(argname="argument hash_key_type", value=hash_key_type, expected_type=type_hints["hash_key_type"])
                check_type(argname="argument operation", value=operation, expected_type=type_hints["operation"])
                check_type(argname="argument payload", value=payload, expected_type=type_hints["payload"])
                check_type(argname="argument payload_field", value=payload_field, expected_type=type_hints["payload_field"])
                check_type(argname="argument range_key_field", value=range_key_field, expected_type=type_hints["range_key_field"])
                check_type(argname="argument range_key_type", value=range_key_type, expected_type=type_hints["range_key_type"])
                check_type(argname="argument range_key_value", value=range_key_value, expected_type=type_hints["range_key_value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "hash_key_field": hash_key_field,
                "hash_key_value": hash_key_value,
                "table_name": table_name,
            }
            if hash_key_type is not None:
                self._values["hash_key_type"] = hash_key_type
            if operation is not None:
                self._values["operation"] = operation
            if payload is not None:
                self._values["payload"] = payload
            if payload_field is not None:
                self._values["payload_field"] = payload_field
            if range_key_field is not None:
                self._values["range_key_field"] = range_key_field
            if range_key_type is not None:
                self._values["range_key_type"] = range_key_type
            if range_key_value is not None:
                self._values["range_key_value"] = range_key_value

        @builtins.property
        def hash_key_field(self) -> builtins.str:
            '''The name of the hash key (also called the partition key).

            The ``hashKeyField`` value must match the partition key of the target DynamoDB table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-dynamodb.html#cfn-iotevents-detectormodel-dynamodb-hashkeyfield
            '''
            result = self._values.get("hash_key_field")
            assert result is not None, "Required property 'hash_key_field' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def hash_key_value(self) -> builtins.str:
            '''The value of the hash key (also called the partition key).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-dynamodb.html#cfn-iotevents-detectormodel-dynamodb-hashkeyvalue
            '''
            result = self._values.get("hash_key_value")
            assert result is not None, "Required property 'hash_key_value' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def table_name(self) -> builtins.str:
            '''The name of the DynamoDB table.

            The ``tableName`` value must match the table name of the target DynamoDB table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-dynamodb.html#cfn-iotevents-detectormodel-dynamodb-tablename
            '''
            result = self._values.get("table_name")
            assert result is not None, "Required property 'table_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def hash_key_type(self) -> typing.Optional[builtins.str]:
            '''The data type for the hash key (also called the partition key). You can specify the following values:.

            - ``'STRING'`` - The hash key is a string.
            - ``'NUMBER'`` - The hash key is a number.

            If you don't specify ``hashKeyType`` , the default value is ``'STRING'`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-dynamodb.html#cfn-iotevents-detectormodel-dynamodb-hashkeytype
            '''
            result = self._values.get("hash_key_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def operation(self) -> typing.Optional[builtins.str]:
            '''The type of operation to perform. You can specify the following values:.

            - ``'INSERT'`` - Insert data as a new item into the DynamoDB table. This item uses the specified hash key as a partition key. If you specified a range key, the item uses the range key as a sort key.
            - ``'UPDATE'`` - Update an existing item of the DynamoDB table with new data. This item's partition key must match the specified hash key. If you specified a range key, the range key must match the item's sort key.
            - ``'DELETE'`` - Delete an existing item of the DynamoDB table. This item's partition key must match the specified hash key. If you specified a range key, the range key must match the item's sort key.

            If you don't specify this parameter, AWS IoT Events triggers the ``'INSERT'`` operation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-dynamodb.html#cfn-iotevents-detectormodel-dynamodb-operation
            '''
            result = self._values.get("operation")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def payload(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDetectorModel.PayloadProperty"]]:
            '''Information needed to configure the payload.

            By default, AWS IoT Events generates a standard payload in JSON for any action. This action payload contains all attribute-value pairs that have the information about the detector model instance and the event triggered the action. To configure the action payload, you can use ``contentExpression`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-dynamodb.html#cfn-iotevents-detectormodel-dynamodb-payload
            '''
            result = self._values.get("payload")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDetectorModel.PayloadProperty"]], result)

        @builtins.property
        def payload_field(self) -> typing.Optional[builtins.str]:
            '''The name of the DynamoDB column that receives the action payload.

            If you don't specify this parameter, the name of the DynamoDB column is ``payload`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-dynamodb.html#cfn-iotevents-detectormodel-dynamodb-payloadfield
            '''
            result = self._values.get("payload_field")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def range_key_field(self) -> typing.Optional[builtins.str]:
            '''The name of the range key (also called the sort key).

            The ``rangeKeyField`` value must match the sort key of the target DynamoDB table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-dynamodb.html#cfn-iotevents-detectormodel-dynamodb-rangekeyfield
            '''
            result = self._values.get("range_key_field")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def range_key_type(self) -> typing.Optional[builtins.str]:
            '''The data type for the range key (also called the sort key), You can specify the following values:.

            - ``'STRING'`` - The range key is a string.
            - ``'NUMBER'`` - The range key is number.

            If you don't specify ``rangeKeyField`` , the default value is ``'STRING'`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-dynamodb.html#cfn-iotevents-detectormodel-dynamodb-rangekeytype
            '''
            result = self._values.get("range_key_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def range_key_value(self) -> typing.Optional[builtins.str]:
            '''The value of the range key (also called the sort key).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-dynamodb.html#cfn-iotevents-detectormodel-dynamodb-rangekeyvalue
            '''
            result = self._values.get("range_key_value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DynamoDBProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotevents.CfnDetectorModel.DynamoDBv2Property",
        jsii_struct_bases=[],
        name_mapping={"table_name": "tableName", "payload": "payload"},
    )
    class DynamoDBv2Property:
        def __init__(
            self,
            *,
            table_name: builtins.str,
            payload: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDetectorModel.PayloadProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Defines an action to write to the Amazon DynamoDB table that you created.

            The default action payload contains all the information about the detector model instance and the event that triggered the action. You can customize the `payload <https://docs.aws.amazon.com/iotevents/latest/apireference/API_Payload.html>`_ . A separate column of the DynamoDB table receives one attribute-value pair in the payload that you specify.

            You must use expressions for all parameters in ``DynamoDBv2Action`` . The expressions accept literals, operators, functions, references, and substitution templates.

            **Examples** - For literal values, the expressions must contain single quotes. For example, the value for the ``tableName`` parameter can be ``'GreenhouseTemperatureTable'`` .

            - For references, you must specify either variables or input values. For example, the value for the ``tableName`` parameter can be ``$variable.ddbtableName`` .
            - For a substitution template, you must use ``${}`` , and the template must be in single quotes. A substitution template can also contain a combination of literals, operators, functions, references, and substitution templates.

            In the following example, the value for the ``contentExpression`` parameter in ``Payload`` uses a substitution template.

            ``'{\\"sensorID\\": \\"${$input.GreenhouseInput.sensor_id}\\", \\"temperature\\": \\"${$input.GreenhouseInput.temperature * 9 / 5 + 32}\\"}'``

            - For a string concatenation, you must use ``+`` . A string concatenation can also contain a combination of literals, operators, functions, references, and substitution templates.

            In the following example, the value for the ``tableName`` parameter uses a string concatenation.

            ``'GreenhouseTemperatureTable ' + $input.GreenhouseInput.date``

            For more information, see `Expressions <https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-expressions.html>`_ in the *AWS IoT Events Developer Guide* .

            The value for the ``type`` parameter in ``Payload`` must be ``JSON`` .

            :param table_name: The name of the DynamoDB table.
            :param payload: Information needed to configure the payload. By default, AWS IoT Events generates a standard payload in JSON for any action. This action payload contains all attribute-value pairs that have the information about the detector model instance and the event triggered the action. To configure the action payload, you can use ``contentExpression`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-dynamodbv2.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotevents as iotevents
                
                dynamo_dBv2_property = iotevents.CfnDetectorModel.DynamoDBv2Property(
                    table_name="tableName",
                
                    # the properties below are optional
                    payload=iotevents.CfnDetectorModel.PayloadProperty(
                        content_expression="contentExpression",
                        type="type"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ce549d899ae554a89d320f79add62caba2098d6b98c681aa6ff7410626c6a145)
                check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
                check_type(argname="argument payload", value=payload, expected_type=type_hints["payload"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "table_name": table_name,
            }
            if payload is not None:
                self._values["payload"] = payload

        @builtins.property
        def table_name(self) -> builtins.str:
            '''The name of the DynamoDB table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-dynamodbv2.html#cfn-iotevents-detectormodel-dynamodbv2-tablename
            '''
            result = self._values.get("table_name")
            assert result is not None, "Required property 'table_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def payload(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDetectorModel.PayloadProperty"]]:
            '''Information needed to configure the payload.

            By default, AWS IoT Events generates a standard payload in JSON for any action. This action payload contains all attribute-value pairs that have the information about the detector model instance and the event triggered the action. To configure the action payload, you can use ``contentExpression`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-dynamodbv2.html#cfn-iotevents-detectormodel-dynamodbv2-payload
            '''
            result = self._values.get("payload")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDetectorModel.PayloadProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DynamoDBv2Property(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotevents.CfnDetectorModel.EventProperty",
        jsii_struct_bases=[],
        name_mapping={
            "event_name": "eventName",
            "actions": "actions",
            "condition": "condition",
        },
    )
    class EventProperty:
        def __init__(
            self,
            *,
            event_name: builtins.str,
            actions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDetectorModel.ActionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            condition: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies the ``actions`` to be performed when the ``condition`` evaluates to TRUE.

            :param event_name: The name of the event.
            :param actions: The actions to be performed.
            :param condition: Optional. The Boolean expression that, when TRUE, causes the ``actions`` to be performed. If not present, the actions are performed (=TRUE). If the expression result is not a Boolean value, the actions are not performed (=FALSE).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-event.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotevents as iotevents
                
                event_property = iotevents.CfnDetectorModel.EventProperty(
                    event_name="eventName",
                
                    # the properties below are optional
                    actions=[iotevents.CfnDetectorModel.ActionProperty(
                        clear_timer=iotevents.CfnDetectorModel.ClearTimerProperty(
                            timer_name="timerName"
                        ),
                        dynamo_db=iotevents.CfnDetectorModel.DynamoDBProperty(
                            hash_key_field="hashKeyField",
                            hash_key_value="hashKeyValue",
                            table_name="tableName",
                
                            # the properties below are optional
                            hash_key_type="hashKeyType",
                            operation="operation",
                            payload=iotevents.CfnDetectorModel.PayloadProperty(
                                content_expression="contentExpression",
                                type="type"
                            ),
                            payload_field="payloadField",
                            range_key_field="rangeKeyField",
                            range_key_type="rangeKeyType",
                            range_key_value="rangeKeyValue"
                        ),
                        dynamo_dBv2=iotevents.CfnDetectorModel.DynamoDBv2Property(
                            table_name="tableName",
                
                            # the properties below are optional
                            payload=iotevents.CfnDetectorModel.PayloadProperty(
                                content_expression="contentExpression",
                                type="type"
                            )
                        ),
                        firehose=iotevents.CfnDetectorModel.FirehoseProperty(
                            delivery_stream_name="deliveryStreamName",
                
                            # the properties below are optional
                            payload=iotevents.CfnDetectorModel.PayloadProperty(
                                content_expression="contentExpression",
                                type="type"
                            ),
                            separator="separator"
                        ),
                        iot_events=iotevents.CfnDetectorModel.IotEventsProperty(
                            input_name="inputName",
                
                            # the properties below are optional
                            payload=iotevents.CfnDetectorModel.PayloadProperty(
                                content_expression="contentExpression",
                                type="type"
                            )
                        ),
                        iot_site_wise=iotevents.CfnDetectorModel.IotSiteWiseProperty(
                            property_value=iotevents.CfnDetectorModel.AssetPropertyValueProperty(
                                value=iotevents.CfnDetectorModel.AssetPropertyVariantProperty(
                                    boolean_value="booleanValue",
                                    double_value="doubleValue",
                                    integer_value="integerValue",
                                    string_value="stringValue"
                                ),
                
                                # the properties below are optional
                                quality="quality",
                                timestamp=iotevents.CfnDetectorModel.AssetPropertyTimestampProperty(
                                    time_in_seconds="timeInSeconds",
                
                                    # the properties below are optional
                                    offset_in_nanos="offsetInNanos"
                                )
                            ),
                
                            # the properties below are optional
                            asset_id="assetId",
                            entry_id="entryId",
                            property_alias="propertyAlias",
                            property_id="propertyId"
                        ),
                        iot_topic_publish=iotevents.CfnDetectorModel.IotTopicPublishProperty(
                            mqtt_topic="mqttTopic",
                
                            # the properties below are optional
                            payload=iotevents.CfnDetectorModel.PayloadProperty(
                                content_expression="contentExpression",
                                type="type"
                            )
                        ),
                        lambda_=iotevents.CfnDetectorModel.LambdaProperty(
                            function_arn="functionArn",
                
                            # the properties below are optional
                            payload=iotevents.CfnDetectorModel.PayloadProperty(
                                content_expression="contentExpression",
                                type="type"
                            )
                        ),
                        reset_timer=iotevents.CfnDetectorModel.ResetTimerProperty(
                            timer_name="timerName"
                        ),
                        set_timer=iotevents.CfnDetectorModel.SetTimerProperty(
                            timer_name="timerName",
                
                            # the properties below are optional
                            duration_expression="durationExpression",
                            seconds=123
                        ),
                        set_variable=iotevents.CfnDetectorModel.SetVariableProperty(
                            value="value",
                            variable_name="variableName"
                        ),
                        sns=iotevents.CfnDetectorModel.SnsProperty(
                            target_arn="targetArn",
                
                            # the properties below are optional
                            payload=iotevents.CfnDetectorModel.PayloadProperty(
                                content_expression="contentExpression",
                                type="type"
                            )
                        ),
                        sqs=iotevents.CfnDetectorModel.SqsProperty(
                            queue_url="queueUrl",
                
                            # the properties below are optional
                            payload=iotevents.CfnDetectorModel.PayloadProperty(
                                content_expression="contentExpression",
                                type="type"
                            ),
                            use_base64=False
                        )
                    )],
                    condition="condition"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__717bd99991f8e8e6bcb7616faed1722ead70bd8378234a60048d02751c39bb8f)
                check_type(argname="argument event_name", value=event_name, expected_type=type_hints["event_name"])
                check_type(argname="argument actions", value=actions, expected_type=type_hints["actions"])
                check_type(argname="argument condition", value=condition, expected_type=type_hints["condition"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "event_name": event_name,
            }
            if actions is not None:
                self._values["actions"] = actions
            if condition is not None:
                self._values["condition"] = condition

        @builtins.property
        def event_name(self) -> builtins.str:
            '''The name of the event.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-event.html#cfn-iotevents-detectormodel-event-eventname
            '''
            result = self._values.get("event_name")
            assert result is not None, "Required property 'event_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def actions(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDetectorModel.ActionProperty"]]]]:
            '''The actions to be performed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-event.html#cfn-iotevents-detectormodel-event-actions
            '''
            result = self._values.get("actions")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDetectorModel.ActionProperty"]]]], result)

        @builtins.property
        def condition(self) -> typing.Optional[builtins.str]:
            '''Optional.

            The Boolean expression that, when TRUE, causes the ``actions`` to be performed. If not present, the actions are performed (=TRUE). If the expression result is not a Boolean value, the actions are not performed (=FALSE).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-event.html#cfn-iotevents-detectormodel-event-condition
            '''
            result = self._values.get("condition")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EventProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotevents.CfnDetectorModel.FirehoseProperty",
        jsii_struct_bases=[],
        name_mapping={
            "delivery_stream_name": "deliveryStreamName",
            "payload": "payload",
            "separator": "separator",
        },
    )
    class FirehoseProperty:
        def __init__(
            self,
            *,
            delivery_stream_name: builtins.str,
            payload: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDetectorModel.PayloadProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            separator: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Sends information about the detector model instance and the event that triggered the action to an Amazon Kinesis Data Firehose delivery stream.

            :param delivery_stream_name: The name of the Kinesis Data Firehose delivery stream where the data is written.
            :param payload: You can configure the action payload when you send a message to an Amazon Kinesis Data Firehose delivery stream.
            :param separator: A character separator that is used to separate records written to the Kinesis Data Firehose delivery stream. Valid values are: '\\n' (newline), '\\t' (tab), '\\r\\n' (Windows newline), ',' (comma).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-firehose.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotevents as iotevents
                
                firehose_property = iotevents.CfnDetectorModel.FirehoseProperty(
                    delivery_stream_name="deliveryStreamName",
                
                    # the properties below are optional
                    payload=iotevents.CfnDetectorModel.PayloadProperty(
                        content_expression="contentExpression",
                        type="type"
                    ),
                    separator="separator"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ff798f3ccc562e611abbd96aff8a343e927e8d0151d6debb2cdde0aa825102c5)
                check_type(argname="argument delivery_stream_name", value=delivery_stream_name, expected_type=type_hints["delivery_stream_name"])
                check_type(argname="argument payload", value=payload, expected_type=type_hints["payload"])
                check_type(argname="argument separator", value=separator, expected_type=type_hints["separator"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "delivery_stream_name": delivery_stream_name,
            }
            if payload is not None:
                self._values["payload"] = payload
            if separator is not None:
                self._values["separator"] = separator

        @builtins.property
        def delivery_stream_name(self) -> builtins.str:
            '''The name of the Kinesis Data Firehose delivery stream where the data is written.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-firehose.html#cfn-iotevents-detectormodel-firehose-deliverystreamname
            '''
            result = self._values.get("delivery_stream_name")
            assert result is not None, "Required property 'delivery_stream_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def payload(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDetectorModel.PayloadProperty"]]:
            '''You can configure the action payload when you send a message to an Amazon Kinesis Data Firehose delivery stream.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-firehose.html#cfn-iotevents-detectormodel-firehose-payload
            '''
            result = self._values.get("payload")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDetectorModel.PayloadProperty"]], result)

        @builtins.property
        def separator(self) -> typing.Optional[builtins.str]:
            '''A character separator that is used to separate records written to the Kinesis Data Firehose delivery stream.

            Valid values are: '\\n' (newline), '\\t' (tab), '\\r\\n' (Windows newline), ',' (comma).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-firehose.html#cfn-iotevents-detectormodel-firehose-separator
            '''
            result = self._values.get("separator")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FirehoseProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotevents.CfnDetectorModel.IotEventsProperty",
        jsii_struct_bases=[],
        name_mapping={"input_name": "inputName", "payload": "payload"},
    )
    class IotEventsProperty:
        def __init__(
            self,
            *,
            input_name: builtins.str,
            payload: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDetectorModel.PayloadProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Sends an AWS IoT Events input, passing in information about the detector model instance and the event that triggered the action.

            :param input_name: The name of the AWS IoT Events input where the data is sent.
            :param payload: You can configure the action payload when you send a message to an AWS IoT Events input.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-iotevents.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotevents as iotevents
                
                iot_events_property = iotevents.CfnDetectorModel.IotEventsProperty(
                    input_name="inputName",
                
                    # the properties below are optional
                    payload=iotevents.CfnDetectorModel.PayloadProperty(
                        content_expression="contentExpression",
                        type="type"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__39ebee23e3171868800d30327b2934e00faad4113cfed4549950bece31b8156b)
                check_type(argname="argument input_name", value=input_name, expected_type=type_hints["input_name"])
                check_type(argname="argument payload", value=payload, expected_type=type_hints["payload"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "input_name": input_name,
            }
            if payload is not None:
                self._values["payload"] = payload

        @builtins.property
        def input_name(self) -> builtins.str:
            '''The name of the AWS IoT Events input where the data is sent.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-iotevents.html#cfn-iotevents-detectormodel-iotevents-inputname
            '''
            result = self._values.get("input_name")
            assert result is not None, "Required property 'input_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def payload(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDetectorModel.PayloadProperty"]]:
            '''You can configure the action payload when you send a message to an AWS IoT Events input.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-iotevents.html#cfn-iotevents-detectormodel-iotevents-payload
            '''
            result = self._values.get("payload")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDetectorModel.PayloadProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IotEventsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotevents.CfnDetectorModel.IotSiteWiseProperty",
        jsii_struct_bases=[],
        name_mapping={
            "property_value": "propertyValue",
            "asset_id": "assetId",
            "entry_id": "entryId",
            "property_alias": "propertyAlias",
            "property_id": "propertyId",
        },
    )
    class IotSiteWiseProperty:
        def __init__(
            self,
            *,
            property_value: typing.Union[_IResolvable_da3f097b, typing.Union["CfnDetectorModel.AssetPropertyValueProperty", typing.Dict[builtins.str, typing.Any]]],
            asset_id: typing.Optional[builtins.str] = None,
            entry_id: typing.Optional[builtins.str] = None,
            property_alias: typing.Optional[builtins.str] = None,
            property_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Sends information about the detector model instance and the event that triggered the action to a specified asset property in AWS IoT SiteWise .

            You must use expressions for all parameters in ``IotSiteWiseAction`` . The expressions accept literals, operators, functions, references, and substitutions templates.

            **Examples** - For literal values, the expressions must contain single quotes. For example, the value for the ``propertyAlias`` parameter can be ``'/company/windfarm/3/turbine/7/temperature'`` .

            - For references, you must specify either variables or input values. For example, the value for the ``assetId`` parameter can be ``$input.TurbineInput.assetId1`` .
            - For a substitution template, you must use ``${}`` , and the template must be in single quotes. A substitution template can also contain a combination of literals, operators, functions, references, and substitution templates.

            In the following example, the value for the ``propertyAlias`` parameter uses a substitution template.

            ``'company/windfarm/${$input.TemperatureInput.sensorData.windfarmID}/turbine/ ${$input.TemperatureInput.sensorData.turbineID}/temperature'``

            You must specify either ``propertyAlias`` or both ``assetId`` and ``propertyId`` to identify the target asset property in AWS IoT SiteWise .

            For more information, see `Expressions <https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-expressions.html>`_ in the *AWS IoT Events Developer Guide* .

            :param property_value: The value to send to the asset property. This value contains timestamp, quality, and value (TQV) information.
            :param asset_id: The ID of the asset that has the specified property.
            :param entry_id: A unique identifier for this entry. You can use the entry ID to track which data entry causes an error in case of failure. The default is a new unique identifier.
            :param property_alias: The alias of the asset property.
            :param property_id: The ID of the asset property.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-iotsitewise.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotevents as iotevents
                
                iot_site_wise_property = iotevents.CfnDetectorModel.IotSiteWiseProperty(
                    property_value=iotevents.CfnDetectorModel.AssetPropertyValueProperty(
                        value=iotevents.CfnDetectorModel.AssetPropertyVariantProperty(
                            boolean_value="booleanValue",
                            double_value="doubleValue",
                            integer_value="integerValue",
                            string_value="stringValue"
                        ),
                
                        # the properties below are optional
                        quality="quality",
                        timestamp=iotevents.CfnDetectorModel.AssetPropertyTimestampProperty(
                            time_in_seconds="timeInSeconds",
                
                            # the properties below are optional
                            offset_in_nanos="offsetInNanos"
                        )
                    ),
                
                    # the properties below are optional
                    asset_id="assetId",
                    entry_id="entryId",
                    property_alias="propertyAlias",
                    property_id="propertyId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__297b1140450b226c15a66b0e140cd227d66d7d0506dd90d971a67e98e9a1da19)
                check_type(argname="argument property_value", value=property_value, expected_type=type_hints["property_value"])
                check_type(argname="argument asset_id", value=asset_id, expected_type=type_hints["asset_id"])
                check_type(argname="argument entry_id", value=entry_id, expected_type=type_hints["entry_id"])
                check_type(argname="argument property_alias", value=property_alias, expected_type=type_hints["property_alias"])
                check_type(argname="argument property_id", value=property_id, expected_type=type_hints["property_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "property_value": property_value,
            }
            if asset_id is not None:
                self._values["asset_id"] = asset_id
            if entry_id is not None:
                self._values["entry_id"] = entry_id
            if property_alias is not None:
                self._values["property_alias"] = property_alias
            if property_id is not None:
                self._values["property_id"] = property_id

        @builtins.property
        def property_value(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnDetectorModel.AssetPropertyValueProperty"]:
            '''The value to send to the asset property.

            This value contains timestamp, quality, and value (TQV) information.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-iotsitewise.html#cfn-iotevents-detectormodel-iotsitewise-propertyvalue
            '''
            result = self._values.get("property_value")
            assert result is not None, "Required property 'property_value' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnDetectorModel.AssetPropertyValueProperty"], result)

        @builtins.property
        def asset_id(self) -> typing.Optional[builtins.str]:
            '''The ID of the asset that has the specified property.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-iotsitewise.html#cfn-iotevents-detectormodel-iotsitewise-assetid
            '''
            result = self._values.get("asset_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def entry_id(self) -> typing.Optional[builtins.str]:
            '''A unique identifier for this entry.

            You can use the entry ID to track which data entry causes an error in case of failure. The default is a new unique identifier.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-iotsitewise.html#cfn-iotevents-detectormodel-iotsitewise-entryid
            '''
            result = self._values.get("entry_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def property_alias(self) -> typing.Optional[builtins.str]:
            '''The alias of the asset property.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-iotsitewise.html#cfn-iotevents-detectormodel-iotsitewise-propertyalias
            '''
            result = self._values.get("property_alias")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def property_id(self) -> typing.Optional[builtins.str]:
            '''The ID of the asset property.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-iotsitewise.html#cfn-iotevents-detectormodel-iotsitewise-propertyid
            '''
            result = self._values.get("property_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IotSiteWiseProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotevents.CfnDetectorModel.IotTopicPublishProperty",
        jsii_struct_bases=[],
        name_mapping={"mqtt_topic": "mqttTopic", "payload": "payload"},
    )
    class IotTopicPublishProperty:
        def __init__(
            self,
            *,
            mqtt_topic: builtins.str,
            payload: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDetectorModel.PayloadProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Information required to publish the MQTT message through the AWS IoT message broker.

            :param mqtt_topic: The MQTT topic of the message. You can use a string expression that includes variables ( ``$variable.<variable-name>`` ) and input values ( ``$input.<input-name>.<path-to-datum>`` ) as the topic string.
            :param payload: You can configure the action payload when you publish a message to an AWS IoT Core topic.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-iottopicpublish.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotevents as iotevents
                
                iot_topic_publish_property = iotevents.CfnDetectorModel.IotTopicPublishProperty(
                    mqtt_topic="mqttTopic",
                
                    # the properties below are optional
                    payload=iotevents.CfnDetectorModel.PayloadProperty(
                        content_expression="contentExpression",
                        type="type"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e9a560fbb56587b6f32e68c81fe2d3de4fde7ce4fb0967fd5f984981abf33e32)
                check_type(argname="argument mqtt_topic", value=mqtt_topic, expected_type=type_hints["mqtt_topic"])
                check_type(argname="argument payload", value=payload, expected_type=type_hints["payload"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "mqtt_topic": mqtt_topic,
            }
            if payload is not None:
                self._values["payload"] = payload

        @builtins.property
        def mqtt_topic(self) -> builtins.str:
            '''The MQTT topic of the message.

            You can use a string expression that includes variables ( ``$variable.<variable-name>`` ) and input values ( ``$input.<input-name>.<path-to-datum>`` ) as the topic string.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-iottopicpublish.html#cfn-iotevents-detectormodel-iottopicpublish-mqtttopic
            '''
            result = self._values.get("mqtt_topic")
            assert result is not None, "Required property 'mqtt_topic' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def payload(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDetectorModel.PayloadProperty"]]:
            '''You can configure the action payload when you publish a message to an AWS IoT Core topic.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-iottopicpublish.html#cfn-iotevents-detectormodel-iottopicpublish-payload
            '''
            result = self._values.get("payload")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDetectorModel.PayloadProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IotTopicPublishProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotevents.CfnDetectorModel.LambdaProperty",
        jsii_struct_bases=[],
        name_mapping={"function_arn": "functionArn", "payload": "payload"},
    )
    class LambdaProperty:
        def __init__(
            self,
            *,
            function_arn: builtins.str,
            payload: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDetectorModel.PayloadProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Calls a Lambda function, passing in information about the detector model instance and the event that triggered the action.

            :param function_arn: The ARN of the Lambda function that is executed.
            :param payload: You can configure the action payload when you send a message to a Lambda function.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-lambda.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotevents as iotevents
                
                lambda_property = iotevents.CfnDetectorModel.LambdaProperty(
                    function_arn="functionArn",
                
                    # the properties below are optional
                    payload=iotevents.CfnDetectorModel.PayloadProperty(
                        content_expression="contentExpression",
                        type="type"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__24efb01bfc6091499688a9ae496c6a60549dc83dd01e864646eaf8bf7add6359)
                check_type(argname="argument function_arn", value=function_arn, expected_type=type_hints["function_arn"])
                check_type(argname="argument payload", value=payload, expected_type=type_hints["payload"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "function_arn": function_arn,
            }
            if payload is not None:
                self._values["payload"] = payload

        @builtins.property
        def function_arn(self) -> builtins.str:
            '''The ARN of the Lambda function that is executed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-lambda.html#cfn-iotevents-detectormodel-lambda-functionarn
            '''
            result = self._values.get("function_arn")
            assert result is not None, "Required property 'function_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def payload(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDetectorModel.PayloadProperty"]]:
            '''You can configure the action payload when you send a message to a Lambda function.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-lambda.html#cfn-iotevents-detectormodel-lambda-payload
            '''
            result = self._values.get("payload")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDetectorModel.PayloadProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LambdaProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotevents.CfnDetectorModel.OnEnterProperty",
        jsii_struct_bases=[],
        name_mapping={"events": "events"},
    )
    class OnEnterProperty:
        def __init__(
            self,
            *,
            events: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDetectorModel.EventProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''When entering this state, perform these ``actions`` if the ``condition`` is TRUE.

            :param events: Specifies the actions that are performed when the state is entered and the ``condition`` is ``TRUE`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-onenter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotevents as iotevents
                
                on_enter_property = iotevents.CfnDetectorModel.OnEnterProperty(
                    events=[iotevents.CfnDetectorModel.EventProperty(
                        event_name="eventName",
                
                        # the properties below are optional
                        actions=[iotevents.CfnDetectorModel.ActionProperty(
                            clear_timer=iotevents.CfnDetectorModel.ClearTimerProperty(
                                timer_name="timerName"
                            ),
                            dynamo_db=iotevents.CfnDetectorModel.DynamoDBProperty(
                                hash_key_field="hashKeyField",
                                hash_key_value="hashKeyValue",
                                table_name="tableName",
                
                                # the properties below are optional
                                hash_key_type="hashKeyType",
                                operation="operation",
                                payload=iotevents.CfnDetectorModel.PayloadProperty(
                                    content_expression="contentExpression",
                                    type="type"
                                ),
                                payload_field="payloadField",
                                range_key_field="rangeKeyField",
                                range_key_type="rangeKeyType",
                                range_key_value="rangeKeyValue"
                            ),
                            dynamo_dBv2=iotevents.CfnDetectorModel.DynamoDBv2Property(
                                table_name="tableName",
                
                                # the properties below are optional
                                payload=iotevents.CfnDetectorModel.PayloadProperty(
                                    content_expression="contentExpression",
                                    type="type"
                                )
                            ),
                            firehose=iotevents.CfnDetectorModel.FirehoseProperty(
                                delivery_stream_name="deliveryStreamName",
                
                                # the properties below are optional
                                payload=iotevents.CfnDetectorModel.PayloadProperty(
                                    content_expression="contentExpression",
                                    type="type"
                                ),
                                separator="separator"
                            ),
                            iot_events=iotevents.CfnDetectorModel.IotEventsProperty(
                                input_name="inputName",
                
                                # the properties below are optional
                                payload=iotevents.CfnDetectorModel.PayloadProperty(
                                    content_expression="contentExpression",
                                    type="type"
                                )
                            ),
                            iot_site_wise=iotevents.CfnDetectorModel.IotSiteWiseProperty(
                                property_value=iotevents.CfnDetectorModel.AssetPropertyValueProperty(
                                    value=iotevents.CfnDetectorModel.AssetPropertyVariantProperty(
                                        boolean_value="booleanValue",
                                        double_value="doubleValue",
                                        integer_value="integerValue",
                                        string_value="stringValue"
                                    ),
                
                                    # the properties below are optional
                                    quality="quality",
                                    timestamp=iotevents.CfnDetectorModel.AssetPropertyTimestampProperty(
                                        time_in_seconds="timeInSeconds",
                
                                        # the properties below are optional
                                        offset_in_nanos="offsetInNanos"
                                    )
                                ),
                
                                # the properties below are optional
                                asset_id="assetId",
                                entry_id="entryId",
                                property_alias="propertyAlias",
                                property_id="propertyId"
                            ),
                            iot_topic_publish=iotevents.CfnDetectorModel.IotTopicPublishProperty(
                                mqtt_topic="mqttTopic",
                
                                # the properties below are optional
                                payload=iotevents.CfnDetectorModel.PayloadProperty(
                                    content_expression="contentExpression",
                                    type="type"
                                )
                            ),
                            lambda_=iotevents.CfnDetectorModel.LambdaProperty(
                                function_arn="functionArn",
                
                                # the properties below are optional
                                payload=iotevents.CfnDetectorModel.PayloadProperty(
                                    content_expression="contentExpression",
                                    type="type"
                                )
                            ),
                            reset_timer=iotevents.CfnDetectorModel.ResetTimerProperty(
                                timer_name="timerName"
                            ),
                            set_timer=iotevents.CfnDetectorModel.SetTimerProperty(
                                timer_name="timerName",
                
                                # the properties below are optional
                                duration_expression="durationExpression",
                                seconds=123
                            ),
                            set_variable=iotevents.CfnDetectorModel.SetVariableProperty(
                                value="value",
                                variable_name="variableName"
                            ),
                            sns=iotevents.CfnDetectorModel.SnsProperty(
                                target_arn="targetArn",
                
                                # the properties below are optional
                                payload=iotevents.CfnDetectorModel.PayloadProperty(
                                    content_expression="contentExpression",
                                    type="type"
                                )
                            ),
                            sqs=iotevents.CfnDetectorModel.SqsProperty(
                                queue_url="queueUrl",
                
                                # the properties below are optional
                                payload=iotevents.CfnDetectorModel.PayloadProperty(
                                    content_expression="contentExpression",
                                    type="type"
                                ),
                                use_base64=False
                            )
                        )],
                        condition="condition"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__aea0f4e8f57882389b42e8f7fa9e7bbe91614a1ae3730ce67ca2fbb72ca564a4)
                check_type(argname="argument events", value=events, expected_type=type_hints["events"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if events is not None:
                self._values["events"] = events

        @builtins.property
        def events(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDetectorModel.EventProperty"]]]]:
            '''Specifies the actions that are performed when the state is entered and the ``condition`` is ``TRUE`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-onenter.html#cfn-iotevents-detectormodel-onenter-events
            '''
            result = self._values.get("events")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDetectorModel.EventProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OnEnterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotevents.CfnDetectorModel.OnExitProperty",
        jsii_struct_bases=[],
        name_mapping={"events": "events"},
    )
    class OnExitProperty:
        def __init__(
            self,
            *,
            events: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDetectorModel.EventProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''When exiting this state, perform these ``actions`` if the specified ``condition`` is ``TRUE`` .

            :param events: Specifies the ``actions`` that are performed when the state is exited and the ``condition`` is ``TRUE`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-onexit.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotevents as iotevents
                
                on_exit_property = iotevents.CfnDetectorModel.OnExitProperty(
                    events=[iotevents.CfnDetectorModel.EventProperty(
                        event_name="eventName",
                
                        # the properties below are optional
                        actions=[iotevents.CfnDetectorModel.ActionProperty(
                            clear_timer=iotevents.CfnDetectorModel.ClearTimerProperty(
                                timer_name="timerName"
                            ),
                            dynamo_db=iotevents.CfnDetectorModel.DynamoDBProperty(
                                hash_key_field="hashKeyField",
                                hash_key_value="hashKeyValue",
                                table_name="tableName",
                
                                # the properties below are optional
                                hash_key_type="hashKeyType",
                                operation="operation",
                                payload=iotevents.CfnDetectorModel.PayloadProperty(
                                    content_expression="contentExpression",
                                    type="type"
                                ),
                                payload_field="payloadField",
                                range_key_field="rangeKeyField",
                                range_key_type="rangeKeyType",
                                range_key_value="rangeKeyValue"
                            ),
                            dynamo_dBv2=iotevents.CfnDetectorModel.DynamoDBv2Property(
                                table_name="tableName",
                
                                # the properties below are optional
                                payload=iotevents.CfnDetectorModel.PayloadProperty(
                                    content_expression="contentExpression",
                                    type="type"
                                )
                            ),
                            firehose=iotevents.CfnDetectorModel.FirehoseProperty(
                                delivery_stream_name="deliveryStreamName",
                
                                # the properties below are optional
                                payload=iotevents.CfnDetectorModel.PayloadProperty(
                                    content_expression="contentExpression",
                                    type="type"
                                ),
                                separator="separator"
                            ),
                            iot_events=iotevents.CfnDetectorModel.IotEventsProperty(
                                input_name="inputName",
                
                                # the properties below are optional
                                payload=iotevents.CfnDetectorModel.PayloadProperty(
                                    content_expression="contentExpression",
                                    type="type"
                                )
                            ),
                            iot_site_wise=iotevents.CfnDetectorModel.IotSiteWiseProperty(
                                property_value=iotevents.CfnDetectorModel.AssetPropertyValueProperty(
                                    value=iotevents.CfnDetectorModel.AssetPropertyVariantProperty(
                                        boolean_value="booleanValue",
                                        double_value="doubleValue",
                                        integer_value="integerValue",
                                        string_value="stringValue"
                                    ),
                
                                    # the properties below are optional
                                    quality="quality",
                                    timestamp=iotevents.CfnDetectorModel.AssetPropertyTimestampProperty(
                                        time_in_seconds="timeInSeconds",
                
                                        # the properties below are optional
                                        offset_in_nanos="offsetInNanos"
                                    )
                                ),
                
                                # the properties below are optional
                                asset_id="assetId",
                                entry_id="entryId",
                                property_alias="propertyAlias",
                                property_id="propertyId"
                            ),
                            iot_topic_publish=iotevents.CfnDetectorModel.IotTopicPublishProperty(
                                mqtt_topic="mqttTopic",
                
                                # the properties below are optional
                                payload=iotevents.CfnDetectorModel.PayloadProperty(
                                    content_expression="contentExpression",
                                    type="type"
                                )
                            ),
                            lambda_=iotevents.CfnDetectorModel.LambdaProperty(
                                function_arn="functionArn",
                
                                # the properties below are optional
                                payload=iotevents.CfnDetectorModel.PayloadProperty(
                                    content_expression="contentExpression",
                                    type="type"
                                )
                            ),
                            reset_timer=iotevents.CfnDetectorModel.ResetTimerProperty(
                                timer_name="timerName"
                            ),
                            set_timer=iotevents.CfnDetectorModel.SetTimerProperty(
                                timer_name="timerName",
                
                                # the properties below are optional
                                duration_expression="durationExpression",
                                seconds=123
                            ),
                            set_variable=iotevents.CfnDetectorModel.SetVariableProperty(
                                value="value",
                                variable_name="variableName"
                            ),
                            sns=iotevents.CfnDetectorModel.SnsProperty(
                                target_arn="targetArn",
                
                                # the properties below are optional
                                payload=iotevents.CfnDetectorModel.PayloadProperty(
                                    content_expression="contentExpression",
                                    type="type"
                                )
                            ),
                            sqs=iotevents.CfnDetectorModel.SqsProperty(
                                queue_url="queueUrl",
                
                                # the properties below are optional
                                payload=iotevents.CfnDetectorModel.PayloadProperty(
                                    content_expression="contentExpression",
                                    type="type"
                                ),
                                use_base64=False
                            )
                        )],
                        condition="condition"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__16290de6f98bd9f79c314df78ddd48700ce8ae4aeab4507ec4086fd6db4afb4e)
                check_type(argname="argument events", value=events, expected_type=type_hints["events"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if events is not None:
                self._values["events"] = events

        @builtins.property
        def events(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDetectorModel.EventProperty"]]]]:
            '''Specifies the ``actions`` that are performed when the state is exited and the ``condition`` is ``TRUE`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-onexit.html#cfn-iotevents-detectormodel-onexit-events
            '''
            result = self._values.get("events")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDetectorModel.EventProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OnExitProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotevents.CfnDetectorModel.OnInputProperty",
        jsii_struct_bases=[],
        name_mapping={"events": "events", "transition_events": "transitionEvents"},
    )
    class OnInputProperty:
        def __init__(
            self,
            *,
            events: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDetectorModel.EventProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            transition_events: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDetectorModel.TransitionEventProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Specifies the actions performed when the ``condition`` evaluates to TRUE.

            :param events: Specifies the actions performed when the ``condition`` evaluates to TRUE.
            :param transition_events: Specifies the actions performed, and the next state entered, when a ``condition`` evaluates to TRUE.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-oninput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotevents as iotevents
                
                on_input_property = iotevents.CfnDetectorModel.OnInputProperty(
                    events=[iotevents.CfnDetectorModel.EventProperty(
                        event_name="eventName",
                
                        # the properties below are optional
                        actions=[iotevents.CfnDetectorModel.ActionProperty(
                            clear_timer=iotevents.CfnDetectorModel.ClearTimerProperty(
                                timer_name="timerName"
                            ),
                            dynamo_db=iotevents.CfnDetectorModel.DynamoDBProperty(
                                hash_key_field="hashKeyField",
                                hash_key_value="hashKeyValue",
                                table_name="tableName",
                
                                # the properties below are optional
                                hash_key_type="hashKeyType",
                                operation="operation",
                                payload=iotevents.CfnDetectorModel.PayloadProperty(
                                    content_expression="contentExpression",
                                    type="type"
                                ),
                                payload_field="payloadField",
                                range_key_field="rangeKeyField",
                                range_key_type="rangeKeyType",
                                range_key_value="rangeKeyValue"
                            ),
                            dynamo_dBv2=iotevents.CfnDetectorModel.DynamoDBv2Property(
                                table_name="tableName",
                
                                # the properties below are optional
                                payload=iotevents.CfnDetectorModel.PayloadProperty(
                                    content_expression="contentExpression",
                                    type="type"
                                )
                            ),
                            firehose=iotevents.CfnDetectorModel.FirehoseProperty(
                                delivery_stream_name="deliveryStreamName",
                
                                # the properties below are optional
                                payload=iotevents.CfnDetectorModel.PayloadProperty(
                                    content_expression="contentExpression",
                                    type="type"
                                ),
                                separator="separator"
                            ),
                            iot_events=iotevents.CfnDetectorModel.IotEventsProperty(
                                input_name="inputName",
                
                                # the properties below are optional
                                payload=iotevents.CfnDetectorModel.PayloadProperty(
                                    content_expression="contentExpression",
                                    type="type"
                                )
                            ),
                            iot_site_wise=iotevents.CfnDetectorModel.IotSiteWiseProperty(
                                property_value=iotevents.CfnDetectorModel.AssetPropertyValueProperty(
                                    value=iotevents.CfnDetectorModel.AssetPropertyVariantProperty(
                                        boolean_value="booleanValue",
                                        double_value="doubleValue",
                                        integer_value="integerValue",
                                        string_value="stringValue"
                                    ),
                
                                    # the properties below are optional
                                    quality="quality",
                                    timestamp=iotevents.CfnDetectorModel.AssetPropertyTimestampProperty(
                                        time_in_seconds="timeInSeconds",
                
                                        # the properties below are optional
                                        offset_in_nanos="offsetInNanos"
                                    )
                                ),
                
                                # the properties below are optional
                                asset_id="assetId",
                                entry_id="entryId",
                                property_alias="propertyAlias",
                                property_id="propertyId"
                            ),
                            iot_topic_publish=iotevents.CfnDetectorModel.IotTopicPublishProperty(
                                mqtt_topic="mqttTopic",
                
                                # the properties below are optional
                                payload=iotevents.CfnDetectorModel.PayloadProperty(
                                    content_expression="contentExpression",
                                    type="type"
                                )
                            ),
                            lambda_=iotevents.CfnDetectorModel.LambdaProperty(
                                function_arn="functionArn",
                
                                # the properties below are optional
                                payload=iotevents.CfnDetectorModel.PayloadProperty(
                                    content_expression="contentExpression",
                                    type="type"
                                )
                            ),
                            reset_timer=iotevents.CfnDetectorModel.ResetTimerProperty(
                                timer_name="timerName"
                            ),
                            set_timer=iotevents.CfnDetectorModel.SetTimerProperty(
                                timer_name="timerName",
                
                                # the properties below are optional
                                duration_expression="durationExpression",
                                seconds=123
                            ),
                            set_variable=iotevents.CfnDetectorModel.SetVariableProperty(
                                value="value",
                                variable_name="variableName"
                            ),
                            sns=iotevents.CfnDetectorModel.SnsProperty(
                                target_arn="targetArn",
                
                                # the properties below are optional
                                payload=iotevents.CfnDetectorModel.PayloadProperty(
                                    content_expression="contentExpression",
                                    type="type"
                                )
                            ),
                            sqs=iotevents.CfnDetectorModel.SqsProperty(
                                queue_url="queueUrl",
                
                                # the properties below are optional
                                payload=iotevents.CfnDetectorModel.PayloadProperty(
                                    content_expression="contentExpression",
                                    type="type"
                                ),
                                use_base64=False
                            )
                        )],
                        condition="condition"
                    )],
                    transition_events=[iotevents.CfnDetectorModel.TransitionEventProperty(
                        condition="condition",
                        event_name="eventName",
                        next_state="nextState",
                
                        # the properties below are optional
                        actions=[iotevents.CfnDetectorModel.ActionProperty(
                            clear_timer=iotevents.CfnDetectorModel.ClearTimerProperty(
                                timer_name="timerName"
                            ),
                            dynamo_db=iotevents.CfnDetectorModel.DynamoDBProperty(
                                hash_key_field="hashKeyField",
                                hash_key_value="hashKeyValue",
                                table_name="tableName",
                
                                # the properties below are optional
                                hash_key_type="hashKeyType",
                                operation="operation",
                                payload=iotevents.CfnDetectorModel.PayloadProperty(
                                    content_expression="contentExpression",
                                    type="type"
                                ),
                                payload_field="payloadField",
                                range_key_field="rangeKeyField",
                                range_key_type="rangeKeyType",
                                range_key_value="rangeKeyValue"
                            ),
                            dynamo_dBv2=iotevents.CfnDetectorModel.DynamoDBv2Property(
                                table_name="tableName",
                
                                # the properties below are optional
                                payload=iotevents.CfnDetectorModel.PayloadProperty(
                                    content_expression="contentExpression",
                                    type="type"
                                )
                            ),
                            firehose=iotevents.CfnDetectorModel.FirehoseProperty(
                                delivery_stream_name="deliveryStreamName",
                
                                # the properties below are optional
                                payload=iotevents.CfnDetectorModel.PayloadProperty(
                                    content_expression="contentExpression",
                                    type="type"
                                ),
                                separator="separator"
                            ),
                            iot_events=iotevents.CfnDetectorModel.IotEventsProperty(
                                input_name="inputName",
                
                                # the properties below are optional
                                payload=iotevents.CfnDetectorModel.PayloadProperty(
                                    content_expression="contentExpression",
                                    type="type"
                                )
                            ),
                            iot_site_wise=iotevents.CfnDetectorModel.IotSiteWiseProperty(
                                property_value=iotevents.CfnDetectorModel.AssetPropertyValueProperty(
                                    value=iotevents.CfnDetectorModel.AssetPropertyVariantProperty(
                                        boolean_value="booleanValue",
                                        double_value="doubleValue",
                                        integer_value="integerValue",
                                        string_value="stringValue"
                                    ),
                
                                    # the properties below are optional
                                    quality="quality",
                                    timestamp=iotevents.CfnDetectorModel.AssetPropertyTimestampProperty(
                                        time_in_seconds="timeInSeconds",
                
                                        # the properties below are optional
                                        offset_in_nanos="offsetInNanos"
                                    )
                                ),
                
                                # the properties below are optional
                                asset_id="assetId",
                                entry_id="entryId",
                                property_alias="propertyAlias",
                                property_id="propertyId"
                            ),
                            iot_topic_publish=iotevents.CfnDetectorModel.IotTopicPublishProperty(
                                mqtt_topic="mqttTopic",
                
                                # the properties below are optional
                                payload=iotevents.CfnDetectorModel.PayloadProperty(
                                    content_expression="contentExpression",
                                    type="type"
                                )
                            ),
                            lambda_=iotevents.CfnDetectorModel.LambdaProperty(
                                function_arn="functionArn",
                
                                # the properties below are optional
                                payload=iotevents.CfnDetectorModel.PayloadProperty(
                                    content_expression="contentExpression",
                                    type="type"
                                )
                            ),
                            reset_timer=iotevents.CfnDetectorModel.ResetTimerProperty(
                                timer_name="timerName"
                            ),
                            set_timer=iotevents.CfnDetectorModel.SetTimerProperty(
                                timer_name="timerName",
                
                                # the properties below are optional
                                duration_expression="durationExpression",
                                seconds=123
                            ),
                            set_variable=iotevents.CfnDetectorModel.SetVariableProperty(
                                value="value",
                                variable_name="variableName"
                            ),
                            sns=iotevents.CfnDetectorModel.SnsProperty(
                                target_arn="targetArn",
                
                                # the properties below are optional
                                payload=iotevents.CfnDetectorModel.PayloadProperty(
                                    content_expression="contentExpression",
                                    type="type"
                                )
                            ),
                            sqs=iotevents.CfnDetectorModel.SqsProperty(
                                queue_url="queueUrl",
                
                                # the properties below are optional
                                payload=iotevents.CfnDetectorModel.PayloadProperty(
                                    content_expression="contentExpression",
                                    type="type"
                                ),
                                use_base64=False
                            )
                        )]
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b69ba177ba3a33e678e1629e61da95d0b56c6dbeb0deed847a52a5b6f265ecf9)
                check_type(argname="argument events", value=events, expected_type=type_hints["events"])
                check_type(argname="argument transition_events", value=transition_events, expected_type=type_hints["transition_events"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if events is not None:
                self._values["events"] = events
            if transition_events is not None:
                self._values["transition_events"] = transition_events

        @builtins.property
        def events(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDetectorModel.EventProperty"]]]]:
            '''Specifies the actions performed when the ``condition`` evaluates to TRUE.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-oninput.html#cfn-iotevents-detectormodel-oninput-events
            '''
            result = self._values.get("events")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDetectorModel.EventProperty"]]]], result)

        @builtins.property
        def transition_events(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDetectorModel.TransitionEventProperty"]]]]:
            '''Specifies the actions performed, and the next state entered, when a ``condition`` evaluates to TRUE.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-oninput.html#cfn-iotevents-detectormodel-oninput-transitionevents
            '''
            result = self._values.get("transition_events")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDetectorModel.TransitionEventProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OnInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotevents.CfnDetectorModel.PayloadProperty",
        jsii_struct_bases=[],
        name_mapping={"content_expression": "contentExpression", "type": "type"},
    )
    class PayloadProperty:
        def __init__(
            self,
            *,
            content_expression: builtins.str,
            type: builtins.str,
        ) -> None:
            '''Information needed to configure the payload.

            By default, AWS IoT Events generates a standard payload in JSON for any action. This action payload contains all attribute-value pairs that have the information about the detector model instance and the event triggered the action. To configure the action payload, you can use ``contentExpression`` .

            :param content_expression: The content of the payload. You can use a string expression that includes quoted strings ( ``'<string>'`` ), variables ( ``$variable.<variable-name>`` ), input values ( ``$input.<input-name>.<path-to-datum>`` ), string concatenations, and quoted strings that contain ``${}`` as the content. The recommended maximum size of a content expression is 1 KB.
            :param type: The value of the payload type can be either ``STRING`` or ``JSON`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-payload.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotevents as iotevents
                
                payload_property = iotevents.CfnDetectorModel.PayloadProperty(
                    content_expression="contentExpression",
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2790fb31ad2046e675044abc890e4a9085c827804c7dd2da845e301a57019f18)
                check_type(argname="argument content_expression", value=content_expression, expected_type=type_hints["content_expression"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "content_expression": content_expression,
                "type": type,
            }

        @builtins.property
        def content_expression(self) -> builtins.str:
            '''The content of the payload.

            You can use a string expression that includes quoted strings ( ``'<string>'`` ), variables ( ``$variable.<variable-name>`` ), input values ( ``$input.<input-name>.<path-to-datum>`` ), string concatenations, and quoted strings that contain ``${}`` as the content. The recommended maximum size of a content expression is 1 KB.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-payload.html#cfn-iotevents-detectormodel-payload-contentexpression
            '''
            result = self._values.get("content_expression")
            assert result is not None, "Required property 'content_expression' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def type(self) -> builtins.str:
            '''The value of the payload type can be either ``STRING`` or ``JSON`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-payload.html#cfn-iotevents-detectormodel-payload-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PayloadProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotevents.CfnDetectorModel.ResetTimerProperty",
        jsii_struct_bases=[],
        name_mapping={"timer_name": "timerName"},
    )
    class ResetTimerProperty:
        def __init__(self, *, timer_name: builtins.str) -> None:
            '''Information required to reset the timer.

            The timer is reset to the previously evaluated result of the duration. The duration expression isn't reevaluated when you reset the timer.

            :param timer_name: The name of the timer to reset.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-resettimer.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotevents as iotevents
                
                reset_timer_property = iotevents.CfnDetectorModel.ResetTimerProperty(
                    timer_name="timerName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cfaaeea93082e9ba0d53049569b60b8aab40bba790a2912a29e4e02e1cad5bee)
                check_type(argname="argument timer_name", value=timer_name, expected_type=type_hints["timer_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "timer_name": timer_name,
            }

        @builtins.property
        def timer_name(self) -> builtins.str:
            '''The name of the timer to reset.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-resettimer.html#cfn-iotevents-detectormodel-resettimer-timername
            '''
            result = self._values.get("timer_name")
            assert result is not None, "Required property 'timer_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResetTimerProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotevents.CfnDetectorModel.SetTimerProperty",
        jsii_struct_bases=[],
        name_mapping={
            "timer_name": "timerName",
            "duration_expression": "durationExpression",
            "seconds": "seconds",
        },
    )
    class SetTimerProperty:
        def __init__(
            self,
            *,
            timer_name: builtins.str,
            duration_expression: typing.Optional[builtins.str] = None,
            seconds: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Information needed to set the timer.

            :param timer_name: The name of the timer.
            :param duration_expression: The duration of the timer, in seconds. You can use a string expression that includes numbers, variables ( ``$variable.<variable-name>`` ), and input values ( ``$input.<input-name>.<path-to-datum>`` ) as the duration. The range of the duration is 1-31622400 seconds. To ensure accuracy, the minimum duration is 60 seconds. The evaluated result of the duration is rounded down to the nearest whole number.
            :param seconds: The number of seconds until the timer expires. The minimum value is 60 seconds to ensure accuracy. The maximum value is 31622400 seconds.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-settimer.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotevents as iotevents
                
                set_timer_property = iotevents.CfnDetectorModel.SetTimerProperty(
                    timer_name="timerName",
                
                    # the properties below are optional
                    duration_expression="durationExpression",
                    seconds=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e2d0222e1d4ee3749b41430abba08489b16cf1a6a208820083451b0c210a1d77)
                check_type(argname="argument timer_name", value=timer_name, expected_type=type_hints["timer_name"])
                check_type(argname="argument duration_expression", value=duration_expression, expected_type=type_hints["duration_expression"])
                check_type(argname="argument seconds", value=seconds, expected_type=type_hints["seconds"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "timer_name": timer_name,
            }
            if duration_expression is not None:
                self._values["duration_expression"] = duration_expression
            if seconds is not None:
                self._values["seconds"] = seconds

        @builtins.property
        def timer_name(self) -> builtins.str:
            '''The name of the timer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-settimer.html#cfn-iotevents-detectormodel-settimer-timername
            '''
            result = self._values.get("timer_name")
            assert result is not None, "Required property 'timer_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def duration_expression(self) -> typing.Optional[builtins.str]:
            '''The duration of the timer, in seconds.

            You can use a string expression that includes numbers, variables ( ``$variable.<variable-name>`` ), and input values ( ``$input.<input-name>.<path-to-datum>`` ) as the duration. The range of the duration is 1-31622400 seconds. To ensure accuracy, the minimum duration is 60 seconds. The evaluated result of the duration is rounded down to the nearest whole number.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-settimer.html#cfn-iotevents-detectormodel-settimer-durationexpression
            '''
            result = self._values.get("duration_expression")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def seconds(self) -> typing.Optional[jsii.Number]:
            '''The number of seconds until the timer expires.

            The minimum value is 60 seconds to ensure accuracy. The maximum value is 31622400 seconds.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-settimer.html#cfn-iotevents-detectormodel-settimer-seconds
            '''
            result = self._values.get("seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SetTimerProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotevents.CfnDetectorModel.SetVariableProperty",
        jsii_struct_bases=[],
        name_mapping={"value": "value", "variable_name": "variableName"},
    )
    class SetVariableProperty:
        def __init__(self, *, value: builtins.str, variable_name: builtins.str) -> None:
            '''Information about the variable and its new value.

            :param value: The new value of the variable.
            :param variable_name: The name of the variable.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-setvariable.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotevents as iotevents
                
                set_variable_property = iotevents.CfnDetectorModel.SetVariableProperty(
                    value="value",
                    variable_name="variableName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f45edf8a7eb1797088c2f77a7e60ad9575cd7f0fc5b734c5a8bb4930902ab37b)
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
                check_type(argname="argument variable_name", value=variable_name, expected_type=type_hints["variable_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "value": value,
                "variable_name": variable_name,
            }

        @builtins.property
        def value(self) -> builtins.str:
            '''The new value of the variable.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-setvariable.html#cfn-iotevents-detectormodel-setvariable-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def variable_name(self) -> builtins.str:
            '''The name of the variable.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-setvariable.html#cfn-iotevents-detectormodel-setvariable-variablename
            '''
            result = self._values.get("variable_name")
            assert result is not None, "Required property 'variable_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SetVariableProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotevents.CfnDetectorModel.SnsProperty",
        jsii_struct_bases=[],
        name_mapping={"target_arn": "targetArn", "payload": "payload"},
    )
    class SnsProperty:
        def __init__(
            self,
            *,
            target_arn: builtins.str,
            payload: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDetectorModel.PayloadProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Information required to publish the Amazon SNS message.

            :param target_arn: The ARN of the Amazon SNS target where the message is sent.
            :param payload: You can configure the action payload when you send a message as an Amazon SNS push notification.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-sns.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotevents as iotevents
                
                sns_property = iotevents.CfnDetectorModel.SnsProperty(
                    target_arn="targetArn",
                
                    # the properties below are optional
                    payload=iotevents.CfnDetectorModel.PayloadProperty(
                        content_expression="contentExpression",
                        type="type"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__aa8303f7597b5d5f0f82a97b7668999b73c7153f44a25feadcc0c469f8fa3ab7)
                check_type(argname="argument target_arn", value=target_arn, expected_type=type_hints["target_arn"])
                check_type(argname="argument payload", value=payload, expected_type=type_hints["payload"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "target_arn": target_arn,
            }
            if payload is not None:
                self._values["payload"] = payload

        @builtins.property
        def target_arn(self) -> builtins.str:
            '''The ARN of the Amazon SNS target where the message is sent.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-sns.html#cfn-iotevents-detectormodel-sns-targetarn
            '''
            result = self._values.get("target_arn")
            assert result is not None, "Required property 'target_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def payload(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDetectorModel.PayloadProperty"]]:
            '''You can configure the action payload when you send a message as an Amazon SNS push notification.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-sns.html#cfn-iotevents-detectormodel-sns-payload
            '''
            result = self._values.get("payload")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDetectorModel.PayloadProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SnsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotevents.CfnDetectorModel.SqsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "queue_url": "queueUrl",
            "payload": "payload",
            "use_base64": "useBase64",
        },
    )
    class SqsProperty:
        def __init__(
            self,
            *,
            queue_url: builtins.str,
            payload: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDetectorModel.PayloadProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            use_base64: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Sends information about the detector model instance and the event that triggered the action to an Amazon SQS queue.

            :param queue_url: The URL of the SQS queue where the data is written.
            :param payload: You can configure the action payload when you send a message to an Amazon SQS queue.
            :param use_base64: Set this to TRUE if you want the data to be base-64 encoded before it is written to the queue. Otherwise, set this to FALSE.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-sqs.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotevents as iotevents
                
                sqs_property = iotevents.CfnDetectorModel.SqsProperty(
                    queue_url="queueUrl",
                
                    # the properties below are optional
                    payload=iotevents.CfnDetectorModel.PayloadProperty(
                        content_expression="contentExpression",
                        type="type"
                    ),
                    use_base64=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6d99d8d56a125c522bfc1a79d3629251230e200bc099c86c56a51ac5219b4ff4)
                check_type(argname="argument queue_url", value=queue_url, expected_type=type_hints["queue_url"])
                check_type(argname="argument payload", value=payload, expected_type=type_hints["payload"])
                check_type(argname="argument use_base64", value=use_base64, expected_type=type_hints["use_base64"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "queue_url": queue_url,
            }
            if payload is not None:
                self._values["payload"] = payload
            if use_base64 is not None:
                self._values["use_base64"] = use_base64

        @builtins.property
        def queue_url(self) -> builtins.str:
            '''The URL of the SQS queue where the data is written.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-sqs.html#cfn-iotevents-detectormodel-sqs-queueurl
            '''
            result = self._values.get("queue_url")
            assert result is not None, "Required property 'queue_url' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def payload(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDetectorModel.PayloadProperty"]]:
            '''You can configure the action payload when you send a message to an Amazon SQS queue.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-sqs.html#cfn-iotevents-detectormodel-sqs-payload
            '''
            result = self._values.get("payload")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDetectorModel.PayloadProperty"]], result)

        @builtins.property
        def use_base64(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Set this to TRUE if you want the data to be base-64 encoded before it is written to the queue.

            Otherwise, set this to FALSE.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-sqs.html#cfn-iotevents-detectormodel-sqs-usebase64
            '''
            result = self._values.get("use_base64")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SqsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotevents.CfnDetectorModel.StateProperty",
        jsii_struct_bases=[],
        name_mapping={
            "state_name": "stateName",
            "on_enter": "onEnter",
            "on_exit": "onExit",
            "on_input": "onInput",
        },
    )
    class StateProperty:
        def __init__(
            self,
            *,
            state_name: builtins.str,
            on_enter: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDetectorModel.OnEnterProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            on_exit: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDetectorModel.OnExitProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            on_input: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDetectorModel.OnInputProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Information that defines a state of a detector.

            :param state_name: The name of the state.
            :param on_enter: When entering this state, perform these ``actions`` if the ``condition`` is TRUE.
            :param on_exit: When exiting this state, perform these ``actions`` if the specified ``condition`` is ``TRUE`` .
            :param on_input: When an input is received and the ``condition`` is TRUE, perform the specified ``actions`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-state.html
            :exampleMetadata: fixture=_generated

            Example::

                
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e95f4745aae8049002469bd2d803c325a39aa9f4f8160aa8060d1cc217b9e015)
                check_type(argname="argument state_name", value=state_name, expected_type=type_hints["state_name"])
                check_type(argname="argument on_enter", value=on_enter, expected_type=type_hints["on_enter"])
                check_type(argname="argument on_exit", value=on_exit, expected_type=type_hints["on_exit"])
                check_type(argname="argument on_input", value=on_input, expected_type=type_hints["on_input"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "state_name": state_name,
            }
            if on_enter is not None:
                self._values["on_enter"] = on_enter
            if on_exit is not None:
                self._values["on_exit"] = on_exit
            if on_input is not None:
                self._values["on_input"] = on_input

        @builtins.property
        def state_name(self) -> builtins.str:
            '''The name of the state.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-state.html#cfn-iotevents-detectormodel-state-statename
            '''
            result = self._values.get("state_name")
            assert result is not None, "Required property 'state_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def on_enter(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDetectorModel.OnEnterProperty"]]:
            '''When entering this state, perform these ``actions`` if the ``condition`` is TRUE.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-state.html#cfn-iotevents-detectormodel-state-onenter
            '''
            result = self._values.get("on_enter")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDetectorModel.OnEnterProperty"]], result)

        @builtins.property
        def on_exit(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDetectorModel.OnExitProperty"]]:
            '''When exiting this state, perform these ``actions`` if the specified ``condition`` is ``TRUE`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-state.html#cfn-iotevents-detectormodel-state-onexit
            '''
            result = self._values.get("on_exit")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDetectorModel.OnExitProperty"]], result)

        @builtins.property
        def on_input(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDetectorModel.OnInputProperty"]]:
            '''When an input is received and the ``condition`` is TRUE, perform the specified ``actions`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-state.html#cfn-iotevents-detectormodel-state-oninput
            '''
            result = self._values.get("on_input")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDetectorModel.OnInputProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotevents.CfnDetectorModel.TransitionEventProperty",
        jsii_struct_bases=[],
        name_mapping={
            "condition": "condition",
            "event_name": "eventName",
            "next_state": "nextState",
            "actions": "actions",
        },
    )
    class TransitionEventProperty:
        def __init__(
            self,
            *,
            condition: builtins.str,
            event_name: builtins.str,
            next_state: builtins.str,
            actions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDetectorModel.ActionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Specifies the actions performed and the next state entered when a ``condition`` evaluates to TRUE.

            :param condition: Required. A Boolean expression that when TRUE causes the actions to be performed and the ``nextState`` to be entered.
            :param event_name: The name of the transition event.
            :param next_state: The next state to enter.
            :param actions: The actions to be performed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-transitionevent.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotevents as iotevents
                
                transition_event_property = iotevents.CfnDetectorModel.TransitionEventProperty(
                    condition="condition",
                    event_name="eventName",
                    next_state="nextState",
                
                    # the properties below are optional
                    actions=[iotevents.CfnDetectorModel.ActionProperty(
                        clear_timer=iotevents.CfnDetectorModel.ClearTimerProperty(
                            timer_name="timerName"
                        ),
                        dynamo_db=iotevents.CfnDetectorModel.DynamoDBProperty(
                            hash_key_field="hashKeyField",
                            hash_key_value="hashKeyValue",
                            table_name="tableName",
                
                            # the properties below are optional
                            hash_key_type="hashKeyType",
                            operation="operation",
                            payload=iotevents.CfnDetectorModel.PayloadProperty(
                                content_expression="contentExpression",
                                type="type"
                            ),
                            payload_field="payloadField",
                            range_key_field="rangeKeyField",
                            range_key_type="rangeKeyType",
                            range_key_value="rangeKeyValue"
                        ),
                        dynamo_dBv2=iotevents.CfnDetectorModel.DynamoDBv2Property(
                            table_name="tableName",
                
                            # the properties below are optional
                            payload=iotevents.CfnDetectorModel.PayloadProperty(
                                content_expression="contentExpression",
                                type="type"
                            )
                        ),
                        firehose=iotevents.CfnDetectorModel.FirehoseProperty(
                            delivery_stream_name="deliveryStreamName",
                
                            # the properties below are optional
                            payload=iotevents.CfnDetectorModel.PayloadProperty(
                                content_expression="contentExpression",
                                type="type"
                            ),
                            separator="separator"
                        ),
                        iot_events=iotevents.CfnDetectorModel.IotEventsProperty(
                            input_name="inputName",
                
                            # the properties below are optional
                            payload=iotevents.CfnDetectorModel.PayloadProperty(
                                content_expression="contentExpression",
                                type="type"
                            )
                        ),
                        iot_site_wise=iotevents.CfnDetectorModel.IotSiteWiseProperty(
                            property_value=iotevents.CfnDetectorModel.AssetPropertyValueProperty(
                                value=iotevents.CfnDetectorModel.AssetPropertyVariantProperty(
                                    boolean_value="booleanValue",
                                    double_value="doubleValue",
                                    integer_value="integerValue",
                                    string_value="stringValue"
                                ),
                
                                # the properties below are optional
                                quality="quality",
                                timestamp=iotevents.CfnDetectorModel.AssetPropertyTimestampProperty(
                                    time_in_seconds="timeInSeconds",
                
                                    # the properties below are optional
                                    offset_in_nanos="offsetInNanos"
                                )
                            ),
                
                            # the properties below are optional
                            asset_id="assetId",
                            entry_id="entryId",
                            property_alias="propertyAlias",
                            property_id="propertyId"
                        ),
                        iot_topic_publish=iotevents.CfnDetectorModel.IotTopicPublishProperty(
                            mqtt_topic="mqttTopic",
                
                            # the properties below are optional
                            payload=iotevents.CfnDetectorModel.PayloadProperty(
                                content_expression="contentExpression",
                                type="type"
                            )
                        ),
                        lambda_=iotevents.CfnDetectorModel.LambdaProperty(
                            function_arn="functionArn",
                
                            # the properties below are optional
                            payload=iotevents.CfnDetectorModel.PayloadProperty(
                                content_expression="contentExpression",
                                type="type"
                            )
                        ),
                        reset_timer=iotevents.CfnDetectorModel.ResetTimerProperty(
                            timer_name="timerName"
                        ),
                        set_timer=iotevents.CfnDetectorModel.SetTimerProperty(
                            timer_name="timerName",
                
                            # the properties below are optional
                            duration_expression="durationExpression",
                            seconds=123
                        ),
                        set_variable=iotevents.CfnDetectorModel.SetVariableProperty(
                            value="value",
                            variable_name="variableName"
                        ),
                        sns=iotevents.CfnDetectorModel.SnsProperty(
                            target_arn="targetArn",
                
                            # the properties below are optional
                            payload=iotevents.CfnDetectorModel.PayloadProperty(
                                content_expression="contentExpression",
                                type="type"
                            )
                        ),
                        sqs=iotevents.CfnDetectorModel.SqsProperty(
                            queue_url="queueUrl",
                
                            # the properties below are optional
                            payload=iotevents.CfnDetectorModel.PayloadProperty(
                                content_expression="contentExpression",
                                type="type"
                            ),
                            use_base64=False
                        )
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__58cc9b74b1b13a3df88f86605e6204fc4e2bb97b6a508a626a96132e5e4073bb)
                check_type(argname="argument condition", value=condition, expected_type=type_hints["condition"])
                check_type(argname="argument event_name", value=event_name, expected_type=type_hints["event_name"])
                check_type(argname="argument next_state", value=next_state, expected_type=type_hints["next_state"])
                check_type(argname="argument actions", value=actions, expected_type=type_hints["actions"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "condition": condition,
                "event_name": event_name,
                "next_state": next_state,
            }
            if actions is not None:
                self._values["actions"] = actions

        @builtins.property
        def condition(self) -> builtins.str:
            '''Required.

            A Boolean expression that when TRUE causes the actions to be performed and the ``nextState`` to be entered.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-transitionevent.html#cfn-iotevents-detectormodel-transitionevent-condition
            '''
            result = self._values.get("condition")
            assert result is not None, "Required property 'condition' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def event_name(self) -> builtins.str:
            '''The name of the transition event.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-transitionevent.html#cfn-iotevents-detectormodel-transitionevent-eventname
            '''
            result = self._values.get("event_name")
            assert result is not None, "Required property 'event_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def next_state(self) -> builtins.str:
            '''The next state to enter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-transitionevent.html#cfn-iotevents-detectormodel-transitionevent-nextstate
            '''
            result = self._values.get("next_state")
            assert result is not None, "Required property 'next_state' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def actions(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDetectorModel.ActionProperty"]]]]:
            '''The actions to be performed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-transitionevent.html#cfn-iotevents-detectormodel-transitionevent-actions
            '''
            result = self._values.get("actions")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDetectorModel.ActionProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TransitionEventProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iotevents.CfnDetectorModelProps",
    jsii_struct_bases=[],
    name_mapping={
        "detector_model_definition": "detectorModelDefinition",
        "role_arn": "roleArn",
        "detector_model_description": "detectorModelDescription",
        "detector_model_name": "detectorModelName",
        "evaluation_method": "evaluationMethod",
        "key": "key",
        "tags": "tags",
    },
)
class CfnDetectorModelProps:
    def __init__(
        self,
        *,
        detector_model_definition: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDetectorModel.DetectorModelDefinitionProperty, typing.Dict[builtins.str, typing.Any]]],
        role_arn: builtins.str,
        detector_model_description: typing.Optional[builtins.str] = None,
        detector_model_name: typing.Optional[builtins.str] = None,
        evaluation_method: typing.Optional[builtins.str] = None,
        key: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDetectorModel``.

        :param detector_model_definition: Information that defines how a detector operates.
        :param role_arn: The ARN of the role that grants permission to AWS IoT Events to perform its operations.
        :param detector_model_description: A brief description of the detector model.
        :param detector_model_name: The name of the detector model.
        :param evaluation_method: Information about the order in which events are evaluated and how actions are executed.
        :param key: The value used to identify a detector instance. When a device or system sends input, a new detector instance with a unique key value is created. AWS IoT Events can continue to route input to its corresponding detector instance based on this identifying information. This parameter uses a JSON-path expression to select the attribute-value pair in the message payload that is used for identification. To route the message to the correct detector instance, the device must send a message payload that contains the same attribute-value.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-detectormodel.html
        :exampleMetadata: fixture=_generated

        Example::

            
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e2611711600761b56c5b9240bfddb7ec561f2c659e9c9866ca3e31a313119eb)
            check_type(argname="argument detector_model_definition", value=detector_model_definition, expected_type=type_hints["detector_model_definition"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument detector_model_description", value=detector_model_description, expected_type=type_hints["detector_model_description"])
            check_type(argname="argument detector_model_name", value=detector_model_name, expected_type=type_hints["detector_model_name"])
            check_type(argname="argument evaluation_method", value=evaluation_method, expected_type=type_hints["evaluation_method"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "detector_model_definition": detector_model_definition,
            "role_arn": role_arn,
        }
        if detector_model_description is not None:
            self._values["detector_model_description"] = detector_model_description
        if detector_model_name is not None:
            self._values["detector_model_name"] = detector_model_name
        if evaluation_method is not None:
            self._values["evaluation_method"] = evaluation_method
        if key is not None:
            self._values["key"] = key
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def detector_model_definition(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnDetectorModel.DetectorModelDefinitionProperty]:
        '''Information that defines how a detector operates.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-detectormodel.html#cfn-iotevents-detectormodel-detectormodeldefinition
        '''
        result = self._values.get("detector_model_definition")
        assert result is not None, "Required property 'detector_model_definition' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnDetectorModel.DetectorModelDefinitionProperty], result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''The ARN of the role that grants permission to AWS IoT Events to perform its operations.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-detectormodel.html#cfn-iotevents-detectormodel-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def detector_model_description(self) -> typing.Optional[builtins.str]:
        '''A brief description of the detector model.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-detectormodel.html#cfn-iotevents-detectormodel-detectormodeldescription
        '''
        result = self._values.get("detector_model_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def detector_model_name(self) -> typing.Optional[builtins.str]:
        '''The name of the detector model.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-detectormodel.html#cfn-iotevents-detectormodel-detectormodelname
        '''
        result = self._values.get("detector_model_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def evaluation_method(self) -> typing.Optional[builtins.str]:
        '''Information about the order in which events are evaluated and how actions are executed.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-detectormodel.html#cfn-iotevents-detectormodel-evaluationmethod
        '''
        result = self._values.get("evaluation_method")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''The value used to identify a detector instance.

        When a device or system sends input, a new detector instance with a unique key value is created. AWS IoT Events can continue to route input to its corresponding detector instance based on this identifying information.

        This parameter uses a JSON-path expression to select the attribute-value pair in the message payload that is used for identification. To route the message to the correct detector instance, the device must send a message payload that contains the same attribute-value.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-detectormodel.html#cfn-iotevents-detectormodel-key
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-detectormodel.html#cfn-iotevents-detectormodel-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDetectorModelProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnInput(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iotevents.CfnInput",
):
    '''The AWS::IoTEvents::Input resource creates an input.

    To monitor your devices and processes, they must have a way to get telemetry data into AWS IoT Events . This is done by sending messages as *inputs* to AWS IoT Events . For more information, see `How to Use AWS IoT Events <https://docs.aws.amazon.com/iotevents/latest/developerguide/how-to-use-iotevents.html>`_ in the *AWS IoT Events Developer Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-input.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iotevents as iotevents
        
        cfn_input = iotevents.CfnInput(self, "MyCfnInput",
            input_definition=iotevents.CfnInput.InputDefinitionProperty(
                attributes=[iotevents.CfnInput.AttributeProperty(
                    json_path="jsonPath"
                )]
            ),
        
            # the properties below are optional
            input_description="inputDescription",
            input_name="inputName",
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
        input_definition: typing.Union[_IResolvable_da3f097b, typing.Union["CfnInput.InputDefinitionProperty", typing.Dict[builtins.str, typing.Any]]],
        input_description: typing.Optional[builtins.str] = None,
        input_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param input_definition: The definition of the input.
        :param input_description: A brief description of the input.
        :param input_name: The name of the input.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11855be4f7bee53ad741f6363d8e68467f417b7f7483fc55460da1fe97129c79)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnInputProps(
            input_definition=input_definition,
            input_description=input_description,
            input_name=input_name,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02f974c7c08e022c5245f053e877e1dcb9db302c7bcb12e452bb07d8fd18b87c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b3260b920a311b7661b2d786c09cfeb4063947acd45edd5e41213dfde768c5e6)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

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
    @jsii.member(jsii_name="inputDefinition")
    def input_definition(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnInput.InputDefinitionProperty"]:
        '''The definition of the input.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnInput.InputDefinitionProperty"], jsii.get(self, "inputDefinition"))

    @input_definition.setter
    def input_definition(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnInput.InputDefinitionProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0004ecf75c5e3b12b061a20c9d32313a59f1da49257f0b4e64ef4078d1319f24)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "inputDefinition", value)

    @builtins.property
    @jsii.member(jsii_name="inputDescription")
    def input_description(self) -> typing.Optional[builtins.str]:
        '''A brief description of the input.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "inputDescription"))

    @input_description.setter
    def input_description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__672cf73a96fd163fb0565663222ff047175ff027f69faa2f36c053476d838b46)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "inputDescription", value)

    @builtins.property
    @jsii.member(jsii_name="inputName")
    def input_name(self) -> typing.Optional[builtins.str]:
        '''The name of the input.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "inputName"))

    @input_name.setter
    def input_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35c7cf9f1b2f6085acdb0b2064761cbaa054e480db69e5e48683595307b7dd11)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "inputName", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3cccadfdb4d8f7d42a3fa7d77dc4ad38b0292efb2ca6816bf878c1321670ceed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotevents.CfnInput.AttributeProperty",
        jsii_struct_bases=[],
        name_mapping={"json_path": "jsonPath"},
    )
    class AttributeProperty:
        def __init__(self, *, json_path: builtins.str) -> None:
            '''The attributes from the JSON payload that are made available by the input.

            Inputs are derived from messages sent to the AWS IoT Events system using ``BatchPutMessage`` . Each such message contains a JSON payload. Those attributes (and their paired values) specified here are available for use in the ``condition`` expressions used by detectors.

            :param json_path: An expression that specifies an attribute-value pair in a JSON structure. Use this to specify an attribute from the JSON payload that is made available by the input. Inputs are derived from messages sent to AWS IoT Events ( ``BatchPutMessage`` ). Each such message contains a JSON payload. The attribute (and its paired value) specified here are available for use in the ``condition`` expressions used by detectors. Syntax: ``<field-name>.<field-name>...``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-input-attribute.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotevents as iotevents
                
                attribute_property = iotevents.CfnInput.AttributeProperty(
                    json_path="jsonPath"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__797d37c850d2f5c2b3a62f58db5353f1f51e8c258592e33a5b8dd7a4b673ed20)
                check_type(argname="argument json_path", value=json_path, expected_type=type_hints["json_path"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "json_path": json_path,
            }

        @builtins.property
        def json_path(self) -> builtins.str:
            '''An expression that specifies an attribute-value pair in a JSON structure.

            Use this to specify an attribute from the JSON payload that is made available by the input. Inputs are derived from messages sent to AWS IoT Events ( ``BatchPutMessage`` ). Each such message contains a JSON payload. The attribute (and its paired value) specified here are available for use in the ``condition`` expressions used by detectors.

            Syntax: ``<field-name>.<field-name>...``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-input-attribute.html#cfn-iotevents-input-attribute-jsonpath
            '''
            result = self._values.get("json_path")
            assert result is not None, "Required property 'json_path' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AttributeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotevents.CfnInput.InputDefinitionProperty",
        jsii_struct_bases=[],
        name_mapping={"attributes": "attributes"},
    )
    class InputDefinitionProperty:
        def __init__(
            self,
            *,
            attributes: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInput.AttributeProperty", typing.Dict[builtins.str, typing.Any]]]]],
        ) -> None:
            '''The definition of the input.

            :param attributes: The attributes from the JSON payload that are made available by the input. Inputs are derived from messages sent to the AWS IoT Events system using ``BatchPutMessage`` . Each such message contains a JSON payload, and those attributes (and their paired values) specified here are available for use in the ``condition`` expressions used by detectors that monitor this input.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-input-inputdefinition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotevents as iotevents
                
                input_definition_property = iotevents.CfnInput.InputDefinitionProperty(
                    attributes=[iotevents.CfnInput.AttributeProperty(
                        json_path="jsonPath"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f28aaf2329f3541c2ea510b4c542b475eeb9d677b36275d8bffa1b5c43d44b5d)
                check_type(argname="argument attributes", value=attributes, expected_type=type_hints["attributes"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "attributes": attributes,
            }

        @builtins.property
        def attributes(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInput.AttributeProperty"]]]:
            '''The attributes from the JSON payload that are made available by the input.

            Inputs are derived from messages sent to the AWS IoT Events system using ``BatchPutMessage`` . Each such message contains a JSON payload, and those attributes (and their paired values) specified here are available for use in the ``condition`` expressions used by detectors that monitor this input.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-input-inputdefinition.html#cfn-iotevents-input-inputdefinition-attributes
            '''
            result = self._values.get("attributes")
            assert result is not None, "Required property 'attributes' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInput.AttributeProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InputDefinitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iotevents.CfnInputProps",
    jsii_struct_bases=[],
    name_mapping={
        "input_definition": "inputDefinition",
        "input_description": "inputDescription",
        "input_name": "inputName",
        "tags": "tags",
    },
)
class CfnInputProps:
    def __init__(
        self,
        *,
        input_definition: typing.Union[_IResolvable_da3f097b, typing.Union[CfnInput.InputDefinitionProperty, typing.Dict[builtins.str, typing.Any]]],
        input_description: typing.Optional[builtins.str] = None,
        input_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnInput``.

        :param input_definition: The definition of the input.
        :param input_description: A brief description of the input.
        :param input_name: The name of the input.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-input.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iotevents as iotevents
            
            cfn_input_props = iotevents.CfnInputProps(
                input_definition=iotevents.CfnInput.InputDefinitionProperty(
                    attributes=[iotevents.CfnInput.AttributeProperty(
                        json_path="jsonPath"
                    )]
                ),
            
                # the properties below are optional
                input_description="inputDescription",
                input_name="inputName",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ece51581a45430852925100971ac147cf205a386827cd21b226948da1b2a722)
            check_type(argname="argument input_definition", value=input_definition, expected_type=type_hints["input_definition"])
            check_type(argname="argument input_description", value=input_description, expected_type=type_hints["input_description"])
            check_type(argname="argument input_name", value=input_name, expected_type=type_hints["input_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "input_definition": input_definition,
        }
        if input_description is not None:
            self._values["input_description"] = input_description
        if input_name is not None:
            self._values["input_name"] = input_name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def input_definition(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnInput.InputDefinitionProperty]:
        '''The definition of the input.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-input.html#cfn-iotevents-input-inputdefinition
        '''
        result = self._values.get("input_definition")
        assert result is not None, "Required property 'input_definition' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnInput.InputDefinitionProperty], result)

    @builtins.property
    def input_description(self) -> typing.Optional[builtins.str]:
        '''A brief description of the input.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-input.html#cfn-iotevents-input-inputdescription
        '''
        result = self._values.get("input_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def input_name(self) -> typing.Optional[builtins.str]:
        '''The name of the input.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-input.html#cfn-iotevents-input-inputname
        '''
        result = self._values.get("input_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-input.html#cfn-iotevents-input-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnInputProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnAlarmModel",
    "CfnAlarmModelProps",
    "CfnDetectorModel",
    "CfnDetectorModelProps",
    "CfnInput",
    "CfnInputProps",
]

publication.publish()

def _typecheckingstub__ef7f48b87ae58ab2d16bfb25fbcc61ae8753eb0c9a5b0016eec37a52e79b7a7d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    alarm_rule: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAlarmModel.AlarmRuleProperty, typing.Dict[builtins.str, typing.Any]]],
    role_arn: builtins.str,
    alarm_capabilities: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAlarmModel.AlarmCapabilitiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    alarm_event_actions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAlarmModel.AlarmEventActionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    alarm_model_description: typing.Optional[builtins.str] = None,
    alarm_model_name: typing.Optional[builtins.str] = None,
    key: typing.Optional[builtins.str] = None,
    severity: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29efb49b22ff313d9ee99306ea7ca4bf99648d4ec281ef880884544374a005e5(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05b98ff8d3be84f09516f43c45c6be0ea4a8c084c6b193e977f2739cd0e26d54(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36c0e05874a966c4cf11e13423d2cf0b8945f4dafb03af1bb65b04fe1f904e1c(
    value: typing.Union[_IResolvable_da3f097b, CfnAlarmModel.AlarmRuleProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__667c04eef9049300d49a54887f048621c4279fc765df4962bf383ab77e428d5c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d85be71c4d51b50fc44306a17518e6e2409c133128f31c26dcdf967abb3e0ec7(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAlarmModel.AlarmCapabilitiesProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8227f73f350bd144d86be0ccf98762b44508b027f4ffb7aef8e68eeaafd91ecd(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAlarmModel.AlarmEventActionsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b540895073c6ca51a688168fe27abe8c0bc5df06473c9a8e026f6b4a5c1881f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2520aa074d1ed7d38b09cd7416997eb16982c8c7dc7a4340e5fd1178569cc01a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f86ab353b386a192172ab818d729e6584ca5b5df31c6e550f1e7986ea1ce3026(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc04b5b9d376105aa5bf470e04873d2255ed6412dbf222f2dbc18a074c52ed49(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__877eb82e1ea1e65eaa71c65808ed46b8a70c4cbff438aa7f010439bd4b409dcb(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6cf300e297184ec092d4441ac920d284db156ae6cb1ff9f0dde90b454a739267(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab691bc61d6c876d3c04cfc2eaaae2a144273102c7fd7065a4db407ff0bac487(
    *,
    dynamo_db: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAlarmModel.DynamoDBProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    dynamo_d_bv2: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAlarmModel.DynamoDBv2Property, typing.Dict[builtins.str, typing.Any]]]] = None,
    firehose: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAlarmModel.FirehoseProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    iot_events: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAlarmModel.IotEventsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    iot_site_wise: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAlarmModel.IotSiteWiseProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    iot_topic_publish: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAlarmModel.IotTopicPublishProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    lambda_: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAlarmModel.LambdaProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sns: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAlarmModel.SnsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sqs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAlarmModel.SqsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8cfea2cb5d08826e83e6dc83754015780aeb22a1b8774e0f8e35b1d0931455b0(
    *,
    acknowledge_flow: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAlarmModel.AcknowledgeFlowProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    initialization_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAlarmModel.InitializationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6ca07dd10460007b069e0fb33a778c8623f821779a57a99e1b7583f9708fb0b(
    *,
    alarm_actions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAlarmModel.AlarmActionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ecdb897257f52e6f2dc0b5e8aa04adf9936f47ba53e3a04c2de77b97b3007a0e(
    *,
    simple_rule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAlarmModel.SimpleRuleProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0faa4e9328819a8804a815994faf7d70d0f09054014c6e47dd3b002c546003d(
    *,
    time_in_seconds: builtins.str,
    offset_in_nanos: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__708234624899e9edfd2c801c216045db009dc0332806973b92a2972970d186a8(
    *,
    value: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAlarmModel.AssetPropertyVariantProperty, typing.Dict[builtins.str, typing.Any]]],
    quality: typing.Optional[builtins.str] = None,
    timestamp: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAlarmModel.AssetPropertyTimestampProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4caad62d2d9efb76f9ed85eeb63e97b3d0a85ede80a6e1541ef55198968a2ed3(
    *,
    boolean_value: typing.Optional[builtins.str] = None,
    double_value: typing.Optional[builtins.str] = None,
    integer_value: typing.Optional[builtins.str] = None,
    string_value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5817f24cc0ee11012a378de58760f08626fd63cf7b576191502d7ed8d10b2ddf(
    *,
    hash_key_field: builtins.str,
    hash_key_value: builtins.str,
    table_name: builtins.str,
    hash_key_type: typing.Optional[builtins.str] = None,
    operation: typing.Optional[builtins.str] = None,
    payload: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAlarmModel.PayloadProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    payload_field: typing.Optional[builtins.str] = None,
    range_key_field: typing.Optional[builtins.str] = None,
    range_key_type: typing.Optional[builtins.str] = None,
    range_key_value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__991f55661aeeabe2f112b3b55306f540afbaca55eac19af02f6046a1039bf0a0(
    *,
    table_name: builtins.str,
    payload: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAlarmModel.PayloadProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6aaead57fb4199647f0274fe275fcc660e36d121f8abbc3801a7154bd92c0923(
    *,
    delivery_stream_name: builtins.str,
    payload: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAlarmModel.PayloadProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    separator: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f006a26469daccaeec8fbdc6b6b96590027aa831f6565f8f5bf0f295a81a2c95(
    *,
    disabled_on_initialization: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1159713658f7035984daf8d6dbfaf0175f9cab27b66825c395143c8befb7e719(
    *,
    input_name: builtins.str,
    payload: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAlarmModel.PayloadProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11694da853291108b198c9c98d58e346ab22cadc06b186dc6b980bb04d7751df(
    *,
    asset_id: typing.Optional[builtins.str] = None,
    entry_id: typing.Optional[builtins.str] = None,
    property_alias: typing.Optional[builtins.str] = None,
    property_id: typing.Optional[builtins.str] = None,
    property_value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAlarmModel.AssetPropertyValueProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd8797ce19f302d10090f97f9aa3b5045c89cb01d164ff9de6b87da2d7a6e25f(
    *,
    mqtt_topic: builtins.str,
    payload: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAlarmModel.PayloadProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a975c271127a1fe7c32f180fab5bb983fa81f890ee87d4cdd1dad0c6d4e60469(
    *,
    function_arn: builtins.str,
    payload: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAlarmModel.PayloadProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d18e90a4d474eeb87d607384857f4c582b60a985502109bd17120c0af558d368(
    *,
    content_expression: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90136387b310cc21ca49a113bb812022359fee99174291ce490e1b433ef6b419(
    *,
    comparison_operator: builtins.str,
    input_property: builtins.str,
    threshold: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce9abb929fe2014828de206b11bb74d7efb0ce4f363c5b1fe4df056896e7de68(
    *,
    target_arn: builtins.str,
    payload: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAlarmModel.PayloadProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f53bd000fd0e8e8506df9f9b2dcacf36f61e120354ff39131baa459b8dfef188(
    *,
    queue_url: builtins.str,
    payload: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAlarmModel.PayloadProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    use_base64: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20e728f3578307e805cd9079d426bae0a7ec729fb1c6704b7c6c04fd09cce9d8(
    *,
    alarm_rule: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAlarmModel.AlarmRuleProperty, typing.Dict[builtins.str, typing.Any]]],
    role_arn: builtins.str,
    alarm_capabilities: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAlarmModel.AlarmCapabilitiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    alarm_event_actions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAlarmModel.AlarmEventActionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    alarm_model_description: typing.Optional[builtins.str] = None,
    alarm_model_name: typing.Optional[builtins.str] = None,
    key: typing.Optional[builtins.str] = None,
    severity: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7801b6324e5f272a708fd3542c09e1cc61e7621f542ce11a4795b2717b8f7f3a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    detector_model_definition: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDetectorModel.DetectorModelDefinitionProperty, typing.Dict[builtins.str, typing.Any]]],
    role_arn: builtins.str,
    detector_model_description: typing.Optional[builtins.str] = None,
    detector_model_name: typing.Optional[builtins.str] = None,
    evaluation_method: typing.Optional[builtins.str] = None,
    key: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29f2e3393710755e327caeb1124191f98f1ffdfa48556729447af0457b842077(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9223278334ea0b572f1758d19c1e4bcc3469b9041fea558d47a8c0c09cdbf578(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63791e6db81942e4097ff9f1b03dce0b5618f92376af9187df3403f25fe75d85(
    value: typing.Union[_IResolvable_da3f097b, CfnDetectorModel.DetectorModelDefinitionProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea88e939b3cea49f4e92a8fa44670ef9976e22c5a0fb5fe78ac052fd14c5dab0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7eee7f26e62967552ad2a22246ac4aa020ed80878cef3e44ceb4849bba312eda(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4faf59137fbafe31260e949107d4c02fc4239abc15c840bc619336d54bf866e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb0b24d2480d69d447d4a28a886f18008b5a68a52c7e66b5764230e251def06d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d0b60cb750a8707e4533e77383c39c786579957920ad5474c000e7a4565e4f4(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0a32c9ce5c2628faeace1b70ec3577ac67b86fb20a6cdea89790127622b2feb(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__997f21492a6bca00169c7708a8d2827cc3198fda198345353c9092e56e7792c1(
    *,
    clear_timer: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDetectorModel.ClearTimerProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    dynamo_db: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDetectorModel.DynamoDBProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    dynamo_d_bv2: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDetectorModel.DynamoDBv2Property, typing.Dict[builtins.str, typing.Any]]]] = None,
    firehose: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDetectorModel.FirehoseProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    iot_events: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDetectorModel.IotEventsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    iot_site_wise: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDetectorModel.IotSiteWiseProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    iot_topic_publish: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDetectorModel.IotTopicPublishProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    lambda_: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDetectorModel.LambdaProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    reset_timer: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDetectorModel.ResetTimerProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    set_timer: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDetectorModel.SetTimerProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    set_variable: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDetectorModel.SetVariableProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sns: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDetectorModel.SnsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sqs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDetectorModel.SqsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d22f888073f939f0cd7ee06c54bc7d6cd951574ecee193dfed4f0e55492753e8(
    *,
    time_in_seconds: builtins.str,
    offset_in_nanos: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49e6195d5246f0fc1891e1c7b239860858968a5d4b50a8581dcfcb07f3c93068(
    *,
    value: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDetectorModel.AssetPropertyVariantProperty, typing.Dict[builtins.str, typing.Any]]],
    quality: typing.Optional[builtins.str] = None,
    timestamp: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDetectorModel.AssetPropertyTimestampProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8b56c1e6c67193acb9830ebc279e1835d5ff3fcd79e142ad47466b5a297929e(
    *,
    boolean_value: typing.Optional[builtins.str] = None,
    double_value: typing.Optional[builtins.str] = None,
    integer_value: typing.Optional[builtins.str] = None,
    string_value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7875bb21ca70e3332dc63f20cd6808a6f0476f0bc6e28fd0b03d0a058575500b(
    *,
    timer_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e1657c0e6d089d8b904914d9cdca2ff5841ab5284a6cbd6261e40e2c2fa9cb0(
    *,
    initial_state_name: builtins.str,
    states: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDetectorModel.StateProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f20bd32cd2bf50da45c673c93066de3531126c3c989ecc1c664070a98ae2fde(
    *,
    hash_key_field: builtins.str,
    hash_key_value: builtins.str,
    table_name: builtins.str,
    hash_key_type: typing.Optional[builtins.str] = None,
    operation: typing.Optional[builtins.str] = None,
    payload: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDetectorModel.PayloadProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    payload_field: typing.Optional[builtins.str] = None,
    range_key_field: typing.Optional[builtins.str] = None,
    range_key_type: typing.Optional[builtins.str] = None,
    range_key_value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce549d899ae554a89d320f79add62caba2098d6b98c681aa6ff7410626c6a145(
    *,
    table_name: builtins.str,
    payload: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDetectorModel.PayloadProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__717bd99991f8e8e6bcb7616faed1722ead70bd8378234a60048d02751c39bb8f(
    *,
    event_name: builtins.str,
    actions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDetectorModel.ActionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    condition: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff798f3ccc562e611abbd96aff8a343e927e8d0151d6debb2cdde0aa825102c5(
    *,
    delivery_stream_name: builtins.str,
    payload: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDetectorModel.PayloadProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    separator: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39ebee23e3171868800d30327b2934e00faad4113cfed4549950bece31b8156b(
    *,
    input_name: builtins.str,
    payload: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDetectorModel.PayloadProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__297b1140450b226c15a66b0e140cd227d66d7d0506dd90d971a67e98e9a1da19(
    *,
    property_value: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDetectorModel.AssetPropertyValueProperty, typing.Dict[builtins.str, typing.Any]]],
    asset_id: typing.Optional[builtins.str] = None,
    entry_id: typing.Optional[builtins.str] = None,
    property_alias: typing.Optional[builtins.str] = None,
    property_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9a560fbb56587b6f32e68c81fe2d3de4fde7ce4fb0967fd5f984981abf33e32(
    *,
    mqtt_topic: builtins.str,
    payload: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDetectorModel.PayloadProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24efb01bfc6091499688a9ae496c6a60549dc83dd01e864646eaf8bf7add6359(
    *,
    function_arn: builtins.str,
    payload: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDetectorModel.PayloadProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aea0f4e8f57882389b42e8f7fa9e7bbe91614a1ae3730ce67ca2fbb72ca564a4(
    *,
    events: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDetectorModel.EventProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16290de6f98bd9f79c314df78ddd48700ce8ae4aeab4507ec4086fd6db4afb4e(
    *,
    events: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDetectorModel.EventProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b69ba177ba3a33e678e1629e61da95d0b56c6dbeb0deed847a52a5b6f265ecf9(
    *,
    events: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDetectorModel.EventProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    transition_events: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDetectorModel.TransitionEventProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2790fb31ad2046e675044abc890e4a9085c827804c7dd2da845e301a57019f18(
    *,
    content_expression: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfaaeea93082e9ba0d53049569b60b8aab40bba790a2912a29e4e02e1cad5bee(
    *,
    timer_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2d0222e1d4ee3749b41430abba08489b16cf1a6a208820083451b0c210a1d77(
    *,
    timer_name: builtins.str,
    duration_expression: typing.Optional[builtins.str] = None,
    seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f45edf8a7eb1797088c2f77a7e60ad9575cd7f0fc5b734c5a8bb4930902ab37b(
    *,
    value: builtins.str,
    variable_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa8303f7597b5d5f0f82a97b7668999b73c7153f44a25feadcc0c469f8fa3ab7(
    *,
    target_arn: builtins.str,
    payload: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDetectorModel.PayloadProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d99d8d56a125c522bfc1a79d3629251230e200bc099c86c56a51ac5219b4ff4(
    *,
    queue_url: builtins.str,
    payload: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDetectorModel.PayloadProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    use_base64: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e95f4745aae8049002469bd2d803c325a39aa9f4f8160aa8060d1cc217b9e015(
    *,
    state_name: builtins.str,
    on_enter: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDetectorModel.OnEnterProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    on_exit: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDetectorModel.OnExitProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    on_input: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDetectorModel.OnInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58cc9b74b1b13a3df88f86605e6204fc4e2bb97b6a508a626a96132e5e4073bb(
    *,
    condition: builtins.str,
    event_name: builtins.str,
    next_state: builtins.str,
    actions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDetectorModel.ActionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e2611711600761b56c5b9240bfddb7ec561f2c659e9c9866ca3e31a313119eb(
    *,
    detector_model_definition: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDetectorModel.DetectorModelDefinitionProperty, typing.Dict[builtins.str, typing.Any]]],
    role_arn: builtins.str,
    detector_model_description: typing.Optional[builtins.str] = None,
    detector_model_name: typing.Optional[builtins.str] = None,
    evaluation_method: typing.Optional[builtins.str] = None,
    key: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11855be4f7bee53ad741f6363d8e68467f417b7f7483fc55460da1fe97129c79(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    input_definition: typing.Union[_IResolvable_da3f097b, typing.Union[CfnInput.InputDefinitionProperty, typing.Dict[builtins.str, typing.Any]]],
    input_description: typing.Optional[builtins.str] = None,
    input_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02f974c7c08e022c5245f053e877e1dcb9db302c7bcb12e452bb07d8fd18b87c(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3260b920a311b7661b2d786c09cfeb4063947acd45edd5e41213dfde768c5e6(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0004ecf75c5e3b12b061a20c9d32313a59f1da49257f0b4e64ef4078d1319f24(
    value: typing.Union[_IResolvable_da3f097b, CfnInput.InputDefinitionProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__672cf73a96fd163fb0565663222ff047175ff027f69faa2f36c053476d838b46(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35c7cf9f1b2f6085acdb0b2064761cbaa054e480db69e5e48683595307b7dd11(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3cccadfdb4d8f7d42a3fa7d77dc4ad38b0292efb2ca6816bf878c1321670ceed(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__797d37c850d2f5c2b3a62f58db5353f1f51e8c258592e33a5b8dd7a4b673ed20(
    *,
    json_path: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f28aaf2329f3541c2ea510b4c542b475eeb9d677b36275d8bffa1b5c43d44b5d(
    *,
    attributes: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInput.AttributeProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ece51581a45430852925100971ac147cf205a386827cd21b226948da1b2a722(
    *,
    input_definition: typing.Union[_IResolvable_da3f097b, typing.Union[CfnInput.InputDefinitionProperty, typing.Dict[builtins.str, typing.Any]]],
    input_description: typing.Optional[builtins.str] = None,
    input_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
