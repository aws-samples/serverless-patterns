'''
# Amazon Simple Notification Service Construct Library

Add an SNS Topic to your stack:

```python
topic = sns.Topic(self, "Topic",
    display_name="Customer subscription topic"
)
```

Add a FIFO SNS topic with content-based de-duplication to your stack:

```python
topic = sns.Topic(self, "Topic",
    content_based_deduplication=True,
    display_name="Customer subscription topic",
    fifo=True
)
```

Add an SNS Topic to your stack with a specified signature version, which corresponds
to the hashing algorithm used while creating the signature of the notifications,
subscription confirmations, or unsubscribe confirmation messages sent by Amazon SNS.

The default signature version is `1` (`SHA1`).
SNS also supports signature version `2` (`SHA256`).

```python
topic = sns.Topic(self, "Topic",
    signature_version="2"
)
```

Note that FIFO topics require a topic name to be provided. The required `.fifo` suffix will be automatically generated and added to the topic name if it is not explicitly provided.

## Subscriptions

Various subscriptions can be added to the topic by calling the
`.addSubscription(...)` method on the topic. It accepts a *subscription* object,
default implementations of which can be found in the
`aws-cdk-lib/aws-sns-subscriptions` package:

Add an HTTPS Subscription to your topic:

```python
my_topic = sns.Topic(self, "MyTopic")

my_topic.add_subscription(subscriptions.UrlSubscription("https://foobar.com/"))
```

Subscribe a queue to the topic:

```python
# queue: sqs.Queue

my_topic = sns.Topic(self, "MyTopic")

my_topic.add_subscription(subscriptions.SqsSubscription(queue))
```

Note that subscriptions of queues in different accounts need to be manually confirmed by
reading the initial message from the queue and visiting the link found in it.

### Filter policy

A filter policy can be specified when subscribing an endpoint to a topic.

Example with a Lambda subscription:

```python
import aws_cdk.aws_lambda as lambda_
# fn: lambda.Function


my_topic = sns.Topic(self, "MyTopic")

# Lambda should receive only message matching the following conditions on attributes:
# color: 'red' or 'orange' or begins with 'bl'
# size: anything but 'small' or 'medium'
# price: between 100 and 200 or greater than 300
# store: attribute must be present
my_topic.add_subscription(subscriptions.LambdaSubscription(fn,
    filter_policy={
        "color": sns.SubscriptionFilter.string_filter(
            allowlist=["red", "orange"],
            match_prefixes=["bl"],
            match_suffixes=["ue"]
        ),
        "size": sns.SubscriptionFilter.string_filter(
            denylist=["small", "medium"]
        ),
        "price": sns.SubscriptionFilter.numeric_filter(
            between=sns.BetweenCondition(start=100, stop=200),
            greater_than=300
        ),
        "store": sns.SubscriptionFilter.exists_filter()
    }
))
```

#### Payload-based filtering

To filter messages based on the payload or body of the message, use the `filterPolicyWithMessageBody` property. This type of filter policy supports creating filters on nested objects.

Example with a Lambda subscription:

```python
import aws_cdk.aws_lambda as lambda_
# fn: lambda.Function


my_topic = sns.Topic(self, "MyTopic")

# Lambda should receive only message matching the following conditions on message body:
# color: 'red' or 'orange'
my_topic.add_subscription(subscriptions.LambdaSubscription(fn,
    filter_policy_with_message_body={
        "background": sns.FilterOrPolicy.policy({
            "color": sns.FilterOrPolicy.filter(sns.SubscriptionFilter.string_filter(
                allowlist=["red", "orange"]
            ))
        })
    }
))
```

### Example of Firehose Subscription

```python
from aws_cdk.aws_kinesisfirehose_alpha import DeliveryStream
# stream: DeliveryStream


topic = sns.Topic(self, "Topic")

sns.Subscription(self, "Subscription",
    topic=topic,
    endpoint=stream.delivery_stream_arn,
    protocol=sns.SubscriptionProtocol.FIREHOSE,
    subscription_role_arn="SAMPLE_ARN"
)
```

## DLQ setup for SNS Subscription

CDK can attach provided Queue as DLQ for your SNS subscription.
See the [SNS DLQ configuration docs](https://docs.aws.amazon.com/sns/latest/dg/sns-configure-dead-letter-queue.html) for more information about this feature.

Example of usage with user provided DLQ.

```python
topic = sns.Topic(self, "Topic")
dl_queue = sqs.Queue(self, "DeadLetterQueue",
    queue_name="MySubscription_DLQ",
    retention_period=Duration.days(14)
)

sns.Subscription(self, "Subscription",
    endpoint="endpoint",
    protocol=sns.SubscriptionProtocol.LAMBDA,
    topic=topic,
    dead_letter_queue=dl_queue
)
```

## CloudWatch Event Rule Target

SNS topics can be used as targets for CloudWatch event rules.

Use the `aws-cdk-lib/aws-events-targets.SnsTopic`:

```python
import aws_cdk.aws_codecommit as codecommit
import aws_cdk.aws_events_targets as targets

# repo: codecommit.Repository

my_topic = sns.Topic(self, "Topic")

repo.on_commit("OnCommit",
    target=targets.SnsTopic(my_topic)
)
```

This will result in adding a target to the event rule and will also modify the
topic resource policy to allow CloudWatch events to publish to the topic.

## Topic Policy

A topic policy is automatically created when `addToResourcePolicy` is called, if
one doesn't already exist. Using `addToResourcePolicy` is the simplest way to
add policies, but a `TopicPolicy` can also be created manually.

```python
topic = sns.Topic(self, "Topic")
topic_policy = sns.TopicPolicy(self, "TopicPolicy",
    topics=[topic]
)

topic_policy.document.add_statements(iam.PolicyStatement(
    actions=["sns:Subscribe"],
    principals=[iam.AnyPrincipal()],
    resources=[topic.topic_arn]
))
```

A policy document can also be passed on `TopicPolicy` construction

```python
topic = sns.Topic(self, "Topic")
policy_document = iam.PolicyDocument(
    assign_sids=True,
    statements=[
        iam.PolicyStatement(
            actions=["sns:Subscribe"],
            principals=[iam.AnyPrincipal()],
            resources=[topic.topic_arn]
        )
    ]
)

topic_policy = sns.TopicPolicy(self, "Policy",
    topics=[topic],
    policy_document=policy_document
)
```

### Enforce encryption of data in transit when publishing to a topic

You can enforce SSL when creating a topic policy by setting the `enforceSSL` flag:

```python
topic = sns.Topic(self, "Topic")
policy_document = iam.PolicyDocument(
    assign_sids=True,
    statements=[
        iam.PolicyStatement(
            actions=["sns:Publish"],
            principals=[iam.ServicePrincipal("s3.amazonaws.com")],
            resources=[topic.topic_arn]
        )
    ]
)

topic_policy = sns.TopicPolicy(self, "Policy",
    topics=[topic],
    policy_document=policy_document,
    enforce_sSL=True
)
```

Similiarly you can enforce SSL by setting the `enforceSSL` flag on the topic:

```python
topic = sns.Topic(self, "TopicAddPolicy",
    enforce_sSL=True
)

topic.add_to_resource_policy(iam.PolicyStatement(
    principals=[iam.ServicePrincipal("s3.amazonaws.com")],
    actions=["sns:Publish"],
    resources=[topic.topic_arn]
))
```

## Delivery status logging

Amazon SNS provides support to log the delivery status of notification messages sent to topics with the following Amazon SNS endpoints:

* HTTP
* Amazon Kinesis Data Firehose
* AWS Lambda
* Platform application endpoint
* Amazon Simple Queue Service

Example with a delivery status logging configuration for SQS:

```python
# role: iam.Role

topic = sns.Topic(self, "MyTopic",
    logging_configs=[sns.LoggingConfig(
        protocol=sns.LoggingProtocol.SQS,
        failure_feedback_role=role,
        success_feedback_role=role,
        success_feedback_sample_rate=50
    )
    ]
)
```

A delivery status logging configuration can also be added to your topic by `addLoggingConfig` method:

```python
# role: iam.Role

topic = sns.Topic(self, "MyTopic")

topic.add_logging_config(
    protocol=sns.LoggingProtocol.SQS,
    failure_feedback_role=role,
    success_feedback_role=role,
    success_feedback_sample_rate=50
)
```

Note that valid values for `successFeedbackSampleRate` are integer between 0-100.

## Archive Policy

Message archiving provides the ability to archive a single copy of all messages published to your topic.
You can store published messages within your topic by enabling the message archive policy on the topic, which enables message archiving for all subscriptions linked to that topic.
Messages can be archived for a minimum of one day to a maximum of 365 days.

Example with an archive policy:

```python
topic = sns.Topic(self, "MyTopic",
    fifo=True,
    message_retention_period_in_days=7
)
```

**Note**: The `messageRetentionPeriodInDays` property is only available for FIFO topics.

## TracingConfig

Tracing mode of an Amazon SNS topic.

If PassThrough, the topic passes trace headers received from the Amazon SNS publisher to its subscription.
If set to Active, Amazon SNS will vend X-Ray segment data to topic owner account if the sampled flag in the tracing header is true.

The default TracingConfig is `TracingConfig.PASS_THROUGH`.

Example with a tracingConfig set to Active:

```python
topic = sns.Topic(self, "MyTopic",
    tracing_config=sns.TracingConfig.ACTIVE
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
    Duration as _Duration_4839e8c3,
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    IResource as _IResource_c80c4260,
    ITaggable as _ITaggable_36806126,
    Resource as _Resource_45bc6135,
    ResourceProps as _ResourceProps_15a65b4e,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)
from ..aws_cloudwatch import (
    Metric as _Metric_e396a4dc,
    MetricOptions as _MetricOptions_1788b62f,
    Unit as _Unit_61bc6f70,
)
from ..aws_codestarnotifications import (
    INotificationRuleTarget as _INotificationRuleTarget_faa3b79b,
    NotificationRuleTargetConfig as _NotificationRuleTargetConfig_ea27e095,
)
from ..aws_iam import (
    AddToResourcePolicyResult as _AddToResourcePolicyResult_1d0a53ad,
    Grant as _Grant_a7ae64f8,
    IGrantable as _IGrantable_71c4f5de,
    IRole as _IRole_235f5d8e,
    PolicyDocument as _PolicyDocument_3ac34393,
    PolicyStatement as _PolicyStatement_0fe33853,
)
from ..aws_kms import IKey as _IKey_5f11635f
from ..aws_sqs import IQueue as _IQueue_7ed6f679


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_sns.BetweenCondition",
    jsii_struct_bases=[],
    name_mapping={"start": "start", "stop": "stop"},
)
class BetweenCondition:
    def __init__(self, *, start: jsii.Number, stop: jsii.Number) -> None:
        '''Between condition for a numeric attribute.

        :param start: The start value.
        :param stop: The stop value.

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_lambda as lambda_
            # fn: lambda.Function
            
            
            my_topic = sns.Topic(self, "MyTopic")
            
            # Lambda should receive only message matching the following conditions on attributes:
            # color: 'red' or 'orange' or begins with 'bl'
            # size: anything but 'small' or 'medium'
            # price: between 100 and 200 or greater than 300
            # store: attribute must be present
            my_topic.add_subscription(subscriptions.LambdaSubscription(fn,
                filter_policy={
                    "color": sns.SubscriptionFilter.string_filter(
                        allowlist=["red", "orange"],
                        match_prefixes=["bl"],
                        match_suffixes=["ue"]
                    ),
                    "size": sns.SubscriptionFilter.string_filter(
                        denylist=["small", "medium"]
                    ),
                    "price": sns.SubscriptionFilter.numeric_filter(
                        between=sns.BetweenCondition(start=100, stop=200),
                        greater_than=300
                    ),
                    "store": sns.SubscriptionFilter.exists_filter()
                }
            ))
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ebb3778ab30030aa884085aeda12c2079b30d59a16602ab32cd66efdb1de356)
            check_type(argname="argument start", value=start, expected_type=type_hints["start"])
            check_type(argname="argument stop", value=stop, expected_type=type_hints["stop"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "start": start,
            "stop": stop,
        }

    @builtins.property
    def start(self) -> jsii.Number:
        '''The start value.'''
        result = self._values.get("start")
        assert result is not None, "Required property 'start' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def stop(self) -> jsii.Number:
        '''The stop value.'''
        result = self._values.get("stop")
        assert result is not None, "Required property 'stop' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BetweenCondition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnSubscription(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_sns.CfnSubscription",
):
    '''The ``AWS::SNS::Subscription`` resource subscribes an endpoint to an Amazon SNS topic.

    For a subscription to be created, the owner of the endpoint must confirm the subscription.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-subscription.html
    :cloudformationResource: AWS::SNS::Subscription
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_sns as sns
        
        # delivery_policy: Any
        # filter_policy: Any
        # redrive_policy: Any
        # replay_policy: Any
        
        cfn_subscription = sns.CfnSubscription(self, "MyCfnSubscription",
            protocol="protocol",
            topic_arn="topicArn",
        
            # the properties below are optional
            delivery_policy=delivery_policy,
            endpoint="endpoint",
            filter_policy=filter_policy,
            filter_policy_scope="filterPolicyScope",
            raw_message_delivery=False,
            redrive_policy=redrive_policy,
            region="region",
            replay_policy=replay_policy,
            subscription_role_arn="subscriptionRoleArn"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        protocol: builtins.str,
        topic_arn: builtins.str,
        delivery_policy: typing.Any = None,
        endpoint: typing.Optional[builtins.str] = None,
        filter_policy: typing.Any = None,
        filter_policy_scope: typing.Optional[builtins.str] = None,
        raw_message_delivery: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        redrive_policy: typing.Any = None,
        region: typing.Optional[builtins.str] = None,
        replay_policy: typing.Any = None,
        subscription_role_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param protocol: The subscription's protocol. For more information, see the ``Protocol`` parameter of the ``[Subscribe](https://docs.aws.amazon.com/sns/latest/api/API_Subscribe.html)`` action in the *Amazon SNS API Reference* .
        :param topic_arn: The ARN of the topic to subscribe to.
        :param delivery_policy: The delivery policy JSON assigned to the subscription. Enables the subscriber to define the message delivery retry strategy in the case of an HTTP/S endpoint subscribed to the topic. For more information, see ``[GetSubscriptionAttributes](https://docs.aws.amazon.com/sns/latest/api/API_GetSubscriptionAttributes.html)`` in the *Amazon SNS API Reference* and `Message delivery retries <https://docs.aws.amazon.com/sns/latest/dg/sns-message-delivery-retries.html>`_ in the *Amazon SNS Developer Guide* .
        :param endpoint: The subscription's endpoint. The endpoint value depends on the protocol that you specify. For more information, see the ``Endpoint`` parameter of the ``[Subscribe](https://docs.aws.amazon.com/sns/latest/api/API_Subscribe.html)`` action in the *Amazon SNS API Reference* .
        :param filter_policy: The filter policy JSON assigned to the subscription. Enables the subscriber to filter out unwanted messages. For more information, see ``[GetSubscriptionAttributes](https://docs.aws.amazon.com/sns/latest/api/API_GetSubscriptionAttributes.html)`` in the *Amazon SNS API Reference* and `Message filtering <https://docs.aws.amazon.com/sns/latest/dg/sns-message-filtering.html>`_ in the *Amazon SNS Developer Guide* .
        :param filter_policy_scope: This attribute lets you choose the filtering scope by using one of the following string value types:. - ``MessageAttributes`` (default) - The filter is applied on the message attributes. - ``MessageBody`` - The filter is applied on the message body.
        :param raw_message_delivery: When set to ``true`` , enables raw message delivery. Raw messages don't contain any JSON formatting and can be sent to Amazon SQS and HTTP/S endpoints. For more information, see ``[GetSubscriptionAttributes](https://docs.aws.amazon.com/sns/latest/api/API_GetSubscriptionAttributes.html)`` in the *Amazon SNS API Reference* .
        :param redrive_policy: When specified, sends undeliverable messages to the specified Amazon SQS dead-letter queue. Messages that can't be delivered due to client errors (for example, when the subscribed endpoint is unreachable) or server errors (for example, when the service that powers the subscribed endpoint becomes unavailable) are held in the dead-letter queue for further analysis or reprocessing. For more information about the redrive policy and dead-letter queues, see `Amazon SQS dead-letter queues <https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html>`_ in the *Amazon SQS Developer Guide* .
        :param region: For cross-region subscriptions, the region in which the topic resides. If no region is specified, AWS CloudFormation uses the region of the caller as the default. If you perform an update operation that only updates the ``Region`` property of a ``AWS::SNS::Subscription`` resource, that operation will fail unless you are either: - Updating the ``Region`` from ``NULL`` to the caller region. - Updating the ``Region`` from the caller region to ``NULL`` .
        :param replay_policy: 
        :param subscription_role_arn: This property applies only to Amazon Data Firehose delivery stream subscriptions. Specify the ARN of the IAM role that has the following: - Permission to write to the Amazon Data Firehose delivery stream - Amazon SNS listed as a trusted entity Specifying a valid ARN for this attribute is required for Firehose delivery stream subscriptions. For more information, see `Fanout to Amazon Data Firehose delivery streams <https://docs.aws.amazon.com/sns/latest/dg/sns-firehose-as-subscriber.html>`_ in the *Amazon SNS Developer Guide.*
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f3839647e73879ccdb1519ec2afccf78b6168046279d32c5390b3e2543d1fec)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSubscriptionProps(
            protocol=protocol,
            topic_arn=topic_arn,
            delivery_policy=delivery_policy,
            endpoint=endpoint,
            filter_policy=filter_policy,
            filter_policy_scope=filter_policy_scope,
            raw_message_delivery=raw_message_delivery,
            redrive_policy=redrive_policy,
            region=region,
            replay_policy=replay_policy,
            subscription_role_arn=subscription_role_arn,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ad167deaa30cad42bef358dc9a03bed1399dc45e07655b5e137a67f04418907)
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
            type_hints = typing.get_type_hints(_typecheckingstub__97d8f48dcae3735a971499612987e1098d379f23b6c7cd953ea2feccf6050c2a)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        '''The subscription's protocol.'''
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7edc75a221f1678a2af2a8200b26975f38bc8f1f405e735dbdeff306d6b51f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="topicArn")
    def topic_arn(self) -> builtins.str:
        '''The ARN of the topic to subscribe to.'''
        return typing.cast(builtins.str, jsii.get(self, "topicArn"))

    @topic_arn.setter
    def topic_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__695665f02c816a5f5b8823c7113d6f83dc37a450f1e44a469efc6b646a042042)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "topicArn", value)

    @builtins.property
    @jsii.member(jsii_name="deliveryPolicy")
    def delivery_policy(self) -> typing.Any:
        '''The delivery policy JSON assigned to the subscription.'''
        return typing.cast(typing.Any, jsii.get(self, "deliveryPolicy"))

    @delivery_policy.setter
    def delivery_policy(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__363ef69700500450c12f41b43c0226475a42d465d0e2c1eb2c6a62103297a77d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deliveryPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="endpoint")
    def endpoint(self) -> typing.Optional[builtins.str]:
        '''The subscription's endpoint.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpoint"))

    @endpoint.setter
    def endpoint(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51bd5ec550058313034fb332f79c3420c0ab46be8aaa0abb6b7489748ace3b8f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpoint", value)

    @builtins.property
    @jsii.member(jsii_name="filterPolicy")
    def filter_policy(self) -> typing.Any:
        '''The filter policy JSON assigned to the subscription.'''
        return typing.cast(typing.Any, jsii.get(self, "filterPolicy"))

    @filter_policy.setter
    def filter_policy(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e0ead2904ccf72657e766b50c2aef479b86c25ba314b73f122eedee3bf8f859)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filterPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="filterPolicyScope")
    def filter_policy_scope(self) -> typing.Optional[builtins.str]:
        '''This attribute lets you choose the filtering scope by using one of the following string value types:.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "filterPolicyScope"))

    @filter_policy_scope.setter
    def filter_policy_scope(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8b99524984cf1e668a25b6f6425da23c5d12b2d696637bdc50a8fdab3282ac6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filterPolicyScope", value)

    @builtins.property
    @jsii.member(jsii_name="rawMessageDelivery")
    def raw_message_delivery(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''When set to ``true`` , enables raw message delivery.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "rawMessageDelivery"))

    @raw_message_delivery.setter
    def raw_message_delivery(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b31b31d2e697eb675dfd0da4695e87324259ab34307bec1a543ab628d2d371d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rawMessageDelivery", value)

    @builtins.property
    @jsii.member(jsii_name="redrivePolicy")
    def redrive_policy(self) -> typing.Any:
        '''When specified, sends undeliverable messages to the specified Amazon SQS dead-letter queue.'''
        return typing.cast(typing.Any, jsii.get(self, "redrivePolicy"))

    @redrive_policy.setter
    def redrive_policy(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5fbcc2d22ef7dec8cd3d31ce95fa8e065175f8957313872e3b1a02015210c603)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redrivePolicy", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> typing.Optional[builtins.str]:
        '''For cross-region subscriptions, the region in which the topic resides.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "region"))

    @region.setter
    def region(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22cba62b05c6e7ecdf0102d83ee908ae549d02df6eb8dd5643c2c42074fdf936)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="replayPolicy")
    def replay_policy(self) -> typing.Any:
        return typing.cast(typing.Any, jsii.get(self, "replayPolicy"))

    @replay_policy.setter
    def replay_policy(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a75cc1735865b82732f90f42a2ba55634431d8bdec48d0a7752a79354f0c850d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replayPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="subscriptionRoleArn")
    def subscription_role_arn(self) -> typing.Optional[builtins.str]:
        '''This property applies only to Amazon Data Firehose delivery stream subscriptions.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subscriptionRoleArn"))

    @subscription_role_arn.setter
    def subscription_role_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a71b3667b255126f8bc5b4059f4687fa922e718121515d78883ff30eb130ad2a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subscriptionRoleArn", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_sns.CfnSubscriptionProps",
    jsii_struct_bases=[],
    name_mapping={
        "protocol": "protocol",
        "topic_arn": "topicArn",
        "delivery_policy": "deliveryPolicy",
        "endpoint": "endpoint",
        "filter_policy": "filterPolicy",
        "filter_policy_scope": "filterPolicyScope",
        "raw_message_delivery": "rawMessageDelivery",
        "redrive_policy": "redrivePolicy",
        "region": "region",
        "replay_policy": "replayPolicy",
        "subscription_role_arn": "subscriptionRoleArn",
    },
)
class CfnSubscriptionProps:
    def __init__(
        self,
        *,
        protocol: builtins.str,
        topic_arn: builtins.str,
        delivery_policy: typing.Any = None,
        endpoint: typing.Optional[builtins.str] = None,
        filter_policy: typing.Any = None,
        filter_policy_scope: typing.Optional[builtins.str] = None,
        raw_message_delivery: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        redrive_policy: typing.Any = None,
        region: typing.Optional[builtins.str] = None,
        replay_policy: typing.Any = None,
        subscription_role_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnSubscription``.

        :param protocol: The subscription's protocol. For more information, see the ``Protocol`` parameter of the ``[Subscribe](https://docs.aws.amazon.com/sns/latest/api/API_Subscribe.html)`` action in the *Amazon SNS API Reference* .
        :param topic_arn: The ARN of the topic to subscribe to.
        :param delivery_policy: The delivery policy JSON assigned to the subscription. Enables the subscriber to define the message delivery retry strategy in the case of an HTTP/S endpoint subscribed to the topic. For more information, see ``[GetSubscriptionAttributes](https://docs.aws.amazon.com/sns/latest/api/API_GetSubscriptionAttributes.html)`` in the *Amazon SNS API Reference* and `Message delivery retries <https://docs.aws.amazon.com/sns/latest/dg/sns-message-delivery-retries.html>`_ in the *Amazon SNS Developer Guide* .
        :param endpoint: The subscription's endpoint. The endpoint value depends on the protocol that you specify. For more information, see the ``Endpoint`` parameter of the ``[Subscribe](https://docs.aws.amazon.com/sns/latest/api/API_Subscribe.html)`` action in the *Amazon SNS API Reference* .
        :param filter_policy: The filter policy JSON assigned to the subscription. Enables the subscriber to filter out unwanted messages. For more information, see ``[GetSubscriptionAttributes](https://docs.aws.amazon.com/sns/latest/api/API_GetSubscriptionAttributes.html)`` in the *Amazon SNS API Reference* and `Message filtering <https://docs.aws.amazon.com/sns/latest/dg/sns-message-filtering.html>`_ in the *Amazon SNS Developer Guide* .
        :param filter_policy_scope: This attribute lets you choose the filtering scope by using one of the following string value types:. - ``MessageAttributes`` (default) - The filter is applied on the message attributes. - ``MessageBody`` - The filter is applied on the message body.
        :param raw_message_delivery: When set to ``true`` , enables raw message delivery. Raw messages don't contain any JSON formatting and can be sent to Amazon SQS and HTTP/S endpoints. For more information, see ``[GetSubscriptionAttributes](https://docs.aws.amazon.com/sns/latest/api/API_GetSubscriptionAttributes.html)`` in the *Amazon SNS API Reference* .
        :param redrive_policy: When specified, sends undeliverable messages to the specified Amazon SQS dead-letter queue. Messages that can't be delivered due to client errors (for example, when the subscribed endpoint is unreachable) or server errors (for example, when the service that powers the subscribed endpoint becomes unavailable) are held in the dead-letter queue for further analysis or reprocessing. For more information about the redrive policy and dead-letter queues, see `Amazon SQS dead-letter queues <https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html>`_ in the *Amazon SQS Developer Guide* .
        :param region: For cross-region subscriptions, the region in which the topic resides. If no region is specified, AWS CloudFormation uses the region of the caller as the default. If you perform an update operation that only updates the ``Region`` property of a ``AWS::SNS::Subscription`` resource, that operation will fail unless you are either: - Updating the ``Region`` from ``NULL`` to the caller region. - Updating the ``Region`` from the caller region to ``NULL`` .
        :param replay_policy: 
        :param subscription_role_arn: This property applies only to Amazon Data Firehose delivery stream subscriptions. Specify the ARN of the IAM role that has the following: - Permission to write to the Amazon Data Firehose delivery stream - Amazon SNS listed as a trusted entity Specifying a valid ARN for this attribute is required for Firehose delivery stream subscriptions. For more information, see `Fanout to Amazon Data Firehose delivery streams <https://docs.aws.amazon.com/sns/latest/dg/sns-firehose-as-subscriber.html>`_ in the *Amazon SNS Developer Guide.*

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-subscription.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_sns as sns
            
            # delivery_policy: Any
            # filter_policy: Any
            # redrive_policy: Any
            # replay_policy: Any
            
            cfn_subscription_props = sns.CfnSubscriptionProps(
                protocol="protocol",
                topic_arn="topicArn",
            
                # the properties below are optional
                delivery_policy=delivery_policy,
                endpoint="endpoint",
                filter_policy=filter_policy,
                filter_policy_scope="filterPolicyScope",
                raw_message_delivery=False,
                redrive_policy=redrive_policy,
                region="region",
                replay_policy=replay_policy,
                subscription_role_arn="subscriptionRoleArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0227b0c451693656571029cae1cbec74d209cf9e946210145d282e8f03fd1d28)
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument topic_arn", value=topic_arn, expected_type=type_hints["topic_arn"])
            check_type(argname="argument delivery_policy", value=delivery_policy, expected_type=type_hints["delivery_policy"])
            check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
            check_type(argname="argument filter_policy", value=filter_policy, expected_type=type_hints["filter_policy"])
            check_type(argname="argument filter_policy_scope", value=filter_policy_scope, expected_type=type_hints["filter_policy_scope"])
            check_type(argname="argument raw_message_delivery", value=raw_message_delivery, expected_type=type_hints["raw_message_delivery"])
            check_type(argname="argument redrive_policy", value=redrive_policy, expected_type=type_hints["redrive_policy"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument replay_policy", value=replay_policy, expected_type=type_hints["replay_policy"])
            check_type(argname="argument subscription_role_arn", value=subscription_role_arn, expected_type=type_hints["subscription_role_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "protocol": protocol,
            "topic_arn": topic_arn,
        }
        if delivery_policy is not None:
            self._values["delivery_policy"] = delivery_policy
        if endpoint is not None:
            self._values["endpoint"] = endpoint
        if filter_policy is not None:
            self._values["filter_policy"] = filter_policy
        if filter_policy_scope is not None:
            self._values["filter_policy_scope"] = filter_policy_scope
        if raw_message_delivery is not None:
            self._values["raw_message_delivery"] = raw_message_delivery
        if redrive_policy is not None:
            self._values["redrive_policy"] = redrive_policy
        if region is not None:
            self._values["region"] = region
        if replay_policy is not None:
            self._values["replay_policy"] = replay_policy
        if subscription_role_arn is not None:
            self._values["subscription_role_arn"] = subscription_role_arn

    @builtins.property
    def protocol(self) -> builtins.str:
        '''The subscription's protocol.

        For more information, see the ``Protocol`` parameter of the ``[Subscribe](https://docs.aws.amazon.com/sns/latest/api/API_Subscribe.html)`` action in the *Amazon SNS API Reference* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-subscription.html#cfn-sns-subscription-protocol
        '''
        result = self._values.get("protocol")
        assert result is not None, "Required property 'protocol' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def topic_arn(self) -> builtins.str:
        '''The ARN of the topic to subscribe to.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-subscription.html#cfn-sns-subscription-topicarn
        '''
        result = self._values.get("topic_arn")
        assert result is not None, "Required property 'topic_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def delivery_policy(self) -> typing.Any:
        '''The delivery policy JSON assigned to the subscription.

        Enables the subscriber to define the message delivery retry strategy in the case of an HTTP/S endpoint subscribed to the topic. For more information, see ``[GetSubscriptionAttributes](https://docs.aws.amazon.com/sns/latest/api/API_GetSubscriptionAttributes.html)`` in the *Amazon SNS API Reference* and `Message delivery retries <https://docs.aws.amazon.com/sns/latest/dg/sns-message-delivery-retries.html>`_ in the *Amazon SNS Developer Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-subscription.html#cfn-sns-subscription-deliverypolicy
        '''
        result = self._values.get("delivery_policy")
        return typing.cast(typing.Any, result)

    @builtins.property
    def endpoint(self) -> typing.Optional[builtins.str]:
        '''The subscription's endpoint.

        The endpoint value depends on the protocol that you specify. For more information, see the ``Endpoint`` parameter of the ``[Subscribe](https://docs.aws.amazon.com/sns/latest/api/API_Subscribe.html)`` action in the *Amazon SNS API Reference* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-subscription.html#cfn-sns-subscription-endpoint
        '''
        result = self._values.get("endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def filter_policy(self) -> typing.Any:
        '''The filter policy JSON assigned to the subscription.

        Enables the subscriber to filter out unwanted messages. For more information, see ``[GetSubscriptionAttributes](https://docs.aws.amazon.com/sns/latest/api/API_GetSubscriptionAttributes.html)`` in the *Amazon SNS API Reference* and `Message filtering <https://docs.aws.amazon.com/sns/latest/dg/sns-message-filtering.html>`_ in the *Amazon SNS Developer Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-subscription.html#cfn-sns-subscription-filterpolicy
        '''
        result = self._values.get("filter_policy")
        return typing.cast(typing.Any, result)

    @builtins.property
    def filter_policy_scope(self) -> typing.Optional[builtins.str]:
        '''This attribute lets you choose the filtering scope by using one of the following string value types:.

        - ``MessageAttributes`` (default) - The filter is applied on the message attributes.
        - ``MessageBody`` - The filter is applied on the message body.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-subscription.html#cfn-sns-subscription-filterpolicyscope
        '''
        result = self._values.get("filter_policy_scope")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def raw_message_delivery(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''When set to ``true`` , enables raw message delivery.

        Raw messages don't contain any JSON formatting and can be sent to Amazon SQS and HTTP/S endpoints. For more information, see ``[GetSubscriptionAttributes](https://docs.aws.amazon.com/sns/latest/api/API_GetSubscriptionAttributes.html)`` in the *Amazon SNS API Reference* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-subscription.html#cfn-sns-subscription-rawmessagedelivery
        '''
        result = self._values.get("raw_message_delivery")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def redrive_policy(self) -> typing.Any:
        '''When specified, sends undeliverable messages to the specified Amazon SQS dead-letter queue.

        Messages that can't be delivered due to client errors (for example, when the subscribed endpoint is unreachable) or server errors (for example, when the service that powers the subscribed endpoint becomes unavailable) are held in the dead-letter queue for further analysis or reprocessing.

        For more information about the redrive policy and dead-letter queues, see `Amazon SQS dead-letter queues <https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html>`_ in the *Amazon SQS Developer Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-subscription.html#cfn-sns-subscription-redrivepolicy
        '''
        result = self._values.get("redrive_policy")
        return typing.cast(typing.Any, result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''For cross-region subscriptions, the region in which the topic resides.

        If no region is specified, AWS CloudFormation uses the region of the caller as the default.

        If you perform an update operation that only updates the ``Region`` property of a ``AWS::SNS::Subscription`` resource, that operation will fail unless you are either:

        - Updating the ``Region`` from ``NULL`` to the caller region.
        - Updating the ``Region`` from the caller region to ``NULL`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-subscription.html#cfn-sns-subscription-region
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def replay_policy(self) -> typing.Any:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-subscription.html#cfn-sns-subscription-replaypolicy
        '''
        result = self._values.get("replay_policy")
        return typing.cast(typing.Any, result)

    @builtins.property
    def subscription_role_arn(self) -> typing.Optional[builtins.str]:
        '''This property applies only to Amazon Data Firehose delivery stream subscriptions.

        Specify the ARN of the IAM role that has the following:

        - Permission to write to the Amazon Data Firehose delivery stream
        - Amazon SNS listed as a trusted entity

        Specifying a valid ARN for this attribute is required for Firehose delivery stream subscriptions. For more information, see `Fanout to Amazon Data Firehose delivery streams <https://docs.aws.amazon.com/sns/latest/dg/sns-firehose-as-subscriber.html>`_ in the *Amazon SNS Developer Guide.*

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-subscription.html#cfn-sns-subscription-subscriptionrolearn
        '''
        result = self._values.get("subscription_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSubscriptionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnTopic(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_sns.CfnTopic",
):
    '''The ``AWS::SNS::Topic`` resource creates a topic to which notifications can be published.

    .. epigraph::

       One account can create a maximum of 100,000 standard topics and 1,000 FIFO topics. For more information, see `Amazon SNS endpoints and quotas <https://docs.aws.amazon.com/general/latest/gr/sns.html>`_ in the *AWS General Reference* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-topic.html
    :cloudformationResource: AWS::SNS::Topic
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_sns as sns
        
        # archive_policy: Any
        # data_protection_policy: Any
        
        cfn_topic = sns.CfnTopic(self, "MyCfnTopic",
            archive_policy=archive_policy,
            content_based_deduplication=False,
            data_protection_policy=data_protection_policy,
            delivery_status_logging=[sns.CfnTopic.LoggingConfigProperty(
                protocol="protocol",
        
                # the properties below are optional
                failure_feedback_role_arn="failureFeedbackRoleArn",
                success_feedback_role_arn="successFeedbackRoleArn",
                success_feedback_sample_rate="successFeedbackSampleRate"
            )],
            display_name="displayName",
            fifo_topic=False,
            kms_master_key_id="kmsMasterKeyId",
            signature_version="signatureVersion",
            subscription=[sns.CfnTopic.SubscriptionProperty(
                endpoint="endpoint",
                protocol="protocol"
            )],
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            topic_name="topicName",
            tracing_config="tracingConfig"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        archive_policy: typing.Any = None,
        content_based_deduplication: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        data_protection_policy: typing.Any = None,
        delivery_status_logging: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTopic.LoggingConfigProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        display_name: typing.Optional[builtins.str] = None,
        fifo_topic: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        kms_master_key_id: typing.Optional[builtins.str] = None,
        signature_version: typing.Optional[builtins.str] = None,
        subscription: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTopic.SubscriptionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        topic_name: typing.Optional[builtins.str] = None,
        tracing_config: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param archive_policy: The archive policy determines the number of days Amazon SNS retains messages. You can set a retention period from 1 to 365 days.
        :param content_based_deduplication: Enables content-based deduplication for FIFO topics. - By default, ``ContentBasedDeduplication`` is set to ``false`` . If you create a FIFO topic and this attribute is ``false`` , you must specify a value for the ``MessageDeduplicationId`` parameter for the `Publish <https://docs.aws.amazon.com/sns/latest/api/API_Publish.html>`_ action. - When you set ``ContentBasedDeduplication`` to ``true`` , Amazon SNS uses a SHA-256 hash to generate the ``MessageDeduplicationId`` using the body of the message (but not the attributes of the message). (Optional) To override the generated value, you can specify a value for the the ``MessageDeduplicationId`` parameter for the ``Publish`` action.
        :param data_protection_policy: The body of the policy document you want to use for this topic. You can only add one policy per topic. The policy must be in JSON string format. Length Constraints: Maximum length of 30,720.
        :param delivery_status_logging: The ``DeliveryStatusLogging`` configuration enables you to log the delivery status of messages sent from your Amazon SNS topic to subscribed endpoints with the following supported delivery protocols:. - HTTP - Amazon Kinesis Data Firehose - AWS Lambda - Platform application endpoint - Amazon Simple Queue Service Once configured, log entries are sent to Amazon CloudWatch Logs.
        :param display_name: The display name to use for an Amazon SNS topic with SMS subscriptions. The display name must be maximum 100 characters long, including hyphens (-), underscores (_), spaces, and tabs.
        :param fifo_topic: Set to true to create a FIFO topic.
        :param kms_master_key_id: The ID of an AWS managed customer master key (CMK) for Amazon SNS or a custom CMK. For more information, see `Key terms <https://docs.aws.amazon.com/sns/latest/dg/sns-server-side-encryption.html#sse-key-terms>`_ . For more examples, see ``[KeyId](https://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeKey.html#API_DescribeKey_RequestParameters)`` in the *AWS Key Management Service API Reference* . This property applies only to `server-side-encryption <https://docs.aws.amazon.com/sns/latest/dg/sns-server-side-encryption.html>`_ .
        :param signature_version: The signature version corresponds to the hashing algorithm used while creating the signature of the notifications, subscription confirmations, or unsubscribe confirmation messages sent by Amazon SNS. By default, ``SignatureVersion`` is set to ``1`` .
        :param subscription: The Amazon SNS subscriptions (endpoints) for this topic. .. epigraph:: If you specify the ``Subscription`` property in the ``AWS::SNS::Topic`` resource and it creates an associated subscription resource, the associated subscription is not deleted when the ``AWS::SNS::Topic`` resource is deleted.
        :param tags: The list of tags to add to a new topic. .. epigraph:: To be able to tag a topic on creation, you must have the ``sns:CreateTopic`` and ``sns:TagResource`` permissions.
        :param topic_name: The name of the topic you want to create. Topic names must include only uppercase and lowercase ASCII letters, numbers, underscores, and hyphens, and must be between 1 and 256 characters long. FIFO topic names must end with ``.fifo`` . If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the topic name. For more information, see `Name type <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html>`_ . .. epigraph:: If you specify a name, you can't perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.
        :param tracing_config: Tracing mode of an Amazon SNS topic. By default ``TracingConfig`` is set to ``PassThrough`` , and the topic passes through the tracing header it receives from an Amazon SNS publisher to its subscriptions. If set to ``Active`` , Amazon SNS will vend X-Ray segment data to topic owner account if the sampled flag in the tracing header is true.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c3e689eaa6b740299fa6db2e53acc51021bc5deb0a8dd6d7bc29e8a364a1dfe)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnTopicProps(
            archive_policy=archive_policy,
            content_based_deduplication=content_based_deduplication,
            data_protection_policy=data_protection_policy,
            delivery_status_logging=delivery_status_logging,
            display_name=display_name,
            fifo_topic=fifo_topic,
            kms_master_key_id=kms_master_key_id,
            signature_version=signature_version,
            subscription=subscription,
            tags=tags,
            topic_name=topic_name,
            tracing_config=tracing_config,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__daf5369a4f3860bacf2f29e2b4cb7ddb422f52f07b72cb603e80cd57ba407136)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9b026fb3f06827298c161d83a15c46ff302bba18c779bbe604b86a1346f8a4d0)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrTopicArn")
    def attr_topic_arn(self) -> builtins.str:
        '''Returns the ARN of an Amazon SNS topic.

        :cloudformationAttribute: TopicArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTopicArn"))

    @builtins.property
    @jsii.member(jsii_name="attrTopicName")
    def attr_topic_name(self) -> builtins.str:
        '''Returns the name of an Amazon SNS topic.

        :cloudformationAttribute: TopicName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTopicName"))

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
    @jsii.member(jsii_name="archivePolicy")
    def archive_policy(self) -> typing.Any:
        '''The archive policy determines the number of days Amazon SNS retains messages.'''
        return typing.cast(typing.Any, jsii.get(self, "archivePolicy"))

    @archive_policy.setter
    def archive_policy(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4e735a5dfc67b4dafec2e9df7180dd3143cb26437dc792dcb49e9563663dd22)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "archivePolicy", value)

    @builtins.property
    @jsii.member(jsii_name="contentBasedDeduplication")
    def content_based_deduplication(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Enables content-based deduplication for FIFO topics.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "contentBasedDeduplication"))

    @content_based_deduplication.setter
    def content_based_deduplication(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61855b81d1d953ec33b8c0af7bad8099bc0ec45c2624d213b520131ecf95b724)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentBasedDeduplication", value)

    @builtins.property
    @jsii.member(jsii_name="dataProtectionPolicy")
    def data_protection_policy(self) -> typing.Any:
        '''The body of the policy document you want to use for this topic.'''
        return typing.cast(typing.Any, jsii.get(self, "dataProtectionPolicy"))

    @data_protection_policy.setter
    def data_protection_policy(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0fa01cdb622f9c1239adaa1d51fb0035fbf98f9f42d4c5cf2e419e59e007298b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataProtectionPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="deliveryStatusLogging")
    def delivery_status_logging(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTopic.LoggingConfigProperty"]]]]:
        '''The ``DeliveryStatusLogging`` configuration enables you to log the delivery status of messages sent from your Amazon SNS topic to subscribed endpoints with the following supported delivery protocols:.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTopic.LoggingConfigProperty"]]]], jsii.get(self, "deliveryStatusLogging"))

    @delivery_status_logging.setter
    def delivery_status_logging(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTopic.LoggingConfigProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c45e4d025e306c26000e7fa2d0ac2f744ec4393a8a4418f9a397a2f5c010e0cf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deliveryStatusLogging", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> typing.Optional[builtins.str]:
        '''The display name to use for an Amazon SNS topic with SMS subscriptions.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e672f7b6cfea2a409a715963f8ef1b01848153bb4867f8ad868e0bcb32a4fe4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="fifoTopic")
    def fifo_topic(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Set to true to create a FIFO topic.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "fifoTopic"))

    @fifo_topic.setter
    def fifo_topic(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a91ed56c1865e9ea5cd3d8d5ffef0aab07b45ce41c2580607fd141166a194ea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fifoTopic", value)

    @builtins.property
    @jsii.member(jsii_name="kmsMasterKeyId")
    def kms_master_key_id(self) -> typing.Optional[builtins.str]:
        '''The ID of an AWS managed customer master key (CMK) for Amazon SNS or a custom CMK.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsMasterKeyId"))

    @kms_master_key_id.setter
    def kms_master_key_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d940f36146ec2822d49a51165f9625c406a6b8add68591ddb68de7681318435b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsMasterKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="signatureVersion")
    def signature_version(self) -> typing.Optional[builtins.str]:
        '''The signature version corresponds to the hashing algorithm used while creating the signature of the notifications, subscription confirmations, or unsubscribe confirmation messages sent by Amazon SNS.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "signatureVersion"))

    @signature_version.setter
    def signature_version(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48790d8e0040c4fbaea7344de60c0f7d90bd512df53025055db78e6b9bac4a4e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "signatureVersion", value)

    @builtins.property
    @jsii.member(jsii_name="subscription")
    def subscription(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTopic.SubscriptionProperty"]]]]:
        '''The Amazon SNS subscriptions (endpoints) for this topic.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTopic.SubscriptionProperty"]]]], jsii.get(self, "subscription"))

    @subscription.setter
    def subscription(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTopic.SubscriptionProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f416792b5d579d938563017fc236edff31ba5aeb335512720ae83552c6832e9c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subscription", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The list of tags to add to a new topic.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4fc70aec71b6f6c75ff5cf5bd0ed0934ffe27fd6747714e83d2cd44e32ff452)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="topicName")
    def topic_name(self) -> typing.Optional[builtins.str]:
        '''The name of the topic you want to create.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "topicName"))

    @topic_name.setter
    def topic_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__774919bb9f8040862e9d2ff7d63e5862fa36e6930f96feffa891ad451553d624)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "topicName", value)

    @builtins.property
    @jsii.member(jsii_name="tracingConfig")
    def tracing_config(self) -> typing.Optional[builtins.str]:
        '''Tracing mode of an Amazon SNS topic.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tracingConfig"))

    @tracing_config.setter
    def tracing_config(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cca8ae0da10f9d461cb6a1d8687e3d2ee9214548942dacdad4fbbf396119fbcc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tracingConfig", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sns.CfnTopic.LoggingConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "protocol": "protocol",
            "failure_feedback_role_arn": "failureFeedbackRoleArn",
            "success_feedback_role_arn": "successFeedbackRoleArn",
            "success_feedback_sample_rate": "successFeedbackSampleRate",
        },
    )
    class LoggingConfigProperty:
        def __init__(
            self,
            *,
            protocol: builtins.str,
            failure_feedback_role_arn: typing.Optional[builtins.str] = None,
            success_feedback_role_arn: typing.Optional[builtins.str] = None,
            success_feedback_sample_rate: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ``LoggingConfig`` property type specifies the ``Delivery`` status logging configuration for an ```AWS::SNS::Topic`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-topic.html>`_ .

            :param protocol: Indicates one of the supported protocols for the Amazon SNS topic. .. epigraph:: At least one of the other three ``LoggingConfig`` properties is recommend along with ``Protocol`` .
            :param failure_feedback_role_arn: The IAM role ARN to be used when logging failed message deliveries in Amazon CloudWatch.
            :param success_feedback_role_arn: The IAM role ARN to be used when logging successful message deliveries in Amazon CloudWatch.
            :param success_feedback_sample_rate: The percentage of successful message deliveries to be logged in Amazon CloudWatch. Valid percentage values range from 0 to 100.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sns-topic-loggingconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sns as sns
                
                logging_config_property = sns.CfnTopic.LoggingConfigProperty(
                    protocol="protocol",
                
                    # the properties below are optional
                    failure_feedback_role_arn="failureFeedbackRoleArn",
                    success_feedback_role_arn="successFeedbackRoleArn",
                    success_feedback_sample_rate="successFeedbackSampleRate"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__504f5c0a818ef27c6f26af4cf94e85376e3929a210ed0fc76e17575e3a997054)
                check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
                check_type(argname="argument failure_feedback_role_arn", value=failure_feedback_role_arn, expected_type=type_hints["failure_feedback_role_arn"])
                check_type(argname="argument success_feedback_role_arn", value=success_feedback_role_arn, expected_type=type_hints["success_feedback_role_arn"])
                check_type(argname="argument success_feedback_sample_rate", value=success_feedback_sample_rate, expected_type=type_hints["success_feedback_sample_rate"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "protocol": protocol,
            }
            if failure_feedback_role_arn is not None:
                self._values["failure_feedback_role_arn"] = failure_feedback_role_arn
            if success_feedback_role_arn is not None:
                self._values["success_feedback_role_arn"] = success_feedback_role_arn
            if success_feedback_sample_rate is not None:
                self._values["success_feedback_sample_rate"] = success_feedback_sample_rate

        @builtins.property
        def protocol(self) -> builtins.str:
            '''Indicates one of the supported protocols for the Amazon SNS topic.

            .. epigraph::

               At least one of the other three ``LoggingConfig`` properties is recommend along with ``Protocol`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sns-topic-loggingconfig.html#cfn-sns-topic-loggingconfig-protocol
            '''
            result = self._values.get("protocol")
            assert result is not None, "Required property 'protocol' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def failure_feedback_role_arn(self) -> typing.Optional[builtins.str]:
            '''The IAM role ARN to be used when logging failed message deliveries in Amazon CloudWatch.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sns-topic-loggingconfig.html#cfn-sns-topic-loggingconfig-failurefeedbackrolearn
            '''
            result = self._values.get("failure_feedback_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def success_feedback_role_arn(self) -> typing.Optional[builtins.str]:
            '''The IAM role ARN to be used when logging successful message deliveries in Amazon CloudWatch.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sns-topic-loggingconfig.html#cfn-sns-topic-loggingconfig-successfeedbackrolearn
            '''
            result = self._values.get("success_feedback_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def success_feedback_sample_rate(self) -> typing.Optional[builtins.str]:
            '''The percentage of successful message deliveries to be logged in Amazon CloudWatch.

            Valid percentage values range from 0 to 100.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sns-topic-loggingconfig.html#cfn-sns-topic-loggingconfig-successfeedbacksamplerate
            '''
            result = self._values.get("success_feedback_sample_rate")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoggingConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sns.CfnTopic.SubscriptionProperty",
        jsii_struct_bases=[],
        name_mapping={"endpoint": "endpoint", "protocol": "protocol"},
    )
    class SubscriptionProperty:
        def __init__(self, *, endpoint: builtins.str, protocol: builtins.str) -> None:
            '''``Subscription`` is an embedded property that describes the subscription endpoints of an Amazon SNS topic.

            .. epigraph::

               For full control over subscription behavior (for example, delivery policy, filtering, raw message delivery, and cross-region subscriptions), use the `AWS::SNS::Subscription <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-subscription.html>`_ resource.

            :param endpoint: The endpoint that receives notifications from the Amazon SNS topic. The endpoint value depends on the protocol that you specify. For more information, see the ``Endpoint`` parameter of the ``[Subscribe](https://docs.aws.amazon.com/sns/latest/api/API_Subscribe.html)`` action in the *Amazon SNS API Reference* .
            :param protocol: The subscription's protocol. For more information, see the ``Protocol`` parameter of the ``[Subscribe](https://docs.aws.amazon.com/sns/latest/api/API_Subscribe.html)`` action in the *Amazon SNS API Reference* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sns-topic-subscription.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sns as sns
                
                subscription_property = sns.CfnTopic.SubscriptionProperty(
                    endpoint="endpoint",
                    protocol="protocol"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b0e99e91f630467ca29bdde2bfed1506da130d5f3e0cae1685b42e10bf0537dc)
                check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
                check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "endpoint": endpoint,
                "protocol": protocol,
            }

        @builtins.property
        def endpoint(self) -> builtins.str:
            '''The endpoint that receives notifications from the Amazon SNS topic.

            The endpoint value depends on the protocol that you specify. For more information, see the ``Endpoint`` parameter of the ``[Subscribe](https://docs.aws.amazon.com/sns/latest/api/API_Subscribe.html)`` action in the *Amazon SNS API Reference* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sns-topic-subscription.html#cfn-sns-topic-subscription-endpoint
            '''
            result = self._values.get("endpoint")
            assert result is not None, "Required property 'endpoint' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def protocol(self) -> builtins.str:
            '''The subscription's protocol.

            For more information, see the ``Protocol`` parameter of the ``[Subscribe](https://docs.aws.amazon.com/sns/latest/api/API_Subscribe.html)`` action in the *Amazon SNS API Reference* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sns-topic-subscription.html#cfn-sns-topic-subscription-protocol
            '''
            result = self._values.get("protocol")
            assert result is not None, "Required property 'protocol' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SubscriptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556)
class CfnTopicInlinePolicy(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_sns.CfnTopicInlinePolicy",
):
    '''The ``AWS::SNS::TopicInlinePolicy`` resource associates one Amazon SNS topic with one policy.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-topicinlinepolicy.html
    :cloudformationResource: AWS::SNS::TopicInlinePolicy
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_sns as sns
        
        # policy_document: Any
        
        cfn_topic_inline_policy = sns.CfnTopicInlinePolicy(self, "MyCfnTopicInlinePolicy",
            policy_document=policy_document,
            topic_arn="topicArn"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        policy_document: typing.Any,
        topic_arn: builtins.str,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param policy_document: A policy document that contains permissions to add to the specified Amazon SNS topic.
        :param topic_arn: The Amazon Resource Name (ARN) of the topic to which you want to add the policy.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc6ea227f85a0ee7689700544a9f92c1220134ca2d2baa5667c368181a9e8a32)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnTopicInlinePolicyProps(
            policy_document=policy_document, topic_arn=topic_arn
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__068f56f45055c0013d26c4ff1b8eba591d1ba7fde252cbc1a41c85476969cd0a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__de3f18c32c20096788214fcc04b3e4bd211654412293d35e75c91ceee4ce8bfb)
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
    @jsii.member(jsii_name="policyDocument")
    def policy_document(self) -> typing.Any:
        '''A policy document that contains permissions to add to the specified Amazon SNS topic.'''
        return typing.cast(typing.Any, jsii.get(self, "policyDocument"))

    @policy_document.setter
    def policy_document(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8275626d8b21f671694dcee09744c4e6b75f065ed837225bf415305c04b7b7ed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyDocument", value)

    @builtins.property
    @jsii.member(jsii_name="topicArn")
    def topic_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the topic to which you want to add the policy.'''
        return typing.cast(builtins.str, jsii.get(self, "topicArn"))

    @topic_arn.setter
    def topic_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7fb2268d3e7860e0e1aef3261e22ab7f2e0f8f6a170f6dc068791cef3502c7d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "topicArn", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_sns.CfnTopicInlinePolicyProps",
    jsii_struct_bases=[],
    name_mapping={"policy_document": "policyDocument", "topic_arn": "topicArn"},
)
class CfnTopicInlinePolicyProps:
    def __init__(self, *, policy_document: typing.Any, topic_arn: builtins.str) -> None:
        '''Properties for defining a ``CfnTopicInlinePolicy``.

        :param policy_document: A policy document that contains permissions to add to the specified Amazon SNS topic.
        :param topic_arn: The Amazon Resource Name (ARN) of the topic to which you want to add the policy.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-topicinlinepolicy.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_sns as sns
            
            # policy_document: Any
            
            cfn_topic_inline_policy_props = sns.CfnTopicInlinePolicyProps(
                policy_document=policy_document,
                topic_arn="topicArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cdf37eb1dc6c7082cc2dd899c6b1f40d17fbd1563f692e9ea9111bd824ec9dad)
            check_type(argname="argument policy_document", value=policy_document, expected_type=type_hints["policy_document"])
            check_type(argname="argument topic_arn", value=topic_arn, expected_type=type_hints["topic_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "policy_document": policy_document,
            "topic_arn": topic_arn,
        }

    @builtins.property
    def policy_document(self) -> typing.Any:
        '''A policy document that contains permissions to add to the specified Amazon SNS topic.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-topicinlinepolicy.html#cfn-sns-topicinlinepolicy-policydocument
        '''
        result = self._values.get("policy_document")
        assert result is not None, "Required property 'policy_document' is missing"
        return typing.cast(typing.Any, result)

    @builtins.property
    def topic_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the topic to which you want to add the policy.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-topicinlinepolicy.html#cfn-sns-topicinlinepolicy-topicarn
        '''
        result = self._values.get("topic_arn")
        assert result is not None, "Required property 'topic_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTopicInlinePolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnTopicPolicy(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_sns.CfnTopicPolicy",
):
    '''The ``AWS::SNS::TopicPolicy`` resource associates Amazon SNS topics with a policy.

    For an example snippet, see `Declaring an Amazon SNS policy <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-iam.html#scenario-sns-policy>`_ in the *AWS CloudFormation User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-topicpolicy.html
    :cloudformationResource: AWS::SNS::TopicPolicy
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_sns as sns
        
        # policy_document: Any
        
        cfn_topic_policy = sns.CfnTopicPolicy(self, "MyCfnTopicPolicy",
            policy_document=policy_document,
            topics=["topics"]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        policy_document: typing.Any,
        topics: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param policy_document: A policy document that contains permissions to add to the specified SNS topics.
        :param topics: The Amazon Resource Names (ARN) of the topics to which you want to add the policy. You can use the ``[Ref](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.html)`` function to specify an ``[AWS::SNS::Topic](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-topic.html)`` resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a74b2018f34253c91ec670526565616a2473df25a6a5108c2fbafc189dd5ce18)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnTopicPolicyProps(policy_document=policy_document, topics=topics)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6ae43fa297025629494d67fe989386d5dddecd1473f7e43bff2e1d5fc227000)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0733bdab832ad72cd8bd92fba796973a855911ccc2927c3343a635279052687c)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The provider-assigned unique ID for this managed resource.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="policyDocument")
    def policy_document(self) -> typing.Any:
        '''A policy document that contains permissions to add to the specified SNS topics.'''
        return typing.cast(typing.Any, jsii.get(self, "policyDocument"))

    @policy_document.setter
    def policy_document(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d6879a3cebc5ad4daeee6ede4d90bd5183664f6abf021b475aa5d9fc535c10c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyDocument", value)

    @builtins.property
    @jsii.member(jsii_name="topics")
    def topics(self) -> typing.List[builtins.str]:
        '''The Amazon Resource Names (ARN) of the topics to which you want to add the policy.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "topics"))

    @topics.setter
    def topics(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4eb0294b972b7ccbe6bd3a88c438e8d519ab90fa35e136b6b4272a65abd4db0a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "topics", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_sns.CfnTopicPolicyProps",
    jsii_struct_bases=[],
    name_mapping={"policy_document": "policyDocument", "topics": "topics"},
)
class CfnTopicPolicyProps:
    def __init__(
        self,
        *,
        policy_document: typing.Any,
        topics: typing.Sequence[builtins.str],
    ) -> None:
        '''Properties for defining a ``CfnTopicPolicy``.

        :param policy_document: A policy document that contains permissions to add to the specified SNS topics.
        :param topics: The Amazon Resource Names (ARN) of the topics to which you want to add the policy. You can use the ``[Ref](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.html)`` function to specify an ``[AWS::SNS::Topic](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-topic.html)`` resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-topicpolicy.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_sns as sns
            
            # policy_document: Any
            
            cfn_topic_policy_props = sns.CfnTopicPolicyProps(
                policy_document=policy_document,
                topics=["topics"]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1894bd2779686bb602d2a76bb004026f405ddb9d5ec17e6982a4da918e8a1a9f)
            check_type(argname="argument policy_document", value=policy_document, expected_type=type_hints["policy_document"])
            check_type(argname="argument topics", value=topics, expected_type=type_hints["topics"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "policy_document": policy_document,
            "topics": topics,
        }

    @builtins.property
    def policy_document(self) -> typing.Any:
        '''A policy document that contains permissions to add to the specified SNS topics.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-topicpolicy.html#cfn-sns-topicpolicy-policydocument
        '''
        result = self._values.get("policy_document")
        assert result is not None, "Required property 'policy_document' is missing"
        return typing.cast(typing.Any, result)

    @builtins.property
    def topics(self) -> typing.List[builtins.str]:
        '''The Amazon Resource Names (ARN) of the topics to which you want to add the policy.

        You can use the ``[Ref](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.html)`` function to specify an ``[AWS::SNS::Topic](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-topic.html)`` resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-topicpolicy.html#cfn-sns-topicpolicy-topics
        '''
        result = self._values.get("topics")
        assert result is not None, "Required property 'topics' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTopicPolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_sns.CfnTopicProps",
    jsii_struct_bases=[],
    name_mapping={
        "archive_policy": "archivePolicy",
        "content_based_deduplication": "contentBasedDeduplication",
        "data_protection_policy": "dataProtectionPolicy",
        "delivery_status_logging": "deliveryStatusLogging",
        "display_name": "displayName",
        "fifo_topic": "fifoTopic",
        "kms_master_key_id": "kmsMasterKeyId",
        "signature_version": "signatureVersion",
        "subscription": "subscription",
        "tags": "tags",
        "topic_name": "topicName",
        "tracing_config": "tracingConfig",
    },
)
class CfnTopicProps:
    def __init__(
        self,
        *,
        archive_policy: typing.Any = None,
        content_based_deduplication: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        data_protection_policy: typing.Any = None,
        delivery_status_logging: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTopic.LoggingConfigProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        display_name: typing.Optional[builtins.str] = None,
        fifo_topic: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        kms_master_key_id: typing.Optional[builtins.str] = None,
        signature_version: typing.Optional[builtins.str] = None,
        subscription: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTopic.SubscriptionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        topic_name: typing.Optional[builtins.str] = None,
        tracing_config: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnTopic``.

        :param archive_policy: The archive policy determines the number of days Amazon SNS retains messages. You can set a retention period from 1 to 365 days.
        :param content_based_deduplication: Enables content-based deduplication for FIFO topics. - By default, ``ContentBasedDeduplication`` is set to ``false`` . If you create a FIFO topic and this attribute is ``false`` , you must specify a value for the ``MessageDeduplicationId`` parameter for the `Publish <https://docs.aws.amazon.com/sns/latest/api/API_Publish.html>`_ action. - When you set ``ContentBasedDeduplication`` to ``true`` , Amazon SNS uses a SHA-256 hash to generate the ``MessageDeduplicationId`` using the body of the message (but not the attributes of the message). (Optional) To override the generated value, you can specify a value for the the ``MessageDeduplicationId`` parameter for the ``Publish`` action.
        :param data_protection_policy: The body of the policy document you want to use for this topic. You can only add one policy per topic. The policy must be in JSON string format. Length Constraints: Maximum length of 30,720.
        :param delivery_status_logging: The ``DeliveryStatusLogging`` configuration enables you to log the delivery status of messages sent from your Amazon SNS topic to subscribed endpoints with the following supported delivery protocols:. - HTTP - Amazon Kinesis Data Firehose - AWS Lambda - Platform application endpoint - Amazon Simple Queue Service Once configured, log entries are sent to Amazon CloudWatch Logs.
        :param display_name: The display name to use for an Amazon SNS topic with SMS subscriptions. The display name must be maximum 100 characters long, including hyphens (-), underscores (_), spaces, and tabs.
        :param fifo_topic: Set to true to create a FIFO topic.
        :param kms_master_key_id: The ID of an AWS managed customer master key (CMK) for Amazon SNS or a custom CMK. For more information, see `Key terms <https://docs.aws.amazon.com/sns/latest/dg/sns-server-side-encryption.html#sse-key-terms>`_ . For more examples, see ``[KeyId](https://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeKey.html#API_DescribeKey_RequestParameters)`` in the *AWS Key Management Service API Reference* . This property applies only to `server-side-encryption <https://docs.aws.amazon.com/sns/latest/dg/sns-server-side-encryption.html>`_ .
        :param signature_version: The signature version corresponds to the hashing algorithm used while creating the signature of the notifications, subscription confirmations, or unsubscribe confirmation messages sent by Amazon SNS. By default, ``SignatureVersion`` is set to ``1`` .
        :param subscription: The Amazon SNS subscriptions (endpoints) for this topic. .. epigraph:: If you specify the ``Subscription`` property in the ``AWS::SNS::Topic`` resource and it creates an associated subscription resource, the associated subscription is not deleted when the ``AWS::SNS::Topic`` resource is deleted.
        :param tags: The list of tags to add to a new topic. .. epigraph:: To be able to tag a topic on creation, you must have the ``sns:CreateTopic`` and ``sns:TagResource`` permissions.
        :param topic_name: The name of the topic you want to create. Topic names must include only uppercase and lowercase ASCII letters, numbers, underscores, and hyphens, and must be between 1 and 256 characters long. FIFO topic names must end with ``.fifo`` . If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the topic name. For more information, see `Name type <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html>`_ . .. epigraph:: If you specify a name, you can't perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.
        :param tracing_config: Tracing mode of an Amazon SNS topic. By default ``TracingConfig`` is set to ``PassThrough`` , and the topic passes through the tracing header it receives from an Amazon SNS publisher to its subscriptions. If set to ``Active`` , Amazon SNS will vend X-Ray segment data to topic owner account if the sampled flag in the tracing header is true.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-topic.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_sns as sns
            
            # archive_policy: Any
            # data_protection_policy: Any
            
            cfn_topic_props = sns.CfnTopicProps(
                archive_policy=archive_policy,
                content_based_deduplication=False,
                data_protection_policy=data_protection_policy,
                delivery_status_logging=[sns.CfnTopic.LoggingConfigProperty(
                    protocol="protocol",
            
                    # the properties below are optional
                    failure_feedback_role_arn="failureFeedbackRoleArn",
                    success_feedback_role_arn="successFeedbackRoleArn",
                    success_feedback_sample_rate="successFeedbackSampleRate"
                )],
                display_name="displayName",
                fifo_topic=False,
                kms_master_key_id="kmsMasterKeyId",
                signature_version="signatureVersion",
                subscription=[sns.CfnTopic.SubscriptionProperty(
                    endpoint="endpoint",
                    protocol="protocol"
                )],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                topic_name="topicName",
                tracing_config="tracingConfig"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39eaeffb1fed865d99c7cf51cdf720d8471aec20b2163161ef50035fbeafbf13)
            check_type(argname="argument archive_policy", value=archive_policy, expected_type=type_hints["archive_policy"])
            check_type(argname="argument content_based_deduplication", value=content_based_deduplication, expected_type=type_hints["content_based_deduplication"])
            check_type(argname="argument data_protection_policy", value=data_protection_policy, expected_type=type_hints["data_protection_policy"])
            check_type(argname="argument delivery_status_logging", value=delivery_status_logging, expected_type=type_hints["delivery_status_logging"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument fifo_topic", value=fifo_topic, expected_type=type_hints["fifo_topic"])
            check_type(argname="argument kms_master_key_id", value=kms_master_key_id, expected_type=type_hints["kms_master_key_id"])
            check_type(argname="argument signature_version", value=signature_version, expected_type=type_hints["signature_version"])
            check_type(argname="argument subscription", value=subscription, expected_type=type_hints["subscription"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument topic_name", value=topic_name, expected_type=type_hints["topic_name"])
            check_type(argname="argument tracing_config", value=tracing_config, expected_type=type_hints["tracing_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if archive_policy is not None:
            self._values["archive_policy"] = archive_policy
        if content_based_deduplication is not None:
            self._values["content_based_deduplication"] = content_based_deduplication
        if data_protection_policy is not None:
            self._values["data_protection_policy"] = data_protection_policy
        if delivery_status_logging is not None:
            self._values["delivery_status_logging"] = delivery_status_logging
        if display_name is not None:
            self._values["display_name"] = display_name
        if fifo_topic is not None:
            self._values["fifo_topic"] = fifo_topic
        if kms_master_key_id is not None:
            self._values["kms_master_key_id"] = kms_master_key_id
        if signature_version is not None:
            self._values["signature_version"] = signature_version
        if subscription is not None:
            self._values["subscription"] = subscription
        if tags is not None:
            self._values["tags"] = tags
        if topic_name is not None:
            self._values["topic_name"] = topic_name
        if tracing_config is not None:
            self._values["tracing_config"] = tracing_config

    @builtins.property
    def archive_policy(self) -> typing.Any:
        '''The archive policy determines the number of days Amazon SNS retains messages.

        You can set a retention period from 1 to 365 days.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-topic.html#cfn-sns-topic-archivepolicy
        '''
        result = self._values.get("archive_policy")
        return typing.cast(typing.Any, result)

    @builtins.property
    def content_based_deduplication(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Enables content-based deduplication for FIFO topics.

        - By default, ``ContentBasedDeduplication`` is set to ``false`` . If you create a FIFO topic and this attribute is ``false`` , you must specify a value for the ``MessageDeduplicationId`` parameter for the `Publish <https://docs.aws.amazon.com/sns/latest/api/API_Publish.html>`_ action.
        - When you set ``ContentBasedDeduplication`` to ``true`` , Amazon SNS uses a SHA-256 hash to generate the ``MessageDeduplicationId`` using the body of the message (but not the attributes of the message).

        (Optional) To override the generated value, you can specify a value for the the ``MessageDeduplicationId`` parameter for the ``Publish`` action.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-topic.html#cfn-sns-topic-contentbaseddeduplication
        '''
        result = self._values.get("content_based_deduplication")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def data_protection_policy(self) -> typing.Any:
        '''The body of the policy document you want to use for this topic.

        You can only add one policy per topic.

        The policy must be in JSON string format.

        Length Constraints: Maximum length of 30,720.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-topic.html#cfn-sns-topic-dataprotectionpolicy
        '''
        result = self._values.get("data_protection_policy")
        return typing.cast(typing.Any, result)

    @builtins.property
    def delivery_status_logging(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnTopic.LoggingConfigProperty]]]]:
        '''The ``DeliveryStatusLogging`` configuration enables you to log the delivery status of messages sent from your Amazon SNS topic to subscribed endpoints with the following supported delivery protocols:.

        - HTTP
        - Amazon Kinesis Data Firehose
        - AWS Lambda
        - Platform application endpoint
        - Amazon Simple Queue Service

        Once configured, log entries are sent to Amazon CloudWatch Logs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-topic.html#cfn-sns-topic-deliverystatuslogging
        '''
        result = self._values.get("delivery_status_logging")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnTopic.LoggingConfigProperty]]]], result)

    @builtins.property
    def display_name(self) -> typing.Optional[builtins.str]:
        '''The display name to use for an Amazon SNS topic with SMS subscriptions.

        The display name must be maximum 100 characters long, including hyphens (-), underscores (_), spaces, and tabs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-topic.html#cfn-sns-topic-displayname
        '''
        result = self._values.get("display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def fifo_topic(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Set to true to create a FIFO topic.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-topic.html#cfn-sns-topic-fifotopic
        '''
        result = self._values.get("fifo_topic")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def kms_master_key_id(self) -> typing.Optional[builtins.str]:
        '''The ID of an AWS managed customer master key (CMK) for Amazon SNS or a custom CMK.

        For more information, see `Key terms <https://docs.aws.amazon.com/sns/latest/dg/sns-server-side-encryption.html#sse-key-terms>`_ . For more examples, see ``[KeyId](https://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeKey.html#API_DescribeKey_RequestParameters)`` in the *AWS Key Management Service API Reference* .

        This property applies only to `server-side-encryption <https://docs.aws.amazon.com/sns/latest/dg/sns-server-side-encryption.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-topic.html#cfn-sns-topic-kmsmasterkeyid
        '''
        result = self._values.get("kms_master_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def signature_version(self) -> typing.Optional[builtins.str]:
        '''The signature version corresponds to the hashing algorithm used while creating the signature of the notifications, subscription confirmations, or unsubscribe confirmation messages sent by Amazon SNS.

        By default, ``SignatureVersion`` is set to ``1`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-topic.html#cfn-sns-topic-signatureversion
        '''
        result = self._values.get("signature_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subscription(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnTopic.SubscriptionProperty]]]]:
        '''The Amazon SNS subscriptions (endpoints) for this topic.

        .. epigraph::

           If you specify the ``Subscription`` property in the ``AWS::SNS::Topic`` resource and it creates an associated subscription resource, the associated subscription is not deleted when the ``AWS::SNS::Topic`` resource is deleted.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-topic.html#cfn-sns-topic-subscription
        '''
        result = self._values.get("subscription")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnTopic.SubscriptionProperty]]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The list of tags to add to a new topic.

        .. epigraph::

           To be able to tag a topic on creation, you must have the ``sns:CreateTopic`` and ``sns:TagResource`` permissions.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-topic.html#cfn-sns-topic-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def topic_name(self) -> typing.Optional[builtins.str]:
        '''The name of the topic you want to create.

        Topic names must include only uppercase and lowercase ASCII letters, numbers, underscores, and hyphens, and must be between 1 and 256 characters long. FIFO topic names must end with ``.fifo`` .

        If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the topic name. For more information, see `Name type <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html>`_ .
        .. epigraph::

           If you specify a name, you can't perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-topic.html#cfn-sns-topic-topicname
        '''
        result = self._values.get("topic_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tracing_config(self) -> typing.Optional[builtins.str]:
        '''Tracing mode of an Amazon SNS topic.

        By default ``TracingConfig`` is set to ``PassThrough`` , and the topic passes through the tracing header it receives from an Amazon SNS publisher to its subscriptions. If set to ``Active`` , Amazon SNS will vend X-Ray segment data to topic owner account if the sampled flag in the tracing header is true.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-topic.html#cfn-sns-topic-tracingconfig
        '''
        result = self._values.get("tracing_config")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTopicProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FilterOrPolicy(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="aws-cdk-lib.aws_sns.FilterOrPolicy",
):
    '''Class for building the FilterPolicy by avoiding union types.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_lambda as lambda_
        # fn: lambda.Function
        
        
        my_topic = sns.Topic(self, "MyTopic")
        
        # Lambda should receive only message matching the following conditions on message body:
        # color: 'red' or 'orange'
        my_topic.add_subscription(subscriptions.LambdaSubscription(fn,
            filter_policy_with_message_body={
                "background": sns.FilterOrPolicy.policy({
                    "color": sns.FilterOrPolicy.filter(sns.SubscriptionFilter.string_filter(
                        allowlist=["red", "orange"]
                    ))
                })
            }
        ))
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="filter")
    @builtins.classmethod
    def filter(cls, filter: "SubscriptionFilter") -> "Filter":
        '''Filter of MessageBody.

        :param filter: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48b960a8d07778472d280833dc7671d5e58991a28e7dd556c9d0aaf7509fb28e)
            check_type(argname="argument filter", value=filter, expected_type=type_hints["filter"])
        return typing.cast("Filter", jsii.sinvoke(cls, "filter", [filter]))

    @jsii.member(jsii_name="policy")
    @builtins.classmethod
    def policy(cls, policy: typing.Mapping[builtins.str, "FilterOrPolicy"]) -> "Policy":
        '''Policy of MessageBody.

        :param policy: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3bfe2da643ae34d8de4bb104c40157d580fd7cce715aa1fe916f39f1922887f1)
            check_type(argname="argument policy", value=policy, expected_type=type_hints["policy"])
        return typing.cast("Policy", jsii.sinvoke(cls, "policy", [policy]))

    @jsii.member(jsii_name="isFilter")
    def is_filter(self) -> builtins.bool:
        '''Check if instance is ``Filter`` type.'''
        return typing.cast(builtins.bool, jsii.invoke(self, "isFilter", []))

    @jsii.member(jsii_name="isPolicy")
    def is_policy(self) -> builtins.bool:
        '''Check if instance is ``Policy`` type.'''
        return typing.cast(builtins.bool, jsii.invoke(self, "isPolicy", []))

    @builtins.property
    @jsii.member(jsii_name="type")
    @abc.abstractmethod
    def type(self) -> "FilterOrPolicyType":
        '''Type switch for disambiguating between subclasses.'''
        ...


