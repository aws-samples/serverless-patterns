'''
# AWS::InternetMonitor Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_internetmonitor as internetmonitor
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for InternetMonitor construct libraries](https://constructs.dev/search?q=internetmonitor)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::InternetMonitor resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_InternetMonitor.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::InternetMonitor](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_InternetMonitor.html).

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
class CfnMonitor(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_internetmonitor.CfnMonitor",
):
    '''The ``AWS::InternetMonitor::Monitor`` resource is an Internet Monitor resource type that contains information about how you create a monitor in Amazon CloudWatch Internet Monitor.

    A monitor in Internet Monitor provides visibility into performance and availability between your applications hosted on AWS and your end users, using a traffic profile that it creates based on the application resources that you add: Virtual Private Clouds (VPCs), Amazon CloudFront distributions, or WorkSpaces directories.

    Internet Monitor also alerts you to internet issues that impact your application in the city-networks (geographies and networks) where your end users use it. With Internet Monitor, you can quickly pinpoint the locations and providers that are affected, so that you can address the issue.

    For more information, see `Using Amazon CloudWatch Internet Monitor <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-InternetMonitor.html>`_ in the *Amazon CloudWatch User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-internetmonitor-monitor.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_internetmonitor as internetmonitor
        
        cfn_monitor = internetmonitor.CfnMonitor(self, "MyCfnMonitor",
            monitor_name="monitorName",
        
            # the properties below are optional
            health_events_config=internetmonitor.CfnMonitor.HealthEventsConfigProperty(
                availability_score_threshold=123,
                performance_score_threshold=123
            ),
            internet_measurements_log_delivery=internetmonitor.CfnMonitor.InternetMeasurementsLogDeliveryProperty(
                s3_config=internetmonitor.CfnMonitor.S3ConfigProperty(
                    bucket_name="bucketName",
                    bucket_prefix="bucketPrefix",
                    log_delivery_status="logDeliveryStatus"
                )
            ),
            max_city_networks_to_monitor=123,
            resources=["resources"],
            resources_to_add=["resourcesToAdd"],
            resources_to_remove=["resourcesToRemove"],
            status="status",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            traffic_percentage_to_monitor=123
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        monitor_name: builtins.str,
        health_events_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMonitor.HealthEventsConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        internet_measurements_log_delivery: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMonitor.InternetMeasurementsLogDeliveryProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        max_city_networks_to_monitor: typing.Optional[jsii.Number] = None,
        resources: typing.Optional[typing.Sequence[builtins.str]] = None,
        resources_to_add: typing.Optional[typing.Sequence[builtins.str]] = None,
        resources_to_remove: typing.Optional[typing.Sequence[builtins.str]] = None,
        status: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        traffic_percentage_to_monitor: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param monitor_name: The name of the monitor. A monitor name can contain only alphanumeric characters, dashes (-), periods (.), and underscores (_).
        :param health_events_config: 
        :param internet_measurements_log_delivery: Publish internet measurements for a monitor for all city-networks (up to the 500,000 service limit) to another location, such as an Amazon S3 bucket. Measurements are also published to Amazon CloudWatch Logs for the first 500 (by traffic volume) city-networks (client locations and ASNs, typically internet service providers or ISPs).
        :param max_city_networks_to_monitor: The maximum number of city-networks to monitor for your resources. A city-network is the location (city) where clients access your application resources from and the network, such as an internet service provider, that clients access the resources through. For more information, see `Choosing a city-network maximum value <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/IMCityNetworksMaximum.html>`_ in *Using Amazon CloudWatch Internet Monitor* .
        :param resources: The resources that have been added for the monitor, listed by their Amazon Resource Names (ARNs).
        :param resources_to_add: The resources to add to a monitor, which you provide as a set of Amazon Resource Names (ARNs). You can add a combination of Virtual Private Clouds (VPCs) and Amazon CloudFront distributions, or you can add Amazon WorkSpaces directories. You can't add all three types of resources. .. epigraph:: If you add only VPC resources, at least one VPC must have an Internet Gateway attached to it, to make sure that it has internet connectivity.
        :param resources_to_remove: The resources to remove from a monitor, which you provide as a set of Amazon Resource Names (ARNs).
        :param status: The status of a monitor. The accepted values that you can specify for ``Status`` are ``ACTIVE`` and ``INACTIVE`` .
        :param tags: The tags for a monitor, listed as a set of *key:value* pairs.
        :param traffic_percentage_to_monitor: The percentage of the internet-facing traffic for your application that you want to monitor. You can also, optionally, set a limit for the number of city-networks (client locations and ASNs, typically internet service providers) that Internet Monitor will monitor traffic for. The city-networks maximum limit caps the number of city-networks that Internet Monitor monitors for your application, regardless of the percentage of traffic that you choose to monitor.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b49625d902a7236b204a8a96b68b35647ded5da14fa0241503fe8aed7ec47718)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnMonitorProps(
            monitor_name=monitor_name,
            health_events_config=health_events_config,
            internet_measurements_log_delivery=internet_measurements_log_delivery,
            max_city_networks_to_monitor=max_city_networks_to_monitor,
            resources=resources,
            resources_to_add=resources_to_add,
            resources_to_remove=resources_to_remove,
            status=status,
            tags=tags,
            traffic_percentage_to_monitor=traffic_percentage_to_monitor,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9b595277fbc445515d03337a4dad34db4660278ac9bbe6f5c8b9c7ed6952d46)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c84a3dbe4ef362dc6094809148408f29e223dcdc3bde69c3aa5c6af04a3682bf)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The time when the monitor was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrModifiedAt")
    def attr_modified_at(self) -> builtins.str:
        '''The last time that the monitor was modified.

        :cloudformationAttribute: ModifiedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrModifiedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrMonitorArn")
    def attr_monitor_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the monitor.

        :cloudformationAttribute: MonitorArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrMonitorArn"))

    @builtins.property
    @jsii.member(jsii_name="attrProcessingStatus")
    def attr_processing_status(self) -> builtins.str:
        '''The health of data processing for the monitor.

        For more information, see ``ProcessingStatus`` under `MonitorListMember <https://docs.aws.amazon.com/internet-monitor/latest/api/API_MonitorListMember.html>`_ in the *Amazon CloudWatch Internet Monitor API Reference* .

        :cloudformationAttribute: ProcessingStatus
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrProcessingStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrProcessingStatusInfo")
    def attr_processing_status_info(self) -> builtins.str:
        '''Additional information about the health of the data processing for the monitor.

        :cloudformationAttribute: ProcessingStatusInfo
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrProcessingStatusInfo"))

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
    @jsii.member(jsii_name="monitorName")
    def monitor_name(self) -> builtins.str:
        '''The name of the monitor.'''
        return typing.cast(builtins.str, jsii.get(self, "monitorName"))

    @monitor_name.setter
    def monitor_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef54ce1b63c1e0317ca73d33869cf2089b1ed66ab1da2e0c8fe45043287b6817)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "monitorName", value)

    @builtins.property
    @jsii.member(jsii_name="healthEventsConfig")
    def health_events_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMonitor.HealthEventsConfigProperty"]]:
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMonitor.HealthEventsConfigProperty"]], jsii.get(self, "healthEventsConfig"))

    @health_events_config.setter
    def health_events_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMonitor.HealthEventsConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1fcad87a381a34c71141a2be73ac8e81c442bd9d4616b8a8a55279c77a30bf9b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "healthEventsConfig", value)

    @builtins.property
    @jsii.member(jsii_name="internetMeasurementsLogDelivery")
    def internet_measurements_log_delivery(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMonitor.InternetMeasurementsLogDeliveryProperty"]]:
        '''Publish internet measurements for a monitor for all city-networks (up to the 500,000 service limit) to another location, such as an Amazon S3 bucket.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMonitor.InternetMeasurementsLogDeliveryProperty"]], jsii.get(self, "internetMeasurementsLogDelivery"))

    @internet_measurements_log_delivery.setter
    def internet_measurements_log_delivery(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMonitor.InternetMeasurementsLogDeliveryProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__edd584d7d64cd02983ca8858b15c31728e9294c416931001fc1a9ce5732ebad9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internetMeasurementsLogDelivery", value)

    @builtins.property
    @jsii.member(jsii_name="maxCityNetworksToMonitor")
    def max_city_networks_to_monitor(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of city-networks to monitor for your resources.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxCityNetworksToMonitor"))

    @max_city_networks_to_monitor.setter
    def max_city_networks_to_monitor(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44b26920fe092fdfabe5783619b4c150b5a44928ea63b71966ac31bfc9220c93)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxCityNetworksToMonitor", value)

    @builtins.property
    @jsii.member(jsii_name="resources")
    def resources(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The resources that have been added for the monitor, listed by their Amazon Resource Names (ARNs).'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "resources"))

    @resources.setter
    def resources(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b341be6dedc5e43e3921317eb724e72355e140557e075d7a60632555b8e832c4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resources", value)

    @builtins.property
    @jsii.member(jsii_name="resourcesToAdd")
    def resources_to_add(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The resources to add to a monitor, which you provide as a set of Amazon Resource Names (ARNs).'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "resourcesToAdd"))

    @resources_to_add.setter
    def resources_to_add(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6eb4096ee765fe908d059e9b8acdca0ec1f047ddb2fe5ede304ab5ee82444f95)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourcesToAdd", value)

    @builtins.property
    @jsii.member(jsii_name="resourcesToRemove")
    def resources_to_remove(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The resources to remove from a monitor, which you provide as a set of Amazon Resource Names (ARNs).'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "resourcesToRemove"))

    @resources_to_remove.setter
    def resources_to_remove(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9387e3cfcac600ed38b66e78df668311b567c717d8143713922de9b400262882)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourcesToRemove", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> typing.Optional[builtins.str]:
        '''The status of a monitor.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "status"))

    @status.setter
    def status(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f131dc53d07b00ba7900326b379a6d12c142d61ae7d7045e4e4abbd87c853da1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags for a monitor, listed as a set of *key:value* pairs.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8356cdf68080604804446d5b83fa308a2aa120e493bdc0ac24c31dbdc37894b7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="trafficPercentageToMonitor")
    def traffic_percentage_to_monitor(self) -> typing.Optional[jsii.Number]:
        '''The percentage of the internet-facing traffic for your application that you want to monitor.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "trafficPercentageToMonitor"))

    @traffic_percentage_to_monitor.setter
    def traffic_percentage_to_monitor(
        self,
        value: typing.Optional[jsii.Number],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b04e25dfeda5e88ea0ba9a753d013df9fa970065f64b69b4e930f01e15363029)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "trafficPercentageToMonitor", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_internetmonitor.CfnMonitor.HealthEventsConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "availability_score_threshold": "availabilityScoreThreshold",
            "performance_score_threshold": "performanceScoreThreshold",
        },
    )
    class HealthEventsConfigProperty:
        def __init__(
            self,
            *,
            availability_score_threshold: typing.Optional[jsii.Number] = None,
            performance_score_threshold: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Define the health event threshold percentages for the performance score and availability score for your application's monitor.

            Amazon CloudWatch Internet Monitor creates a health event when there's an internet issue that affects your application end users where a health score percentage is at or below a set threshold.

            If you don't set a health event threshold, the default value is 95%.

            :param availability_score_threshold: The health event threshold percentage set for availability scores. When the global availability score is at or below this percentage, Internet Monitor creates a health event.
            :param performance_score_threshold: The health event threshold percentage set for performance scores. When the global performance score is at or below this percentage, Internet Monitor creates a health event.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-internetmonitor-monitor-healtheventsconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_internetmonitor as internetmonitor
                
                health_events_config_property = internetmonitor.CfnMonitor.HealthEventsConfigProperty(
                    availability_score_threshold=123,
                    performance_score_threshold=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ba4b92afb6160c9794c6728a23a6695dc294c537ffbfec41a2e2341226207279)
                check_type(argname="argument availability_score_threshold", value=availability_score_threshold, expected_type=type_hints["availability_score_threshold"])
                check_type(argname="argument performance_score_threshold", value=performance_score_threshold, expected_type=type_hints["performance_score_threshold"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if availability_score_threshold is not None:
                self._values["availability_score_threshold"] = availability_score_threshold
            if performance_score_threshold is not None:
                self._values["performance_score_threshold"] = performance_score_threshold

        @builtins.property
        def availability_score_threshold(self) -> typing.Optional[jsii.Number]:
            '''The health event threshold percentage set for availability scores.

            When the global availability score is at or below this percentage, Internet Monitor creates a health event.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-internetmonitor-monitor-healtheventsconfig.html#cfn-internetmonitor-monitor-healtheventsconfig-availabilityscorethreshold
            '''
            result = self._values.get("availability_score_threshold")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def performance_score_threshold(self) -> typing.Optional[jsii.Number]:
            '''The health event threshold percentage set for performance scores.

            When the global performance score is at or below this percentage, Internet Monitor creates a health event.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-internetmonitor-monitor-healtheventsconfig.html#cfn-internetmonitor-monitor-healtheventsconfig-performancescorethreshold
            '''
            result = self._values.get("performance_score_threshold")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HealthEventsConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_internetmonitor.CfnMonitor.InternetMeasurementsLogDeliveryProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_config": "s3Config"},
    )
    class InternetMeasurementsLogDeliveryProperty:
        def __init__(
            self,
            *,
            s3_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMonitor.S3ConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Publish internet measurements to an Amazon S3 bucket in addition to CloudWatch Logs.

            :param s3_config: The configuration information for publishing Amazon CloudWatch Internet Monitor internet measurements to Amazon S3. The configuration includes the bucket name and (optionally) bucket prefix for the S3 bucket to store the measurements, and the delivery status. The delivery status is ``ENABLED`` if you choose to deliver internet measurements to an S3 bucket, and ``DISABLED`` otherwise.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-internetmonitor-monitor-internetmeasurementslogdelivery.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_internetmonitor as internetmonitor
                
                internet_measurements_log_delivery_property = internetmonitor.CfnMonitor.InternetMeasurementsLogDeliveryProperty(
                    s3_config=internetmonitor.CfnMonitor.S3ConfigProperty(
                        bucket_name="bucketName",
                        bucket_prefix="bucketPrefix",
                        log_delivery_status="logDeliveryStatus"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__be81e1048b4dd2c8c398b30d3055a799662f400cb08d51222af40dc7fabaeb42)
                check_type(argname="argument s3_config", value=s3_config, expected_type=type_hints["s3_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if s3_config is not None:
                self._values["s3_config"] = s3_config

        @builtins.property
        def s3_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMonitor.S3ConfigProperty"]]:
            '''The configuration information for publishing Amazon CloudWatch Internet Monitor internet measurements to Amazon S3.

            The configuration includes the bucket name and (optionally) bucket prefix for the S3 bucket to store the measurements, and the delivery status. The delivery status is ``ENABLED`` if you choose to deliver internet measurements to an S3 bucket, and ``DISABLED`` otherwise.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-internetmonitor-monitor-internetmeasurementslogdelivery.html#cfn-internetmonitor-monitor-internetmeasurementslogdelivery-s3config
            '''
            result = self._values.get("s3_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMonitor.S3ConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InternetMeasurementsLogDeliveryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_internetmonitor.CfnMonitor.S3ConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bucket_name": "bucketName",
            "bucket_prefix": "bucketPrefix",
            "log_delivery_status": "logDeliveryStatus",
        },
    )
    class S3ConfigProperty:
        def __init__(
            self,
            *,
            bucket_name: typing.Optional[builtins.str] = None,
            bucket_prefix: typing.Optional[builtins.str] = None,
            log_delivery_status: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The configuration for publishing Amazon CloudWatch Internet Monitor internet measurements to Amazon S3.

            The configuration includes the bucket name and (optionally) bucket prefix for the S3 bucket to store the measurements, and the delivery status. The delivery status is ``ENABLED`` if you choose to deliver internet measurements to S3 logs, and ``DISABLED`` otherwise.

            :param bucket_name: The Amazon S3 bucket name for internet measurements publishing.
            :param bucket_prefix: An optional Amazon S3 bucket prefix for internet measurements publishing.
            :param log_delivery_status: The status of publishing Internet Monitor internet measurements to an Amazon S3 bucket. The delivery status is ``ENABLED`` if you choose to deliver internet measurements to an S3 bucket, and ``DISABLED`` otherwise.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-internetmonitor-monitor-s3config.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_internetmonitor as internetmonitor
                
                s3_config_property = internetmonitor.CfnMonitor.S3ConfigProperty(
                    bucket_name="bucketName",
                    bucket_prefix="bucketPrefix",
                    log_delivery_status="logDeliveryStatus"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3ea826525df0e7912a2b2f0156891d9d00bda155e8b35634621c6e059a1b2b4b)
                check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
                check_type(argname="argument bucket_prefix", value=bucket_prefix, expected_type=type_hints["bucket_prefix"])
                check_type(argname="argument log_delivery_status", value=log_delivery_status, expected_type=type_hints["log_delivery_status"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if bucket_name is not None:
                self._values["bucket_name"] = bucket_name
            if bucket_prefix is not None:
                self._values["bucket_prefix"] = bucket_prefix
            if log_delivery_status is not None:
                self._values["log_delivery_status"] = log_delivery_status

        @builtins.property
        def bucket_name(self) -> typing.Optional[builtins.str]:
            '''The Amazon S3 bucket name for internet measurements publishing.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-internetmonitor-monitor-s3config.html#cfn-internetmonitor-monitor-s3config-bucketname
            '''
            result = self._values.get("bucket_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def bucket_prefix(self) -> typing.Optional[builtins.str]:
            '''An optional Amazon S3 bucket prefix for internet measurements publishing.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-internetmonitor-monitor-s3config.html#cfn-internetmonitor-monitor-s3config-bucketprefix
            '''
            result = self._values.get("bucket_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def log_delivery_status(self) -> typing.Optional[builtins.str]:
            '''The status of publishing Internet Monitor internet measurements to an Amazon S3 bucket.

            The delivery status is ``ENABLED`` if you choose to deliver internet measurements to an S3 bucket, and ``DISABLED`` otherwise.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-internetmonitor-monitor-s3config.html#cfn-internetmonitor-monitor-s3config-logdeliverystatus
            '''
            result = self._values.get("log_delivery_status")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3ConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_internetmonitor.CfnMonitorProps",
    jsii_struct_bases=[],
    name_mapping={
        "monitor_name": "monitorName",
        "health_events_config": "healthEventsConfig",
        "internet_measurements_log_delivery": "internetMeasurementsLogDelivery",
        "max_city_networks_to_monitor": "maxCityNetworksToMonitor",
        "resources": "resources",
        "resources_to_add": "resourcesToAdd",
        "resources_to_remove": "resourcesToRemove",
        "status": "status",
        "tags": "tags",
        "traffic_percentage_to_monitor": "trafficPercentageToMonitor",
    },
)
class CfnMonitorProps:
    def __init__(
        self,
        *,
        monitor_name: builtins.str,
        health_events_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMonitor.HealthEventsConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        internet_measurements_log_delivery: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMonitor.InternetMeasurementsLogDeliveryProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        max_city_networks_to_monitor: typing.Optional[jsii.Number] = None,
        resources: typing.Optional[typing.Sequence[builtins.str]] = None,
        resources_to_add: typing.Optional[typing.Sequence[builtins.str]] = None,
        resources_to_remove: typing.Optional[typing.Sequence[builtins.str]] = None,
        status: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        traffic_percentage_to_monitor: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Properties for defining a ``CfnMonitor``.

        :param monitor_name: The name of the monitor. A monitor name can contain only alphanumeric characters, dashes (-), periods (.), and underscores (_).
        :param health_events_config: 
        :param internet_measurements_log_delivery: Publish internet measurements for a monitor for all city-networks (up to the 500,000 service limit) to another location, such as an Amazon S3 bucket. Measurements are also published to Amazon CloudWatch Logs for the first 500 (by traffic volume) city-networks (client locations and ASNs, typically internet service providers or ISPs).
        :param max_city_networks_to_monitor: The maximum number of city-networks to monitor for your resources. A city-network is the location (city) where clients access your application resources from and the network, such as an internet service provider, that clients access the resources through. For more information, see `Choosing a city-network maximum value <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/IMCityNetworksMaximum.html>`_ in *Using Amazon CloudWatch Internet Monitor* .
        :param resources: The resources that have been added for the monitor, listed by their Amazon Resource Names (ARNs).
        :param resources_to_add: The resources to add to a monitor, which you provide as a set of Amazon Resource Names (ARNs). You can add a combination of Virtual Private Clouds (VPCs) and Amazon CloudFront distributions, or you can add Amazon WorkSpaces directories. You can't add all three types of resources. .. epigraph:: If you add only VPC resources, at least one VPC must have an Internet Gateway attached to it, to make sure that it has internet connectivity.
        :param resources_to_remove: The resources to remove from a monitor, which you provide as a set of Amazon Resource Names (ARNs).
        :param status: The status of a monitor. The accepted values that you can specify for ``Status`` are ``ACTIVE`` and ``INACTIVE`` .
        :param tags: The tags for a monitor, listed as a set of *key:value* pairs.
        :param traffic_percentage_to_monitor: The percentage of the internet-facing traffic for your application that you want to monitor. You can also, optionally, set a limit for the number of city-networks (client locations and ASNs, typically internet service providers) that Internet Monitor will monitor traffic for. The city-networks maximum limit caps the number of city-networks that Internet Monitor monitors for your application, regardless of the percentage of traffic that you choose to monitor.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-internetmonitor-monitor.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_internetmonitor as internetmonitor
            
            cfn_monitor_props = internetmonitor.CfnMonitorProps(
                monitor_name="monitorName",
            
                # the properties below are optional
                health_events_config=internetmonitor.CfnMonitor.HealthEventsConfigProperty(
                    availability_score_threshold=123,
                    performance_score_threshold=123
                ),
                internet_measurements_log_delivery=internetmonitor.CfnMonitor.InternetMeasurementsLogDeliveryProperty(
                    s3_config=internetmonitor.CfnMonitor.S3ConfigProperty(
                        bucket_name="bucketName",
                        bucket_prefix="bucketPrefix",
                        log_delivery_status="logDeliveryStatus"
                    )
                ),
                max_city_networks_to_monitor=123,
                resources=["resources"],
                resources_to_add=["resourcesToAdd"],
                resources_to_remove=["resourcesToRemove"],
                status="status",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                traffic_percentage_to_monitor=123
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a592873878a3205128bdbf7757cbce3b6e97783b1a68d0a1b5510ffc9f9f1fd8)
            check_type(argname="argument monitor_name", value=monitor_name, expected_type=type_hints["monitor_name"])
            check_type(argname="argument health_events_config", value=health_events_config, expected_type=type_hints["health_events_config"])
            check_type(argname="argument internet_measurements_log_delivery", value=internet_measurements_log_delivery, expected_type=type_hints["internet_measurements_log_delivery"])
            check_type(argname="argument max_city_networks_to_monitor", value=max_city_networks_to_monitor, expected_type=type_hints["max_city_networks_to_monitor"])
            check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
            check_type(argname="argument resources_to_add", value=resources_to_add, expected_type=type_hints["resources_to_add"])
            check_type(argname="argument resources_to_remove", value=resources_to_remove, expected_type=type_hints["resources_to_remove"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument traffic_percentage_to_monitor", value=traffic_percentage_to_monitor, expected_type=type_hints["traffic_percentage_to_monitor"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "monitor_name": monitor_name,
        }
        if health_events_config is not None:
            self._values["health_events_config"] = health_events_config
        if internet_measurements_log_delivery is not None:
            self._values["internet_measurements_log_delivery"] = internet_measurements_log_delivery
        if max_city_networks_to_monitor is not None:
            self._values["max_city_networks_to_monitor"] = max_city_networks_to_monitor
        if resources is not None:
            self._values["resources"] = resources
        if resources_to_add is not None:
            self._values["resources_to_add"] = resources_to_add
        if resources_to_remove is not None:
            self._values["resources_to_remove"] = resources_to_remove
        if status is not None:
            self._values["status"] = status
        if tags is not None:
            self._values["tags"] = tags
        if traffic_percentage_to_monitor is not None:
            self._values["traffic_percentage_to_monitor"] = traffic_percentage_to_monitor

    @builtins.property
    def monitor_name(self) -> builtins.str:
        '''The name of the monitor.

        A monitor name can contain only alphanumeric characters, dashes (-), periods (.), and underscores (_).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-internetmonitor-monitor.html#cfn-internetmonitor-monitor-monitorname
        '''
        result = self._values.get("monitor_name")
        assert result is not None, "Required property 'monitor_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def health_events_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnMonitor.HealthEventsConfigProperty]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-internetmonitor-monitor.html#cfn-internetmonitor-monitor-healtheventsconfig
        '''
        result = self._values.get("health_events_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnMonitor.HealthEventsConfigProperty]], result)

    @builtins.property
    def internet_measurements_log_delivery(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnMonitor.InternetMeasurementsLogDeliveryProperty]]:
        '''Publish internet measurements for a monitor for all city-networks (up to the 500,000 service limit) to another location, such as an Amazon S3 bucket.

        Measurements are also published to Amazon CloudWatch Logs for the first 500 (by traffic volume) city-networks (client locations and ASNs, typically internet service providers or ISPs).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-internetmonitor-monitor.html#cfn-internetmonitor-monitor-internetmeasurementslogdelivery
        '''
        result = self._values.get("internet_measurements_log_delivery")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnMonitor.InternetMeasurementsLogDeliveryProperty]], result)

    @builtins.property
    def max_city_networks_to_monitor(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of city-networks to monitor for your resources.

        A city-network is the location (city) where clients access your application resources from and the network, such as an internet service provider, that clients access the resources through.

        For more information, see `Choosing a city-network maximum value <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/IMCityNetworksMaximum.html>`_ in *Using Amazon CloudWatch Internet Monitor* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-internetmonitor-monitor.html#cfn-internetmonitor-monitor-maxcitynetworkstomonitor
        '''
        result = self._values.get("max_city_networks_to_monitor")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def resources(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The resources that have been added for the monitor, listed by their Amazon Resource Names (ARNs).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-internetmonitor-monitor.html#cfn-internetmonitor-monitor-resources
        '''
        result = self._values.get("resources")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def resources_to_add(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The resources to add to a monitor, which you provide as a set of Amazon Resource Names (ARNs).

        You can add a combination of Virtual Private Clouds (VPCs) and Amazon CloudFront distributions, or you can add Amazon WorkSpaces directories. You can't add all three types of resources.
        .. epigraph::

           If you add only VPC resources, at least one VPC must have an Internet Gateway attached to it, to make sure that it has internet connectivity.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-internetmonitor-monitor.html#cfn-internetmonitor-monitor-resourcestoadd
        '''
        result = self._values.get("resources_to_add")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def resources_to_remove(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The resources to remove from a monitor, which you provide as a set of Amazon Resource Names (ARNs).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-internetmonitor-monitor.html#cfn-internetmonitor-monitor-resourcestoremove
        '''
        result = self._values.get("resources_to_remove")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''The status of a monitor.

        The accepted values that you can specify for ``Status`` are ``ACTIVE`` and ``INACTIVE`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-internetmonitor-monitor.html#cfn-internetmonitor-monitor-status
        '''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags for a monitor, listed as a set of *key:value* pairs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-internetmonitor-monitor.html#cfn-internetmonitor-monitor-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def traffic_percentage_to_monitor(self) -> typing.Optional[jsii.Number]:
        '''The percentage of the internet-facing traffic for your application that you want to monitor.

        You can also, optionally, set a limit for the number of city-networks (client locations and ASNs, typically internet service providers) that Internet Monitor will monitor traffic for. The city-networks maximum limit caps the number of city-networks that Internet Monitor monitors for your application, regardless of the percentage of traffic that you choose to monitor.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-internetmonitor-monitor.html#cfn-internetmonitor-monitor-trafficpercentagetomonitor
        '''
        result = self._values.get("traffic_percentage_to_monitor")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMonitorProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnMonitor",
    "CfnMonitorProps",
]

publication.publish()

def _typecheckingstub__b49625d902a7236b204a8a96b68b35647ded5da14fa0241503fe8aed7ec47718(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    monitor_name: builtins.str,
    health_events_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMonitor.HealthEventsConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    internet_measurements_log_delivery: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMonitor.InternetMeasurementsLogDeliveryProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    max_city_networks_to_monitor: typing.Optional[jsii.Number] = None,
    resources: typing.Optional[typing.Sequence[builtins.str]] = None,
    resources_to_add: typing.Optional[typing.Sequence[builtins.str]] = None,
    resources_to_remove: typing.Optional[typing.Sequence[builtins.str]] = None,
    status: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    traffic_percentage_to_monitor: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9b595277fbc445515d03337a4dad34db4660278ac9bbe6f5c8b9c7ed6952d46(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c84a3dbe4ef362dc6094809148408f29e223dcdc3bde69c3aa5c6af04a3682bf(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef54ce1b63c1e0317ca73d33869cf2089b1ed66ab1da2e0c8fe45043287b6817(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1fcad87a381a34c71141a2be73ac8e81c442bd9d4616b8a8a55279c77a30bf9b(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnMonitor.HealthEventsConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__edd584d7d64cd02983ca8858b15c31728e9294c416931001fc1a9ce5732ebad9(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnMonitor.InternetMeasurementsLogDeliveryProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44b26920fe092fdfabe5783619b4c150b5a44928ea63b71966ac31bfc9220c93(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b341be6dedc5e43e3921317eb724e72355e140557e075d7a60632555b8e832c4(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6eb4096ee765fe908d059e9b8acdca0ec1f047ddb2fe5ede304ab5ee82444f95(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9387e3cfcac600ed38b66e78df668311b567c717d8143713922de9b400262882(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f131dc53d07b00ba7900326b379a6d12c142d61ae7d7045e4e4abbd87c853da1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8356cdf68080604804446d5b83fa308a2aa120e493bdc0ac24c31dbdc37894b7(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b04e25dfeda5e88ea0ba9a753d013df9fa970065f64b69b4e930f01e15363029(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba4b92afb6160c9794c6728a23a6695dc294c537ffbfec41a2e2341226207279(
    *,
    availability_score_threshold: typing.Optional[jsii.Number] = None,
    performance_score_threshold: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be81e1048b4dd2c8c398b30d3055a799662f400cb08d51222af40dc7fabaeb42(
    *,
    s3_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMonitor.S3ConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ea826525df0e7912a2b2f0156891d9d00bda155e8b35634621c6e059a1b2b4b(
    *,
    bucket_name: typing.Optional[builtins.str] = None,
    bucket_prefix: typing.Optional[builtins.str] = None,
    log_delivery_status: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a592873878a3205128bdbf7757cbce3b6e97783b1a68d0a1b5510ffc9f9f1fd8(
    *,
    monitor_name: builtins.str,
    health_events_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMonitor.HealthEventsConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    internet_measurements_log_delivery: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMonitor.InternetMeasurementsLogDeliveryProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    max_city_networks_to_monitor: typing.Optional[jsii.Number] = None,
    resources: typing.Optional[typing.Sequence[builtins.str]] = None,
    resources_to_add: typing.Optional[typing.Sequence[builtins.str]] = None,
    resources_to_remove: typing.Optional[typing.Sequence[builtins.str]] = None,
    status: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    traffic_percentage_to_monitor: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass
