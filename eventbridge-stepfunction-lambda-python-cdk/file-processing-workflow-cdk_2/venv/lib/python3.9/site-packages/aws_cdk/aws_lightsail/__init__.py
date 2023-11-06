'''
# AWS::Lightsail Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_lightsail as lightsail
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for Lightsail construct libraries](https://constructs.dev/search?q=lightsail)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::Lightsail resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Lightsail.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::Lightsail](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Lightsail.html).

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
class CfnAlarm(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_lightsail.CfnAlarm",
):
    '''The ``AWS::Lightsail::Alarm`` resource specifies an alarm that can be used to monitor a single metric for one of your Lightsail resources.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-alarm.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_lightsail as lightsail
        
        cfn_alarm = lightsail.CfnAlarm(self, "MyCfnAlarm",
            alarm_name="alarmName",
            comparison_operator="comparisonOperator",
            evaluation_periods=123,
            metric_name="metricName",
            monitored_resource_name="monitoredResourceName",
            threshold=123,
        
            # the properties below are optional
            contact_protocols=["contactProtocols"],
            datapoints_to_alarm=123,
            notification_enabled=False,
            notification_triggers=["notificationTriggers"],
            treat_missing_data="treatMissingData"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        alarm_name: builtins.str,
        comparison_operator: builtins.str,
        evaluation_periods: jsii.Number,
        metric_name: builtins.str,
        monitored_resource_name: builtins.str,
        threshold: jsii.Number,
        contact_protocols: typing.Optional[typing.Sequence[builtins.str]] = None,
        datapoints_to_alarm: typing.Optional[jsii.Number] = None,
        notification_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        notification_triggers: typing.Optional[typing.Sequence[builtins.str]] = None,
        treat_missing_data: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param alarm_name: The name of the alarm.
        :param comparison_operator: The arithmetic operation to use when comparing the specified statistic and threshold.
        :param evaluation_periods: The number of periods over which data is compared to the specified threshold.
        :param metric_name: The name of the metric associated with the alarm.
        :param monitored_resource_name: The name of the Lightsail resource that the alarm monitors.
        :param threshold: The value against which the specified statistic is compared.
        :param contact_protocols: The contact protocols for the alarm, such as ``Email`` , ``SMS`` (text messaging), or both. *Allowed Values* : ``Email`` | ``SMS``
        :param datapoints_to_alarm: The number of data points within the evaluation periods that must be breaching to cause the alarm to go to the ``ALARM`` state.
        :param notification_enabled: A Boolean value indicating whether the alarm is enabled.
        :param notification_triggers: The alarm states that trigger a notification. .. epigraph:: To specify the ``OK`` and ``INSUFFICIENT_DATA`` values, you must also specify ``ContactProtocols`` values. Otherwise, the ``OK`` and ``INSUFFICIENT_DATA`` values will not take effect and the stack will drift. *Allowed Values* : ``OK`` | ``ALARM`` | ``INSUFFICIENT_DATA``
        :param treat_missing_data: Specifies how the alarm handles missing data points. An alarm can treat missing data in the following ways: - ``breaching`` - Assumes the missing data is not within the threshold. Missing data counts towards the number of times that the metric is not within the threshold. - ``notBreaching`` - Assumes the missing data is within the threshold. Missing data does not count towards the number of times that the metric is not within the threshold. - ``ignore`` - Ignores the missing data. Maintains the current alarm state. - ``missing`` - Missing data is treated as missing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52a6d2c9652c1f935ede5b57250bb327a005cfd64bafaed966f96abbe167f1cb)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAlarmProps(
            alarm_name=alarm_name,
            comparison_operator=comparison_operator,
            evaluation_periods=evaluation_periods,
            metric_name=metric_name,
            monitored_resource_name=monitored_resource_name,
            threshold=threshold,
            contact_protocols=contact_protocols,
            datapoints_to_alarm=datapoints_to_alarm,
            notification_enabled=notification_enabled,
            notification_triggers=notification_triggers,
            treat_missing_data=treat_missing_data,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92cba21d204152e76e818434e3b1baf4a449ecb411f8200900c1e7cff19b2968)
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
            type_hints = typing.get_type_hints(_typecheckingstub__02ad248f7a5a406b284b19a230eb250e778357cb79afe022f86b954427facd41)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAlarmArn")
    def attr_alarm_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the alarm.

        :cloudformationAttribute: AlarmArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAlarmArn"))

    @builtins.property
    @jsii.member(jsii_name="attrState")
    def attr_state(self) -> builtins.str:
        '''The current state of the alarm.

        An alarm has the following possible states:

        - ``ALARM`` - The metric is outside of the defined threshold.
        - ``INSUFFICIENT_DATA`` - The alarm has recently started, the metric is not available, or not enough data is available for the metric to determine the alarm state.
        - ``OK`` - The metric is within the defined threshold.

        :cloudformationAttribute: State
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrState"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="alarmName")
    def alarm_name(self) -> builtins.str:
        '''The name of the alarm.'''
        return typing.cast(builtins.str, jsii.get(self, "alarmName"))

    @alarm_name.setter
    def alarm_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6cbef5a5341e55fa03b4be9a6a15a8717434d6fc08dc2002a6a455935ed61cca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alarmName", value)

    @builtins.property
    @jsii.member(jsii_name="comparisonOperator")
    def comparison_operator(self) -> builtins.str:
        '''The arithmetic operation to use when comparing the specified statistic and threshold.'''
        return typing.cast(builtins.str, jsii.get(self, "comparisonOperator"))

    @comparison_operator.setter
    def comparison_operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5f7bab333eda8f33f7cf02bfacceaed6eba1bce4cffab8c704a426a990a39bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "comparisonOperator", value)

    @builtins.property
    @jsii.member(jsii_name="evaluationPeriods")
    def evaluation_periods(self) -> jsii.Number:
        '''The number of periods over which data is compared to the specified threshold.'''
        return typing.cast(jsii.Number, jsii.get(self, "evaluationPeriods"))

    @evaluation_periods.setter
    def evaluation_periods(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dbca6c409a133a482c79d4f2d1d54d380635a6cd16f5659cddbbdca0113f00e2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "evaluationPeriods", value)

    @builtins.property
    @jsii.member(jsii_name="metricName")
    def metric_name(self) -> builtins.str:
        '''The name of the metric associated with the alarm.'''
        return typing.cast(builtins.str, jsii.get(self, "metricName"))

    @metric_name.setter
    def metric_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d56d786f28acdb2b750523f0f764b81b2dbe6c19989d8ad5d6637d38ef41dafd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricName", value)

    @builtins.property
    @jsii.member(jsii_name="monitoredResourceName")
    def monitored_resource_name(self) -> builtins.str:
        '''The name of the Lightsail resource that the alarm monitors.'''
        return typing.cast(builtins.str, jsii.get(self, "monitoredResourceName"))

    @monitored_resource_name.setter
    def monitored_resource_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bed67dce202ef59c6fc0482720e647da6d182a5eb7fc29bd7e33f7c493baeeba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "monitoredResourceName", value)

    @builtins.property
    @jsii.member(jsii_name="threshold")
    def threshold(self) -> jsii.Number:
        '''The value against which the specified statistic is compared.'''
        return typing.cast(jsii.Number, jsii.get(self, "threshold"))

    @threshold.setter
    def threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2207c45df0a7242a484a71d452e6078412a0174e16363bf59797c35aba03cf60)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "threshold", value)

    @builtins.property
    @jsii.member(jsii_name="contactProtocols")
    def contact_protocols(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The contact protocols for the alarm, such as ``Email`` , ``SMS`` (text messaging), or both.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "contactProtocols"))

    @contact_protocols.setter
    def contact_protocols(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e16e66db23d954d5c8b8f71b6a742f8d70605fd3ec588876e4cc4b066986fc5e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contactProtocols", value)

    @builtins.property
    @jsii.member(jsii_name="datapointsToAlarm")
    def datapoints_to_alarm(self) -> typing.Optional[jsii.Number]:
        '''The number of data points within the evaluation periods that must be breaching to cause the alarm to go to the ``ALARM`` state.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "datapointsToAlarm"))

    @datapoints_to_alarm.setter
    def datapoints_to_alarm(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0cf63524930194266731756c5d9e34ac56a21a835ccf654121b2eef068b86851)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datapointsToAlarm", value)

    @builtins.property
    @jsii.member(jsii_name="notificationEnabled")
    def notification_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''A Boolean value indicating whether the alarm is enabled.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "notificationEnabled"))

    @notification_enabled.setter
    def notification_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d1f7e50126b8dc4c73aad55d44ca47c64d1aaa42863a2071146240e12b7fff9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notificationEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="notificationTriggers")
    def notification_triggers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The alarm states that trigger a notification.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "notificationTriggers"))

    @notification_triggers.setter
    def notification_triggers(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a80d0edb78ff630c74b704ff1bb587d3767dde14ca85dfcc06b5a9fce0e6b51a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notificationTriggers", value)

    @builtins.property
    @jsii.member(jsii_name="treatMissingData")
    def treat_missing_data(self) -> typing.Optional[builtins.str]:
        '''Specifies how the alarm handles missing data points.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "treatMissingData"))

    @treat_missing_data.setter
    def treat_missing_data(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__288a8a660b0017ff51421053d89dc9a8f78e3031f9d00e3da7512b2927946c92)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "treatMissingData", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_lightsail.CfnAlarmProps",
    jsii_struct_bases=[],
    name_mapping={
        "alarm_name": "alarmName",
        "comparison_operator": "comparisonOperator",
        "evaluation_periods": "evaluationPeriods",
        "metric_name": "metricName",
        "monitored_resource_name": "monitoredResourceName",
        "threshold": "threshold",
        "contact_protocols": "contactProtocols",
        "datapoints_to_alarm": "datapointsToAlarm",
        "notification_enabled": "notificationEnabled",
        "notification_triggers": "notificationTriggers",
        "treat_missing_data": "treatMissingData",
    },
)
class CfnAlarmProps:
    def __init__(
        self,
        *,
        alarm_name: builtins.str,
        comparison_operator: builtins.str,
        evaluation_periods: jsii.Number,
        metric_name: builtins.str,
        monitored_resource_name: builtins.str,
        threshold: jsii.Number,
        contact_protocols: typing.Optional[typing.Sequence[builtins.str]] = None,
        datapoints_to_alarm: typing.Optional[jsii.Number] = None,
        notification_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        notification_triggers: typing.Optional[typing.Sequence[builtins.str]] = None,
        treat_missing_data: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnAlarm``.

        :param alarm_name: The name of the alarm.
        :param comparison_operator: The arithmetic operation to use when comparing the specified statistic and threshold.
        :param evaluation_periods: The number of periods over which data is compared to the specified threshold.
        :param metric_name: The name of the metric associated with the alarm.
        :param monitored_resource_name: The name of the Lightsail resource that the alarm monitors.
        :param threshold: The value against which the specified statistic is compared.
        :param contact_protocols: The contact protocols for the alarm, such as ``Email`` , ``SMS`` (text messaging), or both. *Allowed Values* : ``Email`` | ``SMS``
        :param datapoints_to_alarm: The number of data points within the evaluation periods that must be breaching to cause the alarm to go to the ``ALARM`` state.
        :param notification_enabled: A Boolean value indicating whether the alarm is enabled.
        :param notification_triggers: The alarm states that trigger a notification. .. epigraph:: To specify the ``OK`` and ``INSUFFICIENT_DATA`` values, you must also specify ``ContactProtocols`` values. Otherwise, the ``OK`` and ``INSUFFICIENT_DATA`` values will not take effect and the stack will drift. *Allowed Values* : ``OK`` | ``ALARM`` | ``INSUFFICIENT_DATA``
        :param treat_missing_data: Specifies how the alarm handles missing data points. An alarm can treat missing data in the following ways: - ``breaching`` - Assumes the missing data is not within the threshold. Missing data counts towards the number of times that the metric is not within the threshold. - ``notBreaching`` - Assumes the missing data is within the threshold. Missing data does not count towards the number of times that the metric is not within the threshold. - ``ignore`` - Ignores the missing data. Maintains the current alarm state. - ``missing`` - Missing data is treated as missing.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-alarm.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_lightsail as lightsail
            
            cfn_alarm_props = lightsail.CfnAlarmProps(
                alarm_name="alarmName",
                comparison_operator="comparisonOperator",
                evaluation_periods=123,
                metric_name="metricName",
                monitored_resource_name="monitoredResourceName",
                threshold=123,
            
                # the properties below are optional
                contact_protocols=["contactProtocols"],
                datapoints_to_alarm=123,
                notification_enabled=False,
                notification_triggers=["notificationTriggers"],
                treat_missing_data="treatMissingData"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8d2af6c4e2ba837e14d1d99b9e23f273f3d750b635d2750e4f758a49c1b5349)
            check_type(argname="argument alarm_name", value=alarm_name, expected_type=type_hints["alarm_name"])
            check_type(argname="argument comparison_operator", value=comparison_operator, expected_type=type_hints["comparison_operator"])
            check_type(argname="argument evaluation_periods", value=evaluation_periods, expected_type=type_hints["evaluation_periods"])
            check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
            check_type(argname="argument monitored_resource_name", value=monitored_resource_name, expected_type=type_hints["monitored_resource_name"])
            check_type(argname="argument threshold", value=threshold, expected_type=type_hints["threshold"])
            check_type(argname="argument contact_protocols", value=contact_protocols, expected_type=type_hints["contact_protocols"])
            check_type(argname="argument datapoints_to_alarm", value=datapoints_to_alarm, expected_type=type_hints["datapoints_to_alarm"])
            check_type(argname="argument notification_enabled", value=notification_enabled, expected_type=type_hints["notification_enabled"])
            check_type(argname="argument notification_triggers", value=notification_triggers, expected_type=type_hints["notification_triggers"])
            check_type(argname="argument treat_missing_data", value=treat_missing_data, expected_type=type_hints["treat_missing_data"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "alarm_name": alarm_name,
            "comparison_operator": comparison_operator,
            "evaluation_periods": evaluation_periods,
            "metric_name": metric_name,
            "monitored_resource_name": monitored_resource_name,
            "threshold": threshold,
        }
        if contact_protocols is not None:
            self._values["contact_protocols"] = contact_protocols
        if datapoints_to_alarm is not None:
            self._values["datapoints_to_alarm"] = datapoints_to_alarm
        if notification_enabled is not None:
            self._values["notification_enabled"] = notification_enabled
        if notification_triggers is not None:
            self._values["notification_triggers"] = notification_triggers
        if treat_missing_data is not None:
            self._values["treat_missing_data"] = treat_missing_data

    @builtins.property
    def alarm_name(self) -> builtins.str:
        '''The name of the alarm.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-alarm.html#cfn-lightsail-alarm-alarmname
        '''
        result = self._values.get("alarm_name")
        assert result is not None, "Required property 'alarm_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def comparison_operator(self) -> builtins.str:
        '''The arithmetic operation to use when comparing the specified statistic and threshold.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-alarm.html#cfn-lightsail-alarm-comparisonoperator
        '''
        result = self._values.get("comparison_operator")
        assert result is not None, "Required property 'comparison_operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def evaluation_periods(self) -> jsii.Number:
        '''The number of periods over which data is compared to the specified threshold.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-alarm.html#cfn-lightsail-alarm-evaluationperiods
        '''
        result = self._values.get("evaluation_periods")
        assert result is not None, "Required property 'evaluation_periods' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def metric_name(self) -> builtins.str:
        '''The name of the metric associated with the alarm.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-alarm.html#cfn-lightsail-alarm-metricname
        '''
        result = self._values.get("metric_name")
        assert result is not None, "Required property 'metric_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def monitored_resource_name(self) -> builtins.str:
        '''The name of the Lightsail resource that the alarm monitors.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-alarm.html#cfn-lightsail-alarm-monitoredresourcename
        '''
        result = self._values.get("monitored_resource_name")
        assert result is not None, "Required property 'monitored_resource_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def threshold(self) -> jsii.Number:
        '''The value against which the specified statistic is compared.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-alarm.html#cfn-lightsail-alarm-threshold
        '''
        result = self._values.get("threshold")
        assert result is not None, "Required property 'threshold' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def contact_protocols(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The contact protocols for the alarm, such as ``Email`` , ``SMS`` (text messaging), or both.

        *Allowed Values* : ``Email`` | ``SMS``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-alarm.html#cfn-lightsail-alarm-contactprotocols
        '''
        result = self._values.get("contact_protocols")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def datapoints_to_alarm(self) -> typing.Optional[jsii.Number]:
        '''The number of data points within the evaluation periods that must be breaching to cause the alarm to go to the ``ALARM`` state.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-alarm.html#cfn-lightsail-alarm-datapointstoalarm
        '''
        result = self._values.get("datapoints_to_alarm")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def notification_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''A Boolean value indicating whether the alarm is enabled.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-alarm.html#cfn-lightsail-alarm-notificationenabled
        '''
        result = self._values.get("notification_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def notification_triggers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The alarm states that trigger a notification.

        .. epigraph::

           To specify the ``OK`` and ``INSUFFICIENT_DATA`` values, you must also specify ``ContactProtocols`` values. Otherwise, the ``OK`` and ``INSUFFICIENT_DATA`` values will not take effect and the stack will drift.

        *Allowed Values* : ``OK`` | ``ALARM`` | ``INSUFFICIENT_DATA``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-alarm.html#cfn-lightsail-alarm-notificationtriggers
        '''
        result = self._values.get("notification_triggers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def treat_missing_data(self) -> typing.Optional[builtins.str]:
        '''Specifies how the alarm handles missing data points.

        An alarm can treat missing data in the following ways:

        - ``breaching`` - Assumes the missing data is not within the threshold. Missing data counts towards the number of times that the metric is not within the threshold.
        - ``notBreaching`` - Assumes the missing data is within the threshold. Missing data does not count towards the number of times that the metric is not within the threshold.
        - ``ignore`` - Ignores the missing data. Maintains the current alarm state.
        - ``missing`` - Missing data is treated as missing.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-alarm.html#cfn-lightsail-alarm-treatmissingdata
        '''
        result = self._values.get("treat_missing_data")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAlarmProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnBucket(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_lightsail.CfnBucket",
):
    '''The ``AWS::Lightsail::Bucket`` resource specifies a bucket.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-bucket.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_lightsail as lightsail
        
        cfn_bucket = lightsail.CfnBucket(self, "MyCfnBucket",
            bucket_name="bucketName",
            bundle_id="bundleId",
        
            # the properties below are optional
            access_rules=lightsail.CfnBucket.AccessRulesProperty(
                allow_public_overrides=False,
                object_access="objectAccess"
            ),
            object_versioning=False,
            read_only_access_accounts=["readOnlyAccessAccounts"],
            resources_receiving_access=["resourcesReceivingAccess"],
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
        bucket_name: builtins.str,
        bundle_id: builtins.str,
        access_rules: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBucket.AccessRulesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        object_versioning: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        read_only_access_accounts: typing.Optional[typing.Sequence[builtins.str]] = None,
        resources_receiving_access: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param bucket_name: The name of the bucket.
        :param bundle_id: The bundle ID for the bucket (for example, ``small_1_0`` ). A bucket bundle specifies the monthly cost, storage space, and data transfer quota for a bucket.
        :param access_rules: An object that describes the access rules for the bucket.
        :param object_versioning: Indicates whether object versioning is enabled for the bucket. The following options can be configured: - ``Enabled`` - Object versioning is enabled. - ``Suspended`` - Object versioning was previously enabled but is currently suspended. Existing object versions are retained. - ``NeverEnabled`` - Object versioning has never been enabled.
        :param read_only_access_accounts: An array of AWS account IDs that have read-only access to the bucket.
        :param resources_receiving_access: An array of Lightsail instances that have access to the bucket.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ in the *AWS CloudFormation User Guide* . .. epigraph:: The ``Value`` of ``Tags`` is optional for Lightsail resources.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f94a4bda809634204637b79ee8727ab741bdbc1389aa69314a9dd6ac07ff80d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnBucketProps(
            bucket_name=bucket_name,
            bundle_id=bundle_id,
            access_rules=access_rules,
            object_versioning=object_versioning,
            read_only_access_accounts=read_only_access_accounts,
            resources_receiving_access=resources_receiving_access,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a55634856786112230a563acc6361f686fcc4372251819f23a60e0b7448a375)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d60747afd5cc92706d65ce7e109be47066c778315246768e80639025bb28b8a4)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAbleToUpdateBundle")
    def attr_able_to_update_bundle(self) -> _IResolvable_da3f097b:
        '''A Boolean value indicating whether the bundle that is currently applied to your distribution can be changed to another bundle.

        :cloudformationAttribute: AbleToUpdateBundle
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrAbleToUpdateBundle"))

    @builtins.property
    @jsii.member(jsii_name="attrBucketArn")
    def attr_bucket_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the bucket.

        :cloudformationAttribute: BucketArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrBucketArn"))

    @builtins.property
    @jsii.member(jsii_name="attrUrl")
    def attr_url(self) -> builtins.str:
        '''The URL of the bucket.

        :cloudformationAttribute: Url
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUrl"))

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
    @jsii.member(jsii_name="bucketName")
    def bucket_name(self) -> builtins.str:
        '''The name of the bucket.'''
        return typing.cast(builtins.str, jsii.get(self, "bucketName"))

    @bucket_name.setter
    def bucket_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__671ba368991f7894cc8ddfe61a9b72e7f6d4f964b0c1b7e3da859b6c5db6cd24)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketName", value)

    @builtins.property
    @jsii.member(jsii_name="bundleId")
    def bundle_id(self) -> builtins.str:
        '''The bundle ID for the bucket (for example, ``small_1_0`` ).'''
        return typing.cast(builtins.str, jsii.get(self, "bundleId"))

    @bundle_id.setter
    def bundle_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6d5cea1c49d3cd6bf89b2a808219992c0ebd27dac7ba487070e177c4603b093)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bundleId", value)

    @builtins.property
    @jsii.member(jsii_name="accessRules")
    def access_rules(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBucket.AccessRulesProperty"]]:
        '''An object that describes the access rules for the bucket.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBucket.AccessRulesProperty"]], jsii.get(self, "accessRules"))

    @access_rules.setter
    def access_rules(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBucket.AccessRulesProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__911a5ab074c6c9182d436d48523575a61c00e4566f9a555177936f1964f07641)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessRules", value)

    @builtins.property
    @jsii.member(jsii_name="objectVersioning")
    def object_versioning(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Indicates whether object versioning is enabled for the bucket.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "objectVersioning"))

    @object_versioning.setter
    def object_versioning(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6191661c271e19e8e8cac9d23703e7a3bcbba2dc5b15936dc4e3f080e7e234af)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "objectVersioning", value)

    @builtins.property
    @jsii.member(jsii_name="readOnlyAccessAccounts")
    def read_only_access_accounts(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of AWS account IDs that have read-only access to the bucket.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "readOnlyAccessAccounts"))

    @read_only_access_accounts.setter
    def read_only_access_accounts(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab9b5622907c27faf77ab0bb3b248846c9d3b055a5fe545e85f5d0221ad5d356)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnlyAccessAccounts", value)

    @builtins.property
    @jsii.member(jsii_name="resourcesReceivingAccess")
    def resources_receiving_access(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of Lightsail instances that have access to the bucket.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "resourcesReceivingAccess"))

    @resources_receiving_access.setter
    def resources_receiving_access(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c511e7332e65a7a04ff0fba1f48703451ea06cf1cd61fd70b6c99a1c016339b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourcesReceivingAccess", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52cc8a8b4e5b6b3a8d087b3ae8257283509372b0fe52e0e90dc9c520fd5f8e34)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lightsail.CfnBucket.AccessRulesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "allow_public_overrides": "allowPublicOverrides",
            "object_access": "objectAccess",
        },
    )
    class AccessRulesProperty:
        def __init__(
            self,
            *,
            allow_public_overrides: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            object_access: typing.Optional[builtins.str] = None,
        ) -> None:
            '''``AccessRules`` is a property of the `AWS::Lightsail::Bucket <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-bucket.html>`_ resource. It describes access rules for a bucket.

            :param allow_public_overrides: A Boolean value indicating whether the access control list (ACL) permissions that are applied to individual objects override the ``GetObject`` option that is currently specified. When this is true, you can use the `PutObjectAcl <https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectAcl.html>`_ Amazon S3 API operation to set individual objects to public (read-only) or private, using either the ``public-read`` ACL or the ``private`` ACL.
            :param object_access: Specifies the anonymous access to all objects in a bucket. The following options can be specified: - ``public`` - Sets all objects in the bucket to public (read-only), making them readable by everyone on the internet. If the ``GetObject`` value is set to ``public`` , then all objects in the bucket default to public regardless of the ``allowPublicOverrides`` value. - ``private`` - Sets all objects in the bucket to private, making them readable only by you and anyone that you grant access to. If the ``GetObject`` value is set to ``private`` , and the ``allowPublicOverrides`` value is set to ``true`` , then all objects in the bucket default to private unless they are configured with a ``public-read`` ACL. Individual objects with a ``public-read`` ACL are readable by everyone on the internet.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-bucket-accessrules.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lightsail as lightsail
                
                access_rules_property = lightsail.CfnBucket.AccessRulesProperty(
                    allow_public_overrides=False,
                    object_access="objectAccess"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__120388e897900c963efef1f8bbf42a875d5673e23401f7d348c6c432975d91b5)
                check_type(argname="argument allow_public_overrides", value=allow_public_overrides, expected_type=type_hints["allow_public_overrides"])
                check_type(argname="argument object_access", value=object_access, expected_type=type_hints["object_access"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if allow_public_overrides is not None:
                self._values["allow_public_overrides"] = allow_public_overrides
            if object_access is not None:
                self._values["object_access"] = object_access

        @builtins.property
        def allow_public_overrides(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''A Boolean value indicating whether the access control list (ACL) permissions that are applied to individual objects override the ``GetObject`` option that is currently specified.

            When this is true, you can use the `PutObjectAcl <https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectAcl.html>`_ Amazon S3 API operation to set individual objects to public (read-only) or private, using either the ``public-read`` ACL or the ``private`` ACL.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-bucket-accessrules.html#cfn-lightsail-bucket-accessrules-allowpublicoverrides
            '''
            result = self._values.get("allow_public_overrides")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def object_access(self) -> typing.Optional[builtins.str]:
            '''Specifies the anonymous access to all objects in a bucket.

            The following options can be specified:

            - ``public`` - Sets all objects in the bucket to public (read-only), making them readable by everyone on the internet.

            If the ``GetObject`` value is set to ``public`` , then all objects in the bucket default to public regardless of the ``allowPublicOverrides`` value.

            - ``private`` - Sets all objects in the bucket to private, making them readable only by you and anyone that you grant access to.

            If the ``GetObject`` value is set to ``private`` , and the ``allowPublicOverrides`` value is set to ``true`` , then all objects in the bucket default to private unless they are configured with a ``public-read`` ACL. Individual objects with a ``public-read`` ACL are readable by everyone on the internet.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-bucket-accessrules.html#cfn-lightsail-bucket-accessrules-getobject
            '''
            result = self._values.get("object_access")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AccessRulesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_lightsail.CfnBucketProps",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_name": "bucketName",
        "bundle_id": "bundleId",
        "access_rules": "accessRules",
        "object_versioning": "objectVersioning",
        "read_only_access_accounts": "readOnlyAccessAccounts",
        "resources_receiving_access": "resourcesReceivingAccess",
        "tags": "tags",
    },
)
class CfnBucketProps:
    def __init__(
        self,
        *,
        bucket_name: builtins.str,
        bundle_id: builtins.str,
        access_rules: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBucket.AccessRulesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        object_versioning: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        read_only_access_accounts: typing.Optional[typing.Sequence[builtins.str]] = None,
        resources_receiving_access: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnBucket``.

        :param bucket_name: The name of the bucket.
        :param bundle_id: The bundle ID for the bucket (for example, ``small_1_0`` ). A bucket bundle specifies the monthly cost, storage space, and data transfer quota for a bucket.
        :param access_rules: An object that describes the access rules for the bucket.
        :param object_versioning: Indicates whether object versioning is enabled for the bucket. The following options can be configured: - ``Enabled`` - Object versioning is enabled. - ``Suspended`` - Object versioning was previously enabled but is currently suspended. Existing object versions are retained. - ``NeverEnabled`` - Object versioning has never been enabled.
        :param read_only_access_accounts: An array of AWS account IDs that have read-only access to the bucket.
        :param resources_receiving_access: An array of Lightsail instances that have access to the bucket.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ in the *AWS CloudFormation User Guide* . .. epigraph:: The ``Value`` of ``Tags`` is optional for Lightsail resources.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-bucket.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_lightsail as lightsail
            
            cfn_bucket_props = lightsail.CfnBucketProps(
                bucket_name="bucketName",
                bundle_id="bundleId",
            
                # the properties below are optional
                access_rules=lightsail.CfnBucket.AccessRulesProperty(
                    allow_public_overrides=False,
                    object_access="objectAccess"
                ),
                object_versioning=False,
                read_only_access_accounts=["readOnlyAccessAccounts"],
                resources_receiving_access=["resourcesReceivingAccess"],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cfc80b7f52bbdf250acb4672ad00571df26e5f1142621c5a91482ece0a300415)
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument bundle_id", value=bundle_id, expected_type=type_hints["bundle_id"])
            check_type(argname="argument access_rules", value=access_rules, expected_type=type_hints["access_rules"])
            check_type(argname="argument object_versioning", value=object_versioning, expected_type=type_hints["object_versioning"])
            check_type(argname="argument read_only_access_accounts", value=read_only_access_accounts, expected_type=type_hints["read_only_access_accounts"])
            check_type(argname="argument resources_receiving_access", value=resources_receiving_access, expected_type=type_hints["resources_receiving_access"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bucket_name": bucket_name,
            "bundle_id": bundle_id,
        }
        if access_rules is not None:
            self._values["access_rules"] = access_rules
        if object_versioning is not None:
            self._values["object_versioning"] = object_versioning
        if read_only_access_accounts is not None:
            self._values["read_only_access_accounts"] = read_only_access_accounts
        if resources_receiving_access is not None:
            self._values["resources_receiving_access"] = resources_receiving_access
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def bucket_name(self) -> builtins.str:
        '''The name of the bucket.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-bucket.html#cfn-lightsail-bucket-bucketname
        '''
        result = self._values.get("bucket_name")
        assert result is not None, "Required property 'bucket_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bundle_id(self) -> builtins.str:
        '''The bundle ID for the bucket (for example, ``small_1_0`` ).

        A bucket bundle specifies the monthly cost, storage space, and data transfer quota for a bucket.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-bucket.html#cfn-lightsail-bucket-bundleid
        '''
        result = self._values.get("bundle_id")
        assert result is not None, "Required property 'bundle_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_rules(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnBucket.AccessRulesProperty]]:
        '''An object that describes the access rules for the bucket.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-bucket.html#cfn-lightsail-bucket-accessrules
        '''
        result = self._values.get("access_rules")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnBucket.AccessRulesProperty]], result)

    @builtins.property
    def object_versioning(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Indicates whether object versioning is enabled for the bucket.

        The following options can be configured:

        - ``Enabled`` - Object versioning is enabled.
        - ``Suspended`` - Object versioning was previously enabled but is currently suspended. Existing object versions are retained.
        - ``NeverEnabled`` - Object versioning has never been enabled.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-bucket.html#cfn-lightsail-bucket-objectversioning
        '''
        result = self._values.get("object_versioning")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def read_only_access_accounts(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of AWS account IDs that have read-only access to the bucket.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-bucket.html#cfn-lightsail-bucket-readonlyaccessaccounts
        '''
        result = self._values.get("read_only_access_accounts")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def resources_receiving_access(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of Lightsail instances that have access to the bucket.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-bucket.html#cfn-lightsail-bucket-resourcesreceivingaccess
        '''
        result = self._values.get("resources_receiving_access")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ in the *AWS CloudFormation User Guide* .
        .. epigraph::

           The ``Value`` of ``Tags`` is optional for Lightsail resources.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-bucket.html#cfn-lightsail-bucket-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBucketProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnCertificate(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_lightsail.CfnCertificate",
):
    '''The ``AWS::Lightsail::Certificate`` resource specifies an SSL/TLS certificate that you can use with a content delivery network (CDN) distribution and a container service.

    .. epigraph::

       For information about certificates that you can use with a load balancer, see `AWS::Lightsail::LoadBalancerTlsCertificate <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-loadbalancertlscertificate.html>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-certificate.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_lightsail as lightsail
        
        cfn_certificate = lightsail.CfnCertificate(self, "MyCfnCertificate",
            certificate_name="certificateName",
            domain_name="domainName",
        
            # the properties below are optional
            subject_alternative_names=["subjectAlternativeNames"],
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
        certificate_name: builtins.str,
        domain_name: builtins.str,
        subject_alternative_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param certificate_name: The name of the certificate.
        :param domain_name: The domain name of the certificate.
        :param subject_alternative_names: An array of strings that specify the alternate domains (such as ``example.org`` ) and subdomains (such as ``blog.example.com`` ) of the certificate.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ in the *AWS CloudFormation User Guide* . .. epigraph:: The ``Value`` of ``Tags`` is optional for Lightsail resources.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e46c9c2a31601388f0189b39ac759febe04b899bf6d84e063082749df57f5ef)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCertificateProps(
            certificate_name=certificate_name,
            domain_name=domain_name,
            subject_alternative_names=subject_alternative_names,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd78f535b6f19bc334f8884c826df32506a72bb7be7a48483b6d136b462c2467)
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
            type_hints = typing.get_type_hints(_typecheckingstub__81b4a0c654d5ac565c158a4cccb760fdd62d938202b41b6cf3140a72c8fb5a1a)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCertificateArn")
    def attr_certificate_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the certificate.

        :cloudformationAttribute: CertificateArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCertificateArn"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The validation status of the certificate.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

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
    @jsii.member(jsii_name="certificateName")
    def certificate_name(self) -> builtins.str:
        '''The name of the certificate.'''
        return typing.cast(builtins.str, jsii.get(self, "certificateName"))

    @certificate_name.setter
    def certificate_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b13a2a543d6b2720b4cf168052ef4b17165797152752e38fff22e9a4fbd5c425)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateName", value)

    @builtins.property
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        '''The domain name of the certificate.'''
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @domain_name.setter
    def domain_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__561359c124f9c2bc11955748c848288878d75889197cec6c9f222b79a3ad2cdb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainName", value)

    @builtins.property
    @jsii.member(jsii_name="subjectAlternativeNames")
    def subject_alternative_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of strings that specify the alternate domains (such as ``example.org`` ) and subdomains (such as ``blog.example.com`` ) of the certificate.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "subjectAlternativeNames"))

    @subject_alternative_names.setter
    def subject_alternative_names(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bde188d393958878c8d4e57a5877d812238d5cefe2fc847b8666282a8e53290a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subjectAlternativeNames", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa0e2472d9d23da3ec2ce0c96320254278721ae808d47271138b62d6684a75b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_lightsail.CfnCertificateProps",
    jsii_struct_bases=[],
    name_mapping={
        "certificate_name": "certificateName",
        "domain_name": "domainName",
        "subject_alternative_names": "subjectAlternativeNames",
        "tags": "tags",
    },
)
class CfnCertificateProps:
    def __init__(
        self,
        *,
        certificate_name: builtins.str,
        domain_name: builtins.str,
        subject_alternative_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnCertificate``.

        :param certificate_name: The name of the certificate.
        :param domain_name: The domain name of the certificate.
        :param subject_alternative_names: An array of strings that specify the alternate domains (such as ``example.org`` ) and subdomains (such as ``blog.example.com`` ) of the certificate.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ in the *AWS CloudFormation User Guide* . .. epigraph:: The ``Value`` of ``Tags`` is optional for Lightsail resources.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-certificate.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_lightsail as lightsail
            
            cfn_certificate_props = lightsail.CfnCertificateProps(
                certificate_name="certificateName",
                domain_name="domainName",
            
                # the properties below are optional
                subject_alternative_names=["subjectAlternativeNames"],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2fece9fd02d544f5e7457740dc0b59430a4b93239cb2e0ea2ff7d402d126510b)
            check_type(argname="argument certificate_name", value=certificate_name, expected_type=type_hints["certificate_name"])
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument subject_alternative_names", value=subject_alternative_names, expected_type=type_hints["subject_alternative_names"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "certificate_name": certificate_name,
            "domain_name": domain_name,
        }
        if subject_alternative_names is not None:
            self._values["subject_alternative_names"] = subject_alternative_names
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def certificate_name(self) -> builtins.str:
        '''The name of the certificate.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-certificate.html#cfn-lightsail-certificate-certificatename
        '''
        result = self._values.get("certificate_name")
        assert result is not None, "Required property 'certificate_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''The domain name of the certificate.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-certificate.html#cfn-lightsail-certificate-domainname
        '''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subject_alternative_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of strings that specify the alternate domains (such as ``example.org`` ) and subdomains (such as ``blog.example.com`` ) of the certificate.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-certificate.html#cfn-lightsail-certificate-subjectalternativenames
        '''
        result = self._values.get("subject_alternative_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ in the *AWS CloudFormation User Guide* .
        .. epigraph::

           The ``Value`` of ``Tags`` is optional for Lightsail resources.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-certificate.html#cfn-lightsail-certificate-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCertificateProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnContainer(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_lightsail.CfnContainer",
):
    '''The ``AWS::Lightsail::Container`` resource specifies a container service.

    A Lightsail container service is a compute resource to which you can deploy containers.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-container.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_lightsail as lightsail
        
        cfn_container = lightsail.CfnContainer(self, "MyCfnContainer",
            power="power",
            scale=123,
            service_name="serviceName",
        
            # the properties below are optional
            container_service_deployment=lightsail.CfnContainer.ContainerServiceDeploymentProperty(
                containers=[lightsail.CfnContainer.ContainerProperty(
                    command=["command"],
                    container_name="containerName",
                    environment=[lightsail.CfnContainer.EnvironmentVariableProperty(
                        value="value",
                        variable="variable"
                    )],
                    image="image",
                    ports=[lightsail.CfnContainer.PortInfoProperty(
                        port="port",
                        protocol="protocol"
                    )]
                )],
                public_endpoint=lightsail.CfnContainer.PublicEndpointProperty(
                    container_name="containerName",
                    container_port=123,
                    health_check_config=lightsail.CfnContainer.HealthCheckConfigProperty(
                        healthy_threshold=123,
                        interval_seconds=123,
                        path="path",
                        success_codes="successCodes",
                        timeout_seconds=123,
                        unhealthy_threshold=123
                    )
                )
            ),
            is_disabled=False,
            public_domain_names=[lightsail.CfnContainer.PublicDomainNameProperty(
                certificate_name="certificateName",
                domain_names=["domainNames"]
            )],
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
        power: builtins.str,
        scale: jsii.Number,
        service_name: builtins.str,
        container_service_deployment: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnContainer.ContainerServiceDeploymentProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        is_disabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        public_domain_names: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnContainer.PublicDomainNameProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param power: The power specification of the container service. The power specifies the amount of RAM, the number of vCPUs, and the base price of the container service.
        :param scale: The scale specification of the container service. The scale specifies the allocated compute nodes of the container service.
        :param service_name: The name of the container service.
        :param container_service_deployment: An object that describes the current container deployment of the container service.
        :param is_disabled: A Boolean value indicating whether the container service is disabled.
        :param public_domain_names: The public domain name of the container service, such as ``example.com`` and ``www.example.com`` . You can specify up to four public domain names for a container service. The domain names that you specify are used when you create a deployment with a container that is configured as the public endpoint of your container service. If you don't specify public domain names, then you can use the default domain of the container service. .. epigraph:: You must create and validate an SSL/TLS certificate before you can use public domain names with your container service. Use the `AWS::Lightsail::Certificate <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-certificate.html>`_ resource to create a certificate for the public domain names that you want to use with your container service.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ in the *AWS CloudFormation User Guide* . .. epigraph:: The ``Value`` of ``Tags`` is optional for Lightsail resources.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94bac8a5de27a74603b05e36d9c72422cb8c35ec6940b2bcc87094fd27fbc7ac)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnContainerProps(
            power=power,
            scale=scale,
            service_name=service_name,
            container_service_deployment=container_service_deployment,
            is_disabled=is_disabled,
            public_domain_names=public_domain_names,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd0b8f262d0bb3db8f5559a78d02ed77d6d817f801cff964ae11b76f927a030d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5ccc317951b85768b34fae7b08d2c64434b38c35cbb35636a5c8f4525537d2e8)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrContainerArn")
    def attr_container_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the container.

        :cloudformationAttribute: ContainerArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrContainerArn"))

    @builtins.property
    @jsii.member(jsii_name="attrUrl")
    def attr_url(self) -> builtins.str:
        '''The publicly accessible URL of the container service.

        If no public endpoint is specified in the current deployment, this URL returns a 404 response.

        :cloudformationAttribute: Url
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUrl"))

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
    @jsii.member(jsii_name="power")
    def power(self) -> builtins.str:
        '''The power specification of the container service.'''
        return typing.cast(builtins.str, jsii.get(self, "power"))

    @power.setter
    def power(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c43b42c387b2dcfa1723f7d229e7a7d6123b4a5dd3c00b08379a0d8c5b9ca0a3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "power", value)

    @builtins.property
    @jsii.member(jsii_name="scale")
    def scale(self) -> jsii.Number:
        '''The scale specification of the container service.'''
        return typing.cast(jsii.Number, jsii.get(self, "scale"))

    @scale.setter
    def scale(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9aa65eb02fb8c30379eca4549f1c20fe31b13502f31a42fb2d5bc4a0c834e54e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scale", value)

    @builtins.property
    @jsii.member(jsii_name="serviceName")
    def service_name(self) -> builtins.str:
        '''The name of the container service.'''
        return typing.cast(builtins.str, jsii.get(self, "serviceName"))

    @service_name.setter
    def service_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc3a585466a749c4c1a1d7e4f0ff912b27ba8bff6127862e194982ee4e1a955d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceName", value)

    @builtins.property
    @jsii.member(jsii_name="containerServiceDeployment")
    def container_service_deployment(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnContainer.ContainerServiceDeploymentProperty"]]:
        '''An object that describes the current container deployment of the container service.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnContainer.ContainerServiceDeploymentProperty"]], jsii.get(self, "containerServiceDeployment"))

    @container_service_deployment.setter
    def container_service_deployment(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnContainer.ContainerServiceDeploymentProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e8ef0ed2b23c56026e0da66efb4213ed90af7b6dfea05d5bbce033060cc7e43)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerServiceDeployment", value)

    @builtins.property
    @jsii.member(jsii_name="isDisabled")
    def is_disabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''A Boolean value indicating whether the container service is disabled.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "isDisabled"))

    @is_disabled.setter
    def is_disabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a52d8c870a181dac72ac9809ac930672df1d327079dcac65e47b7e2aadcd54ed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isDisabled", value)

    @builtins.property
    @jsii.member(jsii_name="publicDomainNames")
    def public_domain_names(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnContainer.PublicDomainNameProperty"]]]]:
        '''The public domain name of the container service, such as ``example.com`` and ``www.example.com`` .'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnContainer.PublicDomainNameProperty"]]]], jsii.get(self, "publicDomainNames"))

    @public_domain_names.setter
    def public_domain_names(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnContainer.PublicDomainNameProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa200bad90bddaf505b39b733612869b17dd2e87cd1aaa81d1cfedde46e1bb8e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicDomainNames", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7eef525fca5f562f87e3ac9c6423f561f56721f252309711cf942b6679b0ed6e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lightsail.CfnContainer.ContainerProperty",
        jsii_struct_bases=[],
        name_mapping={
            "command": "command",
            "container_name": "containerName",
            "environment": "environment",
            "image": "image",
            "ports": "ports",
        },
    )
    class ContainerProperty:
        def __init__(
            self,
            *,
            command: typing.Optional[typing.Sequence[builtins.str]] = None,
            container_name: typing.Optional[builtins.str] = None,
            environment: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnContainer.EnvironmentVariableProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            image: typing.Optional[builtins.str] = None,
            ports: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnContainer.PortInfoProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''``Container`` is a property of the `ContainerServiceDeployment <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-containerservicedeployment.html>`_ property. It describes the settings of a container that will be launched, or that is launched, to an Amazon Lightsail container service.

            :param command: The launch command for the container.
            :param container_name: The name of the container.
            :param environment: The environment variables of the container.
            :param image: The name of the image used for the container. Container images that are sourced from (registered and stored on) your container service start with a colon ( ``:`` ). For example, if your container service name is ``container-service-1`` , the container image label is ``mystaticsite`` , and you want to use the third version ( ``3`` ) of the registered container image, then you should specify ``:container-service-1.mystaticsite.3`` . To use the latest version of a container image, specify ``latest`` instead of a version number (for example, ``:container-service-1.mystaticsite.latest`` ). Your container service will automatically use the highest numbered version of the registered container image. Container images that are sourced from a public registry like Docker Hub don’t start with a colon. For example, ``nginx:latest`` or ``nginx`` .
            :param ports: An object that describes the open firewall ports and protocols of the container.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-container.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lightsail as lightsail
                
                container_property = lightsail.CfnContainer.ContainerProperty(
                    command=["command"],
                    container_name="containerName",
                    environment=[lightsail.CfnContainer.EnvironmentVariableProperty(
                        value="value",
                        variable="variable"
                    )],
                    image="image",
                    ports=[lightsail.CfnContainer.PortInfoProperty(
                        port="port",
                        protocol="protocol"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2643ecd28650d4a160cec5faf8d37c64b7d9033d437056ac73a83cfb6d60a74c)
                check_type(argname="argument command", value=command, expected_type=type_hints["command"])
                check_type(argname="argument container_name", value=container_name, expected_type=type_hints["container_name"])
                check_type(argname="argument environment", value=environment, expected_type=type_hints["environment"])
                check_type(argname="argument image", value=image, expected_type=type_hints["image"])
                check_type(argname="argument ports", value=ports, expected_type=type_hints["ports"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if command is not None:
                self._values["command"] = command
            if container_name is not None:
                self._values["container_name"] = container_name
            if environment is not None:
                self._values["environment"] = environment
            if image is not None:
                self._values["image"] = image
            if ports is not None:
                self._values["ports"] = ports

        @builtins.property
        def command(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The launch command for the container.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-container.html#cfn-lightsail-container-container-command
            '''
            result = self._values.get("command")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def container_name(self) -> typing.Optional[builtins.str]:
            '''The name of the container.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-container.html#cfn-lightsail-container-container-containername
            '''
            result = self._values.get("container_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def environment(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnContainer.EnvironmentVariableProperty"]]]]:
            '''The environment variables of the container.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-container.html#cfn-lightsail-container-container-environment
            '''
            result = self._values.get("environment")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnContainer.EnvironmentVariableProperty"]]]], result)

        @builtins.property
        def image(self) -> typing.Optional[builtins.str]:
            '''The name of the image used for the container.

            Container images that are sourced from (registered and stored on) your container service start with a colon ( ``:`` ). For example, if your container service name is ``container-service-1`` , the container image label is ``mystaticsite`` , and you want to use the third version ( ``3`` ) of the registered container image, then you should specify ``:container-service-1.mystaticsite.3`` . To use the latest version of a container image, specify ``latest`` instead of a version number (for example, ``:container-service-1.mystaticsite.latest`` ). Your container service will automatically use the highest numbered version of the registered container image.

            Container images that are sourced from a public registry like Docker Hub don’t start with a colon. For example, ``nginx:latest`` or ``nginx`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-container.html#cfn-lightsail-container-container-image
            '''
            result = self._values.get("image")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def ports(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnContainer.PortInfoProperty"]]]]:
            '''An object that describes the open firewall ports and protocols of the container.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-container.html#cfn-lightsail-container-container-ports
            '''
            result = self._values.get("ports")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnContainer.PortInfoProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ContainerProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lightsail.CfnContainer.ContainerServiceDeploymentProperty",
        jsii_struct_bases=[],
        name_mapping={"containers": "containers", "public_endpoint": "publicEndpoint"},
    )
    class ContainerServiceDeploymentProperty:
        def __init__(
            self,
            *,
            containers: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnContainer.ContainerProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            public_endpoint: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnContainer.PublicEndpointProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''``ContainerServiceDeployment`` is a property of the `AWS::Lightsail::Container <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-container.html>`_ resource. It describes a container deployment configuration of a container service.

            A deployment specifies the settings, such as the ports and launch command, of containers that are deployed to your container service.

            :param containers: An object that describes the configuration for the containers of the deployment.
            :param public_endpoint: An object that describes the endpoint of the deployment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-containerservicedeployment.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lightsail as lightsail
                
                container_service_deployment_property = lightsail.CfnContainer.ContainerServiceDeploymentProperty(
                    containers=[lightsail.CfnContainer.ContainerProperty(
                        command=["command"],
                        container_name="containerName",
                        environment=[lightsail.CfnContainer.EnvironmentVariableProperty(
                            value="value",
                            variable="variable"
                        )],
                        image="image",
                        ports=[lightsail.CfnContainer.PortInfoProperty(
                            port="port",
                            protocol="protocol"
                        )]
                    )],
                    public_endpoint=lightsail.CfnContainer.PublicEndpointProperty(
                        container_name="containerName",
                        container_port=123,
                        health_check_config=lightsail.CfnContainer.HealthCheckConfigProperty(
                            healthy_threshold=123,
                            interval_seconds=123,
                            path="path",
                            success_codes="successCodes",
                            timeout_seconds=123,
                            unhealthy_threshold=123
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__361b481c01847aedbb1dab6f7a2b940c6da922f6af27593f14d67b2288673a11)
                check_type(argname="argument containers", value=containers, expected_type=type_hints["containers"])
                check_type(argname="argument public_endpoint", value=public_endpoint, expected_type=type_hints["public_endpoint"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if containers is not None:
                self._values["containers"] = containers
            if public_endpoint is not None:
                self._values["public_endpoint"] = public_endpoint

        @builtins.property
        def containers(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnContainer.ContainerProperty"]]]]:
            '''An object that describes the configuration for the containers of the deployment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-containerservicedeployment.html#cfn-lightsail-container-containerservicedeployment-containers
            '''
            result = self._values.get("containers")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnContainer.ContainerProperty"]]]], result)

        @builtins.property
        def public_endpoint(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnContainer.PublicEndpointProperty"]]:
            '''An object that describes the endpoint of the deployment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-containerservicedeployment.html#cfn-lightsail-container-containerservicedeployment-publicendpoint
            '''
            result = self._values.get("public_endpoint")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnContainer.PublicEndpointProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ContainerServiceDeploymentProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lightsail.CfnContainer.EnvironmentVariableProperty",
        jsii_struct_bases=[],
        name_mapping={"value": "value", "variable": "variable"},
    )
    class EnvironmentVariableProperty:
        def __init__(
            self,
            *,
            value: typing.Optional[builtins.str] = None,
            variable: typing.Optional[builtins.str] = None,
        ) -> None:
            '''``EnvironmentVariable`` is a property of the `Container <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-container.html>`_ property. It describes the environment variables of a container on a container service which are key-value parameters that provide dynamic configuration of the application or script run by the container.

            :param value: The environment variable value.
            :param variable: The environment variable key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-environmentvariable.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lightsail as lightsail
                
                environment_variable_property = lightsail.CfnContainer.EnvironmentVariableProperty(
                    value="value",
                    variable="variable"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c0a31811b7a56ea2f4b026dbd07da448a9b8998283ff6d18707ad7fb4b594494)
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
                check_type(argname="argument variable", value=variable, expected_type=type_hints["variable"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if value is not None:
                self._values["value"] = value
            if variable is not None:
                self._values["variable"] = variable

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''The environment variable value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-environmentvariable.html#cfn-lightsail-container-environmentvariable-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def variable(self) -> typing.Optional[builtins.str]:
            '''The environment variable key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-environmentvariable.html#cfn-lightsail-container-environmentvariable-variable
            '''
            result = self._values.get("variable")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EnvironmentVariableProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lightsail.CfnContainer.HealthCheckConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "healthy_threshold": "healthyThreshold",
            "interval_seconds": "intervalSeconds",
            "path": "path",
            "success_codes": "successCodes",
            "timeout_seconds": "timeoutSeconds",
            "unhealthy_threshold": "unhealthyThreshold",
        },
    )
    class HealthCheckConfigProperty:
        def __init__(
            self,
            *,
            healthy_threshold: typing.Optional[jsii.Number] = None,
            interval_seconds: typing.Optional[jsii.Number] = None,
            path: typing.Optional[builtins.str] = None,
            success_codes: typing.Optional[builtins.str] = None,
            timeout_seconds: typing.Optional[jsii.Number] = None,
            unhealthy_threshold: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''``HealthCheckConfig`` is a property of the `PublicEndpoint <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-publicendpoint.html>`_ property. It describes the healthcheck configuration of a container deployment on a container service.

            :param healthy_threshold: The number of consecutive health check successes required before moving the container to the ``Healthy`` state. The default value is ``2`` .
            :param interval_seconds: The approximate interval, in seconds, between health checks of an individual container. You can specify between ``5`` and ``300`` seconds. The default value is ``5`` .
            :param path: The path on the container on which to perform the health check. The default value is ``/`` .
            :param success_codes: The HTTP codes to use when checking for a successful response from a container. You can specify values between ``200`` and ``499`` . You can specify multiple values (for example, ``200,202`` ) or a range of values (for example, ``200-299`` ).
            :param timeout_seconds: The amount of time, in seconds, during which no response means a failed health check. You can specify between ``2`` and ``60`` seconds. The default value is ``2`` .
            :param unhealthy_threshold: The number of consecutive health check failures required before moving the container to the ``Unhealthy`` state. The default value is ``2`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-healthcheckconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lightsail as lightsail
                
                health_check_config_property = lightsail.CfnContainer.HealthCheckConfigProperty(
                    healthy_threshold=123,
                    interval_seconds=123,
                    path="path",
                    success_codes="successCodes",
                    timeout_seconds=123,
                    unhealthy_threshold=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__117cfc04d169db66d5bf8186765ffa02af0a0c5769b9891fd1a2ff4478ccba20)
                check_type(argname="argument healthy_threshold", value=healthy_threshold, expected_type=type_hints["healthy_threshold"])
                check_type(argname="argument interval_seconds", value=interval_seconds, expected_type=type_hints["interval_seconds"])
                check_type(argname="argument path", value=path, expected_type=type_hints["path"])
                check_type(argname="argument success_codes", value=success_codes, expected_type=type_hints["success_codes"])
                check_type(argname="argument timeout_seconds", value=timeout_seconds, expected_type=type_hints["timeout_seconds"])
                check_type(argname="argument unhealthy_threshold", value=unhealthy_threshold, expected_type=type_hints["unhealthy_threshold"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if healthy_threshold is not None:
                self._values["healthy_threshold"] = healthy_threshold
            if interval_seconds is not None:
                self._values["interval_seconds"] = interval_seconds
            if path is not None:
                self._values["path"] = path
            if success_codes is not None:
                self._values["success_codes"] = success_codes
            if timeout_seconds is not None:
                self._values["timeout_seconds"] = timeout_seconds
            if unhealthy_threshold is not None:
                self._values["unhealthy_threshold"] = unhealthy_threshold

        @builtins.property
        def healthy_threshold(self) -> typing.Optional[jsii.Number]:
            '''The number of consecutive health check successes required before moving the container to the ``Healthy`` state.

            The default value is ``2`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-healthcheckconfig.html#cfn-lightsail-container-healthcheckconfig-healthythreshold
            '''
            result = self._values.get("healthy_threshold")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def interval_seconds(self) -> typing.Optional[jsii.Number]:
            '''The approximate interval, in seconds, between health checks of an individual container.

            You can specify between ``5`` and ``300`` seconds. The default value is ``5`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-healthcheckconfig.html#cfn-lightsail-container-healthcheckconfig-intervalseconds
            '''
            result = self._values.get("interval_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def path(self) -> typing.Optional[builtins.str]:
            '''The path on the container on which to perform the health check.

            The default value is ``/`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-healthcheckconfig.html#cfn-lightsail-container-healthcheckconfig-path
            '''
            result = self._values.get("path")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def success_codes(self) -> typing.Optional[builtins.str]:
            '''The HTTP codes to use when checking for a successful response from a container.

            You can specify values between ``200`` and ``499`` . You can specify multiple values (for example, ``200,202`` ) or a range of values (for example, ``200-299`` ).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-healthcheckconfig.html#cfn-lightsail-container-healthcheckconfig-successcodes
            '''
            result = self._values.get("success_codes")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def timeout_seconds(self) -> typing.Optional[jsii.Number]:
            '''The amount of time, in seconds, during which no response means a failed health check.

            You can specify between ``2`` and ``60`` seconds. The default value is ``2`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-healthcheckconfig.html#cfn-lightsail-container-healthcheckconfig-timeoutseconds
            '''
            result = self._values.get("timeout_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def unhealthy_threshold(self) -> typing.Optional[jsii.Number]:
            '''The number of consecutive health check failures required before moving the container to the ``Unhealthy`` state.

            The default value is ``2`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-healthcheckconfig.html#cfn-lightsail-container-healthcheckconfig-unhealthythreshold
            '''
            result = self._values.get("unhealthy_threshold")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HealthCheckConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lightsail.CfnContainer.PortInfoProperty",
        jsii_struct_bases=[],
        name_mapping={"port": "port", "protocol": "protocol"},
    )
    class PortInfoProperty:
        def __init__(
            self,
            *,
            port: typing.Optional[builtins.str] = None,
            protocol: typing.Optional[builtins.str] = None,
        ) -> None:
            '''``PortInfo`` is a property of the `Container <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-container.html>`_ property. It describes the ports to open and the protocols to use for a container on a Amazon Lightsail container service.

            :param port: The open firewall ports of the container.
            :param protocol: The protocol name for the open ports. *Allowed values* : ``HTTP`` | ``HTTPS`` | ``TCP`` | ``UDP``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-portinfo.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lightsail as lightsail
                
                port_info_property = lightsail.CfnContainer.PortInfoProperty(
                    port="port",
                    protocol="protocol"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2957cb3f17880ab79f0061a8100d03ac1b612e1511f4a371be09517cb05571fa)
                check_type(argname="argument port", value=port, expected_type=type_hints["port"])
                check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if port is not None:
                self._values["port"] = port
            if protocol is not None:
                self._values["protocol"] = protocol

        @builtins.property
        def port(self) -> typing.Optional[builtins.str]:
            '''The open firewall ports of the container.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-portinfo.html#cfn-lightsail-container-portinfo-port
            '''
            result = self._values.get("port")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def protocol(self) -> typing.Optional[builtins.str]:
            '''The protocol name for the open ports.

            *Allowed values* : ``HTTP`` | ``HTTPS`` | ``TCP`` | ``UDP``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-portinfo.html#cfn-lightsail-container-portinfo-protocol
            '''
            result = self._values.get("protocol")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PortInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lightsail.CfnContainer.PublicDomainNameProperty",
        jsii_struct_bases=[],
        name_mapping={
            "certificate_name": "certificateName",
            "domain_names": "domainNames",
        },
    )
    class PublicDomainNameProperty:
        def __init__(
            self,
            *,
            certificate_name: typing.Optional[builtins.str] = None,
            domain_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''``PublicDomainName`` is a property of the `AWS::Lightsail::Container <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-container.html>`_ resource. It describes the public domain names to use with a container service, such as ``example.com`` and ``www.example.com`` . It also describes the certificates to use with a container service.

            :param certificate_name: The name of the certificate for the public domains.
            :param domain_names: The public domain names to use with the container service.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-publicdomainname.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lightsail as lightsail
                
                public_domain_name_property = lightsail.CfnContainer.PublicDomainNameProperty(
                    certificate_name="certificateName",
                    domain_names=["domainNames"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6d9c472b649d2e9119b005aacad2dbe93a008b5ae90f7dafffb84c714e14e831)
                check_type(argname="argument certificate_name", value=certificate_name, expected_type=type_hints["certificate_name"])
                check_type(argname="argument domain_names", value=domain_names, expected_type=type_hints["domain_names"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if certificate_name is not None:
                self._values["certificate_name"] = certificate_name
            if domain_names is not None:
                self._values["domain_names"] = domain_names

        @builtins.property
        def certificate_name(self) -> typing.Optional[builtins.str]:
            '''The name of the certificate for the public domains.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-publicdomainname.html#cfn-lightsail-container-publicdomainname-certificatename
            '''
            result = self._values.get("certificate_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def domain_names(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The public domain names to use with the container service.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-publicdomainname.html#cfn-lightsail-container-publicdomainname-domainnames
            '''
            result = self._values.get("domain_names")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PublicDomainNameProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lightsail.CfnContainer.PublicEndpointProperty",
        jsii_struct_bases=[],
        name_mapping={
            "container_name": "containerName",
            "container_port": "containerPort",
            "health_check_config": "healthCheckConfig",
        },
    )
    class PublicEndpointProperty:
        def __init__(
            self,
            *,
            container_name: typing.Optional[builtins.str] = None,
            container_port: typing.Optional[jsii.Number] = None,
            health_check_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnContainer.HealthCheckConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''``PublicEndpoint`` is a property of the `ContainerServiceDeployment <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-containerservicedeployment.html>`_ property. It describes describes the settings of the public endpoint of a container on a container service.

            :param container_name: The name of the container entry of the deployment that the endpoint configuration applies to.
            :param container_port: The port of the specified container to which traffic is forwarded to.
            :param health_check_config: An object that describes the health check configuration of the container.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-publicendpoint.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lightsail as lightsail
                
                public_endpoint_property = lightsail.CfnContainer.PublicEndpointProperty(
                    container_name="containerName",
                    container_port=123,
                    health_check_config=lightsail.CfnContainer.HealthCheckConfigProperty(
                        healthy_threshold=123,
                        interval_seconds=123,
                        path="path",
                        success_codes="successCodes",
                        timeout_seconds=123,
                        unhealthy_threshold=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cd597e5de3f9b4ca413b0f95b46ae241cde5964a9efbb640c28cf6593d3de7b0)
                check_type(argname="argument container_name", value=container_name, expected_type=type_hints["container_name"])
                check_type(argname="argument container_port", value=container_port, expected_type=type_hints["container_port"])
                check_type(argname="argument health_check_config", value=health_check_config, expected_type=type_hints["health_check_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if container_name is not None:
                self._values["container_name"] = container_name
            if container_port is not None:
                self._values["container_port"] = container_port
            if health_check_config is not None:
                self._values["health_check_config"] = health_check_config

        @builtins.property
        def container_name(self) -> typing.Optional[builtins.str]:
            '''The name of the container entry of the deployment that the endpoint configuration applies to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-publicendpoint.html#cfn-lightsail-container-publicendpoint-containername
            '''
            result = self._values.get("container_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def container_port(self) -> typing.Optional[jsii.Number]:
            '''The port of the specified container to which traffic is forwarded to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-publicendpoint.html#cfn-lightsail-container-publicendpoint-containerport
            '''
            result = self._values.get("container_port")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def health_check_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnContainer.HealthCheckConfigProperty"]]:
            '''An object that describes the health check configuration of the container.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-publicendpoint.html#cfn-lightsail-container-publicendpoint-healthcheckconfig
            '''
            result = self._values.get("health_check_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnContainer.HealthCheckConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PublicEndpointProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_lightsail.CfnContainerProps",
    jsii_struct_bases=[],
    name_mapping={
        "power": "power",
        "scale": "scale",
        "service_name": "serviceName",
        "container_service_deployment": "containerServiceDeployment",
        "is_disabled": "isDisabled",
        "public_domain_names": "publicDomainNames",
        "tags": "tags",
    },
)
class CfnContainerProps:
    def __init__(
        self,
        *,
        power: builtins.str,
        scale: jsii.Number,
        service_name: builtins.str,
        container_service_deployment: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainer.ContainerServiceDeploymentProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        is_disabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        public_domain_names: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainer.PublicDomainNameProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnContainer``.

        :param power: The power specification of the container service. The power specifies the amount of RAM, the number of vCPUs, and the base price of the container service.
        :param scale: The scale specification of the container service. The scale specifies the allocated compute nodes of the container service.
        :param service_name: The name of the container service.
        :param container_service_deployment: An object that describes the current container deployment of the container service.
        :param is_disabled: A Boolean value indicating whether the container service is disabled.
        :param public_domain_names: The public domain name of the container service, such as ``example.com`` and ``www.example.com`` . You can specify up to four public domain names for a container service. The domain names that you specify are used when you create a deployment with a container that is configured as the public endpoint of your container service. If you don't specify public domain names, then you can use the default domain of the container service. .. epigraph:: You must create and validate an SSL/TLS certificate before you can use public domain names with your container service. Use the `AWS::Lightsail::Certificate <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-certificate.html>`_ resource to create a certificate for the public domain names that you want to use with your container service.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ in the *AWS CloudFormation User Guide* . .. epigraph:: The ``Value`` of ``Tags`` is optional for Lightsail resources.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-container.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_lightsail as lightsail
            
            cfn_container_props = lightsail.CfnContainerProps(
                power="power",
                scale=123,
                service_name="serviceName",
            
                # the properties below are optional
                container_service_deployment=lightsail.CfnContainer.ContainerServiceDeploymentProperty(
                    containers=[lightsail.CfnContainer.ContainerProperty(
                        command=["command"],
                        container_name="containerName",
                        environment=[lightsail.CfnContainer.EnvironmentVariableProperty(
                            value="value",
                            variable="variable"
                        )],
                        image="image",
                        ports=[lightsail.CfnContainer.PortInfoProperty(
                            port="port",
                            protocol="protocol"
                        )]
                    )],
                    public_endpoint=lightsail.CfnContainer.PublicEndpointProperty(
                        container_name="containerName",
                        container_port=123,
                        health_check_config=lightsail.CfnContainer.HealthCheckConfigProperty(
                            healthy_threshold=123,
                            interval_seconds=123,
                            path="path",
                            success_codes="successCodes",
                            timeout_seconds=123,
                            unhealthy_threshold=123
                        )
                    )
                ),
                is_disabled=False,
                public_domain_names=[lightsail.CfnContainer.PublicDomainNameProperty(
                    certificate_name="certificateName",
                    domain_names=["domainNames"]
                )],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97ba65c009b99fbaa7ef08e0bf85a260e5a557dc34e2894b5cbb3a6a6a4aa907)
            check_type(argname="argument power", value=power, expected_type=type_hints["power"])
            check_type(argname="argument scale", value=scale, expected_type=type_hints["scale"])
            check_type(argname="argument service_name", value=service_name, expected_type=type_hints["service_name"])
            check_type(argname="argument container_service_deployment", value=container_service_deployment, expected_type=type_hints["container_service_deployment"])
            check_type(argname="argument is_disabled", value=is_disabled, expected_type=type_hints["is_disabled"])
            check_type(argname="argument public_domain_names", value=public_domain_names, expected_type=type_hints["public_domain_names"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "power": power,
            "scale": scale,
            "service_name": service_name,
        }
        if container_service_deployment is not None:
            self._values["container_service_deployment"] = container_service_deployment
        if is_disabled is not None:
            self._values["is_disabled"] = is_disabled
        if public_domain_names is not None:
            self._values["public_domain_names"] = public_domain_names
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def power(self) -> builtins.str:
        '''The power specification of the container service.

        The power specifies the amount of RAM, the number of vCPUs, and the base price of the container service.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-container.html#cfn-lightsail-container-power
        '''
        result = self._values.get("power")
        assert result is not None, "Required property 'power' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def scale(self) -> jsii.Number:
        '''The scale specification of the container service.

        The scale specifies the allocated compute nodes of the container service.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-container.html#cfn-lightsail-container-scale
        '''
        result = self._values.get("scale")
        assert result is not None, "Required property 'scale' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def service_name(self) -> builtins.str:
        '''The name of the container service.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-container.html#cfn-lightsail-container-servicename
        '''
        result = self._values.get("service_name")
        assert result is not None, "Required property 'service_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def container_service_deployment(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnContainer.ContainerServiceDeploymentProperty]]:
        '''An object that describes the current container deployment of the container service.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-container.html#cfn-lightsail-container-containerservicedeployment
        '''
        result = self._values.get("container_service_deployment")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnContainer.ContainerServiceDeploymentProperty]], result)

    @builtins.property
    def is_disabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''A Boolean value indicating whether the container service is disabled.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-container.html#cfn-lightsail-container-isdisabled
        '''
        result = self._values.get("is_disabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def public_domain_names(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnContainer.PublicDomainNameProperty]]]]:
        '''The public domain name of the container service, such as ``example.com`` and ``www.example.com`` .

        You can specify up to four public domain names for a container service. The domain names that you specify are used when you create a deployment with a container that is configured as the public endpoint of your container service.

        If you don't specify public domain names, then you can use the default domain of the container service.
        .. epigraph::

           You must create and validate an SSL/TLS certificate before you can use public domain names with your container service. Use the `AWS::Lightsail::Certificate <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-certificate.html>`_ resource to create a certificate for the public domain names that you want to use with your container service.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-container.html#cfn-lightsail-container-publicdomainnames
        '''
        result = self._values.get("public_domain_names")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnContainer.PublicDomainNameProperty]]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ in the *AWS CloudFormation User Guide* .
        .. epigraph::

           The ``Value`` of ``Tags`` is optional for Lightsail resources.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-container.html#cfn-lightsail-container-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnContainerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnDatabase(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_lightsail.CfnDatabase",
):
    '''The ``AWS::Lightsail::Database`` resource specifies an Amazon Lightsail database.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_lightsail as lightsail
        
        cfn_database = lightsail.CfnDatabase(self, "MyCfnDatabase",
            master_database_name="masterDatabaseName",
            master_username="masterUsername",
            relational_database_blueprint_id="relationalDatabaseBlueprintId",
            relational_database_bundle_id="relationalDatabaseBundleId",
            relational_database_name="relationalDatabaseName",
        
            # the properties below are optional
            availability_zone="availabilityZone",
            backup_retention=False,
            ca_certificate_identifier="caCertificateIdentifier",
            master_user_password="masterUserPassword",
            preferred_backup_window="preferredBackupWindow",
            preferred_maintenance_window="preferredMaintenanceWindow",
            publicly_accessible=False,
            relational_database_parameters=[lightsail.CfnDatabase.RelationalDatabaseParameterProperty(
                allowed_values="allowedValues",
                apply_method="applyMethod",
                apply_type="applyType",
                data_type="dataType",
                description="description",
                is_modifiable=False,
                parameter_name="parameterName",
                parameter_value="parameterValue"
            )],
            rotate_master_user_password=False,
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
        master_database_name: builtins.str,
        master_username: builtins.str,
        relational_database_blueprint_id: builtins.str,
        relational_database_bundle_id: builtins.str,
        relational_database_name: builtins.str,
        availability_zone: typing.Optional[builtins.str] = None,
        backup_retention: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ca_certificate_identifier: typing.Optional[builtins.str] = None,
        master_user_password: typing.Optional[builtins.str] = None,
        preferred_backup_window: typing.Optional[builtins.str] = None,
        preferred_maintenance_window: typing.Optional[builtins.str] = None,
        publicly_accessible: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        relational_database_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDatabase.RelationalDatabaseParameterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        rotate_master_user_password: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param master_database_name: The meaning of this parameter differs according to the database engine you use. *MySQL* The name of the database to create when the Lightsail database resource is created. If this parameter isn't specified, no database is created in the database resource. Constraints: - Must contain 1-64 letters or numbers. - Must begin with a letter. Subsequent characters can be letters, underscores, or numbers (0-9). - Can't be a word reserved by the specified database engine. For more information about reserved words in MySQL, see the Keywords and Reserved Words articles for `MySQL 5.6 <https://docs.aws.amazon.com/https://dev.mysql.com/doc/refman/5.6/en/keywords.html>`_ , `MySQL 5.7 <https://docs.aws.amazon.com/https://dev.mysql.com/doc/refman/5.7/en/keywords.html>`_ , and `MySQL 8.0 <https://docs.aws.amazon.com/https://dev.mysql.com/doc/refman/8.0/en/keywords.html>`_ . *PostgreSQL* The name of the database to create when the Lightsail database resource is created. If this parameter isn't specified, a database named ``postgres`` is created in the database resource. Constraints: - Must contain 1-63 letters or numbers. - Must begin with a letter. Subsequent characters can be letters, underscores, or numbers (0-9). - Can't be a word reserved by the specified database engine. For more information about reserved words in PostgreSQL, see the SQL Key Words articles for `PostgreSQL 9.6 <https://docs.aws.amazon.com/https://www.postgresql.org/docs/9.6/sql-keywords-appendix.html>`_ , `PostgreSQL 10 <https://docs.aws.amazon.com/https://www.postgresql.org/docs/10/sql-keywords-appendix.html>`_ , `PostgreSQL 11 <https://docs.aws.amazon.com/https://www.postgresql.org/docs/11/sql-keywords-appendix.html>`_ , and `PostgreSQL 12 <https://docs.aws.amazon.com/https://www.postgresql.org/docs/12/sql-keywords-appendix.html>`_ .
        :param master_username: The name for the primary user. *MySQL* Constraints: - Required for MySQL. - Must be 1-16 letters or numbers. Can contain underscores. - First character must be a letter. - Can't be a reserved word for the chosen database engine. For more information about reserved words in MySQL 5.6 or 5.7, see the Keywords and Reserved Words articles for `MySQL 5.6 <https://docs.aws.amazon.com/https://dev.mysql.com/doc/refman/5.6/en/keywords.html>`_ , `MySQL 5.7 <https://docs.aws.amazon.com/https://dev.mysql.com/doc/refman/5.7/en/keywords.html>`_ , or `MySQL 8.0 <https://docs.aws.amazon.com/https://dev.mysql.com/doc/refman/8.0/en/keywords.html>`_ . *PostgreSQL* Constraints: - Required for PostgreSQL. - Must be 1-63 letters or numbers. Can contain underscores. - First character must be a letter. - Can't be a reserved word for the chosen database engine. For more information about reserved words in MySQL 5.6 or 5.7, see the Keywords and Reserved Words articles for `PostgreSQL 9.6 <https://docs.aws.amazon.com/https://www.postgresql.org/docs/9.6/sql-keywords-appendix.html>`_ , `PostgreSQL 10 <https://docs.aws.amazon.com/https://www.postgresql.org/docs/10/sql-keywords-appendix.html>`_ , `PostgreSQL 11 <https://docs.aws.amazon.com/https://www.postgresql.org/docs/11/sql-keywords-appendix.html>`_ , and `PostgreSQL 12 <https://docs.aws.amazon.com/https://www.postgresql.org/docs/12/sql-keywords-appendix.html>`_ .
        :param relational_database_blueprint_id: The blueprint ID for the database (for example, ``mysql_8_0`` ).
        :param relational_database_bundle_id: The bundle ID for the database (for example, ``medium_1_0`` ).
        :param relational_database_name: The name of the instance.
        :param availability_zone: The Availability Zone for the database.
        :param backup_retention: A Boolean value indicating whether automated backup retention is enabled for the database.
        :param ca_certificate_identifier: The certificate associated with the database.
        :param master_user_password: The password for the primary user of the database. The password can include any printable ASCII character except the following: /, ", or
        :param preferred_backup_window: The daily time range during which automated backups are created for the database (for example, ``16:00-16:30`` ).
        :param preferred_maintenance_window: The weekly time range during which system maintenance can occur for the database, formatted as follows: ``ddd:hh24:mi-ddd:hh24:mi`` . For example, ``Tue:17:00-Tue:17:30`` .
        :param publicly_accessible: A Boolean value indicating whether the database is accessible to anyone on the internet.
        :param relational_database_parameters: An array of parameters for the database.
        :param rotate_master_user_password: A Boolean value indicating whether to change the primary user password to a new, strong password generated by Lightsail . .. epigraph:: The ``RotateMasterUserPassword`` and ``MasterUserPassword`` parameters cannot be used together in the same template.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ in the *AWS CloudFormation User Guide* . .. epigraph:: The ``Value`` of ``Tags`` is optional for Lightsail resources.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__723ca4244db57b3b52ce3ed934765e22e79b12ddfe526a8f6db7bdabff702a66)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDatabaseProps(
            master_database_name=master_database_name,
            master_username=master_username,
            relational_database_blueprint_id=relational_database_blueprint_id,
            relational_database_bundle_id=relational_database_bundle_id,
            relational_database_name=relational_database_name,
            availability_zone=availability_zone,
            backup_retention=backup_retention,
            ca_certificate_identifier=ca_certificate_identifier,
            master_user_password=master_user_password,
            preferred_backup_window=preferred_backup_window,
            preferred_maintenance_window=preferred_maintenance_window,
            publicly_accessible=publicly_accessible,
            relational_database_parameters=relational_database_parameters,
            rotate_master_user_password=rotate_master_user_password,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26cc577f7a052133e01e9648ef301f73e94aaaff3448f91e3db303c34c8e1570)
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
            type_hints = typing.get_type_hints(_typecheckingstub__dedbb2a45b5731e155b72566dddda34421e74a5876a6856f0b9044eb7e422b3d)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrDatabaseArn")
    def attr_database_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the database (for example, ``arn:aws:lightsail:us-east-2:123456789101:RelationalDatabase/244ad76f-8aad-4741-809f-12345EXAMPLE`` ).

        :cloudformationAttribute: DatabaseArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDatabaseArn"))

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
    @jsii.member(jsii_name="masterDatabaseName")
    def master_database_name(self) -> builtins.str:
        '''The meaning of this parameter differs according to the database engine you use.'''
        return typing.cast(builtins.str, jsii.get(self, "masterDatabaseName"))

    @master_database_name.setter
    def master_database_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44bfee7201708398172d9c276409ca3a0edb6fd96fbb53de3c6d21f9ba38f2aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "masterDatabaseName", value)

    @builtins.property
    @jsii.member(jsii_name="masterUsername")
    def master_username(self) -> builtins.str:
        '''The name for the primary user.'''
        return typing.cast(builtins.str, jsii.get(self, "masterUsername"))

    @master_username.setter
    def master_username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7fe99b95647bc539d082d0cd9d6da52a4a6fd8065020323f840fae0e93e829e2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "masterUsername", value)

    @builtins.property
    @jsii.member(jsii_name="relationalDatabaseBlueprintId")
    def relational_database_blueprint_id(self) -> builtins.str:
        '''The blueprint ID for the database (for example, ``mysql_8_0`` ).'''
        return typing.cast(builtins.str, jsii.get(self, "relationalDatabaseBlueprintId"))

    @relational_database_blueprint_id.setter
    def relational_database_blueprint_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d98f0098b8a20a19e0698b2035c421c40d0dd6b470192acb90e2f3aafb4f8c59)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "relationalDatabaseBlueprintId", value)

    @builtins.property
    @jsii.member(jsii_name="relationalDatabaseBundleId")
    def relational_database_bundle_id(self) -> builtins.str:
        '''The bundle ID for the database (for example, ``medium_1_0`` ).'''
        return typing.cast(builtins.str, jsii.get(self, "relationalDatabaseBundleId"))

    @relational_database_bundle_id.setter
    def relational_database_bundle_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0085abf7a85860fb9463b046ff1a50df70621aad07715b1d2264f86ad3b37980)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "relationalDatabaseBundleId", value)

    @builtins.property
    @jsii.member(jsii_name="relationalDatabaseName")
    def relational_database_name(self) -> builtins.str:
        '''The name of the instance.'''
        return typing.cast(builtins.str, jsii.get(self, "relationalDatabaseName"))

    @relational_database_name.setter
    def relational_database_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fda74fa4d573fc976044231318a27a2615dff79bb54e1bf501d7f641ec177f44)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "relationalDatabaseName", value)

    @builtins.property
    @jsii.member(jsii_name="availabilityZone")
    def availability_zone(self) -> typing.Optional[builtins.str]:
        '''The Availability Zone for the database.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "availabilityZone"))

    @availability_zone.setter
    def availability_zone(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e15da72f1f0e0effee27cdac8697b6046c3b8670a5f08070180d1913992dcba5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availabilityZone", value)

    @builtins.property
    @jsii.member(jsii_name="backupRetention")
    def backup_retention(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''A Boolean value indicating whether automated backup retention is enabled for the database.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "backupRetention"))

    @backup_retention.setter
    def backup_retention(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f06245bb04a19656eaedd55d945ba9fc771b141ebea294c5f2e46a5a301a9620)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backupRetention", value)

    @builtins.property
    @jsii.member(jsii_name="caCertificateIdentifier")
    def ca_certificate_identifier(self) -> typing.Optional[builtins.str]:
        '''The certificate associated with the database.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "caCertificateIdentifier"))

    @ca_certificate_identifier.setter
    def ca_certificate_identifier(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8facd20917d86a0338c43b7be0baf738e391c887dd3f80ca4489f3f39581c750)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "caCertificateIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="masterUserPassword")
    def master_user_password(self) -> typing.Optional[builtins.str]:
        '''The password for the primary user of the database.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "masterUserPassword"))

    @master_user_password.setter
    def master_user_password(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8357b41834ed93919de4eea33fb2da779ef94976a107ee989c52c7721b5111b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "masterUserPassword", value)

    @builtins.property
    @jsii.member(jsii_name="preferredBackupWindow")
    def preferred_backup_window(self) -> typing.Optional[builtins.str]:
        '''The daily time range during which automated backups are created for the database (for example, ``16:00-16:30`` ).'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "preferredBackupWindow"))

    @preferred_backup_window.setter
    def preferred_backup_window(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd811ff9c2abe8c9dd2993c66e45e928d4f5d37ba14e6d72d593b8d46e369505)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preferredBackupWindow", value)

    @builtins.property
    @jsii.member(jsii_name="preferredMaintenanceWindow")
    def preferred_maintenance_window(self) -> typing.Optional[builtins.str]:
        '''The weekly time range during which system maintenance can occur for the database, formatted as follows: ``ddd:hh24:mi-ddd:hh24:mi`` .'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "preferredMaintenanceWindow"))

    @preferred_maintenance_window.setter
    def preferred_maintenance_window(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9094db1231b55bdfa84cdc589d3e0d5410170d587cd69d51a1edfe01ff07f862)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preferredMaintenanceWindow", value)

    @builtins.property
    @jsii.member(jsii_name="publiclyAccessible")
    def publicly_accessible(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''A Boolean value indicating whether the database is accessible to anyone on the internet.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "publiclyAccessible"))

    @publicly_accessible.setter
    def publicly_accessible(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8197f292fce266aba628a142dec258c98e7a25fed22896e06e1a90c24a7ba544)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publiclyAccessible", value)

    @builtins.property
    @jsii.member(jsii_name="relationalDatabaseParameters")
    def relational_database_parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDatabase.RelationalDatabaseParameterProperty"]]]]:
        '''An array of parameters for the database.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDatabase.RelationalDatabaseParameterProperty"]]]], jsii.get(self, "relationalDatabaseParameters"))

    @relational_database_parameters.setter
    def relational_database_parameters(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDatabase.RelationalDatabaseParameterProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c96ad668b58f33187ed56194efffce27de109fd0767bcd5c1f2484c5bee18d56)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "relationalDatabaseParameters", value)

    @builtins.property
    @jsii.member(jsii_name="rotateMasterUserPassword")
    def rotate_master_user_password(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''A Boolean value indicating whether to change the primary user password to a new, strong password generated by Lightsail .'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "rotateMasterUserPassword"))

    @rotate_master_user_password.setter
    def rotate_master_user_password(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__091d540f8b782064900c5e22fafb94086a4be8e774d1ca1e28d1034f980c1e78)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rotateMasterUserPassword", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__742edfcb29bb69911299a631b46a0f26a5025e76d10c496b6e66e28bb86874ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lightsail.CfnDatabase.RelationalDatabaseParameterProperty",
        jsii_struct_bases=[],
        name_mapping={
            "allowed_values": "allowedValues",
            "apply_method": "applyMethod",
            "apply_type": "applyType",
            "data_type": "dataType",
            "description": "description",
            "is_modifiable": "isModifiable",
            "parameter_name": "parameterName",
            "parameter_value": "parameterValue",
        },
    )
    class RelationalDatabaseParameterProperty:
        def __init__(
            self,
            *,
            allowed_values: typing.Optional[builtins.str] = None,
            apply_method: typing.Optional[builtins.str] = None,
            apply_type: typing.Optional[builtins.str] = None,
            data_type: typing.Optional[builtins.str] = None,
            description: typing.Optional[builtins.str] = None,
            is_modifiable: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            parameter_name: typing.Optional[builtins.str] = None,
            parameter_value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''``RelationalDatabaseParameter`` is a property of the `AWS::Lightsail::Database <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html>`_ resource. It describes parameters for the database.

            :param allowed_values: The valid range of values for the parameter.
            :param apply_method: Indicates when parameter updates are applied. Can be ``immediate`` or ``pending-reboot`` .
            :param apply_type: Specifies the engine-specific parameter type.
            :param data_type: The valid data type of the parameter.
            :param description: A description of the parameter.
            :param is_modifiable: A Boolean value indicating whether the parameter can be modified.
            :param parameter_name: The name of the parameter.
            :param parameter_value: The value for the parameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-database-relationaldatabaseparameter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lightsail as lightsail
                
                relational_database_parameter_property = lightsail.CfnDatabase.RelationalDatabaseParameterProperty(
                    allowed_values="allowedValues",
                    apply_method="applyMethod",
                    apply_type="applyType",
                    data_type="dataType",
                    description="description",
                    is_modifiable=False,
                    parameter_name="parameterName",
                    parameter_value="parameterValue"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2decf56e5d7a797902c80fb0a4f07e403ddbf32e21ae82ca0276101029f789f8)
                check_type(argname="argument allowed_values", value=allowed_values, expected_type=type_hints["allowed_values"])
                check_type(argname="argument apply_method", value=apply_method, expected_type=type_hints["apply_method"])
                check_type(argname="argument apply_type", value=apply_type, expected_type=type_hints["apply_type"])
                check_type(argname="argument data_type", value=data_type, expected_type=type_hints["data_type"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument is_modifiable", value=is_modifiable, expected_type=type_hints["is_modifiable"])
                check_type(argname="argument parameter_name", value=parameter_name, expected_type=type_hints["parameter_name"])
                check_type(argname="argument parameter_value", value=parameter_value, expected_type=type_hints["parameter_value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if allowed_values is not None:
                self._values["allowed_values"] = allowed_values
            if apply_method is not None:
                self._values["apply_method"] = apply_method
            if apply_type is not None:
                self._values["apply_type"] = apply_type
            if data_type is not None:
                self._values["data_type"] = data_type
            if description is not None:
                self._values["description"] = description
            if is_modifiable is not None:
                self._values["is_modifiable"] = is_modifiable
            if parameter_name is not None:
                self._values["parameter_name"] = parameter_name
            if parameter_value is not None:
                self._values["parameter_value"] = parameter_value

        @builtins.property
        def allowed_values(self) -> typing.Optional[builtins.str]:
            '''The valid range of values for the parameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-database-relationaldatabaseparameter.html#cfn-lightsail-database-relationaldatabaseparameter-allowedvalues
            '''
            result = self._values.get("allowed_values")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def apply_method(self) -> typing.Optional[builtins.str]:
            '''Indicates when parameter updates are applied.

            Can be ``immediate`` or ``pending-reboot`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-database-relationaldatabaseparameter.html#cfn-lightsail-database-relationaldatabaseparameter-applymethod
            '''
            result = self._values.get("apply_method")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def apply_type(self) -> typing.Optional[builtins.str]:
            '''Specifies the engine-specific parameter type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-database-relationaldatabaseparameter.html#cfn-lightsail-database-relationaldatabaseparameter-applytype
            '''
            result = self._values.get("apply_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def data_type(self) -> typing.Optional[builtins.str]:
            '''The valid data type of the parameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-database-relationaldatabaseparameter.html#cfn-lightsail-database-relationaldatabaseparameter-datatype
            '''
            result = self._values.get("data_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''A description of the parameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-database-relationaldatabaseparameter.html#cfn-lightsail-database-relationaldatabaseparameter-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def is_modifiable(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''A Boolean value indicating whether the parameter can be modified.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-database-relationaldatabaseparameter.html#cfn-lightsail-database-relationaldatabaseparameter-ismodifiable
            '''
            result = self._values.get("is_modifiable")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def parameter_name(self) -> typing.Optional[builtins.str]:
            '''The name of the parameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-database-relationaldatabaseparameter.html#cfn-lightsail-database-relationaldatabaseparameter-parametername
            '''
            result = self._values.get("parameter_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def parameter_value(self) -> typing.Optional[builtins.str]:
            '''The value for the parameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-database-relationaldatabaseparameter.html#cfn-lightsail-database-relationaldatabaseparameter-parametervalue
            '''
            result = self._values.get("parameter_value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RelationalDatabaseParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_lightsail.CfnDatabaseProps",
    jsii_struct_bases=[],
    name_mapping={
        "master_database_name": "masterDatabaseName",
        "master_username": "masterUsername",
        "relational_database_blueprint_id": "relationalDatabaseBlueprintId",
        "relational_database_bundle_id": "relationalDatabaseBundleId",
        "relational_database_name": "relationalDatabaseName",
        "availability_zone": "availabilityZone",
        "backup_retention": "backupRetention",
        "ca_certificate_identifier": "caCertificateIdentifier",
        "master_user_password": "masterUserPassword",
        "preferred_backup_window": "preferredBackupWindow",
        "preferred_maintenance_window": "preferredMaintenanceWindow",
        "publicly_accessible": "publiclyAccessible",
        "relational_database_parameters": "relationalDatabaseParameters",
        "rotate_master_user_password": "rotateMasterUserPassword",
        "tags": "tags",
    },
)
class CfnDatabaseProps:
    def __init__(
        self,
        *,
        master_database_name: builtins.str,
        master_username: builtins.str,
        relational_database_blueprint_id: builtins.str,
        relational_database_bundle_id: builtins.str,
        relational_database_name: builtins.str,
        availability_zone: typing.Optional[builtins.str] = None,
        backup_retention: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ca_certificate_identifier: typing.Optional[builtins.str] = None,
        master_user_password: typing.Optional[builtins.str] = None,
        preferred_backup_window: typing.Optional[builtins.str] = None,
        preferred_maintenance_window: typing.Optional[builtins.str] = None,
        publicly_accessible: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        relational_database_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDatabase.RelationalDatabaseParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        rotate_master_user_password: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDatabase``.

        :param master_database_name: The meaning of this parameter differs according to the database engine you use. *MySQL* The name of the database to create when the Lightsail database resource is created. If this parameter isn't specified, no database is created in the database resource. Constraints: - Must contain 1-64 letters or numbers. - Must begin with a letter. Subsequent characters can be letters, underscores, or numbers (0-9). - Can't be a word reserved by the specified database engine. For more information about reserved words in MySQL, see the Keywords and Reserved Words articles for `MySQL 5.6 <https://docs.aws.amazon.com/https://dev.mysql.com/doc/refman/5.6/en/keywords.html>`_ , `MySQL 5.7 <https://docs.aws.amazon.com/https://dev.mysql.com/doc/refman/5.7/en/keywords.html>`_ , and `MySQL 8.0 <https://docs.aws.amazon.com/https://dev.mysql.com/doc/refman/8.0/en/keywords.html>`_ . *PostgreSQL* The name of the database to create when the Lightsail database resource is created. If this parameter isn't specified, a database named ``postgres`` is created in the database resource. Constraints: - Must contain 1-63 letters or numbers. - Must begin with a letter. Subsequent characters can be letters, underscores, or numbers (0-9). - Can't be a word reserved by the specified database engine. For more information about reserved words in PostgreSQL, see the SQL Key Words articles for `PostgreSQL 9.6 <https://docs.aws.amazon.com/https://www.postgresql.org/docs/9.6/sql-keywords-appendix.html>`_ , `PostgreSQL 10 <https://docs.aws.amazon.com/https://www.postgresql.org/docs/10/sql-keywords-appendix.html>`_ , `PostgreSQL 11 <https://docs.aws.amazon.com/https://www.postgresql.org/docs/11/sql-keywords-appendix.html>`_ , and `PostgreSQL 12 <https://docs.aws.amazon.com/https://www.postgresql.org/docs/12/sql-keywords-appendix.html>`_ .
        :param master_username: The name for the primary user. *MySQL* Constraints: - Required for MySQL. - Must be 1-16 letters or numbers. Can contain underscores. - First character must be a letter. - Can't be a reserved word for the chosen database engine. For more information about reserved words in MySQL 5.6 or 5.7, see the Keywords and Reserved Words articles for `MySQL 5.6 <https://docs.aws.amazon.com/https://dev.mysql.com/doc/refman/5.6/en/keywords.html>`_ , `MySQL 5.7 <https://docs.aws.amazon.com/https://dev.mysql.com/doc/refman/5.7/en/keywords.html>`_ , or `MySQL 8.0 <https://docs.aws.amazon.com/https://dev.mysql.com/doc/refman/8.0/en/keywords.html>`_ . *PostgreSQL* Constraints: - Required for PostgreSQL. - Must be 1-63 letters or numbers. Can contain underscores. - First character must be a letter. - Can't be a reserved word for the chosen database engine. For more information about reserved words in MySQL 5.6 or 5.7, see the Keywords and Reserved Words articles for `PostgreSQL 9.6 <https://docs.aws.amazon.com/https://www.postgresql.org/docs/9.6/sql-keywords-appendix.html>`_ , `PostgreSQL 10 <https://docs.aws.amazon.com/https://www.postgresql.org/docs/10/sql-keywords-appendix.html>`_ , `PostgreSQL 11 <https://docs.aws.amazon.com/https://www.postgresql.org/docs/11/sql-keywords-appendix.html>`_ , and `PostgreSQL 12 <https://docs.aws.amazon.com/https://www.postgresql.org/docs/12/sql-keywords-appendix.html>`_ .
        :param relational_database_blueprint_id: The blueprint ID for the database (for example, ``mysql_8_0`` ).
        :param relational_database_bundle_id: The bundle ID for the database (for example, ``medium_1_0`` ).
        :param relational_database_name: The name of the instance.
        :param availability_zone: The Availability Zone for the database.
        :param backup_retention: A Boolean value indicating whether automated backup retention is enabled for the database.
        :param ca_certificate_identifier: The certificate associated with the database.
        :param master_user_password: The password for the primary user of the database. The password can include any printable ASCII character except the following: /, ", or
        :param preferred_backup_window: The daily time range during which automated backups are created for the database (for example, ``16:00-16:30`` ).
        :param preferred_maintenance_window: The weekly time range during which system maintenance can occur for the database, formatted as follows: ``ddd:hh24:mi-ddd:hh24:mi`` . For example, ``Tue:17:00-Tue:17:30`` .
        :param publicly_accessible: A Boolean value indicating whether the database is accessible to anyone on the internet.
        :param relational_database_parameters: An array of parameters for the database.
        :param rotate_master_user_password: A Boolean value indicating whether to change the primary user password to a new, strong password generated by Lightsail . .. epigraph:: The ``RotateMasterUserPassword`` and ``MasterUserPassword`` parameters cannot be used together in the same template.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ in the *AWS CloudFormation User Guide* . .. epigraph:: The ``Value`` of ``Tags`` is optional for Lightsail resources.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_lightsail as lightsail
            
            cfn_database_props = lightsail.CfnDatabaseProps(
                master_database_name="masterDatabaseName",
                master_username="masterUsername",
                relational_database_blueprint_id="relationalDatabaseBlueprintId",
                relational_database_bundle_id="relationalDatabaseBundleId",
                relational_database_name="relationalDatabaseName",
            
                # the properties below are optional
                availability_zone="availabilityZone",
                backup_retention=False,
                ca_certificate_identifier="caCertificateIdentifier",
                master_user_password="masterUserPassword",
                preferred_backup_window="preferredBackupWindow",
                preferred_maintenance_window="preferredMaintenanceWindow",
                publicly_accessible=False,
                relational_database_parameters=[lightsail.CfnDatabase.RelationalDatabaseParameterProperty(
                    allowed_values="allowedValues",
                    apply_method="applyMethod",
                    apply_type="applyType",
                    data_type="dataType",
                    description="description",
                    is_modifiable=False,
                    parameter_name="parameterName",
                    parameter_value="parameterValue"
                )],
                rotate_master_user_password=False,
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54feeda1af4cae8d2e40338b603c7ff96c3a0d88fba114bb9b9549eac1795ac3)
            check_type(argname="argument master_database_name", value=master_database_name, expected_type=type_hints["master_database_name"])
            check_type(argname="argument master_username", value=master_username, expected_type=type_hints["master_username"])
            check_type(argname="argument relational_database_blueprint_id", value=relational_database_blueprint_id, expected_type=type_hints["relational_database_blueprint_id"])
            check_type(argname="argument relational_database_bundle_id", value=relational_database_bundle_id, expected_type=type_hints["relational_database_bundle_id"])
            check_type(argname="argument relational_database_name", value=relational_database_name, expected_type=type_hints["relational_database_name"])
            check_type(argname="argument availability_zone", value=availability_zone, expected_type=type_hints["availability_zone"])
            check_type(argname="argument backup_retention", value=backup_retention, expected_type=type_hints["backup_retention"])
            check_type(argname="argument ca_certificate_identifier", value=ca_certificate_identifier, expected_type=type_hints["ca_certificate_identifier"])
            check_type(argname="argument master_user_password", value=master_user_password, expected_type=type_hints["master_user_password"])
            check_type(argname="argument preferred_backup_window", value=preferred_backup_window, expected_type=type_hints["preferred_backup_window"])
            check_type(argname="argument preferred_maintenance_window", value=preferred_maintenance_window, expected_type=type_hints["preferred_maintenance_window"])
            check_type(argname="argument publicly_accessible", value=publicly_accessible, expected_type=type_hints["publicly_accessible"])
            check_type(argname="argument relational_database_parameters", value=relational_database_parameters, expected_type=type_hints["relational_database_parameters"])
            check_type(argname="argument rotate_master_user_password", value=rotate_master_user_password, expected_type=type_hints["rotate_master_user_password"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "master_database_name": master_database_name,
            "master_username": master_username,
            "relational_database_blueprint_id": relational_database_blueprint_id,
            "relational_database_bundle_id": relational_database_bundle_id,
            "relational_database_name": relational_database_name,
        }
        if availability_zone is not None:
            self._values["availability_zone"] = availability_zone
        if backup_retention is not None:
            self._values["backup_retention"] = backup_retention
        if ca_certificate_identifier is not None:
            self._values["ca_certificate_identifier"] = ca_certificate_identifier
        if master_user_password is not None:
            self._values["master_user_password"] = master_user_password
        if preferred_backup_window is not None:
            self._values["preferred_backup_window"] = preferred_backup_window
        if preferred_maintenance_window is not None:
            self._values["preferred_maintenance_window"] = preferred_maintenance_window
        if publicly_accessible is not None:
            self._values["publicly_accessible"] = publicly_accessible
        if relational_database_parameters is not None:
            self._values["relational_database_parameters"] = relational_database_parameters
        if rotate_master_user_password is not None:
            self._values["rotate_master_user_password"] = rotate_master_user_password
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def master_database_name(self) -> builtins.str:
        '''The meaning of this parameter differs according to the database engine you use.

        *MySQL*

        The name of the database to create when the Lightsail database resource is created. If this parameter isn't specified, no database is created in the database resource.

        Constraints:

        - Must contain 1-64 letters or numbers.
        - Must begin with a letter. Subsequent characters can be letters, underscores, or numbers (0-9).
        - Can't be a word reserved by the specified database engine.

        For more information about reserved words in MySQL, see the Keywords and Reserved Words articles for `MySQL 5.6 <https://docs.aws.amazon.com/https://dev.mysql.com/doc/refman/5.6/en/keywords.html>`_ , `MySQL 5.7 <https://docs.aws.amazon.com/https://dev.mysql.com/doc/refman/5.7/en/keywords.html>`_ , and `MySQL 8.0 <https://docs.aws.amazon.com/https://dev.mysql.com/doc/refman/8.0/en/keywords.html>`_ .

        *PostgreSQL*

        The name of the database to create when the Lightsail database resource is created. If this parameter isn't specified, a database named ``postgres`` is created in the database resource.

        Constraints:

        - Must contain 1-63 letters or numbers.
        - Must begin with a letter. Subsequent characters can be letters, underscores, or numbers (0-9).
        - Can't be a word reserved by the specified database engine.

        For more information about reserved words in PostgreSQL, see the SQL Key Words articles for `PostgreSQL 9.6 <https://docs.aws.amazon.com/https://www.postgresql.org/docs/9.6/sql-keywords-appendix.html>`_ , `PostgreSQL 10 <https://docs.aws.amazon.com/https://www.postgresql.org/docs/10/sql-keywords-appendix.html>`_ , `PostgreSQL 11 <https://docs.aws.amazon.com/https://www.postgresql.org/docs/11/sql-keywords-appendix.html>`_ , and `PostgreSQL 12 <https://docs.aws.amazon.com/https://www.postgresql.org/docs/12/sql-keywords-appendix.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-masterdatabasename
        '''
        result = self._values.get("master_database_name")
        assert result is not None, "Required property 'master_database_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def master_username(self) -> builtins.str:
        '''The name for the primary user.

        *MySQL*

        Constraints:

        - Required for MySQL.
        - Must be 1-16 letters or numbers. Can contain underscores.
        - First character must be a letter.
        - Can't be a reserved word for the chosen database engine.

        For more information about reserved words in MySQL 5.6 or 5.7, see the Keywords and Reserved Words articles for `MySQL 5.6 <https://docs.aws.amazon.com/https://dev.mysql.com/doc/refman/5.6/en/keywords.html>`_ , `MySQL 5.7 <https://docs.aws.amazon.com/https://dev.mysql.com/doc/refman/5.7/en/keywords.html>`_ , or `MySQL 8.0 <https://docs.aws.amazon.com/https://dev.mysql.com/doc/refman/8.0/en/keywords.html>`_ .

        *PostgreSQL*

        Constraints:

        - Required for PostgreSQL.
        - Must be 1-63 letters or numbers. Can contain underscores.
        - First character must be a letter.
        - Can't be a reserved word for the chosen database engine.

        For more information about reserved words in MySQL 5.6 or 5.7, see the Keywords and Reserved Words articles for `PostgreSQL 9.6 <https://docs.aws.amazon.com/https://www.postgresql.org/docs/9.6/sql-keywords-appendix.html>`_ , `PostgreSQL 10 <https://docs.aws.amazon.com/https://www.postgresql.org/docs/10/sql-keywords-appendix.html>`_ , `PostgreSQL 11 <https://docs.aws.amazon.com/https://www.postgresql.org/docs/11/sql-keywords-appendix.html>`_ , and `PostgreSQL 12 <https://docs.aws.amazon.com/https://www.postgresql.org/docs/12/sql-keywords-appendix.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-masterusername
        '''
        result = self._values.get("master_username")
        assert result is not None, "Required property 'master_username' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def relational_database_blueprint_id(self) -> builtins.str:
        '''The blueprint ID for the database (for example, ``mysql_8_0`` ).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-relationaldatabaseblueprintid
        '''
        result = self._values.get("relational_database_blueprint_id")
        assert result is not None, "Required property 'relational_database_blueprint_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def relational_database_bundle_id(self) -> builtins.str:
        '''The bundle ID for the database (for example, ``medium_1_0`` ).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-relationaldatabasebundleid
        '''
        result = self._values.get("relational_database_bundle_id")
        assert result is not None, "Required property 'relational_database_bundle_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def relational_database_name(self) -> builtins.str:
        '''The name of the instance.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-relationaldatabasename
        '''
        result = self._values.get("relational_database_name")
        assert result is not None, "Required property 'relational_database_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def availability_zone(self) -> typing.Optional[builtins.str]:
        '''The Availability Zone for the database.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-availabilityzone
        '''
        result = self._values.get("availability_zone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def backup_retention(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''A Boolean value indicating whether automated backup retention is enabled for the database.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-backupretention
        '''
        result = self._values.get("backup_retention")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def ca_certificate_identifier(self) -> typing.Optional[builtins.str]:
        '''The certificate associated with the database.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-cacertificateidentifier
        '''
        result = self._values.get("ca_certificate_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def master_user_password(self) -> typing.Optional[builtins.str]:
        '''The password for the primary user of the database.

        The password can include any printable ASCII character except the following: /, ", or

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-masteruserpassword
        ::

        . It cannot contain spaces.
        .. epigraph::

        The ``MasterUserPassword`` and ``RotateMasterUserPassword`` parameters cannot be used together in the same template.

        *MySQL*

        Constraints: Must contain 8-41 characters.

        *PostgreSQL*

        Constraints: Must contain 8-128 characters.
        '''
        result = self._values.get("master_user_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def preferred_backup_window(self) -> typing.Optional[builtins.str]:
        '''The daily time range during which automated backups are created for the database (for example, ``16:00-16:30`` ).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-preferredbackupwindow
        '''
        result = self._values.get("preferred_backup_window")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def preferred_maintenance_window(self) -> typing.Optional[builtins.str]:
        '''The weekly time range during which system maintenance can occur for the database, formatted as follows: ``ddd:hh24:mi-ddd:hh24:mi`` .

        For example, ``Tue:17:00-Tue:17:30`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-preferredmaintenancewindow
        '''
        result = self._values.get("preferred_maintenance_window")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def publicly_accessible(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''A Boolean value indicating whether the database is accessible to anyone on the internet.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-publiclyaccessible
        '''
        result = self._values.get("publicly_accessible")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def relational_database_parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDatabase.RelationalDatabaseParameterProperty]]]]:
        '''An array of parameters for the database.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-relationaldatabaseparameters
        '''
        result = self._values.get("relational_database_parameters")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDatabase.RelationalDatabaseParameterProperty]]]], result)

    @builtins.property
    def rotate_master_user_password(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''A Boolean value indicating whether to change the primary user password to a new, strong password generated by Lightsail .

        .. epigraph::

           The ``RotateMasterUserPassword`` and ``MasterUserPassword`` parameters cannot be used together in the same template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-rotatemasteruserpassword
        '''
        result = self._values.get("rotate_master_user_password")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ in the *AWS CloudFormation User Guide* .
        .. epigraph::

           The ``Value`` of ``Tags`` is optional for Lightsail resources.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDatabaseProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnDisk(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_lightsail.CfnDisk",
):
    '''The ``AWS::Lightsail::Disk`` resource specifies a disk that can be attached to an Amazon Lightsail instance that is in the same AWS Region and Availability Zone.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-disk.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_lightsail as lightsail
        
        cfn_disk = lightsail.CfnDisk(self, "MyCfnDisk",
            disk_name="diskName",
            size_in_gb=123,
        
            # the properties below are optional
            add_ons=[lightsail.CfnDisk.AddOnProperty(
                add_on_type="addOnType",
        
                # the properties below are optional
                auto_snapshot_add_on_request=lightsail.CfnDisk.AutoSnapshotAddOnProperty(
                    snapshot_time_of_day="snapshotTimeOfDay"
                ),
                status="status"
            )],
            availability_zone="availabilityZone",
            location=lightsail.CfnDisk.LocationProperty(
                availability_zone="availabilityZone",
                region_name="regionName"
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
        disk_name: builtins.str,
        size_in_gb: jsii.Number,
        add_ons: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDisk.AddOnProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        availability_zone: typing.Optional[builtins.str] = None,
        location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDisk.LocationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param disk_name: The name of the disk.
        :param size_in_gb: The size of the disk in GB.
        :param add_ons: An array of add-ons for the disk. .. epigraph:: If the disk has an add-on enabled when performing a delete disk request, the add-on is automatically disabled before the disk is deleted.
        :param availability_zone: The AWS Region and Availability Zone location for the disk (for example, ``us-east-1a`` ).
        :param location: Location of a resource.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ in the *AWS CloudFormation User Guide* . .. epigraph:: The ``Value`` of ``Tags`` is optional for Lightsail resources.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80a3acf97fc9eaa657a04acbab637a1d0adb76d1178dbca352280131a1e64601)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDiskProps(
            disk_name=disk_name,
            size_in_gb=size_in_gb,
            add_ons=add_ons,
            availability_zone=availability_zone,
            location=location,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea4f169865a73e68a220949579e4971d18e071074b75df08ffa1bf72dedb580c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3fe5653cbcc9bffb3186bb057c3356cf16999f60677b11a964bc4dbaa77b44b4)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAttachedTo")
    def attr_attached_to(self) -> builtins.str:
        '''The instance to which the disk is attached.

        :cloudformationAttribute: AttachedTo
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAttachedTo"))

    @builtins.property
    @jsii.member(jsii_name="attrAttachmentState")
    def attr_attachment_state(self) -> builtins.str:
        '''(Deprecated) The attachment state of the disk.

        .. epigraph::

           In releases prior to November 14, 2017, this parameter returned ``attached`` for system disks in the API response. It is now deprecated, but still included in the response. Use ``isAttached`` instead.

        :cloudformationAttribute: AttachmentState
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAttachmentState"))

    @builtins.property
    @jsii.member(jsii_name="attrDiskArn")
    def attr_disk_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the disk.

        :cloudformationAttribute: DiskArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDiskArn"))

    @builtins.property
    @jsii.member(jsii_name="attrIops")
    def attr_iops(self) -> jsii.Number:
        '''The input/output operations per second (IOPS) of the disk.

        :cloudformationAttribute: Iops
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrIops"))

    @builtins.property
    @jsii.member(jsii_name="attrIsAttached")
    def attr_is_attached(self) -> _IResolvable_da3f097b:
        '''A Boolean value indicating whether the disk is attached to an instance.

        :cloudformationAttribute: IsAttached
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrIsAttached"))

    @builtins.property
    @jsii.member(jsii_name="attrLocationAvailabilityZone")
    def attr_location_availability_zone(self) -> builtins.str:
        '''The Availability Zone in which to create your disk.

        Use the following format: us-east-2a (case sensitive). Be sure to add the include Availability Zones parameter to your request.

        :cloudformationAttribute: Location.AvailabilityZone
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLocationAvailabilityZone"))

    @builtins.property
    @jsii.member(jsii_name="attrLocationRegionName")
    def attr_location_region_name(self) -> builtins.str:
        '''The Region Name in which to create your disk.

        :cloudformationAttribute: Location.RegionName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLocationRegionName"))

    @builtins.property
    @jsii.member(jsii_name="attrPath")
    def attr_path(self) -> builtins.str:
        '''The path of the disk.

        :cloudformationAttribute: Path
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPath"))

    @builtins.property
    @jsii.member(jsii_name="attrResourceType")
    def attr_resource_type(self) -> builtins.str:
        '''The resource type of the disk (for example, ``Disk`` ).

        :cloudformationAttribute: ResourceType
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrResourceType"))

    @builtins.property
    @jsii.member(jsii_name="attrState")
    def attr_state(self) -> builtins.str:
        '''The state of the disk (for example, ``in-use`` ).

        :cloudformationAttribute: State
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrState"))

    @builtins.property
    @jsii.member(jsii_name="attrSupportCode")
    def attr_support_code(self) -> builtins.str:
        '''The support code of the disk.

        Include this code in your email to support when you have questions about a disk or another resource in Lightsail . This code helps our support team to look up your Lightsail information.

        :cloudformationAttribute: SupportCode
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSupportCode"))

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
    @jsii.member(jsii_name="diskName")
    def disk_name(self) -> builtins.str:
        '''The name of the disk.'''
        return typing.cast(builtins.str, jsii.get(self, "diskName"))

    @disk_name.setter
    def disk_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca648103138b58ef4b28158de4e9077eea50974ea860de6e2cafaf7c1ea68497)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diskName", value)

    @builtins.property
    @jsii.member(jsii_name="sizeInGb")
    def size_in_gb(self) -> jsii.Number:
        '''The size of the disk in GB.'''
        return typing.cast(jsii.Number, jsii.get(self, "sizeInGb"))

    @size_in_gb.setter
    def size_in_gb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc1d51effcf0ec678cadc317f7c644119757d22b11d365f942f6e5869972b495)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sizeInGb", value)

    @builtins.property
    @jsii.member(jsii_name="addOns")
    def add_ons(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDisk.AddOnProperty"]]]]:
        '''An array of add-ons for the disk.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDisk.AddOnProperty"]]]], jsii.get(self, "addOns"))

    @add_ons.setter
    def add_ons(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDisk.AddOnProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6bb18dc1c40065ba9615024ffd4c8a5bba5665cf77f22e9fe23067d7b1e0269b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "addOns", value)

    @builtins.property
    @jsii.member(jsii_name="availabilityZone")
    def availability_zone(self) -> typing.Optional[builtins.str]:
        '''The AWS Region and Availability Zone location for the disk (for example, ``us-east-1a`` ).'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "availabilityZone"))

    @availability_zone.setter
    def availability_zone(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a929e131601b77b843b584668029130493ce602b0f8f3773bde8e91acbdc46f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availabilityZone", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDisk.LocationProperty"]]:
        '''Location of a resource.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDisk.LocationProperty"]], jsii.get(self, "location"))

    @location.setter
    def location(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDisk.LocationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ad247d59530c9822b391b02d714793c6faf5b661335e33a60f755e84cac854e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8d9f7c7c9bb1fcb533d5c13ea1040c3fcc188448ff6c785a662ccf8e4342f96)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lightsail.CfnDisk.AddOnProperty",
        jsii_struct_bases=[],
        name_mapping={
            "add_on_type": "addOnType",
            "auto_snapshot_add_on_request": "autoSnapshotAddOnRequest",
            "status": "status",
        },
    )
    class AddOnProperty:
        def __init__(
            self,
            *,
            add_on_type: builtins.str,
            auto_snapshot_add_on_request: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDisk.AutoSnapshotAddOnProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            status: typing.Optional[builtins.str] = None,
        ) -> None:
            '''``AddOn`` is a property of the `AWS::Lightsail::Disk <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-disk.html>`_ resource. It describes the add-ons for a disk.

            :param add_on_type: The add-on type (for example, ``AutoSnapshot`` ). .. epigraph:: ``AutoSnapshot`` is the only add-on that can be enabled for a disk.
            :param auto_snapshot_add_on_request: The parameters for the automatic snapshot add-on, such as the daily time when an automatic snapshot will be created.
            :param status: The status of the add-on. Valid Values: ``Enabled`` | ``Disabled``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-disk-addon.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lightsail as lightsail
                
                add_on_property = lightsail.CfnDisk.AddOnProperty(
                    add_on_type="addOnType",
                
                    # the properties below are optional
                    auto_snapshot_add_on_request=lightsail.CfnDisk.AutoSnapshotAddOnProperty(
                        snapshot_time_of_day="snapshotTimeOfDay"
                    ),
                    status="status"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d6dca6ef6ad37884857f6dd11bf04fa1d4d068cc3716b82e18bc18b6f614d3f3)
                check_type(argname="argument add_on_type", value=add_on_type, expected_type=type_hints["add_on_type"])
                check_type(argname="argument auto_snapshot_add_on_request", value=auto_snapshot_add_on_request, expected_type=type_hints["auto_snapshot_add_on_request"])
                check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "add_on_type": add_on_type,
            }
            if auto_snapshot_add_on_request is not None:
                self._values["auto_snapshot_add_on_request"] = auto_snapshot_add_on_request
            if status is not None:
                self._values["status"] = status

        @builtins.property
        def add_on_type(self) -> builtins.str:
            '''The add-on type (for example, ``AutoSnapshot`` ).

            .. epigraph::

               ``AutoSnapshot`` is the only add-on that can be enabled for a disk.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-disk-addon.html#cfn-lightsail-disk-addon-addontype
            '''
            result = self._values.get("add_on_type")
            assert result is not None, "Required property 'add_on_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def auto_snapshot_add_on_request(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDisk.AutoSnapshotAddOnProperty"]]:
            '''The parameters for the automatic snapshot add-on, such as the daily time when an automatic snapshot will be created.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-disk-addon.html#cfn-lightsail-disk-addon-autosnapshotaddonrequest
            '''
            result = self._values.get("auto_snapshot_add_on_request")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDisk.AutoSnapshotAddOnProperty"]], result)

        @builtins.property
        def status(self) -> typing.Optional[builtins.str]:
            '''The status of the add-on.

            Valid Values: ``Enabled`` | ``Disabled``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-disk-addon.html#cfn-lightsail-disk-addon-status
            '''
            result = self._values.get("status")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AddOnProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lightsail.CfnDisk.AutoSnapshotAddOnProperty",
        jsii_struct_bases=[],
        name_mapping={"snapshot_time_of_day": "snapshotTimeOfDay"},
    )
    class AutoSnapshotAddOnProperty:
        def __init__(
            self,
            *,
            snapshot_time_of_day: typing.Optional[builtins.str] = None,
        ) -> None:
            '''``AutoSnapshotAddOn`` is a property of the `AddOn <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-disk-addon.html>`_ property. It describes the automatic snapshot add-on for a disk.

            :param snapshot_time_of_day: The daily time when an automatic snapshot will be created. Constraints: - Must be in ``HH:00`` format, and in an hourly increment. - Specified in Coordinated Universal Time (UTC). - The snapshot will be automatically created between the time specified and up to 45 minutes after.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-disk-autosnapshotaddon.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lightsail as lightsail
                
                auto_snapshot_add_on_property = lightsail.CfnDisk.AutoSnapshotAddOnProperty(
                    snapshot_time_of_day="snapshotTimeOfDay"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a8fac9a027dbef91fb6dcd3972cd2f428689708e722e631dd37ac710dc2907d7)
                check_type(argname="argument snapshot_time_of_day", value=snapshot_time_of_day, expected_type=type_hints["snapshot_time_of_day"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if snapshot_time_of_day is not None:
                self._values["snapshot_time_of_day"] = snapshot_time_of_day

        @builtins.property
        def snapshot_time_of_day(self) -> typing.Optional[builtins.str]:
            '''The daily time when an automatic snapshot will be created.

            Constraints:

            - Must be in ``HH:00`` format, and in an hourly increment.
            - Specified in Coordinated Universal Time (UTC).
            - The snapshot will be automatically created between the time specified and up to 45 minutes after.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-disk-autosnapshotaddon.html#cfn-lightsail-disk-autosnapshotaddon-snapshottimeofday
            '''
            result = self._values.get("snapshot_time_of_day")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AutoSnapshotAddOnProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lightsail.CfnDisk.LocationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "availability_zone": "availabilityZone",
            "region_name": "regionName",
        },
    )
    class LocationProperty:
        def __init__(
            self,
            *,
            availability_zone: typing.Optional[builtins.str] = None,
            region_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Location of a resource.

            :param availability_zone: The Availability Zone in which to create your disk. Use the following format: us-east-2a (case sensitive). Be sure to add the include Availability Zones parameter to your request.
            :param region_name: The Region Name in which to create your disk.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-disk-location.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lightsail as lightsail
                
                location_property = lightsail.CfnDisk.LocationProperty(
                    availability_zone="availabilityZone",
                    region_name="regionName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a7cd90525af9bd1ae5058a25d04444364be64fc46bff0d7ac63c54d5a6441c33)
                check_type(argname="argument availability_zone", value=availability_zone, expected_type=type_hints["availability_zone"])
                check_type(argname="argument region_name", value=region_name, expected_type=type_hints["region_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if availability_zone is not None:
                self._values["availability_zone"] = availability_zone
            if region_name is not None:
                self._values["region_name"] = region_name

        @builtins.property
        def availability_zone(self) -> typing.Optional[builtins.str]:
            '''The Availability Zone in which to create your disk.

            Use the following format: us-east-2a (case sensitive). Be sure to add the include Availability Zones parameter to your request.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-disk-location.html#cfn-lightsail-disk-location-availabilityzone
            '''
            result = self._values.get("availability_zone")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def region_name(self) -> typing.Optional[builtins.str]:
            '''The Region Name in which to create your disk.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-disk-location.html#cfn-lightsail-disk-location-regionname
            '''
            result = self._values.get("region_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_lightsail.CfnDiskProps",
    jsii_struct_bases=[],
    name_mapping={
        "disk_name": "diskName",
        "size_in_gb": "sizeInGb",
        "add_ons": "addOns",
        "availability_zone": "availabilityZone",
        "location": "location",
        "tags": "tags",
    },
)
class CfnDiskProps:
    def __init__(
        self,
        *,
        disk_name: builtins.str,
        size_in_gb: jsii.Number,
        add_ons: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDisk.AddOnProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        availability_zone: typing.Optional[builtins.str] = None,
        location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDisk.LocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDisk``.

        :param disk_name: The name of the disk.
        :param size_in_gb: The size of the disk in GB.
        :param add_ons: An array of add-ons for the disk. .. epigraph:: If the disk has an add-on enabled when performing a delete disk request, the add-on is automatically disabled before the disk is deleted.
        :param availability_zone: The AWS Region and Availability Zone location for the disk (for example, ``us-east-1a`` ).
        :param location: Location of a resource.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ in the *AWS CloudFormation User Guide* . .. epigraph:: The ``Value`` of ``Tags`` is optional for Lightsail resources.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-disk.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_lightsail as lightsail
            
            cfn_disk_props = lightsail.CfnDiskProps(
                disk_name="diskName",
                size_in_gb=123,
            
                # the properties below are optional
                add_ons=[lightsail.CfnDisk.AddOnProperty(
                    add_on_type="addOnType",
            
                    # the properties below are optional
                    auto_snapshot_add_on_request=lightsail.CfnDisk.AutoSnapshotAddOnProperty(
                        snapshot_time_of_day="snapshotTimeOfDay"
                    ),
                    status="status"
                )],
                availability_zone="availabilityZone",
                location=lightsail.CfnDisk.LocationProperty(
                    availability_zone="availabilityZone",
                    region_name="regionName"
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d095d2590ef382758292269648b2abe4a720c01c7094f3ff4555ad70077f501d)
            check_type(argname="argument disk_name", value=disk_name, expected_type=type_hints["disk_name"])
            check_type(argname="argument size_in_gb", value=size_in_gb, expected_type=type_hints["size_in_gb"])
            check_type(argname="argument add_ons", value=add_ons, expected_type=type_hints["add_ons"])
            check_type(argname="argument availability_zone", value=availability_zone, expected_type=type_hints["availability_zone"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "disk_name": disk_name,
            "size_in_gb": size_in_gb,
        }
        if add_ons is not None:
            self._values["add_ons"] = add_ons
        if availability_zone is not None:
            self._values["availability_zone"] = availability_zone
        if location is not None:
            self._values["location"] = location
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def disk_name(self) -> builtins.str:
        '''The name of the disk.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-disk.html#cfn-lightsail-disk-diskname
        '''
        result = self._values.get("disk_name")
        assert result is not None, "Required property 'disk_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def size_in_gb(self) -> jsii.Number:
        '''The size of the disk in GB.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-disk.html#cfn-lightsail-disk-sizeingb
        '''
        result = self._values.get("size_in_gb")
        assert result is not None, "Required property 'size_in_gb' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def add_ons(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDisk.AddOnProperty]]]]:
        '''An array of add-ons for the disk.

        .. epigraph::

           If the disk has an add-on enabled when performing a delete disk request, the add-on is automatically disabled before the disk is deleted.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-disk.html#cfn-lightsail-disk-addons
        '''
        result = self._values.get("add_ons")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDisk.AddOnProperty]]]], result)

    @builtins.property
    def availability_zone(self) -> typing.Optional[builtins.str]:
        '''The AWS Region and Availability Zone location for the disk (for example, ``us-east-1a`` ).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-disk.html#cfn-lightsail-disk-availabilityzone
        '''
        result = self._values.get("availability_zone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def location(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDisk.LocationProperty]]:
        '''Location of a resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-disk.html#cfn-lightsail-disk-location
        '''
        result = self._values.get("location")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDisk.LocationProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ in the *AWS CloudFormation User Guide* .
        .. epigraph::

           The ``Value`` of ``Tags`` is optional for Lightsail resources.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-disk.html#cfn-lightsail-disk-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDiskProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnDistribution(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_lightsail.CfnDistribution",
):
    '''The ``AWS::Lightsail::Distribution`` resource specifies a content delivery network (CDN) distribution.

    You can create distributions only in the ``us-east-1`` AWS Region.

    A distribution is a globally distributed network of caching servers that improve the performance of your website or web application hosted on a Lightsail instance, static content hosted on a Lightsail bucket, or through a Lightsail load balancer.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-distribution.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_lightsail as lightsail
        
        cfn_distribution = lightsail.CfnDistribution(self, "MyCfnDistribution",
            bundle_id="bundleId",
            default_cache_behavior=lightsail.CfnDistribution.CacheBehaviorProperty(
                behavior="behavior"
            ),
            distribution_name="distributionName",
            origin=lightsail.CfnDistribution.InputOriginProperty(
                name="name",
                protocol_policy="protocolPolicy",
                region_name="regionName"
            ),
        
            # the properties below are optional
            cache_behaviors=[lightsail.CfnDistribution.CacheBehaviorPerPathProperty(
                behavior="behavior",
                path="path"
            )],
            cache_behavior_settings=lightsail.CfnDistribution.CacheSettingsProperty(
                allowed_http_methods="allowedHttpMethods",
                cached_http_methods="cachedHttpMethods",
                default_ttl=123,
                forwarded_cookies=lightsail.CfnDistribution.CookieObjectProperty(
                    cookies_allow_list=["cookiesAllowList"],
                    option="option"
                ),
                forwarded_headers=lightsail.CfnDistribution.HeaderObjectProperty(
                    headers_allow_list=["headersAllowList"],
                    option="option"
                ),
                forwarded_query_strings=lightsail.CfnDistribution.QueryStringObjectProperty(
                    option=False,
                    query_strings_allow_list=["queryStringsAllowList"]
                ),
                maximum_ttl=123,
                minimum_ttl=123
            ),
            certificate_name="certificateName",
            ip_address_type="ipAddressType",
            is_enabled=False,
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
        bundle_id: builtins.str,
        default_cache_behavior: typing.Union[_IResolvable_da3f097b, typing.Union["CfnDistribution.CacheBehaviorProperty", typing.Dict[builtins.str, typing.Any]]],
        distribution_name: builtins.str,
        origin: typing.Union[_IResolvable_da3f097b, typing.Union["CfnDistribution.InputOriginProperty", typing.Dict[builtins.str, typing.Any]]],
        cache_behaviors: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDistribution.CacheBehaviorPerPathProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        cache_behavior_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDistribution.CacheSettingsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        certificate_name: typing.Optional[builtins.str] = None,
        ip_address_type: typing.Optional[builtins.str] = None,
        is_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param bundle_id: The ID of the bundle applied to the distribution.
        :param default_cache_behavior: An object that describes the default cache behavior of the distribution.
        :param distribution_name: The name of the distribution.
        :param origin: An object that describes the origin resource of the distribution, such as a Lightsail instance, bucket, or load balancer. The distribution pulls, caches, and serves content from the origin.
        :param cache_behaviors: An array of objects that describe the per-path cache behavior of the distribution.
        :param cache_behavior_settings: An object that describes the cache behavior settings of the distribution.
        :param certificate_name: The name of the SSL/TLS certificate attached to the distribution.
        :param ip_address_type: The IP address type of the distribution. The possible values are ``ipv4`` for IPv4 only, and ``dualstack`` for IPv4 and IPv6.
        :param is_enabled: A Boolean value indicating whether the distribution is enabled.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ in the *AWS CloudFormation User Guide* . .. epigraph:: The ``Value`` of ``Tags`` is optional for Lightsail resources.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9482ccb96453330c51f380a8c1e2e74f0c57b789e803cc41a6d1f7dcb6be11b9)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDistributionProps(
            bundle_id=bundle_id,
            default_cache_behavior=default_cache_behavior,
            distribution_name=distribution_name,
            origin=origin,
            cache_behaviors=cache_behaviors,
            cache_behavior_settings=cache_behavior_settings,
            certificate_name=certificate_name,
            ip_address_type=ip_address_type,
            is_enabled=is_enabled,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8da47e5ef6c7db02eb83fd111cd49ed93a08332c93a0f1d588cdc74356706636)
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
            type_hints = typing.get_type_hints(_typecheckingstub__bb5945d202d9d8440df9db2cbb8008adb965c2628d41aee45553082f8a9fc477)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAbleToUpdateBundle")
    def attr_able_to_update_bundle(self) -> _IResolvable_da3f097b:
        '''Indicates whether you can update the distribution’s current bundle to another bundle.

        :cloudformationAttribute: AbleToUpdateBundle
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrAbleToUpdateBundle"))

    @builtins.property
    @jsii.member(jsii_name="attrDistributionArn")
    def attr_distribution_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the distribution.

        :cloudformationAttribute: DistributionArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDistributionArn"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The status of the distribution.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

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
    @jsii.member(jsii_name="bundleId")
    def bundle_id(self) -> builtins.str:
        '''The ID of the bundle applied to the distribution.'''
        return typing.cast(builtins.str, jsii.get(self, "bundleId"))

    @bundle_id.setter
    def bundle_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__713bb0b587b041ad1fbbf3481064d8f0e36314c4a715858754917a04e6b59834)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bundleId", value)

    @builtins.property
    @jsii.member(jsii_name="defaultCacheBehavior")
    def default_cache_behavior(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnDistribution.CacheBehaviorProperty"]:
        '''An object that describes the default cache behavior of the distribution.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnDistribution.CacheBehaviorProperty"], jsii.get(self, "defaultCacheBehavior"))

    @default_cache_behavior.setter
    def default_cache_behavior(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnDistribution.CacheBehaviorProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60f134014dad7eff652ae9a0a8f31d075d567a38120fb79b22fc79b66ef4afbf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultCacheBehavior", value)

    @builtins.property
    @jsii.member(jsii_name="distributionName")
    def distribution_name(self) -> builtins.str:
        '''The name of the distribution.'''
        return typing.cast(builtins.str, jsii.get(self, "distributionName"))

    @distribution_name.setter
    def distribution_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f10d8b0a845facf9cb45b4afe93f3ae69d0dab27fa56b50b7cc0e69ee5ab2f3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "distributionName", value)

    @builtins.property
    @jsii.member(jsii_name="origin")
    def origin(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnDistribution.InputOriginProperty"]:
        '''An object that describes the origin resource of the distribution, such as a Lightsail instance, bucket, or load balancer.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnDistribution.InputOriginProperty"], jsii.get(self, "origin"))

    @origin.setter
    def origin(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnDistribution.InputOriginProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7aef6fbf79a3b5e2f5250752a43b5ce48241a88650e2ca85121c71c9eff2e8db)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "origin", value)

    @builtins.property
    @jsii.member(jsii_name="cacheBehaviors")
    def cache_behaviors(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDistribution.CacheBehaviorPerPathProperty"]]]]:
        '''An array of objects that describe the per-path cache behavior of the distribution.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDistribution.CacheBehaviorPerPathProperty"]]]], jsii.get(self, "cacheBehaviors"))

    @cache_behaviors.setter
    def cache_behaviors(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDistribution.CacheBehaviorPerPathProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa33d1002424823136283db85abedb68f706cfe801b8cdda97985832959b3635)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cacheBehaviors", value)

    @builtins.property
    @jsii.member(jsii_name="cacheBehaviorSettings")
    def cache_behavior_settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDistribution.CacheSettingsProperty"]]:
        '''An object that describes the cache behavior settings of the distribution.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDistribution.CacheSettingsProperty"]], jsii.get(self, "cacheBehaviorSettings"))

    @cache_behavior_settings.setter
    def cache_behavior_settings(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDistribution.CacheSettingsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__760802ef8ce7a6adca268629830855308c05a61f03a8580e810b0493e8340ff0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cacheBehaviorSettings", value)

    @builtins.property
    @jsii.member(jsii_name="certificateName")
    def certificate_name(self) -> typing.Optional[builtins.str]:
        '''The name of the SSL/TLS certificate attached to the distribution.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateName"))

    @certificate_name.setter
    def certificate_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a588edb72e589002f8ed3b782d48335de6cd3b97ead472d268cbbc811d7a9aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateName", value)

    @builtins.property
    @jsii.member(jsii_name="ipAddressType")
    def ip_address_type(self) -> typing.Optional[builtins.str]:
        '''The IP address type of the distribution.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipAddressType"))

    @ip_address_type.setter
    def ip_address_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__852740f08ca9ce997952eb51ce9417e48061256a758eed9e4defe320b5cb751d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipAddressType", value)

    @builtins.property
    @jsii.member(jsii_name="isEnabled")
    def is_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''A Boolean value indicating whether the distribution is enabled.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "isEnabled"))

    @is_enabled.setter
    def is_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45ad4bf8bbe0e7c8404bc88c174e7fc60ea632f80e1214c05127c076aa76106d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__908b31b9ccd34cec50f1719ac43f4d386695ad72d71eff4b6177f5f0cbae1d41)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lightsail.CfnDistribution.CacheBehaviorPerPathProperty",
        jsii_struct_bases=[],
        name_mapping={"behavior": "behavior", "path": "path"},
    )
    class CacheBehaviorPerPathProperty:
        def __init__(
            self,
            *,
            behavior: typing.Optional[builtins.str] = None,
            path: typing.Optional[builtins.str] = None,
        ) -> None:
            '''``CacheBehaviorPerPath`` is a property of the `AWS::Lightsail::Distribution <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-distribution.html>`_ resource. It describes the per-path cache behavior of an Amazon Lightsail content delivery network (CDN) distribution.

            Use a per-path cache behavior to override the default cache behavior of a distribution, or to add an exception to it. For example, if you set the ``CacheBehavior`` to ``cache`` , you can use a per-path cache behavior to specify a directory, file, or file type that your distribution will cache. If you don’t want your distribution to cache a specified directory, file, or file type, set the per-path cache behavior to ``dont-cache`` .

            :param behavior: The cache behavior for the specified path. You can specify one of the following per-path cache behaviors: - *``cache``* - This behavior caches the specified path. - *``dont-cache``* - This behavior doesn't cache the specified path.
            :param path: The path to a directory or file to cache, or not cache. Use an asterisk symbol to specify wildcard directories ( ``path/to/assets/*`` ), and file types ( ``*.html`` , ``*jpg`` , ``*js`` ). Directories and file paths are case-sensitive. Examples: - Specify the following to cache all files in the document root of an Apache web server running on a instance. ``var/www/html/`` - Specify the following file to cache only the index page in the document root of an Apache web server. ``var/www/html/index.html`` - Specify the following to cache only the .html files in the document root of an Apache web server. ``var/www/html/*.html`` - Specify the following to cache only the .jpg, .png, and .gif files in the images sub-directory of the document root of an Apache web server. ``var/www/html/images/*.jpg`` ``var/www/html/images/*.png`` ``var/www/html/images/*.gif`` Specify the following to cache all files in the images subdirectory of the document root of an Apache web server. ``var/www/html/images/``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-distribution-cachebehaviorperpath.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lightsail as lightsail
                
                cache_behavior_per_path_property = lightsail.CfnDistribution.CacheBehaviorPerPathProperty(
                    behavior="behavior",
                    path="path"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f2d974d0c55f60f6f3f06797debd277521527e8d953d07b13eb3246980e4f75d)
                check_type(argname="argument behavior", value=behavior, expected_type=type_hints["behavior"])
                check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if behavior is not None:
                self._values["behavior"] = behavior
            if path is not None:
                self._values["path"] = path

        @builtins.property
        def behavior(self) -> typing.Optional[builtins.str]:
            '''The cache behavior for the specified path.

            You can specify one of the following per-path cache behaviors:

            - *``cache``* - This behavior caches the specified path.
            - *``dont-cache``* - This behavior doesn't cache the specified path.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-distribution-cachebehaviorperpath.html#cfn-lightsail-distribution-cachebehaviorperpath-behavior
            '''
            result = self._values.get("behavior")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def path(self) -> typing.Optional[builtins.str]:
            '''The path to a directory or file to cache, or not cache.

            Use an asterisk symbol to specify wildcard directories ( ``path/to/assets/*`` ), and file types ( ``*.html`` , ``*jpg`` , ``*js`` ). Directories and file paths are case-sensitive.

            Examples:

            - Specify the following to cache all files in the document root of an Apache web server running on a instance.

            ``var/www/html/``

            - Specify the following file to cache only the index page in the document root of an Apache web server.

            ``var/www/html/index.html``

            - Specify the following to cache only the .html files in the document root of an Apache web server.

            ``var/www/html/*.html``

            - Specify the following to cache only the .jpg, .png, and .gif files in the images sub-directory of the document root of an Apache web server.

            ``var/www/html/images/*.jpg``

            ``var/www/html/images/*.png``

            ``var/www/html/images/*.gif``

            Specify the following to cache all files in the images subdirectory of the document root of an Apache web server.

            ``var/www/html/images/``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-distribution-cachebehaviorperpath.html#cfn-lightsail-distribution-cachebehaviorperpath-path
            '''
            result = self._values.get("path")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CacheBehaviorPerPathProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lightsail.CfnDistribution.CacheBehaviorProperty",
        jsii_struct_bases=[],
        name_mapping={"behavior": "behavior"},
    )
    class CacheBehaviorProperty:
        def __init__(self, *, behavior: typing.Optional[builtins.str] = None) -> None:
            '''``CacheBehavior`` is a property of the `AWS::Lightsail::Distribution <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-distribution.html>`_ resource. It describes the default cache behavior of an Amazon Lightsail content delivery network (CDN) distribution.

            :param behavior: The cache behavior of the distribution. The following cache behaviors can be specified: - *``cache``* - This option is best for static sites. When specified, your distribution caches and serves your entire website as static content. This behavior is ideal for websites with static content that doesn't change depending on who views it, or for websites that don't use cookies, headers, or query strings to personalize content. - *``dont-cache``* - This option is best for sites that serve a mix of static and dynamic content. When specified, your distribution caches and serves only the content that is specified in the distribution’s ``CacheBehaviorPerPath`` parameter. This behavior is ideal for websites or web applications that use cookies, headers, and query strings to personalize content for individual users.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-distribution-cachebehavior.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lightsail as lightsail
                
                cache_behavior_property = lightsail.CfnDistribution.CacheBehaviorProperty(
                    behavior="behavior"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f5c3a4aa024dd1b6cd4538cc52ce109aa9ade3ffeff44b9a1d33fbc5100a3c2a)
                check_type(argname="argument behavior", value=behavior, expected_type=type_hints["behavior"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if behavior is not None:
                self._values["behavior"] = behavior

        @builtins.property
        def behavior(self) -> typing.Optional[builtins.str]:
            '''The cache behavior of the distribution.

            The following cache behaviors can be specified:

            - *``cache``* - This option is best for static sites. When specified, your distribution caches and serves your entire website as static content. This behavior is ideal for websites with static content that doesn't change depending on who views it, or for websites that don't use cookies, headers, or query strings to personalize content.
            - *``dont-cache``* - This option is best for sites that serve a mix of static and dynamic content. When specified, your distribution caches and serves only the content that is specified in the distribution’s ``CacheBehaviorPerPath`` parameter. This behavior is ideal for websites or web applications that use cookies, headers, and query strings to personalize content for individual users.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-distribution-cachebehavior.html#cfn-lightsail-distribution-cachebehavior-behavior
            '''
            result = self._values.get("behavior")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CacheBehaviorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lightsail.CfnDistribution.CacheSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "allowed_http_methods": "allowedHttpMethods",
            "cached_http_methods": "cachedHttpMethods",
            "default_ttl": "defaultTtl",
            "forwarded_cookies": "forwardedCookies",
            "forwarded_headers": "forwardedHeaders",
            "forwarded_query_strings": "forwardedQueryStrings",
            "maximum_ttl": "maximumTtl",
            "minimum_ttl": "minimumTtl",
        },
    )
    class CacheSettingsProperty:
        def __init__(
            self,
            *,
            allowed_http_methods: typing.Optional[builtins.str] = None,
            cached_http_methods: typing.Optional[builtins.str] = None,
            default_ttl: typing.Optional[jsii.Number] = None,
            forwarded_cookies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDistribution.CookieObjectProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            forwarded_headers: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDistribution.HeaderObjectProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            forwarded_query_strings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDistribution.QueryStringObjectProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            maximum_ttl: typing.Optional[jsii.Number] = None,
            minimum_ttl: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''``CacheSettings`` is a property of the `AWS::Lightsail::Distribution <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-distribution.html>`_ resource. It describes the cache settings of an Amazon Lightsail content delivery network (CDN) distribution.

            These settings apply only to your distribution’s ``CacheBehaviors`` that have a ``Behavior`` of ``cache`` . This includes the ``DefaultCacheBehavior`` .

            :param allowed_http_methods: The HTTP methods that are processed and forwarded to the distribution's origin. You can specify the following options: - ``GET,HEAD`` - The distribution forwards the ``GET`` and ``HEAD`` methods. - ``GET,HEAD,OPTIONS`` - The distribution forwards the ``GET`` , ``HEAD`` , and ``OPTIONS`` methods. - ``GET,HEAD,OPTIONS,PUT,PATCH,POST,DELETE`` - The distribution forwards the ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PUT`` , ``PATCH`` , ``POST`` , and ``DELETE`` methods. If you specify ``GET,HEAD,OPTIONS,PUT,PATCH,POST,DELETE`` , you might need to restrict access to your distribution's origin so users can't perform operations that you don't want them to. For example, you might not want users to have permission to delete objects from your origin.
            :param cached_http_methods: The HTTP method responses that are cached by your distribution. You can specify the following options: - ``GET,HEAD`` - The distribution caches responses to the ``GET`` and ``HEAD`` methods. - ``GET,HEAD,OPTIONS`` - The distribution caches responses to the ``GET`` , ``HEAD`` , and ``OPTIONS`` methods.
            :param default_ttl: The default amount of time that objects stay in the distribution's cache before the distribution forwards another request to the origin to determine whether the content has been updated. .. epigraph:: The value specified applies only when the origin does not add HTTP headers such as ``Cache-Control max-age`` , ``Cache-Control s-maxage`` , and ``Expires`` to objects.
            :param forwarded_cookies: An object that describes the cookies that are forwarded to the origin. Your content is cached based on the cookies that are forwarded.
            :param forwarded_headers: An object that describes the headers that are forwarded to the origin. Your content is cached based on the headers that are forwarded.
            :param forwarded_query_strings: An object that describes the query strings that are forwarded to the origin. Your content is cached based on the query strings that are forwarded.
            :param maximum_ttl: The maximum amount of time that objects stay in the distribution's cache before the distribution forwards another request to the origin to determine whether the object has been updated. The value specified applies only when the origin adds HTTP headers such as ``Cache-Control max-age`` , ``Cache-Control s-maxage`` , and ``Expires`` to objects.
            :param minimum_ttl: The minimum amount of time that objects stay in the distribution's cache before the distribution forwards another request to the origin to determine whether the object has been updated. A value of ``0`` must be specified for ``minimumTTL`` if the distribution is configured to forward all headers to the origin.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-distribution-cachesettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lightsail as lightsail
                
                cache_settings_property = lightsail.CfnDistribution.CacheSettingsProperty(
                    allowed_http_methods="allowedHttpMethods",
                    cached_http_methods="cachedHttpMethods",
                    default_ttl=123,
                    forwarded_cookies=lightsail.CfnDistribution.CookieObjectProperty(
                        cookies_allow_list=["cookiesAllowList"],
                        option="option"
                    ),
                    forwarded_headers=lightsail.CfnDistribution.HeaderObjectProperty(
                        headers_allow_list=["headersAllowList"],
                        option="option"
                    ),
                    forwarded_query_strings=lightsail.CfnDistribution.QueryStringObjectProperty(
                        option=False,
                        query_strings_allow_list=["queryStringsAllowList"]
                    ),
                    maximum_ttl=123,
                    minimum_ttl=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__71273d747070fd305155aa796ba791770952e4398259d9319417dfa9ca649969)
                check_type(argname="argument allowed_http_methods", value=allowed_http_methods, expected_type=type_hints["allowed_http_methods"])
                check_type(argname="argument cached_http_methods", value=cached_http_methods, expected_type=type_hints["cached_http_methods"])
                check_type(argname="argument default_ttl", value=default_ttl, expected_type=type_hints["default_ttl"])
                check_type(argname="argument forwarded_cookies", value=forwarded_cookies, expected_type=type_hints["forwarded_cookies"])
                check_type(argname="argument forwarded_headers", value=forwarded_headers, expected_type=type_hints["forwarded_headers"])
                check_type(argname="argument forwarded_query_strings", value=forwarded_query_strings, expected_type=type_hints["forwarded_query_strings"])
                check_type(argname="argument maximum_ttl", value=maximum_ttl, expected_type=type_hints["maximum_ttl"])
                check_type(argname="argument minimum_ttl", value=minimum_ttl, expected_type=type_hints["minimum_ttl"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if allowed_http_methods is not None:
                self._values["allowed_http_methods"] = allowed_http_methods
            if cached_http_methods is not None:
                self._values["cached_http_methods"] = cached_http_methods
            if default_ttl is not None:
                self._values["default_ttl"] = default_ttl
            if forwarded_cookies is not None:
                self._values["forwarded_cookies"] = forwarded_cookies
            if forwarded_headers is not None:
                self._values["forwarded_headers"] = forwarded_headers
            if forwarded_query_strings is not None:
                self._values["forwarded_query_strings"] = forwarded_query_strings
            if maximum_ttl is not None:
                self._values["maximum_ttl"] = maximum_ttl
            if minimum_ttl is not None:
                self._values["minimum_ttl"] = minimum_ttl

        @builtins.property
        def allowed_http_methods(self) -> typing.Optional[builtins.str]:
            '''The HTTP methods that are processed and forwarded to the distribution's origin.

            You can specify the following options:

            - ``GET,HEAD`` - The distribution forwards the ``GET`` and ``HEAD`` methods.
            - ``GET,HEAD,OPTIONS`` - The distribution forwards the ``GET`` , ``HEAD`` , and ``OPTIONS`` methods.
            - ``GET,HEAD,OPTIONS,PUT,PATCH,POST,DELETE`` - The distribution forwards the ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PUT`` , ``PATCH`` , ``POST`` , and ``DELETE`` methods.

            If you specify ``GET,HEAD,OPTIONS,PUT,PATCH,POST,DELETE`` , you might need to restrict access to your distribution's origin so users can't perform operations that you don't want them to. For example, you might not want users to have permission to delete objects from your origin.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-distribution-cachesettings.html#cfn-lightsail-distribution-cachesettings-allowedhttpmethods
            '''
            result = self._values.get("allowed_http_methods")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def cached_http_methods(self) -> typing.Optional[builtins.str]:
            '''The HTTP method responses that are cached by your distribution.

            You can specify the following options:

            - ``GET,HEAD`` - The distribution caches responses to the ``GET`` and ``HEAD`` methods.
            - ``GET,HEAD,OPTIONS`` - The distribution caches responses to the ``GET`` , ``HEAD`` , and ``OPTIONS`` methods.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-distribution-cachesettings.html#cfn-lightsail-distribution-cachesettings-cachedhttpmethods
            '''
            result = self._values.get("cached_http_methods")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def default_ttl(self) -> typing.Optional[jsii.Number]:
            '''The default amount of time that objects stay in the distribution's cache before the distribution forwards another request to the origin to determine whether the content has been updated.

            .. epigraph::

               The value specified applies only when the origin does not add HTTP headers such as ``Cache-Control max-age`` , ``Cache-Control s-maxage`` , and ``Expires`` to objects.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-distribution-cachesettings.html#cfn-lightsail-distribution-cachesettings-defaultttl
            '''
            result = self._values.get("default_ttl")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def forwarded_cookies(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDistribution.CookieObjectProperty"]]:
            '''An object that describes the cookies that are forwarded to the origin.

            Your content is cached based on the cookies that are forwarded.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-distribution-cachesettings.html#cfn-lightsail-distribution-cachesettings-forwardedcookies
            '''
            result = self._values.get("forwarded_cookies")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDistribution.CookieObjectProperty"]], result)

        @builtins.property
        def forwarded_headers(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDistribution.HeaderObjectProperty"]]:
            '''An object that describes the headers that are forwarded to the origin.

            Your content is cached based on the headers that are forwarded.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-distribution-cachesettings.html#cfn-lightsail-distribution-cachesettings-forwardedheaders
            '''
            result = self._values.get("forwarded_headers")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDistribution.HeaderObjectProperty"]], result)

        @builtins.property
        def forwarded_query_strings(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDistribution.QueryStringObjectProperty"]]:
            '''An object that describes the query strings that are forwarded to the origin.

            Your content is cached based on the query strings that are forwarded.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-distribution-cachesettings.html#cfn-lightsail-distribution-cachesettings-forwardedquerystrings
            '''
            result = self._values.get("forwarded_query_strings")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDistribution.QueryStringObjectProperty"]], result)

        @builtins.property
        def maximum_ttl(self) -> typing.Optional[jsii.Number]:
            '''The maximum amount of time that objects stay in the distribution's cache before the distribution forwards another request to the origin to determine whether the object has been updated.

            The value specified applies only when the origin adds HTTP headers such as ``Cache-Control max-age`` , ``Cache-Control s-maxage`` , and ``Expires`` to objects.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-distribution-cachesettings.html#cfn-lightsail-distribution-cachesettings-maximumttl
            '''
            result = self._values.get("maximum_ttl")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def minimum_ttl(self) -> typing.Optional[jsii.Number]:
            '''The minimum amount of time that objects stay in the distribution's cache before the distribution forwards another request to the origin to determine whether the object has been updated.

            A value of ``0`` must be specified for ``minimumTTL`` if the distribution is configured to forward all headers to the origin.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-distribution-cachesettings.html#cfn-lightsail-distribution-cachesettings-minimumttl
            '''
            result = self._values.get("minimum_ttl")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CacheSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lightsail.CfnDistribution.CookieObjectProperty",
        jsii_struct_bases=[],
        name_mapping={"cookies_allow_list": "cookiesAllowList", "option": "option"},
    )
    class CookieObjectProperty:
        def __init__(
            self,
            *,
            cookies_allow_list: typing.Optional[typing.Sequence[builtins.str]] = None,
            option: typing.Optional[builtins.str] = None,
        ) -> None:
            '''``CookieObject`` is a property of the `CacheSettings <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-distribution-cachesettings.html>`_ property. It describes whether an Amazon Lightsail content delivery network (CDN) distribution forwards cookies to the origin and, if so, which ones.

            For the cookies that you specify, your distribution caches separate versions of the specified content based on the cookie values in viewer requests.

            :param cookies_allow_list: The specific cookies to forward to your distribution's origin.
            :param option: Specifies which cookies to forward to the distribution's origin for a cache behavior. Use one of the following configurations for your distribution: - *``all``* - Forwards all cookies to your origin. - *``none``* - Doesn’t forward cookies to your origin. - *``allow-list``* - Forwards only the cookies that you specify using the ``CookiesAllowList`` parameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-distribution-cookieobject.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lightsail as lightsail
                
                cookie_object_property = lightsail.CfnDistribution.CookieObjectProperty(
                    cookies_allow_list=["cookiesAllowList"],
                    option="option"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d58452d36b0308e6ce28a9b550fe3fce77b87aaad440feefc51f83755937f137)
                check_type(argname="argument cookies_allow_list", value=cookies_allow_list, expected_type=type_hints["cookies_allow_list"])
                check_type(argname="argument option", value=option, expected_type=type_hints["option"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if cookies_allow_list is not None:
                self._values["cookies_allow_list"] = cookies_allow_list
            if option is not None:
                self._values["option"] = option

        @builtins.property
        def cookies_allow_list(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The specific cookies to forward to your distribution's origin.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-distribution-cookieobject.html#cfn-lightsail-distribution-cookieobject-cookiesallowlist
            '''
            result = self._values.get("cookies_allow_list")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def option(self) -> typing.Optional[builtins.str]:
            '''Specifies which cookies to forward to the distribution's origin for a cache behavior.

            Use one of the following configurations for your distribution:

            - *``all``* - Forwards all cookies to your origin.
            - *``none``* - Doesn’t forward cookies to your origin.
            - *``allow-list``* - Forwards only the cookies that you specify using the ``CookiesAllowList`` parameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-distribution-cookieobject.html#cfn-lightsail-distribution-cookieobject-option
            '''
            result = self._values.get("option")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CookieObjectProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lightsail.CfnDistribution.HeaderObjectProperty",
        jsii_struct_bases=[],
        name_mapping={"headers_allow_list": "headersAllowList", "option": "option"},
    )
    class HeaderObjectProperty:
        def __init__(
            self,
            *,
            headers_allow_list: typing.Optional[typing.Sequence[builtins.str]] = None,
            option: typing.Optional[builtins.str] = None,
        ) -> None:
            '''``HeaderObject`` is a property of the `CacheSettings <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-distribution-cachesettings.html>`_ property. It describes the request headers used by your distribution, which caches your content based on the request headers.

            For the headers that you specify, your distribution caches separate versions of the specified content based on the header values in viewer requests. For example, suppose that viewer requests for logo.jpg contain a custom product header that has a value of either acme or apex. Also, suppose that you configure your distribution to cache your content based on values in the product header. Your distribution forwards the product header to the origin and caches the response from the origin once for each header value.

            :param headers_allow_list: The specific headers to forward to your distribution's origin.
            :param option: The headers that you want your distribution to forward to your origin. Your distribution caches your content based on these headers. Use one of the following configurations for your distribution: - *``all``* - Forwards all headers to your origin.. - *``none``* - Forwards only the default headers. - *``allow-list``* - Forwards only the headers that you specify using the ``HeadersAllowList`` parameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-distribution-headerobject.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lightsail as lightsail
                
                header_object_property = lightsail.CfnDistribution.HeaderObjectProperty(
                    headers_allow_list=["headersAllowList"],
                    option="option"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e8800c7d1a30fcdf0e75dfd3650ad86e4223cdabbe6df507c54628133a0c1fc2)
                check_type(argname="argument headers_allow_list", value=headers_allow_list, expected_type=type_hints["headers_allow_list"])
                check_type(argname="argument option", value=option, expected_type=type_hints["option"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if headers_allow_list is not None:
                self._values["headers_allow_list"] = headers_allow_list
            if option is not None:
                self._values["option"] = option

        @builtins.property
        def headers_allow_list(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The specific headers to forward to your distribution's origin.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-distribution-headerobject.html#cfn-lightsail-distribution-headerobject-headersallowlist
            '''
            result = self._values.get("headers_allow_list")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def option(self) -> typing.Optional[builtins.str]:
            '''The headers that you want your distribution to forward to your origin.

            Your distribution caches your content based on these headers.

            Use one of the following configurations for your distribution:

            - *``all``* - Forwards all headers to your origin..
            - *``none``* - Forwards only the default headers.
            - *``allow-list``* - Forwards only the headers that you specify using the ``HeadersAllowList`` parameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-distribution-headerobject.html#cfn-lightsail-distribution-headerobject-option
            '''
            result = self._values.get("option")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HeaderObjectProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lightsail.CfnDistribution.InputOriginProperty",
        jsii_struct_bases=[],
        name_mapping={
            "name": "name",
            "protocol_policy": "protocolPolicy",
            "region_name": "regionName",
        },
    )
    class InputOriginProperty:
        def __init__(
            self,
            *,
            name: typing.Optional[builtins.str] = None,
            protocol_policy: typing.Optional[builtins.str] = None,
            region_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''``InputOrigin`` is a property of the `AWS::Lightsail::Distribution <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-distribution.html>`_ resource. It describes the origin resource of an Amazon Lightsail content delivery network (CDN) distribution.

            An origin can be a instance, bucket, or load balancer. A distribution pulls content from an origin, caches it, and serves it to viewers through a worldwide network of edge servers.

            :param name: The name of the origin resource.
            :param protocol_policy: The protocol that your Amazon Lightsail distribution uses when establishing a connection with your origin to pull content.
            :param region_name: The AWS Region name of the origin resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-distribution-inputorigin.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lightsail as lightsail
                
                input_origin_property = lightsail.CfnDistribution.InputOriginProperty(
                    name="name",
                    protocol_policy="protocolPolicy",
                    region_name="regionName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__accc7b7eb30a60be239eb0280dade3739e4094e04bda535d5fe3d04d2d008607)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument protocol_policy", value=protocol_policy, expected_type=type_hints["protocol_policy"])
                check_type(argname="argument region_name", value=region_name, expected_type=type_hints["region_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if name is not None:
                self._values["name"] = name
            if protocol_policy is not None:
                self._values["protocol_policy"] = protocol_policy
            if region_name is not None:
                self._values["region_name"] = region_name

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the origin resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-distribution-inputorigin.html#cfn-lightsail-distribution-inputorigin-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def protocol_policy(self) -> typing.Optional[builtins.str]:
            '''The protocol that your Amazon Lightsail distribution uses when establishing a connection with your origin to pull content.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-distribution-inputorigin.html#cfn-lightsail-distribution-inputorigin-protocolpolicy
            '''
            result = self._values.get("protocol_policy")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def region_name(self) -> typing.Optional[builtins.str]:
            '''The AWS Region name of the origin resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-distribution-inputorigin.html#cfn-lightsail-distribution-inputorigin-regionname
            '''
            result = self._values.get("region_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InputOriginProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lightsail.CfnDistribution.QueryStringObjectProperty",
        jsii_struct_bases=[],
        name_mapping={
            "option": "option",
            "query_strings_allow_list": "queryStringsAllowList",
        },
    )
    class QueryStringObjectProperty:
        def __init__(
            self,
            *,
            option: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            query_strings_allow_list: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''``QueryStringObject`` is a property of the `CacheSettings <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-distribution-cachesettings.html>`_ property. It describes the query string parameters that an Amazon Lightsail content delivery network (CDN) distribution to bases caching on.

            For the query strings that you specify, your distribution caches separate versions of the specified content based on the query string values in viewer requests.

            :param option: Indicates whether the distribution forwards and caches based on query strings.
            :param query_strings_allow_list: The specific query strings that the distribution forwards to the origin. Your distribution caches content based on the specified query strings. If the ``option`` parameter is true, then your distribution forwards all query strings, regardless of what you specify using the ``QueryStringsAllowList`` parameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-distribution-querystringobject.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lightsail as lightsail
                
                query_string_object_property = lightsail.CfnDistribution.QueryStringObjectProperty(
                    option=False,
                    query_strings_allow_list=["queryStringsAllowList"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d3d10f0e1349e20e39be61df90b8a453ebfd22f3496fc3e4391831ccb7b40abd)
                check_type(argname="argument option", value=option, expected_type=type_hints["option"])
                check_type(argname="argument query_strings_allow_list", value=query_strings_allow_list, expected_type=type_hints["query_strings_allow_list"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if option is not None:
                self._values["option"] = option
            if query_strings_allow_list is not None:
                self._values["query_strings_allow_list"] = query_strings_allow_list

        @builtins.property
        def option(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates whether the distribution forwards and caches based on query strings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-distribution-querystringobject.html#cfn-lightsail-distribution-querystringobject-option
            '''
            result = self._values.get("option")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def query_strings_allow_list(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''The specific query strings that the distribution forwards to the origin.

            Your distribution caches content based on the specified query strings.

            If the ``option`` parameter is true, then your distribution forwards all query strings, regardless of what you specify using the ``QueryStringsAllowList`` parameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-distribution-querystringobject.html#cfn-lightsail-distribution-querystringobject-querystringsallowlist
            '''
            result = self._values.get("query_strings_allow_list")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "QueryStringObjectProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_lightsail.CfnDistributionProps",
    jsii_struct_bases=[],
    name_mapping={
        "bundle_id": "bundleId",
        "default_cache_behavior": "defaultCacheBehavior",
        "distribution_name": "distributionName",
        "origin": "origin",
        "cache_behaviors": "cacheBehaviors",
        "cache_behavior_settings": "cacheBehaviorSettings",
        "certificate_name": "certificateName",
        "ip_address_type": "ipAddressType",
        "is_enabled": "isEnabled",
        "tags": "tags",
    },
)
class CfnDistributionProps:
    def __init__(
        self,
        *,
        bundle_id: builtins.str,
        default_cache_behavior: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDistribution.CacheBehaviorProperty, typing.Dict[builtins.str, typing.Any]]],
        distribution_name: builtins.str,
        origin: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDistribution.InputOriginProperty, typing.Dict[builtins.str, typing.Any]]],
        cache_behaviors: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDistribution.CacheBehaviorPerPathProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        cache_behavior_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDistribution.CacheSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        certificate_name: typing.Optional[builtins.str] = None,
        ip_address_type: typing.Optional[builtins.str] = None,
        is_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDistribution``.

        :param bundle_id: The ID of the bundle applied to the distribution.
        :param default_cache_behavior: An object that describes the default cache behavior of the distribution.
        :param distribution_name: The name of the distribution.
        :param origin: An object that describes the origin resource of the distribution, such as a Lightsail instance, bucket, or load balancer. The distribution pulls, caches, and serves content from the origin.
        :param cache_behaviors: An array of objects that describe the per-path cache behavior of the distribution.
        :param cache_behavior_settings: An object that describes the cache behavior settings of the distribution.
        :param certificate_name: The name of the SSL/TLS certificate attached to the distribution.
        :param ip_address_type: The IP address type of the distribution. The possible values are ``ipv4`` for IPv4 only, and ``dualstack`` for IPv4 and IPv6.
        :param is_enabled: A Boolean value indicating whether the distribution is enabled.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ in the *AWS CloudFormation User Guide* . .. epigraph:: The ``Value`` of ``Tags`` is optional for Lightsail resources.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-distribution.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_lightsail as lightsail
            
            cfn_distribution_props = lightsail.CfnDistributionProps(
                bundle_id="bundleId",
                default_cache_behavior=lightsail.CfnDistribution.CacheBehaviorProperty(
                    behavior="behavior"
                ),
                distribution_name="distributionName",
                origin=lightsail.CfnDistribution.InputOriginProperty(
                    name="name",
                    protocol_policy="protocolPolicy",
                    region_name="regionName"
                ),
            
                # the properties below are optional
                cache_behaviors=[lightsail.CfnDistribution.CacheBehaviorPerPathProperty(
                    behavior="behavior",
                    path="path"
                )],
                cache_behavior_settings=lightsail.CfnDistribution.CacheSettingsProperty(
                    allowed_http_methods="allowedHttpMethods",
                    cached_http_methods="cachedHttpMethods",
                    default_ttl=123,
                    forwarded_cookies=lightsail.CfnDistribution.CookieObjectProperty(
                        cookies_allow_list=["cookiesAllowList"],
                        option="option"
                    ),
                    forwarded_headers=lightsail.CfnDistribution.HeaderObjectProperty(
                        headers_allow_list=["headersAllowList"],
                        option="option"
                    ),
                    forwarded_query_strings=lightsail.CfnDistribution.QueryStringObjectProperty(
                        option=False,
                        query_strings_allow_list=["queryStringsAllowList"]
                    ),
                    maximum_ttl=123,
                    minimum_ttl=123
                ),
                certificate_name="certificateName",
                ip_address_type="ipAddressType",
                is_enabled=False,
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5746be261e67458f872b406208009ddcf740c3277f27869ccbc24697bfb6d14c)
            check_type(argname="argument bundle_id", value=bundle_id, expected_type=type_hints["bundle_id"])
            check_type(argname="argument default_cache_behavior", value=default_cache_behavior, expected_type=type_hints["default_cache_behavior"])
            check_type(argname="argument distribution_name", value=distribution_name, expected_type=type_hints["distribution_name"])
            check_type(argname="argument origin", value=origin, expected_type=type_hints["origin"])
            check_type(argname="argument cache_behaviors", value=cache_behaviors, expected_type=type_hints["cache_behaviors"])
            check_type(argname="argument cache_behavior_settings", value=cache_behavior_settings, expected_type=type_hints["cache_behavior_settings"])
            check_type(argname="argument certificate_name", value=certificate_name, expected_type=type_hints["certificate_name"])
            check_type(argname="argument ip_address_type", value=ip_address_type, expected_type=type_hints["ip_address_type"])
            check_type(argname="argument is_enabled", value=is_enabled, expected_type=type_hints["is_enabled"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bundle_id": bundle_id,
            "default_cache_behavior": default_cache_behavior,
            "distribution_name": distribution_name,
            "origin": origin,
        }
        if cache_behaviors is not None:
            self._values["cache_behaviors"] = cache_behaviors
        if cache_behavior_settings is not None:
            self._values["cache_behavior_settings"] = cache_behavior_settings
        if certificate_name is not None:
            self._values["certificate_name"] = certificate_name
        if ip_address_type is not None:
            self._values["ip_address_type"] = ip_address_type
        if is_enabled is not None:
            self._values["is_enabled"] = is_enabled
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def bundle_id(self) -> builtins.str:
        '''The ID of the bundle applied to the distribution.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-distribution.html#cfn-lightsail-distribution-bundleid
        '''
        result = self._values.get("bundle_id")
        assert result is not None, "Required property 'bundle_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def default_cache_behavior(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnDistribution.CacheBehaviorProperty]:
        '''An object that describes the default cache behavior of the distribution.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-distribution.html#cfn-lightsail-distribution-defaultcachebehavior
        '''
        result = self._values.get("default_cache_behavior")
        assert result is not None, "Required property 'default_cache_behavior' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnDistribution.CacheBehaviorProperty], result)

    @builtins.property
    def distribution_name(self) -> builtins.str:
        '''The name of the distribution.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-distribution.html#cfn-lightsail-distribution-distributionname
        '''
        result = self._values.get("distribution_name")
        assert result is not None, "Required property 'distribution_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def origin(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnDistribution.InputOriginProperty]:
        '''An object that describes the origin resource of the distribution, such as a Lightsail instance, bucket, or load balancer.

        The distribution pulls, caches, and serves content from the origin.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-distribution.html#cfn-lightsail-distribution-origin
        '''
        result = self._values.get("origin")
        assert result is not None, "Required property 'origin' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnDistribution.InputOriginProperty], result)

    @builtins.property
    def cache_behaviors(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDistribution.CacheBehaviorPerPathProperty]]]]:
        '''An array of objects that describe the per-path cache behavior of the distribution.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-distribution.html#cfn-lightsail-distribution-cachebehaviors
        '''
        result = self._values.get("cache_behaviors")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDistribution.CacheBehaviorPerPathProperty]]]], result)

    @builtins.property
    def cache_behavior_settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDistribution.CacheSettingsProperty]]:
        '''An object that describes the cache behavior settings of the distribution.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-distribution.html#cfn-lightsail-distribution-cachebehaviorsettings
        '''
        result = self._values.get("cache_behavior_settings")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDistribution.CacheSettingsProperty]], result)

    @builtins.property
    def certificate_name(self) -> typing.Optional[builtins.str]:
        '''The name of the SSL/TLS certificate attached to the distribution.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-distribution.html#cfn-lightsail-distribution-certificatename
        '''
        result = self._values.get("certificate_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ip_address_type(self) -> typing.Optional[builtins.str]:
        '''The IP address type of the distribution.

        The possible values are ``ipv4`` for IPv4 only, and ``dualstack`` for IPv4 and IPv6.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-distribution.html#cfn-lightsail-distribution-ipaddresstype
        '''
        result = self._values.get("ip_address_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def is_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''A Boolean value indicating whether the distribution is enabled.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-distribution.html#cfn-lightsail-distribution-isenabled
        '''
        result = self._values.get("is_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ in the *AWS CloudFormation User Guide* .
        .. epigraph::

           The ``Value`` of ``Tags`` is optional for Lightsail resources.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-distribution.html#cfn-lightsail-distribution-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDistributionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnInstance(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_lightsail.CfnInstance",
):
    '''The ``AWS::Lightsail::Instance`` resource specifies an Amazon Lightsail instance.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_lightsail as lightsail
        
        cfn_instance = lightsail.CfnInstance(self, "MyCfnInstance",
            blueprint_id="blueprintId",
            bundle_id="bundleId",
            instance_name="instanceName",
        
            # the properties below are optional
            add_ons=[lightsail.CfnInstance.AddOnProperty(
                add_on_type="addOnType",
        
                # the properties below are optional
                auto_snapshot_add_on_request=lightsail.CfnInstance.AutoSnapshotAddOnProperty(
                    snapshot_time_of_day="snapshotTimeOfDay"
                ),
                status="status"
            )],
            availability_zone="availabilityZone",
            hardware=lightsail.CfnInstance.HardwareProperty(
                cpu_count=123,
                disks=[lightsail.CfnInstance.DiskProperty(
                    disk_name="diskName",
                    path="path",
        
                    # the properties below are optional
                    attached_to="attachedTo",
                    attachment_state="attachmentState",
                    iops=123,
                    is_system_disk=False,
                    size_in_gb="sizeInGb"
                )],
                ram_size_in_gb=123
            ),
            key_pair_name="keyPairName",
            location=lightsail.CfnInstance.LocationProperty(
                availability_zone="availabilityZone",
                region_name="regionName"
            ),
            networking=lightsail.CfnInstance.NetworkingProperty(
                ports=[lightsail.CfnInstance.PortProperty(
                    access_direction="accessDirection",
                    access_from="accessFrom",
                    access_type="accessType",
                    cidr_list_aliases=["cidrListAliases"],
                    cidrs=["cidrs"],
                    common_name="commonName",
                    from_port=123,
                    ipv6_cidrs=["ipv6Cidrs"],
                    protocol="protocol",
                    to_port=123
                )],
        
                # the properties below are optional
                monthly_transfer=123
            ),
            state=lightsail.CfnInstance.StateProperty(
                code=123,
                name="name"
            ),
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            user_data="userData"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        blueprint_id: builtins.str,
        bundle_id: builtins.str,
        instance_name: builtins.str,
        add_ons: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInstance.AddOnProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        availability_zone: typing.Optional[builtins.str] = None,
        hardware: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInstance.HardwareProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        key_pair_name: typing.Optional[builtins.str] = None,
        location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInstance.LocationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        networking: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInstance.NetworkingProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        state: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInstance.StateProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        user_data: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param blueprint_id: The blueprint ID for the instance (for example, ``os_amlinux_2016_03`` ).
        :param bundle_id: The bundle ID for the instance (for example, ``micro_1_0`` ).
        :param instance_name: The name of the instance.
        :param add_ons: An array of add-ons for the instance. .. epigraph:: If the instance has an add-on enabled when performing a delete instance request, the add-on is automatically disabled before the instance is deleted.
        :param availability_zone: The Availability Zone for the instance.
        :param hardware: The hardware properties for the instance, such as the vCPU count, attached disks, and amount of RAM. .. epigraph:: The instance restarts when performing an attach disk or detach disk request. This resets the public IP address of your instance if a static IP isn't attached to it.
        :param key_pair_name: The name of the key pair to use for the instance. If no key pair name is specified, the Regional Lightsail default key pair is used.
        :param location: The location for the instance, such as the AWS Region and Availability Zone. .. epigraph:: The ``Location`` property is read-only and should not be specified in a create instance or update instance request.
        :param networking: The public ports and the monthly amount of data transfer allocated for the instance.
        :param state: The status code and the state (for example, ``running`` ) of the instance. .. epigraph:: The ``State`` property is read-only and should not be specified in a create instance or update instance request.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ in the *AWS CloudFormation User Guide* . .. epigraph:: The ``Value`` of ``Tags`` is optional for Lightsail resources.
        :param user_data: The optional launch script for the instance. Specify a launch script to configure an instance with additional user data. For example, you might want to specify ``apt-get -y update`` as a launch script. .. epigraph:: Depending on the blueprint of your instance, the command to get software on your instance varies. Amazon Linux and CentOS use ``yum`` , Debian and Ubuntu use ``apt-get`` , and FreeBSD uses ``pkg`` .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f56ba2d2d7e68ec61cd3684949f9d2894843d2a820ea3c2a5dce40b3698dd9fe)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnInstanceProps(
            blueprint_id=blueprint_id,
            bundle_id=bundle_id,
            instance_name=instance_name,
            add_ons=add_ons,
            availability_zone=availability_zone,
            hardware=hardware,
            key_pair_name=key_pair_name,
            location=location,
            networking=networking,
            state=state,
            tags=tags,
            user_data=user_data,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be47197b4bba429c8a1b13b7bb35c7764b6aff13ccb15e40cefc35fd2df04e45)
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
            type_hints = typing.get_type_hints(_typecheckingstub__cee95794d0d504ed730245ac786397afe3973e5fffef49a4225b4ab4910ea884)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrHardwareCpuCount")
    def attr_hardware_cpu_count(self) -> jsii.Number:
        '''The number of vCPUs the instance has.

        :cloudformationAttribute: Hardware.CpuCount
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrHardwareCpuCount"))

    @builtins.property
    @jsii.member(jsii_name="attrHardwareRamSizeInGb")
    def attr_hardware_ram_size_in_gb(self) -> jsii.Number:
        '''The amount of RAM in GB on the instance (for example, ``1.0`` ).

        :cloudformationAttribute: Hardware.RamSizeInGb
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrHardwareRamSizeInGb"))

    @builtins.property
    @jsii.member(jsii_name="attrInstanceArn")
    def attr_instance_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the instance (for example, ``arn:aws:lightsail:us-east-2:123456789101:Instance/244ad76f-8aad-4741-809f-12345EXAMPLE`` ).

        :cloudformationAttribute: InstanceArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrInstanceArn"))

    @builtins.property
    @jsii.member(jsii_name="attrIsStaticIp")
    def attr_is_static_ip(self) -> _IResolvable_da3f097b:
        '''A Boolean value indicating whether the instance has a static IP assigned to it.

        :cloudformationAttribute: IsStaticIp
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrIsStaticIp"))

    @builtins.property
    @jsii.member(jsii_name="attrLocationAvailabilityZone")
    def attr_location_availability_zone(self) -> builtins.str:
        '''The AWS Region and Availability Zone where the instance is located.

        :cloudformationAttribute: Location.AvailabilityZone
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLocationAvailabilityZone"))

    @builtins.property
    @jsii.member(jsii_name="attrLocationRegionName")
    def attr_location_region_name(self) -> builtins.str:
        '''The AWS Region of the instance.

        :cloudformationAttribute: Location.RegionName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLocationRegionName"))

    @builtins.property
    @jsii.member(jsii_name="attrNetworkingMonthlyTransferGbPerMonthAllocated")
    def attr_networking_monthly_transfer_gb_per_month_allocated(self) -> builtins.str:
        '''The amount of allocated monthly data transfer (in GB) for an instance.

        :cloudformationAttribute: Networking.MonthlyTransfer.GbPerMonthAllocated
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrNetworkingMonthlyTransferGbPerMonthAllocated"))

    @builtins.property
    @jsii.member(jsii_name="attrPrivateIpAddress")
    def attr_private_ip_address(self) -> builtins.str:
        '''The private IP address of the instance.

        :cloudformationAttribute: PrivateIpAddress
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPrivateIpAddress"))

    @builtins.property
    @jsii.member(jsii_name="attrPublicIpAddress")
    def attr_public_ip_address(self) -> builtins.str:
        '''The public IP address of the instance.

        :cloudformationAttribute: PublicIpAddress
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPublicIpAddress"))

    @builtins.property
    @jsii.member(jsii_name="attrResourceType")
    def attr_resource_type(self) -> builtins.str:
        '''The resource type of the instance (for example, ``Instance`` ).

        :cloudformationAttribute: ResourceType
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrResourceType"))

    @builtins.property
    @jsii.member(jsii_name="attrSshKeyName")
    def attr_ssh_key_name(self) -> builtins.str:
        '''The name of the SSH key pair used by the instance.

        :cloudformationAttribute: SshKeyName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSshKeyName"))

    @builtins.property
    @jsii.member(jsii_name="attrStateCode")
    def attr_state_code(self) -> jsii.Number:
        '''The status code of the instance.

        :cloudformationAttribute: State.Code
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrStateCode"))

    @builtins.property
    @jsii.member(jsii_name="attrStateName")
    def attr_state_name(self) -> builtins.str:
        '''The state of the instance (for example, ``running`` or ``pending`` ).

        :cloudformationAttribute: State.Name
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStateName"))

    @builtins.property
    @jsii.member(jsii_name="attrSupportCode")
    def attr_support_code(self) -> builtins.str:
        '''The support code of the instance.

        Include this code in your email to support when you have questions about an instance or another resource in Lightsail . This code helps our support team to look up your Lightsail information.

        :cloudformationAttribute: SupportCode
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSupportCode"))

    @builtins.property
    @jsii.member(jsii_name="attrUserName")
    def attr_user_name(self) -> builtins.str:
        '''The user name for connecting to the instance (for example, ``ec2-user`` ).

        :cloudformationAttribute: UserName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUserName"))

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
    @jsii.member(jsii_name="blueprintId")
    def blueprint_id(self) -> builtins.str:
        '''The blueprint ID for the instance (for example, ``os_amlinux_2016_03`` ).'''
        return typing.cast(builtins.str, jsii.get(self, "blueprintId"))

    @blueprint_id.setter
    def blueprint_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c902440458adfe1266e3dc96225288d15ecf1c1d8bba26d793d37881c351c773)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "blueprintId", value)

    @builtins.property
    @jsii.member(jsii_name="bundleId")
    def bundle_id(self) -> builtins.str:
        '''The bundle ID for the instance (for example, ``micro_1_0`` ).'''
        return typing.cast(builtins.str, jsii.get(self, "bundleId"))

    @bundle_id.setter
    def bundle_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f5e85e9ad23cc8571347b8c2e46e5f249ca7334ed4d54786f85f9f55b4b4261)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bundleId", value)

    @builtins.property
    @jsii.member(jsii_name="instanceName")
    def instance_name(self) -> builtins.str:
        '''The name of the instance.'''
        return typing.cast(builtins.str, jsii.get(self, "instanceName"))

    @instance_name.setter
    def instance_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ff4c2b7a1d245d5744d6342d2f0a8f108daf28fd2169d869ecec762579a76da)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceName", value)

    @builtins.property
    @jsii.member(jsii_name="addOns")
    def add_ons(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInstance.AddOnProperty"]]]]:
        '''An array of add-ons for the instance.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInstance.AddOnProperty"]]]], jsii.get(self, "addOns"))

    @add_ons.setter
    def add_ons(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInstance.AddOnProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a099dffb98d8133f25aa3f4894f04b7838ec68531bc89457bc7ca10ffe65fe77)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "addOns", value)

    @builtins.property
    @jsii.member(jsii_name="availabilityZone")
    def availability_zone(self) -> typing.Optional[builtins.str]:
        '''The Availability Zone for the instance.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "availabilityZone"))

    @availability_zone.setter
    def availability_zone(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9a56dd4f393fedcb7fc5c77d31a9635f61996dce654f144f2bb3f59379891d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availabilityZone", value)

    @builtins.property
    @jsii.member(jsii_name="hardware")
    def hardware(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInstance.HardwareProperty"]]:
        '''The hardware properties for the instance, such as the vCPU count, attached disks, and amount of RAM.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInstance.HardwareProperty"]], jsii.get(self, "hardware"))

    @hardware.setter
    def hardware(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInstance.HardwareProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__918e77b58ce707e3fd0fe417aa8b0279b976fecbc63c99bf33fb6c34fb56e06f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hardware", value)

    @builtins.property
    @jsii.member(jsii_name="keyPairName")
    def key_pair_name(self) -> typing.Optional[builtins.str]:
        '''The name of the key pair to use for the instance.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyPairName"))

    @key_pair_name.setter
    def key_pair_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e99199ed725a507d6941324fca99a5c014fd317cd07b24dacef00536be31eb87)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyPairName", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInstance.LocationProperty"]]:
        '''The location for the instance, such as the AWS Region and Availability Zone.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInstance.LocationProperty"]], jsii.get(self, "location"))

    @location.setter
    def location(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInstance.LocationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1796032b802331052ff1dc453b46bc6f3d89e44ed47ae0a3b75c51d5f4ec330f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="networking")
    def networking(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInstance.NetworkingProperty"]]:
        '''The public ports and the monthly amount of data transfer allocated for the instance.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInstance.NetworkingProperty"]], jsii.get(self, "networking"))

    @networking.setter
    def networking(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInstance.NetworkingProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ae0605c3ecf986c476ae405f626b73a0ead2ba85a44089e88662ab1e59b4436)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networking", value)

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInstance.StateProperty"]]:
        '''The status code and the state (for example, ``running`` ) of the instance.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInstance.StateProperty"]], jsii.get(self, "state"))

    @state.setter
    def state(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInstance.StateProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8016843d96a81bf84ad05c8259de853033dbbd7a359485955cea3d46de80c536)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "state", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af09458d52eaea13266eac32d46975c0c7fb0afae18d4af7c41cdbda91b257f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="userData")
    def user_data(self) -> typing.Optional[builtins.str]:
        '''The optional launch script for the instance.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userData"))

    @user_data.setter
    def user_data(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b37ad7b78e9dfd25f54548408e5d1989fcb19258bb2e95aff2742713f8eca62)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userData", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lightsail.CfnInstance.AddOnProperty",
        jsii_struct_bases=[],
        name_mapping={
            "add_on_type": "addOnType",
            "auto_snapshot_add_on_request": "autoSnapshotAddOnRequest",
            "status": "status",
        },
    )
    class AddOnProperty:
        def __init__(
            self,
            *,
            add_on_type: builtins.str,
            auto_snapshot_add_on_request: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInstance.AutoSnapshotAddOnProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            status: typing.Optional[builtins.str] = None,
        ) -> None:
            '''``AddOn`` is a property of the `AWS::Lightsail::Instance <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html>`_ resource. It describes the add-ons for an instance.

            :param add_on_type: The add-on type (for example, ``AutoSnapshot`` ). .. epigraph:: ``AutoSnapshot`` is the only add-on that can be enabled for an instance.
            :param auto_snapshot_add_on_request: The parameters for the automatic snapshot add-on, such as the daily time when an automatic snapshot will be created.
            :param status: The status of the add-on. Valid Values: ``Enabled`` | ``Disabled``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-addon.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lightsail as lightsail
                
                add_on_property = lightsail.CfnInstance.AddOnProperty(
                    add_on_type="addOnType",
                
                    # the properties below are optional
                    auto_snapshot_add_on_request=lightsail.CfnInstance.AutoSnapshotAddOnProperty(
                        snapshot_time_of_day="snapshotTimeOfDay"
                    ),
                    status="status"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__02dc099cd32004362b392684e938362aec7ce6a9b6b301a80e7139a71b96c02c)
                check_type(argname="argument add_on_type", value=add_on_type, expected_type=type_hints["add_on_type"])
                check_type(argname="argument auto_snapshot_add_on_request", value=auto_snapshot_add_on_request, expected_type=type_hints["auto_snapshot_add_on_request"])
                check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "add_on_type": add_on_type,
            }
            if auto_snapshot_add_on_request is not None:
                self._values["auto_snapshot_add_on_request"] = auto_snapshot_add_on_request
            if status is not None:
                self._values["status"] = status

        @builtins.property
        def add_on_type(self) -> builtins.str:
            '''The add-on type (for example, ``AutoSnapshot`` ).

            .. epigraph::

               ``AutoSnapshot`` is the only add-on that can be enabled for an instance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-addon.html#cfn-lightsail-instance-addon-addontype
            '''
            result = self._values.get("add_on_type")
            assert result is not None, "Required property 'add_on_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def auto_snapshot_add_on_request(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInstance.AutoSnapshotAddOnProperty"]]:
            '''The parameters for the automatic snapshot add-on, such as the daily time when an automatic snapshot will be created.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-addon.html#cfn-lightsail-instance-addon-autosnapshotaddonrequest
            '''
            result = self._values.get("auto_snapshot_add_on_request")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInstance.AutoSnapshotAddOnProperty"]], result)

        @builtins.property
        def status(self) -> typing.Optional[builtins.str]:
            '''The status of the add-on.

            Valid Values: ``Enabled`` | ``Disabled``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-addon.html#cfn-lightsail-instance-addon-status
            '''
            result = self._values.get("status")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AddOnProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lightsail.CfnInstance.AutoSnapshotAddOnProperty",
        jsii_struct_bases=[],
        name_mapping={"snapshot_time_of_day": "snapshotTimeOfDay"},
    )
    class AutoSnapshotAddOnProperty:
        def __init__(
            self,
            *,
            snapshot_time_of_day: typing.Optional[builtins.str] = None,
        ) -> None:
            '''``AutoSnapshotAddOn`` is a property of the `AddOn <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-addon.html>`_ property. It describes the automatic snapshot add-on for an instance.

            :param snapshot_time_of_day: The daily time when an automatic snapshot will be created. Constraints: - Must be in ``HH:00`` format, and in an hourly increment. - Specified in Coordinated Universal Time (UTC). - The snapshot will be automatically created between the time specified and up to 45 minutes after.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-autosnapshotaddon.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lightsail as lightsail
                
                auto_snapshot_add_on_property = lightsail.CfnInstance.AutoSnapshotAddOnProperty(
                    snapshot_time_of_day="snapshotTimeOfDay"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3379f4d4976801e9abba5d85ecd4fc5cb5104c9adb4340cfc90ee57b933f326b)
                check_type(argname="argument snapshot_time_of_day", value=snapshot_time_of_day, expected_type=type_hints["snapshot_time_of_day"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if snapshot_time_of_day is not None:
                self._values["snapshot_time_of_day"] = snapshot_time_of_day

        @builtins.property
        def snapshot_time_of_day(self) -> typing.Optional[builtins.str]:
            '''The daily time when an automatic snapshot will be created.

            Constraints:

            - Must be in ``HH:00`` format, and in an hourly increment.
            - Specified in Coordinated Universal Time (UTC).
            - The snapshot will be automatically created between the time specified and up to 45 minutes after.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-autosnapshotaddon.html#cfn-lightsail-instance-autosnapshotaddon-snapshottimeofday
            '''
            result = self._values.get("snapshot_time_of_day")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AutoSnapshotAddOnProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lightsail.CfnInstance.DiskProperty",
        jsii_struct_bases=[],
        name_mapping={
            "disk_name": "diskName",
            "path": "path",
            "attached_to": "attachedTo",
            "attachment_state": "attachmentState",
            "iops": "iops",
            "is_system_disk": "isSystemDisk",
            "size_in_gb": "sizeInGb",
        },
    )
    class DiskProperty:
        def __init__(
            self,
            *,
            disk_name: builtins.str,
            path: builtins.str,
            attached_to: typing.Optional[builtins.str] = None,
            attachment_state: typing.Optional[builtins.str] = None,
            iops: typing.Optional[jsii.Number] = None,
            is_system_disk: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            size_in_gb: typing.Optional[builtins.str] = None,
        ) -> None:
            '''``Disk`` is a property of the `Hardware <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-hardware.html>`_ property. It describes a disk attached to an instance.

            :param disk_name: The unique name of the disk.
            :param path: The disk path.
            :param attached_to: The resources to which the disk is attached.
            :param attachment_state: (Deprecated) The attachment state of the disk. .. epigraph:: In releases prior to November 14, 2017, this parameter returned ``attached`` for system disks in the API response. It is now deprecated, but still included in the response. Use ``isAttached`` instead.
            :param iops: The input/output operations per second (IOPS) of the disk.
            :param is_system_disk: A Boolean value indicating whether this disk is a system disk (has an operating system loaded on it).
            :param size_in_gb: The size of the disk in GB.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-disk.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lightsail as lightsail
                
                disk_property = lightsail.CfnInstance.DiskProperty(
                    disk_name="diskName",
                    path="path",
                
                    # the properties below are optional
                    attached_to="attachedTo",
                    attachment_state="attachmentState",
                    iops=123,
                    is_system_disk=False,
                    size_in_gb="sizeInGb"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0463034a2cc858b33422d6128a4dfb2d16fb633c63e6c0729f35dc20125c37c4)
                check_type(argname="argument disk_name", value=disk_name, expected_type=type_hints["disk_name"])
                check_type(argname="argument path", value=path, expected_type=type_hints["path"])
                check_type(argname="argument attached_to", value=attached_to, expected_type=type_hints["attached_to"])
                check_type(argname="argument attachment_state", value=attachment_state, expected_type=type_hints["attachment_state"])
                check_type(argname="argument iops", value=iops, expected_type=type_hints["iops"])
                check_type(argname="argument is_system_disk", value=is_system_disk, expected_type=type_hints["is_system_disk"])
                check_type(argname="argument size_in_gb", value=size_in_gb, expected_type=type_hints["size_in_gb"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "disk_name": disk_name,
                "path": path,
            }
            if attached_to is not None:
                self._values["attached_to"] = attached_to
            if attachment_state is not None:
                self._values["attachment_state"] = attachment_state
            if iops is not None:
                self._values["iops"] = iops
            if is_system_disk is not None:
                self._values["is_system_disk"] = is_system_disk
            if size_in_gb is not None:
                self._values["size_in_gb"] = size_in_gb

        @builtins.property
        def disk_name(self) -> builtins.str:
            '''The unique name of the disk.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-disk.html#cfn-lightsail-instance-disk-diskname
            '''
            result = self._values.get("disk_name")
            assert result is not None, "Required property 'disk_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def path(self) -> builtins.str:
            '''The disk path.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-disk.html#cfn-lightsail-instance-disk-path
            '''
            result = self._values.get("path")
            assert result is not None, "Required property 'path' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def attached_to(self) -> typing.Optional[builtins.str]:
            '''The resources to which the disk is attached.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-disk.html#cfn-lightsail-instance-disk-attachedto
            '''
            result = self._values.get("attached_to")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def attachment_state(self) -> typing.Optional[builtins.str]:
            '''(Deprecated) The attachment state of the disk.

            .. epigraph::

               In releases prior to November 14, 2017, this parameter returned ``attached`` for system disks in the API response. It is now deprecated, but still included in the response. Use ``isAttached`` instead.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-disk.html#cfn-lightsail-instance-disk-attachmentstate
            '''
            result = self._values.get("attachment_state")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def iops(self) -> typing.Optional[jsii.Number]:
            '''The input/output operations per second (IOPS) of the disk.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-disk.html#cfn-lightsail-instance-disk-iops
            '''
            result = self._values.get("iops")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def is_system_disk(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''A Boolean value indicating whether this disk is a system disk (has an operating system loaded on it).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-disk.html#cfn-lightsail-instance-disk-issystemdisk
            '''
            result = self._values.get("is_system_disk")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def size_in_gb(self) -> typing.Optional[builtins.str]:
            '''The size of the disk in GB.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-disk.html#cfn-lightsail-instance-disk-sizeingb
            '''
            result = self._values.get("size_in_gb")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DiskProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lightsail.CfnInstance.HardwareProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cpu_count": "cpuCount",
            "disks": "disks",
            "ram_size_in_gb": "ramSizeInGb",
        },
    )
    class HardwareProperty:
        def __init__(
            self,
            *,
            cpu_count: typing.Optional[jsii.Number] = None,
            disks: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInstance.DiskProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            ram_size_in_gb: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''``Hardware`` is a property of the `AWS::Lightsail::Instance <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html>`_ resource. It describes the hardware properties for the instance, such as the vCPU count, attached disks, and amount of RAM.

            :param cpu_count: The number of vCPUs the instance has. .. epigraph:: The ``CpuCount`` property is read-only and should not be specified in a create instance or update instance request.
            :param disks: The disks attached to the instance. The instance restarts when performing an attach disk or detach disk request. This resets the public IP address of your instance if a static IP isn't attached to it.
            :param ram_size_in_gb: The amount of RAM in GB on the instance (for example, ``1.0`` ). .. epigraph:: The ``RamSizeInGb`` property is read-only and should not be specified in a create instance or update instance request.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-hardware.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lightsail as lightsail
                
                hardware_property = lightsail.CfnInstance.HardwareProperty(
                    cpu_count=123,
                    disks=[lightsail.CfnInstance.DiskProperty(
                        disk_name="diskName",
                        path="path",
                
                        # the properties below are optional
                        attached_to="attachedTo",
                        attachment_state="attachmentState",
                        iops=123,
                        is_system_disk=False,
                        size_in_gb="sizeInGb"
                    )],
                    ram_size_in_gb=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cf4e04cb05bf874499d602adfa37eca6eb395e84f62083580547a6d07384e740)
                check_type(argname="argument cpu_count", value=cpu_count, expected_type=type_hints["cpu_count"])
                check_type(argname="argument disks", value=disks, expected_type=type_hints["disks"])
                check_type(argname="argument ram_size_in_gb", value=ram_size_in_gb, expected_type=type_hints["ram_size_in_gb"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if cpu_count is not None:
                self._values["cpu_count"] = cpu_count
            if disks is not None:
                self._values["disks"] = disks
            if ram_size_in_gb is not None:
                self._values["ram_size_in_gb"] = ram_size_in_gb

        @builtins.property
        def cpu_count(self) -> typing.Optional[jsii.Number]:
            '''The number of vCPUs the instance has.

            .. epigraph::

               The ``CpuCount`` property is read-only and should not be specified in a create instance or update instance request.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-hardware.html#cfn-lightsail-instance-hardware-cpucount
            '''
            result = self._values.get("cpu_count")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def disks(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInstance.DiskProperty"]]]]:
            '''The disks attached to the instance.

            The instance restarts when performing an attach disk or detach disk request. This resets the public IP address of your instance if a static IP isn't attached to it.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-hardware.html#cfn-lightsail-instance-hardware-disks
            '''
            result = self._values.get("disks")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInstance.DiskProperty"]]]], result)

        @builtins.property
        def ram_size_in_gb(self) -> typing.Optional[jsii.Number]:
            '''The amount of RAM in GB on the instance (for example, ``1.0`` ).

            .. epigraph::

               The ``RamSizeInGb`` property is read-only and should not be specified in a create instance or update instance request.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-hardware.html#cfn-lightsail-instance-hardware-ramsizeingb
            '''
            result = self._values.get("ram_size_in_gb")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HardwareProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lightsail.CfnInstance.LocationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "availability_zone": "availabilityZone",
            "region_name": "regionName",
        },
    )
    class LocationProperty:
        def __init__(
            self,
            *,
            availability_zone: typing.Optional[builtins.str] = None,
            region_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''``Location`` is a property of the `AWS::Lightsail::Instance <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html>`_ resource. It describes the location for an instance.

            :param availability_zone: The Availability Zone for the instance.
            :param region_name: The name of the AWS Region for the instance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-location.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lightsail as lightsail
                
                location_property = lightsail.CfnInstance.LocationProperty(
                    availability_zone="availabilityZone",
                    region_name="regionName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__42891a6c84f248f5fa55c61278147e8c2099067282ab557ea17c9ca87b6139fb)
                check_type(argname="argument availability_zone", value=availability_zone, expected_type=type_hints["availability_zone"])
                check_type(argname="argument region_name", value=region_name, expected_type=type_hints["region_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if availability_zone is not None:
                self._values["availability_zone"] = availability_zone
            if region_name is not None:
                self._values["region_name"] = region_name

        @builtins.property
        def availability_zone(self) -> typing.Optional[builtins.str]:
            '''The Availability Zone for the instance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-location.html#cfn-lightsail-instance-location-availabilityzone
            '''
            result = self._values.get("availability_zone")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def region_name(self) -> typing.Optional[builtins.str]:
            '''The name of the AWS Region for the instance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-location.html#cfn-lightsail-instance-location-regionname
            '''
            result = self._values.get("region_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lightsail.CfnInstance.MonthlyTransferProperty",
        jsii_struct_bases=[],
        name_mapping={"gb_per_month_allocated": "gbPerMonthAllocated"},
    )
    class MonthlyTransferProperty:
        def __init__(
            self,
            *,
            gb_per_month_allocated: typing.Optional[builtins.str] = None,
        ) -> None:
            '''``MonthlyTransfer`` is a property of the `Networking <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-networking.html>`_ property. It describes the amount of allocated monthly data transfer (in GB) for an instance.

            :param gb_per_month_allocated: The amount of allocated monthly data transfer (in GB) for an instance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-monthlytransfer.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lightsail as lightsail
                
                monthly_transfer_property = lightsail.CfnInstance.MonthlyTransferProperty(
                    gb_per_month_allocated="gbPerMonthAllocated"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__011a40f828871b8a7d528d71ece98fab8b8e3b2ee997c8468da4950f05813b90)
                check_type(argname="argument gb_per_month_allocated", value=gb_per_month_allocated, expected_type=type_hints["gb_per_month_allocated"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if gb_per_month_allocated is not None:
                self._values["gb_per_month_allocated"] = gb_per_month_allocated

        @builtins.property
        def gb_per_month_allocated(self) -> typing.Optional[builtins.str]:
            '''The amount of allocated monthly data transfer (in GB) for an instance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-monthlytransfer.html#cfn-lightsail-instance-monthlytransfer-gbpermonthallocated
            '''
            result = self._values.get("gb_per_month_allocated")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonthlyTransferProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lightsail.CfnInstance.NetworkingProperty",
        jsii_struct_bases=[],
        name_mapping={"ports": "ports", "monthly_transfer": "monthlyTransfer"},
    )
    class NetworkingProperty:
        def __init__(
            self,
            *,
            ports: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInstance.PortProperty", typing.Dict[builtins.str, typing.Any]]]]],
            monthly_transfer: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''``Networking`` is a property of the `AWS::Lightsail::Instance <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html>`_ resource. It describes the public ports and the monthly amount of data transfer allocated for the instance.

            :param ports: An array of ports to open on the instance.
            :param monthly_transfer: The monthly amount of data transfer, in GB, allocated for the instance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-networking.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lightsail as lightsail
                
                networking_property = lightsail.CfnInstance.NetworkingProperty(
                    ports=[lightsail.CfnInstance.PortProperty(
                        access_direction="accessDirection",
                        access_from="accessFrom",
                        access_type="accessType",
                        cidr_list_aliases=["cidrListAliases"],
                        cidrs=["cidrs"],
                        common_name="commonName",
                        from_port=123,
                        ipv6_cidrs=["ipv6Cidrs"],
                        protocol="protocol",
                        to_port=123
                    )],
                
                    # the properties below are optional
                    monthly_transfer=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a9aa7120f291685e085f9178bd3e3c7de7699e996ed43a42cba437f80bc78e7a)
                check_type(argname="argument ports", value=ports, expected_type=type_hints["ports"])
                check_type(argname="argument monthly_transfer", value=monthly_transfer, expected_type=type_hints["monthly_transfer"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "ports": ports,
            }
            if monthly_transfer is not None:
                self._values["monthly_transfer"] = monthly_transfer

        @builtins.property
        def ports(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInstance.PortProperty"]]]:
            '''An array of ports to open on the instance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-networking.html#cfn-lightsail-instance-networking-ports
            '''
            result = self._values.get("ports")
            assert result is not None, "Required property 'ports' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInstance.PortProperty"]]], result)

        @builtins.property
        def monthly_transfer(self) -> typing.Optional[jsii.Number]:
            '''The monthly amount of data transfer, in GB, allocated for the instance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-networking.html#cfn-lightsail-instance-networking-monthlytransfer
            '''
            result = self._values.get("monthly_transfer")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NetworkingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lightsail.CfnInstance.PortProperty",
        jsii_struct_bases=[],
        name_mapping={
            "access_direction": "accessDirection",
            "access_from": "accessFrom",
            "access_type": "accessType",
            "cidr_list_aliases": "cidrListAliases",
            "cidrs": "cidrs",
            "common_name": "commonName",
            "from_port": "fromPort",
            "ipv6_cidrs": "ipv6Cidrs",
            "protocol": "protocol",
            "to_port": "toPort",
        },
    )
    class PortProperty:
        def __init__(
            self,
            *,
            access_direction: typing.Optional[builtins.str] = None,
            access_from: typing.Optional[builtins.str] = None,
            access_type: typing.Optional[builtins.str] = None,
            cidr_list_aliases: typing.Optional[typing.Sequence[builtins.str]] = None,
            cidrs: typing.Optional[typing.Sequence[builtins.str]] = None,
            common_name: typing.Optional[builtins.str] = None,
            from_port: typing.Optional[jsii.Number] = None,
            ipv6_cidrs: typing.Optional[typing.Sequence[builtins.str]] = None,
            protocol: typing.Optional[builtins.str] = None,
            to_port: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''``Port`` is a property of the `Networking <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-networking.html>`_ property. It describes information about ports for an instance.

            :param access_direction: The access direction ( ``inbound`` or ``outbound`` ). .. epigraph:: Lightsail currently supports only ``inbound`` access direction.
            :param access_from: The location from which access is allowed. For example, ``Anywhere (0.0.0.0/0)`` , or ``Custom`` if a specific IP address or range of IP addresses is allowed.
            :param access_type: The type of access ( ``Public`` or ``Private`` ).
            :param cidr_list_aliases: An alias that defines access for a preconfigured range of IP addresses. The only alias currently supported is ``lightsail-connect`` , which allows IP addresses of the browser-based RDP/SSH client in the Lightsail console to connect to your instance.
            :param cidrs: The IPv4 address, or range of IPv4 addresses (in CIDR notation) that are allowed to connect to an instance through the ports, and the protocol. .. epigraph:: The ``ipv6Cidrs`` parameter lists the IPv6 addresses that are allowed to connect to an instance. Examples: - To allow the IP address ``192.0.2.44`` , specify ``192.0.2.44`` or ``192.0.2.44/32`` . - To allow the IP addresses ``192.0.2.0`` to ``192.0.2.255`` , specify ``192.0.2.0/24`` .
            :param common_name: The common name of the port information.
            :param from_port: The first port in a range of open ports on an instance. Allowed ports: - TCP and UDP - ``0`` to ``65535`` - ICMP - The ICMP type for IPv4 addresses. For example, specify ``8`` as the ``fromPort`` (ICMP type), and ``-1`` as the ``toPort`` (ICMP code), to enable ICMP Ping. - ICMPv6 - The ICMP type for IPv6 addresses. For example, specify ``128`` as the ``fromPort`` (ICMPv6 type), and ``0`` as ``toPort`` (ICMPv6 code).
            :param ipv6_cidrs: The IPv6 address, or range of IPv6 addresses (in CIDR notation) that are allowed to connect to an instance through the ports, and the protocol. Only devices with an IPv6 address can connect to an instance through IPv6; otherwise, IPv4 should be used. .. epigraph:: The ``cidrs`` parameter lists the IPv4 addresses that are allowed to connect to an instance.
            :param protocol: The IP protocol name. The name can be one of the following: - ``tcp`` - Transmission Control Protocol (TCP) provides reliable, ordered, and error-checked delivery of streamed data between applications running on hosts communicating by an IP network. If you have an application that doesn't require reliable data stream service, use UDP instead. - ``all`` - All transport layer protocol types. - ``udp`` - With User Datagram Protocol (UDP), computer applications can send messages (or datagrams) to other hosts on an Internet Protocol (IP) network. Prior communications are not required to set up transmission channels or data paths. Applications that don't require reliable data stream service can use UDP, which provides a connectionless datagram service that emphasizes reduced latency over reliability. If you do require reliable data stream service, use TCP instead. - ``icmp`` - Internet Control Message Protocol (ICMP) is used to send error messages and operational information indicating success or failure when communicating with an instance. For example, an error is indicated when an instance could not be reached. When you specify ``icmp`` as the ``protocol`` , you must specify the ICMP type using the ``fromPort`` parameter, and ICMP code using the ``toPort`` parameter.
            :param to_port: The last port in a range of open ports on an instance. Allowed ports: - TCP and UDP - ``0`` to ``65535`` - ICMP - The ICMP code for IPv4 addresses. For example, specify ``8`` as the ``fromPort`` (ICMP type), and ``-1`` as the ``toPort`` (ICMP code), to enable ICMP Ping. - ICMPv6 - The ICMP code for IPv6 addresses. For example, specify ``128`` as the ``fromPort`` (ICMPv6 type), and ``0`` as ``toPort`` (ICMPv6 code).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-port.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lightsail as lightsail
                
                port_property = lightsail.CfnInstance.PortProperty(
                    access_direction="accessDirection",
                    access_from="accessFrom",
                    access_type="accessType",
                    cidr_list_aliases=["cidrListAliases"],
                    cidrs=["cidrs"],
                    common_name="commonName",
                    from_port=123,
                    ipv6_cidrs=["ipv6Cidrs"],
                    protocol="protocol",
                    to_port=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3a910b73471578cf7936f197ae2e435d87605ce8b975d2f1a342c41809a845fa)
                check_type(argname="argument access_direction", value=access_direction, expected_type=type_hints["access_direction"])
                check_type(argname="argument access_from", value=access_from, expected_type=type_hints["access_from"])
                check_type(argname="argument access_type", value=access_type, expected_type=type_hints["access_type"])
                check_type(argname="argument cidr_list_aliases", value=cidr_list_aliases, expected_type=type_hints["cidr_list_aliases"])
                check_type(argname="argument cidrs", value=cidrs, expected_type=type_hints["cidrs"])
                check_type(argname="argument common_name", value=common_name, expected_type=type_hints["common_name"])
                check_type(argname="argument from_port", value=from_port, expected_type=type_hints["from_port"])
                check_type(argname="argument ipv6_cidrs", value=ipv6_cidrs, expected_type=type_hints["ipv6_cidrs"])
                check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
                check_type(argname="argument to_port", value=to_port, expected_type=type_hints["to_port"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if access_direction is not None:
                self._values["access_direction"] = access_direction
            if access_from is not None:
                self._values["access_from"] = access_from
            if access_type is not None:
                self._values["access_type"] = access_type
            if cidr_list_aliases is not None:
                self._values["cidr_list_aliases"] = cidr_list_aliases
            if cidrs is not None:
                self._values["cidrs"] = cidrs
            if common_name is not None:
                self._values["common_name"] = common_name
            if from_port is not None:
                self._values["from_port"] = from_port
            if ipv6_cidrs is not None:
                self._values["ipv6_cidrs"] = ipv6_cidrs
            if protocol is not None:
                self._values["protocol"] = protocol
            if to_port is not None:
                self._values["to_port"] = to_port

        @builtins.property
        def access_direction(self) -> typing.Optional[builtins.str]:
            '''The access direction ( ``inbound`` or ``outbound`` ).

            .. epigraph::

               Lightsail currently supports only ``inbound`` access direction.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-port.html#cfn-lightsail-instance-port-accessdirection
            '''
            result = self._values.get("access_direction")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def access_from(self) -> typing.Optional[builtins.str]:
            '''The location from which access is allowed.

            For example, ``Anywhere (0.0.0.0/0)`` , or ``Custom`` if a specific IP address or range of IP addresses is allowed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-port.html#cfn-lightsail-instance-port-accessfrom
            '''
            result = self._values.get("access_from")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def access_type(self) -> typing.Optional[builtins.str]:
            '''The type of access ( ``Public`` or ``Private`` ).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-port.html#cfn-lightsail-instance-port-accesstype
            '''
            result = self._values.get("access_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def cidr_list_aliases(self) -> typing.Optional[typing.List[builtins.str]]:
            '''An alias that defines access for a preconfigured range of IP addresses.

            The only alias currently supported is ``lightsail-connect`` , which allows IP addresses of the browser-based RDP/SSH client in the Lightsail console to connect to your instance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-port.html#cfn-lightsail-instance-port-cidrlistaliases
            '''
            result = self._values.get("cidr_list_aliases")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def cidrs(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The IPv4 address, or range of IPv4 addresses (in CIDR notation) that are allowed to connect to an instance through the ports, and the protocol.

            .. epigraph::

               The ``ipv6Cidrs`` parameter lists the IPv6 addresses that are allowed to connect to an instance.

            Examples:

            - To allow the IP address ``192.0.2.44`` , specify ``192.0.2.44`` or ``192.0.2.44/32`` .
            - To allow the IP addresses ``192.0.2.0`` to ``192.0.2.255`` , specify ``192.0.2.0/24`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-port.html#cfn-lightsail-instance-port-cidrs
            '''
            result = self._values.get("cidrs")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def common_name(self) -> typing.Optional[builtins.str]:
            '''The common name of the port information.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-port.html#cfn-lightsail-instance-port-commonname
            '''
            result = self._values.get("common_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def from_port(self) -> typing.Optional[jsii.Number]:
            '''The first port in a range of open ports on an instance.

            Allowed ports:

            - TCP and UDP - ``0`` to ``65535``
            - ICMP - The ICMP type for IPv4 addresses. For example, specify ``8`` as the ``fromPort`` (ICMP type), and ``-1`` as the ``toPort`` (ICMP code), to enable ICMP Ping.
            - ICMPv6 - The ICMP type for IPv6 addresses. For example, specify ``128`` as the ``fromPort`` (ICMPv6 type), and ``0`` as ``toPort`` (ICMPv6 code).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-port.html#cfn-lightsail-instance-port-fromport
            '''
            result = self._values.get("from_port")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def ipv6_cidrs(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The IPv6 address, or range of IPv6 addresses (in CIDR notation) that are allowed to connect to an instance through the ports, and the protocol.

            Only devices with an IPv6 address can connect to an instance through IPv6; otherwise, IPv4 should be used.
            .. epigraph::

               The ``cidrs`` parameter lists the IPv4 addresses that are allowed to connect to an instance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-port.html#cfn-lightsail-instance-port-ipv6cidrs
            '''
            result = self._values.get("ipv6_cidrs")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def protocol(self) -> typing.Optional[builtins.str]:
            '''The IP protocol name.

            The name can be one of the following:

            - ``tcp`` - Transmission Control Protocol (TCP) provides reliable, ordered, and error-checked delivery of streamed data between applications running on hosts communicating by an IP network. If you have an application that doesn't require reliable data stream service, use UDP instead.
            - ``all`` - All transport layer protocol types.
            - ``udp`` - With User Datagram Protocol (UDP), computer applications can send messages (or datagrams) to other hosts on an Internet Protocol (IP) network. Prior communications are not required to set up transmission channels or data paths. Applications that don't require reliable data stream service can use UDP, which provides a connectionless datagram service that emphasizes reduced latency over reliability. If you do require reliable data stream service, use TCP instead.
            - ``icmp`` - Internet Control Message Protocol (ICMP) is used to send error messages and operational information indicating success or failure when communicating with an instance. For example, an error is indicated when an instance could not be reached. When you specify ``icmp`` as the ``protocol`` , you must specify the ICMP type using the ``fromPort`` parameter, and ICMP code using the ``toPort`` parameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-port.html#cfn-lightsail-instance-port-protocol
            '''
            result = self._values.get("protocol")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def to_port(self) -> typing.Optional[jsii.Number]:
            '''The last port in a range of open ports on an instance.

            Allowed ports:

            - TCP and UDP - ``0`` to ``65535``
            - ICMP - The ICMP code for IPv4 addresses. For example, specify ``8`` as the ``fromPort`` (ICMP type), and ``-1`` as the ``toPort`` (ICMP code), to enable ICMP Ping.
            - ICMPv6 - The ICMP code for IPv6 addresses. For example, specify ``128`` as the ``fromPort`` (ICMPv6 type), and ``0`` as ``toPort`` (ICMPv6 code).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-port.html#cfn-lightsail-instance-port-toport
            '''
            result = self._values.get("to_port")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PortProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lightsail.CfnInstance.StateProperty",
        jsii_struct_bases=[],
        name_mapping={"code": "code", "name": "name"},
    )
    class StateProperty:
        def __init__(
            self,
            *,
            code: typing.Optional[jsii.Number] = None,
            name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''``State`` is a property of the `AWS::Lightsail::Instance <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html>`_ resource. It describes the status code and the state (for example, ``running`` ) of an instance.

            :param code: The status code of the instance.
            :param name: The state of the instance (for example, ``running`` or ``pending`` ).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-state.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lightsail as lightsail
                
                state_property = lightsail.CfnInstance.StateProperty(
                    code=123,
                    name="name"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5e9f9e996c0dfa91ed16946148a8dc76af0067f4e87e53af0be16aa75d5f4e42)
                check_type(argname="argument code", value=code, expected_type=type_hints["code"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if code is not None:
                self._values["code"] = code
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def code(self) -> typing.Optional[jsii.Number]:
            '''The status code of the instance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-state.html#cfn-lightsail-instance-state-code
            '''
            result = self._values.get("code")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The state of the instance (for example, ``running`` or ``pending`` ).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-state.html#cfn-lightsail-instance-state-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_lightsail.CfnInstanceProps",
    jsii_struct_bases=[],
    name_mapping={
        "blueprint_id": "blueprintId",
        "bundle_id": "bundleId",
        "instance_name": "instanceName",
        "add_ons": "addOns",
        "availability_zone": "availabilityZone",
        "hardware": "hardware",
        "key_pair_name": "keyPairName",
        "location": "location",
        "networking": "networking",
        "state": "state",
        "tags": "tags",
        "user_data": "userData",
    },
)
class CfnInstanceProps:
    def __init__(
        self,
        *,
        blueprint_id: builtins.str,
        bundle_id: builtins.str,
        instance_name: builtins.str,
        add_ons: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstance.AddOnProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        availability_zone: typing.Optional[builtins.str] = None,
        hardware: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstance.HardwareProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        key_pair_name: typing.Optional[builtins.str] = None,
        location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstance.LocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        networking: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstance.NetworkingProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        state: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstance.StateProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        user_data: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnInstance``.

        :param blueprint_id: The blueprint ID for the instance (for example, ``os_amlinux_2016_03`` ).
        :param bundle_id: The bundle ID for the instance (for example, ``micro_1_0`` ).
        :param instance_name: The name of the instance.
        :param add_ons: An array of add-ons for the instance. .. epigraph:: If the instance has an add-on enabled when performing a delete instance request, the add-on is automatically disabled before the instance is deleted.
        :param availability_zone: The Availability Zone for the instance.
        :param hardware: The hardware properties for the instance, such as the vCPU count, attached disks, and amount of RAM. .. epigraph:: The instance restarts when performing an attach disk or detach disk request. This resets the public IP address of your instance if a static IP isn't attached to it.
        :param key_pair_name: The name of the key pair to use for the instance. If no key pair name is specified, the Regional Lightsail default key pair is used.
        :param location: The location for the instance, such as the AWS Region and Availability Zone. .. epigraph:: The ``Location`` property is read-only and should not be specified in a create instance or update instance request.
        :param networking: The public ports and the monthly amount of data transfer allocated for the instance.
        :param state: The status code and the state (for example, ``running`` ) of the instance. .. epigraph:: The ``State`` property is read-only and should not be specified in a create instance or update instance request.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ in the *AWS CloudFormation User Guide* . .. epigraph:: The ``Value`` of ``Tags`` is optional for Lightsail resources.
        :param user_data: The optional launch script for the instance. Specify a launch script to configure an instance with additional user data. For example, you might want to specify ``apt-get -y update`` as a launch script. .. epigraph:: Depending on the blueprint of your instance, the command to get software on your instance varies. Amazon Linux and CentOS use ``yum`` , Debian and Ubuntu use ``apt-get`` , and FreeBSD uses ``pkg`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_lightsail as lightsail
            
            cfn_instance_props = lightsail.CfnInstanceProps(
                blueprint_id="blueprintId",
                bundle_id="bundleId",
                instance_name="instanceName",
            
                # the properties below are optional
                add_ons=[lightsail.CfnInstance.AddOnProperty(
                    add_on_type="addOnType",
            
                    # the properties below are optional
                    auto_snapshot_add_on_request=lightsail.CfnInstance.AutoSnapshotAddOnProperty(
                        snapshot_time_of_day="snapshotTimeOfDay"
                    ),
                    status="status"
                )],
                availability_zone="availabilityZone",
                hardware=lightsail.CfnInstance.HardwareProperty(
                    cpu_count=123,
                    disks=[lightsail.CfnInstance.DiskProperty(
                        disk_name="diskName",
                        path="path",
            
                        # the properties below are optional
                        attached_to="attachedTo",
                        attachment_state="attachmentState",
                        iops=123,
                        is_system_disk=False,
                        size_in_gb="sizeInGb"
                    )],
                    ram_size_in_gb=123
                ),
                key_pair_name="keyPairName",
                location=lightsail.CfnInstance.LocationProperty(
                    availability_zone="availabilityZone",
                    region_name="regionName"
                ),
                networking=lightsail.CfnInstance.NetworkingProperty(
                    ports=[lightsail.CfnInstance.PortProperty(
                        access_direction="accessDirection",
                        access_from="accessFrom",
                        access_type="accessType",
                        cidr_list_aliases=["cidrListAliases"],
                        cidrs=["cidrs"],
                        common_name="commonName",
                        from_port=123,
                        ipv6_cidrs=["ipv6Cidrs"],
                        protocol="protocol",
                        to_port=123
                    )],
            
                    # the properties below are optional
                    monthly_transfer=123
                ),
                state=lightsail.CfnInstance.StateProperty(
                    code=123,
                    name="name"
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                user_data="userData"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e0def276816b17135efe655ecd6a1a965ddb59099e6f411660bf2c2e3faeeaa)
            check_type(argname="argument blueprint_id", value=blueprint_id, expected_type=type_hints["blueprint_id"])
            check_type(argname="argument bundle_id", value=bundle_id, expected_type=type_hints["bundle_id"])
            check_type(argname="argument instance_name", value=instance_name, expected_type=type_hints["instance_name"])
            check_type(argname="argument add_ons", value=add_ons, expected_type=type_hints["add_ons"])
            check_type(argname="argument availability_zone", value=availability_zone, expected_type=type_hints["availability_zone"])
            check_type(argname="argument hardware", value=hardware, expected_type=type_hints["hardware"])
            check_type(argname="argument key_pair_name", value=key_pair_name, expected_type=type_hints["key_pair_name"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument networking", value=networking, expected_type=type_hints["networking"])
            check_type(argname="argument state", value=state, expected_type=type_hints["state"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument user_data", value=user_data, expected_type=type_hints["user_data"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "blueprint_id": blueprint_id,
            "bundle_id": bundle_id,
            "instance_name": instance_name,
        }
        if add_ons is not None:
            self._values["add_ons"] = add_ons
        if availability_zone is not None:
            self._values["availability_zone"] = availability_zone
        if hardware is not None:
            self._values["hardware"] = hardware
        if key_pair_name is not None:
            self._values["key_pair_name"] = key_pair_name
        if location is not None:
            self._values["location"] = location
        if networking is not None:
            self._values["networking"] = networking
        if state is not None:
            self._values["state"] = state
        if tags is not None:
            self._values["tags"] = tags
        if user_data is not None:
            self._values["user_data"] = user_data

    @builtins.property
    def blueprint_id(self) -> builtins.str:
        '''The blueprint ID for the instance (for example, ``os_amlinux_2016_03`` ).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-blueprintid
        '''
        result = self._values.get("blueprint_id")
        assert result is not None, "Required property 'blueprint_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bundle_id(self) -> builtins.str:
        '''The bundle ID for the instance (for example, ``micro_1_0`` ).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-bundleid
        '''
        result = self._values.get("bundle_id")
        assert result is not None, "Required property 'bundle_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def instance_name(self) -> builtins.str:
        '''The name of the instance.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-instancename
        '''
        result = self._values.get("instance_name")
        assert result is not None, "Required property 'instance_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def add_ons(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnInstance.AddOnProperty]]]]:
        '''An array of add-ons for the instance.

        .. epigraph::

           If the instance has an add-on enabled when performing a delete instance request, the add-on is automatically disabled before the instance is deleted.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-addons
        '''
        result = self._values.get("add_ons")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnInstance.AddOnProperty]]]], result)

    @builtins.property
    def availability_zone(self) -> typing.Optional[builtins.str]:
        '''The Availability Zone for the instance.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-availabilityzone
        '''
        result = self._values.get("availability_zone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def hardware(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnInstance.HardwareProperty]]:
        '''The hardware properties for the instance, such as the vCPU count, attached disks, and amount of RAM.

        .. epigraph::

           The instance restarts when performing an attach disk or detach disk request. This resets the public IP address of your instance if a static IP isn't attached to it.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-hardware
        '''
        result = self._values.get("hardware")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnInstance.HardwareProperty]], result)

    @builtins.property
    def key_pair_name(self) -> typing.Optional[builtins.str]:
        '''The name of the key pair to use for the instance.

        If no key pair name is specified, the Regional Lightsail default key pair is used.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-keypairname
        '''
        result = self._values.get("key_pair_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def location(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnInstance.LocationProperty]]:
        '''The location for the instance, such as the AWS Region and Availability Zone.

        .. epigraph::

           The ``Location`` property is read-only and should not be specified in a create instance or update instance request.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-location
        '''
        result = self._values.get("location")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnInstance.LocationProperty]], result)

    @builtins.property
    def networking(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnInstance.NetworkingProperty]]:
        '''The public ports and the monthly amount of data transfer allocated for the instance.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-networking
        '''
        result = self._values.get("networking")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnInstance.NetworkingProperty]], result)

    @builtins.property
    def state(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnInstance.StateProperty]]:
        '''The status code and the state (for example, ``running`` ) of the instance.

        .. epigraph::

           The ``State`` property is read-only and should not be specified in a create instance or update instance request.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-state
        '''
        result = self._values.get("state")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnInstance.StateProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ in the *AWS CloudFormation User Guide* .
        .. epigraph::

           The ``Value`` of ``Tags`` is optional for Lightsail resources.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def user_data(self) -> typing.Optional[builtins.str]:
        '''The optional launch script for the instance.

        Specify a launch script to configure an instance with additional user data. For example, you might want to specify ``apt-get -y update`` as a launch script.
        .. epigraph::

           Depending on the blueprint of your instance, the command to get software on your instance varies. Amazon Linux and CentOS use ``yum`` , Debian and Ubuntu use ``apt-get`` , and FreeBSD uses ``pkg`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-userdata
        '''
        result = self._values.get("user_data")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnInstanceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnLoadBalancer(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_lightsail.CfnLoadBalancer",
):
    '''The ``AWS::Lightsail::LoadBalancer`` resource specifies a load balancer that can be used with Lightsail instances.

    .. epigraph::

       You cannot attach a TLS certificate to a load balancer using the ``AWS::Lightsail::LoadBalancer`` resource type. Instead, use the ``AWS::Lightsail::LoadBalancerTlsCertificate`` resource type to create a certificate and attach it to a load balancer.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-loadbalancer.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_lightsail as lightsail
        
        cfn_load_balancer = lightsail.CfnLoadBalancer(self, "MyCfnLoadBalancer",
            instance_port=123,
            load_balancer_name="loadBalancerName",
        
            # the properties below are optional
            attached_instances=["attachedInstances"],
            health_check_path="healthCheckPath",
            ip_address_type="ipAddressType",
            session_stickiness_enabled=False,
            session_stickiness_lb_cookie_duration_seconds="sessionStickinessLbCookieDurationSeconds",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            tls_policy_name="tlsPolicyName"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        instance_port: jsii.Number,
        load_balancer_name: builtins.str,
        attached_instances: typing.Optional[typing.Sequence[builtins.str]] = None,
        health_check_path: typing.Optional[builtins.str] = None,
        ip_address_type: typing.Optional[builtins.str] = None,
        session_stickiness_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        session_stickiness_lb_cookie_duration_seconds: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        tls_policy_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param instance_port: The port that the load balancer uses to direct traffic to your Lightsail instances. For HTTP traffic, specify port ``80`` . For HTTPS traffic, specify port ``443`` .
        :param load_balancer_name: The name of the load balancer.
        :param attached_instances: The Lightsail instances to attach to the load balancer.
        :param health_check_path: The path on the attached instance where the health check will be performed. If no path is specified, the load balancer tries to make a request to the default (root) page ( ``/index.html`` ).
        :param ip_address_type: The IP address type of the load balancer. The possible values are ``ipv4`` for IPv4 only, and ``dualstack`` for both IPv4 and IPv6.
        :param session_stickiness_enabled: A Boolean value indicating whether session stickiness is enabled. Enable session stickiness (also known as *session affinity* ) to bind a user's session to a specific instance. This ensures that all requests from the user during the session are sent to the same instance.
        :param session_stickiness_lb_cookie_duration_seconds: The time period, in seconds, after which the load balancer session stickiness cookie should be considered stale. If you do not specify this parameter, the default value is 0, which indicates that the sticky session should last for the duration of the browser session.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ in the *AWS CloudFormation User Guide* . .. epigraph:: The ``Value`` of ``Tags`` is optional for Lightsail resources.
        :param tls_policy_name: The name of the TLS security policy for the load balancer.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7424f399a4c81195a3832bf4c1d53a1869a11a94a74f58e7efaf927f44364614)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnLoadBalancerProps(
            instance_port=instance_port,
            load_balancer_name=load_balancer_name,
            attached_instances=attached_instances,
            health_check_path=health_check_path,
            ip_address_type=ip_address_type,
            session_stickiness_enabled=session_stickiness_enabled,
            session_stickiness_lb_cookie_duration_seconds=session_stickiness_lb_cookie_duration_seconds,
            tags=tags,
            tls_policy_name=tls_policy_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__31f7abe244f876394bc038308ea33c66bfe259f6bac63c7a7311664365295aae)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e52afad487ef5f48ccd656aebec9f80189f8e70917a767f20754594458adb55c)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrLoadBalancerArn")
    def attr_load_balancer_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the load balancer.

        :cloudformationAttribute: LoadBalancerArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLoadBalancerArn"))

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
    @jsii.member(jsii_name="instancePort")
    def instance_port(self) -> jsii.Number:
        '''The port that the load balancer uses to direct traffic to your Lightsail instances.'''
        return typing.cast(jsii.Number, jsii.get(self, "instancePort"))

    @instance_port.setter
    def instance_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__400516c5f0e10f776899b7edb1e990db4f4a24e3325177548046802d33c26a5f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instancePort", value)

    @builtins.property
    @jsii.member(jsii_name="loadBalancerName")
    def load_balancer_name(self) -> builtins.str:
        '''The name of the load balancer.'''
        return typing.cast(builtins.str, jsii.get(self, "loadBalancerName"))

    @load_balancer_name.setter
    def load_balancer_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e88376ead8f2114df0c93a8a49a09abc0c2aba0302879ce3720d58cee7c2719)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loadBalancerName", value)

    @builtins.property
    @jsii.member(jsii_name="attachedInstances")
    def attached_instances(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The Lightsail instances to attach to the load balancer.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "attachedInstances"))

    @attached_instances.setter
    def attached_instances(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4648ebf266af790248fa827ea484bb236262c06a7cba26c3fb76498f32796266)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "attachedInstances", value)

    @builtins.property
    @jsii.member(jsii_name="healthCheckPath")
    def health_check_path(self) -> typing.Optional[builtins.str]:
        '''The path on the attached instance where the health check will be performed.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "healthCheckPath"))

    @health_check_path.setter
    def health_check_path(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3bb17a4c6a795e8df00992dc4953caa4b3826d13bbd31239cf7e659a8d3a569)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "healthCheckPath", value)

    @builtins.property
    @jsii.member(jsii_name="ipAddressType")
    def ip_address_type(self) -> typing.Optional[builtins.str]:
        '''The IP address type of the load balancer.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipAddressType"))

    @ip_address_type.setter
    def ip_address_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6d2a98739f1d1aac5be4e44af011db153c8aa9cda2208cd4d793ab91d7b024d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipAddressType", value)

    @builtins.property
    @jsii.member(jsii_name="sessionStickinessEnabled")
    def session_stickiness_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''A Boolean value indicating whether session stickiness is enabled.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "sessionStickinessEnabled"))

    @session_stickiness_enabled.setter
    def session_stickiness_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60d3bde218d3bcb6c355f873dd0255f6432fda15433610cbd8c4755bbdabed21)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sessionStickinessEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="sessionStickinessLbCookieDurationSeconds")
    def session_stickiness_lb_cookie_duration_seconds(
        self,
    ) -> typing.Optional[builtins.str]:
        '''The time period, in seconds, after which the load balancer session stickiness cookie should be considered stale.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sessionStickinessLbCookieDurationSeconds"))

    @session_stickiness_lb_cookie_duration_seconds.setter
    def session_stickiness_lb_cookie_duration_seconds(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09c637e41f600eb13a6c074f22338a4435394664f425f957444e9b8dfcf2aa9c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sessionStickinessLbCookieDurationSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__afc022f5045d5ea7f789cb66d1e19f0beb665d810659027059f4ceb4cf6599b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="tlsPolicyName")
    def tls_policy_name(self) -> typing.Optional[builtins.str]:
        '''The name of the TLS security policy for the load balancer.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tlsPolicyName"))

    @tls_policy_name.setter
    def tls_policy_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af314ec18592fe248ceaa789a42b5f2269e8f7ffe3ee545ee0ccc9f2be2dc9b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tlsPolicyName", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_lightsail.CfnLoadBalancerProps",
    jsii_struct_bases=[],
    name_mapping={
        "instance_port": "instancePort",
        "load_balancer_name": "loadBalancerName",
        "attached_instances": "attachedInstances",
        "health_check_path": "healthCheckPath",
        "ip_address_type": "ipAddressType",
        "session_stickiness_enabled": "sessionStickinessEnabled",
        "session_stickiness_lb_cookie_duration_seconds": "sessionStickinessLbCookieDurationSeconds",
        "tags": "tags",
        "tls_policy_name": "tlsPolicyName",
    },
)
class CfnLoadBalancerProps:
    def __init__(
        self,
        *,
        instance_port: jsii.Number,
        load_balancer_name: builtins.str,
        attached_instances: typing.Optional[typing.Sequence[builtins.str]] = None,
        health_check_path: typing.Optional[builtins.str] = None,
        ip_address_type: typing.Optional[builtins.str] = None,
        session_stickiness_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        session_stickiness_lb_cookie_duration_seconds: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        tls_policy_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnLoadBalancer``.

        :param instance_port: The port that the load balancer uses to direct traffic to your Lightsail instances. For HTTP traffic, specify port ``80`` . For HTTPS traffic, specify port ``443`` .
        :param load_balancer_name: The name of the load balancer.
        :param attached_instances: The Lightsail instances to attach to the load balancer.
        :param health_check_path: The path on the attached instance where the health check will be performed. If no path is specified, the load balancer tries to make a request to the default (root) page ( ``/index.html`` ).
        :param ip_address_type: The IP address type of the load balancer. The possible values are ``ipv4`` for IPv4 only, and ``dualstack`` for both IPv4 and IPv6.
        :param session_stickiness_enabled: A Boolean value indicating whether session stickiness is enabled. Enable session stickiness (also known as *session affinity* ) to bind a user's session to a specific instance. This ensures that all requests from the user during the session are sent to the same instance.
        :param session_stickiness_lb_cookie_duration_seconds: The time period, in seconds, after which the load balancer session stickiness cookie should be considered stale. If you do not specify this parameter, the default value is 0, which indicates that the sticky session should last for the duration of the browser session.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ in the *AWS CloudFormation User Guide* . .. epigraph:: The ``Value`` of ``Tags`` is optional for Lightsail resources.
        :param tls_policy_name: The name of the TLS security policy for the load balancer.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-loadbalancer.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_lightsail as lightsail
            
            cfn_load_balancer_props = lightsail.CfnLoadBalancerProps(
                instance_port=123,
                load_balancer_name="loadBalancerName",
            
                # the properties below are optional
                attached_instances=["attachedInstances"],
                health_check_path="healthCheckPath",
                ip_address_type="ipAddressType",
                session_stickiness_enabled=False,
                session_stickiness_lb_cookie_duration_seconds="sessionStickinessLbCookieDurationSeconds",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                tls_policy_name="tlsPolicyName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f2f4d23f6e12e19581cf7aac426cbcebf3bbb277d69cf495d240afd4e81bb5e)
            check_type(argname="argument instance_port", value=instance_port, expected_type=type_hints["instance_port"])
            check_type(argname="argument load_balancer_name", value=load_balancer_name, expected_type=type_hints["load_balancer_name"])
            check_type(argname="argument attached_instances", value=attached_instances, expected_type=type_hints["attached_instances"])
            check_type(argname="argument health_check_path", value=health_check_path, expected_type=type_hints["health_check_path"])
            check_type(argname="argument ip_address_type", value=ip_address_type, expected_type=type_hints["ip_address_type"])
            check_type(argname="argument session_stickiness_enabled", value=session_stickiness_enabled, expected_type=type_hints["session_stickiness_enabled"])
            check_type(argname="argument session_stickiness_lb_cookie_duration_seconds", value=session_stickiness_lb_cookie_duration_seconds, expected_type=type_hints["session_stickiness_lb_cookie_duration_seconds"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tls_policy_name", value=tls_policy_name, expected_type=type_hints["tls_policy_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_port": instance_port,
            "load_balancer_name": load_balancer_name,
        }
        if attached_instances is not None:
            self._values["attached_instances"] = attached_instances
        if health_check_path is not None:
            self._values["health_check_path"] = health_check_path
        if ip_address_type is not None:
            self._values["ip_address_type"] = ip_address_type
        if session_stickiness_enabled is not None:
            self._values["session_stickiness_enabled"] = session_stickiness_enabled
        if session_stickiness_lb_cookie_duration_seconds is not None:
            self._values["session_stickiness_lb_cookie_duration_seconds"] = session_stickiness_lb_cookie_duration_seconds
        if tags is not None:
            self._values["tags"] = tags
        if tls_policy_name is not None:
            self._values["tls_policy_name"] = tls_policy_name

    @builtins.property
    def instance_port(self) -> jsii.Number:
        '''The port that the load balancer uses to direct traffic to your Lightsail instances.

        For HTTP traffic, specify port ``80`` . For HTTPS traffic, specify port ``443`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-loadbalancer.html#cfn-lightsail-loadbalancer-instanceport
        '''
        result = self._values.get("instance_port")
        assert result is not None, "Required property 'instance_port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def load_balancer_name(self) -> builtins.str:
        '''The name of the load balancer.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-loadbalancer.html#cfn-lightsail-loadbalancer-loadbalancername
        '''
        result = self._values.get("load_balancer_name")
        assert result is not None, "Required property 'load_balancer_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def attached_instances(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The Lightsail instances to attach to the load balancer.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-loadbalancer.html#cfn-lightsail-loadbalancer-attachedinstances
        '''
        result = self._values.get("attached_instances")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def health_check_path(self) -> typing.Optional[builtins.str]:
        '''The path on the attached instance where the health check will be performed.

        If no path is specified, the load balancer tries to make a request to the default (root) page ( ``/index.html`` ).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-loadbalancer.html#cfn-lightsail-loadbalancer-healthcheckpath
        '''
        result = self._values.get("health_check_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ip_address_type(self) -> typing.Optional[builtins.str]:
        '''The IP address type of the load balancer.

        The possible values are ``ipv4`` for IPv4 only, and ``dualstack`` for both IPv4 and IPv6.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-loadbalancer.html#cfn-lightsail-loadbalancer-ipaddresstype
        '''
        result = self._values.get("ip_address_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def session_stickiness_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''A Boolean value indicating whether session stickiness is enabled.

        Enable session stickiness (also known as *session affinity* ) to bind a user's session to a specific instance. This ensures that all requests from the user during the session are sent to the same instance.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-loadbalancer.html#cfn-lightsail-loadbalancer-sessionstickinessenabled
        '''
        result = self._values.get("session_stickiness_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def session_stickiness_lb_cookie_duration_seconds(
        self,
    ) -> typing.Optional[builtins.str]:
        '''The time period, in seconds, after which the load balancer session stickiness cookie should be considered stale.

        If you do not specify this parameter, the default value is 0, which indicates that the sticky session should last for the duration of the browser session.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-loadbalancer.html#cfn-lightsail-loadbalancer-sessionstickinesslbcookiedurationseconds
        '''
        result = self._values.get("session_stickiness_lb_cookie_duration_seconds")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ in the *AWS CloudFormation User Guide* .
        .. epigraph::

           The ``Value`` of ``Tags`` is optional for Lightsail resources.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-loadbalancer.html#cfn-lightsail-loadbalancer-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def tls_policy_name(self) -> typing.Optional[builtins.str]:
        '''The name of the TLS security policy for the load balancer.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-loadbalancer.html#cfn-lightsail-loadbalancer-tlspolicyname
        '''
        result = self._values.get("tls_policy_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLoadBalancerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnLoadBalancerTlsCertificate(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_lightsail.CfnLoadBalancerTlsCertificate",
):
    '''The ``AWS::Lightsail::LoadBalancerTlsCertificate`` resource specifies a TLS certificate that can be used with a Lightsail load balancer.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-loadbalancertlscertificate.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_lightsail as lightsail
        
        cfn_load_balancer_tls_certificate = lightsail.CfnLoadBalancerTlsCertificate(self, "MyCfnLoadBalancerTlsCertificate",
            certificate_domain_name="certificateDomainName",
            certificate_name="certificateName",
            load_balancer_name="loadBalancerName",
        
            # the properties below are optional
            certificate_alternative_names=["certificateAlternativeNames"],
            https_redirection_enabled=False,
            is_attached=False
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        certificate_domain_name: builtins.str,
        certificate_name: builtins.str,
        load_balancer_name: builtins.str,
        certificate_alternative_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        https_redirection_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        is_attached: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param certificate_domain_name: The domain name for the SSL/TLS certificate. For example, ``example.com`` or ``www.example.com`` .
        :param certificate_name: The name of the SSL/TLS certificate.
        :param load_balancer_name: The name of the load balancer that the SSL/TLS certificate is attached to.
        :param certificate_alternative_names: An array of alternative domain names and subdomain names for your SSL/TLS certificate. In addition to the primary domain name, you can have up to nine alternative domain names. Wildcards (such as ``*.example.com`` ) are not supported.
        :param https_redirection_enabled: A Boolean value indicating whether HTTPS redirection is enabled for the load balancer that the TLS certificate is attached to.
        :param is_attached: A Boolean value indicating whether the SSL/TLS certificate is attached to a Lightsail load balancer.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0690a757a43538375584bafa46effdc256cd7146a3c192b0c4ff30490e4544e3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnLoadBalancerTlsCertificateProps(
            certificate_domain_name=certificate_domain_name,
            certificate_name=certificate_name,
            load_balancer_name=load_balancer_name,
            certificate_alternative_names=certificate_alternative_names,
            https_redirection_enabled=https_redirection_enabled,
            is_attached=is_attached,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a97d8d5e661589838048f732390ac6917df684142502cf96d4c4bedf29b23918)
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
            type_hints = typing.get_type_hints(_typecheckingstub__359468b4ef33a2b6efbdadb5f942165574bc4cd87e9e587af4b2bf50125c00e3)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrLoadBalancerTlsCertificateArn")
    def attr_load_balancer_tls_certificate_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the SSL/TLS certificate.

        :cloudformationAttribute: LoadBalancerTlsCertificateArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLoadBalancerTlsCertificateArn"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The validation status of the SSL/TLS certificate.

        Valid Values: ``PENDING_VALIDATION`` | ``ISSUED`` | ``INACTIVE`` | ``EXPIRED`` | ``VALIDATION_TIMED_OUT`` | ``REVOKED`` | ``FAILED`` | ``UNKNOWN``

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="certificateDomainName")
    def certificate_domain_name(self) -> builtins.str:
        '''The domain name for the SSL/TLS certificate.'''
        return typing.cast(builtins.str, jsii.get(self, "certificateDomainName"))

    @certificate_domain_name.setter
    def certificate_domain_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__482e67af63ec25c06cc769b8af2f431d3a603fb7710846f9e4eea18243b32523)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateDomainName", value)

    @builtins.property
    @jsii.member(jsii_name="certificateName")
    def certificate_name(self) -> builtins.str:
        '''The name of the SSL/TLS certificate.'''
        return typing.cast(builtins.str, jsii.get(self, "certificateName"))

    @certificate_name.setter
    def certificate_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea365fd72d444e37ddfbaf0234a061e0de0d732b186a069b7b1a5a39df3f1fa7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateName", value)

    @builtins.property
    @jsii.member(jsii_name="loadBalancerName")
    def load_balancer_name(self) -> builtins.str:
        '''The name of the load balancer that the SSL/TLS certificate is attached to.'''
        return typing.cast(builtins.str, jsii.get(self, "loadBalancerName"))

    @load_balancer_name.setter
    def load_balancer_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a5a1e61e1a29373de67690023777c77e5784ddd1eed009193ccd79c31375ac5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loadBalancerName", value)

    @builtins.property
    @jsii.member(jsii_name="certificateAlternativeNames")
    def certificate_alternative_names(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of alternative domain names and subdomain names for your SSL/TLS certificate.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "certificateAlternativeNames"))

    @certificate_alternative_names.setter
    def certificate_alternative_names(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59e23f97955e00f6360d16e0ab87bc69835eef51e52cf890a348794bbef17fa7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateAlternativeNames", value)

    @builtins.property
    @jsii.member(jsii_name="httpsRedirectionEnabled")
    def https_redirection_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''A Boolean value indicating whether HTTPS redirection is enabled for the load balancer that the TLS certificate is attached to.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "httpsRedirectionEnabled"))

    @https_redirection_enabled.setter
    def https_redirection_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49793fdda64b6efcd50edc14b8d59ea6317d02a33455daea3c5f0340008da31c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpsRedirectionEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="isAttached")
    def is_attached(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''A Boolean value indicating whether the SSL/TLS certificate is attached to a Lightsail load balancer.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "isAttached"))

    @is_attached.setter
    def is_attached(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__acab8637e92a20e3ce530799832a4d75e98bf630ea28f6276cce2b5ad63208b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isAttached", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_lightsail.CfnLoadBalancerTlsCertificateProps",
    jsii_struct_bases=[],
    name_mapping={
        "certificate_domain_name": "certificateDomainName",
        "certificate_name": "certificateName",
        "load_balancer_name": "loadBalancerName",
        "certificate_alternative_names": "certificateAlternativeNames",
        "https_redirection_enabled": "httpsRedirectionEnabled",
        "is_attached": "isAttached",
    },
)
class CfnLoadBalancerTlsCertificateProps:
    def __init__(
        self,
        *,
        certificate_domain_name: builtins.str,
        certificate_name: builtins.str,
        load_balancer_name: builtins.str,
        certificate_alternative_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        https_redirection_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        is_attached: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    ) -> None:
        '''Properties for defining a ``CfnLoadBalancerTlsCertificate``.

        :param certificate_domain_name: The domain name for the SSL/TLS certificate. For example, ``example.com`` or ``www.example.com`` .
        :param certificate_name: The name of the SSL/TLS certificate.
        :param load_balancer_name: The name of the load balancer that the SSL/TLS certificate is attached to.
        :param certificate_alternative_names: An array of alternative domain names and subdomain names for your SSL/TLS certificate. In addition to the primary domain name, you can have up to nine alternative domain names. Wildcards (such as ``*.example.com`` ) are not supported.
        :param https_redirection_enabled: A Boolean value indicating whether HTTPS redirection is enabled for the load balancer that the TLS certificate is attached to.
        :param is_attached: A Boolean value indicating whether the SSL/TLS certificate is attached to a Lightsail load balancer.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-loadbalancertlscertificate.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_lightsail as lightsail
            
            cfn_load_balancer_tls_certificate_props = lightsail.CfnLoadBalancerTlsCertificateProps(
                certificate_domain_name="certificateDomainName",
                certificate_name="certificateName",
                load_balancer_name="loadBalancerName",
            
                # the properties below are optional
                certificate_alternative_names=["certificateAlternativeNames"],
                https_redirection_enabled=False,
                is_attached=False
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6bbb3dc854056a7a9bdff668a8aa163cf8480e4748e2322ea115d3e425bbe0f)
            check_type(argname="argument certificate_domain_name", value=certificate_domain_name, expected_type=type_hints["certificate_domain_name"])
            check_type(argname="argument certificate_name", value=certificate_name, expected_type=type_hints["certificate_name"])
            check_type(argname="argument load_balancer_name", value=load_balancer_name, expected_type=type_hints["load_balancer_name"])
            check_type(argname="argument certificate_alternative_names", value=certificate_alternative_names, expected_type=type_hints["certificate_alternative_names"])
            check_type(argname="argument https_redirection_enabled", value=https_redirection_enabled, expected_type=type_hints["https_redirection_enabled"])
            check_type(argname="argument is_attached", value=is_attached, expected_type=type_hints["is_attached"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "certificate_domain_name": certificate_domain_name,
            "certificate_name": certificate_name,
            "load_balancer_name": load_balancer_name,
        }
        if certificate_alternative_names is not None:
            self._values["certificate_alternative_names"] = certificate_alternative_names
        if https_redirection_enabled is not None:
            self._values["https_redirection_enabled"] = https_redirection_enabled
        if is_attached is not None:
            self._values["is_attached"] = is_attached

    @builtins.property
    def certificate_domain_name(self) -> builtins.str:
        '''The domain name for the SSL/TLS certificate.

        For example, ``example.com`` or ``www.example.com`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-loadbalancertlscertificate.html#cfn-lightsail-loadbalancertlscertificate-certificatedomainname
        '''
        result = self._values.get("certificate_domain_name")
        assert result is not None, "Required property 'certificate_domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def certificate_name(self) -> builtins.str:
        '''The name of the SSL/TLS certificate.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-loadbalancertlscertificate.html#cfn-lightsail-loadbalancertlscertificate-certificatename
        '''
        result = self._values.get("certificate_name")
        assert result is not None, "Required property 'certificate_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def load_balancer_name(self) -> builtins.str:
        '''The name of the load balancer that the SSL/TLS certificate is attached to.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-loadbalancertlscertificate.html#cfn-lightsail-loadbalancertlscertificate-loadbalancername
        '''
        result = self._values.get("load_balancer_name")
        assert result is not None, "Required property 'load_balancer_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def certificate_alternative_names(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of alternative domain names and subdomain names for your SSL/TLS certificate.

        In addition to the primary domain name, you can have up to nine alternative domain names. Wildcards (such as ``*.example.com`` ) are not supported.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-loadbalancertlscertificate.html#cfn-lightsail-loadbalancertlscertificate-certificatealternativenames
        '''
        result = self._values.get("certificate_alternative_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def https_redirection_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''A Boolean value indicating whether HTTPS redirection is enabled for the load balancer that the TLS certificate is attached to.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-loadbalancertlscertificate.html#cfn-lightsail-loadbalancertlscertificate-httpsredirectionenabled
        '''
        result = self._values.get("https_redirection_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def is_attached(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''A Boolean value indicating whether the SSL/TLS certificate is attached to a Lightsail load balancer.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-loadbalancertlscertificate.html#cfn-lightsail-loadbalancertlscertificate-isattached
        '''
        result = self._values.get("is_attached")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLoadBalancerTlsCertificateProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnStaticIp(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_lightsail.CfnStaticIp",
):
    '''The ``AWS::Lightsail::StaticIp`` resource specifies a static IP that can be attached to an Amazon Lightsail instance that is in the same AWS Region and Availability Zone.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-staticip.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_lightsail as lightsail
        
        cfn_static_ip = lightsail.CfnStaticIp(self, "MyCfnStaticIp",
            static_ip_name="staticIpName",
        
            # the properties below are optional
            attached_to="attachedTo"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        static_ip_name: builtins.str,
        attached_to: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param static_ip_name: The name of the static IP.
        :param attached_to: The instance that the static IP is attached to.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f5a6b62049424b56120c89b71c0a6a728662c6441d26ce029e6afa1e2b26e7c9)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnStaticIpProps(
            static_ip_name=static_ip_name, attached_to=attached_to
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7e5c95f646daff7dce693141b7ff4bbef8bf3da49746df55bd2d94acaca762c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__fc71884f0ce4406b29cffbc0c47fa1f33b7e74d6e1e637327f1630e06ca9a755)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrIpAddress")
    def attr_ip_address(self) -> builtins.str:
        '''The IP address of the static IP.

        :cloudformationAttribute: IpAddress
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIpAddress"))

    @builtins.property
    @jsii.member(jsii_name="attrIsAttached")
    def attr_is_attached(self) -> _IResolvable_da3f097b:
        '''A Boolean value indicating whether the static IP is attached to an instance.

        :cloudformationAttribute: IsAttached
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrIsAttached"))

    @builtins.property
    @jsii.member(jsii_name="attrStaticIpArn")
    def attr_static_ip_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the static IP (for example, ``arn:aws:lightsail:us-east-2:123456789101:StaticIp/244ad76f-8aad-4741-809f-12345EXAMPLE`` ).

        :cloudformationAttribute: StaticIpArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStaticIpArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="staticIpName")
    def static_ip_name(self) -> builtins.str:
        '''The name of the static IP.'''
        return typing.cast(builtins.str, jsii.get(self, "staticIpName"))

    @static_ip_name.setter
    def static_ip_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52e39df405854b7de9a88345f26f35243baca3a3754da4cac25bd6ca1e79dc14)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "staticIpName", value)

    @builtins.property
    @jsii.member(jsii_name="attachedTo")
    def attached_to(self) -> typing.Optional[builtins.str]:
        '''The instance that the static IP is attached to.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "attachedTo"))

    @attached_to.setter
    def attached_to(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c2d9d917457bb338d59787b3dda39043267dcfa899e281196bff60209e197d68)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "attachedTo", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_lightsail.CfnStaticIpProps",
    jsii_struct_bases=[],
    name_mapping={"static_ip_name": "staticIpName", "attached_to": "attachedTo"},
)
class CfnStaticIpProps:
    def __init__(
        self,
        *,
        static_ip_name: builtins.str,
        attached_to: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnStaticIp``.

        :param static_ip_name: The name of the static IP.
        :param attached_to: The instance that the static IP is attached to.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-staticip.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_lightsail as lightsail
            
            cfn_static_ip_props = lightsail.CfnStaticIpProps(
                static_ip_name="staticIpName",
            
                # the properties below are optional
                attached_to="attachedTo"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5bc95e214923f08eafcf70fdee5ec4aa29288061794f727d4705d465e9c89da)
            check_type(argname="argument static_ip_name", value=static_ip_name, expected_type=type_hints["static_ip_name"])
            check_type(argname="argument attached_to", value=attached_to, expected_type=type_hints["attached_to"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "static_ip_name": static_ip_name,
        }
        if attached_to is not None:
            self._values["attached_to"] = attached_to

    @builtins.property
    def static_ip_name(self) -> builtins.str:
        '''The name of the static IP.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-staticip.html#cfn-lightsail-staticip-staticipname
        '''
        result = self._values.get("static_ip_name")
        assert result is not None, "Required property 'static_ip_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def attached_to(self) -> typing.Optional[builtins.str]:
        '''The instance that the static IP is attached to.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-staticip.html#cfn-lightsail-staticip-attachedto
        '''
        result = self._values.get("attached_to")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnStaticIpProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnAlarm",
    "CfnAlarmProps",
    "CfnBucket",
    "CfnBucketProps",
    "CfnCertificate",
    "CfnCertificateProps",
    "CfnContainer",
    "CfnContainerProps",
    "CfnDatabase",
    "CfnDatabaseProps",
    "CfnDisk",
    "CfnDiskProps",
    "CfnDistribution",
    "CfnDistributionProps",
    "CfnInstance",
    "CfnInstanceProps",
    "CfnLoadBalancer",
    "CfnLoadBalancerProps",
    "CfnLoadBalancerTlsCertificate",
    "CfnLoadBalancerTlsCertificateProps",
    "CfnStaticIp",
    "CfnStaticIpProps",
]

publication.publish()

def _typecheckingstub__52a6d2c9652c1f935ede5b57250bb327a005cfd64bafaed966f96abbe167f1cb(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    alarm_name: builtins.str,
    comparison_operator: builtins.str,
    evaluation_periods: jsii.Number,
    metric_name: builtins.str,
    monitored_resource_name: builtins.str,
    threshold: jsii.Number,
    contact_protocols: typing.Optional[typing.Sequence[builtins.str]] = None,
    datapoints_to_alarm: typing.Optional[jsii.Number] = None,
    notification_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    notification_triggers: typing.Optional[typing.Sequence[builtins.str]] = None,
    treat_missing_data: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92cba21d204152e76e818434e3b1baf4a449ecb411f8200900c1e7cff19b2968(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02ad248f7a5a406b284b19a230eb250e778357cb79afe022f86b954427facd41(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6cbef5a5341e55fa03b4be9a6a15a8717434d6fc08dc2002a6a455935ed61cca(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5f7bab333eda8f33f7cf02bfacceaed6eba1bce4cffab8c704a426a990a39bb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dbca6c409a133a482c79d4f2d1d54d380635a6cd16f5659cddbbdca0113f00e2(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d56d786f28acdb2b750523f0f764b81b2dbe6c19989d8ad5d6637d38ef41dafd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bed67dce202ef59c6fc0482720e647da6d182a5eb7fc29bd7e33f7c493baeeba(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2207c45df0a7242a484a71d452e6078412a0174e16363bf59797c35aba03cf60(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e16e66db23d954d5c8b8f71b6a742f8d70605fd3ec588876e4cc4b066986fc5e(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0cf63524930194266731756c5d9e34ac56a21a835ccf654121b2eef068b86851(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d1f7e50126b8dc4c73aad55d44ca47c64d1aaa42863a2071146240e12b7fff9(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a80d0edb78ff630c74b704ff1bb587d3767dde14ca85dfcc06b5a9fce0e6b51a(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__288a8a660b0017ff51421053d89dc9a8f78e3031f9d00e3da7512b2927946c92(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8d2af6c4e2ba837e14d1d99b9e23f273f3d750b635d2750e4f758a49c1b5349(
    *,
    alarm_name: builtins.str,
    comparison_operator: builtins.str,
    evaluation_periods: jsii.Number,
    metric_name: builtins.str,
    monitored_resource_name: builtins.str,
    threshold: jsii.Number,
    contact_protocols: typing.Optional[typing.Sequence[builtins.str]] = None,
    datapoints_to_alarm: typing.Optional[jsii.Number] = None,
    notification_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    notification_triggers: typing.Optional[typing.Sequence[builtins.str]] = None,
    treat_missing_data: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f94a4bda809634204637b79ee8727ab741bdbc1389aa69314a9dd6ac07ff80d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    bucket_name: builtins.str,
    bundle_id: builtins.str,
    access_rules: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBucket.AccessRulesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    object_versioning: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    read_only_access_accounts: typing.Optional[typing.Sequence[builtins.str]] = None,
    resources_receiving_access: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a55634856786112230a563acc6361f686fcc4372251819f23a60e0b7448a375(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d60747afd5cc92706d65ce7e109be47066c778315246768e80639025bb28b8a4(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__671ba368991f7894cc8ddfe61a9b72e7f6d4f964b0c1b7e3da859b6c5db6cd24(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6d5cea1c49d3cd6bf89b2a808219992c0ebd27dac7ba487070e177c4603b093(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__911a5ab074c6c9182d436d48523575a61c00e4566f9a555177936f1964f07641(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnBucket.AccessRulesProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6191661c271e19e8e8cac9d23703e7a3bcbba2dc5b15936dc4e3f080e7e234af(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab9b5622907c27faf77ab0bb3b248846c9d3b055a5fe545e85f5d0221ad5d356(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c511e7332e65a7a04ff0fba1f48703451ea06cf1cd61fd70b6c99a1c016339b(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52cc8a8b4e5b6b3a8d087b3ae8257283509372b0fe52e0e90dc9c520fd5f8e34(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__120388e897900c963efef1f8bbf42a875d5673e23401f7d348c6c432975d91b5(
    *,
    allow_public_overrides: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    object_access: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfc80b7f52bbdf250acb4672ad00571df26e5f1142621c5a91482ece0a300415(
    *,
    bucket_name: builtins.str,
    bundle_id: builtins.str,
    access_rules: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBucket.AccessRulesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    object_versioning: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    read_only_access_accounts: typing.Optional[typing.Sequence[builtins.str]] = None,
    resources_receiving_access: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e46c9c2a31601388f0189b39ac759febe04b899bf6d84e063082749df57f5ef(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    certificate_name: builtins.str,
    domain_name: builtins.str,
    subject_alternative_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd78f535b6f19bc334f8884c826df32506a72bb7be7a48483b6d136b462c2467(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81b4a0c654d5ac565c158a4cccb760fdd62d938202b41b6cf3140a72c8fb5a1a(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b13a2a543d6b2720b4cf168052ef4b17165797152752e38fff22e9a4fbd5c425(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__561359c124f9c2bc11955748c848288878d75889197cec6c9f222b79a3ad2cdb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bde188d393958878c8d4e57a5877d812238d5cefe2fc847b8666282a8e53290a(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa0e2472d9d23da3ec2ce0c96320254278721ae808d47271138b62d6684a75b8(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2fece9fd02d544f5e7457740dc0b59430a4b93239cb2e0ea2ff7d402d126510b(
    *,
    certificate_name: builtins.str,
    domain_name: builtins.str,
    subject_alternative_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94bac8a5de27a74603b05e36d9c72422cb8c35ec6940b2bcc87094fd27fbc7ac(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    power: builtins.str,
    scale: jsii.Number,
    service_name: builtins.str,
    container_service_deployment: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainer.ContainerServiceDeploymentProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    is_disabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    public_domain_names: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainer.PublicDomainNameProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd0b8f262d0bb3db8f5559a78d02ed77d6d817f801cff964ae11b76f927a030d(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ccc317951b85768b34fae7b08d2c64434b38c35cbb35636a5c8f4525537d2e8(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c43b42c387b2dcfa1723f7d229e7a7d6123b4a5dd3c00b08379a0d8c5b9ca0a3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9aa65eb02fb8c30379eca4549f1c20fe31b13502f31a42fb2d5bc4a0c834e54e(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc3a585466a749c4c1a1d7e4f0ff912b27ba8bff6127862e194982ee4e1a955d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e8ef0ed2b23c56026e0da66efb4213ed90af7b6dfea05d5bbce033060cc7e43(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnContainer.ContainerServiceDeploymentProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a52d8c870a181dac72ac9809ac930672df1d327079dcac65e47b7e2aadcd54ed(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa200bad90bddaf505b39b733612869b17dd2e87cd1aaa81d1cfedde46e1bb8e(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnContainer.PublicDomainNameProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7eef525fca5f562f87e3ac9c6423f561f56721f252309711cf942b6679b0ed6e(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2643ecd28650d4a160cec5faf8d37c64b7d9033d437056ac73a83cfb6d60a74c(
    *,
    command: typing.Optional[typing.Sequence[builtins.str]] = None,
    container_name: typing.Optional[builtins.str] = None,
    environment: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainer.EnvironmentVariableProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    image: typing.Optional[builtins.str] = None,
    ports: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainer.PortInfoProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__361b481c01847aedbb1dab6f7a2b940c6da922f6af27593f14d67b2288673a11(
    *,
    containers: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainer.ContainerProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    public_endpoint: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainer.PublicEndpointProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0a31811b7a56ea2f4b026dbd07da448a9b8998283ff6d18707ad7fb4b594494(
    *,
    value: typing.Optional[builtins.str] = None,
    variable: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__117cfc04d169db66d5bf8186765ffa02af0a0c5769b9891fd1a2ff4478ccba20(
    *,
    healthy_threshold: typing.Optional[jsii.Number] = None,
    interval_seconds: typing.Optional[jsii.Number] = None,
    path: typing.Optional[builtins.str] = None,
    success_codes: typing.Optional[builtins.str] = None,
    timeout_seconds: typing.Optional[jsii.Number] = None,
    unhealthy_threshold: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2957cb3f17880ab79f0061a8100d03ac1b612e1511f4a371be09517cb05571fa(
    *,
    port: typing.Optional[builtins.str] = None,
    protocol: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d9c472b649d2e9119b005aacad2dbe93a008b5ae90f7dafffb84c714e14e831(
    *,
    certificate_name: typing.Optional[builtins.str] = None,
    domain_names: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd597e5de3f9b4ca413b0f95b46ae241cde5964a9efbb640c28cf6593d3de7b0(
    *,
    container_name: typing.Optional[builtins.str] = None,
    container_port: typing.Optional[jsii.Number] = None,
    health_check_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainer.HealthCheckConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97ba65c009b99fbaa7ef08e0bf85a260e5a557dc34e2894b5cbb3a6a6a4aa907(
    *,
    power: builtins.str,
    scale: jsii.Number,
    service_name: builtins.str,
    container_service_deployment: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainer.ContainerServiceDeploymentProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    is_disabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    public_domain_names: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainer.PublicDomainNameProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__723ca4244db57b3b52ce3ed934765e22e79b12ddfe526a8f6db7bdabff702a66(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    master_database_name: builtins.str,
    master_username: builtins.str,
    relational_database_blueprint_id: builtins.str,
    relational_database_bundle_id: builtins.str,
    relational_database_name: builtins.str,
    availability_zone: typing.Optional[builtins.str] = None,
    backup_retention: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    ca_certificate_identifier: typing.Optional[builtins.str] = None,
    master_user_password: typing.Optional[builtins.str] = None,
    preferred_backup_window: typing.Optional[builtins.str] = None,
    preferred_maintenance_window: typing.Optional[builtins.str] = None,
    publicly_accessible: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    relational_database_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDatabase.RelationalDatabaseParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    rotate_master_user_password: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26cc577f7a052133e01e9648ef301f73e94aaaff3448f91e3db303c34c8e1570(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dedbb2a45b5731e155b72566dddda34421e74a5876a6856f0b9044eb7e422b3d(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44bfee7201708398172d9c276409ca3a0edb6fd96fbb53de3c6d21f9ba38f2aa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7fe99b95647bc539d082d0cd9d6da52a4a6fd8065020323f840fae0e93e829e2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d98f0098b8a20a19e0698b2035c421c40d0dd6b470192acb90e2f3aafb4f8c59(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0085abf7a85860fb9463b046ff1a50df70621aad07715b1d2264f86ad3b37980(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fda74fa4d573fc976044231318a27a2615dff79bb54e1bf501d7f641ec177f44(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e15da72f1f0e0effee27cdac8697b6046c3b8670a5f08070180d1913992dcba5(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f06245bb04a19656eaedd55d945ba9fc771b141ebea294c5f2e46a5a301a9620(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8facd20917d86a0338c43b7be0baf738e391c887dd3f80ca4489f3f39581c750(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8357b41834ed93919de4eea33fb2da779ef94976a107ee989c52c7721b5111b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd811ff9c2abe8c9dd2993c66e45e928d4f5d37ba14e6d72d593b8d46e369505(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9094db1231b55bdfa84cdc589d3e0d5410170d587cd69d51a1edfe01ff07f862(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8197f292fce266aba628a142dec258c98e7a25fed22896e06e1a90c24a7ba544(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c96ad668b58f33187ed56194efffce27de109fd0767bcd5c1f2484c5bee18d56(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDatabase.RelationalDatabaseParameterProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__091d540f8b782064900c5e22fafb94086a4be8e774d1ca1e28d1034f980c1e78(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__742edfcb29bb69911299a631b46a0f26a5025e76d10c496b6e66e28bb86874ec(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2decf56e5d7a797902c80fb0a4f07e403ddbf32e21ae82ca0276101029f789f8(
    *,
    allowed_values: typing.Optional[builtins.str] = None,
    apply_method: typing.Optional[builtins.str] = None,
    apply_type: typing.Optional[builtins.str] = None,
    data_type: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    is_modifiable: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    parameter_name: typing.Optional[builtins.str] = None,
    parameter_value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54feeda1af4cae8d2e40338b603c7ff96c3a0d88fba114bb9b9549eac1795ac3(
    *,
    master_database_name: builtins.str,
    master_username: builtins.str,
    relational_database_blueprint_id: builtins.str,
    relational_database_bundle_id: builtins.str,
    relational_database_name: builtins.str,
    availability_zone: typing.Optional[builtins.str] = None,
    backup_retention: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    ca_certificate_identifier: typing.Optional[builtins.str] = None,
    master_user_password: typing.Optional[builtins.str] = None,
    preferred_backup_window: typing.Optional[builtins.str] = None,
    preferred_maintenance_window: typing.Optional[builtins.str] = None,
    publicly_accessible: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    relational_database_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDatabase.RelationalDatabaseParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    rotate_master_user_password: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80a3acf97fc9eaa657a04acbab637a1d0adb76d1178dbca352280131a1e64601(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    disk_name: builtins.str,
    size_in_gb: jsii.Number,
    add_ons: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDisk.AddOnProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    availability_zone: typing.Optional[builtins.str] = None,
    location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDisk.LocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea4f169865a73e68a220949579e4971d18e071074b75df08ffa1bf72dedb580c(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3fe5653cbcc9bffb3186bb057c3356cf16999f60677b11a964bc4dbaa77b44b4(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca648103138b58ef4b28158de4e9077eea50974ea860de6e2cafaf7c1ea68497(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc1d51effcf0ec678cadc317f7c644119757d22b11d365f942f6e5869972b495(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6bb18dc1c40065ba9615024ffd4c8a5bba5665cf77f22e9fe23067d7b1e0269b(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDisk.AddOnProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a929e131601b77b843b584668029130493ce602b0f8f3773bde8e91acbdc46f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ad247d59530c9822b391b02d714793c6faf5b661335e33a60f755e84cac854e(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDisk.LocationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8d9f7c7c9bb1fcb533d5c13ea1040c3fcc188448ff6c785a662ccf8e4342f96(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6dca6ef6ad37884857f6dd11bf04fa1d4d068cc3716b82e18bc18b6f614d3f3(
    *,
    add_on_type: builtins.str,
    auto_snapshot_add_on_request: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDisk.AutoSnapshotAddOnProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    status: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8fac9a027dbef91fb6dcd3972cd2f428689708e722e631dd37ac710dc2907d7(
    *,
    snapshot_time_of_day: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7cd90525af9bd1ae5058a25d04444364be64fc46bff0d7ac63c54d5a6441c33(
    *,
    availability_zone: typing.Optional[builtins.str] = None,
    region_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d095d2590ef382758292269648b2abe4a720c01c7094f3ff4555ad70077f501d(
    *,
    disk_name: builtins.str,
    size_in_gb: jsii.Number,
    add_ons: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDisk.AddOnProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    availability_zone: typing.Optional[builtins.str] = None,
    location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDisk.LocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9482ccb96453330c51f380a8c1e2e74f0c57b789e803cc41a6d1f7dcb6be11b9(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    bundle_id: builtins.str,
    default_cache_behavior: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDistribution.CacheBehaviorProperty, typing.Dict[builtins.str, typing.Any]]],
    distribution_name: builtins.str,
    origin: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDistribution.InputOriginProperty, typing.Dict[builtins.str, typing.Any]]],
    cache_behaviors: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDistribution.CacheBehaviorPerPathProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    cache_behavior_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDistribution.CacheSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    certificate_name: typing.Optional[builtins.str] = None,
    ip_address_type: typing.Optional[builtins.str] = None,
    is_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8da47e5ef6c7db02eb83fd111cd49ed93a08332c93a0f1d588cdc74356706636(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb5945d202d9d8440df9db2cbb8008adb965c2628d41aee45553082f8a9fc477(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__713bb0b587b041ad1fbbf3481064d8f0e36314c4a715858754917a04e6b59834(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60f134014dad7eff652ae9a0a8f31d075d567a38120fb79b22fc79b66ef4afbf(
    value: typing.Union[_IResolvable_da3f097b, CfnDistribution.CacheBehaviorProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f10d8b0a845facf9cb45b4afe93f3ae69d0dab27fa56b50b7cc0e69ee5ab2f3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7aef6fbf79a3b5e2f5250752a43b5ce48241a88650e2ca85121c71c9eff2e8db(
    value: typing.Union[_IResolvable_da3f097b, CfnDistribution.InputOriginProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa33d1002424823136283db85abedb68f706cfe801b8cdda97985832959b3635(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDistribution.CacheBehaviorPerPathProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__760802ef8ce7a6adca268629830855308c05a61f03a8580e810b0493e8340ff0(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDistribution.CacheSettingsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a588edb72e589002f8ed3b782d48335de6cd3b97ead472d268cbbc811d7a9aa(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__852740f08ca9ce997952eb51ce9417e48061256a758eed9e4defe320b5cb751d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45ad4bf8bbe0e7c8404bc88c174e7fc60ea632f80e1214c05127c076aa76106d(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__908b31b9ccd34cec50f1719ac43f4d386695ad72d71eff4b6177f5f0cbae1d41(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2d974d0c55f60f6f3f06797debd277521527e8d953d07b13eb3246980e4f75d(
    *,
    behavior: typing.Optional[builtins.str] = None,
    path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5c3a4aa024dd1b6cd4538cc52ce109aa9ade3ffeff44b9a1d33fbc5100a3c2a(
    *,
    behavior: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71273d747070fd305155aa796ba791770952e4398259d9319417dfa9ca649969(
    *,
    allowed_http_methods: typing.Optional[builtins.str] = None,
    cached_http_methods: typing.Optional[builtins.str] = None,
    default_ttl: typing.Optional[jsii.Number] = None,
    forwarded_cookies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDistribution.CookieObjectProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    forwarded_headers: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDistribution.HeaderObjectProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    forwarded_query_strings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDistribution.QueryStringObjectProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    maximum_ttl: typing.Optional[jsii.Number] = None,
    minimum_ttl: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d58452d36b0308e6ce28a9b550fe3fce77b87aaad440feefc51f83755937f137(
    *,
    cookies_allow_list: typing.Optional[typing.Sequence[builtins.str]] = None,
    option: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8800c7d1a30fcdf0e75dfd3650ad86e4223cdabbe6df507c54628133a0c1fc2(
    *,
    headers_allow_list: typing.Optional[typing.Sequence[builtins.str]] = None,
    option: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__accc7b7eb30a60be239eb0280dade3739e4094e04bda535d5fe3d04d2d008607(
    *,
    name: typing.Optional[builtins.str] = None,
    protocol_policy: typing.Optional[builtins.str] = None,
    region_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3d10f0e1349e20e39be61df90b8a453ebfd22f3496fc3e4391831ccb7b40abd(
    *,
    option: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    query_strings_allow_list: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5746be261e67458f872b406208009ddcf740c3277f27869ccbc24697bfb6d14c(
    *,
    bundle_id: builtins.str,
    default_cache_behavior: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDistribution.CacheBehaviorProperty, typing.Dict[builtins.str, typing.Any]]],
    distribution_name: builtins.str,
    origin: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDistribution.InputOriginProperty, typing.Dict[builtins.str, typing.Any]]],
    cache_behaviors: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDistribution.CacheBehaviorPerPathProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    cache_behavior_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDistribution.CacheSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    certificate_name: typing.Optional[builtins.str] = None,
    ip_address_type: typing.Optional[builtins.str] = None,
    is_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f56ba2d2d7e68ec61cd3684949f9d2894843d2a820ea3c2a5dce40b3698dd9fe(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    blueprint_id: builtins.str,
    bundle_id: builtins.str,
    instance_name: builtins.str,
    add_ons: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstance.AddOnProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    availability_zone: typing.Optional[builtins.str] = None,
    hardware: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstance.HardwareProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    key_pair_name: typing.Optional[builtins.str] = None,
    location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstance.LocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    networking: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstance.NetworkingProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    state: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstance.StateProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    user_data: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be47197b4bba429c8a1b13b7bb35c7764b6aff13ccb15e40cefc35fd2df04e45(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cee95794d0d504ed730245ac786397afe3973e5fffef49a4225b4ab4910ea884(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c902440458adfe1266e3dc96225288d15ecf1c1d8bba26d793d37881c351c773(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f5e85e9ad23cc8571347b8c2e46e5f249ca7334ed4d54786f85f9f55b4b4261(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ff4c2b7a1d245d5744d6342d2f0a8f108daf28fd2169d869ecec762579a76da(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a099dffb98d8133f25aa3f4894f04b7838ec68531bc89457bc7ca10ffe65fe77(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnInstance.AddOnProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9a56dd4f393fedcb7fc5c77d31a9635f61996dce654f144f2bb3f59379891d4(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__918e77b58ce707e3fd0fe417aa8b0279b976fecbc63c99bf33fb6c34fb56e06f(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnInstance.HardwareProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e99199ed725a507d6941324fca99a5c014fd317cd07b24dacef00536be31eb87(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1796032b802331052ff1dc453b46bc6f3d89e44ed47ae0a3b75c51d5f4ec330f(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnInstance.LocationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ae0605c3ecf986c476ae405f626b73a0ead2ba85a44089e88662ab1e59b4436(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnInstance.NetworkingProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8016843d96a81bf84ad05c8259de853033dbbd7a359485955cea3d46de80c536(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnInstance.StateProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af09458d52eaea13266eac32d46975c0c7fb0afae18d4af7c41cdbda91b257f5(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b37ad7b78e9dfd25f54548408e5d1989fcb19258bb2e95aff2742713f8eca62(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02dc099cd32004362b392684e938362aec7ce6a9b6b301a80e7139a71b96c02c(
    *,
    add_on_type: builtins.str,
    auto_snapshot_add_on_request: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstance.AutoSnapshotAddOnProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    status: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3379f4d4976801e9abba5d85ecd4fc5cb5104c9adb4340cfc90ee57b933f326b(
    *,
    snapshot_time_of_day: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0463034a2cc858b33422d6128a4dfb2d16fb633c63e6c0729f35dc20125c37c4(
    *,
    disk_name: builtins.str,
    path: builtins.str,
    attached_to: typing.Optional[builtins.str] = None,
    attachment_state: typing.Optional[builtins.str] = None,
    iops: typing.Optional[jsii.Number] = None,
    is_system_disk: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    size_in_gb: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf4e04cb05bf874499d602adfa37eca6eb395e84f62083580547a6d07384e740(
    *,
    cpu_count: typing.Optional[jsii.Number] = None,
    disks: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstance.DiskProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ram_size_in_gb: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42891a6c84f248f5fa55c61278147e8c2099067282ab557ea17c9ca87b6139fb(
    *,
    availability_zone: typing.Optional[builtins.str] = None,
    region_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__011a40f828871b8a7d528d71ece98fab8b8e3b2ee997c8468da4950f05813b90(
    *,
    gb_per_month_allocated: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9aa7120f291685e085f9178bd3e3c7de7699e996ed43a42cba437f80bc78e7a(
    *,
    ports: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstance.PortProperty, typing.Dict[builtins.str, typing.Any]]]]],
    monthly_transfer: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a910b73471578cf7936f197ae2e435d87605ce8b975d2f1a342c41809a845fa(
    *,
    access_direction: typing.Optional[builtins.str] = None,
    access_from: typing.Optional[builtins.str] = None,
    access_type: typing.Optional[builtins.str] = None,
    cidr_list_aliases: typing.Optional[typing.Sequence[builtins.str]] = None,
    cidrs: typing.Optional[typing.Sequence[builtins.str]] = None,
    common_name: typing.Optional[builtins.str] = None,
    from_port: typing.Optional[jsii.Number] = None,
    ipv6_cidrs: typing.Optional[typing.Sequence[builtins.str]] = None,
    protocol: typing.Optional[builtins.str] = None,
    to_port: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e9f9e996c0dfa91ed16946148a8dc76af0067f4e87e53af0be16aa75d5f4e42(
    *,
    code: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e0def276816b17135efe655ecd6a1a965ddb59099e6f411660bf2c2e3faeeaa(
    *,
    blueprint_id: builtins.str,
    bundle_id: builtins.str,
    instance_name: builtins.str,
    add_ons: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstance.AddOnProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    availability_zone: typing.Optional[builtins.str] = None,
    hardware: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstance.HardwareProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    key_pair_name: typing.Optional[builtins.str] = None,
    location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstance.LocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    networking: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstance.NetworkingProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    state: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstance.StateProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    user_data: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7424f399a4c81195a3832bf4c1d53a1869a11a94a74f58e7efaf927f44364614(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    instance_port: jsii.Number,
    load_balancer_name: builtins.str,
    attached_instances: typing.Optional[typing.Sequence[builtins.str]] = None,
    health_check_path: typing.Optional[builtins.str] = None,
    ip_address_type: typing.Optional[builtins.str] = None,
    session_stickiness_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    session_stickiness_lb_cookie_duration_seconds: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    tls_policy_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31f7abe244f876394bc038308ea33c66bfe259f6bac63c7a7311664365295aae(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e52afad487ef5f48ccd656aebec9f80189f8e70917a767f20754594458adb55c(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__400516c5f0e10f776899b7edb1e990db4f4a24e3325177548046802d33c26a5f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e88376ead8f2114df0c93a8a49a09abc0c2aba0302879ce3720d58cee7c2719(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4648ebf266af790248fa827ea484bb236262c06a7cba26c3fb76498f32796266(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3bb17a4c6a795e8df00992dc4953caa4b3826d13bbd31239cf7e659a8d3a569(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6d2a98739f1d1aac5be4e44af011db153c8aa9cda2208cd4d793ab91d7b024d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60d3bde218d3bcb6c355f873dd0255f6432fda15433610cbd8c4755bbdabed21(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09c637e41f600eb13a6c074f22338a4435394664f425f957444e9b8dfcf2aa9c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afc022f5045d5ea7f789cb66d1e19f0beb665d810659027059f4ceb4cf6599b6(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af314ec18592fe248ceaa789a42b5f2269e8f7ffe3ee545ee0ccc9f2be2dc9b8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f2f4d23f6e12e19581cf7aac426cbcebf3bbb277d69cf495d240afd4e81bb5e(
    *,
    instance_port: jsii.Number,
    load_balancer_name: builtins.str,
    attached_instances: typing.Optional[typing.Sequence[builtins.str]] = None,
    health_check_path: typing.Optional[builtins.str] = None,
    ip_address_type: typing.Optional[builtins.str] = None,
    session_stickiness_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    session_stickiness_lb_cookie_duration_seconds: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    tls_policy_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0690a757a43538375584bafa46effdc256cd7146a3c192b0c4ff30490e4544e3(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    certificate_domain_name: builtins.str,
    certificate_name: builtins.str,
    load_balancer_name: builtins.str,
    certificate_alternative_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    https_redirection_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    is_attached: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a97d8d5e661589838048f732390ac6917df684142502cf96d4c4bedf29b23918(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__359468b4ef33a2b6efbdadb5f942165574bc4cd87e9e587af4b2bf50125c00e3(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__482e67af63ec25c06cc769b8af2f431d3a603fb7710846f9e4eea18243b32523(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea365fd72d444e37ddfbaf0234a061e0de0d732b186a069b7b1a5a39df3f1fa7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a5a1e61e1a29373de67690023777c77e5784ddd1eed009193ccd79c31375ac5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59e23f97955e00f6360d16e0ab87bc69835eef51e52cf890a348794bbef17fa7(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49793fdda64b6efcd50edc14b8d59ea6317d02a33455daea3c5f0340008da31c(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__acab8637e92a20e3ce530799832a4d75e98bf630ea28f6276cce2b5ad63208b8(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6bbb3dc854056a7a9bdff668a8aa163cf8480e4748e2322ea115d3e425bbe0f(
    *,
    certificate_domain_name: builtins.str,
    certificate_name: builtins.str,
    load_balancer_name: builtins.str,
    certificate_alternative_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    https_redirection_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    is_attached: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5a6b62049424b56120c89b71c0a6a728662c6441d26ce029e6afa1e2b26e7c9(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    static_ip_name: builtins.str,
    attached_to: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7e5c95f646daff7dce693141b7ff4bbef8bf3da49746df55bd2d94acaca762c(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc71884f0ce4406b29cffbc0c47fa1f33b7e74d6e1e637327f1630e06ca9a755(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52e39df405854b7de9a88345f26f35243baca3a3754da4cac25bd6ca1e79dc14(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2d9d917457bb338d59787b3dda39043267dcfa899e281196bff60209e197d68(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5bc95e214923f08eafcf70fdee5ec4aa29288061794f727d4705d465e9c89da(
    *,
    static_ip_name: builtins.str,
    attached_to: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
