'''
# AWS CloudTrail Construct Library

## Trail

AWS CloudTrail enables governance, compliance, and operational and risk auditing of your AWS account. Actions taken by
a user, role, or an AWS service are recorded as events in CloudTrail. Learn more at the [CloudTrail
documentation](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html).

The `Trail` construct enables ongoing delivery of events as log files to an Amazon S3 bucket. Learn more about [Creating
a Trail for Your AWS Account](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html).
The following code creates a simple CloudTrail for your account -

```python
trail = cloudtrail.Trail(self, "CloudTrail")
```

By default, this will create a new S3 Bucket that CloudTrail will write to, and choose a few other reasonable defaults
such as turning on multi-region and global service events.
The defaults for each property and how to override them are all documented on the `TrailProps` interface.

## Log File Validation

In order to validate that the CloudTrail log file was not modified after CloudTrail delivered it, CloudTrail provides a
digital signature for each file. Learn more at [Validating CloudTrail Log File
Integrity](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-log-file-validation-intro.html).

This is enabled on the `Trail` construct by default, but can be turned off by setting `enableFileValidation` to `false`.

```python
trail = cloudtrail.Trail(self, "CloudTrail",
    enable_file_validation=False
)
```

## Notifications

Amazon SNS notifications can be configured upon new log files containing Trail events are delivered to S3.
Learn more at [Configuring Amazon SNS Notifications for
CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.html).
The following code configures an SNS topic to be notified -

```python
topic = sns.Topic(self, "TrailTopic")
trail = cloudtrail.Trail(self, "CloudTrail",
    sns_topic=topic
)
```

## Service Integrations

Besides sending trail events to S3, they can also be configured to notify other AWS services -

### Amazon CloudWatch Logs

CloudTrail events can be delivered to a CloudWatch Logs LogGroup. By default, a new LogGroup is created with a
default retention setting. The following code enables sending CloudWatch logs but specifies a particular retention
period for the created Log Group.

```python
import aws_cdk.aws_logs as logs


trail = cloudtrail.Trail(self, "CloudTrail",
    send_to_cloud_watch_logs=True,
    cloud_watch_logs_retention=logs.RetentionDays.FOUR_MONTHS
)
```

If you would like to use a specific log group instead, this can be configured via `cloudwatchLogGroup`.

### Amazon EventBridge

Amazon EventBridge rules can be configured to be triggered when CloudTrail events occur using the `Trail.onEvent()` API.
Using APIs available in `aws-events`, these events can be filtered to match to those that are of interest, either from
a specific service, account or time range. See [Events delivered via
CloudTrail](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/EventTypes.html#events-for-services-not-listed)
to learn more about the event structure for events from CloudTrail.

The following code filters events for S3 from a specific AWS account and triggers a lambda function.

```python
my_function_handler = lambda_.Function(self, "MyFunction",
    code=lambda_.Code.from_asset("resource/myfunction"),
    runtime=lambda_.Runtime.NODEJS_LATEST,
    handler="index.handler"
)

event_rule = cloudtrail.Trail.on_event(self, "MyCloudWatchEvent",
    target=targets.LambdaFunction(my_function_handler)
)

event_rule.add_event_pattern(
    account=["123456789012"],
    source=["aws.s3"]
)
```

## Multi-Region & Global Service Events

By default, a `Trail` is configured to deliver log files from multiple regions to a single S3 bucket for a given
account. This creates shadow trails (replication of the trails) in all of the other regions. Learn more about [How
CloudTrail Behaves Regionally](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-concepts.html#cloudtrail-concepts-regional-and-global-services)
and about the [`IsMultiRegion`
property](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-ismultiregiontrail).

For most services, events are recorded in the region where the action occurred. For global services such as AWS IAM,
AWS STS, Amazon CloudFront, Route 53, etc., events are delivered to any trail that includes global services. Learn more
[About Global Service Events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-concepts.html#cloudtrail-concepts-global-service-events).

Events for global services are turned on by default for `Trail` constructs in the CDK.

The following code disables multi-region trail delivery and trail delivery for global services for a specific `Trail` -

```python
trail = cloudtrail.Trail(self, "CloudTrail",
    # ...
    is_multi_region_trail=False,
    include_global_service_events=False
)
```

## Events Types

**Management events** provide information about management operations that are performed on resources in your AWS
account. These are also known as control plane operations. Learn more about [Management
Events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-concepts.html#cloudtrail-concepts-events).

By default, a `Trail` logs all management events. However, they can be configured to either be turned off, or to only
log 'Read' or 'Write' events.

The following code configures the `Trail` to only track management events that are of type 'Read'.

```python
trail = cloudtrail.Trail(self, "CloudTrail",
    # ...
    management_events=cloudtrail.ReadWriteType.READ_ONLY
)
```

**Data events** provide information about the resource operations performed on or in a resource. These are also known
as data plane operations. Learn more about [Data
Events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-concepts.html#cloudtrail-concepts-events).
By default, no data events are logged for a `Trail`.

AWS CloudTrail supports data event logging for Amazon S3 objects and AWS Lambda functions.

The `logAllS3DataEvents()` API configures the trail to log all S3 data events while the `addS3EventSelector()` API can
be used to configure logging of S3 data events for specific buckets and specific object prefix. The following code
configures logging of S3 data events for `fooBucket` and with object prefix `bar/`.

```python
import aws_cdk.aws_s3 as s3
# bucket: s3.Bucket


trail = cloudtrail.Trail(self, "MyAmazingCloudTrail")

# Adds an event selector to the bucket foo
trail.add_s3_event_selector([
    bucket=bucket,
    object_prefix="bar/"
])
```

Similarly, the `logAllLambdaDataEvents()` configures the trail to log all Lambda data events while the
`addLambdaEventSelector()` API can be used to configure logging for specific Lambda functions. The following code
configures logging of Lambda data events for a specific Function.

```python
trail = cloudtrail.Trail(self, "MyAmazingCloudTrail")
amazing_function = lambda_.Function(self, "AnAmazingFunction",
    runtime=lambda_.Runtime.NODEJS_LATEST,
    handler="hello.handler",
    code=lambda_.Code.from_asset("lambda")
)

# Add an event selector to log data events for the provided Lambda functions.
trail.add_lambda_event_selector([amazing_function])
```

## Organization Trail

It is possible to create a trail that will be applied to all accounts in an organization if the current account manages an organization.
To enable this, the property `isOrganizationTrail` must be set. If this property is set and the current account does not manage an organization, the stack will fail to deploy.

```python
cloudtrail.Trail(self, "OrganizationTrail",
    is_organization_trail=True
)
```

## CloudTrail Insights

Set `InsightSelector` to enable Insight.
Insights selector values can be `ApiCallRateInsight`, `ApiErrorRateInsight`, or both.

```python
cloudtrail.Trail(self, "Insights",
    insight_types=[cloudtrail.InsightType.API_CALL_RATE, cloudtrail.InsightType.API_ERROR_RATE
    ]
)
```
'''
from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)

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
    Resource as _Resource_45bc6135,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)
from ..aws_events import (
    EventPattern as _EventPattern_fe557901,
    IRuleTarget as _IRuleTarget_7a91f454,
    OnEventOptions as _OnEventOptions_8711b8b3,
    Rule as _Rule_334ed2b5,
)
from ..aws_kms import IKey as _IKey_5f11635f
from ..aws_lambda import IFunction as _IFunction_6adb0ab8
from ..aws_logs import (
    ILogGroup as _ILogGroup_3c4fa718, RetentionDays as _RetentionDays_070f99f0
)
from ..aws_s3 import IBucket as _IBucket_42e086fd
from ..aws_sns import ITopic as _ITopic_9eca4852


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudtrail.AddEventSelectorOptions",
    jsii_struct_bases=[],
    name_mapping={
        "exclude_management_event_sources": "excludeManagementEventSources",
        "include_management_events": "includeManagementEvents",
        "read_write_type": "readWriteType",
    },
)
class AddEventSelectorOptions:
    def __init__(
        self,
        *,
        exclude_management_event_sources: typing.Optional[typing.Sequence["ManagementEventSources"]] = None,
        include_management_events: typing.Optional[builtins.bool] = None,
        read_write_type: typing.Optional["ReadWriteType"] = None,
    ) -> None:
        '''Options for adding an event selector.

        :param exclude_management_event_sources: An optional list of service event sources from which you do not want management events to be logged on your trail. Default: []
        :param include_management_events: Specifies whether the event selector includes management events for the trail. Default: true
        :param read_write_type: Specifies whether to log read-only events, write-only events, or all events. Default: ReadWriteType.All

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_cloudtrail as cloudtrail
            
            # source_bucket: s3.Bucket
            
            source_output = codepipeline.Artifact()
            key = "some/key.zip"
            trail = cloudtrail.Trail(self, "CloudTrail")
            trail.add_s3_event_selector([cloudtrail.S3EventSelector(
                bucket=source_bucket,
                object_prefix=key
            )],
                read_write_type=cloudtrail.ReadWriteType.WRITE_ONLY
            )
            source_action = codepipeline_actions.S3SourceAction(
                action_name="S3Source",
                bucket_key=key,
                bucket=source_bucket,
                output=source_output,
                trigger=codepipeline_actions.S3Trigger.EVENTS
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73fc595c7387ed1256397f5af21fd7ee999ae00a4ffd0d01a01810f05f0a7ae5)
            check_type(argname="argument exclude_management_event_sources", value=exclude_management_event_sources, expected_type=type_hints["exclude_management_event_sources"])
            check_type(argname="argument include_management_events", value=include_management_events, expected_type=type_hints["include_management_events"])
            check_type(argname="argument read_write_type", value=read_write_type, expected_type=type_hints["read_write_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if exclude_management_event_sources is not None:
            self._values["exclude_management_event_sources"] = exclude_management_event_sources
        if include_management_events is not None:
            self._values["include_management_events"] = include_management_events
        if read_write_type is not None:
            self._values["read_write_type"] = read_write_type

    @builtins.property
    def exclude_management_event_sources(
        self,
    ) -> typing.Optional[typing.List["ManagementEventSources"]]:
        '''An optional list of service event sources from which you do not want management events to be logged on your trail.

        :default: []
        '''
        result = self._values.get("exclude_management_event_sources")
        return typing.cast(typing.Optional[typing.List["ManagementEventSources"]], result)

    @builtins.property
    def include_management_events(self) -> typing.Optional[builtins.bool]:
        '''Specifies whether the event selector includes management events for the trail.

        :default: true
        '''
        result = self._values.get("include_management_events")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def read_write_type(self) -> typing.Optional["ReadWriteType"]:
        '''Specifies whether to log read-only events, write-only events, or all events.

        :default: ReadWriteType.All
        '''
        result = self._values.get("read_write_type")
        return typing.cast(typing.Optional["ReadWriteType"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AddEventSelectorOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnChannel(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudtrail.CfnChannel",
):
    '''Contains information about a returned CloudTrail channel.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-channel.html
    :cloudformationResource: AWS::CloudTrail::Channel
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_cloudtrail as cloudtrail
        
        cfn_channel = cloudtrail.CfnChannel(self, "MyCfnChannel",
            destinations=[cloudtrail.CfnChannel.DestinationProperty(
                location="location",
                type="type"
            )],
            name="name",
            source="source",
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
        destinations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnChannel.DestinationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        name: typing.Optional[builtins.str] = None,
        source: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param destinations: One or more event data stores to which events arriving through a channel will be logged.
        :param name: The name of the channel.
        :param source: The name of the partner or external event source. You cannot change this name after you create the channel. A maximum of one channel is allowed per source. A source can be either ``Custom`` for all valid non- AWS events, or the name of a partner event source. For information about the source names for available partners, see `Additional information about integration partners <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-event-data-store-integration.html#cloudtrail-lake-partner-information>`_ in the CloudTrail User Guide.
        :param tags: A list of tags.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4004ebed14c16ae6f20ecf5d65ea8487ea49b0bd7c3ce35ca361518f9fec0fa6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnChannelProps(
            destinations=destinations, name=name, source=source, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12052607593ad96dcef135d212789e6caf3b7f7cd49c9ce2468646f9efbcb963)
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
            type_hints = typing.get_type_hints(_typecheckingstub__cd31f5742125109282b44493267cb4e1405b919ba97bb1b7f18668a0624611e2)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrChannelArn")
    def attr_channel_arn(self) -> builtins.str:
        '''``Ref`` returns the ARN of the CloudTrail channel, such as ``arn:aws:cloudtrail:us-east-2:123456789012:channel/01234567890`` .

        :cloudformationAttribute: ChannelArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrChannelArn"))

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
    @jsii.member(jsii_name="destinations")
    def destinations(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnChannel.DestinationProperty"]]]]:
        '''One or more event data stores to which events arriving through a channel will be logged.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnChannel.DestinationProperty"]]]], jsii.get(self, "destinations"))

    @destinations.setter
    def destinations(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnChannel.DestinationProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af90446cbf2dae59bef52fb3ee6ec0e5b9c6098eff5af75a5963dd51c4683a5e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinations", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the channel.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f6f560b40b7326691d9bf63d6ea7b8ad77377af3911f812fa5d243141752b34)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(self) -> typing.Optional[builtins.str]:
        '''The name of the partner or external event source.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "source"))

    @source.setter
    def source(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63777c16355eca1495edc2932fdadb55a7e3c86d73124f1d93d1c28b2ad64ee7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "source", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of tags.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29044cfd0c28f00acd85e04beb454a19a2c4d87d4786f0af019f0209c639da8b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cloudtrail.CfnChannel.DestinationProperty",
        jsii_struct_bases=[],
        name_mapping={"location": "location", "type": "type"},
    )
    class DestinationProperty:
        def __init__(self, *, location: builtins.str, type: builtins.str) -> None:
            '''Contains information about the destination receiving events.

            :param location: For channels used for a CloudTrail Lake integration, the location is the ARN of an event data store that receives events from a channel. For service-linked channels, the location is the name of the AWS service.
            :param type: The type of destination for events arriving from a channel. For channels used for a CloudTrail Lake integration, the value is ``EVENT_DATA_STORE`` . For service-linked channels, the value is ``AWS_SERVICE`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-channel-destination.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cloudtrail as cloudtrail
                
                destination_property = cloudtrail.CfnChannel.DestinationProperty(
                    location="location",
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__619b701f7c6b5470537230c8a847919a410a57fbf2eab022694dc1fef7b41c92)
                check_type(argname="argument location", value=location, expected_type=type_hints["location"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "location": location,
                "type": type,
            }

        @builtins.property
        def location(self) -> builtins.str:
            '''For channels used for a CloudTrail Lake integration, the location is the ARN of an event data store that receives events from a channel.

            For service-linked channels, the location is the name of the AWS service.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-channel-destination.html#cfn-cloudtrail-channel-destination-location
            '''
            result = self._values.get("location")
            assert result is not None, "Required property 'location' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def type(self) -> builtins.str:
            '''The type of destination for events arriving from a channel.

            For channels used for a CloudTrail Lake integration, the value is ``EVENT_DATA_STORE`` . For service-linked channels, the value is ``AWS_SERVICE`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-channel-destination.html#cfn-cloudtrail-channel-destination-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudtrail.CfnChannelProps",
    jsii_struct_bases=[],
    name_mapping={
        "destinations": "destinations",
        "name": "name",
        "source": "source",
        "tags": "tags",
    },
)
class CfnChannelProps:
    def __init__(
        self,
        *,
        destinations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnChannel.DestinationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        name: typing.Optional[builtins.str] = None,
        source: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnChannel``.

        :param destinations: One or more event data stores to which events arriving through a channel will be logged.
        :param name: The name of the channel.
        :param source: The name of the partner or external event source. You cannot change this name after you create the channel. A maximum of one channel is allowed per source. A source can be either ``Custom`` for all valid non- AWS events, or the name of a partner event source. For information about the source names for available partners, see `Additional information about integration partners <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-event-data-store-integration.html#cloudtrail-lake-partner-information>`_ in the CloudTrail User Guide.
        :param tags: A list of tags.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-channel.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cloudtrail as cloudtrail
            
            cfn_channel_props = cloudtrail.CfnChannelProps(
                destinations=[cloudtrail.CfnChannel.DestinationProperty(
                    location="location",
                    type="type"
                )],
                name="name",
                source="source",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__767e83e8a394410f21e7f497da1effaf3ef0c04f6e829362db73a8f535dd5356)
            check_type(argname="argument destinations", value=destinations, expected_type=type_hints["destinations"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if destinations is not None:
            self._values["destinations"] = destinations
        if name is not None:
            self._values["name"] = name
        if source is not None:
            self._values["source"] = source
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def destinations(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnChannel.DestinationProperty]]]]:
        '''One or more event data stores to which events arriving through a channel will be logged.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-channel.html#cfn-cloudtrail-channel-destinations
        '''
        result = self._values.get("destinations")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnChannel.DestinationProperty]]]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the channel.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-channel.html#cfn-cloudtrail-channel-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source(self) -> typing.Optional[builtins.str]:
        '''The name of the partner or external event source.

        You cannot change this name after you create the channel. A maximum of one channel is allowed per source.

        A source can be either ``Custom`` for all valid non- AWS events, or the name of a partner event source. For information about the source names for available partners, see `Additional information about integration partners <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-event-data-store-integration.html#cloudtrail-lake-partner-information>`_ in the CloudTrail User Guide.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-channel.html#cfn-cloudtrail-channel-source
        '''
        result = self._values.get("source")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of tags.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-channel.html#cfn-cloudtrail-channel-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnChannelProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnEventDataStore(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudtrail.CfnEventDataStore",
):
    '''Creates a new event data store.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-eventdatastore.html
    :cloudformationResource: AWS::CloudTrail::EventDataStore
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_cloudtrail as cloudtrail
        
        cfn_event_data_store = cloudtrail.CfnEventDataStore(self, "MyCfnEventDataStore",
            advanced_event_selectors=[cloudtrail.CfnEventDataStore.AdvancedEventSelectorProperty(
                field_selectors=[cloudtrail.CfnEventDataStore.AdvancedFieldSelectorProperty(
                    field="field",
        
                    # the properties below are optional
                    ends_with=["endsWith"],
                    equal_to=["equalTo"],
                    not_ends_with=["notEndsWith"],
                    not_equals=["notEquals"],
                    not_starts_with=["notStartsWith"],
                    starts_with=["startsWith"]
                )],
        
                # the properties below are optional
                name="name"
            )],
            billing_mode="billingMode",
            federation_enabled=False,
            federation_role_arn="federationRoleArn",
            ingestion_enabled=False,
            insights_destination="insightsDestination",
            insight_selectors=[cloudtrail.CfnEventDataStore.InsightSelectorProperty(
                insight_type="insightType"
            )],
            kms_key_id="kmsKeyId",
            multi_region_enabled=False,
            name="name",
            organization_enabled=False,
            retention_period=123,
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            termination_protection_enabled=False
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        advanced_event_selectors: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEventDataStore.AdvancedEventSelectorProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        billing_mode: typing.Optional[builtins.str] = None,
        federation_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        federation_role_arn: typing.Optional[builtins.str] = None,
        ingestion_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        insights_destination: typing.Optional[builtins.str] = None,
        insight_selectors: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEventDataStore.InsightSelectorProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        multi_region_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        name: typing.Optional[builtins.str] = None,
        organization_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        retention_period: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        termination_protection_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param advanced_event_selectors: The advanced event selectors to use to select the events for the data store. You can configure up to five advanced event selectors for each event data store. For more information about how to use advanced event selectors to log CloudTrail events, see `Log events by using advanced event selectors <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html#creating-data-event-selectors-advanced>`_ in the CloudTrail User Guide. For more information about how to use advanced event selectors to include AWS Config configuration items in your event data store, see `Create an event data store for AWS Config configuration items <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/lake-eds-cli.html#lake-cli-create-eds-config>`_ in the CloudTrail User Guide. For more information about how to use advanced event selectors to include events outside of AWS events in your event data store, see `Create an integration to log events from outside AWS <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/lake-integrations-cli.html#lake-cli-create-integration>`_ in the CloudTrail User Guide.
        :param billing_mode: The billing mode for the event data store determines the cost for ingesting events and the default and maximum retention period for the event data store. The following are the possible values: - ``EXTENDABLE_RETENTION_PRICING`` - This billing mode is generally recommended if you want a flexible retention period of up to 3653 days (about 10 years). The default retention period for this billing mode is 366 days. - ``FIXED_RETENTION_PRICING`` - This billing mode is recommended if you expect to ingest more than 25 TB of event data per month and need a retention period of up to 2557 days (about 7 years). The default retention period for this billing mode is 2557 days. The default value is ``EXTENDABLE_RETENTION_PRICING`` . For more information about CloudTrail pricing, see `AWS CloudTrail Pricing <https://docs.aws.amazon.com/cloudtrail/pricing/>`_ and `Managing CloudTrail Lake costs <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake-manage-costs.html>`_ .
        :param federation_enabled: Indicates if `Lake query federation <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-federation.html>`_ is enabled. By default, Lake query federation is disabled. You cannot delete an event data store if Lake query federation is enabled.
        :param federation_role_arn: If Lake query federation is enabled, provides the ARN of the federation role used to access the resources for the federated event data store. The federation role must exist in your account and provide the `required minimum permissions <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-federation.html#query-federation-permissions-role>`_ .
        :param ingestion_enabled: Specifies whether the event data store should start ingesting live events. The default is true.
        :param insights_destination: The ARN (or ID suffix of the ARN) of the destination event data store that logs Insights events. For more information, see `Create an event data store for CloudTrail Insights events <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-event-data-store-insights.html>`_ .
        :param insight_selectors: A JSON string that contains the Insights types you want to log on an event data store. ``ApiCallRateInsight`` and ``ApiErrorRateInsight`` are valid Insight types. The ``ApiCallRateInsight`` Insights type analyzes write-only management API calls that are aggregated per minute against a baseline API call volume. The ``ApiErrorRateInsight`` Insights type analyzes management API calls that result in error codes. The error is shown if the API call is unsuccessful.
        :param kms_key_id: Specifies the AWS KMS key ID to use to encrypt the events delivered by CloudTrail. The value can be an alias name prefixed by ``alias/`` , a fully specified ARN to an alias, a fully specified ARN to a key, or a globally unique identifier. .. epigraph:: Disabling or deleting the KMS key, or removing CloudTrail permissions on the key, prevents CloudTrail from logging events to the event data store, and prevents users from querying the data in the event data store that was encrypted with the key. After you associate an event data store with a KMS key, the KMS key cannot be removed or changed. Before you disable or delete a KMS key that you are using with an event data store, delete or back up your event data store. CloudTrail also supports AWS KMS multi-Region keys. For more information about multi-Region keys, see `Using multi-Region keys <https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html>`_ in the *AWS Key Management Service Developer Guide* . Examples: - ``alias/MyAliasName`` - ``arn:aws:kms:us-east-2:123456789012:alias/MyAliasName`` - ``arn:aws:kms:us-east-2:123456789012:key/12345678-1234-1234-1234-123456789012`` - ``12345678-1234-1234-1234-123456789012``
        :param multi_region_enabled: Specifies whether the event data store includes events from all Regions, or only from the Region in which the event data store is created.
        :param name: The name of the event data store.
        :param organization_enabled: Specifies whether an event data store collects events logged for an organization in AWS Organizations .
        :param retention_period: The retention period of the event data store, in days. If ``BillingMode`` is set to ``EXTENDABLE_RETENTION_PRICING`` , you can set a retention period of up to 3653 days, the equivalent of 10 years. If ``BillingMode`` is set to ``FIXED_RETENTION_PRICING`` , you can set a retention period of up to 2557 days, the equivalent of seven years. CloudTrail Lake determines whether to retain an event by checking if the ``eventTime`` of the event is within the specified retention period. For example, if you set a retention period of 90 days, CloudTrail will remove events when the ``eventTime`` is older than 90 days. .. epigraph:: If you plan to copy trail events to this event data store, we recommend that you consider both the age of the events that you want to copy as well as how long you want to keep the copied events in your event data store. For example, if you copy trail events that are 5 years old and specify a retention period of 7 years, the event data store will retain those events for two years.
        :param tags: A list of tags.
        :param termination_protection_enabled: Specifies whether termination protection is enabled for the event data store. If termination protection is enabled, you cannot delete the event data store until termination protection is disabled.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__058a94222b13ad44b4607ad5932ec9b6a2defcb250ff436576e6e8976e7b2bee)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnEventDataStoreProps(
            advanced_event_selectors=advanced_event_selectors,
            billing_mode=billing_mode,
            federation_enabled=federation_enabled,
            federation_role_arn=federation_role_arn,
            ingestion_enabled=ingestion_enabled,
            insights_destination=insights_destination,
            insight_selectors=insight_selectors,
            kms_key_id=kms_key_id,
            multi_region_enabled=multi_region_enabled,
            name=name,
            organization_enabled=organization_enabled,
            retention_period=retention_period,
            tags=tags,
            termination_protection_enabled=termination_protection_enabled,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21862a9cccdc40ba09d15f004dcda554d20814b630b70c51ae59a1212bbb14c4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2ee95efcc007233c035a77dfd382e47456926b86a000891448961781bff2a95e)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedTimestamp")
    def attr_created_timestamp(self) -> builtins.str:
        '''``Ref`` returns the time stamp of the creation of the event data store, such as ``1248496624`` .

        :cloudformationAttribute: CreatedTimestamp
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedTimestamp"))

    @builtins.property
    @jsii.member(jsii_name="attrEventDataStoreArn")
    def attr_event_data_store_arn(self) -> builtins.str:
        '''``Ref`` returns the ARN of the CloudTrail event data store, such as ``arn:aws:cloudtrail:us-east-1:12345678910:eventdatastore/EXAMPLE-f852-4e8f-8bd1-bcf6cEXAMPLE`` .

        :cloudformationAttribute: EventDataStoreArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEventDataStoreArn"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''``Ref`` returns the status of the event data store, such as ``ENABLED`` .

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdatedTimestamp")
    def attr_updated_timestamp(self) -> builtins.str:
        '''``Ref`` returns the time stamp that updates were made to an event data store, such as ``1598296624`` .

        :cloudformationAttribute: UpdatedTimestamp
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdatedTimestamp"))

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
    @jsii.member(jsii_name="advancedEventSelectors")
    def advanced_event_selectors(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEventDataStore.AdvancedEventSelectorProperty"]]]]:
        '''The advanced event selectors to use to select the events for the data store.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEventDataStore.AdvancedEventSelectorProperty"]]]], jsii.get(self, "advancedEventSelectors"))

    @advanced_event_selectors.setter
    def advanced_event_selectors(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEventDataStore.AdvancedEventSelectorProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7bc51d9a1ef5affc48ffb624785b29a7a5d0a3eba5e72b94f687da94194f4973)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "advancedEventSelectors", value)

    @builtins.property
    @jsii.member(jsii_name="billingMode")
    def billing_mode(self) -> typing.Optional[builtins.str]:
        '''The billing mode for the event data store determines the cost for ingesting events and the default and maximum retention period for the event data store.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "billingMode"))

    @billing_mode.setter
    def billing_mode(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__106939491635761bff083d6af3ca26d1723f9df71ec433399c5746554b88e334)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "billingMode", value)

    @builtins.property
    @jsii.member(jsii_name="federationEnabled")
    def federation_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Indicates if `Lake query federation <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-federation.html>`_ is enabled. By default, Lake query federation is disabled. You cannot delete an event data store if Lake query federation is enabled.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "federationEnabled"))

    @federation_enabled.setter
    def federation_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__765513d5a073b76962f766e5dc1a967c4ad42a5bb2200d9f880aac945789b35d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "federationEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="federationRoleArn")
    def federation_role_arn(self) -> typing.Optional[builtins.str]:
        '''If Lake query federation is enabled, provides the ARN of the federation role used to access the resources for the federated event data store.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "federationRoleArn"))

    @federation_role_arn.setter
    def federation_role_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02d5876fb281f125b4a84c7554b6ae992b9b7433cab839d402d60601a9872704)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "federationRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="ingestionEnabled")
    def ingestion_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether the event data store should start ingesting live events.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "ingestionEnabled"))

    @ingestion_enabled.setter
    def ingestion_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3120b4fc57c151f577843e6f55242684964162de4d4061991c82480a0fae581b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ingestionEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="insightsDestination")
    def insights_destination(self) -> typing.Optional[builtins.str]:
        '''The ARN (or ID suffix of the ARN) of the destination event data store that logs Insights events.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "insightsDestination"))

    @insights_destination.setter
    def insights_destination(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d10aa59d5d60b5a68edf57d8df52934e03f5e4f0802a1d7dab4552592f2ee609)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "insightsDestination", value)

    @builtins.property
    @jsii.member(jsii_name="insightSelectors")
    def insight_selectors(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEventDataStore.InsightSelectorProperty"]]]]:
        '''A JSON string that contains the Insights types you want to log on an event data store.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEventDataStore.InsightSelectorProperty"]]]], jsii.get(self, "insightSelectors"))

    @insight_selectors.setter
    def insight_selectors(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEventDataStore.InsightSelectorProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b360ff34d6b267287ccf6e4c636b401ab6c739c7a90856639462b1c738855c92)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "insightSelectors", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Specifies the AWS KMS key ID to use to encrypt the events delivered by CloudTrail.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2945b7a3d4af202bf1a8d8550ce4b17a1ab219e4dd829832fc9bd51a53c69b0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="multiRegionEnabled")
    def multi_region_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether the event data store includes events from all Regions, or only from the Region in which the event data store is created.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "multiRegionEnabled"))

    @multi_region_enabled.setter
    def multi_region_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__69742230d7479a5e2d180046d6dbe2ea4627b1fbe6861d248e8fa77f7c0dcd20)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "multiRegionEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the event data store.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a01c2b1ec1e4ebac8e9e92744ee1402309ee4033c2267e1089f605b125f4b192)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="organizationEnabled")
    def organization_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether an event data store collects events logged for an organization in AWS Organizations .'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "organizationEnabled"))

    @organization_enabled.setter
    def organization_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__565712bf828bb8c2b0f6a80ca025d431aa72043d60fff9a95e02336f6f1e0d1c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "organizationEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="retentionPeriod")
    def retention_period(self) -> typing.Optional[jsii.Number]:
        '''The retention period of the event data store, in days.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retentionPeriod"))

    @retention_period.setter
    def retention_period(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9508e34267838b75568905c8769ff7999130a13cb85b3d1abf67ef17b5958102)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retentionPeriod", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of tags.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6acb86a62af0621d981781f78b5611035089e25ca1472411f75d1b6e352ead2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="terminationProtectionEnabled")
    def termination_protection_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether termination protection is enabled for the event data store.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "terminationProtectionEnabled"))

    @termination_protection_enabled.setter
    def termination_protection_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f57ea7bcecd4a4cd58674384395db2bcf2721c3bcfa216c86922651a268041e5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terminationProtectionEnabled", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cloudtrail.CfnEventDataStore.AdvancedEventSelectorProperty",
        jsii_struct_bases=[],
        name_mapping={"field_selectors": "fieldSelectors", "name": "name"},
    )
    class AdvancedEventSelectorProperty:
        def __init__(
            self,
            *,
            field_selectors: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEventDataStore.AdvancedFieldSelectorProperty", typing.Dict[builtins.str, typing.Any]]]]],
            name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Advanced event selectors let you create fine-grained selectors for CloudTrail management and data events.

            They help you control costs by logging only those events that are important to you. For more information about advanced event selectors, see `Logging management events <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.html>`_ and `Logging data events <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html>`_ in the *AWS CloudTrail User Guide* .

            You cannot apply both event selectors and advanced event selectors to a trail.

            *Supported CloudTrail event record fields for management events*

            - ``eventCategory`` (required)
            - ``eventSource``
            - ``readOnly``

            *Supported CloudTrail event record fields for data events*

            - ``eventCategory`` (required)
            - ``resources.type`` (required)
            - ``readOnly``
            - ``eventName``
            - ``resources.ARN``

            .. epigraph::

               For event data stores for CloudTrail Insights events, AWS Config configuration items, Audit Manager evidence, or events outside of AWS , the only supported field is ``eventCategory`` .

            :param field_selectors: Contains all selector statements in an advanced event selector.
            :param name: An optional, descriptive name for an advanced event selector, such as "Log data events for only two S3 buckets".

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-eventdatastore-advancedeventselector.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cloudtrail as cloudtrail
                
                advanced_event_selector_property = cloudtrail.CfnEventDataStore.AdvancedEventSelectorProperty(
                    field_selectors=[cloudtrail.CfnEventDataStore.AdvancedFieldSelectorProperty(
                        field="field",
                
                        # the properties below are optional
                        ends_with=["endsWith"],
                        equal_to=["equalTo"],
                        not_ends_with=["notEndsWith"],
                        not_equals=["notEquals"],
                        not_starts_with=["notStartsWith"],
                        starts_with=["startsWith"]
                    )],
                
                    # the properties below are optional
                    name="name"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__40ce53f73864cb5c89f3baf13c64dba67cc42e274565b6c52a84904f6fd5f4b3)
                check_type(argname="argument field_selectors", value=field_selectors, expected_type=type_hints["field_selectors"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "field_selectors": field_selectors,
            }
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def field_selectors(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEventDataStore.AdvancedFieldSelectorProperty"]]]:
            '''Contains all selector statements in an advanced event selector.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-eventdatastore-advancedeventselector.html#cfn-cloudtrail-eventdatastore-advancedeventselector-fieldselectors
            '''
            result = self._values.get("field_selectors")
            assert result is not None, "Required property 'field_selectors' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEventDataStore.AdvancedFieldSelectorProperty"]]], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''An optional, descriptive name for an advanced event selector, such as "Log data events for only two S3 buckets".

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-eventdatastore-advancedeventselector.html#cfn-cloudtrail-eventdatastore-advancedeventselector-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AdvancedEventSelectorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cloudtrail.CfnEventDataStore.AdvancedFieldSelectorProperty",
        jsii_struct_bases=[],
        name_mapping={
            "field": "field",
            "ends_with": "endsWith",
            "equal_to": "equalTo",
            "not_ends_with": "notEndsWith",
            "not_equals": "notEquals",
            "not_starts_with": "notStartsWith",
            "starts_with": "startsWith",
        },
    )
    class AdvancedFieldSelectorProperty:
        def __init__(
            self,
            *,
            field: builtins.str,
            ends_with: typing.Optional[typing.Sequence[builtins.str]] = None,
            equal_to: typing.Optional[typing.Sequence[builtins.str]] = None,
            not_ends_with: typing.Optional[typing.Sequence[builtins.str]] = None,
            not_equals: typing.Optional[typing.Sequence[builtins.str]] = None,
            not_starts_with: typing.Optional[typing.Sequence[builtins.str]] = None,
            starts_with: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''A single selector statement in an advanced event selector.

            :param field: A field in a CloudTrail event record on which to filter events to be logged. For event data stores for CloudTrail Insights events, AWS Config configuration items, Audit Manager evidence, or events outside of AWS , the field is used only for selecting events as filtering is not supported. For CloudTrail management events, supported fields include ``readOnly`` , ``eventCategory`` , and ``eventSource`` . For CloudTrail data events, supported fields include ``readOnly`` , ``eventCategory`` , ``eventName`` , ``resources.type`` , and ``resources.ARN`` . For event data stores for CloudTrail Insights events, AWS Config configuration items, Audit Manager evidence, or events outside of AWS , the only supported field is ``eventCategory`` . - *``readOnly``* - Optional. Can be set to ``Equals`` a value of ``true`` or ``false`` . If you do not add this field, CloudTrail logs both ``read`` and ``write`` events. A value of ``true`` logs only ``read`` events. A value of ``false`` logs only ``write`` events. - *``eventSource``* - For filtering management events only. This can be set to ``NotEquals`` ``kms.amazonaws.com`` or ``NotEquals`` ``rdsdata.amazonaws.com`` . - *``eventName``* - Can use any operator. You can use it to ﬁlter in or ﬁlter out any data event logged to CloudTrail, such as ``PutBucket`` or ``GetSnapshotBlock`` . You can have multiple values for this ﬁeld, separated by commas. - *``eventCategory``* - This is required and must be set to ``Equals`` . - For CloudTrail management events, the value must be ``Management`` . - For CloudTrail data events, the value must be ``Data`` . The following are used only for event data stores: - For CloudTrail Insights events, the value must be ``Insight`` . - For AWS Config configuration items, the value must be ``ConfigurationItem`` . - For Audit Manager evidence, the value must be ``Evidence`` . - For non- AWS events, the value must be ``ActivityAuditLog`` . - *``resources.type``* - This ﬁeld is required for CloudTrail data events. ``resources.type`` can only use the ``Equals`` operator, and the value can be one of the following: - ``AWS::DynamoDB::Table`` - ``AWS::Lambda::Function`` - ``AWS::S3::Object`` - ``AWS::AppConfig::Configuration`` - ``AWS::B2BI::Transformer`` - ``AWS::Bedrock::AgentAlias`` - ``AWS::Bedrock::KnowledgeBase`` - ``AWS::Cassandra::Table`` - ``AWS::CloudFront::KeyValueStore`` - ``AWS::CloudTrail::Channel`` - ``AWS::CodeWhisperer::Customization`` - ``AWS::CodeWhisperer::Profile`` - ``AWS::Cognito::IdentityPool`` - ``AWS::DynamoDB::Stream`` - ``AWS::EC2::Snapshot`` - ``AWS::EMRWAL::Workspace`` - ``AWS::FinSpace::Environment`` - ``AWS::Glue::Table`` - ``AWS::GreengrassV2::ComponentVersion`` - ``AWS::GreengrassV2::Deployment`` - ``AWS::GuardDuty::Detector`` - ``AWS::IoT::Certificate`` - ``AWS::IoT::Thing`` - ``AWS::IoTSiteWise::Asset`` - ``AWS::IoTSiteWise::TimeSeries`` - ``AWS::IoTTwinMaker::Entity`` - ``AWS::IoTTwinMaker::Workspace`` - ``AWS::KendraRanking::ExecutionPlan`` - ``AWS::KinesisVideo::Stream`` - ``AWS::ManagedBlockchain::Network`` - ``AWS::ManagedBlockchain::Node`` - ``AWS::MedicalImaging::Datastore`` - ``AWS::NeptuneGraph::Graph`` - ``AWS::PCAConnectorAD::Connector`` - ``AWS::QApps:QApp`` - ``AWS::QBusiness::Application`` - ``AWS::QBusiness::DataSource`` - ``AWS::QBusiness::Index`` - ``AWS::QBusiness::WebExperience`` - ``AWS::RDS::DBCluster`` - ``AWS::S3::AccessPoint`` - ``AWS::S3ObjectLambda::AccessPoint`` - ``AWS::S3Outposts::Object`` - ``AWS::SageMaker::Endpoint`` - ``AWS::SageMaker::ExperimentTrialComponent`` - ``AWS::SageMaker::FeatureGroup`` - ``AWS::ServiceDiscovery::Namespace`` - ``AWS::ServiceDiscovery::Service`` - ``AWS::SCN::Instance`` - ``AWS::SNS::PlatformEndpoint`` - ``AWS::SNS::Topic`` - ``AWS::SQS::Queue`` - ``AWS::SSM::ManagedNode`` - ``AWS::SSMMessages::ControlChannel`` - ``AWS::SWF::Domain`` - ``AWS::ThinClient::Device`` - ``AWS::ThinClient::Environment`` - ``AWS::Timestream::Database`` - ``AWS::Timestream::Table`` - ``AWS::VerifiedPermissions::PolicyStore`` - ``AWS::XRay::Trace`` You can have only one ``resources.type`` ﬁeld per selector. To log data events on more than one resource type, add another selector. - *``resources.ARN``* - You can use any operator with ``resources.ARN`` , but if you use ``Equals`` or ``NotEquals`` , the value must exactly match the ARN of a valid resource of the type you've speciﬁed in the template as the value of resources.type. .. epigraph:: You can't use the ``resources.ARN`` field to filter resource types that do not have ARNs. The ``resources.ARN`` field can be set one of the following. If resources.type equals ``AWS::S3::Object`` , the ARN must be in one of the following formats. To log all data events for all objects in a specific S3 bucket, use the ``StartsWith`` operator, and include only the bucket ARN as the matching value. The trailing slash is intentional; do not exclude it. Replace the text between less than and greater than symbols (<>) with resource-specific information. - ``arn:<partition>:s3:::<bucket_name>/`` - ``arn:<partition>:s3:::<bucket_name>/<object_path>/`` When resources.type equals ``AWS::DynamoDB::Table`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:dynamodb:<region>:<account_ID>:table/<table_name>`` When resources.type equals ``AWS::Lambda::Function`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:lambda:<region>:<account_ID>:function:<function_name>`` When resources.type equals ``AWS::AppConfig::Configuration`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:appconfig:<region>:<account_ID>:application/<application_ID>/environment/<environment_ID>/configuration/<configuration_profile_ID>`` When resources.type equals ``AWS::B2BI::Transformer`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:b2bi:<region>:<account_ID>:transformer/<transformer_ID>`` When resources.type equals ``AWS::Bedrock::AgentAlias`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:bedrock:<region>:<account_ID>:agent-alias/<agent_ID>/<alias_ID>`` When resources.type equals ``AWS::Bedrock::KnowledgeBase`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:bedrock:<region>:<account_ID>:knowledge-base/<knowledge_base_ID>`` When resources.type equals ``AWS::Cassandra::Table`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:cassandra:<region>:<account_ID>:/keyspace/<keyspace_name>/table/<table_name>`` When resources.type equals ``AWS::CloudFront::KeyValueStore`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:cloudfront:<region>:<account_ID>:key-value-store/<KVS_name>`` When resources.type equals ``AWS::CloudTrail::Channel`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:cloudtrail:<region>:<account_ID>:channel/<channel_UUID>`` When resources.type equals ``AWS::CodeWhisperer::Customization`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:codewhisperer:<region>:<account_ID>:customization/<customization_ID>`` When resources.type equals ``AWS::CodeWhisperer::Profile`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:codewhisperer:<region>:<account_ID>:profile/<profile_ID>`` When resources.type equals ``AWS::Cognito::IdentityPool`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:cognito-identity:<region>:<account_ID>:identitypool/<identity_pool_ID>`` When ``resources.type`` equals ``AWS::DynamoDB::Stream`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:dynamodb:<region>:<account_ID>:table/<table_name>/stream/<date_time>`` When ``resources.type`` equals ``AWS::EC2::Snapshot`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:ec2:<region>::snapshot/<snapshot_ID>`` When ``resources.type`` equals ``AWS::EMRWAL::Workspace`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:emrwal:<region>:<account_ID>:workspace/<workspace_name>`` When ``resources.type`` equals ``AWS::FinSpace::Environment`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:finspace:<region>:<account_ID>:environment/<environment_ID>`` When ``resources.type`` equals ``AWS::Glue::Table`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:glue:<region>:<account_ID>:table/<database_name>/<table_name>`` When ``resources.type`` equals ``AWS::GreengrassV2::ComponentVersion`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:greengrass:<region>:<account_ID>:components/<component_name>`` When ``resources.type`` equals ``AWS::GreengrassV2::Deployment`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:greengrass:<region>:<account_ID>:deployments/<deployment_ID`` When ``resources.type`` equals ``AWS::GuardDuty::Detector`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:guardduty:<region>:<account_ID>:detector/<detector_ID>`` When ``resources.type`` equals ``AWS::IoT::Certificate`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:iot:<region>:<account_ID>:cert/<certificate_ID>`` When ``resources.type`` equals ``AWS::IoT::Thing`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:iot:<region>:<account_ID>:thing/<thing_ID>`` When ``resources.type`` equals ``AWS::IoTSiteWise::Asset`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:iotsitewise:<region>:<account_ID>:asset/<asset_ID>`` When ``resources.type`` equals ``AWS::IoTSiteWise::TimeSeries`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:iotsitewise:<region>:<account_ID>:timeseries/<timeseries_ID>`` When ``resources.type`` equals ``AWS::IoTTwinMaker::Entity`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:iottwinmaker:<region>:<account_ID>:workspace/<workspace_ID>/entity/<entity_ID>`` When ``resources.type`` equals ``AWS::IoTTwinMaker::Workspace`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:iottwinmaker:<region>:<account_ID>:workspace/<workspace_ID>`` When ``resources.type`` equals ``AWS::KendraRanking::ExecutionPlan`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:kendra-ranking:<region>:<account_ID>:rescore-execution-plan/<rescore_execution_plan_ID>`` When ``resources.type`` equals ``AWS::KinesisVideo::Stream`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:kinesisvideo:<region>:<account_ID>:stream/<stream_name>/<creation_time>`` When ``resources.type`` equals ``AWS::ManagedBlockchain::Network`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:managedblockchain:::networks/<network_name>`` When ``resources.type`` equals ``AWS::ManagedBlockchain::Node`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:managedblockchain:<region>:<account_ID>:nodes/<node_ID>`` When ``resources.type`` equals ``AWS::MedicalImaging::Datastore`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:medical-imaging:<region>:<account_ID>:datastore/<data_store_ID>`` When ``resources.type`` equals ``AWS::NeptuneGraph::Graph`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:neptune-graph:<region>:<account_ID>:graph/<graph_ID>`` When ``resources.type`` equals ``AWS::PCAConnectorAD::Connector`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:pca-connector-ad:<region>:<account_ID>:connector/<connector_ID>`` When ``resources.type`` equals ``AWS::QApps:QApp`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:qapps:<region>:<account_ID>:application/<application_UUID>/qapp/<qapp_UUID>`` When ``resources.type`` equals ``AWS::QBusiness::Application`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:qbusiness:<region>:<account_ID>:application/<application_ID>`` When ``resources.type`` equals ``AWS::QBusiness::DataSource`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:qbusiness:<region>:<account_ID>:application/<application_ID>/index/<index_ID>/data-source/<datasource_ID>`` When ``resources.type`` equals ``AWS::QBusiness::Index`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:qbusiness:<region>:<account_ID>:application/<application_ID>/index/<index_ID>`` When ``resources.type`` equals ``AWS::QBusiness::WebExperience`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:qbusiness:<region>:<account_ID>:application/<application_ID>/web-experience/<web_experience_ID>`` When ``resources.type`` equals ``AWS::RDS::DBCluster`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:rds:<region>:<account_ID>:cluster/<cluster_name>`` When ``resources.type`` equals ``AWS::S3::AccessPoint`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in one of the following formats. To log events on all objects in an S3 access point, we recommend that you use only the access point ARN, don’t include the object path, and use the ``StartsWith`` or ``NotStartsWith`` operators. - ``arn:<partition>:s3:<region>:<account_ID>:accesspoint/<access_point_name>`` - ``arn:<partition>:s3:<region>:<account_ID>:accesspoint/<access_point_name>/object/<object_path>`` When ``resources.type`` equals ``AWS::S3ObjectLambda::AccessPoint`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:s3-object-lambda:<region>:<account_ID>:accesspoint/<access_point_name>`` When ``resources.type`` equals ``AWS::S3Outposts::Object`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:s3-outposts:<region>:<account_ID>:<object_path>`` When ``resources.type`` equals ``AWS::SageMaker::Endpoint`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:sagemaker:<region>:<account_ID>:endpoint/<endpoint_name>`` When ``resources.type`` equals ``AWS::SageMaker::ExperimentTrialComponent`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:sagemaker:<region>:<account_ID>:experiment-trial-component/<experiment_trial_component_name>`` When ``resources.type`` equals ``AWS::SageMaker::FeatureGroup`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:sagemaker:<region>:<account_ID>:feature-group/<feature_group_name>`` When ``resources.type`` equals ``AWS::SCN::Instance`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:scn:<region>:<account_ID>:instance/<instance_ID>`` When ``resources.type`` equals ``AWS::ServiceDiscovery::Namespace`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:servicediscovery:<region>:<account_ID>:namespace/<namespace_ID>`` When ``resources.type`` equals ``AWS::ServiceDiscovery::Service`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:servicediscovery:<region>:<account_ID>:service/<service_ID>`` When ``resources.type`` equals ``AWS::SNS::PlatformEndpoint`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:sns:<region>:<account_ID>:endpoint/<endpoint_type>/<endpoint_name>/<endpoint_ID>`` When ``resources.type`` equals ``AWS::SNS::Topic`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:sns:<region>:<account_ID>:<topic_name>`` When ``resources.type`` equals ``AWS::SQS::Queue`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:sqs:<region>:<account_ID>:<queue_name>`` When ``resources.type`` equals ``AWS::SSM::ManagedNode`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in one of the following formats: - ``arn:<partition>:ssm:<region>:<account_ID>:managed-instance/<instance_ID>`` - ``arn:<partition>:ec2:<region>:<account_ID>:instance/<instance_ID>`` When ``resources.type`` equals ``AWS::SSMMessages::ControlChannel`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:ssmmessages:<region>:<account_ID>:control-channel/<channel_ID>`` When ``resources.type`` equals ``AWS::SWF::Domain`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:swf:<region>:<account_ID>:domain/<domain_name>`` When ``resources.type`` equals ``AWS::ThinClient::Device`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:thinclient:<region>:<account_ID>:device/<device_ID>`` When ``resources.type`` equals ``AWS::ThinClient::Environment`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:thinclient:<region>:<account_ID>:environment/<environment_ID>`` When ``resources.type`` equals ``AWS::Timestream::Database`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:timestream:<region>:<account_ID>:database/<database_name>`` When ``resources.type`` equals ``AWS::Timestream::Table`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:timestream:<region>:<account_ID>:database/<database_name>/table/<table_name>`` When resources.type equals ``AWS::VerifiedPermissions::PolicyStore`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:verifiedpermissions:<region>:<account_ID>:policy-store/<policy_store_UUID>``
            :param ends_with: An operator that includes events that match the last few characters of the event record field specified as the value of ``Field`` .
            :param equal_to: An operator that includes events that match the exact value of the event record field specified as the value of ``Field`` . This is the only valid operator that you can use with the ``readOnly`` , ``eventCategory`` , and ``resources.type`` fields.
            :param not_ends_with: An operator that excludes events that match the last few characters of the event record field specified as the value of ``Field`` .
            :param not_equals: An operator that excludes events that match the exact value of the event record field specified as the value of ``Field`` .
            :param not_starts_with: An operator that excludes events that match the first few characters of the event record field specified as the value of ``Field`` .
            :param starts_with: An operator that includes events that match the first few characters of the event record field specified as the value of ``Field`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-eventdatastore-advancedfieldselector.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cloudtrail as cloudtrail
                
                advanced_field_selector_property = cloudtrail.CfnEventDataStore.AdvancedFieldSelectorProperty(
                    field="field",
                
                    # the properties below are optional
                    ends_with=["endsWith"],
                    equal_to=["equalTo"],
                    not_ends_with=["notEndsWith"],
                    not_equals=["notEquals"],
                    not_starts_with=["notStartsWith"],
                    starts_with=["startsWith"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__13e48a5f3f6a4ee090f15046f2744cbdc1f623a943843b6e8cd72526e852b9e5)
                check_type(argname="argument field", value=field, expected_type=type_hints["field"])
                check_type(argname="argument ends_with", value=ends_with, expected_type=type_hints["ends_with"])
                check_type(argname="argument equal_to", value=equal_to, expected_type=type_hints["equal_to"])
                check_type(argname="argument not_ends_with", value=not_ends_with, expected_type=type_hints["not_ends_with"])
                check_type(argname="argument not_equals", value=not_equals, expected_type=type_hints["not_equals"])
                check_type(argname="argument not_starts_with", value=not_starts_with, expected_type=type_hints["not_starts_with"])
                check_type(argname="argument starts_with", value=starts_with, expected_type=type_hints["starts_with"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "field": field,
            }
            if ends_with is not None:
                self._values["ends_with"] = ends_with
            if equal_to is not None:
                self._values["equal_to"] = equal_to
            if not_ends_with is not None:
                self._values["not_ends_with"] = not_ends_with
            if not_equals is not None:
                self._values["not_equals"] = not_equals
            if not_starts_with is not None:
                self._values["not_starts_with"] = not_starts_with
            if starts_with is not None:
                self._values["starts_with"] = starts_with

        @builtins.property
        def field(self) -> builtins.str:
            '''A field in a CloudTrail event record on which to filter events to be logged.

            For event data stores for CloudTrail Insights events, AWS Config configuration items, Audit Manager evidence, or events outside of AWS , the field is used only for selecting events as filtering is not supported.

            For CloudTrail management events, supported fields include ``readOnly`` , ``eventCategory`` , and ``eventSource`` .

            For CloudTrail data events, supported fields include ``readOnly`` , ``eventCategory`` , ``eventName`` , ``resources.type`` , and ``resources.ARN`` .

            For event data stores for CloudTrail Insights events, AWS Config configuration items, Audit Manager evidence, or events outside of AWS , the only supported field is ``eventCategory`` .

            - *``readOnly``* - Optional. Can be set to ``Equals`` a value of ``true`` or ``false`` . If you do not add this field, CloudTrail logs both ``read`` and ``write`` events. A value of ``true`` logs only ``read`` events. A value of ``false`` logs only ``write`` events.
            - *``eventSource``* - For filtering management events only. This can be set to ``NotEquals`` ``kms.amazonaws.com`` or ``NotEquals`` ``rdsdata.amazonaws.com`` .
            - *``eventName``* - Can use any operator. You can use it to ﬁlter in or ﬁlter out any data event logged to CloudTrail, such as ``PutBucket`` or ``GetSnapshotBlock`` . You can have multiple values for this ﬁeld, separated by commas.
            - *``eventCategory``* - This is required and must be set to ``Equals`` .
            - For CloudTrail management events, the value must be ``Management`` .
            - For CloudTrail data events, the value must be ``Data`` .

            The following are used only for event data stores:

            - For CloudTrail Insights events, the value must be ``Insight`` .
            - For AWS Config configuration items, the value must be ``ConfigurationItem`` .
            - For Audit Manager evidence, the value must be ``Evidence`` .
            - For non- AWS events, the value must be ``ActivityAuditLog`` .
            - *``resources.type``* - This ﬁeld is required for CloudTrail data events. ``resources.type`` can only use the ``Equals`` operator, and the value can be one of the following:
            - ``AWS::DynamoDB::Table``
            - ``AWS::Lambda::Function``
            - ``AWS::S3::Object``
            - ``AWS::AppConfig::Configuration``
            - ``AWS::B2BI::Transformer``
            - ``AWS::Bedrock::AgentAlias``
            - ``AWS::Bedrock::KnowledgeBase``
            - ``AWS::Cassandra::Table``
            - ``AWS::CloudFront::KeyValueStore``
            - ``AWS::CloudTrail::Channel``
            - ``AWS::CodeWhisperer::Customization``
            - ``AWS::CodeWhisperer::Profile``
            - ``AWS::Cognito::IdentityPool``
            - ``AWS::DynamoDB::Stream``
            - ``AWS::EC2::Snapshot``
            - ``AWS::EMRWAL::Workspace``
            - ``AWS::FinSpace::Environment``
            - ``AWS::Glue::Table``
            - ``AWS::GreengrassV2::ComponentVersion``
            - ``AWS::GreengrassV2::Deployment``
            - ``AWS::GuardDuty::Detector``
            - ``AWS::IoT::Certificate``
            - ``AWS::IoT::Thing``
            - ``AWS::IoTSiteWise::Asset``
            - ``AWS::IoTSiteWise::TimeSeries``
            - ``AWS::IoTTwinMaker::Entity``
            - ``AWS::IoTTwinMaker::Workspace``
            - ``AWS::KendraRanking::ExecutionPlan``
            - ``AWS::KinesisVideo::Stream``
            - ``AWS::ManagedBlockchain::Network``
            - ``AWS::ManagedBlockchain::Node``
            - ``AWS::MedicalImaging::Datastore``
            - ``AWS::NeptuneGraph::Graph``
            - ``AWS::PCAConnectorAD::Connector``
            - ``AWS::QApps:QApp``
            - ``AWS::QBusiness::Application``
            - ``AWS::QBusiness::DataSource``
            - ``AWS::QBusiness::Index``
            - ``AWS::QBusiness::WebExperience``
            - ``AWS::RDS::DBCluster``
            - ``AWS::S3::AccessPoint``
            - ``AWS::S3ObjectLambda::AccessPoint``
            - ``AWS::S3Outposts::Object``
            - ``AWS::SageMaker::Endpoint``
            - ``AWS::SageMaker::ExperimentTrialComponent``
            - ``AWS::SageMaker::FeatureGroup``
            - ``AWS::ServiceDiscovery::Namespace``
            - ``AWS::ServiceDiscovery::Service``
            - ``AWS::SCN::Instance``
            - ``AWS::SNS::PlatformEndpoint``
            - ``AWS::SNS::Topic``
            - ``AWS::SQS::Queue``
            - ``AWS::SSM::ManagedNode``
            - ``AWS::SSMMessages::ControlChannel``
            - ``AWS::SWF::Domain``
            - ``AWS::ThinClient::Device``
            - ``AWS::ThinClient::Environment``
            - ``AWS::Timestream::Database``
            - ``AWS::Timestream::Table``
            - ``AWS::VerifiedPermissions::PolicyStore``
            - ``AWS::XRay::Trace``

            You can have only one ``resources.type`` ﬁeld per selector. To log data events on more than one resource type, add another selector.

            - *``resources.ARN``* - You can use any operator with ``resources.ARN`` , but if you use ``Equals`` or ``NotEquals`` , the value must exactly match the ARN of a valid resource of the type you've speciﬁed in the template as the value of resources.type.

            .. epigraph::

               You can't use the ``resources.ARN`` field to filter resource types that do not have ARNs.

            The ``resources.ARN`` field can be set one of the following.

            If resources.type equals ``AWS::S3::Object`` , the ARN must be in one of the following formats. To log all data events for all objects in a specific S3 bucket, use the ``StartsWith`` operator, and include only the bucket ARN as the matching value.

            The trailing slash is intentional; do not exclude it. Replace the text between less than and greater than symbols (<>) with resource-specific information.

            - ``arn:<partition>:s3:::<bucket_name>/``
            - ``arn:<partition>:s3:::<bucket_name>/<object_path>/``

            When resources.type equals ``AWS::DynamoDB::Table`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:dynamodb:<region>:<account_ID>:table/<table_name>``

            When resources.type equals ``AWS::Lambda::Function`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:lambda:<region>:<account_ID>:function:<function_name>``

            When resources.type equals ``AWS::AppConfig::Configuration`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:appconfig:<region>:<account_ID>:application/<application_ID>/environment/<environment_ID>/configuration/<configuration_profile_ID>``

            When resources.type equals ``AWS::B2BI::Transformer`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:b2bi:<region>:<account_ID>:transformer/<transformer_ID>``

            When resources.type equals ``AWS::Bedrock::AgentAlias`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:bedrock:<region>:<account_ID>:agent-alias/<agent_ID>/<alias_ID>``

            When resources.type equals ``AWS::Bedrock::KnowledgeBase`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:bedrock:<region>:<account_ID>:knowledge-base/<knowledge_base_ID>``

            When resources.type equals ``AWS::Cassandra::Table`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:cassandra:<region>:<account_ID>:/keyspace/<keyspace_name>/table/<table_name>``

            When resources.type equals ``AWS::CloudFront::KeyValueStore`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:cloudfront:<region>:<account_ID>:key-value-store/<KVS_name>``

            When resources.type equals ``AWS::CloudTrail::Channel`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:cloudtrail:<region>:<account_ID>:channel/<channel_UUID>``

            When resources.type equals ``AWS::CodeWhisperer::Customization`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:codewhisperer:<region>:<account_ID>:customization/<customization_ID>``

            When resources.type equals ``AWS::CodeWhisperer::Profile`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:codewhisperer:<region>:<account_ID>:profile/<profile_ID>``

            When resources.type equals ``AWS::Cognito::IdentityPool`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:cognito-identity:<region>:<account_ID>:identitypool/<identity_pool_ID>``

            When ``resources.type`` equals ``AWS::DynamoDB::Stream`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:dynamodb:<region>:<account_ID>:table/<table_name>/stream/<date_time>``

            When ``resources.type`` equals ``AWS::EC2::Snapshot`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:ec2:<region>::snapshot/<snapshot_ID>``

            When ``resources.type`` equals ``AWS::EMRWAL::Workspace`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:emrwal:<region>:<account_ID>:workspace/<workspace_name>``

            When ``resources.type`` equals ``AWS::FinSpace::Environment`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:finspace:<region>:<account_ID>:environment/<environment_ID>``

            When ``resources.type`` equals ``AWS::Glue::Table`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:glue:<region>:<account_ID>:table/<database_name>/<table_name>``

            When ``resources.type`` equals ``AWS::GreengrassV2::ComponentVersion`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:greengrass:<region>:<account_ID>:components/<component_name>``

            When ``resources.type`` equals ``AWS::GreengrassV2::Deployment`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:greengrass:<region>:<account_ID>:deployments/<deployment_ID``

            When ``resources.type`` equals ``AWS::GuardDuty::Detector`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:guardduty:<region>:<account_ID>:detector/<detector_ID>``

            When ``resources.type`` equals ``AWS::IoT::Certificate`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:iot:<region>:<account_ID>:cert/<certificate_ID>``

            When ``resources.type`` equals ``AWS::IoT::Thing`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:iot:<region>:<account_ID>:thing/<thing_ID>``

            When ``resources.type`` equals ``AWS::IoTSiteWise::Asset`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:iotsitewise:<region>:<account_ID>:asset/<asset_ID>``

            When ``resources.type`` equals ``AWS::IoTSiteWise::TimeSeries`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:iotsitewise:<region>:<account_ID>:timeseries/<timeseries_ID>``

            When ``resources.type`` equals ``AWS::IoTTwinMaker::Entity`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:iottwinmaker:<region>:<account_ID>:workspace/<workspace_ID>/entity/<entity_ID>``

            When ``resources.type`` equals ``AWS::IoTTwinMaker::Workspace`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:iottwinmaker:<region>:<account_ID>:workspace/<workspace_ID>``

            When ``resources.type`` equals ``AWS::KendraRanking::ExecutionPlan`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:kendra-ranking:<region>:<account_ID>:rescore-execution-plan/<rescore_execution_plan_ID>``

            When ``resources.type`` equals ``AWS::KinesisVideo::Stream`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:kinesisvideo:<region>:<account_ID>:stream/<stream_name>/<creation_time>``

            When ``resources.type`` equals ``AWS::ManagedBlockchain::Network`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:managedblockchain:::networks/<network_name>``

            When ``resources.type`` equals ``AWS::ManagedBlockchain::Node`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:managedblockchain:<region>:<account_ID>:nodes/<node_ID>``

            When ``resources.type`` equals ``AWS::MedicalImaging::Datastore`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:medical-imaging:<region>:<account_ID>:datastore/<data_store_ID>``

            When ``resources.type`` equals ``AWS::NeptuneGraph::Graph`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:neptune-graph:<region>:<account_ID>:graph/<graph_ID>``

            When ``resources.type`` equals ``AWS::PCAConnectorAD::Connector`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:pca-connector-ad:<region>:<account_ID>:connector/<connector_ID>``

            When ``resources.type`` equals ``AWS::QApps:QApp`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:qapps:<region>:<account_ID>:application/<application_UUID>/qapp/<qapp_UUID>``

            When ``resources.type`` equals ``AWS::QBusiness::Application`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:qbusiness:<region>:<account_ID>:application/<application_ID>``

            When ``resources.type`` equals ``AWS::QBusiness::DataSource`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:qbusiness:<region>:<account_ID>:application/<application_ID>/index/<index_ID>/data-source/<datasource_ID>``

            When ``resources.type`` equals ``AWS::QBusiness::Index`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:qbusiness:<region>:<account_ID>:application/<application_ID>/index/<index_ID>``

            When ``resources.type`` equals ``AWS::QBusiness::WebExperience`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:qbusiness:<region>:<account_ID>:application/<application_ID>/web-experience/<web_experience_ID>``

            When ``resources.type`` equals ``AWS::RDS::DBCluster`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:rds:<region>:<account_ID>:cluster/<cluster_name>``

            When ``resources.type`` equals ``AWS::S3::AccessPoint`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in one of the following formats. To log events on all objects in an S3 access point, we recommend that you use only the access point ARN, don’t include the object path, and use the ``StartsWith`` or ``NotStartsWith`` operators.

            - ``arn:<partition>:s3:<region>:<account_ID>:accesspoint/<access_point_name>``
            - ``arn:<partition>:s3:<region>:<account_ID>:accesspoint/<access_point_name>/object/<object_path>``

            When ``resources.type`` equals ``AWS::S3ObjectLambda::AccessPoint`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:s3-object-lambda:<region>:<account_ID>:accesspoint/<access_point_name>``

            When ``resources.type`` equals ``AWS::S3Outposts::Object`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:s3-outposts:<region>:<account_ID>:<object_path>``

            When ``resources.type`` equals ``AWS::SageMaker::Endpoint`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:sagemaker:<region>:<account_ID>:endpoint/<endpoint_name>``

            When ``resources.type`` equals ``AWS::SageMaker::ExperimentTrialComponent`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:sagemaker:<region>:<account_ID>:experiment-trial-component/<experiment_trial_component_name>``

            When ``resources.type`` equals ``AWS::SageMaker::FeatureGroup`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:sagemaker:<region>:<account_ID>:feature-group/<feature_group_name>``

            When ``resources.type`` equals ``AWS::SCN::Instance`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:scn:<region>:<account_ID>:instance/<instance_ID>``

            When ``resources.type`` equals ``AWS::ServiceDiscovery::Namespace`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:servicediscovery:<region>:<account_ID>:namespace/<namespace_ID>``

            When ``resources.type`` equals ``AWS::ServiceDiscovery::Service`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:servicediscovery:<region>:<account_ID>:service/<service_ID>``

            When ``resources.type`` equals ``AWS::SNS::PlatformEndpoint`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:sns:<region>:<account_ID>:endpoint/<endpoint_type>/<endpoint_name>/<endpoint_ID>``

            When ``resources.type`` equals ``AWS::SNS::Topic`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:sns:<region>:<account_ID>:<topic_name>``

            When ``resources.type`` equals ``AWS::SQS::Queue`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:sqs:<region>:<account_ID>:<queue_name>``

            When ``resources.type`` equals ``AWS::SSM::ManagedNode`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in one of the following formats:

            - ``arn:<partition>:ssm:<region>:<account_ID>:managed-instance/<instance_ID>``
            - ``arn:<partition>:ec2:<region>:<account_ID>:instance/<instance_ID>``

            When ``resources.type`` equals ``AWS::SSMMessages::ControlChannel`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:ssmmessages:<region>:<account_ID>:control-channel/<channel_ID>``

            When ``resources.type`` equals ``AWS::SWF::Domain`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:swf:<region>:<account_ID>:domain/<domain_name>``

            When ``resources.type`` equals ``AWS::ThinClient::Device`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:thinclient:<region>:<account_ID>:device/<device_ID>``

            When ``resources.type`` equals ``AWS::ThinClient::Environment`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:thinclient:<region>:<account_ID>:environment/<environment_ID>``

            When ``resources.type`` equals ``AWS::Timestream::Database`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:timestream:<region>:<account_ID>:database/<database_name>``

            When ``resources.type`` equals ``AWS::Timestream::Table`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:timestream:<region>:<account_ID>:database/<database_name>/table/<table_name>``

            When resources.type equals ``AWS::VerifiedPermissions::PolicyStore`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:verifiedpermissions:<region>:<account_ID>:policy-store/<policy_store_UUID>``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-eventdatastore-advancedfieldselector.html#cfn-cloudtrail-eventdatastore-advancedfieldselector-field
            '''
            result = self._values.get("field")
            assert result is not None, "Required property 'field' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def ends_with(self) -> typing.Optional[typing.List[builtins.str]]:
            '''An operator that includes events that match the last few characters of the event record field specified as the value of ``Field`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-eventdatastore-advancedfieldselector.html#cfn-cloudtrail-eventdatastore-advancedfieldselector-endswith
            '''
            result = self._values.get("ends_with")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def equal_to(self) -> typing.Optional[typing.List[builtins.str]]:
            '''An operator that includes events that match the exact value of the event record field specified as the value of ``Field`` .

            This is the only valid operator that you can use with the ``readOnly`` , ``eventCategory`` , and ``resources.type`` fields.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-eventdatastore-advancedfieldselector.html#cfn-cloudtrail-eventdatastore-advancedfieldselector-equals
            '''
            result = self._values.get("equal_to")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def not_ends_with(self) -> typing.Optional[typing.List[builtins.str]]:
            '''An operator that excludes events that match the last few characters of the event record field specified as the value of ``Field`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-eventdatastore-advancedfieldselector.html#cfn-cloudtrail-eventdatastore-advancedfieldselector-notendswith
            '''
            result = self._values.get("not_ends_with")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def not_equals(self) -> typing.Optional[typing.List[builtins.str]]:
            '''An operator that excludes events that match the exact value of the event record field specified as the value of ``Field`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-eventdatastore-advancedfieldselector.html#cfn-cloudtrail-eventdatastore-advancedfieldselector-notequals
            '''
            result = self._values.get("not_equals")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def not_starts_with(self) -> typing.Optional[typing.List[builtins.str]]:
            '''An operator that excludes events that match the first few characters of the event record field specified as the value of ``Field`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-eventdatastore-advancedfieldselector.html#cfn-cloudtrail-eventdatastore-advancedfieldselector-notstartswith
            '''
            result = self._values.get("not_starts_with")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def starts_with(self) -> typing.Optional[typing.List[builtins.str]]:
            '''An operator that includes events that match the first few characters of the event record field specified as the value of ``Field`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-eventdatastore-advancedfieldselector.html#cfn-cloudtrail-eventdatastore-advancedfieldselector-startswith
            '''
            result = self._values.get("starts_with")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AdvancedFieldSelectorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cloudtrail.CfnEventDataStore.InsightSelectorProperty",
        jsii_struct_bases=[],
        name_mapping={"insight_type": "insightType"},
    )
    class InsightSelectorProperty:
        def __init__(
            self,
            *,
            insight_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A JSON string that contains a list of Insights types that are logged on an event data store.

            :param insight_type: The type of Insights events to log on an event data store. ``ApiCallRateInsight`` and ``ApiErrorRateInsight`` are valid Insight types. The ``ApiCallRateInsight`` Insights type analyzes write-only management API calls that are aggregated per minute against a baseline API call volume. The ``ApiErrorRateInsight`` Insights type analyzes management API calls that result in error codes. The error is shown if the API call is unsuccessful.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-eventdatastore-insightselector.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cloudtrail as cloudtrail
                
                insight_selector_property = cloudtrail.CfnEventDataStore.InsightSelectorProperty(
                    insight_type="insightType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5dc8183d614f9c9498310cd377ff020cdc048d422b2548bbe678fc3c199d1dc6)
                check_type(argname="argument insight_type", value=insight_type, expected_type=type_hints["insight_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if insight_type is not None:
                self._values["insight_type"] = insight_type

        @builtins.property
        def insight_type(self) -> typing.Optional[builtins.str]:
            '''The type of Insights events to log on an event data store. ``ApiCallRateInsight`` and ``ApiErrorRateInsight`` are valid Insight types.

            The ``ApiCallRateInsight`` Insights type analyzes write-only management API calls that are aggregated per minute against a baseline API call volume.

            The ``ApiErrorRateInsight`` Insights type analyzes management API calls that result in error codes. The error is shown if the API call is unsuccessful.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-eventdatastore-insightselector.html#cfn-cloudtrail-eventdatastore-insightselector-insighttype
            '''
            result = self._values.get("insight_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InsightSelectorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudtrail.CfnEventDataStoreProps",
    jsii_struct_bases=[],
    name_mapping={
        "advanced_event_selectors": "advancedEventSelectors",
        "billing_mode": "billingMode",
        "federation_enabled": "federationEnabled",
        "federation_role_arn": "federationRoleArn",
        "ingestion_enabled": "ingestionEnabled",
        "insights_destination": "insightsDestination",
        "insight_selectors": "insightSelectors",
        "kms_key_id": "kmsKeyId",
        "multi_region_enabled": "multiRegionEnabled",
        "name": "name",
        "organization_enabled": "organizationEnabled",
        "retention_period": "retentionPeriod",
        "tags": "tags",
        "termination_protection_enabled": "terminationProtectionEnabled",
    },
)
class CfnEventDataStoreProps:
    def __init__(
        self,
        *,
        advanced_event_selectors: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEventDataStore.AdvancedEventSelectorProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        billing_mode: typing.Optional[builtins.str] = None,
        federation_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        federation_role_arn: typing.Optional[builtins.str] = None,
        ingestion_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        insights_destination: typing.Optional[builtins.str] = None,
        insight_selectors: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEventDataStore.InsightSelectorProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        multi_region_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        name: typing.Optional[builtins.str] = None,
        organization_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        retention_period: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        termination_protection_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    ) -> None:
        '''Properties for defining a ``CfnEventDataStore``.

        :param advanced_event_selectors: The advanced event selectors to use to select the events for the data store. You can configure up to five advanced event selectors for each event data store. For more information about how to use advanced event selectors to log CloudTrail events, see `Log events by using advanced event selectors <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html#creating-data-event-selectors-advanced>`_ in the CloudTrail User Guide. For more information about how to use advanced event selectors to include AWS Config configuration items in your event data store, see `Create an event data store for AWS Config configuration items <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/lake-eds-cli.html#lake-cli-create-eds-config>`_ in the CloudTrail User Guide. For more information about how to use advanced event selectors to include events outside of AWS events in your event data store, see `Create an integration to log events from outside AWS <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/lake-integrations-cli.html#lake-cli-create-integration>`_ in the CloudTrail User Guide.
        :param billing_mode: The billing mode for the event data store determines the cost for ingesting events and the default and maximum retention period for the event data store. The following are the possible values: - ``EXTENDABLE_RETENTION_PRICING`` - This billing mode is generally recommended if you want a flexible retention period of up to 3653 days (about 10 years). The default retention period for this billing mode is 366 days. - ``FIXED_RETENTION_PRICING`` - This billing mode is recommended if you expect to ingest more than 25 TB of event data per month and need a retention period of up to 2557 days (about 7 years). The default retention period for this billing mode is 2557 days. The default value is ``EXTENDABLE_RETENTION_PRICING`` . For more information about CloudTrail pricing, see `AWS CloudTrail Pricing <https://docs.aws.amazon.com/cloudtrail/pricing/>`_ and `Managing CloudTrail Lake costs <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake-manage-costs.html>`_ .
        :param federation_enabled: Indicates if `Lake query federation <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-federation.html>`_ is enabled. By default, Lake query federation is disabled. You cannot delete an event data store if Lake query federation is enabled.
        :param federation_role_arn: If Lake query federation is enabled, provides the ARN of the federation role used to access the resources for the federated event data store. The federation role must exist in your account and provide the `required minimum permissions <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-federation.html#query-federation-permissions-role>`_ .
        :param ingestion_enabled: Specifies whether the event data store should start ingesting live events. The default is true.
        :param insights_destination: The ARN (or ID suffix of the ARN) of the destination event data store that logs Insights events. For more information, see `Create an event data store for CloudTrail Insights events <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-event-data-store-insights.html>`_ .
        :param insight_selectors: A JSON string that contains the Insights types you want to log on an event data store. ``ApiCallRateInsight`` and ``ApiErrorRateInsight`` are valid Insight types. The ``ApiCallRateInsight`` Insights type analyzes write-only management API calls that are aggregated per minute against a baseline API call volume. The ``ApiErrorRateInsight`` Insights type analyzes management API calls that result in error codes. The error is shown if the API call is unsuccessful.
        :param kms_key_id: Specifies the AWS KMS key ID to use to encrypt the events delivered by CloudTrail. The value can be an alias name prefixed by ``alias/`` , a fully specified ARN to an alias, a fully specified ARN to a key, or a globally unique identifier. .. epigraph:: Disabling or deleting the KMS key, or removing CloudTrail permissions on the key, prevents CloudTrail from logging events to the event data store, and prevents users from querying the data in the event data store that was encrypted with the key. After you associate an event data store with a KMS key, the KMS key cannot be removed or changed. Before you disable or delete a KMS key that you are using with an event data store, delete or back up your event data store. CloudTrail also supports AWS KMS multi-Region keys. For more information about multi-Region keys, see `Using multi-Region keys <https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html>`_ in the *AWS Key Management Service Developer Guide* . Examples: - ``alias/MyAliasName`` - ``arn:aws:kms:us-east-2:123456789012:alias/MyAliasName`` - ``arn:aws:kms:us-east-2:123456789012:key/12345678-1234-1234-1234-123456789012`` - ``12345678-1234-1234-1234-123456789012``
        :param multi_region_enabled: Specifies whether the event data store includes events from all Regions, or only from the Region in which the event data store is created.
        :param name: The name of the event data store.
        :param organization_enabled: Specifies whether an event data store collects events logged for an organization in AWS Organizations .
        :param retention_period: The retention period of the event data store, in days. If ``BillingMode`` is set to ``EXTENDABLE_RETENTION_PRICING`` , you can set a retention period of up to 3653 days, the equivalent of 10 years. If ``BillingMode`` is set to ``FIXED_RETENTION_PRICING`` , you can set a retention period of up to 2557 days, the equivalent of seven years. CloudTrail Lake determines whether to retain an event by checking if the ``eventTime`` of the event is within the specified retention period. For example, if you set a retention period of 90 days, CloudTrail will remove events when the ``eventTime`` is older than 90 days. .. epigraph:: If you plan to copy trail events to this event data store, we recommend that you consider both the age of the events that you want to copy as well as how long you want to keep the copied events in your event data store. For example, if you copy trail events that are 5 years old and specify a retention period of 7 years, the event data store will retain those events for two years.
        :param tags: A list of tags.
        :param termination_protection_enabled: Specifies whether termination protection is enabled for the event data store. If termination protection is enabled, you cannot delete the event data store until termination protection is disabled.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-eventdatastore.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cloudtrail as cloudtrail
            
            cfn_event_data_store_props = cloudtrail.CfnEventDataStoreProps(
                advanced_event_selectors=[cloudtrail.CfnEventDataStore.AdvancedEventSelectorProperty(
                    field_selectors=[cloudtrail.CfnEventDataStore.AdvancedFieldSelectorProperty(
                        field="field",
            
                        # the properties below are optional
                        ends_with=["endsWith"],
                        equal_to=["equalTo"],
                        not_ends_with=["notEndsWith"],
                        not_equals=["notEquals"],
                        not_starts_with=["notStartsWith"],
                        starts_with=["startsWith"]
                    )],
            
                    # the properties below are optional
                    name="name"
                )],
                billing_mode="billingMode",
                federation_enabled=False,
                federation_role_arn="federationRoleArn",
                ingestion_enabled=False,
                insights_destination="insightsDestination",
                insight_selectors=[cloudtrail.CfnEventDataStore.InsightSelectorProperty(
                    insight_type="insightType"
                )],
                kms_key_id="kmsKeyId",
                multi_region_enabled=False,
                name="name",
                organization_enabled=False,
                retention_period=123,
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                termination_protection_enabled=False
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc172d8375a6bcb019f0df4a0d571d671956c64545dc03fc01f9ad66e38ac10e)
            check_type(argname="argument advanced_event_selectors", value=advanced_event_selectors, expected_type=type_hints["advanced_event_selectors"])
            check_type(argname="argument billing_mode", value=billing_mode, expected_type=type_hints["billing_mode"])
            check_type(argname="argument federation_enabled", value=federation_enabled, expected_type=type_hints["federation_enabled"])
            check_type(argname="argument federation_role_arn", value=federation_role_arn, expected_type=type_hints["federation_role_arn"])
            check_type(argname="argument ingestion_enabled", value=ingestion_enabled, expected_type=type_hints["ingestion_enabled"])
            check_type(argname="argument insights_destination", value=insights_destination, expected_type=type_hints["insights_destination"])
            check_type(argname="argument insight_selectors", value=insight_selectors, expected_type=type_hints["insight_selectors"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            check_type(argname="argument multi_region_enabled", value=multi_region_enabled, expected_type=type_hints["multi_region_enabled"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument organization_enabled", value=organization_enabled, expected_type=type_hints["organization_enabled"])
            check_type(argname="argument retention_period", value=retention_period, expected_type=type_hints["retention_period"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument termination_protection_enabled", value=termination_protection_enabled, expected_type=type_hints["termination_protection_enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if advanced_event_selectors is not None:
            self._values["advanced_event_selectors"] = advanced_event_selectors
        if billing_mode is not None:
            self._values["billing_mode"] = billing_mode
        if federation_enabled is not None:
            self._values["federation_enabled"] = federation_enabled
        if federation_role_arn is not None:
            self._values["federation_role_arn"] = federation_role_arn
        if ingestion_enabled is not None:
            self._values["ingestion_enabled"] = ingestion_enabled
        if insights_destination is not None:
            self._values["insights_destination"] = insights_destination
        if insight_selectors is not None:
            self._values["insight_selectors"] = insight_selectors
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if multi_region_enabled is not None:
            self._values["multi_region_enabled"] = multi_region_enabled
        if name is not None:
            self._values["name"] = name
        if organization_enabled is not None:
            self._values["organization_enabled"] = organization_enabled
        if retention_period is not None:
            self._values["retention_period"] = retention_period
        if tags is not None:
            self._values["tags"] = tags
        if termination_protection_enabled is not None:
            self._values["termination_protection_enabled"] = termination_protection_enabled

    @builtins.property
    def advanced_event_selectors(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnEventDataStore.AdvancedEventSelectorProperty]]]]:
        '''The advanced event selectors to use to select the events for the data store.

        You can configure up to five advanced event selectors for each event data store.

        For more information about how to use advanced event selectors to log CloudTrail events, see `Log events by using advanced event selectors <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html#creating-data-event-selectors-advanced>`_ in the CloudTrail User Guide.

        For more information about how to use advanced event selectors to include AWS Config configuration items in your event data store, see `Create an event data store for AWS Config configuration items <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/lake-eds-cli.html#lake-cli-create-eds-config>`_ in the CloudTrail User Guide.

        For more information about how to use advanced event selectors to include events outside of AWS events in your event data store, see `Create an integration to log events from outside AWS <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/lake-integrations-cli.html#lake-cli-create-integration>`_ in the CloudTrail User Guide.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-eventdatastore.html#cfn-cloudtrail-eventdatastore-advancedeventselectors
        '''
        result = self._values.get("advanced_event_selectors")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnEventDataStore.AdvancedEventSelectorProperty]]]], result)

    @builtins.property
    def billing_mode(self) -> typing.Optional[builtins.str]:
        '''The billing mode for the event data store determines the cost for ingesting events and the default and maximum retention period for the event data store.

        The following are the possible values:

        - ``EXTENDABLE_RETENTION_PRICING`` - This billing mode is generally recommended if you want a flexible retention period of up to 3653 days (about 10 years). The default retention period for this billing mode is 366 days.
        - ``FIXED_RETENTION_PRICING`` - This billing mode is recommended if you expect to ingest more than 25 TB of event data per month and need a retention period of up to 2557 days (about 7 years). The default retention period for this billing mode is 2557 days.

        The default value is ``EXTENDABLE_RETENTION_PRICING`` .

        For more information about CloudTrail pricing, see `AWS CloudTrail Pricing <https://docs.aws.amazon.com/cloudtrail/pricing/>`_ and `Managing CloudTrail Lake costs <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake-manage-costs.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-eventdatastore.html#cfn-cloudtrail-eventdatastore-billingmode
        '''
        result = self._values.get("billing_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def federation_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Indicates if `Lake query federation <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-federation.html>`_ is enabled. By default, Lake query federation is disabled. You cannot delete an event data store if Lake query federation is enabled.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-eventdatastore.html#cfn-cloudtrail-eventdatastore-federationenabled
        '''
        result = self._values.get("federation_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def federation_role_arn(self) -> typing.Optional[builtins.str]:
        '''If Lake query federation is enabled, provides the ARN of the federation role used to access the resources for the federated event data store.

        The federation role must exist in your account and provide the `required minimum permissions <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-federation.html#query-federation-permissions-role>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-eventdatastore.html#cfn-cloudtrail-eventdatastore-federationrolearn
        '''
        result = self._values.get("federation_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ingestion_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether the event data store should start ingesting live events.

        The default is true.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-eventdatastore.html#cfn-cloudtrail-eventdatastore-ingestionenabled
        '''
        result = self._values.get("ingestion_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def insights_destination(self) -> typing.Optional[builtins.str]:
        '''The ARN (or ID suffix of the ARN) of the destination event data store that logs Insights events.

        For more information, see `Create an event data store for CloudTrail Insights events <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-event-data-store-insights.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-eventdatastore.html#cfn-cloudtrail-eventdatastore-insightsdestination
        '''
        result = self._values.get("insights_destination")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def insight_selectors(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnEventDataStore.InsightSelectorProperty]]]]:
        '''A JSON string that contains the Insights types you want to log on an event data store.

        ``ApiCallRateInsight`` and ``ApiErrorRateInsight`` are valid Insight types.

        The ``ApiCallRateInsight`` Insights type analyzes write-only management API calls that are aggregated per minute against a baseline API call volume.

        The ``ApiErrorRateInsight`` Insights type analyzes management API calls that result in error codes. The error is shown if the API call is unsuccessful.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-eventdatastore.html#cfn-cloudtrail-eventdatastore-insightselectors
        '''
        result = self._values.get("insight_selectors")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnEventDataStore.InsightSelectorProperty]]]], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Specifies the AWS KMS key ID to use to encrypt the events delivered by CloudTrail.

        The value can be an alias name prefixed by ``alias/`` , a fully specified ARN to an alias, a fully specified ARN to a key, or a globally unique identifier.
        .. epigraph::

           Disabling or deleting the KMS key, or removing CloudTrail permissions on the key, prevents CloudTrail from logging events to the event data store, and prevents users from querying the data in the event data store that was encrypted with the key. After you associate an event data store with a KMS key, the KMS key cannot be removed or changed. Before you disable or delete a KMS key that you are using with an event data store, delete or back up your event data store.

        CloudTrail also supports AWS KMS multi-Region keys. For more information about multi-Region keys, see `Using multi-Region keys <https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html>`_ in the *AWS Key Management Service Developer Guide* .

        Examples:

        - ``alias/MyAliasName``
        - ``arn:aws:kms:us-east-2:123456789012:alias/MyAliasName``
        - ``arn:aws:kms:us-east-2:123456789012:key/12345678-1234-1234-1234-123456789012``
        - ``12345678-1234-1234-1234-123456789012``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-eventdatastore.html#cfn-cloudtrail-eventdatastore-kmskeyid
        '''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def multi_region_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether the event data store includes events from all Regions, or only from the Region in which the event data store is created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-eventdatastore.html#cfn-cloudtrail-eventdatastore-multiregionenabled
        '''
        result = self._values.get("multi_region_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the event data store.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-eventdatastore.html#cfn-cloudtrail-eventdatastore-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def organization_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether an event data store collects events logged for an organization in AWS Organizations .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-eventdatastore.html#cfn-cloudtrail-eventdatastore-organizationenabled
        '''
        result = self._values.get("organization_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def retention_period(self) -> typing.Optional[jsii.Number]:
        '''The retention period of the event data store, in days.

        If ``BillingMode`` is set to ``EXTENDABLE_RETENTION_PRICING`` , you can set a retention period of up to 3653 days, the equivalent of 10 years. If ``BillingMode`` is set to ``FIXED_RETENTION_PRICING`` , you can set a retention period of up to 2557 days, the equivalent of seven years.

        CloudTrail Lake determines whether to retain an event by checking if the ``eventTime`` of the event is within the specified retention period. For example, if you set a retention period of 90 days, CloudTrail will remove events when the ``eventTime`` is older than 90 days.
        .. epigraph::

           If you plan to copy trail events to this event data store, we recommend that you consider both the age of the events that you want to copy as well as how long you want to keep the copied events in your event data store. For example, if you copy trail events that are 5 years old and specify a retention period of 7 years, the event data store will retain those events for two years.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-eventdatastore.html#cfn-cloudtrail-eventdatastore-retentionperiod
        '''
        result = self._values.get("retention_period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of tags.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-eventdatastore.html#cfn-cloudtrail-eventdatastore-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def termination_protection_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether termination protection is enabled for the event data store.

        If termination protection is enabled, you cannot delete the event data store until termination protection is disabled.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-eventdatastore.html#cfn-cloudtrail-eventdatastore-terminationprotectionenabled
        '''
        result = self._values.get("termination_protection_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEventDataStoreProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnResourcePolicy(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudtrail.CfnResourcePolicy",
):
    '''Attaches a resource-based permission policy to a CloudTrail channel that is used for an integration with an event source outside of AWS .

    For more information about resource-based policies, see `CloudTrail resource-based policy examples <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/security_iam_resource-based-policy-examples.html>`_ in the *CloudTrail User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-resourcepolicy.html
    :cloudformationResource: AWS::CloudTrail::ResourcePolicy
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_cloudtrail as cloudtrail
        
        # resource_policy: Any
        
        cfn_resource_policy = cloudtrail.CfnResourcePolicy(self, "MyCfnResourcePolicy",
            resource_arn="resourceArn",
            resource_policy=resource_policy
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        resource_arn: builtins.str,
        resource_policy: typing.Any,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param resource_arn: The Amazon Resource Name (ARN) of the CloudTrail channel attached to the resource-based policy. The following is the format of a resource ARN: ``arn:aws:cloudtrail:us-east-2:123456789012:channel/MyChannel`` .
        :param resource_policy: A JSON-formatted string for an AWS resource-based policy. The following are requirements for the resource policy: - Contains only one action: cloudtrail-data:PutAuditEvents - Contains at least one statement. The policy can have a maximum of 20 statements. - Each statement contains at least one principal. A statement can have a maximum of 50 principals.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e63ea1d0937535109b462c5587b69e94988e2caeb02b49177c8a53040c569033)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnResourcePolicyProps(
            resource_arn=resource_arn, resource_policy=resource_policy
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b32eb6fa58caf5ce6823a322212ade70664d4d37672f421c013fb2553ece2012)
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
            type_hints = typing.get_type_hints(_typecheckingstub__cb1739db5f96a9531e5f3655ec7c5b40527ac758bdb8bb842b79ad2206ec375f)
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
    @jsii.member(jsii_name="resourceArn")
    def resource_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the CloudTrail channel attached to the resource-based policy.'''
        return typing.cast(builtins.str, jsii.get(self, "resourceArn"))

    @resource_arn.setter
    def resource_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c2bbc7a61c40e678ccc323afced9d77064978b41254369fee4db815497450dcd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceArn", value)

    @builtins.property
    @jsii.member(jsii_name="resourcePolicy")
    def resource_policy(self) -> typing.Any:
        '''A JSON-formatted string for an AWS resource-based policy.'''
        return typing.cast(typing.Any, jsii.get(self, "resourcePolicy"))

    @resource_policy.setter
    def resource_policy(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e81052ff397bfd1d58bc17a51da7f1ee393c63b322c1b7d43b49b11f481e0ade)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourcePolicy", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudtrail.CfnResourcePolicyProps",
    jsii_struct_bases=[],
    name_mapping={"resource_arn": "resourceArn", "resource_policy": "resourcePolicy"},
)
class CfnResourcePolicyProps:
    def __init__(
        self,
        *,
        resource_arn: builtins.str,
        resource_policy: typing.Any,
    ) -> None:
        '''Properties for defining a ``CfnResourcePolicy``.

        :param resource_arn: The Amazon Resource Name (ARN) of the CloudTrail channel attached to the resource-based policy. The following is the format of a resource ARN: ``arn:aws:cloudtrail:us-east-2:123456789012:channel/MyChannel`` .
        :param resource_policy: A JSON-formatted string for an AWS resource-based policy. The following are requirements for the resource policy: - Contains only one action: cloudtrail-data:PutAuditEvents - Contains at least one statement. The policy can have a maximum of 20 statements. - Each statement contains at least one principal. A statement can have a maximum of 50 principals.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-resourcepolicy.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cloudtrail as cloudtrail
            
            # resource_policy: Any
            
            cfn_resource_policy_props = cloudtrail.CfnResourcePolicyProps(
                resource_arn="resourceArn",
                resource_policy=resource_policy
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a325337b33ae7cf48e36873295a3efad9af30e81615a436102a6dd5c10a2f08)
            check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
            check_type(argname="argument resource_policy", value=resource_policy, expected_type=type_hints["resource_policy"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resource_arn": resource_arn,
            "resource_policy": resource_policy,
        }

    @builtins.property
    def resource_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the CloudTrail channel attached to the resource-based policy.

        The following is the format of a resource ARN: ``arn:aws:cloudtrail:us-east-2:123456789012:channel/MyChannel`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-resourcepolicy.html#cfn-cloudtrail-resourcepolicy-resourcearn
        '''
        result = self._values.get("resource_arn")
        assert result is not None, "Required property 'resource_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_policy(self) -> typing.Any:
        '''A JSON-formatted string for an AWS resource-based policy.

        The following are requirements for the resource policy:

        - Contains only one action: cloudtrail-data:PutAuditEvents
        - Contains at least one statement. The policy can have a maximum of 20 statements.
        - Each statement contains at least one principal. A statement can have a maximum of 50 principals.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-resourcepolicy.html#cfn-cloudtrail-resourcepolicy-resourcepolicy
        '''
        result = self._values.get("resource_policy")
        assert result is not None, "Required property 'resource_policy' is missing"
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResourcePolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnTrail(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudtrail.CfnTrail",
):
    '''Creates a trail that specifies the settings for delivery of log data to an Amazon S3 bucket.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html
    :cloudformationResource: AWS::CloudTrail::Trail
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_cloudtrail as cloudtrail
        
        cfn_trail = cloudtrail.CfnTrail(self, "MyCfnTrail",
            is_logging=False,
            s3_bucket_name="s3BucketName",
        
            # the properties below are optional
            advanced_event_selectors=[cloudtrail.CfnTrail.AdvancedEventSelectorProperty(
                field_selectors=[cloudtrail.CfnTrail.AdvancedFieldSelectorProperty(
                    field="field",
        
                    # the properties below are optional
                    ends_with=["endsWith"],
                    equal_to=["equalTo"],
                    not_ends_with=["notEndsWith"],
                    not_equals=["notEquals"],
                    not_starts_with=["notStartsWith"],
                    starts_with=["startsWith"]
                )],
        
                # the properties below are optional
                name="name"
            )],
            cloud_watch_logs_log_group_arn="cloudWatchLogsLogGroupArn",
            cloud_watch_logs_role_arn="cloudWatchLogsRoleArn",
            enable_log_file_validation=False,
            event_selectors=[cloudtrail.CfnTrail.EventSelectorProperty(
                data_resources=[cloudtrail.CfnTrail.DataResourceProperty(
                    type="type",
        
                    # the properties below are optional
                    values=["values"]
                )],
                exclude_management_event_sources=["excludeManagementEventSources"],
                include_management_events=False,
                read_write_type="readWriteType"
            )],
            include_global_service_events=False,
            insight_selectors=[cloudtrail.CfnTrail.InsightSelectorProperty(
                insight_type="insightType"
            )],
            is_multi_region_trail=False,
            is_organization_trail=False,
            kms_key_id="kmsKeyId",
            s3_key_prefix="s3KeyPrefix",
            sns_topic_name="snsTopicName",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            trail_name="trailName"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        is_logging: typing.Union[builtins.bool, _IResolvable_da3f097b],
        s3_bucket_name: builtins.str,
        advanced_event_selectors: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTrail.AdvancedEventSelectorProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        cloud_watch_logs_log_group_arn: typing.Optional[builtins.str] = None,
        cloud_watch_logs_role_arn: typing.Optional[builtins.str] = None,
        enable_log_file_validation: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        event_selectors: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTrail.EventSelectorProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        include_global_service_events: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        insight_selectors: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTrail.InsightSelectorProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        is_multi_region_trail: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        is_organization_trail: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        s3_key_prefix: typing.Optional[builtins.str] = None,
        sns_topic_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        trail_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param is_logging: Whether the CloudTrail trail is currently logging AWS API calls.
        :param s3_bucket_name: Specifies the name of the Amazon S3 bucket designated for publishing log files. See `Amazon S3 Bucket naming rules <https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html>`_ .
        :param advanced_event_selectors: Specifies the settings for advanced event selectors. You can add advanced event selectors, and conditions for your advanced event selectors, up to a maximum of 500 values for all conditions and selectors on a trail. You can use either ``AdvancedEventSelectors`` or ``EventSelectors`` , but not both. If you apply ``AdvancedEventSelectors`` to a trail, any existing ``EventSelectors`` are overwritten. For more information about advanced event selectors, see `Logging data events <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html>`_ in the *AWS CloudTrail User Guide* .
        :param cloud_watch_logs_log_group_arn: Specifies a log group name using an Amazon Resource Name (ARN), a unique identifier that represents the log group to which CloudTrail logs are delivered. You must use a log group that exists in your account. Not required unless you specify ``CloudWatchLogsRoleArn`` .
        :param cloud_watch_logs_role_arn: Specifies the role for the CloudWatch Logs endpoint to assume to write to a user's log group. You must use a role that exists in your account.
        :param enable_log_file_validation: Specifies whether log file validation is enabled. The default is false. .. epigraph:: When you disable log file integrity validation, the chain of digest files is broken after one hour. CloudTrail does not create digest files for log files that were delivered during a period in which log file integrity validation was disabled. For example, if you enable log file integrity validation at noon on January 1, disable it at noon on January 2, and re-enable it at noon on January 10, digest files will not be created for the log files delivered from noon on January 2 to noon on January 10. The same applies whenever you stop CloudTrail logging or delete a trail.
        :param event_selectors: Use event selectors to further specify the management and data event settings for your trail. By default, trails created without specific event selectors will be configured to log all read and write management events, and no data events. When an event occurs in your account, CloudTrail evaluates the event selector for all trails. For each trail, if the event matches any event selector, the trail processes and logs the event. If the event doesn't match any event selector, the trail doesn't log the event. You can configure up to five event selectors for a trail. You cannot apply both event selectors and advanced event selectors to a trail.
        :param include_global_service_events: Specifies whether the trail is publishing events from global services such as IAM to the log files.
        :param insight_selectors: A JSON string that contains the Insights types you want to log on a trail. ``ApiCallRateInsight`` and ``ApiErrorRateInsight`` are valid Insight types. The ``ApiCallRateInsight`` Insights type analyzes write-only management API calls that are aggregated per minute against a baseline API call volume. The ``ApiErrorRateInsight`` Insights type analyzes management API calls that result in error codes. The error is shown if the API call is unsuccessful.
        :param is_multi_region_trail: Specifies whether the trail applies only to the current Region or to all Regions. The default is false. If the trail exists only in the current Region and this value is set to true, shadow trails (replications of the trail) will be created in the other Regions. If the trail exists in all Regions and this value is set to false, the trail will remain in the Region where it was created, and its shadow trails in other Regions will be deleted. As a best practice, consider using trails that log events in all Regions.
        :param is_organization_trail: Specifies whether the trail is applied to all accounts in an organization in AWS Organizations , or only for the current AWS account . The default is false, and cannot be true unless the call is made on behalf of an AWS account that is the management account for an organization in AWS Organizations . If the trail is not an organization trail and this is set to ``true`` , the trail will be created in all AWS accounts that belong to the organization. If the trail is an organization trail and this is set to ``false`` , the trail will remain in the current AWS account but be deleted from all member accounts in the organization. .. epigraph:: Only the management account for the organization can convert an organization trail to a non-organization trail, or convert a non-organization trail to an organization trail.
        :param kms_key_id: Specifies the AWS KMS key ID to use to encrypt the logs delivered by CloudTrail. The value can be an alias name prefixed by "alias/", a fully specified ARN to an alias, a fully specified ARN to a key, or a globally unique identifier. CloudTrail also supports AWS KMS multi-Region keys. For more information about multi-Region keys, see `Using multi-Region keys <https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html>`_ in the *AWS Key Management Service Developer Guide* . Examples: - alias/MyAliasName - arn:aws:kms:us-east-2:123456789012:alias/MyAliasName - arn:aws:kms:us-east-2:123456789012:key/12345678-1234-1234-1234-123456789012 - 12345678-1234-1234-1234-123456789012
        :param s3_key_prefix: Specifies the Amazon S3 key prefix that comes after the name of the bucket you have designated for log file delivery. For more information, see `Finding Your CloudTrail Log Files <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/get-and-view-cloudtrail-log-files.html#cloudtrail-find-log-files>`_ . The maximum length is 200 characters.
        :param sns_topic_name: Specifies the name of the Amazon SNS topic defined for notification of log file delivery. The maximum length is 256 characters.
        :param tags: A custom set of tags (key-value pairs) for this trail.
        :param trail_name: Specifies the name of the trail. The name must meet the following requirements:. - Contain only ASCII letters (a-z, A-Z), numbers (0-9), periods (.), underscores (_), or dashes (-) - Start with a letter or number, and end with a letter or number - Be between 3 and 128 characters - Have no adjacent periods, underscores or dashes. Names like ``my-_namespace`` and ``my--namespace`` are not valid. - Not be in IP address format (for example, 192.168.5.4)
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2259d5765ec84e4697f55f0d491871f1aa010feb94b3445a33a9e4b9f9cfbbd5)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnTrailProps(
            is_logging=is_logging,
            s3_bucket_name=s3_bucket_name,
            advanced_event_selectors=advanced_event_selectors,
            cloud_watch_logs_log_group_arn=cloud_watch_logs_log_group_arn,
            cloud_watch_logs_role_arn=cloud_watch_logs_role_arn,
            enable_log_file_validation=enable_log_file_validation,
            event_selectors=event_selectors,
            include_global_service_events=include_global_service_events,
            insight_selectors=insight_selectors,
            is_multi_region_trail=is_multi_region_trail,
            is_organization_trail=is_organization_trail,
            kms_key_id=kms_key_id,
            s3_key_prefix=s3_key_prefix,
            sns_topic_name=sns_topic_name,
            tags=tags,
            trail_name=trail_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27c0b3977f3ce3e2ad80b21e158e38a08a45c6700ebeed895b3710e8c214a1bb)
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
            type_hints = typing.get_type_hints(_typecheckingstub__340f9d2dc4d668d217253c3ecdc1999319497932039d9878e65bb3b5c99c3e42)
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
        '''``Ref`` returns the ARN of the CloudTrail trail, such as ``arn:aws:cloudtrail:us-east-2:123456789012:trail/myCloudTrail`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrSnsTopicArn")
    def attr_sns_topic_arn(self) -> builtins.str:
        '''``Ref`` returns the ARN of the Amazon SNS topic that's associated with the CloudTrail trail, such as ``arn:aws:sns:us-east-2:123456789012:mySNSTopic`` .

        :cloudformationAttribute: SnsTopicArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSnsTopicArn"))

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
    @jsii.member(jsii_name="isLogging")
    def is_logging(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
        '''Whether the CloudTrail trail is currently logging AWS API calls.'''
        return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], jsii.get(self, "isLogging"))

    @is_logging.setter
    def is_logging(
        self,
        value: typing.Union[builtins.bool, _IResolvable_da3f097b],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28420bf6c9605a8eeb3ac59acf7f894b63e53a96b92e9d477f9cd206f2f9cf41)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isLogging", value)

    @builtins.property
    @jsii.member(jsii_name="s3BucketName")
    def s3_bucket_name(self) -> builtins.str:
        '''Specifies the name of the Amazon S3 bucket designated for publishing log files.'''
        return typing.cast(builtins.str, jsii.get(self, "s3BucketName"))

    @s3_bucket_name.setter
    def s3_bucket_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__950bb01f69a31c7f47512f3a4330d4ce5db85c66795a79936ef3af33a322c8b2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3BucketName", value)

    @builtins.property
    @jsii.member(jsii_name="advancedEventSelectors")
    def advanced_event_selectors(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTrail.AdvancedEventSelectorProperty"]]]]:
        '''Specifies the settings for advanced event selectors.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTrail.AdvancedEventSelectorProperty"]]]], jsii.get(self, "advancedEventSelectors"))

    @advanced_event_selectors.setter
    def advanced_event_selectors(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTrail.AdvancedEventSelectorProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae10dc28d41ecf82427e4cef4ce27f9c40933974aaf57ffd8e73f19c06621f53)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "advancedEventSelectors", value)

    @builtins.property
    @jsii.member(jsii_name="cloudWatchLogsLogGroupArn")
    def cloud_watch_logs_log_group_arn(self) -> typing.Optional[builtins.str]:
        '''Specifies a log group name using an Amazon Resource Name (ARN), a unique identifier that represents the log group to which CloudTrail logs are delivered.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cloudWatchLogsLogGroupArn"))

    @cloud_watch_logs_log_group_arn.setter
    def cloud_watch_logs_log_group_arn(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58f37437f0af59fad3f65c1d9ef003f52fa49f6aabcba3b40c779f379b8b0410)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloudWatchLogsLogGroupArn", value)

    @builtins.property
    @jsii.member(jsii_name="cloudWatchLogsRoleArn")
    def cloud_watch_logs_role_arn(self) -> typing.Optional[builtins.str]:
        '''Specifies the role for the CloudWatch Logs endpoint to assume to write to a user's log group.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cloudWatchLogsRoleArn"))

    @cloud_watch_logs_role_arn.setter
    def cloud_watch_logs_role_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cabe9b73fb8bc4d76fde324653a247811fa621cc9003d2c46e84b890b919cd28)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloudWatchLogsRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="enableLogFileValidation")
    def enable_log_file_validation(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether log file validation is enabled.

        The default is false.
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "enableLogFileValidation"))

    @enable_log_file_validation.setter
    def enable_log_file_validation(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b942505386f8e61551da02925be57cd0474923089182c193fde0b17fe804056)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableLogFileValidation", value)

    @builtins.property
    @jsii.member(jsii_name="eventSelectors")
    def event_selectors(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTrail.EventSelectorProperty"]]]]:
        '''Use event selectors to further specify the management and data event settings for your trail.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTrail.EventSelectorProperty"]]]], jsii.get(self, "eventSelectors"))

    @event_selectors.setter
    def event_selectors(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTrail.EventSelectorProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ef2943100a700e4bd2b0922f697c3d0da51c014bec4f2a8c4063f59e83067d7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventSelectors", value)

    @builtins.property
    @jsii.member(jsii_name="includeGlobalServiceEvents")
    def include_global_service_events(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether the trail is publishing events from global services such as IAM to the log files.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "includeGlobalServiceEvents"))

    @include_global_service_events.setter
    def include_global_service_events(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a1c2489b0dca720e7fab9917132eaf8dc9468d58f2d500bccd7579577d74434)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeGlobalServiceEvents", value)

    @builtins.property
    @jsii.member(jsii_name="insightSelectors")
    def insight_selectors(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTrail.InsightSelectorProperty"]]]]:
        '''A JSON string that contains the Insights types you want to log on a trail.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTrail.InsightSelectorProperty"]]]], jsii.get(self, "insightSelectors"))

    @insight_selectors.setter
    def insight_selectors(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTrail.InsightSelectorProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d11150f51682efcafc38f048d84c35a263b443e02355965298d566b0714947d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "insightSelectors", value)

    @builtins.property
    @jsii.member(jsii_name="isMultiRegionTrail")
    def is_multi_region_trail(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether the trail applies only to the current Region or to all Regions.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "isMultiRegionTrail"))

    @is_multi_region_trail.setter
    def is_multi_region_trail(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48558347dbb5febc8abf93096cfc174c76cbab4c443d68076643e329fb0787c0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isMultiRegionTrail", value)

    @builtins.property
    @jsii.member(jsii_name="isOrganizationTrail")
    def is_organization_trail(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether the trail is applied to all accounts in an organization in AWS Organizations , or only for the current AWS account .'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "isOrganizationTrail"))

    @is_organization_trail.setter
    def is_organization_trail(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__583ab7d05361279f7f55956fec04616c02d033f55ef6113a3cf8c36630cd5ec5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isOrganizationTrail", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Specifies the AWS KMS key ID to use to encrypt the logs delivered by CloudTrail.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4fac6d2810385893265f6ef2611c9d8ceaa7635731b1ae56291d8e43a83cc907)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="s3KeyPrefix")
    def s3_key_prefix(self) -> typing.Optional[builtins.str]:
        '''Specifies the Amazon S3 key prefix that comes after the name of the bucket you have designated for log file delivery.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "s3KeyPrefix"))

    @s3_key_prefix.setter
    def s3_key_prefix(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a62410d04026f326fad72a00ba17b36e83eb965baeada846126607f600de0f7f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3KeyPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="snsTopicName")
    def sns_topic_name(self) -> typing.Optional[builtins.str]:
        '''Specifies the name of the Amazon SNS topic defined for notification of log file delivery.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "snsTopicName"))

    @sns_topic_name.setter
    def sns_topic_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99ce4d6977c0c8f0ad39dd667104baf8babcda3f6e64b94361cd24302f9bfb12)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snsTopicName", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A custom set of tags (key-value pairs) for this trail.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b6e90bde6d2082aefdd7c19acee054825987d54ead9c95ec2dbe11a014f72339)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="trailName")
    def trail_name(self) -> typing.Optional[builtins.str]:
        '''Specifies the name of the trail.

        The name must meet the following requirements:.
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "trailName"))

    @trail_name.setter
    def trail_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29683f56476eaa26adca4a9a9312d409428d1af457282b2a0f93af552333a02e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "trailName", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cloudtrail.CfnTrail.AdvancedEventSelectorProperty",
        jsii_struct_bases=[],
        name_mapping={"field_selectors": "fieldSelectors", "name": "name"},
    )
    class AdvancedEventSelectorProperty:
        def __init__(
            self,
            *,
            field_selectors: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTrail.AdvancedFieldSelectorProperty", typing.Dict[builtins.str, typing.Any]]]]],
            name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Advanced event selectors let you create fine-grained selectors for CloudTrail management and data events.

            They help you control costs by logging only those events that are important to you. For more information about advanced event selectors, see `Logging management events <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.html>`_ and `Logging data events <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html>`_ in the *AWS CloudTrail User Guide* .

            You cannot apply both event selectors and advanced event selectors to a trail.

            *Supported CloudTrail event record fields for management events*

            - ``eventCategory`` (required)
            - ``eventSource``
            - ``readOnly``

            *Supported CloudTrail event record fields for data events*

            - ``eventCategory`` (required)
            - ``resources.type`` (required)
            - ``readOnly``
            - ``eventName``
            - ``resources.ARN``

            .. epigraph::

               For event data stores for CloudTrail Insights events, AWS Config configuration items, Audit Manager evidence, or events outside of AWS , the only supported field is ``eventCategory`` .

            :param field_selectors: Contains all selector statements in an advanced event selector.
            :param name: An optional, descriptive name for an advanced event selector, such as "Log data events for only two S3 buckets".

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-advancedeventselector.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cloudtrail as cloudtrail
                
                advanced_event_selector_property = cloudtrail.CfnTrail.AdvancedEventSelectorProperty(
                    field_selectors=[cloudtrail.CfnTrail.AdvancedFieldSelectorProperty(
                        field="field",
                
                        # the properties below are optional
                        ends_with=["endsWith"],
                        equal_to=["equalTo"],
                        not_ends_with=["notEndsWith"],
                        not_equals=["notEquals"],
                        not_starts_with=["notStartsWith"],
                        starts_with=["startsWith"]
                    )],
                
                    # the properties below are optional
                    name="name"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6dd875607ea907f4214c12153b0923eaa1b2093e9c2bd798cc9ef56cf7886059)
                check_type(argname="argument field_selectors", value=field_selectors, expected_type=type_hints["field_selectors"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "field_selectors": field_selectors,
            }
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def field_selectors(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTrail.AdvancedFieldSelectorProperty"]]]:
            '''Contains all selector statements in an advanced event selector.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-advancedeventselector.html#cfn-cloudtrail-trail-advancedeventselector-fieldselectors
            '''
            result = self._values.get("field_selectors")
            assert result is not None, "Required property 'field_selectors' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTrail.AdvancedFieldSelectorProperty"]]], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''An optional, descriptive name for an advanced event selector, such as "Log data events for only two S3 buckets".

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-advancedeventselector.html#cfn-cloudtrail-trail-advancedeventselector-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AdvancedEventSelectorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cloudtrail.CfnTrail.AdvancedFieldSelectorProperty",
        jsii_struct_bases=[],
        name_mapping={
            "field": "field",
            "ends_with": "endsWith",
            "equal_to": "equalTo",
            "not_ends_with": "notEndsWith",
            "not_equals": "notEquals",
            "not_starts_with": "notStartsWith",
            "starts_with": "startsWith",
        },
    )
    class AdvancedFieldSelectorProperty:
        def __init__(
            self,
            *,
            field: builtins.str,
            ends_with: typing.Optional[typing.Sequence[builtins.str]] = None,
            equal_to: typing.Optional[typing.Sequence[builtins.str]] = None,
            not_ends_with: typing.Optional[typing.Sequence[builtins.str]] = None,
            not_equals: typing.Optional[typing.Sequence[builtins.str]] = None,
            not_starts_with: typing.Optional[typing.Sequence[builtins.str]] = None,
            starts_with: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''A single selector statement in an advanced event selector.

            :param field: A field in a CloudTrail event record on which to filter events to be logged. For event data stores for CloudTrail Insights events, AWS Config configuration items, Audit Manager evidence, or events outside of AWS , the field is used only for selecting events as filtering is not supported. For CloudTrail management events, supported fields include ``readOnly`` , ``eventCategory`` , and ``eventSource`` . For CloudTrail data events, supported fields include ``readOnly`` , ``eventCategory`` , ``eventName`` , ``resources.type`` , and ``resources.ARN`` . For event data stores for CloudTrail Insights events, AWS Config configuration items, Audit Manager evidence, or events outside of AWS , the only supported field is ``eventCategory`` . - *``readOnly``* - Optional. Can be set to ``Equals`` a value of ``true`` or ``false`` . If you do not add this field, CloudTrail logs both ``read`` and ``write`` events. A value of ``true`` logs only ``read`` events. A value of ``false`` logs only ``write`` events. - *``eventSource``* - For filtering management events only. This can be set to ``NotEquals`` ``kms.amazonaws.com`` or ``NotEquals`` ``rdsdata.amazonaws.com`` . - *``eventName``* - Can use any operator. You can use it to ﬁlter in or ﬁlter out any data event logged to CloudTrail, such as ``PutBucket`` or ``GetSnapshotBlock`` . You can have multiple values for this ﬁeld, separated by commas. - *``eventCategory``* - This is required and must be set to ``Equals`` . - For CloudTrail management events, the value must be ``Management`` . - For CloudTrail data events, the value must be ``Data`` . The following are used only for event data stores: - For CloudTrail Insights events, the value must be ``Insight`` . - For AWS Config configuration items, the value must be ``ConfigurationItem`` . - For Audit Manager evidence, the value must be ``Evidence`` . - For non- AWS events, the value must be ``ActivityAuditLog`` . - *``resources.type``* - This ﬁeld is required for CloudTrail data events. ``resources.type`` can only use the ``Equals`` operator, and the value can be one of the following: - ``AWS::DynamoDB::Table`` - ``AWS::Lambda::Function`` - ``AWS::S3::Object`` - ``AWS::AppConfig::Configuration`` - ``AWS::B2BI::Transformer`` - ``AWS::Bedrock::AgentAlias`` - ``AWS::Bedrock::KnowledgeBase`` - ``AWS::Cassandra::Table`` - ``AWS::CloudFront::KeyValueStore`` - ``AWS::CloudTrail::Channel`` - ``AWS::CodeWhisperer::Customization`` - ``AWS::CodeWhisperer::Profile`` - ``AWS::Cognito::IdentityPool`` - ``AWS::DynamoDB::Stream`` - ``AWS::EC2::Snapshot`` - ``AWS::EMRWAL::Workspace`` - ``AWS::FinSpace::Environment`` - ``AWS::Glue::Table`` - ``AWS::GreengrassV2::ComponentVersion`` - ``AWS::GreengrassV2::Deployment`` - ``AWS::GuardDuty::Detector`` - ``AWS::IoT::Certificate`` - ``AWS::IoT::Thing`` - ``AWS::IoTSiteWise::Asset`` - ``AWS::IoTSiteWise::TimeSeries`` - ``AWS::IoTTwinMaker::Entity`` - ``AWS::IoTTwinMaker::Workspace`` - ``AWS::KendraRanking::ExecutionPlan`` - ``AWS::KinesisVideo::Stream`` - ``AWS::ManagedBlockchain::Network`` - ``AWS::ManagedBlockchain::Node`` - ``AWS::MedicalImaging::Datastore`` - ``AWS::NeptuneGraph::Graph`` - ``AWS::PCAConnectorAD::Connector`` - ``AWS::QApps:QApp`` - ``AWS::QBusiness::Application`` - ``AWS::QBusiness::DataSource`` - ``AWS::QBusiness::Index`` - ``AWS::QBusiness::WebExperience`` - ``AWS::RDS::DBCluster`` - ``AWS::S3::AccessPoint`` - ``AWS::S3ObjectLambda::AccessPoint`` - ``AWS::S3Outposts::Object`` - ``AWS::SageMaker::Endpoint`` - ``AWS::SageMaker::ExperimentTrialComponent`` - ``AWS::SageMaker::FeatureGroup`` - ``AWS::ServiceDiscovery::Namespace`` - ``AWS::ServiceDiscovery::Service`` - ``AWS::SCN::Instance`` - ``AWS::SNS::PlatformEndpoint`` - ``AWS::SNS::Topic`` - ``AWS::SQS::Queue`` - ``AWS::SSM::ManagedNode`` - ``AWS::SSMMessages::ControlChannel`` - ``AWS::SWF::Domain`` - ``AWS::ThinClient::Device`` - ``AWS::ThinClient::Environment`` - ``AWS::Timestream::Database`` - ``AWS::Timestream::Table`` - ``AWS::VerifiedPermissions::PolicyStore`` - ``AWS::XRay::Trace`` You can have only one ``resources.type`` ﬁeld per selector. To log data events on more than one resource type, add another selector. - *``resources.ARN``* - You can use any operator with ``resources.ARN`` , but if you use ``Equals`` or ``NotEquals`` , the value must exactly match the ARN of a valid resource of the type you've speciﬁed in the template as the value of resources.type. .. epigraph:: You can't use the ``resources.ARN`` field to filter resource types that do not have ARNs. The ``resources.ARN`` field can be set one of the following. If resources.type equals ``AWS::S3::Object`` , the ARN must be in one of the following formats. To log all data events for all objects in a specific S3 bucket, use the ``StartsWith`` operator, and include only the bucket ARN as the matching value. The trailing slash is intentional; do not exclude it. Replace the text between less than and greater than symbols (<>) with resource-specific information. - ``arn:<partition>:s3:::<bucket_name>/`` - ``arn:<partition>:s3:::<bucket_name>/<object_path>/`` When resources.type equals ``AWS::DynamoDB::Table`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:dynamodb:<region>:<account_ID>:table/<table_name>`` When resources.type equals ``AWS::Lambda::Function`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:lambda:<region>:<account_ID>:function:<function_name>`` When resources.type equals ``AWS::AppConfig::Configuration`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:appconfig:<region>:<account_ID>:application/<application_ID>/environment/<environment_ID>/configuration/<configuration_profile_ID>`` When resources.type equals ``AWS::B2BI::Transformer`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:b2bi:<region>:<account_ID>:transformer/<transformer_ID>`` When resources.type equals ``AWS::Bedrock::AgentAlias`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:bedrock:<region>:<account_ID>:agent-alias/<agent_ID>/<alias_ID>`` When resources.type equals ``AWS::Bedrock::KnowledgeBase`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:bedrock:<region>:<account_ID>:knowledge-base/<knowledge_base_ID>`` When resources.type equals ``AWS::Cassandra::Table`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:cassandra:<region>:<account_ID>:/keyspace/<keyspace_name>/table/<table_name>`` When resources.type equals ``AWS::CloudFront::KeyValueStore`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:cloudfront:<region>:<account_ID>:key-value-store/<KVS_name>`` When resources.type equals ``AWS::CloudTrail::Channel`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:cloudtrail:<region>:<account_ID>:channel/<channel_UUID>`` When resources.type equals ``AWS::CodeWhisperer::Customization`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:codewhisperer:<region>:<account_ID>:customization/<customization_ID>`` When resources.type equals ``AWS::CodeWhisperer::Profile`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:codewhisperer:<region>:<account_ID>:profile/<profile_ID>`` When resources.type equals ``AWS::Cognito::IdentityPool`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:cognito-identity:<region>:<account_ID>:identitypool/<identity_pool_ID>`` When ``resources.type`` equals ``AWS::DynamoDB::Stream`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:dynamodb:<region>:<account_ID>:table/<table_name>/stream/<date_time>`` When ``resources.type`` equals ``AWS::EC2::Snapshot`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:ec2:<region>::snapshot/<snapshot_ID>`` When ``resources.type`` equals ``AWS::EMRWAL::Workspace`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:emrwal:<region>:<account_ID>:workspace/<workspace_name>`` When ``resources.type`` equals ``AWS::FinSpace::Environment`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:finspace:<region>:<account_ID>:environment/<environment_ID>`` When ``resources.type`` equals ``AWS::Glue::Table`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:glue:<region>:<account_ID>:table/<database_name>/<table_name>`` When ``resources.type`` equals ``AWS::GreengrassV2::ComponentVersion`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:greengrass:<region>:<account_ID>:components/<component_name>`` When ``resources.type`` equals ``AWS::GreengrassV2::Deployment`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:greengrass:<region>:<account_ID>:deployments/<deployment_ID`` When ``resources.type`` equals ``AWS::GuardDuty::Detector`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:guardduty:<region>:<account_ID>:detector/<detector_ID>`` When ``resources.type`` equals ``AWS::IoT::Certificate`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:iot:<region>:<account_ID>:cert/<certificate_ID>`` When ``resources.type`` equals ``AWS::IoT::Thing`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:iot:<region>:<account_ID>:thing/<thing_ID>`` When ``resources.type`` equals ``AWS::IoTSiteWise::Asset`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:iotsitewise:<region>:<account_ID>:asset/<asset_ID>`` When ``resources.type`` equals ``AWS::IoTSiteWise::TimeSeries`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:iotsitewise:<region>:<account_ID>:timeseries/<timeseries_ID>`` When ``resources.type`` equals ``AWS::IoTTwinMaker::Entity`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:iottwinmaker:<region>:<account_ID>:workspace/<workspace_ID>/entity/<entity_ID>`` When ``resources.type`` equals ``AWS::IoTTwinMaker::Workspace`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:iottwinmaker:<region>:<account_ID>:workspace/<workspace_ID>`` When ``resources.type`` equals ``AWS::KendraRanking::ExecutionPlan`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:kendra-ranking:<region>:<account_ID>:rescore-execution-plan/<rescore_execution_plan_ID>`` When ``resources.type`` equals ``AWS::KinesisVideo::Stream`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:kinesisvideo:<region>:<account_ID>:stream/<stream_name>/<creation_time>`` When ``resources.type`` equals ``AWS::ManagedBlockchain::Network`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:managedblockchain:::networks/<network_name>`` When ``resources.type`` equals ``AWS::ManagedBlockchain::Node`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:managedblockchain:<region>:<account_ID>:nodes/<node_ID>`` When ``resources.type`` equals ``AWS::MedicalImaging::Datastore`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:medical-imaging:<region>:<account_ID>:datastore/<data_store_ID>`` When ``resources.type`` equals ``AWS::NeptuneGraph::Graph`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:neptune-graph:<region>:<account_ID>:graph/<graph_ID>`` When ``resources.type`` equals ``AWS::PCAConnectorAD::Connector`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:pca-connector-ad:<region>:<account_ID>:connector/<connector_ID>`` When ``resources.type`` equals ``AWS::QApps:QApp`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:qapps:<region>:<account_ID>:application/<application_UUID>/qapp/<qapp_UUID>`` When ``resources.type`` equals ``AWS::QBusiness::Application`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:qbusiness:<region>:<account_ID>:application/<application_ID>`` When ``resources.type`` equals ``AWS::QBusiness::DataSource`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:qbusiness:<region>:<account_ID>:application/<application_ID>/index/<index_ID>/data-source/<datasource_ID>`` When ``resources.type`` equals ``AWS::QBusiness::Index`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:qbusiness:<region>:<account_ID>:application/<application_ID>/index/<index_ID>`` When ``resources.type`` equals ``AWS::QBusiness::WebExperience`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:qbusiness:<region>:<account_ID>:application/<application_ID>/web-experience/<web_experience_ID>`` When ``resources.type`` equals ``AWS::RDS::DBCluster`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:rds:<region>:<account_ID>:cluster/<cluster_name>`` When ``resources.type`` equals ``AWS::S3::AccessPoint`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in one of the following formats. To log events on all objects in an S3 access point, we recommend that you use only the access point ARN, don’t include the object path, and use the ``StartsWith`` or ``NotStartsWith`` operators. - ``arn:<partition>:s3:<region>:<account_ID>:accesspoint/<access_point_name>`` - ``arn:<partition>:s3:<region>:<account_ID>:accesspoint/<access_point_name>/object/<object_path>`` When ``resources.type`` equals ``AWS::S3ObjectLambda::AccessPoint`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:s3-object-lambda:<region>:<account_ID>:accesspoint/<access_point_name>`` When ``resources.type`` equals ``AWS::S3Outposts::Object`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:s3-outposts:<region>:<account_ID>:<object_path>`` When ``resources.type`` equals ``AWS::SageMaker::Endpoint`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:sagemaker:<region>:<account_ID>:endpoint/<endpoint_name>`` When ``resources.type`` equals ``AWS::SageMaker::ExperimentTrialComponent`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:sagemaker:<region>:<account_ID>:experiment-trial-component/<experiment_trial_component_name>`` When ``resources.type`` equals ``AWS::SageMaker::FeatureGroup`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:sagemaker:<region>:<account_ID>:feature-group/<feature_group_name>`` When ``resources.type`` equals ``AWS::SCN::Instance`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:scn:<region>:<account_ID>:instance/<instance_ID>`` When ``resources.type`` equals ``AWS::ServiceDiscovery::Namespace`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:servicediscovery:<region>:<account_ID>:namespace/<namespace_ID>`` When ``resources.type`` equals ``AWS::ServiceDiscovery::Service`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:servicediscovery:<region>:<account_ID>:service/<service_ID>`` When ``resources.type`` equals ``AWS::SNS::PlatformEndpoint`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:sns:<region>:<account_ID>:endpoint/<endpoint_type>/<endpoint_name>/<endpoint_ID>`` When ``resources.type`` equals ``AWS::SNS::Topic`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:sns:<region>:<account_ID>:<topic_name>`` When ``resources.type`` equals ``AWS::SQS::Queue`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:sqs:<region>:<account_ID>:<queue_name>`` When ``resources.type`` equals ``AWS::SSM::ManagedNode`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in one of the following formats: - ``arn:<partition>:ssm:<region>:<account_ID>:managed-instance/<instance_ID>`` - ``arn:<partition>:ec2:<region>:<account_ID>:instance/<instance_ID>`` When ``resources.type`` equals ``AWS::SSMMessages::ControlChannel`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:ssmmessages:<region>:<account_ID>:control-channel/<channel_ID>`` When ``resources.type`` equals ``AWS::SWF::Domain`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:swf:<region>:<account_ID>:domain/<domain_name>`` When ``resources.type`` equals ``AWS::ThinClient::Device`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:thinclient:<region>:<account_ID>:device/<device_ID>`` When ``resources.type`` equals ``AWS::ThinClient::Environment`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:thinclient:<region>:<account_ID>:environment/<environment_ID>`` When ``resources.type`` equals ``AWS::Timestream::Database`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:timestream:<region>:<account_ID>:database/<database_name>`` When ``resources.type`` equals ``AWS::Timestream::Table`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:timestream:<region>:<account_ID>:database/<database_name>/table/<table_name>`` When resources.type equals ``AWS::VerifiedPermissions::PolicyStore`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format: - ``arn:<partition>:verifiedpermissions:<region>:<account_ID>:policy-store/<policy_store_UUID>``
            :param ends_with: An operator that includes events that match the last few characters of the event record field specified as the value of ``Field`` .
            :param equal_to: An operator that includes events that match the exact value of the event record field specified as the value of ``Field`` . This is the only valid operator that you can use with the ``readOnly`` , ``eventCategory`` , and ``resources.type`` fields.
            :param not_ends_with: An operator that excludes events that match the last few characters of the event record field specified as the value of ``Field`` .
            :param not_equals: An operator that excludes events that match the exact value of the event record field specified as the value of ``Field`` .
            :param not_starts_with: An operator that excludes events that match the first few characters of the event record field specified as the value of ``Field`` .
            :param starts_with: An operator that includes events that match the first few characters of the event record field specified as the value of ``Field`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-advancedfieldselector.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cloudtrail as cloudtrail
                
                advanced_field_selector_property = cloudtrail.CfnTrail.AdvancedFieldSelectorProperty(
                    field="field",
                
                    # the properties below are optional
                    ends_with=["endsWith"],
                    equal_to=["equalTo"],
                    not_ends_with=["notEndsWith"],
                    not_equals=["notEquals"],
                    not_starts_with=["notStartsWith"],
                    starts_with=["startsWith"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ec8d9a5e1a3e1eac8b87551fd80e338cfe5e5578a88b45c91f7b6ae91857b236)
                check_type(argname="argument field", value=field, expected_type=type_hints["field"])
                check_type(argname="argument ends_with", value=ends_with, expected_type=type_hints["ends_with"])
                check_type(argname="argument equal_to", value=equal_to, expected_type=type_hints["equal_to"])
                check_type(argname="argument not_ends_with", value=not_ends_with, expected_type=type_hints["not_ends_with"])
                check_type(argname="argument not_equals", value=not_equals, expected_type=type_hints["not_equals"])
                check_type(argname="argument not_starts_with", value=not_starts_with, expected_type=type_hints["not_starts_with"])
                check_type(argname="argument starts_with", value=starts_with, expected_type=type_hints["starts_with"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "field": field,
            }
            if ends_with is not None:
                self._values["ends_with"] = ends_with
            if equal_to is not None:
                self._values["equal_to"] = equal_to
            if not_ends_with is not None:
                self._values["not_ends_with"] = not_ends_with
            if not_equals is not None:
                self._values["not_equals"] = not_equals
            if not_starts_with is not None:
                self._values["not_starts_with"] = not_starts_with
            if starts_with is not None:
                self._values["starts_with"] = starts_with

        @builtins.property
        def field(self) -> builtins.str:
            '''A field in a CloudTrail event record on which to filter events to be logged.

            For event data stores for CloudTrail Insights events, AWS Config configuration items, Audit Manager evidence, or events outside of AWS , the field is used only for selecting events as filtering is not supported.

            For CloudTrail management events, supported fields include ``readOnly`` , ``eventCategory`` , and ``eventSource`` .

            For CloudTrail data events, supported fields include ``readOnly`` , ``eventCategory`` , ``eventName`` , ``resources.type`` , and ``resources.ARN`` .

            For event data stores for CloudTrail Insights events, AWS Config configuration items, Audit Manager evidence, or events outside of AWS , the only supported field is ``eventCategory`` .

            - *``readOnly``* - Optional. Can be set to ``Equals`` a value of ``true`` or ``false`` . If you do not add this field, CloudTrail logs both ``read`` and ``write`` events. A value of ``true`` logs only ``read`` events. A value of ``false`` logs only ``write`` events.
            - *``eventSource``* - For filtering management events only. This can be set to ``NotEquals`` ``kms.amazonaws.com`` or ``NotEquals`` ``rdsdata.amazonaws.com`` .
            - *``eventName``* - Can use any operator. You can use it to ﬁlter in or ﬁlter out any data event logged to CloudTrail, such as ``PutBucket`` or ``GetSnapshotBlock`` . You can have multiple values for this ﬁeld, separated by commas.
            - *``eventCategory``* - This is required and must be set to ``Equals`` .
            - For CloudTrail management events, the value must be ``Management`` .
            - For CloudTrail data events, the value must be ``Data`` .

            The following are used only for event data stores:

            - For CloudTrail Insights events, the value must be ``Insight`` .
            - For AWS Config configuration items, the value must be ``ConfigurationItem`` .
            - For Audit Manager evidence, the value must be ``Evidence`` .
            - For non- AWS events, the value must be ``ActivityAuditLog`` .
            - *``resources.type``* - This ﬁeld is required for CloudTrail data events. ``resources.type`` can only use the ``Equals`` operator, and the value can be one of the following:
            - ``AWS::DynamoDB::Table``
            - ``AWS::Lambda::Function``
            - ``AWS::S3::Object``
            - ``AWS::AppConfig::Configuration``
            - ``AWS::B2BI::Transformer``
            - ``AWS::Bedrock::AgentAlias``
            - ``AWS::Bedrock::KnowledgeBase``
            - ``AWS::Cassandra::Table``
            - ``AWS::CloudFront::KeyValueStore``
            - ``AWS::CloudTrail::Channel``
            - ``AWS::CodeWhisperer::Customization``
            - ``AWS::CodeWhisperer::Profile``
            - ``AWS::Cognito::IdentityPool``
            - ``AWS::DynamoDB::Stream``
            - ``AWS::EC2::Snapshot``
            - ``AWS::EMRWAL::Workspace``
            - ``AWS::FinSpace::Environment``
            - ``AWS::Glue::Table``
            - ``AWS::GreengrassV2::ComponentVersion``
            - ``AWS::GreengrassV2::Deployment``
            - ``AWS::GuardDuty::Detector``
            - ``AWS::IoT::Certificate``
            - ``AWS::IoT::Thing``
            - ``AWS::IoTSiteWise::Asset``
            - ``AWS::IoTSiteWise::TimeSeries``
            - ``AWS::IoTTwinMaker::Entity``
            - ``AWS::IoTTwinMaker::Workspace``
            - ``AWS::KendraRanking::ExecutionPlan``
            - ``AWS::KinesisVideo::Stream``
            - ``AWS::ManagedBlockchain::Network``
            - ``AWS::ManagedBlockchain::Node``
            - ``AWS::MedicalImaging::Datastore``
            - ``AWS::NeptuneGraph::Graph``
            - ``AWS::PCAConnectorAD::Connector``
            - ``AWS::QApps:QApp``
            - ``AWS::QBusiness::Application``
            - ``AWS::QBusiness::DataSource``
            - ``AWS::QBusiness::Index``
            - ``AWS::QBusiness::WebExperience``
            - ``AWS::RDS::DBCluster``
            - ``AWS::S3::AccessPoint``
            - ``AWS::S3ObjectLambda::AccessPoint``
            - ``AWS::S3Outposts::Object``
            - ``AWS::SageMaker::Endpoint``
            - ``AWS::SageMaker::ExperimentTrialComponent``
            - ``AWS::SageMaker::FeatureGroup``
            - ``AWS::ServiceDiscovery::Namespace``
            - ``AWS::ServiceDiscovery::Service``
            - ``AWS::SCN::Instance``
            - ``AWS::SNS::PlatformEndpoint``
            - ``AWS::SNS::Topic``
            - ``AWS::SQS::Queue``
            - ``AWS::SSM::ManagedNode``
            - ``AWS::SSMMessages::ControlChannel``
            - ``AWS::SWF::Domain``
            - ``AWS::ThinClient::Device``
            - ``AWS::ThinClient::Environment``
            - ``AWS::Timestream::Database``
            - ``AWS::Timestream::Table``
            - ``AWS::VerifiedPermissions::PolicyStore``
            - ``AWS::XRay::Trace``

            You can have only one ``resources.type`` ﬁeld per selector. To log data events on more than one resource type, add another selector.

            - *``resources.ARN``* - You can use any operator with ``resources.ARN`` , but if you use ``Equals`` or ``NotEquals`` , the value must exactly match the ARN of a valid resource of the type you've speciﬁed in the template as the value of resources.type.

            .. epigraph::

               You can't use the ``resources.ARN`` field to filter resource types that do not have ARNs.

            The ``resources.ARN`` field can be set one of the following.

            If resources.type equals ``AWS::S3::Object`` , the ARN must be in one of the following formats. To log all data events for all objects in a specific S3 bucket, use the ``StartsWith`` operator, and include only the bucket ARN as the matching value.

            The trailing slash is intentional; do not exclude it. Replace the text between less than and greater than symbols (<>) with resource-specific information.

            - ``arn:<partition>:s3:::<bucket_name>/``
            - ``arn:<partition>:s3:::<bucket_name>/<object_path>/``

            When resources.type equals ``AWS::DynamoDB::Table`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:dynamodb:<region>:<account_ID>:table/<table_name>``

            When resources.type equals ``AWS::Lambda::Function`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:lambda:<region>:<account_ID>:function:<function_name>``

            When resources.type equals ``AWS::AppConfig::Configuration`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:appconfig:<region>:<account_ID>:application/<application_ID>/environment/<environment_ID>/configuration/<configuration_profile_ID>``

            When resources.type equals ``AWS::B2BI::Transformer`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:b2bi:<region>:<account_ID>:transformer/<transformer_ID>``

            When resources.type equals ``AWS::Bedrock::AgentAlias`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:bedrock:<region>:<account_ID>:agent-alias/<agent_ID>/<alias_ID>``

            When resources.type equals ``AWS::Bedrock::KnowledgeBase`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:bedrock:<region>:<account_ID>:knowledge-base/<knowledge_base_ID>``

            When resources.type equals ``AWS::Cassandra::Table`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:cassandra:<region>:<account_ID>:/keyspace/<keyspace_name>/table/<table_name>``

            When resources.type equals ``AWS::CloudFront::KeyValueStore`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:cloudfront:<region>:<account_ID>:key-value-store/<KVS_name>``

            When resources.type equals ``AWS::CloudTrail::Channel`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:cloudtrail:<region>:<account_ID>:channel/<channel_UUID>``

            When resources.type equals ``AWS::CodeWhisperer::Customization`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:codewhisperer:<region>:<account_ID>:customization/<customization_ID>``

            When resources.type equals ``AWS::CodeWhisperer::Profile`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:codewhisperer:<region>:<account_ID>:profile/<profile_ID>``

            When resources.type equals ``AWS::Cognito::IdentityPool`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:cognito-identity:<region>:<account_ID>:identitypool/<identity_pool_ID>``

            When ``resources.type`` equals ``AWS::DynamoDB::Stream`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:dynamodb:<region>:<account_ID>:table/<table_name>/stream/<date_time>``

            When ``resources.type`` equals ``AWS::EC2::Snapshot`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:ec2:<region>::snapshot/<snapshot_ID>``

            When ``resources.type`` equals ``AWS::EMRWAL::Workspace`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:emrwal:<region>:<account_ID>:workspace/<workspace_name>``

            When ``resources.type`` equals ``AWS::FinSpace::Environment`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:finspace:<region>:<account_ID>:environment/<environment_ID>``

            When ``resources.type`` equals ``AWS::Glue::Table`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:glue:<region>:<account_ID>:table/<database_name>/<table_name>``

            When ``resources.type`` equals ``AWS::GreengrassV2::ComponentVersion`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:greengrass:<region>:<account_ID>:components/<component_name>``

            When ``resources.type`` equals ``AWS::GreengrassV2::Deployment`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:greengrass:<region>:<account_ID>:deployments/<deployment_ID``

            When ``resources.type`` equals ``AWS::GuardDuty::Detector`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:guardduty:<region>:<account_ID>:detector/<detector_ID>``

            When ``resources.type`` equals ``AWS::IoT::Certificate`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:iot:<region>:<account_ID>:cert/<certificate_ID>``

            When ``resources.type`` equals ``AWS::IoT::Thing`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:iot:<region>:<account_ID>:thing/<thing_ID>``

            When ``resources.type`` equals ``AWS::IoTSiteWise::Asset`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:iotsitewise:<region>:<account_ID>:asset/<asset_ID>``

            When ``resources.type`` equals ``AWS::IoTSiteWise::TimeSeries`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:iotsitewise:<region>:<account_ID>:timeseries/<timeseries_ID>``

            When ``resources.type`` equals ``AWS::IoTTwinMaker::Entity`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:iottwinmaker:<region>:<account_ID>:workspace/<workspace_ID>/entity/<entity_ID>``

            When ``resources.type`` equals ``AWS::IoTTwinMaker::Workspace`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:iottwinmaker:<region>:<account_ID>:workspace/<workspace_ID>``

            When ``resources.type`` equals ``AWS::KendraRanking::ExecutionPlan`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:kendra-ranking:<region>:<account_ID>:rescore-execution-plan/<rescore_execution_plan_ID>``

            When ``resources.type`` equals ``AWS::KinesisVideo::Stream`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:kinesisvideo:<region>:<account_ID>:stream/<stream_name>/<creation_time>``

            When ``resources.type`` equals ``AWS::ManagedBlockchain::Network`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:managedblockchain:::networks/<network_name>``

            When ``resources.type`` equals ``AWS::ManagedBlockchain::Node`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:managedblockchain:<region>:<account_ID>:nodes/<node_ID>``

            When ``resources.type`` equals ``AWS::MedicalImaging::Datastore`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:medical-imaging:<region>:<account_ID>:datastore/<data_store_ID>``

            When ``resources.type`` equals ``AWS::NeptuneGraph::Graph`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:neptune-graph:<region>:<account_ID>:graph/<graph_ID>``

            When ``resources.type`` equals ``AWS::PCAConnectorAD::Connector`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:pca-connector-ad:<region>:<account_ID>:connector/<connector_ID>``

            When ``resources.type`` equals ``AWS::QApps:QApp`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:qapps:<region>:<account_ID>:application/<application_UUID>/qapp/<qapp_UUID>``

            When ``resources.type`` equals ``AWS::QBusiness::Application`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:qbusiness:<region>:<account_ID>:application/<application_ID>``

            When ``resources.type`` equals ``AWS::QBusiness::DataSource`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:qbusiness:<region>:<account_ID>:application/<application_ID>/index/<index_ID>/data-source/<datasource_ID>``

            When ``resources.type`` equals ``AWS::QBusiness::Index`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:qbusiness:<region>:<account_ID>:application/<application_ID>/index/<index_ID>``

            When ``resources.type`` equals ``AWS::QBusiness::WebExperience`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:qbusiness:<region>:<account_ID>:application/<application_ID>/web-experience/<web_experience_ID>``

            When ``resources.type`` equals ``AWS::RDS::DBCluster`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:rds:<region>:<account_ID>:cluster/<cluster_name>``

            When ``resources.type`` equals ``AWS::S3::AccessPoint`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in one of the following formats. To log events on all objects in an S3 access point, we recommend that you use only the access point ARN, don’t include the object path, and use the ``StartsWith`` or ``NotStartsWith`` operators.

            - ``arn:<partition>:s3:<region>:<account_ID>:accesspoint/<access_point_name>``
            - ``arn:<partition>:s3:<region>:<account_ID>:accesspoint/<access_point_name>/object/<object_path>``

            When ``resources.type`` equals ``AWS::S3ObjectLambda::AccessPoint`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:s3-object-lambda:<region>:<account_ID>:accesspoint/<access_point_name>``

            When ``resources.type`` equals ``AWS::S3Outposts::Object`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:s3-outposts:<region>:<account_ID>:<object_path>``

            When ``resources.type`` equals ``AWS::SageMaker::Endpoint`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:sagemaker:<region>:<account_ID>:endpoint/<endpoint_name>``

            When ``resources.type`` equals ``AWS::SageMaker::ExperimentTrialComponent`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:sagemaker:<region>:<account_ID>:experiment-trial-component/<experiment_trial_component_name>``

            When ``resources.type`` equals ``AWS::SageMaker::FeatureGroup`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:sagemaker:<region>:<account_ID>:feature-group/<feature_group_name>``

            When ``resources.type`` equals ``AWS::SCN::Instance`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:scn:<region>:<account_ID>:instance/<instance_ID>``

            When ``resources.type`` equals ``AWS::ServiceDiscovery::Namespace`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:servicediscovery:<region>:<account_ID>:namespace/<namespace_ID>``

            When ``resources.type`` equals ``AWS::ServiceDiscovery::Service`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:servicediscovery:<region>:<account_ID>:service/<service_ID>``

            When ``resources.type`` equals ``AWS::SNS::PlatformEndpoint`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:sns:<region>:<account_ID>:endpoint/<endpoint_type>/<endpoint_name>/<endpoint_ID>``

            When ``resources.type`` equals ``AWS::SNS::Topic`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:sns:<region>:<account_ID>:<topic_name>``

            When ``resources.type`` equals ``AWS::SQS::Queue`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:sqs:<region>:<account_ID>:<queue_name>``

            When ``resources.type`` equals ``AWS::SSM::ManagedNode`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in one of the following formats:

            - ``arn:<partition>:ssm:<region>:<account_ID>:managed-instance/<instance_ID>``
            - ``arn:<partition>:ec2:<region>:<account_ID>:instance/<instance_ID>``

            When ``resources.type`` equals ``AWS::SSMMessages::ControlChannel`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:ssmmessages:<region>:<account_ID>:control-channel/<channel_ID>``

            When ``resources.type`` equals ``AWS::SWF::Domain`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:swf:<region>:<account_ID>:domain/<domain_name>``

            When ``resources.type`` equals ``AWS::ThinClient::Device`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:thinclient:<region>:<account_ID>:device/<device_ID>``

            When ``resources.type`` equals ``AWS::ThinClient::Environment`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:thinclient:<region>:<account_ID>:environment/<environment_ID>``

            When ``resources.type`` equals ``AWS::Timestream::Database`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:timestream:<region>:<account_ID>:database/<database_name>``

            When ``resources.type`` equals ``AWS::Timestream::Table`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:timestream:<region>:<account_ID>:database/<database_name>/table/<table_name>``

            When resources.type equals ``AWS::VerifiedPermissions::PolicyStore`` , and the operator is set to ``Equals`` or ``NotEquals`` , the ARN must be in the following format:

            - ``arn:<partition>:verifiedpermissions:<region>:<account_ID>:policy-store/<policy_store_UUID>``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-advancedfieldselector.html#cfn-cloudtrail-trail-advancedfieldselector-field
            '''
            result = self._values.get("field")
            assert result is not None, "Required property 'field' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def ends_with(self) -> typing.Optional[typing.List[builtins.str]]:
            '''An operator that includes events that match the last few characters of the event record field specified as the value of ``Field`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-advancedfieldselector.html#cfn-cloudtrail-trail-advancedfieldselector-endswith
            '''
            result = self._values.get("ends_with")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def equal_to(self) -> typing.Optional[typing.List[builtins.str]]:
            '''An operator that includes events that match the exact value of the event record field specified as the value of ``Field`` .

            This is the only valid operator that you can use with the ``readOnly`` , ``eventCategory`` , and ``resources.type`` fields.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-advancedfieldselector.html#cfn-cloudtrail-trail-advancedfieldselector-equals
            '''
            result = self._values.get("equal_to")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def not_ends_with(self) -> typing.Optional[typing.List[builtins.str]]:
            '''An operator that excludes events that match the last few characters of the event record field specified as the value of ``Field`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-advancedfieldselector.html#cfn-cloudtrail-trail-advancedfieldselector-notendswith
            '''
            result = self._values.get("not_ends_with")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def not_equals(self) -> typing.Optional[typing.List[builtins.str]]:
            '''An operator that excludes events that match the exact value of the event record field specified as the value of ``Field`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-advancedfieldselector.html#cfn-cloudtrail-trail-advancedfieldselector-notequals
            '''
            result = self._values.get("not_equals")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def not_starts_with(self) -> typing.Optional[typing.List[builtins.str]]:
            '''An operator that excludes events that match the first few characters of the event record field specified as the value of ``Field`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-advancedfieldselector.html#cfn-cloudtrail-trail-advancedfieldselector-notstartswith
            '''
            result = self._values.get("not_starts_with")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def starts_with(self) -> typing.Optional[typing.List[builtins.str]]:
            '''An operator that includes events that match the first few characters of the event record field specified as the value of ``Field`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-advancedfieldselector.html#cfn-cloudtrail-trail-advancedfieldselector-startswith
            '''
            result = self._values.get("starts_with")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AdvancedFieldSelectorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cloudtrail.CfnTrail.DataResourceProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type", "values": "values"},
    )
    class DataResourceProperty:
        def __init__(
            self,
            *,
            type: builtins.str,
            values: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Data events provide information about the resource operations performed on or within a resource itself.

            These are also known as data plane operations. You can specify up to 250 data resources for a trail.

            Configure the ``DataResource`` to specify the resource type and resource ARNs for which you want to log data events.

            You can specify the following resource types in your event selectors for your trail:

            - ``AWS::DynamoDB::Table``
            - ``AWS::Lambda::Function``
            - ``AWS::S3::Object``

            .. epigraph::

               The total number of allowed data resources is 250. This number can be distributed between 1 and 5 event selectors, but the total cannot exceed 250 across all selectors for the trail.

               If you are using advanced event selectors, the maximum total number of values for all conditions, across all advanced event selectors for the trail, is 500.

            The following example demonstrates how logging works when you configure logging of all data events for an S3 bucket named ``bucket-1`` . In this example, the CloudTrail user specified an empty prefix, and the option to log both ``Read`` and ``Write`` data events.

            - A user uploads an image file to ``bucket-1`` .
            - The ``PutObject`` API operation is an Amazon S3 object-level API. It is recorded as a data event in CloudTrail. Because the CloudTrail user specified an S3 bucket with an empty prefix, events that occur on any object in that bucket are logged. The trail processes and logs the event.
            - A user uploads an object to an Amazon S3 bucket named ``arn:aws:s3:::bucket-2`` .
            - The ``PutObject`` API operation occurred for an object in an S3 bucket that the CloudTrail user didn't specify for the trail. The trail doesn’t log the event.

            The following example demonstrates how logging works when you configure logging of AWS Lambda data events for a Lambda function named *MyLambdaFunction* , but not for all Lambda functions.

            - A user runs a script that includes a call to the *MyLambdaFunction* function and the *MyOtherLambdaFunction* function.
            - The ``Invoke`` API operation on *MyLambdaFunction* is an Lambda API. It is recorded as a data event in CloudTrail. Because the CloudTrail user specified logging data events for *MyLambdaFunction* , any invocations of that function are logged. The trail processes and logs the event.
            - The ``Invoke`` API operation on *MyOtherLambdaFunction* is an Lambda API. Because the CloudTrail user did not specify logging data events for all Lambda functions, the ``Invoke`` operation for *MyOtherLambdaFunction* does not match the function specified for the trail. The trail doesn’t log the event.

            :param type: The resource type in which you want to log data events. You can specify the following *basic* event selector resource types: - ``AWS::DynamoDB::Table`` - ``AWS::Lambda::Function`` - ``AWS::S3::Object`` Additional resource types are available through *advanced* event selectors. For more information about these additional resource types, see `AdvancedFieldSelector <https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_AdvancedFieldSelector.html>`_ .
            :param values: An array of Amazon Resource Name (ARN) strings or partial ARN strings for the specified resource type. - To log data events for all objects in all S3 buckets in your AWS account , specify the prefix as ``arn:aws:s3`` . .. epigraph:: This also enables logging of data event activity performed by any user or role in your AWS account , even if that activity is performed on a bucket that belongs to another AWS account . - To log data events for all objects in an S3 bucket, specify the bucket and an empty object prefix such as ``arn:aws:s3:::bucket-1/`` . The trail logs data events for all objects in this S3 bucket. - To log data events for specific objects, specify the S3 bucket and object prefix such as ``arn:aws:s3:::bucket-1/example-images`` . The trail logs data events for objects in this S3 bucket that match the prefix. - To log data events for all Lambda functions in your AWS account , specify the prefix as ``arn:aws:lambda`` . .. epigraph:: This also enables logging of ``Invoke`` activity performed by any user or role in your AWS account , even if that activity is performed on a function that belongs to another AWS account . - To log data events for a specific Lambda function, specify the function ARN. .. epigraph:: Lambda function ARNs are exact. For example, if you specify a function ARN *arn:aws:lambda:us-west-2:111111111111:function:helloworld* , data events will only be logged for *arn:aws:lambda:us-west-2:111111111111:function:helloworld* . They will not be logged for *arn:aws:lambda:us-west-2:111111111111:function:helloworld2* . - To log data events for all DynamoDB tables in your AWS account , specify the prefix as ``arn:aws:dynamodb`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-dataresource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cloudtrail as cloudtrail
                
                data_resource_property = cloudtrail.CfnTrail.DataResourceProperty(
                    type="type",
                
                    # the properties below are optional
                    values=["values"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__eba75230621acc9cbcd78ccb16505dcc1e9707f9ce1d5b5c64f36220a2fbd761)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument values", value=values, expected_type=type_hints["values"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "type": type,
            }
            if values is not None:
                self._values["values"] = values

        @builtins.property
        def type(self) -> builtins.str:
            '''The resource type in which you want to log data events.

            You can specify the following *basic* event selector resource types:

            - ``AWS::DynamoDB::Table``
            - ``AWS::Lambda::Function``
            - ``AWS::S3::Object``

            Additional resource types are available through *advanced* event selectors. For more information about these additional resource types, see `AdvancedFieldSelector <https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_AdvancedFieldSelector.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-dataresource.html#cfn-cloudtrail-trail-dataresource-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def values(self) -> typing.Optional[typing.List[builtins.str]]:
            '''An array of Amazon Resource Name (ARN) strings or partial ARN strings for the specified resource type.

            - To log data events for all objects in all S3 buckets in your AWS account , specify the prefix as ``arn:aws:s3`` .

            .. epigraph::

               This also enables logging of data event activity performed by any user or role in your AWS account , even if that activity is performed on a bucket that belongs to another AWS account .

            - To log data events for all objects in an S3 bucket, specify the bucket and an empty object prefix such as ``arn:aws:s3:::bucket-1/`` . The trail logs data events for all objects in this S3 bucket.
            - To log data events for specific objects, specify the S3 bucket and object prefix such as ``arn:aws:s3:::bucket-1/example-images`` . The trail logs data events for objects in this S3 bucket that match the prefix.
            - To log data events for all Lambda functions in your AWS account , specify the prefix as ``arn:aws:lambda`` .

            .. epigraph::

               This also enables logging of ``Invoke`` activity performed by any user or role in your AWS account , even if that activity is performed on a function that belongs to another AWS account .

            - To log data events for a specific Lambda function, specify the function ARN.

            .. epigraph::

               Lambda function ARNs are exact. For example, if you specify a function ARN *arn:aws:lambda:us-west-2:111111111111:function:helloworld* , data events will only be logged for *arn:aws:lambda:us-west-2:111111111111:function:helloworld* . They will not be logged for *arn:aws:lambda:us-west-2:111111111111:function:helloworld2* .

            - To log data events for all DynamoDB tables in your AWS account , specify the prefix as ``arn:aws:dynamodb`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-dataresource.html#cfn-cloudtrail-trail-dataresource-values
            '''
            result = self._values.get("values")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cloudtrail.CfnTrail.EventSelectorProperty",
        jsii_struct_bases=[],
        name_mapping={
            "data_resources": "dataResources",
            "exclude_management_event_sources": "excludeManagementEventSources",
            "include_management_events": "includeManagementEvents",
            "read_write_type": "readWriteType",
        },
    )
    class EventSelectorProperty:
        def __init__(
            self,
            *,
            data_resources: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTrail.DataResourceProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            exclude_management_event_sources: typing.Optional[typing.Sequence[builtins.str]] = None,
            include_management_events: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            read_write_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Use event selectors to further specify the management and data event settings for your trail.

            By default, trails created without specific event selectors will be configured to log all read and write management events, and no data events. When an event occurs in your account, CloudTrail evaluates the event selector for all trails. For each trail, if the event matches any event selector, the trail processes and logs the event. If the event doesn't match any event selector, the trail doesn't log the event.

            You can configure up to five event selectors for a trail.

            You cannot apply both event selectors and advanced event selectors to a trail.

            :param data_resources: CloudTrail supports data event logging for Amazon S3 objects, AWS Lambda functions, and Amazon DynamoDB tables with basic event selectors. You can specify up to 250 resources for an individual event selector, but the total number of data resources cannot exceed 250 across all event selectors in a trail. This limit does not apply if you configure resource logging for all data events. For more information, see `Data Events <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html>`_ and `Limits in AWS CloudTrail <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/WhatIsCloudTrail-Limits.html>`_ in the *AWS CloudTrail User Guide* .
            :param exclude_management_event_sources: An optional list of service event sources from which you do not want management events to be logged on your trail. In this release, the list can be empty (disables the filter), or it can filter out AWS Key Management Service or Amazon RDS Data API events by containing ``kms.amazonaws.com`` or ``rdsdata.amazonaws.com`` . By default, ``ExcludeManagementEventSources`` is empty, and AWS KMS and Amazon RDS Data API events are logged to your trail. You can exclude management event sources only in Regions that support the event source.
            :param include_management_events: Specify if you want your event selector to include management events for your trail. For more information, see `Management Events <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.html>`_ in the *AWS CloudTrail User Guide* . By default, the value is ``true`` . The first copy of management events is free. You are charged for additional copies of management events that you are logging on any subsequent trail in the same Region. For more information about CloudTrail pricing, see `AWS CloudTrail Pricing <https://docs.aws.amazon.com/cloudtrail/pricing/>`_ .
            :param read_write_type: Specify if you want your trail to log read-only events, write-only events, or all. For example, the EC2 ``GetConsoleOutput`` is a read-only API operation and ``RunInstances`` is a write-only API operation. By default, the value is ``All`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-eventselector.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cloudtrail as cloudtrail
                
                event_selector_property = cloudtrail.CfnTrail.EventSelectorProperty(
                    data_resources=[cloudtrail.CfnTrail.DataResourceProperty(
                        type="type",
                
                        # the properties below are optional
                        values=["values"]
                    )],
                    exclude_management_event_sources=["excludeManagementEventSources"],
                    include_management_events=False,
                    read_write_type="readWriteType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b6a456b792eafca6f1c49386b9ce4f496975ac1ff51f363686c31755c3ba2007)
                check_type(argname="argument data_resources", value=data_resources, expected_type=type_hints["data_resources"])
                check_type(argname="argument exclude_management_event_sources", value=exclude_management_event_sources, expected_type=type_hints["exclude_management_event_sources"])
                check_type(argname="argument include_management_events", value=include_management_events, expected_type=type_hints["include_management_events"])
                check_type(argname="argument read_write_type", value=read_write_type, expected_type=type_hints["read_write_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if data_resources is not None:
                self._values["data_resources"] = data_resources
            if exclude_management_event_sources is not None:
                self._values["exclude_management_event_sources"] = exclude_management_event_sources
            if include_management_events is not None:
                self._values["include_management_events"] = include_management_events
            if read_write_type is not None:
                self._values["read_write_type"] = read_write_type

        @builtins.property
        def data_resources(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTrail.DataResourceProperty"]]]]:
            '''CloudTrail supports data event logging for Amazon S3 objects, AWS Lambda functions, and Amazon DynamoDB tables with basic event selectors.

            You can specify up to 250 resources for an individual event selector, but the total number of data resources cannot exceed 250 across all event selectors in a trail. This limit does not apply if you configure resource logging for all data events.

            For more information, see `Data Events <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html>`_ and `Limits in AWS CloudTrail <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/WhatIsCloudTrail-Limits.html>`_ in the *AWS CloudTrail User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-eventselector.html#cfn-cloudtrail-trail-eventselector-dataresources
            '''
            result = self._values.get("data_resources")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTrail.DataResourceProperty"]]]], result)

        @builtins.property
        def exclude_management_event_sources(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''An optional list of service event sources from which you do not want management events to be logged on your trail.

            In this release, the list can be empty (disables the filter), or it can filter out AWS Key Management Service or Amazon RDS Data API events by containing ``kms.amazonaws.com`` or ``rdsdata.amazonaws.com`` . By default, ``ExcludeManagementEventSources`` is empty, and AWS KMS and Amazon RDS Data API events are logged to your trail. You can exclude management event sources only in Regions that support the event source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-eventselector.html#cfn-cloudtrail-trail-eventselector-excludemanagementeventsources
            '''
            result = self._values.get("exclude_management_event_sources")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def include_management_events(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specify if you want your event selector to include management events for your trail.

            For more information, see `Management Events <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.html>`_ in the *AWS CloudTrail User Guide* .

            By default, the value is ``true`` .

            The first copy of management events is free. You are charged for additional copies of management events that you are logging on any subsequent trail in the same Region. For more information about CloudTrail pricing, see `AWS CloudTrail Pricing <https://docs.aws.amazon.com/cloudtrail/pricing/>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-eventselector.html#cfn-cloudtrail-trail-eventselector-includemanagementevents
            '''
            result = self._values.get("include_management_events")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def read_write_type(self) -> typing.Optional[builtins.str]:
            '''Specify if you want your trail to log read-only events, write-only events, or all.

            For example, the EC2 ``GetConsoleOutput`` is a read-only API operation and ``RunInstances`` is a write-only API operation.

            By default, the value is ``All`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-eventselector.html#cfn-cloudtrail-trail-eventselector-readwritetype
            '''
            result = self._values.get("read_write_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EventSelectorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cloudtrail.CfnTrail.InsightSelectorProperty",
        jsii_struct_bases=[],
        name_mapping={"insight_type": "insightType"},
    )
    class InsightSelectorProperty:
        def __init__(
            self,
            *,
            insight_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A JSON string that contains a list of Insights types that are logged on a trail.

            :param insight_type: The type of Insights events to log on a trail. ``ApiCallRateInsight`` and ``ApiErrorRateInsight`` are valid Insight types. The ``ApiCallRateInsight`` Insights type analyzes write-only management API calls that are aggregated per minute against a baseline API call volume. The ``ApiErrorRateInsight`` Insights type analyzes management API calls that result in error codes. The error is shown if the API call is unsuccessful.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-insightselector.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cloudtrail as cloudtrail
                
                insight_selector_property = cloudtrail.CfnTrail.InsightSelectorProperty(
                    insight_type="insightType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c36e7d325732c46967fd652ce7b5b56b5b548efaa4c260b4d0918a84e4b31748)
                check_type(argname="argument insight_type", value=insight_type, expected_type=type_hints["insight_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if insight_type is not None:
                self._values["insight_type"] = insight_type

        @builtins.property
        def insight_type(self) -> typing.Optional[builtins.str]:
            '''The type of Insights events to log on a trail. ``ApiCallRateInsight`` and ``ApiErrorRateInsight`` are valid Insight types.

            The ``ApiCallRateInsight`` Insights type analyzes write-only management API calls that are aggregated per minute against a baseline API call volume.

            The ``ApiErrorRateInsight`` Insights type analyzes management API calls that result in error codes. The error is shown if the API call is unsuccessful.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-insightselector.html#cfn-cloudtrail-trail-insightselector-insighttype
            '''
            result = self._values.get("insight_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InsightSelectorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudtrail.CfnTrailProps",
    jsii_struct_bases=[],
    name_mapping={
        "is_logging": "isLogging",
        "s3_bucket_name": "s3BucketName",
        "advanced_event_selectors": "advancedEventSelectors",
        "cloud_watch_logs_log_group_arn": "cloudWatchLogsLogGroupArn",
        "cloud_watch_logs_role_arn": "cloudWatchLogsRoleArn",
        "enable_log_file_validation": "enableLogFileValidation",
        "event_selectors": "eventSelectors",
        "include_global_service_events": "includeGlobalServiceEvents",
        "insight_selectors": "insightSelectors",
        "is_multi_region_trail": "isMultiRegionTrail",
        "is_organization_trail": "isOrganizationTrail",
        "kms_key_id": "kmsKeyId",
        "s3_key_prefix": "s3KeyPrefix",
        "sns_topic_name": "snsTopicName",
        "tags": "tags",
        "trail_name": "trailName",
    },
)
class CfnTrailProps:
    def __init__(
        self,
        *,
        is_logging: typing.Union[builtins.bool, _IResolvable_da3f097b],
        s3_bucket_name: builtins.str,
        advanced_event_selectors: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTrail.AdvancedEventSelectorProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        cloud_watch_logs_log_group_arn: typing.Optional[builtins.str] = None,
        cloud_watch_logs_role_arn: typing.Optional[builtins.str] = None,
        enable_log_file_validation: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        event_selectors: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTrail.EventSelectorProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        include_global_service_events: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        insight_selectors: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTrail.InsightSelectorProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        is_multi_region_trail: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        is_organization_trail: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        s3_key_prefix: typing.Optional[builtins.str] = None,
        sns_topic_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        trail_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnTrail``.

        :param is_logging: Whether the CloudTrail trail is currently logging AWS API calls.
        :param s3_bucket_name: Specifies the name of the Amazon S3 bucket designated for publishing log files. See `Amazon S3 Bucket naming rules <https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html>`_ .
        :param advanced_event_selectors: Specifies the settings for advanced event selectors. You can add advanced event selectors, and conditions for your advanced event selectors, up to a maximum of 500 values for all conditions and selectors on a trail. You can use either ``AdvancedEventSelectors`` or ``EventSelectors`` , but not both. If you apply ``AdvancedEventSelectors`` to a trail, any existing ``EventSelectors`` are overwritten. For more information about advanced event selectors, see `Logging data events <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html>`_ in the *AWS CloudTrail User Guide* .
        :param cloud_watch_logs_log_group_arn: Specifies a log group name using an Amazon Resource Name (ARN), a unique identifier that represents the log group to which CloudTrail logs are delivered. You must use a log group that exists in your account. Not required unless you specify ``CloudWatchLogsRoleArn`` .
        :param cloud_watch_logs_role_arn: Specifies the role for the CloudWatch Logs endpoint to assume to write to a user's log group. You must use a role that exists in your account.
        :param enable_log_file_validation: Specifies whether log file validation is enabled. The default is false. .. epigraph:: When you disable log file integrity validation, the chain of digest files is broken after one hour. CloudTrail does not create digest files for log files that were delivered during a period in which log file integrity validation was disabled. For example, if you enable log file integrity validation at noon on January 1, disable it at noon on January 2, and re-enable it at noon on January 10, digest files will not be created for the log files delivered from noon on January 2 to noon on January 10. The same applies whenever you stop CloudTrail logging or delete a trail.
        :param event_selectors: Use event selectors to further specify the management and data event settings for your trail. By default, trails created without specific event selectors will be configured to log all read and write management events, and no data events. When an event occurs in your account, CloudTrail evaluates the event selector for all trails. For each trail, if the event matches any event selector, the trail processes and logs the event. If the event doesn't match any event selector, the trail doesn't log the event. You can configure up to five event selectors for a trail. You cannot apply both event selectors and advanced event selectors to a trail.
        :param include_global_service_events: Specifies whether the trail is publishing events from global services such as IAM to the log files.
        :param insight_selectors: A JSON string that contains the Insights types you want to log on a trail. ``ApiCallRateInsight`` and ``ApiErrorRateInsight`` are valid Insight types. The ``ApiCallRateInsight`` Insights type analyzes write-only management API calls that are aggregated per minute against a baseline API call volume. The ``ApiErrorRateInsight`` Insights type analyzes management API calls that result in error codes. The error is shown if the API call is unsuccessful.
        :param is_multi_region_trail: Specifies whether the trail applies only to the current Region or to all Regions. The default is false. If the trail exists only in the current Region and this value is set to true, shadow trails (replications of the trail) will be created in the other Regions. If the trail exists in all Regions and this value is set to false, the trail will remain in the Region where it was created, and its shadow trails in other Regions will be deleted. As a best practice, consider using trails that log events in all Regions.
        :param is_organization_trail: Specifies whether the trail is applied to all accounts in an organization in AWS Organizations , or only for the current AWS account . The default is false, and cannot be true unless the call is made on behalf of an AWS account that is the management account for an organization in AWS Organizations . If the trail is not an organization trail and this is set to ``true`` , the trail will be created in all AWS accounts that belong to the organization. If the trail is an organization trail and this is set to ``false`` , the trail will remain in the current AWS account but be deleted from all member accounts in the organization. .. epigraph:: Only the management account for the organization can convert an organization trail to a non-organization trail, or convert a non-organization trail to an organization trail.
        :param kms_key_id: Specifies the AWS KMS key ID to use to encrypt the logs delivered by CloudTrail. The value can be an alias name prefixed by "alias/", a fully specified ARN to an alias, a fully specified ARN to a key, or a globally unique identifier. CloudTrail also supports AWS KMS multi-Region keys. For more information about multi-Region keys, see `Using multi-Region keys <https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html>`_ in the *AWS Key Management Service Developer Guide* . Examples: - alias/MyAliasName - arn:aws:kms:us-east-2:123456789012:alias/MyAliasName - arn:aws:kms:us-east-2:123456789012:key/12345678-1234-1234-1234-123456789012 - 12345678-1234-1234-1234-123456789012
        :param s3_key_prefix: Specifies the Amazon S3 key prefix that comes after the name of the bucket you have designated for log file delivery. For more information, see `Finding Your CloudTrail Log Files <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/get-and-view-cloudtrail-log-files.html#cloudtrail-find-log-files>`_ . The maximum length is 200 characters.
        :param sns_topic_name: Specifies the name of the Amazon SNS topic defined for notification of log file delivery. The maximum length is 256 characters.
        :param tags: A custom set of tags (key-value pairs) for this trail.
        :param trail_name: Specifies the name of the trail. The name must meet the following requirements:. - Contain only ASCII letters (a-z, A-Z), numbers (0-9), periods (.), underscores (_), or dashes (-) - Start with a letter or number, and end with a letter or number - Be between 3 and 128 characters - Have no adjacent periods, underscores or dashes. Names like ``my-_namespace`` and ``my--namespace`` are not valid. - Not be in IP address format (for example, 192.168.5.4)

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cloudtrail as cloudtrail
            
            cfn_trail_props = cloudtrail.CfnTrailProps(
                is_logging=False,
                s3_bucket_name="s3BucketName",
            
                # the properties below are optional
                advanced_event_selectors=[cloudtrail.CfnTrail.AdvancedEventSelectorProperty(
                    field_selectors=[cloudtrail.CfnTrail.AdvancedFieldSelectorProperty(
                        field="field",
            
                        # the properties below are optional
                        ends_with=["endsWith"],
                        equal_to=["equalTo"],
                        not_ends_with=["notEndsWith"],
                        not_equals=["notEquals"],
                        not_starts_with=["notStartsWith"],
                        starts_with=["startsWith"]
                    )],
            
                    # the properties below are optional
                    name="name"
                )],
                cloud_watch_logs_log_group_arn="cloudWatchLogsLogGroupArn",
                cloud_watch_logs_role_arn="cloudWatchLogsRoleArn",
                enable_log_file_validation=False,
                event_selectors=[cloudtrail.CfnTrail.EventSelectorProperty(
                    data_resources=[cloudtrail.CfnTrail.DataResourceProperty(
                        type="type",
            
                        # the properties below are optional
                        values=["values"]
                    )],
                    exclude_management_event_sources=["excludeManagementEventSources"],
                    include_management_events=False,
                    read_write_type="readWriteType"
                )],
                include_global_service_events=False,
                insight_selectors=[cloudtrail.CfnTrail.InsightSelectorProperty(
                    insight_type="insightType"
                )],
                is_multi_region_trail=False,
                is_organization_trail=False,
                kms_key_id="kmsKeyId",
                s3_key_prefix="s3KeyPrefix",
                sns_topic_name="snsTopicName",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                trail_name="trailName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe29eec9c2fc5386dadc73c14bab1f4c61dc9a7cd9ad26812bf169694fa1ed79)
            check_type(argname="argument is_logging", value=is_logging, expected_type=type_hints["is_logging"])
            check_type(argname="argument s3_bucket_name", value=s3_bucket_name, expected_type=type_hints["s3_bucket_name"])
            check_type(argname="argument advanced_event_selectors", value=advanced_event_selectors, expected_type=type_hints["advanced_event_selectors"])
            check_type(argname="argument cloud_watch_logs_log_group_arn", value=cloud_watch_logs_log_group_arn, expected_type=type_hints["cloud_watch_logs_log_group_arn"])
            check_type(argname="argument cloud_watch_logs_role_arn", value=cloud_watch_logs_role_arn, expected_type=type_hints["cloud_watch_logs_role_arn"])
            check_type(argname="argument enable_log_file_validation", value=enable_log_file_validation, expected_type=type_hints["enable_log_file_validation"])
            check_type(argname="argument event_selectors", value=event_selectors, expected_type=type_hints["event_selectors"])
            check_type(argname="argument include_global_service_events", value=include_global_service_events, expected_type=type_hints["include_global_service_events"])
            check_type(argname="argument insight_selectors", value=insight_selectors, expected_type=type_hints["insight_selectors"])
            check_type(argname="argument is_multi_region_trail", value=is_multi_region_trail, expected_type=type_hints["is_multi_region_trail"])
            check_type(argname="argument is_organization_trail", value=is_organization_trail, expected_type=type_hints["is_organization_trail"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            check_type(argname="argument s3_key_prefix", value=s3_key_prefix, expected_type=type_hints["s3_key_prefix"])
            check_type(argname="argument sns_topic_name", value=sns_topic_name, expected_type=type_hints["sns_topic_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument trail_name", value=trail_name, expected_type=type_hints["trail_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "is_logging": is_logging,
            "s3_bucket_name": s3_bucket_name,
        }
        if advanced_event_selectors is not None:
            self._values["advanced_event_selectors"] = advanced_event_selectors
        if cloud_watch_logs_log_group_arn is not None:
            self._values["cloud_watch_logs_log_group_arn"] = cloud_watch_logs_log_group_arn
        if cloud_watch_logs_role_arn is not None:
            self._values["cloud_watch_logs_role_arn"] = cloud_watch_logs_role_arn
        if enable_log_file_validation is not None:
            self._values["enable_log_file_validation"] = enable_log_file_validation
        if event_selectors is not None:
            self._values["event_selectors"] = event_selectors
        if include_global_service_events is not None:
            self._values["include_global_service_events"] = include_global_service_events
        if insight_selectors is not None:
            self._values["insight_selectors"] = insight_selectors
        if is_multi_region_trail is not None:
            self._values["is_multi_region_trail"] = is_multi_region_trail
        if is_organization_trail is not None:
            self._values["is_organization_trail"] = is_organization_trail
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if s3_key_prefix is not None:
            self._values["s3_key_prefix"] = s3_key_prefix
        if sns_topic_name is not None:
            self._values["sns_topic_name"] = sns_topic_name
        if tags is not None:
            self._values["tags"] = tags
        if trail_name is not None:
            self._values["trail_name"] = trail_name

    @builtins.property
    def is_logging(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
        '''Whether the CloudTrail trail is currently logging AWS API calls.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-islogging
        '''
        result = self._values.get("is_logging")
        assert result is not None, "Required property 'is_logging' is missing"
        return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

    @builtins.property
    def s3_bucket_name(self) -> builtins.str:
        '''Specifies the name of the Amazon S3 bucket designated for publishing log files.

        See `Amazon S3 Bucket naming rules <https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-s3bucketname
        '''
        result = self._values.get("s3_bucket_name")
        assert result is not None, "Required property 's3_bucket_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def advanced_event_selectors(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnTrail.AdvancedEventSelectorProperty]]]]:
        '''Specifies the settings for advanced event selectors.

        You can add advanced event selectors, and conditions for your advanced event selectors, up to a maximum of 500 values for all conditions and selectors on a trail. You can use either ``AdvancedEventSelectors`` or ``EventSelectors`` , but not both. If you apply ``AdvancedEventSelectors`` to a trail, any existing ``EventSelectors`` are overwritten. For more information about advanced event selectors, see `Logging data events <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html>`_ in the *AWS CloudTrail User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-advancedeventselectors
        '''
        result = self._values.get("advanced_event_selectors")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnTrail.AdvancedEventSelectorProperty]]]], result)

    @builtins.property
    def cloud_watch_logs_log_group_arn(self) -> typing.Optional[builtins.str]:
        '''Specifies a log group name using an Amazon Resource Name (ARN), a unique identifier that represents the log group to which CloudTrail logs are delivered.

        You must use a log group that exists in your account.

        Not required unless you specify ``CloudWatchLogsRoleArn`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-cloudwatchlogsloggrouparn
        '''
        result = self._values.get("cloud_watch_logs_log_group_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cloud_watch_logs_role_arn(self) -> typing.Optional[builtins.str]:
        '''Specifies the role for the CloudWatch Logs endpoint to assume to write to a user's log group.

        You must use a role that exists in your account.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-cloudwatchlogsrolearn
        '''
        result = self._values.get("cloud_watch_logs_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_log_file_validation(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether log file validation is enabled. The default is false.

        .. epigraph::

           When you disable log file integrity validation, the chain of digest files is broken after one hour. CloudTrail does not create digest files for log files that were delivered during a period in which log file integrity validation was disabled. For example, if you enable log file integrity validation at noon on January 1, disable it at noon on January 2, and re-enable it at noon on January 10, digest files will not be created for the log files delivered from noon on January 2 to noon on January 10. The same applies whenever you stop CloudTrail logging or delete a trail.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-enablelogfilevalidation
        '''
        result = self._values.get("enable_log_file_validation")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def event_selectors(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnTrail.EventSelectorProperty]]]]:
        '''Use event selectors to further specify the management and data event settings for your trail.

        By default, trails created without specific event selectors will be configured to log all read and write management events, and no data events. When an event occurs in your account, CloudTrail evaluates the event selector for all trails. For each trail, if the event matches any event selector, the trail processes and logs the event. If the event doesn't match any event selector, the trail doesn't log the event.

        You can configure up to five event selectors for a trail.

        You cannot apply both event selectors and advanced event selectors to a trail.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-eventselectors
        '''
        result = self._values.get("event_selectors")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnTrail.EventSelectorProperty]]]], result)

    @builtins.property
    def include_global_service_events(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether the trail is publishing events from global services such as IAM to the log files.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-includeglobalserviceevents
        '''
        result = self._values.get("include_global_service_events")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def insight_selectors(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnTrail.InsightSelectorProperty]]]]:
        '''A JSON string that contains the Insights types you want to log on a trail.

        ``ApiCallRateInsight`` and ``ApiErrorRateInsight`` are valid Insight types.

        The ``ApiCallRateInsight`` Insights type analyzes write-only management API calls that are aggregated per minute against a baseline API call volume.

        The ``ApiErrorRateInsight`` Insights type analyzes management API calls that result in error codes. The error is shown if the API call is unsuccessful.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-insightselectors
        '''
        result = self._values.get("insight_selectors")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnTrail.InsightSelectorProperty]]]], result)

    @builtins.property
    def is_multi_region_trail(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether the trail applies only to the current Region or to all Regions.

        The default is false. If the trail exists only in the current Region and this value is set to true, shadow trails (replications of the trail) will be created in the other Regions. If the trail exists in all Regions and this value is set to false, the trail will remain in the Region where it was created, and its shadow trails in other Regions will be deleted. As a best practice, consider using trails that log events in all Regions.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-ismultiregiontrail
        '''
        result = self._values.get("is_multi_region_trail")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def is_organization_trail(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether the trail is applied to all accounts in an organization in AWS Organizations , or only for the current AWS account .

        The default is false, and cannot be true unless the call is made on behalf of an AWS account that is the management account for an organization in AWS Organizations . If the trail is not an organization trail and this is set to ``true`` , the trail will be created in all AWS accounts that belong to the organization. If the trail is an organization trail and this is set to ``false`` , the trail will remain in the current AWS account but be deleted from all member accounts in the organization.
        .. epigraph::

           Only the management account for the organization can convert an organization trail to a non-organization trail, or convert a non-organization trail to an organization trail.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-isorganizationtrail
        '''
        result = self._values.get("is_organization_trail")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Specifies the AWS KMS key ID to use to encrypt the logs delivered by CloudTrail.

        The value can be an alias name prefixed by "alias/", a fully specified ARN to an alias, a fully specified ARN to a key, or a globally unique identifier.

        CloudTrail also supports AWS KMS multi-Region keys. For more information about multi-Region keys, see `Using multi-Region keys <https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html>`_ in the *AWS Key Management Service Developer Guide* .

        Examples:

        - alias/MyAliasName
        - arn:aws:kms:us-east-2:123456789012:alias/MyAliasName
        - arn:aws:kms:us-east-2:123456789012:key/12345678-1234-1234-1234-123456789012
        - 12345678-1234-1234-1234-123456789012

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-kmskeyid
        '''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def s3_key_prefix(self) -> typing.Optional[builtins.str]:
        '''Specifies the Amazon S3 key prefix that comes after the name of the bucket you have designated for log file delivery.

        For more information, see `Finding Your CloudTrail Log Files <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/get-and-view-cloudtrail-log-files.html#cloudtrail-find-log-files>`_ . The maximum length is 200 characters.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-s3keyprefix
        '''
        result = self._values.get("s3_key_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sns_topic_name(self) -> typing.Optional[builtins.str]:
        '''Specifies the name of the Amazon SNS topic defined for notification of log file delivery.

        The maximum length is 256 characters.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-snstopicname
        '''
        result = self._values.get("sns_topic_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A custom set of tags (key-value pairs) for this trail.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def trail_name(self) -> typing.Optional[builtins.str]:
        '''Specifies the name of the trail. The name must meet the following requirements:.

        - Contain only ASCII letters (a-z, A-Z), numbers (0-9), periods (.), underscores (_), or dashes (-)
        - Start with a letter or number, and end with a letter or number
        - Be between 3 and 128 characters
        - Have no adjacent periods, underscores or dashes. Names like ``my-_namespace`` and ``my--namespace`` are not valid.
        - Not be in IP address format (for example, 192.168.5.4)

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-trailname
        '''
        result = self._values.get("trail_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTrailProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_cloudtrail.DataResourceType")
class DataResourceType(enum.Enum):
    '''Resource type for a data event.'''

    LAMBDA_FUNCTION = "LAMBDA_FUNCTION"
    '''Data resource type for Lambda function.'''
    S3_OBJECT = "S3_OBJECT"
    '''Data resource type for S3 objects.'''


class InsightType(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudtrail.InsightType",
):
    '''Util element for InsightSelector.

    :exampleMetadata: infused

    Example::

        cloudtrail.Trail(self, "Insights",
            insight_types=[cloudtrail.InsightType.API_CALL_RATE, cloudtrail.InsightType.API_ERROR_RATE
            ]
        )
    '''

    def __init__(self, value: builtins.str) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1cb2fd9327becb7b11bbb80f00762b693b18c3d8338685289adc8907f8b2c231)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.create(self.__class__, self, [value])

    @jsii.python.classproperty
    @jsii.member(jsii_name="API_CALL_RATE")
    def API_CALL_RATE(cls) -> "InsightType":
        '''The type of insights to log on a trail.

        (API Call Rate)
        '''
        return typing.cast("InsightType", jsii.sget(cls, "API_CALL_RATE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="API_ERROR_RATE")
    def API_ERROR_RATE(cls) -> "InsightType":
        '''The type of insights to log on a trail.

        (API Error Rate)
        '''
        return typing.cast("InsightType", jsii.sget(cls, "API_ERROR_RATE"))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))


@jsii.enum(jsii_type="aws-cdk-lib.aws_cloudtrail.ManagementEventSources")
class ManagementEventSources(enum.Enum):
    '''Types of management event sources that can be excluded.'''

    KMS = "KMS"
    '''AWS Key Management Service (AWS KMS) events.'''
    RDS_DATA_API = "RDS_DATA_API"
    '''Data API events.'''


@jsii.enum(jsii_type="aws-cdk-lib.aws_cloudtrail.ReadWriteType")
class ReadWriteType(enum.Enum):
    '''Types of events that CloudTrail can log.

    :exampleMetadata: infused

    Example::

        trail = cloudtrail.Trail(self, "CloudTrail",
            # ...
            management_events=cloudtrail.ReadWriteType.READ_ONLY
        )
    '''

    READ_ONLY = "READ_ONLY"
    '''Read-only events include API operations that read your resources, but don't make changes.

    For example, read-only events include the Amazon EC2 DescribeSecurityGroups
    and DescribeSubnets API operations.
    '''
    WRITE_ONLY = "WRITE_ONLY"
    '''Write-only events include API operations that modify (or might modify) your resources.

    For example, the Amazon EC2 RunInstances and TerminateInstances API
    operations modify your instances.
    '''
    ALL = "ALL"
    '''All events.'''
    NONE = "NONE"
    '''No events.'''


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudtrail.S3EventSelector",
    jsii_struct_bases=[],
    name_mapping={"bucket": "bucket", "object_prefix": "objectPrefix"},
)
class S3EventSelector:
    def __init__(
        self,
        *,
        bucket: _IBucket_42e086fd,
        object_prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Selecting an S3 bucket and an optional prefix to be logged for data events.

        :param bucket: S3 bucket.
        :param object_prefix: Data events for objects whose key matches this prefix will be logged. Default: - all objects

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cloudtrail as cloudtrail
            from aws_cdk import aws_s3 as s3
            
            # bucket: s3.Bucket
            
            s3_event_selector = cloudtrail.S3EventSelector(
                bucket=bucket,
            
                # the properties below are optional
                object_prefix="objectPrefix"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d0df2bbec441689030ea9ec1ee0c490c06396957a77ed6d3353b714dbe525ea)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument object_prefix", value=object_prefix, expected_type=type_hints["object_prefix"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bucket": bucket,
        }
        if object_prefix is not None:
            self._values["object_prefix"] = object_prefix

    @builtins.property
    def bucket(self) -> _IBucket_42e086fd:
        '''S3 bucket.'''
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return typing.cast(_IBucket_42e086fd, result)

    @builtins.property
    def object_prefix(self) -> typing.Optional[builtins.str]:
        '''Data events for objects whose key matches this prefix will be logged.

        :default: - all objects
        '''
        result = self._values.get("object_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3EventSelector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Trail(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudtrail.Trail",
):
    '''Cloud trail allows you to log events that happen in your AWS account For example:.

    import { CloudTrail } from 'aws-cdk-lib/aws-cloudtrail'

    const cloudTrail = new CloudTrail(this, 'MyTrail');

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_cloudtrail as cloudtrail
        
        
        my_key_alias = kms.Alias.from_alias_name(self, "myKey", "alias/aws/s3")
        trail = cloudtrail.Trail(self, "myCloudTrail",
            send_to_cloud_watch_logs=True,
            encryption_key=my_key_alias
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        bucket: typing.Optional[_IBucket_42e086fd] = None,
        cloud_watch_log_group: typing.Optional[_ILogGroup_3c4fa718] = None,
        cloud_watch_logs_retention: typing.Optional[_RetentionDays_070f99f0] = None,
        enable_file_validation: typing.Optional[builtins.bool] = None,
        encryption_key: typing.Optional[_IKey_5f11635f] = None,
        include_global_service_events: typing.Optional[builtins.bool] = None,
        insight_types: typing.Optional[typing.Sequence[InsightType]] = None,
        is_multi_region_trail: typing.Optional[builtins.bool] = None,
        is_organization_trail: typing.Optional[builtins.bool] = None,
        management_events: typing.Optional[ReadWriteType] = None,
        org_id: typing.Optional[builtins.str] = None,
        s3_key_prefix: typing.Optional[builtins.str] = None,
        send_to_cloud_watch_logs: typing.Optional[builtins.bool] = None,
        sns_topic: typing.Optional[_ITopic_9eca4852] = None,
        trail_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param bucket: The Amazon S3 bucket. Default: - if not supplied a bucket will be created with all the correct permisions
        :param cloud_watch_log_group: Log Group to which CloudTrail to push logs to. Ignored if sendToCloudWatchLogs is set to false. Default: - a new log group is created and used.
        :param cloud_watch_logs_retention: How long to retain logs in CloudWatchLogs. Ignored if sendToCloudWatchLogs is false or if cloudWatchLogGroup is set. Default: logs.RetentionDays.ONE_YEAR
        :param enable_file_validation: To determine whether a log file was modified, deleted, or unchanged after CloudTrail delivered it, you can use CloudTrail log file integrity validation. This feature is built using industry standard algorithms: SHA-256 for hashing and SHA-256 with RSA for digital signing. This makes it computationally infeasible to modify, delete or forge CloudTrail log files without detection. You can use the AWS CLI to validate the files in the location where CloudTrail delivered them. Default: true
        :param encryption_key: The AWS Key Management Service (AWS KMS) key ID that you want to use to encrypt CloudTrail logs. Default: - No encryption.
        :param include_global_service_events: For most services, events are recorded in the region where the action occurred. For global services such as AWS Identity and Access Management (IAM), AWS STS, Amazon CloudFront, and Route 53, events are delivered to any trail that includes global services, and are logged as occurring in US East (N. Virginia) Region. Default: true
        :param insight_types: A JSON string that contains the insight types you want to log on a trail. Default: - No Value.
        :param is_multi_region_trail: Whether or not this trail delivers log files from multiple regions to a single S3 bucket for a single account. Default: true
        :param is_organization_trail: Specifies whether the trail is applied to all accounts in an organization in AWS Organizations, or only for the current AWS account. If this is set to true then the current account *must* be the management account. If it is not, then CloudFormation will throw an error. If this is set to true and the current account is a management account for an organization in AWS Organizations, the trail will be created in all AWS accounts that belong to the organization. If this is set to false, the trail will remain in the current AWS account but be deleted from all member accounts in the organization. Default: - false
        :param management_events: When an event occurs in your account, CloudTrail evaluates whether the event matches the settings for your trails. Only events that match your trail settings are delivered to your Amazon S3 bucket and Amazon CloudWatch Logs log group. This method sets the management configuration for this trail. Management events provide insight into management operations that are performed on resources in your AWS account. These are also known as control plane operations. Management events can also include non-API events that occur in your account. For example, when a user logs in to your account, CloudTrail logs the ConsoleLogin event. Default: ReadWriteType.ALL
        :param org_id: The orgId. Required when ``isOrganizationTrail`` is set to true to attach the necessary permissions. Default: - No orgId
        :param s3_key_prefix: An Amazon S3 object key prefix that precedes the name of all log files. Default: - No prefix.
        :param send_to_cloud_watch_logs: If CloudTrail pushes logs to CloudWatch Logs in addition to S3. Disabled for cost out of the box. Default: false
        :param sns_topic: SNS topic that is notified when new log files are published. Default: - No notifications.
        :param trail_name: The name of the trail. We recommend customers do not set an explicit name. Default: - AWS CloudFormation generated name.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b48a378f80b4a1726c79900e866bb932a0819e2b9124d6c5818259bf8c2efd3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = TrailProps(
            bucket=bucket,
            cloud_watch_log_group=cloud_watch_log_group,
            cloud_watch_logs_retention=cloud_watch_logs_retention,
            enable_file_validation=enable_file_validation,
            encryption_key=encryption_key,
            include_global_service_events=include_global_service_events,
            insight_types=insight_types,
            is_multi_region_trail=is_multi_region_trail,
            is_organization_trail=is_organization_trail,
            management_events=management_events,
            org_id=org_id,
            s3_key_prefix=s3_key_prefix,
            send_to_cloud_watch_logs=send_to_cloud_watch_logs,
            sns_topic=sns_topic,
            trail_name=trail_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="onEvent")
    @builtins.classmethod
    def on_event(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        target: typing.Optional[_IRuleTarget_7a91f454] = None,
        cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
        rule_name: typing.Optional[builtins.str] = None,
    ) -> _Rule_334ed2b5:
        '''Create an event rule for when an event is recorded by any Trail in the account.

        Note that the event doesn't necessarily have to come from this Trail, it can
        be captured from any one.

        Be sure to filter the event further down using an event pattern.

        :param scope: -
        :param id: -
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        :param cross_stack_scope: The scope to use if the source of the rule and its target are in different Stacks (but in the same account & region). This helps dealing with cycles that often arise in these situations. Default: - none (the main scope will be used, even for cross-stack Events)
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3da7eec1f43e2097945d61dbe36980d815e286492252afbfa5b77f6f90154c3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = _OnEventOptions_8711b8b3(
            target=target,
            cross_stack_scope=cross_stack_scope,
            description=description,
            event_pattern=event_pattern,
            rule_name=rule_name,
        )

        return typing.cast(_Rule_334ed2b5, jsii.sinvoke(cls, "onEvent", [scope, id, options]))

    @jsii.member(jsii_name="addEventSelector")
    def add_event_selector(
        self,
        data_resource_type: DataResourceType,
        data_resource_values: typing.Sequence[builtins.str],
        *,
        exclude_management_event_sources: typing.Optional[typing.Sequence[ManagementEventSources]] = None,
        include_management_events: typing.Optional[builtins.bool] = None,
        read_write_type: typing.Optional[ReadWriteType] = None,
    ) -> None:
        '''When an event occurs in your account, CloudTrail evaluates whether the event matches the settings for your trails.

        Only events that match your trail settings are delivered to your Amazon S3 bucket and Amazon CloudWatch Logs log group.

        This method adds an Event Selector for filtering events that match either S3 or Lambda function operations.

        Data events: These events provide insight into the resource operations performed on or within a resource.
        These are also known as data plane operations.

        :param data_resource_type: -
        :param data_resource_values: the list of data resource ARNs to include in logging (maximum 250 entries).
        :param exclude_management_event_sources: An optional list of service event sources from which you do not want management events to be logged on your trail. Default: []
        :param include_management_events: Specifies whether the event selector includes management events for the trail. Default: true
        :param read_write_type: Specifies whether to log read-only events, write-only events, or all events. Default: ReadWriteType.All
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a83bd81f5369dec88236698aaaacd2b411e71f0b26a1820dac4d9708b35eeb2)
            check_type(argname="argument data_resource_type", value=data_resource_type, expected_type=type_hints["data_resource_type"])
            check_type(argname="argument data_resource_values", value=data_resource_values, expected_type=type_hints["data_resource_values"])
        options = AddEventSelectorOptions(
            exclude_management_event_sources=exclude_management_event_sources,
            include_management_events=include_management_events,
            read_write_type=read_write_type,
        )

        return typing.cast(None, jsii.invoke(self, "addEventSelector", [data_resource_type, data_resource_values, options]))

    @jsii.member(jsii_name="addLambdaEventSelector")
    def add_lambda_event_selector(
        self,
        handlers: typing.Sequence[_IFunction_6adb0ab8],
        *,
        exclude_management_event_sources: typing.Optional[typing.Sequence[ManagementEventSources]] = None,
        include_management_events: typing.Optional[builtins.bool] = None,
        read_write_type: typing.Optional[ReadWriteType] = None,
    ) -> None:
        '''When an event occurs in your account, CloudTrail evaluates whether the event matches the settings for your trails.

        Only events that match your trail settings are delivered to your Amazon S3 bucket and Amazon CloudWatch Logs log group.

        This method adds a Lambda Data Event Selector for filtering events that match Lambda function operations.

        Data events: These events provide insight into the resource operations performed on or within a resource.
        These are also known as data plane operations.

        :param handlers: the list of lambda function handlers whose data events should be logged (maximum 250 entries).
        :param exclude_management_event_sources: An optional list of service event sources from which you do not want management events to be logged on your trail. Default: []
        :param include_management_events: Specifies whether the event selector includes management events for the trail. Default: true
        :param read_write_type: Specifies whether to log read-only events, write-only events, or all events. Default: ReadWriteType.All
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4c1abc3131dbd715c5dbbad63c8d79ef1bb110ded697e9202e474e8c0766da0)
            check_type(argname="argument handlers", value=handlers, expected_type=type_hints["handlers"])
        options = AddEventSelectorOptions(
            exclude_management_event_sources=exclude_management_event_sources,
            include_management_events=include_management_events,
            read_write_type=read_write_type,
        )

        return typing.cast(None, jsii.invoke(self, "addLambdaEventSelector", [handlers, options]))

    @jsii.member(jsii_name="addS3EventSelector")
    def add_s3_event_selector(
        self,
        s3_selector: typing.Sequence[typing.Union[S3EventSelector, typing.Dict[builtins.str, typing.Any]]],
        *,
        exclude_management_event_sources: typing.Optional[typing.Sequence[ManagementEventSources]] = None,
        include_management_events: typing.Optional[builtins.bool] = None,
        read_write_type: typing.Optional[ReadWriteType] = None,
    ) -> None:
        '''When an event occurs in your account, CloudTrail evaluates whether the event matches the settings for your trails.

        Only events that match your trail settings are delivered to your Amazon S3 bucket and Amazon CloudWatch Logs log group.

        This method adds an S3 Data Event Selector for filtering events that match S3 operations.

        Data events: These events provide insight into the resource operations performed on or within a resource.
        These are also known as data plane operations.

        :param s3_selector: the list of S3 bucket with optional prefix to include in logging (maximum 250 entries).
        :param exclude_management_event_sources: An optional list of service event sources from which you do not want management events to be logged on your trail. Default: []
        :param include_management_events: Specifies whether the event selector includes management events for the trail. Default: true
        :param read_write_type: Specifies whether to log read-only events, write-only events, or all events. Default: ReadWriteType.All
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4675fde35c881f97ed3c098123c51ad64ff5ae73a4d353d16fd977d9951fefb2)
            check_type(argname="argument s3_selector", value=s3_selector, expected_type=type_hints["s3_selector"])
        options = AddEventSelectorOptions(
            exclude_management_event_sources=exclude_management_event_sources,
            include_management_events=include_management_events,
            read_write_type=read_write_type,
        )

        return typing.cast(None, jsii.invoke(self, "addS3EventSelector", [s3_selector, options]))

    @jsii.member(jsii_name="logAllLambdaDataEvents")
    def log_all_lambda_data_events(
        self,
        *,
        exclude_management_event_sources: typing.Optional[typing.Sequence[ManagementEventSources]] = None,
        include_management_events: typing.Optional[builtins.bool] = None,
        read_write_type: typing.Optional[ReadWriteType] = None,
    ) -> None:
        '''Log all Lambda data events for all lambda functions the account.

        :param exclude_management_event_sources: An optional list of service event sources from which you do not want management events to be logged on your trail. Default: []
        :param include_management_events: Specifies whether the event selector includes management events for the trail. Default: true
        :param read_write_type: Specifies whether to log read-only events, write-only events, or all events. Default: ReadWriteType.All

        :default: false

        :see: https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html
        '''
        options = AddEventSelectorOptions(
            exclude_management_event_sources=exclude_management_event_sources,
            include_management_events=include_management_events,
            read_write_type=read_write_type,
        )

        return typing.cast(None, jsii.invoke(self, "logAllLambdaDataEvents", [options]))

    @jsii.member(jsii_name="logAllS3DataEvents")
    def log_all_s3_data_events(
        self,
        *,
        exclude_management_event_sources: typing.Optional[typing.Sequence[ManagementEventSources]] = None,
        include_management_events: typing.Optional[builtins.bool] = None,
        read_write_type: typing.Optional[ReadWriteType] = None,
    ) -> None:
        '''Log all S3 data events for all objects for all buckets in the account.

        :param exclude_management_event_sources: An optional list of service event sources from which you do not want management events to be logged on your trail. Default: []
        :param include_management_events: Specifies whether the event selector includes management events for the trail. Default: true
        :param read_write_type: Specifies whether to log read-only events, write-only events, or all events. Default: ReadWriteType.All

        :default: false

        :see: https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html
        '''
        options = AddEventSelectorOptions(
            exclude_management_event_sources=exclude_management_event_sources,
            include_management_events=include_management_events,
            read_write_type=read_write_type,
        )

        return typing.cast(None, jsii.invoke(self, "logAllS3DataEvents", [options]))

    @builtins.property
    @jsii.member(jsii_name="trailArn")
    def trail_arn(self) -> builtins.str:
        '''ARN of the CloudTrail trail i.e. arn:aws:cloudtrail:us-east-2:123456789012:trail/myCloudTrail.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "trailArn"))

    @builtins.property
    @jsii.member(jsii_name="trailSnsTopicArn")
    def trail_sns_topic_arn(self) -> builtins.str:
        '''ARN of the Amazon SNS topic that's associated with the CloudTrail trail, i.e. arn:aws:sns:us-east-2:123456789012:mySNSTopic.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "trailSnsTopicArn"))

    @builtins.property
    @jsii.member(jsii_name="logGroup")
    def log_group(self) -> typing.Optional[_ILogGroup_3c4fa718]:
        '''The CloudWatch log group to which CloudTrail events are sent.

        ``undefined`` if ``sendToCloudWatchLogs`` property is false.
        '''
        return typing.cast(typing.Optional[_ILogGroup_3c4fa718], jsii.get(self, "logGroup"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudtrail.TrailProps",
    jsii_struct_bases=[],
    name_mapping={
        "bucket": "bucket",
        "cloud_watch_log_group": "cloudWatchLogGroup",
        "cloud_watch_logs_retention": "cloudWatchLogsRetention",
        "enable_file_validation": "enableFileValidation",
        "encryption_key": "encryptionKey",
        "include_global_service_events": "includeGlobalServiceEvents",
        "insight_types": "insightTypes",
        "is_multi_region_trail": "isMultiRegionTrail",
        "is_organization_trail": "isOrganizationTrail",
        "management_events": "managementEvents",
        "org_id": "orgId",
        "s3_key_prefix": "s3KeyPrefix",
        "send_to_cloud_watch_logs": "sendToCloudWatchLogs",
        "sns_topic": "snsTopic",
        "trail_name": "trailName",
    },
)
class TrailProps:
    def __init__(
        self,
        *,
        bucket: typing.Optional[_IBucket_42e086fd] = None,
        cloud_watch_log_group: typing.Optional[_ILogGroup_3c4fa718] = None,
        cloud_watch_logs_retention: typing.Optional[_RetentionDays_070f99f0] = None,
        enable_file_validation: typing.Optional[builtins.bool] = None,
        encryption_key: typing.Optional[_IKey_5f11635f] = None,
        include_global_service_events: typing.Optional[builtins.bool] = None,
        insight_types: typing.Optional[typing.Sequence[InsightType]] = None,
        is_multi_region_trail: typing.Optional[builtins.bool] = None,
        is_organization_trail: typing.Optional[builtins.bool] = None,
        management_events: typing.Optional[ReadWriteType] = None,
        org_id: typing.Optional[builtins.str] = None,
        s3_key_prefix: typing.Optional[builtins.str] = None,
        send_to_cloud_watch_logs: typing.Optional[builtins.bool] = None,
        sns_topic: typing.Optional[_ITopic_9eca4852] = None,
        trail_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for an AWS CloudTrail trail.

        :param bucket: The Amazon S3 bucket. Default: - if not supplied a bucket will be created with all the correct permisions
        :param cloud_watch_log_group: Log Group to which CloudTrail to push logs to. Ignored if sendToCloudWatchLogs is set to false. Default: - a new log group is created and used.
        :param cloud_watch_logs_retention: How long to retain logs in CloudWatchLogs. Ignored if sendToCloudWatchLogs is false or if cloudWatchLogGroup is set. Default: logs.RetentionDays.ONE_YEAR
        :param enable_file_validation: To determine whether a log file was modified, deleted, or unchanged after CloudTrail delivered it, you can use CloudTrail log file integrity validation. This feature is built using industry standard algorithms: SHA-256 for hashing and SHA-256 with RSA for digital signing. This makes it computationally infeasible to modify, delete or forge CloudTrail log files without detection. You can use the AWS CLI to validate the files in the location where CloudTrail delivered them. Default: true
        :param encryption_key: The AWS Key Management Service (AWS KMS) key ID that you want to use to encrypt CloudTrail logs. Default: - No encryption.
        :param include_global_service_events: For most services, events are recorded in the region where the action occurred. For global services such as AWS Identity and Access Management (IAM), AWS STS, Amazon CloudFront, and Route 53, events are delivered to any trail that includes global services, and are logged as occurring in US East (N. Virginia) Region. Default: true
        :param insight_types: A JSON string that contains the insight types you want to log on a trail. Default: - No Value.
        :param is_multi_region_trail: Whether or not this trail delivers log files from multiple regions to a single S3 bucket for a single account. Default: true
        :param is_organization_trail: Specifies whether the trail is applied to all accounts in an organization in AWS Organizations, or only for the current AWS account. If this is set to true then the current account *must* be the management account. If it is not, then CloudFormation will throw an error. If this is set to true and the current account is a management account for an organization in AWS Organizations, the trail will be created in all AWS accounts that belong to the organization. If this is set to false, the trail will remain in the current AWS account but be deleted from all member accounts in the organization. Default: - false
        :param management_events: When an event occurs in your account, CloudTrail evaluates whether the event matches the settings for your trails. Only events that match your trail settings are delivered to your Amazon S3 bucket and Amazon CloudWatch Logs log group. This method sets the management configuration for this trail. Management events provide insight into management operations that are performed on resources in your AWS account. These are also known as control plane operations. Management events can also include non-API events that occur in your account. For example, when a user logs in to your account, CloudTrail logs the ConsoleLogin event. Default: ReadWriteType.ALL
        :param org_id: The orgId. Required when ``isOrganizationTrail`` is set to true to attach the necessary permissions. Default: - No orgId
        :param s3_key_prefix: An Amazon S3 object key prefix that precedes the name of all log files. Default: - No prefix.
        :param send_to_cloud_watch_logs: If CloudTrail pushes logs to CloudWatch Logs in addition to S3. Disabled for cost out of the box. Default: false
        :param sns_topic: SNS topic that is notified when new log files are published. Default: - No notifications.
        :param trail_name: The name of the trail. We recommend customers do not set an explicit name. Default: - AWS CloudFormation generated name.

        :exampleMetadata: infused

        Example::

            trail = cloudtrail.Trail(self, "CloudTrail",
                # ...
                management_events=cloudtrail.ReadWriteType.READ_ONLY
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5ff27b267882181cdb7a08f4ac78fe9eaffb7f3b50db3ce4f2dc9ce929af6f7)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument cloud_watch_log_group", value=cloud_watch_log_group, expected_type=type_hints["cloud_watch_log_group"])
            check_type(argname="argument cloud_watch_logs_retention", value=cloud_watch_logs_retention, expected_type=type_hints["cloud_watch_logs_retention"])
            check_type(argname="argument enable_file_validation", value=enable_file_validation, expected_type=type_hints["enable_file_validation"])
            check_type(argname="argument encryption_key", value=encryption_key, expected_type=type_hints["encryption_key"])
            check_type(argname="argument include_global_service_events", value=include_global_service_events, expected_type=type_hints["include_global_service_events"])
            check_type(argname="argument insight_types", value=insight_types, expected_type=type_hints["insight_types"])
            check_type(argname="argument is_multi_region_trail", value=is_multi_region_trail, expected_type=type_hints["is_multi_region_trail"])
            check_type(argname="argument is_organization_trail", value=is_organization_trail, expected_type=type_hints["is_organization_trail"])
            check_type(argname="argument management_events", value=management_events, expected_type=type_hints["management_events"])
            check_type(argname="argument org_id", value=org_id, expected_type=type_hints["org_id"])
            check_type(argname="argument s3_key_prefix", value=s3_key_prefix, expected_type=type_hints["s3_key_prefix"])
            check_type(argname="argument send_to_cloud_watch_logs", value=send_to_cloud_watch_logs, expected_type=type_hints["send_to_cloud_watch_logs"])
            check_type(argname="argument sns_topic", value=sns_topic, expected_type=type_hints["sns_topic"])
            check_type(argname="argument trail_name", value=trail_name, expected_type=type_hints["trail_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if bucket is not None:
            self._values["bucket"] = bucket
        if cloud_watch_log_group is not None:
            self._values["cloud_watch_log_group"] = cloud_watch_log_group
        if cloud_watch_logs_retention is not None:
            self._values["cloud_watch_logs_retention"] = cloud_watch_logs_retention
        if enable_file_validation is not None:
            self._values["enable_file_validation"] = enable_file_validation
        if encryption_key is not None:
            self._values["encryption_key"] = encryption_key
        if include_global_service_events is not None:
            self._values["include_global_service_events"] = include_global_service_events
        if insight_types is not None:
            self._values["insight_types"] = insight_types
        if is_multi_region_trail is not None:
            self._values["is_multi_region_trail"] = is_multi_region_trail
        if is_organization_trail is not None:
            self._values["is_organization_trail"] = is_organization_trail
        if management_events is not None:
            self._values["management_events"] = management_events
        if org_id is not None:
            self._values["org_id"] = org_id
        if s3_key_prefix is not None:
            self._values["s3_key_prefix"] = s3_key_prefix
        if send_to_cloud_watch_logs is not None:
            self._values["send_to_cloud_watch_logs"] = send_to_cloud_watch_logs
        if sns_topic is not None:
            self._values["sns_topic"] = sns_topic
        if trail_name is not None:
            self._values["trail_name"] = trail_name

    @builtins.property
    def bucket(self) -> typing.Optional[_IBucket_42e086fd]:
        '''The Amazon S3 bucket.

        :default: - if not supplied a bucket will be created with all the correct permisions
        '''
        result = self._values.get("bucket")
        return typing.cast(typing.Optional[_IBucket_42e086fd], result)

    @builtins.property
    def cloud_watch_log_group(self) -> typing.Optional[_ILogGroup_3c4fa718]:
        '''Log Group to which CloudTrail to push logs to.

        Ignored if sendToCloudWatchLogs is set to false.

        :default: - a new log group is created and used.
        '''
        result = self._values.get("cloud_watch_log_group")
        return typing.cast(typing.Optional[_ILogGroup_3c4fa718], result)

    @builtins.property
    def cloud_watch_logs_retention(self) -> typing.Optional[_RetentionDays_070f99f0]:
        '''How long to retain logs in CloudWatchLogs.

        Ignored if sendToCloudWatchLogs is false or if cloudWatchLogGroup is set.

        :default: logs.RetentionDays.ONE_YEAR
        '''
        result = self._values.get("cloud_watch_logs_retention")
        return typing.cast(typing.Optional[_RetentionDays_070f99f0], result)

    @builtins.property
    def enable_file_validation(self) -> typing.Optional[builtins.bool]:
        '''To determine whether a log file was modified, deleted, or unchanged after CloudTrail delivered it, you can use CloudTrail log file integrity validation.

        This feature is built using industry standard algorithms: SHA-256 for hashing and SHA-256 with RSA for digital signing.
        This makes it computationally infeasible to modify, delete or forge CloudTrail log files without detection.
        You can use the AWS CLI to validate the files in the location where CloudTrail delivered them.

        :default: true
        '''
        result = self._values.get("enable_file_validation")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def encryption_key(self) -> typing.Optional[_IKey_5f11635f]:
        '''The AWS Key Management Service (AWS KMS) key ID that you want to use to encrypt CloudTrail logs.

        :default: - No encryption.
        '''
        result = self._values.get("encryption_key")
        return typing.cast(typing.Optional[_IKey_5f11635f], result)

    @builtins.property
    def include_global_service_events(self) -> typing.Optional[builtins.bool]:
        '''For most services, events are recorded in the region where the action occurred.

        For global services such as AWS Identity and Access Management (IAM), AWS STS, Amazon CloudFront, and Route 53,
        events are delivered to any trail that includes global services, and are logged as occurring in US East (N. Virginia) Region.

        :default: true
        '''
        result = self._values.get("include_global_service_events")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def insight_types(self) -> typing.Optional[typing.List[InsightType]]:
        '''A JSON string that contains the insight types you want to log on a trail.

        :default: - No Value.
        '''
        result = self._values.get("insight_types")
        return typing.cast(typing.Optional[typing.List[InsightType]], result)

    @builtins.property
    def is_multi_region_trail(self) -> typing.Optional[builtins.bool]:
        '''Whether or not this trail delivers log files from multiple regions to a single S3 bucket for a single account.

        :default: true
        '''
        result = self._values.get("is_multi_region_trail")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def is_organization_trail(self) -> typing.Optional[builtins.bool]:
        '''Specifies whether the trail is applied to all accounts in an organization in AWS Organizations, or only for the current AWS account.

        If this is set to true then the current account *must* be the management account. If it is not, then CloudFormation will throw an error.

        If this is set to true and the current account is a management account for an organization in AWS Organizations, the trail will be created in all AWS accounts that belong to the organization.
        If this is set to false, the trail will remain in the current AWS account but be deleted from all member accounts in the organization.

        :default: - false
        '''
        result = self._values.get("is_organization_trail")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def management_events(self) -> typing.Optional[ReadWriteType]:
        '''When an event occurs in your account, CloudTrail evaluates whether the event matches the settings for your trails.

        Only events that match your trail settings are delivered to your Amazon S3 bucket and Amazon CloudWatch Logs log group.

        This method sets the management configuration for this trail.

        Management events provide insight into management operations that are performed on resources in your AWS account.
        These are also known as control plane operations.
        Management events can also include non-API events that occur in your account.
        For example, when a user logs in to your account, CloudTrail logs the ConsoleLogin event.

        :default: ReadWriteType.ALL
        '''
        result = self._values.get("management_events")
        return typing.cast(typing.Optional[ReadWriteType], result)

    @builtins.property
    def org_id(self) -> typing.Optional[builtins.str]:
        '''The orgId.

        Required when ``isOrganizationTrail`` is set to true to attach the necessary permissions.

        :default: - No orgId
        '''
        result = self._values.get("org_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def s3_key_prefix(self) -> typing.Optional[builtins.str]:
        '''An Amazon S3 object key prefix that precedes the name of all log files.

        :default: - No prefix.
        '''
        result = self._values.get("s3_key_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def send_to_cloud_watch_logs(self) -> typing.Optional[builtins.bool]:
        '''If CloudTrail pushes logs to CloudWatch Logs in addition to S3.

        Disabled for cost out of the box.

        :default: false
        '''
        result = self._values.get("send_to_cloud_watch_logs")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def sns_topic(self) -> typing.Optional[_ITopic_9eca4852]:
        '''SNS topic that is notified when new log files are published.

        :default: - No notifications.
        '''
        result = self._values.get("sns_topic")
        return typing.cast(typing.Optional[_ITopic_9eca4852], result)

    @builtins.property
    def trail_name(self) -> typing.Optional[builtins.str]:
        '''The name of the trail.

        We recommend customers do not set an explicit name.

        :default: - AWS CloudFormation generated name.
        '''
        result = self._values.get("trail_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TrailProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AddEventSelectorOptions",
    "CfnChannel",
    "CfnChannelProps",
    "CfnEventDataStore",
    "CfnEventDataStoreProps",
    "CfnResourcePolicy",
    "CfnResourcePolicyProps",
    "CfnTrail",
    "CfnTrailProps",
    "DataResourceType",
    "InsightType",
    "ManagementEventSources",
    "ReadWriteType",
    "S3EventSelector",
    "Trail",
    "TrailProps",
]

publication.publish()

def _typecheckingstub__73fc595c7387ed1256397f5af21fd7ee999ae00a4ffd0d01a01810f05f0a7ae5(
    *,
    exclude_management_event_sources: typing.Optional[typing.Sequence[ManagementEventSources]] = None,
    include_management_events: typing.Optional[builtins.bool] = None,
    read_write_type: typing.Optional[ReadWriteType] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4004ebed14c16ae6f20ecf5d65ea8487ea49b0bd7c3ce35ca361518f9fec0fa6(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    destinations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnChannel.DestinationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    name: typing.Optional[builtins.str] = None,
    source: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12052607593ad96dcef135d212789e6caf3b7f7cd49c9ce2468646f9efbcb963(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd31f5742125109282b44493267cb4e1405b919ba97bb1b7f18668a0624611e2(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af90446cbf2dae59bef52fb3ee6ec0e5b9c6098eff5af75a5963dd51c4683a5e(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnChannel.DestinationProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f6f560b40b7326691d9bf63d6ea7b8ad77377af3911f812fa5d243141752b34(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63777c16355eca1495edc2932fdadb55a7e3c86d73124f1d93d1c28b2ad64ee7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29044cfd0c28f00acd85e04beb454a19a2c4d87d4786f0af019f0209c639da8b(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__619b701f7c6b5470537230c8a847919a410a57fbf2eab022694dc1fef7b41c92(
    *,
    location: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__767e83e8a394410f21e7f497da1effaf3ef0c04f6e829362db73a8f535dd5356(
    *,
    destinations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnChannel.DestinationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    name: typing.Optional[builtins.str] = None,
    source: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__058a94222b13ad44b4607ad5932ec9b6a2defcb250ff436576e6e8976e7b2bee(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    advanced_event_selectors: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEventDataStore.AdvancedEventSelectorProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    billing_mode: typing.Optional[builtins.str] = None,
    federation_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    federation_role_arn: typing.Optional[builtins.str] = None,
    ingestion_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    insights_destination: typing.Optional[builtins.str] = None,
    insight_selectors: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEventDataStore.InsightSelectorProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    multi_region_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    name: typing.Optional[builtins.str] = None,
    organization_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    retention_period: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    termination_protection_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21862a9cccdc40ba09d15f004dcda554d20814b630b70c51ae59a1212bbb14c4(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ee95efcc007233c035a77dfd382e47456926b86a000891448961781bff2a95e(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7bc51d9a1ef5affc48ffb624785b29a7a5d0a3eba5e72b94f687da94194f4973(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnEventDataStore.AdvancedEventSelectorProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__106939491635761bff083d6af3ca26d1723f9df71ec433399c5746554b88e334(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__765513d5a073b76962f766e5dc1a967c4ad42a5bb2200d9f880aac945789b35d(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02d5876fb281f125b4a84c7554b6ae992b9b7433cab839d402d60601a9872704(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3120b4fc57c151f577843e6f55242684964162de4d4061991c82480a0fae581b(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d10aa59d5d60b5a68edf57d8df52934e03f5e4f0802a1d7dab4552592f2ee609(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b360ff34d6b267287ccf6e4c636b401ab6c739c7a90856639462b1c738855c92(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnEventDataStore.InsightSelectorProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2945b7a3d4af202bf1a8d8550ce4b17a1ab219e4dd829832fc9bd51a53c69b0(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69742230d7479a5e2d180046d6dbe2ea4627b1fbe6861d248e8fa77f7c0dcd20(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a01c2b1ec1e4ebac8e9e92744ee1402309ee4033c2267e1089f605b125f4b192(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__565712bf828bb8c2b0f6a80ca025d431aa72043d60fff9a95e02336f6f1e0d1c(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9508e34267838b75568905c8769ff7999130a13cb85b3d1abf67ef17b5958102(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6acb86a62af0621d981781f78b5611035089e25ca1472411f75d1b6e352ead2(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f57ea7bcecd4a4cd58674384395db2bcf2721c3bcfa216c86922651a268041e5(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40ce53f73864cb5c89f3baf13c64dba67cc42e274565b6c52a84904f6fd5f4b3(
    *,
    field_selectors: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEventDataStore.AdvancedFieldSelectorProperty, typing.Dict[builtins.str, typing.Any]]]]],
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13e48a5f3f6a4ee090f15046f2744cbdc1f623a943843b6e8cd72526e852b9e5(
    *,
    field: builtins.str,
    ends_with: typing.Optional[typing.Sequence[builtins.str]] = None,
    equal_to: typing.Optional[typing.Sequence[builtins.str]] = None,
    not_ends_with: typing.Optional[typing.Sequence[builtins.str]] = None,
    not_equals: typing.Optional[typing.Sequence[builtins.str]] = None,
    not_starts_with: typing.Optional[typing.Sequence[builtins.str]] = None,
    starts_with: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5dc8183d614f9c9498310cd377ff020cdc048d422b2548bbe678fc3c199d1dc6(
    *,
    insight_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc172d8375a6bcb019f0df4a0d571d671956c64545dc03fc01f9ad66e38ac10e(
    *,
    advanced_event_selectors: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEventDataStore.AdvancedEventSelectorProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    billing_mode: typing.Optional[builtins.str] = None,
    federation_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    federation_role_arn: typing.Optional[builtins.str] = None,
    ingestion_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    insights_destination: typing.Optional[builtins.str] = None,
    insight_selectors: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEventDataStore.InsightSelectorProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    multi_region_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    name: typing.Optional[builtins.str] = None,
    organization_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    retention_period: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    termination_protection_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e63ea1d0937535109b462c5587b69e94988e2caeb02b49177c8a53040c569033(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    resource_arn: builtins.str,
    resource_policy: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b32eb6fa58caf5ce6823a322212ade70664d4d37672f421c013fb2553ece2012(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb1739db5f96a9531e5f3655ec7c5b40527ac758bdb8bb842b79ad2206ec375f(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2bbc7a61c40e678ccc323afced9d77064978b41254369fee4db815497450dcd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e81052ff397bfd1d58bc17a51da7f1ee393c63b322c1b7d43b49b11f481e0ade(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a325337b33ae7cf48e36873295a3efad9af30e81615a436102a6dd5c10a2f08(
    *,
    resource_arn: builtins.str,
    resource_policy: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2259d5765ec84e4697f55f0d491871f1aa010feb94b3445a33a9e4b9f9cfbbd5(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    is_logging: typing.Union[builtins.bool, _IResolvable_da3f097b],
    s3_bucket_name: builtins.str,
    advanced_event_selectors: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTrail.AdvancedEventSelectorProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    cloud_watch_logs_log_group_arn: typing.Optional[builtins.str] = None,
    cloud_watch_logs_role_arn: typing.Optional[builtins.str] = None,
    enable_log_file_validation: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    event_selectors: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTrail.EventSelectorProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    include_global_service_events: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    insight_selectors: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTrail.InsightSelectorProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    is_multi_region_trail: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    is_organization_trail: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    s3_key_prefix: typing.Optional[builtins.str] = None,
    sns_topic_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    trail_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27c0b3977f3ce3e2ad80b21e158e38a08a45c6700ebeed895b3710e8c214a1bb(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__340f9d2dc4d668d217253c3ecdc1999319497932039d9878e65bb3b5c99c3e42(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28420bf6c9605a8eeb3ac59acf7f894b63e53a96b92e9d477f9cd206f2f9cf41(
    value: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__950bb01f69a31c7f47512f3a4330d4ce5db85c66795a79936ef3af33a322c8b2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae10dc28d41ecf82427e4cef4ce27f9c40933974aaf57ffd8e73f19c06621f53(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnTrail.AdvancedEventSelectorProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58f37437f0af59fad3f65c1d9ef003f52fa49f6aabcba3b40c779f379b8b0410(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cabe9b73fb8bc4d76fde324653a247811fa621cc9003d2c46e84b890b919cd28(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b942505386f8e61551da02925be57cd0474923089182c193fde0b17fe804056(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ef2943100a700e4bd2b0922f697c3d0da51c014bec4f2a8c4063f59e83067d7(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnTrail.EventSelectorProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a1c2489b0dca720e7fab9917132eaf8dc9468d58f2d500bccd7579577d74434(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d11150f51682efcafc38f048d84c35a263b443e02355965298d566b0714947d(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnTrail.InsightSelectorProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48558347dbb5febc8abf93096cfc174c76cbab4c443d68076643e329fb0787c0(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__583ab7d05361279f7f55956fec04616c02d033f55ef6113a3cf8c36630cd5ec5(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4fac6d2810385893265f6ef2611c9d8ceaa7635731b1ae56291d8e43a83cc907(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a62410d04026f326fad72a00ba17b36e83eb965baeada846126607f600de0f7f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99ce4d6977c0c8f0ad39dd667104baf8babcda3f6e64b94361cd24302f9bfb12(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6e90bde6d2082aefdd7c19acee054825987d54ead9c95ec2dbe11a014f72339(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29683f56476eaa26adca4a9a9312d409428d1af457282b2a0f93af552333a02e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6dd875607ea907f4214c12153b0923eaa1b2093e9c2bd798cc9ef56cf7886059(
    *,
    field_selectors: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTrail.AdvancedFieldSelectorProperty, typing.Dict[builtins.str, typing.Any]]]]],
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec8d9a5e1a3e1eac8b87551fd80e338cfe5e5578a88b45c91f7b6ae91857b236(
    *,
    field: builtins.str,
    ends_with: typing.Optional[typing.Sequence[builtins.str]] = None,
    equal_to: typing.Optional[typing.Sequence[builtins.str]] = None,
    not_ends_with: typing.Optional[typing.Sequence[builtins.str]] = None,
    not_equals: typing.Optional[typing.Sequence[builtins.str]] = None,
    not_starts_with: typing.Optional[typing.Sequence[builtins.str]] = None,
    starts_with: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eba75230621acc9cbcd78ccb16505dcc1e9707f9ce1d5b5c64f36220a2fbd761(
    *,
    type: builtins.str,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6a456b792eafca6f1c49386b9ce4f496975ac1ff51f363686c31755c3ba2007(
    *,
    data_resources: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTrail.DataResourceProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    exclude_management_event_sources: typing.Optional[typing.Sequence[builtins.str]] = None,
    include_management_events: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    read_write_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c36e7d325732c46967fd652ce7b5b56b5b548efaa4c260b4d0918a84e4b31748(
    *,
    insight_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe29eec9c2fc5386dadc73c14bab1f4c61dc9a7cd9ad26812bf169694fa1ed79(
    *,
    is_logging: typing.Union[builtins.bool, _IResolvable_da3f097b],
    s3_bucket_name: builtins.str,
    advanced_event_selectors: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTrail.AdvancedEventSelectorProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    cloud_watch_logs_log_group_arn: typing.Optional[builtins.str] = None,
    cloud_watch_logs_role_arn: typing.Optional[builtins.str] = None,
    enable_log_file_validation: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    event_selectors: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTrail.EventSelectorProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    include_global_service_events: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    insight_selectors: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTrail.InsightSelectorProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    is_multi_region_trail: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    is_organization_trail: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    s3_key_prefix: typing.Optional[builtins.str] = None,
    sns_topic_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    trail_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1cb2fd9327becb7b11bbb80f00762b693b18c3d8338685289adc8907f8b2c231(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d0df2bbec441689030ea9ec1ee0c490c06396957a77ed6d3353b714dbe525ea(
    *,
    bucket: _IBucket_42e086fd,
    object_prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b48a378f80b4a1726c79900e866bb932a0819e2b9124d6c5818259bf8c2efd3(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    bucket: typing.Optional[_IBucket_42e086fd] = None,
    cloud_watch_log_group: typing.Optional[_ILogGroup_3c4fa718] = None,
    cloud_watch_logs_retention: typing.Optional[_RetentionDays_070f99f0] = None,
    enable_file_validation: typing.Optional[builtins.bool] = None,
    encryption_key: typing.Optional[_IKey_5f11635f] = None,
    include_global_service_events: typing.Optional[builtins.bool] = None,
    insight_types: typing.Optional[typing.Sequence[InsightType]] = None,
    is_multi_region_trail: typing.Optional[builtins.bool] = None,
    is_organization_trail: typing.Optional[builtins.bool] = None,
    management_events: typing.Optional[ReadWriteType] = None,
    org_id: typing.Optional[builtins.str] = None,
    s3_key_prefix: typing.Optional[builtins.str] = None,
    send_to_cloud_watch_logs: typing.Optional[builtins.bool] = None,
    sns_topic: typing.Optional[_ITopic_9eca4852] = None,
    trail_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3da7eec1f43e2097945d61dbe36980d815e286492252afbfa5b77f6f90154c3(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    target: typing.Optional[_IRuleTarget_7a91f454] = None,
    cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
    description: typing.Optional[builtins.str] = None,
    event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
    rule_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a83bd81f5369dec88236698aaaacd2b411e71f0b26a1820dac4d9708b35eeb2(
    data_resource_type: DataResourceType,
    data_resource_values: typing.Sequence[builtins.str],
    *,
    exclude_management_event_sources: typing.Optional[typing.Sequence[ManagementEventSources]] = None,
    include_management_events: typing.Optional[builtins.bool] = None,
    read_write_type: typing.Optional[ReadWriteType] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4c1abc3131dbd715c5dbbad63c8d79ef1bb110ded697e9202e474e8c0766da0(
    handlers: typing.Sequence[_IFunction_6adb0ab8],
    *,
    exclude_management_event_sources: typing.Optional[typing.Sequence[ManagementEventSources]] = None,
    include_management_events: typing.Optional[builtins.bool] = None,
    read_write_type: typing.Optional[ReadWriteType] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4675fde35c881f97ed3c098123c51ad64ff5ae73a4d353d16fd977d9951fefb2(
    s3_selector: typing.Sequence[typing.Union[S3EventSelector, typing.Dict[builtins.str, typing.Any]]],
    *,
    exclude_management_event_sources: typing.Optional[typing.Sequence[ManagementEventSources]] = None,
    include_management_events: typing.Optional[builtins.bool] = None,
    read_write_type: typing.Optional[ReadWriteType] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5ff27b267882181cdb7a08f4ac78fe9eaffb7f3b50db3ce4f2dc9ce929af6f7(
    *,
    bucket: typing.Optional[_IBucket_42e086fd] = None,
    cloud_watch_log_group: typing.Optional[_ILogGroup_3c4fa718] = None,
    cloud_watch_logs_retention: typing.Optional[_RetentionDays_070f99f0] = None,
    enable_file_validation: typing.Optional[builtins.bool] = None,
    encryption_key: typing.Optional[_IKey_5f11635f] = None,
    include_global_service_events: typing.Optional[builtins.bool] = None,
    insight_types: typing.Optional[typing.Sequence[InsightType]] = None,
    is_multi_region_trail: typing.Optional[builtins.bool] = None,
    is_organization_trail: typing.Optional[builtins.bool] = None,
    management_events: typing.Optional[ReadWriteType] = None,
    org_id: typing.Optional[builtins.str] = None,
    s3_key_prefix: typing.Optional[builtins.str] = None,
    send_to_cloud_watch_logs: typing.Optional[builtins.bool] = None,
    sns_topic: typing.Optional[_ITopic_9eca4852] = None,
    trail_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