class _FilterOrPolicyProxy(FilterOrPolicy):
    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> "FilterOrPolicyType":
        '''Type switch for disambiguating between subclasses.'''
        return typing.cast("FilterOrPolicyType", jsii.get(self, "type"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, FilterOrPolicy).__jsii_proxy_class__ = lambda : _FilterOrPolicyProxy


@jsii.enum(jsii_type="aws-cdk-lib.aws_sns.FilterOrPolicyType")
class FilterOrPolicyType(enum.Enum):
    '''The type of the MessageBody at a given key value pair.'''

    FILTER = "FILTER"
    '''The filter of the MessageBody.'''
    POLICY = "POLICY"
    '''A nested key of the MessageBody.'''


@jsii.interface(jsii_type="aws-cdk-lib.aws_sns.ITopic")
class ITopic(
    _IResource_c80c4260,
    _INotificationRuleTarget_faa3b79b,
    typing_extensions.Protocol,
):
    '''Represents an SNS topic.'''

    @builtins.property
    @jsii.member(jsii_name="contentBasedDeduplication")
    def content_based_deduplication(self) -> builtins.bool:
        '''Enables content-based deduplication for FIFO topics.

        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="fifo")
    def fifo(self) -> builtins.bool:
        '''Whether this topic is an Amazon SNS FIFO queue.

        If false, this is a standard topic.

        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="topicArn")
    def topic_arn(self) -> builtins.str:
        '''The ARN of the topic.

        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="topicName")
    def topic_name(self) -> builtins.str:
        '''The name of the topic.

        :attribute: true
        '''
        ...

    @jsii.member(jsii_name="addSubscription")
    def add_subscription(self, subscription: "ITopicSubscription") -> "Subscription":
        '''Subscribe some endpoint to this topic.

        :param subscription: -
        '''
        ...

    @jsii.member(jsii_name="addToResourcePolicy")
    def add_to_resource_policy(
        self,
        statement: _PolicyStatement_0fe33853,
    ) -> _AddToResourcePolicyResult_1d0a53ad:
        '''Adds a statement to the IAM resource policy associated with this topic.

        If this topic was created in this stack (``new Topic``), a topic policy
        will be automatically created upon the first call to ``addToResourcePolicy``. If
        the topic is imported (``Topic.import``), then this is a no-op.

        :param statement: -
        '''
        ...

    @jsii.member(jsii_name="grantPublish")
    def grant_publish(self, identity: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant topic publishing permissions to the given identity.

        :param identity: -
        '''
        ...

    @jsii.member(jsii_name="metric")
    def metric(
        self,
        metric_name: builtins.str,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''Return the given named metric for this Topic.

        :param metric_name: -
        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        '''
        ...

    @jsii.member(jsii_name="metricNumberOfMessagesPublished")
    def metric_number_of_messages_published(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''The number of messages published to your Amazon SNS topics.

        Sum over 5 minutes

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        '''
        ...

    @jsii.member(jsii_name="metricNumberOfNotificationsDelivered")
    def metric_number_of_notifications_delivered(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''The number of messages successfully delivered from your Amazon SNS topics to subscribing endpoints.

        Sum over 5 minutes

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        '''
        ...

    @jsii.member(jsii_name="metricNumberOfNotificationsFailed")
    def metric_number_of_notifications_failed(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''The number of messages that Amazon SNS failed to deliver.

        Sum over 5 minutes

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        '''
        ...

    @jsii.member(jsii_name="metricNumberOfNotificationsFilteredOut")
    def metric_number_of_notifications_filtered_out(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''The number of messages that were rejected by subscription filter policies.

        Sum over 5 minutes

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        '''
        ...

    @jsii.member(jsii_name="metricNumberOfNotificationsFilteredOutInvalidAttributes")
    def metric_number_of_notifications_filtered_out_invalid_attributes(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''The number of messages that were rejected by subscription filter policies because the messages' attributes are invalid.

        Sum over 5 minutes

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        '''
        ...

    @jsii.member(jsii_name="metricNumberOfNotificationsFilteredOutNoMessageAttributes")
    def metric_number_of_notifications_filtered_out_no_message_attributes(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''The number of messages that were rejected by subscription filter policies because the messages have no attributes.

        Sum over 5 minutes

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        '''
        ...

    @jsii.member(jsii_name="metricPublishSize")
    def metric_publish_size(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''Metric for the size of messages published through this topic.

        Average over 5 minutes

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        '''
        ...

    @jsii.member(jsii_name="metricSMSMonthToDateSpentUSD")
    def metric_sms_month_to_date_spent_usd(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''The charges you have accrued since the start of the current calendar month for sending SMS messages.

        Maximum over 5 minutes

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        '''
        ...

    @jsii.member(jsii_name="metricSMSSuccessRate")
    def metric_sms_success_rate(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''The rate of successful SMS message deliveries.

        Sum over 5 minutes

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        '''
        ...


class _ITopicProxy(
    jsii.proxy_for(_IResource_c80c4260), # type: ignore[misc]
    jsii.proxy_for(_INotificationRuleTarget_faa3b79b), # type: ignore[misc]
):
    '''Represents an SNS topic.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_sns.ITopic"

    @builtins.property
    @jsii.member(jsii_name="contentBasedDeduplication")
    def content_based_deduplication(self) -> builtins.bool:
        '''Enables content-based deduplication for FIFO topics.

        :attribute: true
        '''
        return typing.cast(builtins.bool, jsii.get(self, "contentBasedDeduplication"))

    @builtins.property
    @jsii.member(jsii_name="fifo")
    def fifo(self) -> builtins.bool:
        '''Whether this topic is an Amazon SNS FIFO queue.

        If false, this is a standard topic.

        :attribute: true
        '''
        return typing.cast(builtins.bool, jsii.get(self, "fifo"))

    @builtins.property
    @jsii.member(jsii_name="topicArn")
    def topic_arn(self) -> builtins.str:
        '''The ARN of the topic.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "topicArn"))

    @builtins.property
    @jsii.member(jsii_name="topicName")
    def topic_name(self) -> builtins.str:
        '''The name of the topic.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "topicName"))

    @jsii.member(jsii_name="addSubscription")
    def add_subscription(self, subscription: "ITopicSubscription") -> "Subscription":
        '''Subscribe some endpoint to this topic.

        :param subscription: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3254ccc49f43f33130f11f9db98dd8a000762fcec4aeed1d0e619180d6590c66)
            check_type(argname="argument subscription", value=subscription, expected_type=type_hints["subscription"])
        return typing.cast("Subscription", jsii.invoke(self, "addSubscription", [subscription]))

    @jsii.member(jsii_name="addToResourcePolicy")
    def add_to_resource_policy(
        self,
        statement: _PolicyStatement_0fe33853,
    ) -> _AddToResourcePolicyResult_1d0a53ad:
        '''Adds a statement to the IAM resource policy associated with this topic.

        If this topic was created in this stack (``new Topic``), a topic policy
        will be automatically created upon the first call to ``addToResourcePolicy``. If
        the topic is imported (``Topic.import``), then this is a no-op.

        :param statement: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a25cf01212afa98a52126c366524ccb1dfcf92425078abf30316c0b680f26307)
            check_type(argname="argument statement", value=statement, expected_type=type_hints["statement"])
        return typing.cast(_AddToResourcePolicyResult_1d0a53ad, jsii.invoke(self, "addToResourcePolicy", [statement]))

    @jsii.member(jsii_name="grantPublish")
    def grant_publish(self, identity: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant topic publishing permissions to the given identity.

        :param identity: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf96d0b079cfedfe1ad406a08f2229f4ed5332b9d92fc6d78e1571fce3a1ee5f)
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantPublish", [identity]))

    @jsii.member(jsii_name="metric")
    def metric(
        self,
        metric_name: builtins.str,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''Return the given named metric for this Topic.

        :param metric_name: -
        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05c3997edd40866d6774aed03c03e55b6cf80f23f518be34bcdf19adf065db7c)
            check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
        props = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metric", [metric_name, props]))

    @jsii.member(jsii_name="metricNumberOfMessagesPublished")
    def metric_number_of_messages_published(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''The number of messages published to your Amazon SNS topics.

        Sum over 5 minutes

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        '''
        props = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricNumberOfMessagesPublished", [props]))

    @jsii.member(jsii_name="metricNumberOfNotificationsDelivered")
    def metric_number_of_notifications_delivered(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''The number of messages successfully delivered from your Amazon SNS topics to subscribing endpoints.

        Sum over 5 minutes

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        '''
        props = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricNumberOfNotificationsDelivered", [props]))

    @jsii.member(jsii_name="metricNumberOfNotificationsFailed")
    def metric_number_of_notifications_failed(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''The number of messages that Amazon SNS failed to deliver.

        Sum over 5 minutes

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        '''
        props = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricNumberOfNotificationsFailed", [props]))

    @jsii.member(jsii_name="metricNumberOfNotificationsFilteredOut")
    def metric_number_of_notifications_filtered_out(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''The number of messages that were rejected by subscription filter policies.

        Sum over 5 minutes

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        '''
        props = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricNumberOfNotificationsFilteredOut", [props]))

    @jsii.member(jsii_name="metricNumberOfNotificationsFilteredOutInvalidAttributes")
    def metric_number_of_notifications_filtered_out_invalid_attributes(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''The number of messages that were rejected by subscription filter policies because the messages' attributes are invalid.

        Sum over 5 minutes

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        '''
        props = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricNumberOfNotificationsFilteredOutInvalidAttributes", [props]))

    @jsii.member(jsii_name="metricNumberOfNotificationsFilteredOutNoMessageAttributes")
    def metric_number_of_notifications_filtered_out_no_message_attributes(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''The number of messages that were rejected by subscription filter policies because the messages have no attributes.

        Sum over 5 minutes

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        '''
        props = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricNumberOfNotificationsFilteredOutNoMessageAttributes", [props]))

    @jsii.member(jsii_name="metricPublishSize")
    def metric_publish_size(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''Metric for the size of messages published through this topic.

        Average over 5 minutes

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        '''
        props = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricPublishSize", [props]))

    @jsii.member(jsii_name="metricSMSMonthToDateSpentUSD")
    def metric_sms_month_to_date_spent_usd(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''The charges you have accrued since the start of the current calendar month for sending SMS messages.

        Maximum over 5 minutes

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        '''
        props = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricSMSMonthToDateSpentUSD", [props]))

    @jsii.member(jsii_name="metricSMSSuccessRate")
    def metric_sms_success_rate(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''The rate of successful SMS message deliveries.

        Sum over 5 minutes

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        '''
        props = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricSMSSuccessRate", [props]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITopic).__jsii_proxy_class__ = lambda : _ITopicProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_sns.ITopicSubscription")
class ITopicSubscription(typing_extensions.Protocol):
    '''Topic subscription.'''

    @jsii.member(jsii_name="bind")
    def bind(self, topic: ITopic) -> "TopicSubscriptionConfig":
        '''Returns a configuration used to subscribe to an SNS topic.

        :param topic: topic for which subscription will be configured.
        '''
        ...


class _ITopicSubscriptionProxy:
    '''Topic subscription.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_sns.ITopicSubscription"

    @jsii.member(jsii_name="bind")
    def bind(self, topic: ITopic) -> "TopicSubscriptionConfig":
        '''Returns a configuration used to subscribe to an SNS topic.

        :param topic: topic for which subscription will be configured.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__daf70c7f74db8d44ef157cdd3df3a90e91ac1b55f6be3c7ec557b2c6d285720a)
            check_type(argname="argument topic", value=topic, expected_type=type_hints["topic"])
        return typing.cast("TopicSubscriptionConfig", jsii.invoke(self, "bind", [topic]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITopicSubscription).__jsii_proxy_class__ = lambda : _ITopicSubscriptionProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_sns.LoggingConfig",
    jsii_struct_bases=[],
    name_mapping={
        "protocol": "protocol",
        "failure_feedback_role": "failureFeedbackRole",
        "success_feedback_role": "successFeedbackRole",
        "success_feedback_sample_rate": "successFeedbackSampleRate",
    },
)
class LoggingConfig:
    def __init__(
        self,
        *,
        protocol: "LoggingProtocol",
        failure_feedback_role: typing.Optional[_IRole_235f5d8e] = None,
        success_feedback_role: typing.Optional[_IRole_235f5d8e] = None,
        success_feedback_sample_rate: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''A logging configuration for delivery status of messages sent from SNS topic to subscribed endpoints.

        :param protocol: Indicates one of the supported protocols for the SNS topic.
        :param failure_feedback_role: The IAM role to be used when logging failed message deliveries in Amazon CloudWatch. Default: None
        :param success_feedback_role: The IAM role to be used when logging successful message deliveries in Amazon CloudWatch. Default: None
        :param success_feedback_sample_rate: The percentage of successful message deliveries to be logged in Amazon CloudWatch. Valid values are integer between 0-100 Default: None

        :see: https://docs.aws.amazon.com/sns/latest/dg/sns-topic-attributes.html.
        :exampleMetadata: infused

        Example::

            # role: iam.Role
            
            topic = sns.Topic(self, "MyTopic")
            
            topic.add_logging_config(
                protocol=sns.LoggingProtocol.SQS,
                failure_feedback_role=role,
                success_feedback_role=role,
                success_feedback_sample_rate=50
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9eb41e45f77d56f958dda8c78b2c068faf3edbd60bc3b2a62a19317f5490622)
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument failure_feedback_role", value=failure_feedback_role, expected_type=type_hints["failure_feedback_role"])
            check_type(argname="argument success_feedback_role", value=success_feedback_role, expected_type=type_hints["success_feedback_role"])
            check_type(argname="argument success_feedback_sample_rate", value=success_feedback_sample_rate, expected_type=type_hints["success_feedback_sample_rate"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "protocol": protocol,
        }
        if failure_feedback_role is not None:
            self._values["failure_feedback_role"] = failure_feedback_role
        if success_feedback_role is not None:
            self._values["success_feedback_role"] = success_feedback_role
        if success_feedback_sample_rate is not None:
            self._values["success_feedback_sample_rate"] = success_feedback_sample_rate

    @builtins.property
    def protocol(self) -> "LoggingProtocol":
        '''Indicates one of the supported protocols for the SNS topic.'''
        result = self._values.get("protocol")
        assert result is not None, "Required property 'protocol' is missing"
        return typing.cast("LoggingProtocol", result)

    @builtins.property
    def failure_feedback_role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''The IAM role to be used when logging failed message deliveries in Amazon CloudWatch.

        :default: None
        '''
        result = self._values.get("failure_feedback_role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    @builtins.property
    def success_feedback_role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''The IAM role to be used when logging successful message deliveries in Amazon CloudWatch.

        :default: None
        '''
        result = self._values.get("success_feedback_role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    @builtins.property
    def success_feedback_sample_rate(self) -> typing.Optional[jsii.Number]:
        '''The percentage of successful message deliveries to be logged in Amazon CloudWatch.

        Valid values are integer between 0-100

        :default: None
        '''
        result = self._values.get("success_feedback_sample_rate")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoggingConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_sns.LoggingProtocol")
class LoggingProtocol(enum.Enum):
    '''The type of supported protocol for delivery status logging.

    :exampleMetadata: infused

    Example::

        # role: iam.Role
        
        topic = sns.Topic(self, "MyTopic",
            logging_configs=[sns.LoggingConfig(
                protocol=sns.LoggingProtocol.SQS,
                failure_feedback_role=role,
                success_feedback_role=role,
                success_feedback_sample_rate=50
            )
            ]
        )
    '''

    HTTP = "HTTP"
    '''HTTP.'''
    SQS = "SQS"
    '''Amazon Simple Queue Service.'''
    LAMBDA = "LAMBDA"
    '''AWS Lambda.'''
    FIREHOSE = "FIREHOSE"
    '''Amazon Kinesis Data Firehose.'''
    APPLICATION = "APPLICATION"
    '''Platform application endpoint.'''


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_sns.NumericConditions",
    jsii_struct_bases=[],
    name_mapping={
        "allowlist": "allowlist",
        "between": "between",
        "between_strict": "betweenStrict",
        "greater_than": "greaterThan",
        "greater_than_or_equal_to": "greaterThanOrEqualTo",
        "less_than": "lessThan",
        "less_than_or_equal_to": "lessThanOrEqualTo",
    },
)
class NumericConditions:
    def __init__(
        self,
        *,
        allowlist: typing.Optional[typing.Sequence[jsii.Number]] = None,
        between: typing.Optional[typing.Union[BetweenCondition, typing.Dict[builtins.str, typing.Any]]] = None,
        between_strict: typing.Optional[typing.Union[BetweenCondition, typing.Dict[builtins.str, typing.Any]]] = None,
        greater_than: typing.Optional[jsii.Number] = None,
        greater_than_or_equal_to: typing.Optional[jsii.Number] = None,
        less_than: typing.Optional[jsii.Number] = None,
        less_than_or_equal_to: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Conditions that can be applied to numeric attributes.

        :param allowlist: Match one or more values. Default: - None
        :param between: Match values that are between the specified values. Default: - None
        :param between_strict: Match values that are strictly between the specified values. Default: - None
        :param greater_than: Match values that are greater than the specified value. Default: - None
        :param greater_than_or_equal_to: Match values that are greater than or equal to the specified value. Default: - None
        :param less_than: Match values that are less than the specified value. Default: - None
        :param less_than_or_equal_to: Match values that are less than or equal to the specified value. Default: - None

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_lambda as lambda_
            # fn: lambda.Function
            
            
            my_topic = sns.Topic(self, "MyTopic")
            
            # Lambda should receive only message matching the following conditions on attributes:
            # color: 'red' or 'orange' or begins with 'bl'
            # size: anything but 'small' or 'medium'
            # price: between 100 and 200 or greater than 300
            # store: attribute must be present
            my_topic.add_subscription(subscriptions.LambdaSubscription(fn,
                filter_policy={
                    "color": sns.SubscriptionFilter.string_filter(
                        allowlist=["red", "orange"],
                        match_prefixes=["bl"],
                        match_suffixes=["ue"]
                    ),
                    "size": sns.SubscriptionFilter.string_filter(
                        denylist=["small", "medium"]
                    ),
                    "price": sns.SubscriptionFilter.numeric_filter(
                        between=sns.BetweenCondition(start=100, stop=200),
                        greater_than=300
                    ),
                    "store": sns.SubscriptionFilter.exists_filter()
                }
            ))
        '''
        if isinstance(between, dict):
            between = BetweenCondition(**between)
        if isinstance(between_strict, dict):
            between_strict = BetweenCondition(**between_strict)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__275a537da31cf603117422e452eeec6e2885ee8265e341324d589072c1703641)
            check_type(argname="argument allowlist", value=allowlist, expected_type=type_hints["allowlist"])
            check_type(argname="argument between", value=between, expected_type=type_hints["between"])
            check_type(argname="argument between_strict", value=between_strict, expected_type=type_hints["between_strict"])
            check_type(argname="argument greater_than", value=greater_than, expected_type=type_hints["greater_than"])
            check_type(argname="argument greater_than_or_equal_to", value=greater_than_or_equal_to, expected_type=type_hints["greater_than_or_equal_to"])
            check_type(argname="argument less_than", value=less_than, expected_type=type_hints["less_than"])
            check_type(argname="argument less_than_or_equal_to", value=less_than_or_equal_to, expected_type=type_hints["less_than_or_equal_to"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if allowlist is not None:
            self._values["allowlist"] = allowlist
        if between is not None:
            self._values["between"] = between
        if between_strict is not None:
            self._values["between_strict"] = between_strict
        if greater_than is not None:
            self._values["greater_than"] = greater_than
        if greater_than_or_equal_to is not None:
            self._values["greater_than_or_equal_to"] = greater_than_or_equal_to
        if less_than is not None:
            self._values["less_than"] = less_than
        if less_than_or_equal_to is not None:
            self._values["less_than_or_equal_to"] = less_than_or_equal_to

    @builtins.property
    def allowlist(self) -> typing.Optional[typing.List[jsii.Number]]:
        '''Match one or more values.

        :default: - None
        '''
        result = self._values.get("allowlist")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    @builtins.property
    def between(self) -> typing.Optional[BetweenCondition]:
        '''Match values that are between the specified values.

        :default: - None
        '''
        result = self._values.get("between")
        return typing.cast(typing.Optional[BetweenCondition], result)

    @builtins.property
    def between_strict(self) -> typing.Optional[BetweenCondition]:
        '''Match values that are strictly between the specified values.

        :default: - None
        '''
        result = self._values.get("between_strict")
        return typing.cast(typing.Optional[BetweenCondition], result)

    @builtins.property
    def greater_than(self) -> typing.Optional[jsii.Number]:
        '''Match values that are greater than the specified value.

        :default: - None
        '''
        result = self._values.get("greater_than")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def greater_than_or_equal_to(self) -> typing.Optional[jsii.Number]:
        '''Match values that are greater than or equal to the specified value.

        :default: - None
        '''
        result = self._values.get("greater_than_or_equal_to")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def less_than(self) -> typing.Optional[jsii.Number]:
        '''Match values that are less than the specified value.

        :default: - None
        '''
        result = self._values.get("less_than")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def less_than_or_equal_to(self) -> typing.Optional[jsii.Number]:
        '''Match values that are less than or equal to the specified value.

        :default: - None
        '''
        result = self._values.get("less_than_or_equal_to")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NumericConditions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Policy(
    FilterOrPolicy,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_sns.Policy",
):
    '''Policy Implementation of FilterOrPolicy.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_sns as sns
        
        # filter_or_policy: sns.FilterOrPolicy
        
        policy = sns.Policy({
            "policy_doc_key": filter_or_policy
        })
    '''

    def __init__(
        self,
        policy_doc: typing.Mapping[builtins.str, FilterOrPolicy],
    ) -> None:
        '''Policy constructor.

        :param policy_doc: policy argument to construct.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83467db20c58c3a233e8e98fe95c435848f7d6f585004282a535427100d7c20f)
            check_type(argname="argument policy_doc", value=policy_doc, expected_type=type_hints["policy_doc"])
        jsii.create(self.__class__, self, [policy_doc])

    @builtins.property
    @jsii.member(jsii_name="policyDoc")
    def policy_doc(self) -> typing.Mapping[builtins.str, FilterOrPolicy]:
        '''policy argument to construct.'''
        return typing.cast(typing.Mapping[builtins.str, FilterOrPolicy], jsii.get(self, "policyDoc"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> FilterOrPolicyType:
        '''Type used in DFS buildFilterPolicyWithMessageBody to determine json value type.'''
        return typing.cast(FilterOrPolicyType, jsii.get(self, "type"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_sns.StringConditions",
    jsii_struct_bases=[],
    name_mapping={
        "allowlist": "allowlist",
        "denylist": "denylist",
        "match_prefixes": "matchPrefixes",
        "match_suffixes": "matchSuffixes",
    },
)
class StringConditions:
    def __init__(
        self,
        *,
        allowlist: typing.Optional[typing.Sequence[builtins.str]] = None,
        denylist: typing.Optional[typing.Sequence[builtins.str]] = None,
        match_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
        match_suffixes: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Conditions that can be applied to string attributes.

        :param allowlist: Match one or more values. Default: - None
        :param denylist: Match any value that doesn't include any of the specified values. Default: - None
        :param match_prefixes: Matches values that begins with the specified prefixes. Default: - None
        :param match_suffixes: Matches values that end with the specified suffixes. Default: - None

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_lambda as lambda_
            # fn: lambda.Function
            
            
            my_topic = sns.Topic(self, "MyTopic")
            
            # Lambda should receive only message matching the following conditions on attributes:
            # color: 'red' or 'orange' or begins with 'bl'
            # size: anything but 'small' or 'medium'
            # price: between 100 and 200 or greater than 300
            # store: attribute must be present
            my_topic.add_subscription(subscriptions.LambdaSubscription(fn,
                filter_policy={
                    "color": sns.SubscriptionFilter.string_filter(
                        allowlist=["red", "orange"],
                        match_prefixes=["bl"],
                        match_suffixes=["ue"]
                    ),
                    "size": sns.SubscriptionFilter.string_filter(
                        denylist=["small", "medium"]
                    ),
                    "price": sns.SubscriptionFilter.numeric_filter(
                        between=sns.BetweenCondition(start=100, stop=200),
                        greater_than=300
                    ),
                    "store": sns.SubscriptionFilter.exists_filter()
                }
            ))
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__608bd3c9ae19b496ea71293f19119c75ba12a13947777e25f50e21d76ee1afa9)
            check_type(argname="argument allowlist", value=allowlist, expected_type=type_hints["allowlist"])
            check_type(argname="argument denylist", value=denylist, expected_type=type_hints["denylist"])
            check_type(argname="argument match_prefixes", value=match_prefixes, expected_type=type_hints["match_prefixes"])
            check_type(argname="argument match_suffixes", value=match_suffixes, expected_type=type_hints["match_suffixes"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if allowlist is not None:
            self._values["allowlist"] = allowlist
        if denylist is not None:
            self._values["denylist"] = denylist
        if match_prefixes is not None:
            self._values["match_prefixes"] = match_prefixes
        if match_suffixes is not None:
            self._values["match_suffixes"] = match_suffixes

    @builtins.property
    def allowlist(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Match one or more values.

        :default: - None
        '''
        result = self._values.get("allowlist")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def denylist(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Match any value that doesn't include any of the specified values.

        :default: - None
        '''
        result = self._values.get("denylist")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def match_prefixes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Matches values that begins with the specified prefixes.

        :default: - None
        '''
        result = self._values.get("match_prefixes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def match_suffixes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Matches values that end with the specified suffixes.

        :default: - None
        '''
        result = self._values.get("match_suffixes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StringConditions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Subscription(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_sns.Subscription",
):
    '''A new subscription.

    Prefer to use the ``ITopic.addSubscription()`` methods to create instances of
    this class.

    :exampleMetadata: infused

    Example::

        from aws_cdk.aws_kinesisfirehose_alpha import DeliveryStream
        # stream: DeliveryStream
        
        
        topic = sns.Topic(self, "Topic")
        
        sns.Subscription(self, "Subscription",
            topic=topic,
            endpoint=stream.delivery_stream_arn,
            protocol=sns.SubscriptionProtocol.FIREHOSE,
            subscription_role_arn="SAMPLE_ARN"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        topic: ITopic,
        endpoint: builtins.str,
        protocol: "SubscriptionProtocol",
        dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
        filter_policy: typing.Optional[typing.Mapping[builtins.str, "SubscriptionFilter"]] = None,
        filter_policy_with_message_body: typing.Optional[typing.Mapping[builtins.str, FilterOrPolicy]] = None,
        raw_message_delivery: typing.Optional[builtins.bool] = None,
        region: typing.Optional[builtins.str] = None,
        subscription_role_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param topic: The topic to subscribe to.
        :param endpoint: The subscription endpoint. The meaning of this value depends on the value for 'protocol'.
        :param protocol: What type of subscription to add.
        :param dead_letter_queue: Queue to be used as dead letter queue. If not passed no dead letter queue is enabled. Default: - No dead letter queue enabled.
        :param filter_policy: The filter policy. Default: - all messages are delivered
        :param filter_policy_with_message_body: The filter policy that is applied on the message body. To apply a filter policy to the message attributes, use ``filterPolicy``. A maximum of one of ``filterPolicyWithMessageBody`` and ``filterPolicy`` may be used. Default: - all messages are delivered
        :param raw_message_delivery: true if raw message delivery is enabled for the subscription. Raw messages are free of JSON formatting and can be sent to HTTP/S and Amazon SQS endpoints. For more information, see GetSubscriptionAttributes in the Amazon Simple Notification Service API Reference. Default: false
        :param region: The region where the topic resides, in the case of cross-region subscriptions. Default: - the region where the CloudFormation stack is being deployed.
        :param subscription_role_arn: Arn of role allowing access to firehose delivery stream. Required for a firehose subscription protocol. Default: - No subscription role is provided
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ba93ce15c8c35d2f3ef25181ab5de6aae90de3adaf596e2b2f2e51f92bce5a3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = SubscriptionProps(
            topic=topic,
            endpoint=endpoint,
            protocol=protocol,
            dead_letter_queue=dead_letter_queue,
            filter_policy=filter_policy,
            filter_policy_with_message_body=filter_policy_with_message_body,
            raw_message_delivery=raw_message_delivery,
            region=region,
            subscription_role_arn=subscription_role_arn,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="deadLetterQueue")
    def dead_letter_queue(self) -> typing.Optional[_IQueue_7ed6f679]:
        '''The DLQ associated with this subscription if present.'''
        return typing.cast(typing.Optional[_IQueue_7ed6f679], jsii.get(self, "deadLetterQueue"))


class SubscriptionFilter(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_sns.SubscriptionFilter",
):
    '''A subscription filter for an attribute.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_lambda as lambda_
        # fn: lambda.Function
        
        
        my_topic = sns.Topic(self, "MyTopic")
        
        # Lambda should receive only message matching the following conditions on attributes:
        # color: 'red' or 'orange' or begins with 'bl'
        # size: anything but 'small' or 'medium'
        # price: between 100 and 200 or greater than 300
        # store: attribute must be present
        my_topic.add_subscription(subscriptions.LambdaSubscription(fn,
            filter_policy={
                "color": sns.SubscriptionFilter.string_filter(
                    allowlist=["red", "orange"],
                    match_prefixes=["bl"],
                    match_suffixes=["ue"]
                ),
                "size": sns.SubscriptionFilter.string_filter(
                    denylist=["small", "medium"]
                ),
                "price": sns.SubscriptionFilter.numeric_filter(
                    between=sns.BetweenCondition(start=100, stop=200),
                    greater_than=300
                ),
                "store": sns.SubscriptionFilter.exists_filter()
            }
        ))
    '''

    def __init__(
        self,
        conditions: typing.Optional[typing.Sequence[typing.Any]] = None,
    ) -> None:
        '''
        :param conditions: conditions that specify the message attributes that should be included, excluded, matched, etc.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1fada138ee1fc7d11bbf797b2a645bbf52b3239972a66be3174051b994ad84a8)
            check_type(argname="argument conditions", value=conditions, expected_type=type_hints["conditions"])
        jsii.create(self.__class__, self, [conditions])

    @jsii.member(jsii_name="existsFilter")
    @builtins.classmethod
    def exists_filter(cls) -> "SubscriptionFilter":
        '''Returns a subscription filter for attribute key matching.'''
        return typing.cast("SubscriptionFilter", jsii.sinvoke(cls, "existsFilter", []))

    @jsii.member(jsii_name="numericFilter")
    @builtins.classmethod
    def numeric_filter(
        cls,
        *,
        allowlist: typing.Optional[typing.Sequence[jsii.Number]] = None,
        between: typing.Optional[typing.Union[BetweenCondition, typing.Dict[builtins.str, typing.Any]]] = None,
        between_strict: typing.Optional[typing.Union[BetweenCondition, typing.Dict[builtins.str, typing.Any]]] = None,
        greater_than: typing.Optional[jsii.Number] = None,
        greater_than_or_equal_to: typing.Optional[jsii.Number] = None,
        less_than: typing.Optional[jsii.Number] = None,
        less_than_or_equal_to: typing.Optional[jsii.Number] = None,
    ) -> "SubscriptionFilter":
        '''Returns a subscription filter for a numeric attribute.

        :param allowlist: Match one or more values. Default: - None
        :param between: Match values that are between the specified values. Default: - None
        :param between_strict: Match values that are strictly between the specified values. Default: - None
        :param greater_than: Match values that are greater than the specified value. Default: - None
        :param greater_than_or_equal_to: Match values that are greater than or equal to the specified value. Default: - None
        :param less_than: Match values that are less than the specified value. Default: - None
        :param less_than_or_equal_to: Match values that are less than or equal to the specified value. Default: - None
        '''
        numeric_conditions = NumericConditions(
            allowlist=allowlist,
            between=between,
            between_strict=between_strict,
            greater_than=greater_than,
            greater_than_or_equal_to=greater_than_or_equal_to,
            less_than=less_than,
            less_than_or_equal_to=less_than_or_equal_to,
        )

        return typing.cast("SubscriptionFilter", jsii.sinvoke(cls, "numericFilter", [numeric_conditions]))

    @jsii.member(jsii_name="stringFilter")
    @builtins.classmethod
    def string_filter(
        cls,
        *,
        allowlist: typing.Optional[typing.Sequence[builtins.str]] = None,
        denylist: typing.Optional[typing.Sequence[builtins.str]] = None,
        match_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
        match_suffixes: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> "SubscriptionFilter":
        '''Returns a subscription filter for a string attribute.

        :param allowlist: Match one or more values. Default: - None
        :param denylist: Match any value that doesn't include any of the specified values. Default: - None
        :param match_prefixes: Matches values that begins with the specified prefixes. Default: - None
        :param match_suffixes: Matches values that end with the specified suffixes. Default: - None
        '''
        string_conditions = StringConditions(
            allowlist=allowlist,
            denylist=denylist,
            match_prefixes=match_prefixes,
            match_suffixes=match_suffixes,
        )

        return typing.cast("SubscriptionFilter", jsii.sinvoke(cls, "stringFilter", [string_conditions]))

    @builtins.property
    @jsii.member(jsii_name="conditions")
    def conditions(self) -> typing.List[typing.Any]:
        '''conditions that specify the message attributes that should be included, excluded, matched, etc.'''
        return typing.cast(typing.List[typing.Any], jsii.get(self, "conditions"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_sns.SubscriptionOptions",
    jsii_struct_bases=[],
    name_mapping={
        "endpoint": "endpoint",
        "protocol": "protocol",
        "dead_letter_queue": "deadLetterQueue",
        "filter_policy": "filterPolicy",
        "filter_policy_with_message_body": "filterPolicyWithMessageBody",
        "raw_message_delivery": "rawMessageDelivery",
        "region": "region",
        "subscription_role_arn": "subscriptionRoleArn",
    },
)
class SubscriptionOptions:
    def __init__(
        self,
        *,
        endpoint: builtins.str,
        protocol: "SubscriptionProtocol",
        dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
        filter_policy: typing.Optional[typing.Mapping[builtins.str, SubscriptionFilter]] = None,
        filter_policy_with_message_body: typing.Optional[typing.Mapping[builtins.str, FilterOrPolicy]] = None,
        raw_message_delivery: typing.Optional[builtins.bool] = None,
        region: typing.Optional[builtins.str] = None,
        subscription_role_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Options for creating a new subscription.

        :param endpoint: The subscription endpoint. The meaning of this value depends on the value for 'protocol'.
        :param protocol: What type of subscription to add.
        :param dead_letter_queue: Queue to be used as dead letter queue. If not passed no dead letter queue is enabled. Default: - No dead letter queue enabled.
        :param filter_policy: The filter policy. Default: - all messages are delivered
        :param filter_policy_with_message_body: The filter policy that is applied on the message body. To apply a filter policy to the message attributes, use ``filterPolicy``. A maximum of one of ``filterPolicyWithMessageBody`` and ``filterPolicy`` may be used. Default: - all messages are delivered
        :param raw_message_delivery: true if raw message delivery is enabled for the subscription. Raw messages are free of JSON formatting and can be sent to HTTP/S and Amazon SQS endpoints. For more information, see GetSubscriptionAttributes in the Amazon Simple Notification Service API Reference. Default: false
        :param region: The region where the topic resides, in the case of cross-region subscriptions. Default: - the region where the CloudFormation stack is being deployed.
        :param subscription_role_arn: Arn of role allowing access to firehose delivery stream. Required for a firehose subscription protocol. Default: - No subscription role is provided

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_sns as sns
            from aws_cdk import aws_sqs as sqs
            
            # filter_or_policy: sns.FilterOrPolicy
            # queue: sqs.Queue
            # subscription_filter: sns.SubscriptionFilter
            
            subscription_options = sns.SubscriptionOptions(
                endpoint="endpoint",
                protocol=sns.SubscriptionProtocol.HTTP,
            
                # the properties below are optional
                dead_letter_queue=queue,
                filter_policy={
                    "filter_policy_key": subscription_filter
                },
                filter_policy_with_message_body={
                    "filter_policy_with_message_body_key": filter_or_policy
                },
                raw_message_delivery=False,
                region="region",
                subscription_role_arn="subscriptionRoleArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bce75a2ad593ea78ce07c3bf1cbe6c0262cc48f6f133af363ca95a0cadfb6008)
            check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument dead_letter_queue", value=dead_letter_queue, expected_type=type_hints["dead_letter_queue"])
            check_type(argname="argument filter_policy", value=filter_policy, expected_type=type_hints["filter_policy"])
            check_type(argname="argument filter_policy_with_message_body", value=filter_policy_with_message_body, expected_type=type_hints["filter_policy_with_message_body"])
            check_type(argname="argument raw_message_delivery", value=raw_message_delivery, expected_type=type_hints["raw_message_delivery"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument subscription_role_arn", value=subscription_role_arn, expected_type=type_hints["subscription_role_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "endpoint": endpoint,
            "protocol": protocol,
        }
        if dead_letter_queue is not None:
            self._values["dead_letter_queue"] = dead_letter_queue
        if filter_policy is not None:
            self._values["filter_policy"] = filter_policy
        if filter_policy_with_message_body is not None:
            self._values["filter_policy_with_message_body"] = filter_policy_with_message_body
        if raw_message_delivery is not None:
            self._values["raw_message_delivery"] = raw_message_delivery
        if region is not None:
            self._values["region"] = region
        if subscription_role_arn is not None:
            self._values["subscription_role_arn"] = subscription_role_arn

    @builtins.property
    def endpoint(self) -> builtins.str:
        '''The subscription endpoint.

        The meaning of this value depends on the value for 'protocol'.
        '''
        result = self._values.get("endpoint")
        assert result is not None, "Required property 'endpoint' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def protocol(self) -> "SubscriptionProtocol":
        '''What type of subscription to add.'''
        result = self._values.get("protocol")
        assert result is not None, "Required property 'protocol' is missing"
        return typing.cast("SubscriptionProtocol", result)

    @builtins.property
    def dead_letter_queue(self) -> typing.Optional[_IQueue_7ed6f679]:
        '''Queue to be used as dead letter queue.

        If not passed no dead letter queue is enabled.

        :default: - No dead letter queue enabled.
        '''
        result = self._values.get("dead_letter_queue")
        return typing.cast(typing.Optional[_IQueue_7ed6f679], result)

    @builtins.property
    def filter_policy(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, SubscriptionFilter]]:
        '''The filter policy.

        :default: - all messages are delivered
        '''
        result = self._values.get("filter_policy")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, SubscriptionFilter]], result)

    @builtins.property
    def filter_policy_with_message_body(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, FilterOrPolicy]]:
        '''The filter policy that is applied on the message body.

        To apply a filter policy to the message attributes, use ``filterPolicy``. A maximum of one of ``filterPolicyWithMessageBody`` and ``filterPolicy`` may be used.

        :default: - all messages are delivered
        '''
        result = self._values.get("filter_policy_with_message_body")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, FilterOrPolicy]], result)

    @builtins.property
    def raw_message_delivery(self) -> typing.Optional[builtins.bool]:
        '''true if raw message delivery is enabled for the subscription.

        Raw messages are free of JSON formatting and can be
        sent to HTTP/S and Amazon SQS endpoints. For more information, see GetSubscriptionAttributes in the Amazon Simple
        Notification Service API Reference.

        :default: false
        '''
        result = self._values.get("raw_message_delivery")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''The region where the topic resides, in the case of cross-region subscriptions.

        :default: - the region where the CloudFormation stack is being deployed.

        :link: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-subscription.html#cfn-sns-subscription-region
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subscription_role_arn(self) -> typing.Optional[builtins.str]:
        '''Arn of role allowing access to firehose delivery stream.

        Required for a firehose subscription protocol.

        :default: - No subscription role is provided
        '''
        result = self._values.get("subscription_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SubscriptionOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_sns.SubscriptionProps",
    jsii_struct_bases=[SubscriptionOptions],
    name_mapping={
        "endpoint": "endpoint",
        "protocol": "protocol",
        "dead_letter_queue": "deadLetterQueue",
        "filter_policy": "filterPolicy",
        "filter_policy_with_message_body": "filterPolicyWithMessageBody",
        "raw_message_delivery": "rawMessageDelivery",
        "region": "region",
        "subscription_role_arn": "subscriptionRoleArn",
        "topic": "topic",
    },
)
class SubscriptionProps(SubscriptionOptions):
    def __init__(
        self,
        *,
        endpoint: builtins.str,
        protocol: "SubscriptionProtocol",
        dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
        filter_policy: typing.Optional[typing.Mapping[builtins.str, SubscriptionFilter]] = None,
        filter_policy_with_message_body: typing.Optional[typing.Mapping[builtins.str, FilterOrPolicy]] = None,
        raw_message_delivery: typing.Optional[builtins.bool] = None,
        region: typing.Optional[builtins.str] = None,
        subscription_role_arn: typing.Optional[builtins.str] = None,
        topic: ITopic,
    ) -> None:
        '''Properties for creating a new subscription.

        :param endpoint: The subscription endpoint. The meaning of this value depends on the value for 'protocol'.
        :param protocol: What type of subscription to add.
        :param dead_letter_queue: Queue to be used as dead letter queue. If not passed no dead letter queue is enabled. Default: - No dead letter queue enabled.
        :param filter_policy: The filter policy. Default: - all messages are delivered
        :param filter_policy_with_message_body: The filter policy that is applied on the message body. To apply a filter policy to the message attributes, use ``filterPolicy``. A maximum of one of ``filterPolicyWithMessageBody`` and ``filterPolicy`` may be used. Default: - all messages are delivered
        :param raw_message_delivery: true if raw message delivery is enabled for the subscription. Raw messages are free of JSON formatting and can be sent to HTTP/S and Amazon SQS endpoints. For more information, see GetSubscriptionAttributes in the Amazon Simple Notification Service API Reference. Default: false
        :param region: The region where the topic resides, in the case of cross-region subscriptions. Default: - the region where the CloudFormation stack is being deployed.
        :param subscription_role_arn: Arn of role allowing access to firehose delivery stream. Required for a firehose subscription protocol. Default: - No subscription role is provided
        :param topic: The topic to subscribe to.

        :exampleMetadata: infused

        Example::

            from aws_cdk.aws_kinesisfirehose_alpha import DeliveryStream
            # stream: DeliveryStream
            
            
            topic = sns.Topic(self, "Topic")
            
            sns.Subscription(self, "Subscription",
                topic=topic,
                endpoint=stream.delivery_stream_arn,
                protocol=sns.SubscriptionProtocol.FIREHOSE,
                subscription_role_arn="SAMPLE_ARN"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca027bfed18b17f0f94ff71f11bf24813f4ec24f9b1029e73d8da4ef880e57a4)
            check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument dead_letter_queue", value=dead_letter_queue, expected_type=type_hints["dead_letter_queue"])
            check_type(argname="argument filter_policy", value=filter_policy, expected_type=type_hints["filter_policy"])
            check_type(argname="argument filter_policy_with_message_body", value=filter_policy_with_message_body, expected_type=type_hints["filter_policy_with_message_body"])
            check_type(argname="argument raw_message_delivery", value=raw_message_delivery, expected_type=type_hints["raw_message_delivery"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument subscription_role_arn", value=subscription_role_arn, expected_type=type_hints["subscription_role_arn"])
            check_type(argname="argument topic", value=topic, expected_type=type_hints["topic"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "endpoint": endpoint,
            "protocol": protocol,
            "topic": topic,
        }
        if dead_letter_queue is not None:
            self._values["dead_letter_queue"] = dead_letter_queue
        if filter_policy is not None:
            self._values["filter_policy"] = filter_policy
        if filter_policy_with_message_body is not None:
            self._values["filter_policy_with_message_body"] = filter_policy_with_message_body
        if raw_message_delivery is not None:
            self._values["raw_message_delivery"] = raw_message_delivery
        if region is not None:
            self._values["region"] = region
        if subscription_role_arn is not None:
            self._values["subscription_role_arn"] = subscription_role_arn

    @builtins.property
    def endpoint(self) -> builtins.str:
        '''The subscription endpoint.

        The meaning of this value depends on the value for 'protocol'.
        '''
        result = self._values.get("endpoint")
        assert result is not None, "Required property 'endpoint' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def protocol(self) -> "SubscriptionProtocol":
        '''What type of subscription to add.'''
        result = self._values.get("protocol")
        assert result is not None, "Required property 'protocol' is missing"
        return typing.cast("SubscriptionProtocol", result)

    @builtins.property
    def dead_letter_queue(self) -> typing.Optional[_IQueue_7ed6f679]:
        '''Queue to be used as dead letter queue.

        If not passed no dead letter queue is enabled.

        :default: - No dead letter queue enabled.
        '''
        result = self._values.get("dead_letter_queue")
        return typing.cast(typing.Optional[_IQueue_7ed6f679], result)

    @builtins.property
    def filter_policy(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, SubscriptionFilter]]:
        '''The filter policy.

        :default: - all messages are delivered
        '''
        result = self._values.get("filter_policy")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, SubscriptionFilter]], result)

    @builtins.property
    def filter_policy_with_message_body(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, FilterOrPolicy]]:
        '''The filter policy that is applied on the message body.

        To apply a filter policy to the message attributes, use ``filterPolicy``. A maximum of one of ``filterPolicyWithMessageBody`` and ``filterPolicy`` may be used.

        :default: - all messages are delivered
        '''
        result = self._values.get("filter_policy_with_message_body")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, FilterOrPolicy]], result)

    @builtins.property
    def raw_message_delivery(self) -> typing.Optional[builtins.bool]:
        '''true if raw message delivery is enabled for the subscription.

        Raw messages are free of JSON formatting and can be
        sent to HTTP/S and Amazon SQS endpoints. For more information, see GetSubscriptionAttributes in the Amazon Simple
        Notification Service API Reference.

        :default: false
        '''
        result = self._values.get("raw_message_delivery")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''The region where the topic resides, in the case of cross-region subscriptions.

        :default: - the region where the CloudFormation stack is being deployed.

        :link: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-subscription.html#cfn-sns-subscription-region
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subscription_role_arn(self) -> typing.Optional[builtins.str]:
        '''Arn of role allowing access to firehose delivery stream.

        Required for a firehose subscription protocol.

        :default: - No subscription role is provided
        '''
        result = self._values.get("subscription_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def topic(self) -> ITopic:
        '''The topic to subscribe to.'''
        result = self._values.get("topic")
        assert result is not None, "Required property 'topic' is missing"
        return typing.cast(ITopic, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SubscriptionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_sns.SubscriptionProtocol")
class SubscriptionProtocol(enum.Enum):
    '''The type of subscription, controlling the type of the endpoint parameter.

    :exampleMetadata: infused

    Example::

        from aws_cdk.aws_kinesisfirehose_alpha import DeliveryStream
        # stream: DeliveryStream
        
        
        topic = sns.Topic(self, "Topic")
        
        sns.Subscription(self, "Subscription",
            topic=topic,
            endpoint=stream.delivery_stream_arn,
            protocol=sns.SubscriptionProtocol.FIREHOSE,
            subscription_role_arn="SAMPLE_ARN"
        )
    '''

    HTTP = "HTTP"
    '''JSON-encoded message is POSTED to an HTTP url.'''
    HTTPS = "HTTPS"
    '''JSON-encoded message is POSTed to an HTTPS url.'''
    EMAIL = "EMAIL"
    '''Notifications are sent via email.'''
    EMAIL_JSON = "EMAIL_JSON"
    '''Notifications are JSON-encoded and sent via mail.'''
    SMS = "SMS"
    '''Notification is delivered by SMS.'''
    SQS = "SQS"
    '''Notifications are enqueued into an SQS queue.'''
    APPLICATION = "APPLICATION"
    '''JSON-encoded notifications are sent to a mobile app endpoint.'''
    LAMBDA = "LAMBDA"
    '''Notifications trigger a Lambda function.'''
    FIREHOSE = "FIREHOSE"
    '''Notifications put records into a firehose delivery stream.'''


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_sns.TopicAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "topic_arn": "topicArn",
        "content_based_deduplication": "contentBasedDeduplication",
    },
)
class TopicAttributes:
    def __init__(
        self,
        *,
        topic_arn: builtins.str,
        content_based_deduplication: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Represents an SNS topic defined outside of this stack.

        :param topic_arn: The ARN of the SNS topic.
        :param content_based_deduplication: Whether content-based deduplication is enabled. Only applicable for FIFO topics. Default: false

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_sns as sns
            
            topic_attributes = sns.TopicAttributes(
                topic_arn="topicArn",
            
                # the properties below are optional
                content_based_deduplication=False
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8362e16cf38fb93899cf1443c05ea87f926cf385d45c4f25eb95067bff9642a)
            check_type(argname="argument topic_arn", value=topic_arn, expected_type=type_hints["topic_arn"])
            check_type(argname="argument content_based_deduplication", value=content_based_deduplication, expected_type=type_hints["content_based_deduplication"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "topic_arn": topic_arn,
        }
        if content_based_deduplication is not None:
            self._values["content_based_deduplication"] = content_based_deduplication

    @builtins.property
    def topic_arn(self) -> builtins.str:
        '''The ARN of the SNS topic.'''
        result = self._values.get("topic_arn")
        assert result is not None, "Required property 'topic_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def content_based_deduplication(self) -> typing.Optional[builtins.bool]:
        '''Whether content-based deduplication is enabled.

        Only applicable for FIFO topics.

        :default: false
        '''
        result = self._values.get("content_based_deduplication")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TopicAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(ITopic)
class TopicBase(
    _Resource_45bc6135,
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="aws-cdk-lib.aws_sns.TopicBase",
):
    '''Either a new or imported Topic.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        account: typing.Optional[builtins.str] = None,
        environment_from_arn: typing.Optional[builtins.str] = None,
        physical_name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param account: The AWS account ID this resource belongs to. Default: - the resource is in the same account as the stack it belongs to
        :param environment_from_arn: ARN to deduce region and account from. The ARN is parsed and the account and region are taken from the ARN. This should be used for imported resources. Cannot be supplied together with either ``account`` or ``region``. Default: - take environment from ``account``, ``region`` parameters, or use Stack environment.
        :param physical_name: The value passed in by users to the physical name prop of the resource. - ``undefined`` implies that a physical name will be allocated by CloudFormation during deployment. - a concrete value implies a specific physical name - ``PhysicalName.GENERATE_IF_NEEDED`` is a marker that indicates that a physical will only be generated by the CDK if it is needed for cross-environment references. Otherwise, it will be allocated by CloudFormation. Default: - The physical name will be allocated by CloudFormation at deployment time
        :param region: The AWS region this resource belongs to. Default: - the resource is in the same region as the stack it belongs to
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e97a3ac4042ed403ad7f37324d239151dacf8c0ddc949fcb2cda9467c86d55c3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = _ResourceProps_15a65b4e(
            account=account,
            environment_from_arn=environment_from_arn,
            physical_name=physical_name,
            region=region,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="addSubscription")
    def add_subscription(self, topic_subscription: ITopicSubscription) -> Subscription:
        '''Subscribe some endpoint to this topic.

        :param topic_subscription: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3af87d479cce0479b13b487a212b9eb786dc4faba1cadb3a6451209927770a60)
            check_type(argname="argument topic_subscription", value=topic_subscription, expected_type=type_hints["topic_subscription"])
        return typing.cast(Subscription, jsii.invoke(self, "addSubscription", [topic_subscription]))

    @jsii.member(jsii_name="addToResourcePolicy")
    def add_to_resource_policy(
        self,
        statement: _PolicyStatement_0fe33853,
    ) -> _AddToResourcePolicyResult_1d0a53ad:
        '''Adds a statement to the IAM resource policy associated with this topic.

        If this topic was created in this stack (``new Topic``), a topic policy
        will be automatically created upon the first call to ``addToResourcePolicy``. If
        the topic is imported (``Topic.import``), then this is a no-op.

        :param statement: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7f4d520e0fc706fbd4e1415b076009a3ab58db83ac7b721c03dba894f99c83d)
            check_type(argname="argument statement", value=statement, expected_type=type_hints["statement"])
        return typing.cast(_AddToResourcePolicyResult_1d0a53ad, jsii.invoke(self, "addToResourcePolicy", [statement]))

    @jsii.member(jsii_name="bindAsNotificationRuleTarget")
    def bind_as_notification_rule_target(
        self,
        _scope: _constructs_77d1e7e8.Construct,
    ) -> _NotificationRuleTargetConfig_ea27e095:
        '''Represents a notification target That allows SNS topic to associate with this rule target.

        :param _scope: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04cdaba4727d1a890bbc0d5d2854229f71f59b72c42feadb21ad6387b14c83bd)
            check_type(argname="argument _scope", value=_scope, expected_type=type_hints["_scope"])
        return typing.cast(_NotificationRuleTargetConfig_ea27e095, jsii.invoke(self, "bindAsNotificationRuleTarget", [_scope]))

    @jsii.member(jsii_name="createSSLPolicyDocument")
    def _create_ssl_policy_document(self) -> _PolicyStatement_0fe33853:
        '''Adds a statement to enforce encryption of data in transit when publishing to the topic.

        For more information, see https://docs.aws.amazon.com/sns/latest/dg/sns-security-best-practices.html#enforce-encryption-data-in-transit.
        '''
        return typing.cast(_PolicyStatement_0fe33853, jsii.invoke(self, "createSSLPolicyDocument", []))

    @jsii.member(jsii_name="grantPublish")
    def grant_publish(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant topic publishing permissions to the given identity.

        :param grantee: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6461236ee087e9f8e6de731371b913e918bbd3ec5d928bd677a69c9c8eb82381)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantPublish", [grantee]))

    @jsii.member(jsii_name="metric")
    def metric(
        self,
        metric_name: builtins.str,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''Return the given named metric for this Topic.

        :param metric_name: -
        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b07969d7a2c71869715d0fe87d9b0d9d67f663ddecc9d81d353ba532fdaa3b8d)
            check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
        props = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metric", [metric_name, props]))

    @jsii.member(jsii_name="metricNumberOfMessagesPublished")
    def metric_number_of_messages_published(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''The number of messages published to your Amazon SNS topics.

        Sum over 5 minutes

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        '''
        props = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricNumberOfMessagesPublished", [props]))

    @jsii.member(jsii_name="metricNumberOfNotificationsDelivered")
    def metric_number_of_notifications_delivered(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''The number of messages successfully delivered from your Amazon SNS topics to subscribing endpoints.

        Sum over 5 minutes

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        '''
        props = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricNumberOfNotificationsDelivered", [props]))

    @jsii.member(jsii_name="metricNumberOfNotificationsFailed")
    def metric_number_of_notifications_failed(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''The number of messages that Amazon SNS failed to deliver.

        Sum over 5 minutes

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        '''
        props = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricNumberOfNotificationsFailed", [props]))

    @jsii.member(jsii_name="metricNumberOfNotificationsFilteredOut")
    def metric_number_of_notifications_filtered_out(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''The number of messages that were rejected by subscription filter policies.

        Sum over 5 minutes

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        '''
        props = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricNumberOfNotificationsFilteredOut", [props]))

    @jsii.member(jsii_name="metricNumberOfNotificationsFilteredOutInvalidAttributes")
    def metric_number_of_notifications_filtered_out_invalid_attributes(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''The number of messages that were rejected by subscription filter policies because the messages' attributes are invalid.

        Sum over 5 minutes

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        '''
        props = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricNumberOfNotificationsFilteredOutInvalidAttributes", [props]))

    @jsii.member(jsii_name="metricNumberOfNotificationsFilteredOutNoMessageAttributes")
    def metric_number_of_notifications_filtered_out_no_message_attributes(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''The number of messages that were rejected by subscription filter policies because the messages have no attributes.

        Sum over 5 minutes

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        '''
        props = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricNumberOfNotificationsFilteredOutNoMessageAttributes", [props]))

    @jsii.member(jsii_name="metricPublishSize")
    def metric_publish_size(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''Metric for the size of messages published through this topic.

        Average over 5 minutes

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        '''
        props = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricPublishSize", [props]))

    @jsii.member(jsii_name="metricSMSMonthToDateSpentUSD")
    def metric_sms_month_to_date_spent_usd(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''The charges you have accrued since the start of the current calendar month for sending SMS messages.

        Maximum over 5 minutes

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        '''
        props = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricSMSMonthToDateSpentUSD", [props]))

    @jsii.member(jsii_name="metricSMSSuccessRate")
    def metric_sms_success_rate(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''The rate of successful SMS message deliveries.

        Sum over 5 minutes

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        '''
        props = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricSMSSuccessRate", [props]))

    @builtins.property
    @jsii.member(jsii_name="autoCreatePolicy")
    @abc.abstractmethod
    def _auto_create_policy(self) -> builtins.bool:
        '''Controls automatic creation of policy objects.

        Set by subclasses.
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="contentBasedDeduplication")
    @abc.abstractmethod
    def content_based_deduplication(self) -> builtins.bool:
        '''Enables content-based deduplication for FIFO topics.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="fifo")
    @abc.abstractmethod
    def fifo(self) -> builtins.bool:
        '''Whether this topic is an Amazon SNS FIFO queue.

        If false, this is a standard topic.
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="topicArn")
    @abc.abstractmethod
    def topic_arn(self) -> builtins.str:
        '''The ARN of the topic.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="topicName")
    @abc.abstractmethod
    def topic_name(self) -> builtins.str:
        '''The name of the topic.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="enforceSSL")
    def _enforce_ssl(self) -> typing.Optional[builtins.bool]:
        '''Adds a statement to enforce encryption of data in transit when publishing to the topic.'''
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "enforceSSL"))

    @_enforce_ssl.setter
    def _enforce_ssl(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41d14f58fd3a68985cc9146f591de9ef04f0766e0e4ab580bec4fe74fde70eee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enforceSSL", value)


class _TopicBaseProxy(
    TopicBase,
    jsii.proxy_for(_Resource_45bc6135), # type: ignore[misc]
):
    @builtins.property
    @jsii.member(jsii_name="autoCreatePolicy")
    def _auto_create_policy(self) -> builtins.bool:
        '''Controls automatic creation of policy objects.

        Set by subclasses.
        '''
        return typing.cast(builtins.bool, jsii.get(self, "autoCreatePolicy"))

    @builtins.property
    @jsii.member(jsii_name="contentBasedDeduplication")
    def content_based_deduplication(self) -> builtins.bool:
        '''Enables content-based deduplication for FIFO topics.'''
        return typing.cast(builtins.bool, jsii.get(self, "contentBasedDeduplication"))

    @builtins.property
    @jsii.member(jsii_name="fifo")
    def fifo(self) -> builtins.bool:
        '''Whether this topic is an Amazon SNS FIFO queue.

        If false, this is a standard topic.
        '''
        return typing.cast(builtins.bool, jsii.get(self, "fifo"))

    @builtins.property
    @jsii.member(jsii_name="topicArn")
    def topic_arn(self) -> builtins.str:
        '''The ARN of the topic.'''
        return typing.cast(builtins.str, jsii.get(self, "topicArn"))

    @builtins.property
    @jsii.member(jsii_name="topicName")
    def topic_name(self) -> builtins.str:
        '''The name of the topic.'''
        return typing.cast(builtins.str, jsii.get(self, "topicName"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, TopicBase).__jsii_proxy_class__ = lambda : _TopicBaseProxy


class TopicPolicy(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_sns.TopicPolicy",
):
    '''The policy for an SNS Topic.

    Policies define the operations that are allowed on this resource.

    You almost never need to define this construct directly.

    All AWS resources that support resource policies have a method called
    ``addToResourcePolicy()``, which will automatically create a new resource
    policy if one doesn't exist yet, otherwise it will add to the existing
    policy.

    Prefer to use ``addToResourcePolicy()`` instead.

    :exampleMetadata: infused

    Example::

        topic = sns.Topic(self, "Topic")
        policy_document = iam.PolicyDocument(
            assign_sids=True,
            statements=[
                iam.PolicyStatement(
                    actions=["sns:Subscribe"],
                    principals=[iam.AnyPrincipal()],
                    resources=[topic.topic_arn]
                )
            ]
        )
        
        topic_policy = sns.TopicPolicy(self, "Policy",
            topics=[topic],
            policy_document=policy_document
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        topics: typing.Sequence[ITopic],
        enforce_ssl: typing.Optional[builtins.bool] = None,
        policy_document: typing.Optional[_PolicyDocument_3ac34393] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param topics: The set of topics this policy applies to.
        :param enforce_ssl: Adds a statement to enforce encryption of data in transit when publishing to the topic. For more information, see https://docs.aws.amazon.com/sns/latest/dg/sns-security-best-practices.html#enforce-encryption-data-in-transit. Default: false
        :param policy_document: IAM policy document to apply to topic(s). Default: empty policy document
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12a056cfcdc8bff96e7fe29bb021bebfb1f092d261da925723087b52a2a52c91)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = TopicPolicyProps(
            topics=topics, enforce_ssl=enforce_ssl, policy_document=policy_document
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="createSSLPolicyDocument")
    def _create_ssl_policy_document(
        self,
        topic_arn: builtins.str,
    ) -> _PolicyStatement_0fe33853:
        '''Adds a statement to enforce encryption of data in transit when publishing to the topic.

        For more information, see https://docs.aws.amazon.com/sns/latest/dg/sns-security-best-practices.html#enforce-encryption-data-in-transit.

        :param topic_arn: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68fd01009ddae128e0ad9f5816da32ac0ad127b82df6140a2431cf829c9a7488)
            check_type(argname="argument topic_arn", value=topic_arn, expected_type=type_hints["topic_arn"])
        return typing.cast(_PolicyStatement_0fe33853, jsii.invoke(self, "createSSLPolicyDocument", [topic_arn]))

    @builtins.property
    @jsii.member(jsii_name="document")
    def document(self) -> _PolicyDocument_3ac34393:
        '''The IAM policy document for this policy.'''
        return typing.cast(_PolicyDocument_3ac34393, jsii.get(self, "document"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_sns.TopicPolicyProps",
    jsii_struct_bases=[],
    name_mapping={
        "topics": "topics",
        "enforce_ssl": "enforceSSL",
        "policy_document": "policyDocument",
    },
)
class TopicPolicyProps:
    def __init__(
        self,
        *,
        topics: typing.Sequence[ITopic],
        enforce_ssl: typing.Optional[builtins.bool] = None,
        policy_document: typing.Optional[_PolicyDocument_3ac34393] = None,
    ) -> None:
        '''Properties to associate SNS topics with a policy.

        :param topics: The set of topics this policy applies to.
        :param enforce_ssl: Adds a statement to enforce encryption of data in transit when publishing to the topic. For more information, see https://docs.aws.amazon.com/sns/latest/dg/sns-security-best-practices.html#enforce-encryption-data-in-transit. Default: false
        :param policy_document: IAM policy document to apply to topic(s). Default: empty policy document

        :exampleMetadata: infused

        Example::

            topic = sns.Topic(self, "Topic")
            policy_document = iam.PolicyDocument(
                assign_sids=True,
                statements=[
                    iam.PolicyStatement(
                        actions=["sns:Subscribe"],
                        principals=[iam.AnyPrincipal()],
                        resources=[topic.topic_arn]
                    )
                ]
            )
            
            topic_policy = sns.TopicPolicy(self, "Policy",
                topics=[topic],
                policy_document=policy_document
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4116dddf14d28d4bd4bb7d68b0eda71322f8faeb2468828dde6eca112513ba6b)
            check_type(argname="argument topics", value=topics, expected_type=type_hints["topics"])
            check_type(argname="argument enforce_ssl", value=enforce_ssl, expected_type=type_hints["enforce_ssl"])
            check_type(argname="argument policy_document", value=policy_document, expected_type=type_hints["policy_document"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "topics": topics,
        }
        if enforce_ssl is not None:
            self._values["enforce_ssl"] = enforce_ssl
        if policy_document is not None:
            self._values["policy_document"] = policy_document

    @builtins.property
    def topics(self) -> typing.List[ITopic]:
        '''The set of topics this policy applies to.'''
        result = self._values.get("topics")
        assert result is not None, "Required property 'topics' is missing"
        return typing.cast(typing.List[ITopic], result)

    @builtins.property
    def enforce_ssl(self) -> typing.Optional[builtins.bool]:
        '''Adds a statement to enforce encryption of data in transit when publishing to the topic.

        For more information, see https://docs.aws.amazon.com/sns/latest/dg/sns-security-best-practices.html#enforce-encryption-data-in-transit.

        :default: false
        '''
        result = self._values.get("enforce_ssl")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def policy_document(self) -> typing.Optional[_PolicyDocument_3ac34393]:
        '''IAM policy document to apply to topic(s).

        :default: empty policy document
        '''
        result = self._values.get("policy_document")
        return typing.cast(typing.Optional[_PolicyDocument_3ac34393], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TopicPolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_sns.TopicProps",
    jsii_struct_bases=[],
    name_mapping={
        "content_based_deduplication": "contentBasedDeduplication",
        "display_name": "displayName",
        "enforce_ssl": "enforceSSL",
        "fifo": "fifo",
        "logging_configs": "loggingConfigs",
        "master_key": "masterKey",
        "message_retention_period_in_days": "messageRetentionPeriodInDays",
        "signature_version": "signatureVersion",
        "topic_name": "topicName",
        "tracing_config": "tracingConfig",
    },
)
class TopicProps:
    def __init__(
        self,
        *,
        content_based_deduplication: typing.Optional[builtins.bool] = None,
        display_name: typing.Optional[builtins.str] = None,
        enforce_ssl: typing.Optional[builtins.bool] = None,
        fifo: typing.Optional[builtins.bool] = None,
        logging_configs: typing.Optional[typing.Sequence[typing.Union[LoggingConfig, typing.Dict[builtins.str, typing.Any]]]] = None,
        master_key: typing.Optional[_IKey_5f11635f] = None,
        message_retention_period_in_days: typing.Optional[jsii.Number] = None,
        signature_version: typing.Optional[builtins.str] = None,
        topic_name: typing.Optional[builtins.str] = None,
        tracing_config: typing.Optional["TracingConfig"] = None,
    ) -> None:
        '''Properties for a new SNS topic.

        :param content_based_deduplication: Enables content-based deduplication for FIFO topics. Default: None
        :param display_name: A developer-defined string that can be used to identify this SNS topic. Default: None
        :param enforce_ssl: Adds a statement to enforce encryption of data in transit when publishing to the topic. Default: false
        :param fifo: Set to true to create a FIFO topic. Default: None
        :param logging_configs: The list of delivery status logging configurations for the topic. Default: None
        :param master_key: A KMS Key, either managed by this CDK app, or imported. Default: None
        :param message_retention_period_in_days: The number of days Amazon SNS retains messages. It can only be set for FIFO topics. Default: - do not archive messages
        :param signature_version: The signature version corresponds to the hashing algorithm used while creating the signature of the notifications, subscription confirmations, or unsubscribe confirmation messages sent by Amazon SNS. Default: 1
        :param topic_name: A name for the topic. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the topic name. For more information, see Name Type. Default: Generated name
        :param tracing_config: Tracing mode of an Amazon SNS topic. Default: TracingConfig.PASS_THROUGH

        :exampleMetadata: infused

        Example::

            topic = sns.Topic(self, "MyTopic",
                tracing_config=sns.TracingConfig.ACTIVE
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__093960c1ab5457cc6797eb4a06c9e8fc74e41d4eaa9d0a17f00fa896dadf9161)
            check_type(argname="argument content_based_deduplication", value=content_based_deduplication, expected_type=type_hints["content_based_deduplication"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument enforce_ssl", value=enforce_ssl, expected_type=type_hints["enforce_ssl"])
            check_type(argname="argument fifo", value=fifo, expected_type=type_hints["fifo"])
            check_type(argname="argument logging_configs", value=logging_configs, expected_type=type_hints["logging_configs"])
            check_type(argname="argument master_key", value=master_key, expected_type=type_hints["master_key"])
            check_type(argname="argument message_retention_period_in_days", value=message_retention_period_in_days, expected_type=type_hints["message_retention_period_in_days"])
            check_type(argname="argument signature_version", value=signature_version, expected_type=type_hints["signature_version"])
            check_type(argname="argument topic_name", value=topic_name, expected_type=type_hints["topic_name"])
            check_type(argname="argument tracing_config", value=tracing_config, expected_type=type_hints["tracing_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if content_based_deduplication is not None:
            self._values["content_based_deduplication"] = content_based_deduplication
        if display_name is not None:
            self._values["display_name"] = display_name
        if enforce_ssl is not None:
            self._values["enforce_ssl"] = enforce_ssl
        if fifo is not None:
            self._values["fifo"] = fifo
        if logging_configs is not None:
            self._values["logging_configs"] = logging_configs
        if master_key is not None:
            self._values["master_key"] = master_key
        if message_retention_period_in_days is not None:
            self._values["message_retention_period_in_days"] = message_retention_period_in_days
        if signature_version is not None:
            self._values["signature_version"] = signature_version
        if topic_name is not None:
            self._values["topic_name"] = topic_name
        if tracing_config is not None:
            self._values["tracing_config"] = tracing_config

    @builtins.property
    def content_based_deduplication(self) -> typing.Optional[builtins.bool]:
        '''Enables content-based deduplication for FIFO topics.

        :default: None
        '''
        result = self._values.get("content_based_deduplication")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def display_name(self) -> typing.Optional[builtins.str]:
        '''A developer-defined string that can be used to identify this SNS topic.

        :default: None
        '''
        result = self._values.get("display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enforce_ssl(self) -> typing.Optional[builtins.bool]:
        '''Adds a statement to enforce encryption of data in transit when publishing to the topic.

        :default: false

        :see: https://docs.aws.amazon.com/sns/latest/dg/sns-security-best-practices.html#enforce-encryption-data-in-transit.
        '''
        result = self._values.get("enforce_ssl")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def fifo(self) -> typing.Optional[builtins.bool]:
        '''Set to true to create a FIFO topic.

        :default: None
        '''
        result = self._values.get("fifo")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def logging_configs(self) -> typing.Optional[typing.List[LoggingConfig]]:
        '''The list of delivery status logging configurations for the topic.

        :default: None

        :see: https://docs.aws.amazon.com/sns/latest/dg/sns-topic-attributes.html.
        '''
        result = self._values.get("logging_configs")
        return typing.cast(typing.Optional[typing.List[LoggingConfig]], result)

    @builtins.property
    def master_key(self) -> typing.Optional[_IKey_5f11635f]:
        '''A KMS Key, either managed by this CDK app, or imported.

        :default: None
        '''
        result = self._values.get("master_key")
        return typing.cast(typing.Optional[_IKey_5f11635f], result)

    @builtins.property
    def message_retention_period_in_days(self) -> typing.Optional[jsii.Number]:
        '''The number of days Amazon SNS retains messages.

        It can only be set for FIFO topics.

        :default: - do not archive messages

        :see: https://docs.aws.amazon.com/sns/latest/dg/fifo-message-archiving-replay.html
        '''
        result = self._values.get("message_retention_period_in_days")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def signature_version(self) -> typing.Optional[builtins.str]:
        '''The signature version corresponds to the hashing algorithm used while creating the signature of the notifications, subscription confirmations, or unsubscribe confirmation messages sent by Amazon SNS.

        :default: 1

        :see: https://docs.aws.amazon.com/sns/latest/dg/sns-verify-signature-of-message.html.
        '''
        result = self._values.get("signature_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def topic_name(self) -> typing.Optional[builtins.str]:
        '''A name for the topic.

        If you don't specify a name, AWS CloudFormation generates a unique
        physical ID and uses that ID for the topic name. For more information,
        see Name Type.

        :default: Generated name
        '''
        result = self._values.get("topic_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tracing_config(self) -> typing.Optional["TracingConfig"]:
        '''Tracing mode of an Amazon SNS topic.

        :default: TracingConfig.PASS_THROUGH

        :see: https://docs.aws.amazon.com/sns/latest/dg/sns-active-tracing.html
        '''
        result = self._values.get("tracing_config")
        return typing.cast(typing.Optional["TracingConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TopicProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_sns.TopicSubscriptionConfig",
    jsii_struct_bases=[SubscriptionOptions],
    name_mapping={
        "endpoint": "endpoint",
        "protocol": "protocol",
        "dead_letter_queue": "deadLetterQueue",
        "filter_policy": "filterPolicy",
        "filter_policy_with_message_body": "filterPolicyWithMessageBody",
        "raw_message_delivery": "rawMessageDelivery",
        "region": "region",
        "subscription_role_arn": "subscriptionRoleArn",
        "subscriber_id": "subscriberId",
        "subscriber_scope": "subscriberScope",
        "subscription_dependency": "subscriptionDependency",
    },
)
class TopicSubscriptionConfig(SubscriptionOptions):
    def __init__(
        self,
        *,
        endpoint: builtins.str,
        protocol: SubscriptionProtocol,
        dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
        filter_policy: typing.Optional[typing.Mapping[builtins.str, SubscriptionFilter]] = None,
        filter_policy_with_message_body: typing.Optional[typing.Mapping[builtins.str, FilterOrPolicy]] = None,
        raw_message_delivery: typing.Optional[builtins.bool] = None,
        region: typing.Optional[builtins.str] = None,
        subscription_role_arn: typing.Optional[builtins.str] = None,
        subscriber_id: builtins.str,
        subscriber_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
        subscription_dependency: typing.Optional[_constructs_77d1e7e8.IDependable] = None,
    ) -> None:
        '''Subscription configuration.

        :param endpoint: The subscription endpoint. The meaning of this value depends on the value for 'protocol'.
        :param protocol: What type of subscription to add.
        :param dead_letter_queue: Queue to be used as dead letter queue. If not passed no dead letter queue is enabled. Default: - No dead letter queue enabled.
        :param filter_policy: The filter policy. Default: - all messages are delivered
        :param filter_policy_with_message_body: The filter policy that is applied on the message body. To apply a filter policy to the message attributes, use ``filterPolicy``. A maximum of one of ``filterPolicyWithMessageBody`` and ``filterPolicy`` may be used. Default: - all messages are delivered
        :param raw_message_delivery: true if raw message delivery is enabled for the subscription. Raw messages are free of JSON formatting and can be sent to HTTP/S and Amazon SQS endpoints. For more information, see GetSubscriptionAttributes in the Amazon Simple Notification Service API Reference. Default: false
        :param region: The region where the topic resides, in the case of cross-region subscriptions. Default: - the region where the CloudFormation stack is being deployed.
        :param subscription_role_arn: Arn of role allowing access to firehose delivery stream. Required for a firehose subscription protocol. Default: - No subscription role is provided
        :param subscriber_id: The id of the SNS subscription resource created under ``scope``. In most cases, it is recommended to use the ``uniqueId`` of the topic you are subscribing to.
        :param subscriber_scope: The scope in which to create the SNS subscription resource. Normally you'd want the subscription to be created on the consuming stack because the topic is usually referenced by the consumer's resource policy (e.g. SQS queue policy). Otherwise, it will cause a cyclic reference. If this is undefined, the subscription will be created on the topic's stack. Default: - use the topic as the scope of the subscription, in which case ``subscriberId`` must be defined.
        :param subscription_dependency: The resources that need to be created before the subscription can be safely created. For example for SQS subscription, the subscription needs to have a dependency on the SQS queue policy in order for the subscription to successfully deliver messages. Default: - empty list

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_sns as sns
            from aws_cdk import aws_sqs as sqs
            import constructs as constructs
            
            # construct: constructs.Construct
            # dependable: constructs.IDependable
            # filter_or_policy: sns.FilterOrPolicy
            # queue: sqs.Queue
            # subscription_filter: sns.SubscriptionFilter
            
            topic_subscription_config = sns.TopicSubscriptionConfig(
                endpoint="endpoint",
                protocol=sns.SubscriptionProtocol.HTTP,
                subscriber_id="subscriberId",
            
                # the properties below are optional
                dead_letter_queue=queue,
                filter_policy={
                    "filter_policy_key": subscription_filter
                },
                filter_policy_with_message_body={
                    "filter_policy_with_message_body_key": filter_or_policy
                },
                raw_message_delivery=False,
                region="region",
                subscriber_scope=construct,
                subscription_dependency=dependable,
                subscription_role_arn="subscriptionRoleArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd56ac6d2cb8c4c70278e4ea1ea1a8ca0d0a6de563f2be0fe02916900d9f0d01)
            check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument dead_letter_queue", value=dead_letter_queue, expected_type=type_hints["dead_letter_queue"])
            check_type(argname="argument filter_policy", value=filter_policy, expected_type=type_hints["filter_policy"])
            check_type(argname="argument filter_policy_with_message_body", value=filter_policy_with_message_body, expected_type=type_hints["filter_policy_with_message_body"])
            check_type(argname="argument raw_message_delivery", value=raw_message_delivery, expected_type=type_hints["raw_message_delivery"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument subscription_role_arn", value=subscription_role_arn, expected_type=type_hints["subscription_role_arn"])
            check_type(argname="argument subscriber_id", value=subscriber_id, expected_type=type_hints["subscriber_id"])
            check_type(argname="argument subscriber_scope", value=subscriber_scope, expected_type=type_hints["subscriber_scope"])
            check_type(argname="argument subscription_dependency", value=subscription_dependency, expected_type=type_hints["subscription_dependency"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "endpoint": endpoint,
            "protocol": protocol,
            "subscriber_id": subscriber_id,
        }
        if dead_letter_queue is not None:
            self._values["dead_letter_queue"] = dead_letter_queue
        if filter_policy is not None:
            self._values["filter_policy"] = filter_policy
        if filter_policy_with_message_body is not None:
            self._values["filter_policy_with_message_body"] = filter_policy_with_message_body
        if raw_message_delivery is not None:
            self._values["raw_message_delivery"] = raw_message_delivery
        if region is not None:
            self._values["region"] = region
        if subscription_role_arn is not None:
            self._values["subscription_role_arn"] = subscription_role_arn
        if subscriber_scope is not None:
            self._values["subscriber_scope"] = subscriber_scope
        if subscription_dependency is not None:
            self._values["subscription_dependency"] = subscription_dependency

    @builtins.property
    def endpoint(self) -> builtins.str:
        '''The subscription endpoint.

        The meaning of this value depends on the value for 'protocol'.
        '''
        result = self._values.get("endpoint")
        assert result is not None, "Required property 'endpoint' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def protocol(self) -> SubscriptionProtocol:
        '''What type of subscription to add.'''
        result = self._values.get("protocol")
        assert result is not None, "Required property 'protocol' is missing"
        return typing.cast(SubscriptionProtocol, result)

    @builtins.property
    def dead_letter_queue(self) -> typing.Optional[_IQueue_7ed6f679]:
        '''Queue to be used as dead letter queue.

        If not passed no dead letter queue is enabled.

        :default: - No dead letter queue enabled.
        '''
        result = self._values.get("dead_letter_queue")
        return typing.cast(typing.Optional[_IQueue_7ed6f679], result)

    @builtins.property
    def filter_policy(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, SubscriptionFilter]]:
        '''The filter policy.

        :default: - all messages are delivered
        '''
        result = self._values.get("filter_policy")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, SubscriptionFilter]], result)

    @builtins.property
    def filter_policy_with_message_body(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, FilterOrPolicy]]:
        '''The filter policy that is applied on the message body.

        To apply a filter policy to the message attributes, use ``filterPolicy``. A maximum of one of ``filterPolicyWithMessageBody`` and ``filterPolicy`` may be used.

        :default: - all messages are delivered
        '''
        result = self._values.get("filter_policy_with_message_body")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, FilterOrPolicy]], result)

    @builtins.property
    def raw_message_delivery(self) -> typing.Optional[builtins.bool]:
        '''true if raw message delivery is enabled for the subscription.

        Raw messages are free of JSON formatting and can be
        sent to HTTP/S and Amazon SQS endpoints. For more information, see GetSubscriptionAttributes in the Amazon Simple
        Notification Service API Reference.

        :default: false
        '''
        result = self._values.get("raw_message_delivery")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''The region where the topic resides, in the case of cross-region subscriptions.

        :default: - the region where the CloudFormation stack is being deployed.

        :link: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-subscription.html#cfn-sns-subscription-region
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subscription_role_arn(self) -> typing.Optional[builtins.str]:
        '''Arn of role allowing access to firehose delivery stream.

        Required for a firehose subscription protocol.

        :default: - No subscription role is provided
        '''
        result = self._values.get("subscription_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subscriber_id(self) -> builtins.str:
        '''The id of the SNS subscription resource created under ``scope``.

        In most
        cases, it is recommended to use the ``uniqueId`` of the topic you are
        subscribing to.
        '''
        result = self._values.get("subscriber_id")
        assert result is not None, "Required property 'subscriber_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subscriber_scope(self) -> typing.Optional[_constructs_77d1e7e8.Construct]:
        '''The scope in which to create the SNS subscription resource.

        Normally you'd
        want the subscription to be created on the consuming stack because the
        topic is usually referenced by the consumer's resource policy (e.g. SQS
        queue policy). Otherwise, it will cause a cyclic reference.

        If this is undefined, the subscription will be created on the topic's stack.

        :default: - use the topic as the scope of the subscription, in which case ``subscriberId`` must be defined.
        '''
        result = self._values.get("subscriber_scope")
        return typing.cast(typing.Optional[_constructs_77d1e7e8.Construct], result)

    @builtins.property
    def subscription_dependency(
        self,
    ) -> typing.Optional[_constructs_77d1e7e8.IDependable]:
        '''The resources that need to be created before the subscription can be safely created.

        For example for SQS subscription, the subscription needs to have a dependency on the SQS queue policy
        in order for the subscription to successfully deliver messages.

        :default: - empty list
        '''
        result = self._values.get("subscription_dependency")
        return typing.cast(typing.Optional[_constructs_77d1e7e8.IDependable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TopicSubscriptionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_sns.TracingConfig")
class TracingConfig(enum.Enum):
    '''The tracing mode of an Amazon SNS topic.

    :exampleMetadata: infused

    Example::

        topic = sns.Topic(self, "MyTopic",
            tracing_config=sns.TracingConfig.ACTIVE
        )
    '''

    PASS_THROUGH = "PASS_THROUGH"
    '''The mode that topic passes trace headers received from the Amazon SNS publisher to its subscription.'''
    ACTIVE = "ACTIVE"
    '''The mode that Amazon SNS vend X-Ray segment data to topic owner account if the sampled flag in the tracing header is true.'''


class Filter(
    FilterOrPolicy,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_sns.Filter",
):
    '''Filter implementation of FilterOrPolicy.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_sns as sns
        
        # subscription_filter: sns.SubscriptionFilter
        
        filter = sns.Filter(subscription_filter)
    '''

    def __init__(self, filter_doc: SubscriptionFilter) -> None:
        '''Policy constructor.

        :param filter_doc: filter argument to construct.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0551be63b85435b5784eced066cfabfd78ec6716576cb76dfb0117c2ba208fdc)
            check_type(argname="argument filter_doc", value=filter_doc, expected_type=type_hints["filter_doc"])
        jsii.create(self.__class__, self, [filter_doc])

    @builtins.property
    @jsii.member(jsii_name="filterDoc")
    def filter_doc(self) -> SubscriptionFilter:
        '''filter argument to construct.'''
        return typing.cast(SubscriptionFilter, jsii.get(self, "filterDoc"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> FilterOrPolicyType:
        '''Type used in DFS buildFilterPolicyWithMessageBody to determine json value type.'''
        return typing.cast(FilterOrPolicyType, jsii.get(self, "type"))


class Topic(TopicBase, metaclass=jsii.JSIIMeta, jsii_type="aws-cdk-lib.aws_sns.Topic"):
    '''A new SNS topic.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_sns as sns
        
        
        topic = sns.Topic(self, "MyTopic")
        
        topic_rule = iot.TopicRule(self, "TopicRule",
            sql=iot.IotSql.from_string_as_ver20160323("SELECT topic(2) as device_id, year, month, day FROM 'device/+/data'"),
            actions=[
                actions.SnsTopicAction(topic,
                    message_format=actions.SnsActionMessageFormat.JSON
                )
            ]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        content_based_deduplication: typing.Optional[builtins.bool] = None,
        display_name: typing.Optional[builtins.str] = None,
        enforce_ssl: typing.Optional[builtins.bool] = None,
        fifo: typing.Optional[builtins.bool] = None,
        logging_configs: typing.Optional[typing.Sequence[typing.Union[LoggingConfig, typing.Dict[builtins.str, typing.Any]]]] = None,
        master_key: typing.Optional[_IKey_5f11635f] = None,
        message_retention_period_in_days: typing.Optional[jsii.Number] = None,
        signature_version: typing.Optional[builtins.str] = None,
        topic_name: typing.Optional[builtins.str] = None,
        tracing_config: typing.Optional[TracingConfig] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param content_based_deduplication: Enables content-based deduplication for FIFO topics. Default: None
        :param display_name: A developer-defined string that can be used to identify this SNS topic. Default: None
        :param enforce_ssl: Adds a statement to enforce encryption of data in transit when publishing to the topic. Default: false
        :param fifo: Set to true to create a FIFO topic. Default: None
        :param logging_configs: The list of delivery status logging configurations for the topic. Default: None
        :param master_key: A KMS Key, either managed by this CDK app, or imported. Default: None
        :param message_retention_period_in_days: The number of days Amazon SNS retains messages. It can only be set for FIFO topics. Default: - do not archive messages
        :param signature_version: The signature version corresponds to the hashing algorithm used while creating the signature of the notifications, subscription confirmations, or unsubscribe confirmation messages sent by Amazon SNS. Default: 1
        :param topic_name: A name for the topic. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the topic name. For more information, see Name Type. Default: Generated name
        :param tracing_config: Tracing mode of an Amazon SNS topic. Default: TracingConfig.PASS_THROUGH
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5bf7b7a1001dc600e81a7f1c5015e367dc471dcd727360f62a7eaf6ebf762afd)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = TopicProps(
            content_based_deduplication=content_based_deduplication,
            display_name=display_name,
            enforce_ssl=enforce_ssl,
            fifo=fifo,
            logging_configs=logging_configs,
            master_key=master_key,
            message_retention_period_in_days=message_retention_period_in_days,
            signature_version=signature_version,
            topic_name=topic_name,
            tracing_config=tracing_config,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromTopicArn")
    @builtins.classmethod
    def from_topic_arn(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        topic_arn: builtins.str,
    ) -> ITopic:
        '''Import an existing SNS topic provided an ARN.

        :param scope: The parent creating construct.
        :param id: The construct's name.
        :param topic_arn: topic ARN (i.e. arn:aws:sns:us-east-2:444455556666:MyTopic).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__957d6ca1d36d79217c9c31f9f5959901c25a458abcbfc9b7eb6aa5b70506ad52)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument topic_arn", value=topic_arn, expected_type=type_hints["topic_arn"])
        return typing.cast(ITopic, jsii.sinvoke(cls, "fromTopicArn", [scope, id, topic_arn]))

    @jsii.member(jsii_name="fromTopicAttributes")
    @builtins.classmethod
    def from_topic_attributes(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        topic_arn: builtins.str,
        content_based_deduplication: typing.Optional[builtins.bool] = None,
    ) -> ITopic:
        '''Import an existing SNS topic provided a topic attributes.

        :param scope: The parent creating construct.
        :param id: The construct's name.
        :param topic_arn: The ARN of the SNS topic.
        :param content_based_deduplication: Whether content-based deduplication is enabled. Only applicable for FIFO topics. Default: false
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3116994a7284b362cb667f2b74c1b4035605be5e3339d6c2782787473f6131f6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        attrs = TopicAttributes(
            topic_arn=topic_arn,
            content_based_deduplication=content_based_deduplication,
        )

        return typing.cast(ITopic, jsii.sinvoke(cls, "fromTopicAttributes", [scope, id, attrs]))

    @jsii.member(jsii_name="addLoggingConfig")
    def add_logging_config(
        self,
        *,
        protocol: LoggingProtocol,
        failure_feedback_role: typing.Optional[_IRole_235f5d8e] = None,
        success_feedback_role: typing.Optional[_IRole_235f5d8e] = None,
        success_feedback_sample_rate: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Adds a delivery status logging configuration to the topic.

        :param protocol: Indicates one of the supported protocols for the SNS topic.
        :param failure_feedback_role: The IAM role to be used when logging failed message deliveries in Amazon CloudWatch. Default: None
        :param success_feedback_role: The IAM role to be used when logging successful message deliveries in Amazon CloudWatch. Default: None
        :param success_feedback_sample_rate: The percentage of successful message deliveries to be logged in Amazon CloudWatch. Valid values are integer between 0-100 Default: None
        '''
        config = LoggingConfig(
            protocol=protocol,
            failure_feedback_role=failure_feedback_role,
            success_feedback_role=success_feedback_role,
            success_feedback_sample_rate=success_feedback_sample_rate,
        )

        return typing.cast(None, jsii.invoke(self, "addLoggingConfig", [config]))

    @builtins.property
    @jsii.member(jsii_name="autoCreatePolicy")
    def _auto_create_policy(self) -> builtins.bool:
        '''Controls automatic creation of policy objects.

        Set by subclasses.
        '''
        return typing.cast(builtins.bool, jsii.get(self, "autoCreatePolicy"))

    @builtins.property
    @jsii.member(jsii_name="contentBasedDeduplication")
    def content_based_deduplication(self) -> builtins.bool:
        '''Enables content-based deduplication for FIFO topics.'''
        return typing.cast(builtins.bool, jsii.get(self, "contentBasedDeduplication"))

    @builtins.property
    @jsii.member(jsii_name="fifo")
    def fifo(self) -> builtins.bool:
        '''Whether this topic is an Amazon SNS FIFO queue.

        If false, this is a standard topic.
        '''
        return typing.cast(builtins.bool, jsii.get(self, "fifo"))

    @builtins.property
    @jsii.member(jsii_name="topicArn")
    def topic_arn(self) -> builtins.str:
        '''The ARN of the topic.'''
        return typing.cast(builtins.str, jsii.get(self, "topicArn"))

    @builtins.property
    @jsii.member(jsii_name="topicName")
    def topic_name(self) -> builtins.str:
        '''The name of the topic.'''
        return typing.cast(builtins.str, jsii.get(self, "topicName"))


__all__ = [
    "BetweenCondition",
    "CfnSubscription",
    "CfnSubscriptionProps",
    "CfnTopic",
    "CfnTopicInlinePolicy",
    "CfnTopicInlinePolicyProps",
    "CfnTopicPolicy",
    "CfnTopicPolicyProps",
    "CfnTopicProps",
    "Filter",
    "FilterOrPolicy",
    "FilterOrPolicyType",
    "ITopic",
    "ITopicSubscription",
    "LoggingConfig",
    "LoggingProtocol",
    "NumericConditions",
    "Policy",
    "StringConditions",
    "Subscription",
    "SubscriptionFilter",
    "SubscriptionOptions",
    "SubscriptionProps",
    "SubscriptionProtocol",
    "Topic",
    "TopicAttributes",
    "TopicBase",
    "TopicPolicy",
    "TopicPolicyProps",
    "TopicProps",
    "TopicSubscriptionConfig",
    "TracingConfig",
]

publication.publish()

def _typecheckingstub__5ebb3778ab30030aa884085aeda12c2079b30d59a16602ab32cd66efdb1de356(
    *,
    start: jsii.Number,
    stop: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f3839647e73879ccdb1519ec2afccf78b6168046279d32c5390b3e2543d1fec(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    protocol: builtins.str,
    topic_arn: builtins.str,
    delivery_policy: typing.Any = None,
    endpoint: typing.Optional[builtins.str] = None,
    filter_policy: typing.Any = None,
    filter_policy_scope: typing.Optional[builtins.str] = None,
    raw_message_delivery: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    redrive_policy: typing.Any = None,
    region: typing.Optional[builtins.str] = None,
    replay_policy: typing.Any = None,
    subscription_role_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ad167deaa30cad42bef358dc9a03bed1399dc45e07655b5e137a67f04418907(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97d8f48dcae3735a971499612987e1098d379f23b6c7cd953ea2feccf6050c2a(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7edc75a221f1678a2af2a8200b26975f38bc8f1f405e735dbdeff306d6b51f8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__695665f02c816a5f5b8823c7113d6f83dc37a450f1e44a469efc6b646a042042(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__363ef69700500450c12f41b43c0226475a42d465d0e2c1eb2c6a62103297a77d(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51bd5ec550058313034fb332f79c3420c0ab46be8aaa0abb6b7489748ace3b8f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e0ead2904ccf72657e766b50c2aef479b86c25ba314b73f122eedee3bf8f859(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8b99524984cf1e668a25b6f6425da23c5d12b2d696637bdc50a8fdab3282ac6(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b31b31d2e697eb675dfd0da4695e87324259ab34307bec1a543ab628d2d371d0(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5fbcc2d22ef7dec8cd3d31ce95fa8e065175f8957313872e3b1a02015210c603(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22cba62b05c6e7ecdf0102d83ee908ae549d02df6eb8dd5643c2c42074fdf936(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a75cc1735865b82732f90f42a2ba55634431d8bdec48d0a7752a79354f0c850d(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a71b3667b255126f8bc5b4059f4687fa922e718121515d78883ff30eb130ad2a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0227b0c451693656571029cae1cbec74d209cf9e946210145d282e8f03fd1d28(
    *,
    protocol: builtins.str,
    topic_arn: builtins.str,
    delivery_policy: typing.Any = None,
    endpoint: typing.Optional[builtins.str] = None,
    filter_policy: typing.Any = None,
    filter_policy_scope: typing.Optional[builtins.str] = None,
    raw_message_delivery: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    redrive_policy: typing.Any = None,
    region: typing.Optional[builtins.str] = None,
    replay_policy: typing.Any = None,
    subscription_role_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c3e689eaa6b740299fa6db2e53acc51021bc5deb0a8dd6d7bc29e8a364a1dfe(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    archive_policy: typing.Any = None,
    content_based_deduplication: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    data_protection_policy: typing.Any = None,
    delivery_status_logging: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTopic.LoggingConfigProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    display_name: typing.Optional[builtins.str] = None,
    fifo_topic: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    kms_master_key_id: typing.Optional[builtins.str] = None,
    signature_version: typing.Optional[builtins.str] = None,
    subscription: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTopic.SubscriptionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    topic_name: typing.Optional[builtins.str] = None,
    tracing_config: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__daf5369a4f3860bacf2f29e2b4cb7ddb422f52f07b72cb603e80cd57ba407136(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b026fb3f06827298c161d83a15c46ff302bba18c779bbe604b86a1346f8a4d0(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4e735a5dfc67b4dafec2e9df7180dd3143cb26437dc792dcb49e9563663dd22(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61855b81d1d953ec33b8c0af7bad8099bc0ec45c2624d213b520131ecf95b724(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0fa01cdb622f9c1239adaa1d51fb0035fbf98f9f42d4c5cf2e419e59e007298b(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c45e4d025e306c26000e7fa2d0ac2f744ec4393a8a4418f9a397a2f5c010e0cf(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnTopic.LoggingConfigProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e672f7b6cfea2a409a715963f8ef1b01848153bb4867f8ad868e0bcb32a4fe4(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a91ed56c1865e9ea5cd3d8d5ffef0aab07b45ce41c2580607fd141166a194ea(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d940f36146ec2822d49a51165f9625c406a6b8add68591ddb68de7681318435b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48790d8e0040c4fbaea7344de60c0f7d90bd512df53025055db78e6b9bac4a4e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f416792b5d579d938563017fc236edff31ba5aeb335512720ae83552c6832e9c(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnTopic.SubscriptionProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4fc70aec71b6f6c75ff5cf5bd0ed0934ffe27fd6747714e83d2cd44e32ff452(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__774919bb9f8040862e9d2ff7d63e5862fa36e6930f96feffa891ad451553d624(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cca8ae0da10f9d461cb6a1d8687e3d2ee9214548942dacdad4fbbf396119fbcc(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__504f5c0a818ef27c6f26af4cf94e85376e3929a210ed0fc76e17575e3a997054(
    *,
    protocol: builtins.str,
    failure_feedback_role_arn: typing.Optional[builtins.str] = None,
    success_feedback_role_arn: typing.Optional[builtins.str] = None,
    success_feedback_sample_rate: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0e99e91f630467ca29bdde2bfed1506da130d5f3e0cae1685b42e10bf0537dc(
    *,
    endpoint: builtins.str,
    protocol: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc6ea227f85a0ee7689700544a9f92c1220134ca2d2baa5667c368181a9e8a32(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    policy_document: typing.Any,
    topic_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__068f56f45055c0013d26c4ff1b8eba591d1ba7fde252cbc1a41c85476969cd0a(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de3f18c32c20096788214fcc04b3e4bd211654412293d35e75c91ceee4ce8bfb(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8275626d8b21f671694dcee09744c4e6b75f065ed837225bf415305c04b7b7ed(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7fb2268d3e7860e0e1aef3261e22ab7f2e0f8f6a170f6dc068791cef3502c7d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cdf37eb1dc6c7082cc2dd899c6b1f40d17fbd1563f692e9ea9111bd824ec9dad(
    *,
    policy_document: typing.Any,
    topic_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a74b2018f34253c91ec670526565616a2473df25a6a5108c2fbafc189dd5ce18(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    policy_document: typing.Any,
    topics: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6ae43fa297025629494d67fe989386d5dddecd1473f7e43bff2e1d5fc227000(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0733bdab832ad72cd8bd92fba796973a855911ccc2927c3343a635279052687c(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d6879a3cebc5ad4daeee6ede4d90bd5183664f6abf021b475aa5d9fc535c10c(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4eb0294b972b7ccbe6bd3a88c438e8d519ab90fa35e136b6b4272a65abd4db0a(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1894bd2779686bb602d2a76bb004026f405ddb9d5ec17e6982a4da918e8a1a9f(
    *,
    policy_document: typing.Any,
    topics: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39eaeffb1fed865d99c7cf51cdf720d8471aec20b2163161ef50035fbeafbf13(
    *,
    archive_policy: typing.Any = None,
    content_based_deduplication: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    data_protection_policy: typing.Any = None,
    delivery_status_logging: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTopic.LoggingConfigProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    display_name: typing.Optional[builtins.str] = None,
    fifo_topic: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    kms_master_key_id: typing.Optional[builtins.str] = None,
    signature_version: typing.Optional[builtins.str] = None,
    subscription: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTopic.SubscriptionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    topic_name: typing.Optional[builtins.str] = None,
    tracing_config: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48b960a8d07778472d280833dc7671d5e58991a28e7dd556c9d0aaf7509fb28e(
    filter: SubscriptionFilter,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3bfe2da643ae34d8de4bb104c40157d580fd7cce715aa1fe916f39f1922887f1(
    policy: typing.Mapping[builtins.str, FilterOrPolicy],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3254ccc49f43f33130f11f9db98dd8a000762fcec4aeed1d0e619180d6590c66(
    subscription: ITopicSubscription,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a25cf01212afa98a52126c366524ccb1dfcf92425078abf30316c0b680f26307(
    statement: _PolicyStatement_0fe33853,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf96d0b079cfedfe1ad406a08f2229f4ed5332b9d92fc6d78e1571fce3a1ee5f(
    identity: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05c3997edd40866d6774aed03c03e55b6cf80f23f518be34bcdf19adf065db7c(
    metric_name: builtins.str,
    *,
    account: typing.Optional[builtins.str] = None,
    color: typing.Optional[builtins.str] = None,
    dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    label: typing.Optional[builtins.str] = None,
    period: typing.Optional[_Duration_4839e8c3] = None,
    region: typing.Optional[builtins.str] = None,
    statistic: typing.Optional[builtins.str] = None,
    unit: typing.Optional[_Unit_61bc6f70] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__daf70c7f74db8d44ef157cdd3df3a90e91ac1b55f6be3c7ec557b2c6d285720a(
    topic: ITopic,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9eb41e45f77d56f958dda8c78b2c068faf3edbd60bc3b2a62a19317f5490622(
    *,
    protocol: LoggingProtocol,
    failure_feedback_role: typing.Optional[_IRole_235f5d8e] = None,
    success_feedback_role: typing.Optional[_IRole_235f5d8e] = None,
    success_feedback_sample_rate: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__275a537da31cf603117422e452eeec6e2885ee8265e341324d589072c1703641(
    *,
    allowlist: typing.Optional[typing.Sequence[jsii.Number]] = None,
    between: typing.Optional[typing.Union[BetweenCondition, typing.Dict[builtins.str, typing.Any]]] = None,
    between_strict: typing.Optional[typing.Union[BetweenCondition, typing.Dict[builtins.str, typing.Any]]] = None,
    greater_than: typing.Optional[jsii.Number] = None,
    greater_than_or_equal_to: typing.Optional[jsii.Number] = None,
    less_than: typing.Optional[jsii.Number] = None,
    less_than_or_equal_to: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83467db20c58c3a233e8e98fe95c435848f7d6f585004282a535427100d7c20f(
    policy_doc: typing.Mapping[builtins.str, FilterOrPolicy],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__608bd3c9ae19b496ea71293f19119c75ba12a13947777e25f50e21d76ee1afa9(
    *,
    allowlist: typing.Optional[typing.Sequence[builtins.str]] = None,
    denylist: typing.Optional[typing.Sequence[builtins.str]] = None,
    match_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
    match_suffixes: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ba93ce15c8c35d2f3ef25181ab5de6aae90de3adaf596e2b2f2e51f92bce5a3(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    topic: ITopic,
    endpoint: builtins.str,
    protocol: SubscriptionProtocol,
    dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
    filter_policy: typing.Optional[typing.Mapping[builtins.str, SubscriptionFilter]] = None,
    filter_policy_with_message_body: typing.Optional[typing.Mapping[builtins.str, FilterOrPolicy]] = None,
    raw_message_delivery: typing.Optional[builtins.bool] = None,
    region: typing.Optional[builtins.str] = None,
    subscription_role_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1fada138ee1fc7d11bbf797b2a645bbf52b3239972a66be3174051b994ad84a8(
    conditions: typing.Optional[typing.Sequence[typing.Any]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bce75a2ad593ea78ce07c3bf1cbe6c0262cc48f6f133af363ca95a0cadfb6008(
    *,
    endpoint: builtins.str,
    protocol: SubscriptionProtocol,
    dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
    filter_policy: typing.Optional[typing.Mapping[builtins.str, SubscriptionFilter]] = None,
    filter_policy_with_message_body: typing.Optional[typing.Mapping[builtins.str, FilterOrPolicy]] = None,
    raw_message_delivery: typing.Optional[builtins.bool] = None,
    region: typing.Optional[builtins.str] = None,
    subscription_role_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca027bfed18b17f0f94ff71f11bf24813f4ec24f9b1029e73d8da4ef880e57a4(
    *,
    endpoint: builtins.str,
    protocol: SubscriptionProtocol,
    dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
    filter_policy: typing.Optional[typing.Mapping[builtins.str, SubscriptionFilter]] = None,
    filter_policy_with_message_body: typing.Optional[typing.Mapping[builtins.str, FilterOrPolicy]] = None,
    raw_message_delivery: typing.Optional[builtins.bool] = None,
    region: typing.Optional[builtins.str] = None,
    subscription_role_arn: typing.Optional[builtins.str] = None,
    topic: ITopic,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8362e16cf38fb93899cf1443c05ea87f926cf385d45c4f25eb95067bff9642a(
    *,
    topic_arn: builtins.str,
    content_based_deduplication: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e97a3ac4042ed403ad7f37324d239151dacf8c0ddc949fcb2cda9467c86d55c3(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    account: typing.Optional[builtins.str] = None,
    environment_from_arn: typing.Optional[builtins.str] = None,
    physical_name: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3af87d479cce0479b13b487a212b9eb786dc4faba1cadb3a6451209927770a60(
    topic_subscription: ITopicSubscription,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7f4d520e0fc706fbd4e1415b076009a3ab58db83ac7b721c03dba894f99c83d(
    statement: _PolicyStatement_0fe33853,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04cdaba4727d1a890bbc0d5d2854229f71f59b72c42feadb21ad6387b14c83bd(
    _scope: _constructs_77d1e7e8.Construct,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6461236ee087e9f8e6de731371b913e918bbd3ec5d928bd677a69c9c8eb82381(
    grantee: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b07969d7a2c71869715d0fe87d9b0d9d67f663ddecc9d81d353ba532fdaa3b8d(
    metric_name: builtins.str,
    *,
    account: typing.Optional[builtins.str] = None,
    color: typing.Optional[builtins.str] = None,
    dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    label: typing.Optional[builtins.str] = None,
    period: typing.Optional[_Duration_4839e8c3] = None,
    region: typing.Optional[builtins.str] = None,
    statistic: typing.Optional[builtins.str] = None,
    unit: typing.Optional[_Unit_61bc6f70] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41d14f58fd3a68985cc9146f591de9ef04f0766e0e4ab580bec4fe74fde70eee(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12a056cfcdc8bff96e7fe29bb021bebfb1f092d261da925723087b52a2a52c91(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    topics: typing.Sequence[ITopic],
    enforce_ssl: typing.Optional[builtins.bool] = None,
    policy_document: typing.Optional[_PolicyDocument_3ac34393] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68fd01009ddae128e0ad9f5816da32ac0ad127b82df6140a2431cf829c9a7488(
    topic_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4116dddf14d28d4bd4bb7d68b0eda71322f8faeb2468828dde6eca112513ba6b(
    *,
    topics: typing.Sequence[ITopic],
    enforce_ssl: typing.Optional[builtins.bool] = None,
    policy_document: typing.Optional[_PolicyDocument_3ac34393] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__093960c1ab5457cc6797eb4a06c9e8fc74e41d4eaa9d0a17f00fa896dadf9161(
    *,
    content_based_deduplication: typing.Optional[builtins.bool] = None,
    display_name: typing.Optional[builtins.str] = None,
    enforce_ssl: typing.Optional[builtins.bool] = None,
    fifo: typing.Optional[builtins.bool] = None,
    logging_configs: typing.Optional[typing.Sequence[typing.Union[LoggingConfig, typing.Dict[builtins.str, typing.Any]]]] = None,
    master_key: typing.Optional[_IKey_5f11635f] = None,
    message_retention_period_in_days: typing.Optional[jsii.Number] = None,
    signature_version: typing.Optional[builtins.str] = None,
    topic_name: typing.Optional[builtins.str] = None,
    tracing_config: typing.Optional[TracingConfig] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd56ac6d2cb8c4c70278e4ea1ea1a8ca0d0a6de563f2be0fe02916900d9f0d01(
    *,
    endpoint: builtins.str,
    protocol: SubscriptionProtocol,
    dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
    filter_policy: typing.Optional[typing.Mapping[builtins.str, SubscriptionFilter]] = None,
    filter_policy_with_message_body: typing.Optional[typing.Mapping[builtins.str, FilterOrPolicy]] = None,
    raw_message_delivery: typing.Optional[builtins.bool] = None,
    region: typing.Optional[builtins.str] = None,
    subscription_role_arn: typing.Optional[builtins.str] = None,
    subscriber_id: builtins.str,
    subscriber_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
    subscription_dependency: typing.Optional[_constructs_77d1e7e8.IDependable] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0551be63b85435b5784eced066cfabfd78ec6716576cb76dfb0117c2ba208fdc(
    filter_doc: SubscriptionFilter,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5bf7b7a1001dc600e81a7f1c5015e367dc471dcd727360f62a7eaf6ebf762afd(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    content_based_deduplication: typing.Optional[builtins.bool] = None,
    display_name: typing.Optional[builtins.str] = None,
    enforce_ssl: typing.Optional[builtins.bool] = None,
    fifo: typing.Optional[builtins.bool] = None,
    logging_configs: typing.Optional[typing.Sequence[typing.Union[LoggingConfig, typing.Dict[builtins.str, typing.Any]]]] = None,
    master_key: typing.Optional[_IKey_5f11635f] = None,
    message_retention_period_in_days: typing.Optional[jsii.Number] = None,
    signature_version: typing.Optional[builtins.str] = None,
    topic_name: typing.Optional[builtins.str] = None,
    tracing_config: typing.Optional[TracingConfig] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__957d6ca1d36d79217c9c31f9f5959901c25a458abcbfc9b7eb6aa5b70506ad52(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    topic_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3116994a7284b362cb667f2b74c1b4035605be5e3339d6c2782787473f6131f6(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    topic_arn: builtins.str,
    content_based_deduplication: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass
