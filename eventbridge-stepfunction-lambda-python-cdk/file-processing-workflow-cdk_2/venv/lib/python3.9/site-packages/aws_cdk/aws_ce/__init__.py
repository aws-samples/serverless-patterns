'''
# AWS::CE Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_ce as ce
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for CE construct libraries](https://constructs.dev/search?q=ce)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::CE resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_CE.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::CE](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_CE.html).

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
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556)
class CfnAnomalyMonitor(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ce.CfnAnomalyMonitor",
):
    '''The ``AWS::CE::AnomalyMonitor`` resource is a Cost Explorer resource type that continuously inspects your account's cost data for anomalies, based on ``MonitorType`` and ``MonitorSpecification`` .

    The content consists of detailed metadata and the current status of the monitor object.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalymonitor.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ce as ce
        
        cfn_anomaly_monitor = ce.CfnAnomalyMonitor(self, "MyCfnAnomalyMonitor",
            monitor_name="monitorName",
            monitor_type="monitorType",
        
            # the properties below are optional
            monitor_dimension="monitorDimension",
            monitor_specification="monitorSpecification",
            resource_tags=[ce.CfnAnomalyMonitor.ResourceTagProperty(
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
        monitor_name: builtins.str,
        monitor_type: builtins.str,
        monitor_dimension: typing.Optional[builtins.str] = None,
        monitor_specification: typing.Optional[builtins.str] = None,
        resource_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAnomalyMonitor.ResourceTagProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param monitor_name: The name of the monitor.
        :param monitor_type: The possible type values.
        :param monitor_dimension: The dimensions to evaluate.
        :param monitor_specification: The array of ``MonitorSpecification`` in JSON array format. For instance, you can use ``MonitorSpecification`` to specify a tag, Cost Category, or linked account for your custom anomaly monitor. For further information, see the `Examples <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalymonitor.html#aws-resource-ce-anomalymonitor--examples>`_ section of this page.
        :param resource_tags: Tags to assign to monitor.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1da201141928cd17a5dfa2d08e87045b296530c05640d211ef71adaee76034d3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAnomalyMonitorProps(
            monitor_name=monitor_name,
            monitor_type=monitor_type,
            monitor_dimension=monitor_dimension,
            monitor_specification=monitor_specification,
            resource_tags=resource_tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6921f8abc6dadac739e2b96af2776140990a7019006bfdd7eb73d790e771a751)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c18e7a7bff8e46a4e848ee3e3e50aab723d5eea60fb1bcfe13cb9258fc9b62b4)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreationDate")
    def attr_creation_date(self) -> builtins.str:
        '''The date when the monitor was created.

        :cloudformationAttribute: CreationDate
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationDate"))

    @builtins.property
    @jsii.member(jsii_name="attrDimensionalValueCount")
    def attr_dimensional_value_count(self) -> jsii.Number:
        '''The value for evaluated dimensions.

        :cloudformationAttribute: DimensionalValueCount
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrDimensionalValueCount"))

    @builtins.property
    @jsii.member(jsii_name="attrLastEvaluatedDate")
    def attr_last_evaluated_date(self) -> builtins.str:
        '''The date when the monitor last evaluated for anomalies.

        :cloudformationAttribute: LastEvaluatedDate
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastEvaluatedDate"))

    @builtins.property
    @jsii.member(jsii_name="attrLastUpdatedDate")
    def attr_last_updated_date(self) -> builtins.str:
        '''The date when the monitor was last updated.

        :cloudformationAttribute: LastUpdatedDate
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastUpdatedDate"))

    @builtins.property
    @jsii.member(jsii_name="attrMonitorArn")
    def attr_monitor_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) value for the monitor.

        :cloudformationAttribute: MonitorArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrMonitorArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="monitorName")
    def monitor_name(self) -> builtins.str:
        '''The name of the monitor.'''
        return typing.cast(builtins.str, jsii.get(self, "monitorName"))

    @monitor_name.setter
    def monitor_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cfeecbe9441840f2127a89ea3c6dcac344dda1d52a4499f3590067d9fff9ddb7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "monitorName", value)

    @builtins.property
    @jsii.member(jsii_name="monitorType")
    def monitor_type(self) -> builtins.str:
        '''The possible type values.'''
        return typing.cast(builtins.str, jsii.get(self, "monitorType"))

    @monitor_type.setter
    def monitor_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e5bea89fd492e9706efb91eaa83153a8dbfa7897ada18db8817750d506e8b35)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "monitorType", value)

    @builtins.property
    @jsii.member(jsii_name="monitorDimension")
    def monitor_dimension(self) -> typing.Optional[builtins.str]:
        '''The dimensions to evaluate.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "monitorDimension"))

    @monitor_dimension.setter
    def monitor_dimension(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__081fb13a76df355e897fe83b300dc3c3b7b314dd67c85a0848b5ad8edf04af7b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "monitorDimension", value)

    @builtins.property
    @jsii.member(jsii_name="monitorSpecification")
    def monitor_specification(self) -> typing.Optional[builtins.str]:
        '''The array of ``MonitorSpecification`` in JSON array format.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "monitorSpecification"))

    @monitor_specification.setter
    def monitor_specification(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__defe54ffa1f8d0ba42e79c23d33cf33a974c7edb52b847d17428227cd77608f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "monitorSpecification", value)

    @builtins.property
    @jsii.member(jsii_name="resourceTags")
    def resource_tags(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAnomalyMonitor.ResourceTagProperty"]]]]:
        '''Tags to assign to monitor.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAnomalyMonitor.ResourceTagProperty"]]]], jsii.get(self, "resourceTags"))

    @resource_tags.setter
    def resource_tags(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAnomalyMonitor.ResourceTagProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba083795f73cd6c7f4640bfcb9887f75331ec7dd734bce22e3485bbd80c7ad10)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceTags", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ce.CfnAnomalyMonitor.ResourceTagProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class ResourceTagProperty:
        def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
            '''The tag structure that contains a tag key and value.

            .. epigraph::

               Tagging is supported only for the following Cost Explorer resource types: ```AnomalyMonitor`` <https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AnomalyMonitor.html>`_ , ```AnomalySubscription`` <https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AnomalySubscription.html>`_ , ```CostCategory`` <https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostCategory.html>`_ .

            :param key: The key that's associated with the tag.
            :param value: The value that's associated with the tag.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ce-anomalymonitor-resourcetag.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ce as ce
                
                resource_tag_property = ce.CfnAnomalyMonitor.ResourceTagProperty(
                    key="key",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cc18b973c71e81e255e27dad2836a92430d74f82a098cca99c00f6f0961ac825)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "key": key,
                "value": value,
            }

        @builtins.property
        def key(self) -> builtins.str:
            '''The key that's associated with the tag.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ce-anomalymonitor-resourcetag.html#cfn-ce-anomalymonitor-resourcetag-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''The value that's associated with the tag.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ce-anomalymonitor-resourcetag.html#cfn-ce-anomalymonitor-resourcetag-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResourceTagProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ce.CfnAnomalyMonitorProps",
    jsii_struct_bases=[],
    name_mapping={
        "monitor_name": "monitorName",
        "monitor_type": "monitorType",
        "monitor_dimension": "monitorDimension",
        "monitor_specification": "monitorSpecification",
        "resource_tags": "resourceTags",
    },
)
class CfnAnomalyMonitorProps:
    def __init__(
        self,
        *,
        monitor_name: builtins.str,
        monitor_type: builtins.str,
        monitor_dimension: typing.Optional[builtins.str] = None,
        monitor_specification: typing.Optional[builtins.str] = None,
        resource_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnomalyMonitor.ResourceTagProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnAnomalyMonitor``.

        :param monitor_name: The name of the monitor.
        :param monitor_type: The possible type values.
        :param monitor_dimension: The dimensions to evaluate.
        :param monitor_specification: The array of ``MonitorSpecification`` in JSON array format. For instance, you can use ``MonitorSpecification`` to specify a tag, Cost Category, or linked account for your custom anomaly monitor. For further information, see the `Examples <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalymonitor.html#aws-resource-ce-anomalymonitor--examples>`_ section of this page.
        :param resource_tags: Tags to assign to monitor.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalymonitor.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ce as ce
            
            cfn_anomaly_monitor_props = ce.CfnAnomalyMonitorProps(
                monitor_name="monitorName",
                monitor_type="monitorType",
            
                # the properties below are optional
                monitor_dimension="monitorDimension",
                monitor_specification="monitorSpecification",
                resource_tags=[ce.CfnAnomalyMonitor.ResourceTagProperty(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cecf9328096cac203771c26042b74dd2c0cac83d731fd388244ec9f88a93ad85)
            check_type(argname="argument monitor_name", value=monitor_name, expected_type=type_hints["monitor_name"])
            check_type(argname="argument monitor_type", value=monitor_type, expected_type=type_hints["monitor_type"])
            check_type(argname="argument monitor_dimension", value=monitor_dimension, expected_type=type_hints["monitor_dimension"])
            check_type(argname="argument monitor_specification", value=monitor_specification, expected_type=type_hints["monitor_specification"])
            check_type(argname="argument resource_tags", value=resource_tags, expected_type=type_hints["resource_tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "monitor_name": monitor_name,
            "monitor_type": monitor_type,
        }
        if monitor_dimension is not None:
            self._values["monitor_dimension"] = monitor_dimension
        if monitor_specification is not None:
            self._values["monitor_specification"] = monitor_specification
        if resource_tags is not None:
            self._values["resource_tags"] = resource_tags

    @builtins.property
    def monitor_name(self) -> builtins.str:
        '''The name of the monitor.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalymonitor.html#cfn-ce-anomalymonitor-monitorname
        '''
        result = self._values.get("monitor_name")
        assert result is not None, "Required property 'monitor_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def monitor_type(self) -> builtins.str:
        '''The possible type values.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalymonitor.html#cfn-ce-anomalymonitor-monitortype
        '''
        result = self._values.get("monitor_type")
        assert result is not None, "Required property 'monitor_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def monitor_dimension(self) -> typing.Optional[builtins.str]:
        '''The dimensions to evaluate.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalymonitor.html#cfn-ce-anomalymonitor-monitordimension
        '''
        result = self._values.get("monitor_dimension")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def monitor_specification(self) -> typing.Optional[builtins.str]:
        '''The array of ``MonitorSpecification`` in JSON array format.

        For instance, you can use ``MonitorSpecification`` to specify a tag, Cost Category, or linked account for your custom anomaly monitor. For further information, see the `Examples <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalymonitor.html#aws-resource-ce-anomalymonitor--examples>`_ section of this page.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalymonitor.html#cfn-ce-anomalymonitor-monitorspecification
        '''
        result = self._values.get("monitor_specification")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resource_tags(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnAnomalyMonitor.ResourceTagProperty]]]]:
        '''Tags to assign to monitor.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalymonitor.html#cfn-ce-anomalymonitor-resourcetags
        '''
        result = self._values.get("resource_tags")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnAnomalyMonitor.ResourceTagProperty]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAnomalyMonitorProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnAnomalySubscription(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ce.CfnAnomalySubscription",
):
    '''The ``AWS::CE::AnomalySubscription`` resource (also referred to as an alert subscription) is a Cost Explorer resource type that sends notifications about specific anomalies that meet an alerting criteria defined by you.

    You can specify the frequency of the alerts and the subscribers to notify.

    Anomaly subscriptions can be associated with one or more ```AWS::CE::AnomalyMonitor`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalymonitor.html>`_ resources, and they only send notifications about anomalies detected by those associated monitors. You can also configure a threshold to further control which anomalies are included in the notifications.

    Anomalies that don’t exceed the chosen threshold and therefore don’t trigger notifications from an anomaly subscription will still be available on the console and from the ```GetAnomalies`` <https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetAnomalies.html>`_ API.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalysubscription.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ce as ce
        
        cfn_anomaly_subscription = ce.CfnAnomalySubscription(self, "MyCfnAnomalySubscription",
            frequency="frequency",
            monitor_arn_list=["monitorArnList"],
            subscribers=[ce.CfnAnomalySubscription.SubscriberProperty(
                address="address",
                type="type",
        
                # the properties below are optional
                status="status"
            )],
            subscription_name="subscriptionName",
        
            # the properties below are optional
            resource_tags=[ce.CfnAnomalySubscription.ResourceTagProperty(
                key="key",
                value="value"
            )],
            threshold=123,
            threshold_expression="thresholdExpression"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        frequency: builtins.str,
        monitor_arn_list: typing.Sequence[builtins.str],
        subscribers: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAnomalySubscription.SubscriberProperty", typing.Dict[builtins.str, typing.Any]]]]],
        subscription_name: builtins.str,
        resource_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAnomalySubscription.ResourceTagProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        threshold: typing.Optional[jsii.Number] = None,
        threshold_expression: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param frequency: The frequency that anomaly notifications are sent. Notifications are sent either over email (for DAILY and WEEKLY frequencies) or SNS (for IMMEDIATE frequency). For more information, see `Creating an Amazon SNS topic for anomaly notifications <https://docs.aws.amazon.com/cost-management/latest/userguide/ad-SNS.html>`_ .
        :param monitor_arn_list: A list of cost anomaly monitors.
        :param subscribers: A list of subscribers to notify.
        :param subscription_name: The name for the subscription.
        :param resource_tags: Tags to assign to subscription.
        :param threshold: (deprecated). An absolute dollar value that must be exceeded by the anomaly's total impact (see `Impact <https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Impact.html>`_ for more details) for an anomaly notification to be generated. This field has been deprecated. To specify a threshold, use ThresholdExpression. Continued use of Threshold will be treated as shorthand syntax for a ThresholdExpression. One of Threshold or ThresholdExpression is required for ``AWS::CE::AnomalySubscription`` . You cannot specify both.
        :param threshold_expression: An `Expression <https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Expression.html>`_ object in JSON string format used to specify the anomalies that you want to generate alerts for. This supports dimensions and nested expressions. The supported dimensions are ``ANOMALY_TOTAL_IMPACT_ABSOLUTE`` and ``ANOMALY_TOTAL_IMPACT_PERCENTAGE`` , corresponding to an anomaly’s TotalImpact and TotalImpactPercentage, respectively (see `Impact <https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Impact.html>`_ for more details). The supported nested expression types are ``AND`` and ``OR`` . The match option ``GREATER_THAN_OR_EQUAL`` is required. Values must be numbers between 0 and 10,000,000,000 in string format. One of Threshold or ThresholdExpression is required for ``AWS::CE::AnomalySubscription`` . You cannot specify both. For further information, see the `Examples <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalysubscription.html#aws-resource-ce-anomalysubscription--examples>`_ section of this page.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a7fbd046e3b9f6f7efea32f7eb528d813f3ccf81de7e59ec417de1ea0ca07d6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAnomalySubscriptionProps(
            frequency=frequency,
            monitor_arn_list=monitor_arn_list,
            subscribers=subscribers,
            subscription_name=subscription_name,
            resource_tags=resource_tags,
            threshold=threshold,
            threshold_expression=threshold_expression,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c54286f48d192b89d3c5e9f4bece98af6cb4bd7105c8a82d31e76abe30545c0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d3c2f4d61d0c155803b7895cff82b1eedd3dc1f5e6fcec96cf441bd563253a86)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAccountId")
    def attr_account_id(self) -> builtins.str:
        '''Your unique account identifier.

        :cloudformationAttribute: AccountId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAccountId"))

    @builtins.property
    @jsii.member(jsii_name="attrSubscriptionArn")
    def attr_subscription_arn(self) -> builtins.str:
        '''The ``AnomalySubscription`` Amazon Resource Name (ARN).

        :cloudformationAttribute: SubscriptionArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSubscriptionArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="frequency")
    def frequency(self) -> builtins.str:
        '''The frequency that anomaly notifications are sent.'''
        return typing.cast(builtins.str, jsii.get(self, "frequency"))

    @frequency.setter
    def frequency(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f65afcf3186751c82f39cbede0dcab6ddc80f7d9c0b422c5b129658eaab61559)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "frequency", value)

    @builtins.property
    @jsii.member(jsii_name="monitorArnList")
    def monitor_arn_list(self) -> typing.List[builtins.str]:
        '''A list of cost anomaly monitors.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "monitorArnList"))

    @monitor_arn_list.setter
    def monitor_arn_list(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f4d8eb48da6a9844668f539149825f89478d1e3e3ed4e1afcd927a288c88922)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "monitorArnList", value)

    @builtins.property
    @jsii.member(jsii_name="subscribers")
    def subscribers(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAnomalySubscription.SubscriberProperty"]]]:
        '''A list of subscribers to notify.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAnomalySubscription.SubscriberProperty"]]], jsii.get(self, "subscribers"))

    @subscribers.setter
    def subscribers(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAnomalySubscription.SubscriberProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5656753df5f64fe42e45494608ada7acc3f3ea8f09a108fc5083bce855ae7242)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subscribers", value)

    @builtins.property
    @jsii.member(jsii_name="subscriptionName")
    def subscription_name(self) -> builtins.str:
        '''The name for the subscription.'''
        return typing.cast(builtins.str, jsii.get(self, "subscriptionName"))

    @subscription_name.setter
    def subscription_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f1c77a5656251a1b2332edd8152e7fb9ac370a8031e07485ff8e8b8927e8804)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subscriptionName", value)

    @builtins.property
    @jsii.member(jsii_name="resourceTags")
    def resource_tags(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAnomalySubscription.ResourceTagProperty"]]]]:
        '''Tags to assign to subscription.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAnomalySubscription.ResourceTagProperty"]]]], jsii.get(self, "resourceTags"))

    @resource_tags.setter
    def resource_tags(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAnomalySubscription.ResourceTagProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96793ef54afc05012d539871c866a4c4cbe5b328c47be446ea5408e64a1f523a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceTags", value)

    @builtins.property
    @jsii.member(jsii_name="threshold")
    def threshold(self) -> typing.Optional[jsii.Number]:
        '''(deprecated).'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "threshold"))

    @threshold.setter
    def threshold(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2ca78f072bfc658750298a3034ad4215f682bc5042b1decb8a002cf443b518e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "threshold", value)

    @builtins.property
    @jsii.member(jsii_name="thresholdExpression")
    def threshold_expression(self) -> typing.Optional[builtins.str]:
        '''An `Expression <https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Expression.html>`_ object in JSON string format used to specify the anomalies that you want to generate alerts for. This supports dimensions and nested expressions. The supported dimensions are ``ANOMALY_TOTAL_IMPACT_ABSOLUTE`` and ``ANOMALY_TOTAL_IMPACT_PERCENTAGE`` , corresponding to an anomaly’s TotalImpact and TotalImpactPercentage, respectively (see `Impact <https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Impact.html>`_ for more details). The supported nested expression types are ``AND`` and ``OR`` . The match option ``GREATER_THAN_OR_EQUAL`` is required. Values must be numbers between 0 and 10,000,000,000 in string format.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "thresholdExpression"))

    @threshold_expression.setter
    def threshold_expression(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7af5c240cdcab7ad56cf11aac1adeb1e136f2fd4b10b281e21e29b1ef870583)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "thresholdExpression", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ce.CfnAnomalySubscription.ResourceTagProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class ResourceTagProperty:
        def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
            '''The tag structure that contains a tag key and value.

            .. epigraph::

               Tagging is supported only for the following Cost Explorer resource types: ```AnomalyMonitor`` <https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AnomalyMonitor.html>`_ , ```AnomalySubscription`` <https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AnomalySubscription.html>`_ , ```CostCategory`` <https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostCategory.html>`_ .

            :param key: The key that's associated with the tag.
            :param value: The value that's associated with the tag.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ce-anomalysubscription-resourcetag.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ce as ce
                
                resource_tag_property = ce.CfnAnomalySubscription.ResourceTagProperty(
                    key="key",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__35c1680ae1c4709516aa75a05e96a554da511c81b2ef5c9752e0d8801e4ad445)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "key": key,
                "value": value,
            }

        @builtins.property
        def key(self) -> builtins.str:
            '''The key that's associated with the tag.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ce-anomalysubscription-resourcetag.html#cfn-ce-anomalysubscription-resourcetag-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''The value that's associated with the tag.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ce-anomalysubscription-resourcetag.html#cfn-ce-anomalysubscription-resourcetag-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResourceTagProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ce.CfnAnomalySubscription.SubscriberProperty",
        jsii_struct_bases=[],
        name_mapping={"address": "address", "type": "type", "status": "status"},
    )
    class SubscriberProperty:
        def __init__(
            self,
            *,
            address: builtins.str,
            type: builtins.str,
            status: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The recipient of ``AnomalySubscription`` notifications.

            :param address: The email address or SNS Topic Amazon Resource Name (ARN), depending on the ``Type`` .
            :param type: The notification delivery channel.
            :param status: Indicates if the subscriber accepts the notifications.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ce-anomalysubscription-subscriber.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ce as ce
                
                subscriber_property = ce.CfnAnomalySubscription.SubscriberProperty(
                    address="address",
                    type="type",
                
                    # the properties below are optional
                    status="status"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__94192f14eef4d01fe40ae59ec5600ceee6ddb3486c0056d9f68639a5574d726f)
                check_type(argname="argument address", value=address, expected_type=type_hints["address"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "address": address,
                "type": type,
            }
            if status is not None:
                self._values["status"] = status

        @builtins.property
        def address(self) -> builtins.str:
            '''The email address or SNS Topic Amazon Resource Name (ARN), depending on the ``Type`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ce-anomalysubscription-subscriber.html#cfn-ce-anomalysubscription-subscriber-address
            '''
            result = self._values.get("address")
            assert result is not None, "Required property 'address' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def type(self) -> builtins.str:
            '''The notification delivery channel.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ce-anomalysubscription-subscriber.html#cfn-ce-anomalysubscription-subscriber-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def status(self) -> typing.Optional[builtins.str]:
            '''Indicates if the subscriber accepts the notifications.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ce-anomalysubscription-subscriber.html#cfn-ce-anomalysubscription-subscriber-status
            '''
            result = self._values.get("status")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SubscriberProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ce.CfnAnomalySubscriptionProps",
    jsii_struct_bases=[],
    name_mapping={
        "frequency": "frequency",
        "monitor_arn_list": "monitorArnList",
        "subscribers": "subscribers",
        "subscription_name": "subscriptionName",
        "resource_tags": "resourceTags",
        "threshold": "threshold",
        "threshold_expression": "thresholdExpression",
    },
)
class CfnAnomalySubscriptionProps:
    def __init__(
        self,
        *,
        frequency: builtins.str,
        monitor_arn_list: typing.Sequence[builtins.str],
        subscribers: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnomalySubscription.SubscriberProperty, typing.Dict[builtins.str, typing.Any]]]]],
        subscription_name: builtins.str,
        resource_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnomalySubscription.ResourceTagProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        threshold: typing.Optional[jsii.Number] = None,
        threshold_expression: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnAnomalySubscription``.

        :param frequency: The frequency that anomaly notifications are sent. Notifications are sent either over email (for DAILY and WEEKLY frequencies) or SNS (for IMMEDIATE frequency). For more information, see `Creating an Amazon SNS topic for anomaly notifications <https://docs.aws.amazon.com/cost-management/latest/userguide/ad-SNS.html>`_ .
        :param monitor_arn_list: A list of cost anomaly monitors.
        :param subscribers: A list of subscribers to notify.
        :param subscription_name: The name for the subscription.
        :param resource_tags: Tags to assign to subscription.
        :param threshold: (deprecated). An absolute dollar value that must be exceeded by the anomaly's total impact (see `Impact <https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Impact.html>`_ for more details) for an anomaly notification to be generated. This field has been deprecated. To specify a threshold, use ThresholdExpression. Continued use of Threshold will be treated as shorthand syntax for a ThresholdExpression. One of Threshold or ThresholdExpression is required for ``AWS::CE::AnomalySubscription`` . You cannot specify both.
        :param threshold_expression: An `Expression <https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Expression.html>`_ object in JSON string format used to specify the anomalies that you want to generate alerts for. This supports dimensions and nested expressions. The supported dimensions are ``ANOMALY_TOTAL_IMPACT_ABSOLUTE`` and ``ANOMALY_TOTAL_IMPACT_PERCENTAGE`` , corresponding to an anomaly’s TotalImpact and TotalImpactPercentage, respectively (see `Impact <https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Impact.html>`_ for more details). The supported nested expression types are ``AND`` and ``OR`` . The match option ``GREATER_THAN_OR_EQUAL`` is required. Values must be numbers between 0 and 10,000,000,000 in string format. One of Threshold or ThresholdExpression is required for ``AWS::CE::AnomalySubscription`` . You cannot specify both. For further information, see the `Examples <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalysubscription.html#aws-resource-ce-anomalysubscription--examples>`_ section of this page.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalysubscription.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ce as ce
            
            cfn_anomaly_subscription_props = ce.CfnAnomalySubscriptionProps(
                frequency="frequency",
                monitor_arn_list=["monitorArnList"],
                subscribers=[ce.CfnAnomalySubscription.SubscriberProperty(
                    address="address",
                    type="type",
            
                    # the properties below are optional
                    status="status"
                )],
                subscription_name="subscriptionName",
            
                # the properties below are optional
                resource_tags=[ce.CfnAnomalySubscription.ResourceTagProperty(
                    key="key",
                    value="value"
                )],
                threshold=123,
                threshold_expression="thresholdExpression"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ecbba42bf6256357cc87f360e68887f3b891e586d17671e12b6514517d7b303c)
            check_type(argname="argument frequency", value=frequency, expected_type=type_hints["frequency"])
            check_type(argname="argument monitor_arn_list", value=monitor_arn_list, expected_type=type_hints["monitor_arn_list"])
            check_type(argname="argument subscribers", value=subscribers, expected_type=type_hints["subscribers"])
            check_type(argname="argument subscription_name", value=subscription_name, expected_type=type_hints["subscription_name"])
            check_type(argname="argument resource_tags", value=resource_tags, expected_type=type_hints["resource_tags"])
            check_type(argname="argument threshold", value=threshold, expected_type=type_hints["threshold"])
            check_type(argname="argument threshold_expression", value=threshold_expression, expected_type=type_hints["threshold_expression"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "frequency": frequency,
            "monitor_arn_list": monitor_arn_list,
            "subscribers": subscribers,
            "subscription_name": subscription_name,
        }
        if resource_tags is not None:
            self._values["resource_tags"] = resource_tags
        if threshold is not None:
            self._values["threshold"] = threshold
        if threshold_expression is not None:
            self._values["threshold_expression"] = threshold_expression

    @builtins.property
    def frequency(self) -> builtins.str:
        '''The frequency that anomaly notifications are sent.

        Notifications are sent either over email (for DAILY and WEEKLY frequencies) or SNS (for IMMEDIATE frequency). For more information, see `Creating an Amazon SNS topic for anomaly notifications <https://docs.aws.amazon.com/cost-management/latest/userguide/ad-SNS.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalysubscription.html#cfn-ce-anomalysubscription-frequency
        '''
        result = self._values.get("frequency")
        assert result is not None, "Required property 'frequency' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def monitor_arn_list(self) -> typing.List[builtins.str]:
        '''A list of cost anomaly monitors.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalysubscription.html#cfn-ce-anomalysubscription-monitorarnlist
        '''
        result = self._values.get("monitor_arn_list")
        assert result is not None, "Required property 'monitor_arn_list' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def subscribers(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnAnomalySubscription.SubscriberProperty]]]:
        '''A list of subscribers to notify.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalysubscription.html#cfn-ce-anomalysubscription-subscribers
        '''
        result = self._values.get("subscribers")
        assert result is not None, "Required property 'subscribers' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnAnomalySubscription.SubscriberProperty]]], result)

    @builtins.property
    def subscription_name(self) -> builtins.str:
        '''The name for the subscription.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalysubscription.html#cfn-ce-anomalysubscription-subscriptionname
        '''
        result = self._values.get("subscription_name")
        assert result is not None, "Required property 'subscription_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_tags(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnAnomalySubscription.ResourceTagProperty]]]]:
        '''Tags to assign to subscription.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalysubscription.html#cfn-ce-anomalysubscription-resourcetags
        '''
        result = self._values.get("resource_tags")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnAnomalySubscription.ResourceTagProperty]]]], result)

    @builtins.property
    def threshold(self) -> typing.Optional[jsii.Number]:
        '''(deprecated).

        An absolute dollar value that must be exceeded by the anomaly's total impact (see `Impact <https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Impact.html>`_ for more details) for an anomaly notification to be generated.

        This field has been deprecated. To specify a threshold, use ThresholdExpression. Continued use of Threshold will be treated as shorthand syntax for a ThresholdExpression.

        One of Threshold or ThresholdExpression is required for ``AWS::CE::AnomalySubscription`` . You cannot specify both.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalysubscription.html#cfn-ce-anomalysubscription-threshold
        '''
        result = self._values.get("threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def threshold_expression(self) -> typing.Optional[builtins.str]:
        '''An `Expression <https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Expression.html>`_ object in JSON string format used to specify the anomalies that you want to generate alerts for. This supports dimensions and nested expressions. The supported dimensions are ``ANOMALY_TOTAL_IMPACT_ABSOLUTE`` and ``ANOMALY_TOTAL_IMPACT_PERCENTAGE`` , corresponding to an anomaly’s TotalImpact and TotalImpactPercentage, respectively (see `Impact <https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Impact.html>`_ for more details). The supported nested expression types are ``AND`` and ``OR`` . The match option ``GREATER_THAN_OR_EQUAL`` is required. Values must be numbers between 0 and 10,000,000,000 in string format.

        One of Threshold or ThresholdExpression is required for ``AWS::CE::AnomalySubscription`` . You cannot specify both.

        For further information, see the `Examples <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalysubscription.html#aws-resource-ce-anomalysubscription--examples>`_ section of this page.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-anomalysubscription.html#cfn-ce-anomalysubscription-thresholdexpression
        '''
        result = self._values.get("threshold_expression")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAnomalySubscriptionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnCostCategory(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ce.CfnCostCategory",
):
    '''The ``AWS::CE::CostCategory`` resource creates groupings of cost that you can use across products in the AWS Billing and Cost Management console, such as Cost Explorer and AWS Budgets.

    For more information, see `Managing Your Costs with Cost Categories <https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/manage-cost-categories.html>`_ in the *AWS Billing and Cost Management User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-costcategory.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ce as ce
        
        cfn_cost_category = ce.CfnCostCategory(self, "MyCfnCostCategory",
            name="name",
            rules="rules",
            rule_version="ruleVersion",
        
            # the properties below are optional
            default_value="defaultValue",
            split_charge_rules="splitChargeRules"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        rules: builtins.str,
        rule_version: builtins.str,
        default_value: typing.Optional[builtins.str] = None,
        split_charge_rules: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The unique name of the Cost Category.
        :param rules: The array of CostCategoryRule in JSON array format. .. epigraph:: Rules are processed in order. If there are multiple rules that match the line item, then the first rule to match is used to determine that Cost Category value.
        :param rule_version: The rule schema version in this particular Cost Category.
        :param default_value: The default value for the cost category.
        :param split_charge_rules: The split charge rules that are used to allocate your charges between your Cost Category values.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d86a2b59e53c629c2de8bd291387500a9799712ca28f9459ef98f5dd619ad1a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCostCategoryProps(
            name=name,
            rules=rules,
            rule_version=rule_version,
            default_value=default_value,
            split_charge_rules=split_charge_rules,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea083274a2ae3f772a3f5c49320005c446ad623aa9e43da318adf0f2887f40a3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3f5803e9496c40234ca2172a547ee068f22f7fe2519c03d75cf8be6d7d5276ed)
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
        '''The unique identifier for your Cost Category.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrEffectiveStart")
    def attr_effective_start(self) -> builtins.str:
        '''The Cost Category's effective start date.

        :cloudformationAttribute: EffectiveStart
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEffectiveStart"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The unique name of the Cost Category.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c70a6a6b30c7629cbf9648d7cb87767c0abcdca421a37e18c362abd473958d6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="rules")
    def rules(self) -> builtins.str:
        '''The array of CostCategoryRule in JSON array format.'''
        return typing.cast(builtins.str, jsii.get(self, "rules"))

    @rules.setter
    def rules(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9949839e9bb2a9a8c66eb12f61f2ab9292a938d8843dde18183b57639dde8109)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rules", value)

    @builtins.property
    @jsii.member(jsii_name="ruleVersion")
    def rule_version(self) -> builtins.str:
        '''The rule schema version in this particular Cost Category.'''
        return typing.cast(builtins.str, jsii.get(self, "ruleVersion"))

    @rule_version.setter
    def rule_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__329b7ef9b522a04c5bcb415a88b90570cf2a6fa953de9bc5006b25fb356691ef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleVersion", value)

    @builtins.property
    @jsii.member(jsii_name="defaultValue")
    def default_value(self) -> typing.Optional[builtins.str]:
        '''The default value for the cost category.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultValue"))

    @default_value.setter
    def default_value(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa6f1a5d75da4f48510e6e623a48160929ac48b171d83bf2f8ea5f74c5c47828)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultValue", value)

    @builtins.property
    @jsii.member(jsii_name="splitChargeRules")
    def split_charge_rules(self) -> typing.Optional[builtins.str]:
        '''The split charge rules that are used to allocate your charges between your Cost Category values.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "splitChargeRules"))

    @split_charge_rules.setter
    def split_charge_rules(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae51b4a5cd7f6e8738ed01709064f1d42c9cdd90e02dfe56151acb9345ff50db)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "splitChargeRules", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ce.CfnCostCategoryProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "rules": "rules",
        "rule_version": "ruleVersion",
        "default_value": "defaultValue",
        "split_charge_rules": "splitChargeRules",
    },
)
class CfnCostCategoryProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        rules: builtins.str,
        rule_version: builtins.str,
        default_value: typing.Optional[builtins.str] = None,
        split_charge_rules: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnCostCategory``.

        :param name: The unique name of the Cost Category.
        :param rules: The array of CostCategoryRule in JSON array format. .. epigraph:: Rules are processed in order. If there are multiple rules that match the line item, then the first rule to match is used to determine that Cost Category value.
        :param rule_version: The rule schema version in this particular Cost Category.
        :param default_value: The default value for the cost category.
        :param split_charge_rules: The split charge rules that are used to allocate your charges between your Cost Category values.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-costcategory.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ce as ce
            
            cfn_cost_category_props = ce.CfnCostCategoryProps(
                name="name",
                rules="rules",
                rule_version="ruleVersion",
            
                # the properties below are optional
                default_value="defaultValue",
                split_charge_rules="splitChargeRules"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22fe6bbc471c7d1efb8863c64af07f8dbb0f94f407bc64ec8606d11422837dd3)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument rules", value=rules, expected_type=type_hints["rules"])
            check_type(argname="argument rule_version", value=rule_version, expected_type=type_hints["rule_version"])
            check_type(argname="argument default_value", value=default_value, expected_type=type_hints["default_value"])
            check_type(argname="argument split_charge_rules", value=split_charge_rules, expected_type=type_hints["split_charge_rules"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "rules": rules,
            "rule_version": rule_version,
        }
        if default_value is not None:
            self._values["default_value"] = default_value
        if split_charge_rules is not None:
            self._values["split_charge_rules"] = split_charge_rules

    @builtins.property
    def name(self) -> builtins.str:
        '''The unique name of the Cost Category.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-costcategory.html#cfn-ce-costcategory-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rules(self) -> builtins.str:
        '''The array of CostCategoryRule in JSON array format.

        .. epigraph::

           Rules are processed in order. If there are multiple rules that match the line item, then the first rule to match is used to determine that Cost Category value.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-costcategory.html#cfn-ce-costcategory-rules
        '''
        result = self._values.get("rules")
        assert result is not None, "Required property 'rules' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rule_version(self) -> builtins.str:
        '''The rule schema version in this particular Cost Category.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-costcategory.html#cfn-ce-costcategory-ruleversion
        '''
        result = self._values.get("rule_version")
        assert result is not None, "Required property 'rule_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def default_value(self) -> typing.Optional[builtins.str]:
        '''The default value for the cost category.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-costcategory.html#cfn-ce-costcategory-defaultvalue
        '''
        result = self._values.get("default_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def split_charge_rules(self) -> typing.Optional[builtins.str]:
        '''The split charge rules that are used to allocate your charges between your Cost Category values.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-costcategory.html#cfn-ce-costcategory-splitchargerules
        '''
        result = self._values.get("split_charge_rules")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCostCategoryProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnAnomalyMonitor",
    "CfnAnomalyMonitorProps",
    "CfnAnomalySubscription",
    "CfnAnomalySubscriptionProps",
    "CfnCostCategory",
    "CfnCostCategoryProps",
]

publication.publish()

def _typecheckingstub__1da201141928cd17a5dfa2d08e87045b296530c05640d211ef71adaee76034d3(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    monitor_name: builtins.str,
    monitor_type: builtins.str,
    monitor_dimension: typing.Optional[builtins.str] = None,
    monitor_specification: typing.Optional[builtins.str] = None,
    resource_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnomalyMonitor.ResourceTagProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6921f8abc6dadac739e2b96af2776140990a7019006bfdd7eb73d790e771a751(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c18e7a7bff8e46a4e848ee3e3e50aab723d5eea60fb1bcfe13cb9258fc9b62b4(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfeecbe9441840f2127a89ea3c6dcac344dda1d52a4499f3590067d9fff9ddb7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e5bea89fd492e9706efb91eaa83153a8dbfa7897ada18db8817750d506e8b35(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__081fb13a76df355e897fe83b300dc3c3b7b314dd67c85a0848b5ad8edf04af7b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__defe54ffa1f8d0ba42e79c23d33cf33a974c7edb52b847d17428227cd77608f8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba083795f73cd6c7f4640bfcb9887f75331ec7dd734bce22e3485bbd80c7ad10(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnAnomalyMonitor.ResourceTagProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc18b973c71e81e255e27dad2836a92430d74f82a098cca99c00f6f0961ac825(
    *,
    key: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cecf9328096cac203771c26042b74dd2c0cac83d731fd388244ec9f88a93ad85(
    *,
    monitor_name: builtins.str,
    monitor_type: builtins.str,
    monitor_dimension: typing.Optional[builtins.str] = None,
    monitor_specification: typing.Optional[builtins.str] = None,
    resource_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnomalyMonitor.ResourceTagProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a7fbd046e3b9f6f7efea32f7eb528d813f3ccf81de7e59ec417de1ea0ca07d6(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    frequency: builtins.str,
    monitor_arn_list: typing.Sequence[builtins.str],
    subscribers: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnomalySubscription.SubscriberProperty, typing.Dict[builtins.str, typing.Any]]]]],
    subscription_name: builtins.str,
    resource_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnomalySubscription.ResourceTagProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    threshold: typing.Optional[jsii.Number] = None,
    threshold_expression: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c54286f48d192b89d3c5e9f4bece98af6cb4bd7105c8a82d31e76abe30545c0(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3c2f4d61d0c155803b7895cff82b1eedd3dc1f5e6fcec96cf441bd563253a86(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f65afcf3186751c82f39cbede0dcab6ddc80f7d9c0b422c5b129658eaab61559(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f4d8eb48da6a9844668f539149825f89478d1e3e3ed4e1afcd927a288c88922(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5656753df5f64fe42e45494608ada7acc3f3ea8f09a108fc5083bce855ae7242(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnAnomalySubscription.SubscriberProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f1c77a5656251a1b2332edd8152e7fb9ac370a8031e07485ff8e8b8927e8804(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96793ef54afc05012d539871c866a4c4cbe5b328c47be446ea5408e64a1f523a(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnAnomalySubscription.ResourceTagProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2ca78f072bfc658750298a3034ad4215f682bc5042b1decb8a002cf443b518e(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7af5c240cdcab7ad56cf11aac1adeb1e136f2fd4b10b281e21e29b1ef870583(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35c1680ae1c4709516aa75a05e96a554da511c81b2ef5c9752e0d8801e4ad445(
    *,
    key: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94192f14eef4d01fe40ae59ec5600ceee6ddb3486c0056d9f68639a5574d726f(
    *,
    address: builtins.str,
    type: builtins.str,
    status: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ecbba42bf6256357cc87f360e68887f3b891e586d17671e12b6514517d7b303c(
    *,
    frequency: builtins.str,
    monitor_arn_list: typing.Sequence[builtins.str],
    subscribers: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnomalySubscription.SubscriberProperty, typing.Dict[builtins.str, typing.Any]]]]],
    subscription_name: builtins.str,
    resource_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnomalySubscription.ResourceTagProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    threshold: typing.Optional[jsii.Number] = None,
    threshold_expression: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d86a2b59e53c629c2de8bd291387500a9799712ca28f9459ef98f5dd619ad1a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    rules: builtins.str,
    rule_version: builtins.str,
    default_value: typing.Optional[builtins.str] = None,
    split_charge_rules: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea083274a2ae3f772a3f5c49320005c446ad623aa9e43da318adf0f2887f40a3(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f5803e9496c40234ca2172a547ee068f22f7fe2519c03d75cf8be6d7d5276ed(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c70a6a6b30c7629cbf9648d7cb87767c0abcdca421a37e18c362abd473958d6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9949839e9bb2a9a8c66eb12f61f2ab9292a938d8843dde18183b57639dde8109(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__329b7ef9b522a04c5bcb415a88b90570cf2a6fa953de9bc5006b25fb356691ef(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa6f1a5d75da4f48510e6e623a48160929ac48b171d83bf2f8ea5f74c5c47828(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae51b4a5cd7f6e8738ed01709064f1d42c9cdd90e02dfe56151acb9345ff50db(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22fe6bbc471c7d1efb8863c64af07f8dbb0f94f407bc64ec8606d11422837dd3(
    *,
    name: builtins.str,
    rules: builtins.str,
    rule_version: builtins.str,
    default_value: typing.Optional[builtins.str] = None,
    split_charge_rules: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
