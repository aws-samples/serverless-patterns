'''
# Amazon CloudWatch Logs Construct Library

This library supplies constructs for working with CloudWatch Logs.

## Log Groups/Streams

The basic unit of CloudWatch is a *Log Group*. Every log group typically has the
same kind of data logged to it, in the same format. If there are multiple
applications or services logging into the Log Group, each of them creates a new
*Log Stream*.

Every log operation creates a "log event", which can consist of a simple string
or a single-line JSON object. JSON objects have the advantage that they afford
more filtering abilities (see below).

The only configurable attribute for log streams is the retention period, which
configures after how much time the events in the log stream expire and are
deleted.

The default retention period if not supplied is 2 years, but it can be set to
one of the values in the `RetentionDays` enum to configure a different
retention period (including infinite retention).

```python
# Configure log group for short retention
log_group = LogGroup(stack, "LogGroup",
    retention=RetentionDays.ONE_WEEK
)# Configure log group for infinite retention
log_group = LogGroup(stack, "LogGroup",
    retention=Infinity
)
```

## LogRetention

The `LogRetention` construct is a way to control the retention period of log groups that are created outside of the CDK. The construct is usually
used on log groups that are auto created by AWS services, such as [AWS
lambda](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-cloudwatchlogs.html).

This is implemented using a [CloudFormation custom
resource](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cfn-customresource.html)
which pre-creates the log group if it doesn't exist, and sets the specified log retention period (never expire, by default).

By default, the log group will be created in the same region as the stack. The `logGroupRegion` property can be used to configure
log groups in other regions. This is typically useful when controlling retention for log groups auto-created by global services that
publish their log group to a specific region, such as AWS Chatbot creating a log group in `us-east-1`.

By default, the log group created by LogRetention will be retained after the stack is deleted. If the RemovalPolicy is set to DESTROY, then the log group will be deleted when the stack is deleted.

## Resource Policy

CloudWatch Resource Policies allow other AWS services or IAM Principals to put log events into the log groups.
A resource policy is automatically created when `addToResourcePolicy` is called on the LogGroup for the first time:

```python
log_group = logs.LogGroup(self, "LogGroup")
log_group.add_to_resource_policy(iam.PolicyStatement(
    actions=["logs:CreateLogStream", "logs:PutLogEvents"],
    principals=[iam.ServicePrincipal("es.amazonaws.com")],
    resources=[log_group.log_group_arn]
))
```

Or more conveniently, write permissions to the log group can be granted as follows which gives same result as in the above example.

```python
log_group = logs.LogGroup(self, "LogGroup")
log_group.grant_write(iam.ServicePrincipal("es.amazonaws.com"))
```

Similarily, read permissions can be granted to the log group as follows.

```python
log_group = logs.LogGroup(self, "LogGroup")
log_group.grant_read(iam.ServicePrincipal("es.amazonaws.com"))
```

Be aware that any ARNs or tokenized values passed to the resource policy will be converted into AWS Account IDs.
This is because CloudWatch Logs Resource Policies do not accept ARNs as principals, but they do accept
Account ID strings. Non-ARN principals, like Service principals or Any principals, are accepted by CloudWatch.

## Encrypting Log Groups

By default, log group data is always encrypted in CloudWatch Logs. You have the
option to encrypt log group data using a AWS KMS customer master key (CMK) should
you not wish to use the default AWS encryption. Keep in mind that if you decide to
encrypt a log group, any service or IAM identity that needs to read the encrypted
log streams in the future will require the same CMK to decrypt the data.

Here's a simple example of creating an encrypted Log Group using a KMS CMK.

```python
import aws_cdk.aws_kms as kms


logs.LogGroup(self, "LogGroup",
    encryption_key=kms.Key(self, "Key")
)
```

See the AWS documentation for more detailed information about [encrypting CloudWatch
Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/encrypt-log-data-kms.html).

## Subscriptions and Destinations

Log events matching a particular filter can be sent to either a Lambda function
or a Kinesis stream.

If the Kinesis stream lives in a different account, a `CrossAccountDestination`
object needs to be added in the destination account which will act as a proxy
for the remote Kinesis stream. This object is automatically created for you
if you use the CDK Kinesis library.

Create a `SubscriptionFilter`, initialize it with an appropriate `Pattern` (see
below) and supply the intended destination:

```python
import aws_cdk.aws_logs_destinations as destinations

# fn: lambda.Function
# log_group: logs.LogGroup


logs.SubscriptionFilter(self, "Subscription",
    log_group=log_group,
    destination=destinations.LambdaDestination(fn),
    filter_pattern=logs.FilterPattern.all_terms("ERROR", "MainThread"),
    filter_name="ErrorInMainThread"
)
```

## Metric Filters

CloudWatch Logs can extract and emit metrics based on a textual log stream.
Depending on your needs, this may be a more convenient way of generating metrics
for you application than making calls to CloudWatch Metrics yourself.

A `MetricFilter` either emits a fixed number every time it sees a log event
matching a particular pattern (see below), or extracts a number from the log
event and uses that as the metric value.

Example:

```python
MetricFilter(self, "MetricFilter",
    log_group=log_group,
    metric_namespace="MyApp",
    metric_name="Latency",
    filter_pattern=FilterPattern.exists("$.latency"),
    metric_value="$.latency"
)
```

Remember that if you want to use a value from the log event as the metric value,
you must mention it in your pattern somewhere.

A very simple MetricFilter can be created by using the `logGroup.extractMetric()`
helper function:

```python
# log_group: logs.LogGroup

log_group.extract_metric("$.jsonField", "Namespace", "MetricName")
```

Will extract the value of `jsonField` wherever it occurs in JSON-structured
log records in the LogGroup, and emit them to CloudWatch Metrics under
the name `Namespace/MetricName`.

### Exposing Metric on a Metric Filter

You can expose a metric on a metric filter by calling the `MetricFilter.metric()` API.
This has a default of `statistic = 'avg'` if the statistic is not set in the `props`.

```python
# log_group: logs.LogGroup

mf = logs.MetricFilter(self, "MetricFilter",
    log_group=log_group,
    metric_namespace="MyApp",
    metric_name="Latency",
    filter_pattern=logs.FilterPattern.exists("$.latency"),
    metric_value="$.latency",
    dimensions={
        "ErrorCode": "$.errorCode"
    },
    unit=cloudwatch.Unit.MILLISECONDS
)

# expose a metric from the metric filter
metric = mf.metric()

# you can use the metric to create a new alarm
cloudwatch.Alarm(self, "alarm from metric filter",
    metric=metric,
    threshold=100,
    evaluation_periods=2
)
```

## Patterns

Patterns describe which log events match a subscription or metric filter. There
are three types of patterns:

* Text patterns
* JSON patterns
* Space-delimited table patterns

All patterns are constructed by using static functions on the `FilterPattern`
class.

In addition to the patterns above, the following special patterns exist:

* `FilterPattern.allEvents()`: matches all log events.
* `FilterPattern.literal(string)`: if you already know what pattern expression to
  use, this function takes a string and will use that as the log pattern. For
  more information, see the [Filter and Pattern
  Syntax](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html).

### Text Patterns

Text patterns match if the literal strings appear in the text form of the log
line.

* `FilterPattern.allTerms(term, term, ...)`: matches if all of the given terms
  (substrings) appear in the log event.
* `FilterPattern.anyTerm(term, term, ...)`: matches if all of the given terms
  (substrings) appear in the log event.
* `FilterPattern.anyTermGroup([term, term, ...], [term, term, ...], ...)`: matches if
  all of the terms in any of the groups (specified as arrays) matches. This is
  an OR match.

Examples:

```python
# Search for lines that contain both "ERROR" and "MainThread"
pattern1 = logs.FilterPattern.all_terms("ERROR", "MainThread")

# Search for lines that either contain both "ERROR" and "MainThread", or
# both "WARN" and "Deadlock".
pattern2 = logs.FilterPattern.any_term_group(["ERROR", "MainThread"], ["WARN", "Deadlock"])
```

## JSON Patterns

JSON patterns apply if the log event is the JSON representation of an object
(without any other characters, so it cannot include a prefix such as timestamp
or log level). JSON patterns can make comparisons on the values inside the
fields.

* **Strings**: the comparison operators allowed for strings are `=` and `!=`.
  String values can start or end with a `*` wildcard.
* **Numbers**: the comparison operators allowed for numbers are `=`, `!=`,
  `<`, `<=`, `>`, `>=`.

Fields in the JSON structure are identified by identifier the complete object as `$`
and then descending into it, such as `$.field` or `$.list[0].field`.

* `FilterPattern.stringValue(field, comparison, string)`: matches if the given
  field compares as indicated with the given string value.
* `FilterPattern.numberValue(field, comparison, number)`: matches if the given
  field compares as indicated with the given numerical value.
* `FilterPattern.isNull(field)`: matches if the given field exists and has the
  value `null`.
* `FilterPattern.notExists(field)`: matches if the given field is not in the JSON
  structure.
* `FilterPattern.exists(field)`: matches if the given field is in the JSON
  structure.
* `FilterPattern.booleanValue(field, boolean)`: matches if the given field
  is exactly the given boolean value.
* `FilterPattern.all(jsonPattern, jsonPattern, ...)`: matches if all of the
  given JSON patterns match. This makes an AND combination of the given
  patterns.
* `FilterPattern.any(jsonPattern, jsonPattern, ...)`: matches if any of the
  given JSON patterns match. This makes an OR combination of the given
  patterns.

Example:

```python
# Search for all events where the component field is equal to
# "HttpServer" and either error is true or the latency is higher
# than 1000.
pattern = logs.FilterPattern.all(
    logs.FilterPattern.string_value("$.component", "=", "HttpServer"),
    logs.FilterPattern.any(
        logs.FilterPattern.boolean_value("$.error", True),
        logs.FilterPattern.number_value("$.latency", ">", 1000)))
```

## Space-delimited table patterns

If the log events are rows of a space-delimited table, this pattern can be used
to identify the columns in that structure and add conditions on any of them. The
canonical example where you would apply this type of pattern is Apache server
logs.

Text that is surrounded by `"..."` quotes or `[...]` square brackets will
be treated as one column.

* `FilterPattern.spaceDelimited(column, column, ...)`: construct a
  `SpaceDelimitedTextPattern` object with the indicated columns. The columns
  map one-by-one the columns found in the log event. The string `"..."` may
  be used to specify an arbitrary number of unnamed columns anywhere in the
  name list (but may only be specified once).

After constructing a `SpaceDelimitedTextPattern`, you can use the following
two members to add restrictions:

* `pattern.whereString(field, comparison, string)`: add a string condition.
  The rules are the same as for JSON patterns.
* `pattern.whereNumber(field, comparison, number)`: add a numerical condition.
  The rules are the same as for JSON patterns.

Multiple restrictions can be added on the same column; they must all apply.

Example:

```python
# Search for all events where the component is "HttpServer" and the
# result code is not equal to 200.
pattern = logs.FilterPattern.space_delimited("time", "component", "...", "result_code", "latency").where_string("component", "=", "HttpServer").where_number("result_code", "!=", 200)
```

## Logs Insights Query Definition

Creates a query definition for CloudWatch Logs Insights.

Example:

```python
logs.QueryDefinition(self, "QueryDefinition",
    query_definition_name="MyQuery",
    query_string=logs.QueryString(
        fields=["@timestamp", "@message"],
        parse_statements=["@message \"[*] *\" as loggingType, loggingMessage", "@message \"<*>: *\" as differentLoggingType, differentLoggingMessage"
        ],
        filter_statements=["loggingType = \"ERROR\"", "loggingMessage = \"A very strange error occurred!\""
        ],
        sort="@timestamp desc",
        limit=20
    )
)
```

## Data Protection Policy

Creates a data protection policy and assigns it to the log group. A data protection policy can help safeguard sensitive data that's ingested by the log group by auditing and masking the sensitive log data. When a user who does not have permission to view masked data views a log event that includes masked data, the sensitive data is replaced by asterisks.

For more information, see [Protect sensitive log data with masking](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/mask-sensitive-log-data.html).

For a list of types of identifiers that can be audited and masked, see [Types of data that you can protect](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/protect-sensitive-log-data-types.html)

If a new identifier is supported but not yet in the `DataIdentifiers` enum, the full ARN of the identifier can be supplied in `identifierArnStrings` instead.

Each policy may consist of a log group, S3 bucket, and/or Firehose delivery stream audit destination.

Example:

```python
import aws_cdk.aws_kinesisfirehose_alpha as kinesisfirehose
import aws_cdk.aws_kinesisfirehose_destinations_alpha as destinations


log_group_destination = logs.LogGroup(self, "LogGroupLambdaAudit",
    log_group_name="auditDestinationForCDK"
)

bucket = s3.Bucket(self, "audit-bucket")
s3_destination = destinations.S3Bucket(bucket)

delivery_stream = kinesisfirehose.DeliveryStream(self, "Delivery Stream",
    destinations=[s3_destination]
)

data_protection_policy = logs.DataProtectionPolicy(
    name="data protection policy",
    description="policy description",
    identifiers=[logs.DataIdentifier.DRIVERSLICENSE_US, logs.DataIdentifier("EmailAddress")],
    log_group_audit_destination=log_group_destination,
    s3_bucket_audit_destination=bucket,
    delivery_stream_name_audit_destination=delivery_stream.delivery_stream_name
)

logs.LogGroup(self, "LogGroupLambda",
    log_group_name="cdkIntegLogGroup",
    data_protection_policy=data_protection_policy
)
```

## Notes

Be aware that Log Group ARNs will always have the string `:*` appended to
them, to match the behavior of [the CloudFormation `AWS::Logs::LogGroup`
resource](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loggroup.html#aws-resource-logs-loggroup-return-values).
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
    Duration as _Duration_4839e8c3,
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    IResource as _IResource_c80c4260,
    ITaggable as _ITaggable_36806126,
    RemovalPolicy as _RemovalPolicy_9f93c814,
    Resource as _Resource_45bc6135,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)
from ..aws_cloudwatch import (
    Metric as _Metric_e396a4dc,
    MetricOptions as _MetricOptions_1788b62f,
    Unit as _Unit_61bc6f70,
)
from ..aws_iam import (
    AddToResourcePolicyResult as _AddToResourcePolicyResult_1d0a53ad,
    Grant as _Grant_a7ae64f8,
    IGrantable as _IGrantable_71c4f5de,
    IResourceWithPolicy as _IResourceWithPolicy_720d64fc,
    IRole as _IRole_235f5d8e,
    PolicyDocument as _PolicyDocument_3ac34393,
    PolicyStatement as _PolicyStatement_0fe33853,
)
from ..aws_kms import IKey as _IKey_5f11635f
from ..aws_s3 import IBucket as _IBucket_42e086fd


@jsii.implements(_IInspectable_c2943556)
class CfnAccountPolicy(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_logs.CfnAccountPolicy",
):
    '''Creates or updates an account-level data protection policy that applies to all log groups in the account.

    A data protection policy can help safeguard sensitive data that's ingested by your log groups by auditing and masking the sensitive log data. Each account can have only one account-level policy.
    .. epigraph::

       Sensitive data is detected and masked when it is ingested into a log group. When you set a data protection policy, log events ingested into the log groups before that time are not masked.

    If you create a data protection policy for your whole account, it applies to both existing log groups and all log groups that are created later in this account. The account policy is applied to existing log groups with eventual consistency. It might take up to 5 minutes before sensitive data in existing log groups begins to be masked.

    By default, when a user views a log event that includes masked data, the sensitive data is replaced by asterisks. A user who has the ``logs:Unmask`` permission can use a `GetLogEvents <https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_GetLogEvents.html>`_ or `FilterLogEvents <https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_FilterLogEvents.html>`_ operation with the ``unmask`` parameter set to ``true`` to view the unmasked log events. Users with the ``logs:Unmask`` can also view unmasked data in the CloudWatch Logs console by running a CloudWatch Logs Insights query with the ``unmask`` query command.

    For more information, including a list of types of data that can be audited and masked, see `Protect sensitive log data with masking <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/mask-sensitive-log-data.html>`_ .

    To create an account-level policy, you must be signed on with the ``logs:PutDataProtectionPolicy`` and ``logs:PutAccountPolicy`` permissions.

    An account-level policy applies to all log groups in the account. You can also create a data protection policy that applies to just one log group. If a log group has its own data protection policy and the account also has an account-level data protection policy, then the two policies are cumulative. Any sensitive term specified in either policy is masked.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-accountpolicy.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_logs as logs
        
        cfn_account_policy = logs.CfnAccountPolicy(self, "MyCfnAccountPolicy",
            policy_document="policyDocument",
            policy_name="policyName",
            policy_type="policyType",
        
            # the properties below are optional
            scope="scope"
        )
    '''

    def __init__(
        self,
        scope_: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        policy_document: builtins.str,
        policy_name: builtins.str,
        policy_type: builtins.str,
        scope: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope_: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param policy_document: Specify the data protection policy, in JSON. This policy must include two JSON blocks: - The first block must include both a ``DataIdentifer`` array and an ``Operation`` property with an ``Audit`` action. The ``DataIdentifer`` array lists the types of sensitive data that you want to mask. For more information about the available options, see `Types of data that you can mask <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/mask-sensitive-log-data-types.html>`_ . The ``Operation`` property with an ``Audit`` action is required to find the sensitive data terms. This ``Audit`` action must contain a ``FindingsDestination`` object. You can optionally use that ``FindingsDestination`` object to list one or more destinations to send audit findings to. If you specify destinations such as log groups, Kinesis Data Firehose streams, and S3 buckets, they must already exist. - The second block must include both a ``DataIdentifer`` array and an ``Operation`` property with an ``Deidentify`` action. The ``DataIdentifer`` array must exactly match the ``DataIdentifer`` array in the first block of the policy. The ``Operation`` property with the ``Deidentify`` action is what actually masks the data, and it must contain the ``"MaskConfig": {}`` object. The ``"MaskConfig": {}`` object must be empty. .. epigraph:: The contents of the two ``DataIdentifer`` arrays must match exactly.
        :param policy_name: A name for the policy. This must be unique within the account.
        :param policy_type: Currently the only valid value for this parameter is ``DATA_PROTECTION_POLICY`` .
        :param scope: Currently the only valid value for this parameter is ``ALL`` , which specifies that the data protection policy applies to all log groups in the account. If you omit this parameter, the default of ``ALL`` is used.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__125a77dd271c26d92d39f5fc5e47e588668423ade67a45afc5817e4df1ee8dd0)
            check_type(argname="argument scope_", value=scope_, expected_type=type_hints["scope_"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAccountPolicyProps(
            policy_document=policy_document,
            policy_name=policy_name,
            policy_type=policy_type,
            scope=scope,
        )

        jsii.create(self.__class__, self, [scope_, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ebfd4fb8cf24056dd4dacb27f135740e6f55ee47d01767451cebf21c25f0837a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9fa52c452e9fe5605a874b3dd89e31ad16dc4f246300b4319af792307b4ae876)
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
        '''The account ID of the account where this policy was created.

        For example, ``123456789012`` .

        :cloudformationAttribute: AccountId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAccountId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="policyDocument")
    def policy_document(self) -> builtins.str:
        '''Specify the data protection policy, in JSON.'''
        return typing.cast(builtins.str, jsii.get(self, "policyDocument"))

    @policy_document.setter
    def policy_document(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c653a261ed47c5ebab7b21521ba00f1e039f43a3aee30163835cda4b9b741be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyDocument", value)

    @builtins.property
    @jsii.member(jsii_name="policyName")
    def policy_name(self) -> builtins.str:
        '''A name for the policy.'''
        return typing.cast(builtins.str, jsii.get(self, "policyName"))

    @policy_name.setter
    def policy_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a3c39fb59cb9806cbee8cf38c347eab7bc33fee8e2148f96faae887592ab14c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyName", value)

    @builtins.property
    @jsii.member(jsii_name="policyType")
    def policy_type(self) -> builtins.str:
        '''Currently the only valid value for this parameter is ``DATA_PROTECTION_POLICY`` .'''
        return typing.cast(builtins.str, jsii.get(self, "policyType"))

    @policy_type.setter
    def policy_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6152ad747f0f8c8124fd42f55dd6679b842c8faa8ef76cc08b3c59d43df9e9c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyType", value)

    @builtins.property
    @jsii.member(jsii_name="scope")
    def scope(self) -> typing.Optional[builtins.str]:
        '''Currently the only valid value for this parameter is ``ALL`` , which specifies that the data protection policy applies to all log groups in the account.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scope"))

    @scope.setter
    def scope(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a2b34c27c4f47efc3559774d8625b4374c145ac113ac7b65b32dbafd795a627)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scope", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.CfnAccountPolicyProps",
    jsii_struct_bases=[],
    name_mapping={
        "policy_document": "policyDocument",
        "policy_name": "policyName",
        "policy_type": "policyType",
        "scope": "scope",
    },
)
class CfnAccountPolicyProps:
    def __init__(
        self,
        *,
        policy_document: builtins.str,
        policy_name: builtins.str,
        policy_type: builtins.str,
        scope: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnAccountPolicy``.

        :param policy_document: Specify the data protection policy, in JSON. This policy must include two JSON blocks: - The first block must include both a ``DataIdentifer`` array and an ``Operation`` property with an ``Audit`` action. The ``DataIdentifer`` array lists the types of sensitive data that you want to mask. For more information about the available options, see `Types of data that you can mask <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/mask-sensitive-log-data-types.html>`_ . The ``Operation`` property with an ``Audit`` action is required to find the sensitive data terms. This ``Audit`` action must contain a ``FindingsDestination`` object. You can optionally use that ``FindingsDestination`` object to list one or more destinations to send audit findings to. If you specify destinations such as log groups, Kinesis Data Firehose streams, and S3 buckets, they must already exist. - The second block must include both a ``DataIdentifer`` array and an ``Operation`` property with an ``Deidentify`` action. The ``DataIdentifer`` array must exactly match the ``DataIdentifer`` array in the first block of the policy. The ``Operation`` property with the ``Deidentify`` action is what actually masks the data, and it must contain the ``"MaskConfig": {}`` object. The ``"MaskConfig": {}`` object must be empty. .. epigraph:: The contents of the two ``DataIdentifer`` arrays must match exactly.
        :param policy_name: A name for the policy. This must be unique within the account.
        :param policy_type: Currently the only valid value for this parameter is ``DATA_PROTECTION_POLICY`` .
        :param scope: Currently the only valid value for this parameter is ``ALL`` , which specifies that the data protection policy applies to all log groups in the account. If you omit this parameter, the default of ``ALL`` is used.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-accountpolicy.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_logs as logs
            
            cfn_account_policy_props = logs.CfnAccountPolicyProps(
                policy_document="policyDocument",
                policy_name="policyName",
                policy_type="policyType",
            
                # the properties below are optional
                scope="scope"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e40dcebab5dfdd5fd816fda98a9c4e710aa8bc28c8bbd574a9451defb6d0d66)
            check_type(argname="argument policy_document", value=policy_document, expected_type=type_hints["policy_document"])
            check_type(argname="argument policy_name", value=policy_name, expected_type=type_hints["policy_name"])
            check_type(argname="argument policy_type", value=policy_type, expected_type=type_hints["policy_type"])
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "policy_document": policy_document,
            "policy_name": policy_name,
            "policy_type": policy_type,
        }
        if scope is not None:
            self._values["scope"] = scope

    @builtins.property
    def policy_document(self) -> builtins.str:
        '''Specify the data protection policy, in JSON.

        This policy must include two JSON blocks:

        - The first block must include both a ``DataIdentifer`` array and an ``Operation`` property with an ``Audit`` action. The ``DataIdentifer`` array lists the types of sensitive data that you want to mask. For more information about the available options, see `Types of data that you can mask <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/mask-sensitive-log-data-types.html>`_ .

        The ``Operation`` property with an ``Audit`` action is required to find the sensitive data terms. This ``Audit`` action must contain a ``FindingsDestination`` object. You can optionally use that ``FindingsDestination`` object to list one or more destinations to send audit findings to. If you specify destinations such as log groups, Kinesis Data Firehose streams, and S3 buckets, they must already exist.

        - The second block must include both a ``DataIdentifer`` array and an ``Operation`` property with an ``Deidentify`` action. The ``DataIdentifer`` array must exactly match the ``DataIdentifer`` array in the first block of the policy.

        The ``Operation`` property with the ``Deidentify`` action is what actually masks the data, and it must contain the ``"MaskConfig": {}`` object. The ``"MaskConfig": {}`` object must be empty.
        .. epigraph::

           The contents of the two ``DataIdentifer`` arrays must match exactly.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-accountpolicy.html#cfn-logs-accountpolicy-policydocument
        '''
        result = self._values.get("policy_document")
        assert result is not None, "Required property 'policy_document' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def policy_name(self) -> builtins.str:
        '''A name for the policy.

        This must be unique within the account.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-accountpolicy.html#cfn-logs-accountpolicy-policyname
        '''
        result = self._values.get("policy_name")
        assert result is not None, "Required property 'policy_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def policy_type(self) -> builtins.str:
        '''Currently the only valid value for this parameter is ``DATA_PROTECTION_POLICY`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-accountpolicy.html#cfn-logs-accountpolicy-policytype
        '''
        result = self._values.get("policy_type")
        assert result is not None, "Required property 'policy_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def scope(self) -> typing.Optional[builtins.str]:
        '''Currently the only valid value for this parameter is ``ALL`` , which specifies that the data protection policy applies to all log groups in the account.

        If you omit this parameter, the default of ``ALL`` is used.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-accountpolicy.html#cfn-logs-accountpolicy-scope
        '''
        result = self._values.get("scope")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAccountPolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnDestination(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_logs.CfnDestination",
):
    '''The AWS::Logs::Destination resource specifies a CloudWatch Logs destination.

    A destination encapsulates a physical resource (such as an Amazon Kinesis data stream) and enables you to subscribe that resource to a stream of log events.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-destination.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_logs as logs
        
        cfn_destination = logs.CfnDestination(self, "MyCfnDestination",
            destination_name="destinationName",
            role_arn="roleArn",
            target_arn="targetArn",
        
            # the properties below are optional
            destination_policy="destinationPolicy"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        destination_name: builtins.str,
        role_arn: builtins.str,
        target_arn: builtins.str,
        destination_policy: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param destination_name: The name of the destination.
        :param role_arn: The ARN of an IAM role that permits CloudWatch Logs to send data to the specified AWS resource.
        :param target_arn: The Amazon Resource Name (ARN) of the physical target where the log events are delivered (for example, a Kinesis stream).
        :param destination_policy: An IAM policy document that governs which AWS accounts can create subscription filters against this destination.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44e37c6c2772abdacfbcd01df5c5418fca8937b435df3890a5a5cb3437b9bab5)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDestinationProps(
            destination_name=destination_name,
            role_arn=role_arn,
            target_arn=target_arn,
            destination_policy=destination_policy,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96cb24255178be4bad07466bab77f2ccec3a7bf2f35acfe8bf018152eb28bb7e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0f9dedbbaf433f224026d220b3fb36706410370925367aeada047e8858f484ac)
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
        '''The ARN of the CloudWatch Logs destination, such as ``arn:aws:logs:us-west-1:123456789012:destination:MyDestination`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="destinationName")
    def destination_name(self) -> builtins.str:
        '''The name of the destination.'''
        return typing.cast(builtins.str, jsii.get(self, "destinationName"))

    @destination_name.setter
    def destination_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5158605e72fe974296ad671ff50605f46d8a94d78d818e766756296254fa5758)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationName", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''The ARN of an IAM role that permits CloudWatch Logs to send data to the specified AWS resource.'''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__908d4772c2472f7ef1a59ee7f794734117f87a8908ceda3def1feff5578217c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="targetArn")
    def target_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the physical target where the log events are delivered (for example, a Kinesis stream).'''
        return typing.cast(builtins.str, jsii.get(self, "targetArn"))

    @target_arn.setter
    def target_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90e291c0d065725c0ff62d5808258937a46aa7e3d79209721b2ffdb32fc0db6b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetArn", value)

    @builtins.property
    @jsii.member(jsii_name="destinationPolicy")
    def destination_policy(self) -> typing.Optional[builtins.str]:
        '''An IAM policy document that governs which AWS accounts can create subscription filters against this destination.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationPolicy"))

    @destination_policy.setter
    def destination_policy(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b0569830af0faea41307b4fd071b0ef86a0b49f3514f3050bfa53cc72d3ddee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationPolicy", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.CfnDestinationProps",
    jsii_struct_bases=[],
    name_mapping={
        "destination_name": "destinationName",
        "role_arn": "roleArn",
        "target_arn": "targetArn",
        "destination_policy": "destinationPolicy",
    },
)
class CfnDestinationProps:
    def __init__(
        self,
        *,
        destination_name: builtins.str,
        role_arn: builtins.str,
        target_arn: builtins.str,
        destination_policy: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnDestination``.

        :param destination_name: The name of the destination.
        :param role_arn: The ARN of an IAM role that permits CloudWatch Logs to send data to the specified AWS resource.
        :param target_arn: The Amazon Resource Name (ARN) of the physical target where the log events are delivered (for example, a Kinesis stream).
        :param destination_policy: An IAM policy document that governs which AWS accounts can create subscription filters against this destination.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-destination.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_logs as logs
            
            cfn_destination_props = logs.CfnDestinationProps(
                destination_name="destinationName",
                role_arn="roleArn",
                target_arn="targetArn",
            
                # the properties below are optional
                destination_policy="destinationPolicy"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__faf2f9f88fd096e79a2445aab3efdc3a85509df7ba06ffc305c9faf39fa77a56)
            check_type(argname="argument destination_name", value=destination_name, expected_type=type_hints["destination_name"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument target_arn", value=target_arn, expected_type=type_hints["target_arn"])
            check_type(argname="argument destination_policy", value=destination_policy, expected_type=type_hints["destination_policy"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "destination_name": destination_name,
            "role_arn": role_arn,
            "target_arn": target_arn,
        }
        if destination_policy is not None:
            self._values["destination_policy"] = destination_policy

    @builtins.property
    def destination_name(self) -> builtins.str:
        '''The name of the destination.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-destination.html#cfn-logs-destination-destinationname
        '''
        result = self._values.get("destination_name")
        assert result is not None, "Required property 'destination_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''The ARN of an IAM role that permits CloudWatch Logs to send data to the specified AWS resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-destination.html#cfn-logs-destination-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the physical target where the log events are delivered (for example, a Kinesis stream).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-destination.html#cfn-logs-destination-targetarn
        '''
        result = self._values.get("target_arn")
        assert result is not None, "Required property 'target_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def destination_policy(self) -> typing.Optional[builtins.str]:
        '''An IAM policy document that governs which AWS accounts can create subscription filters against this destination.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-destination.html#cfn-logs-destination-destinationpolicy
        '''
        result = self._values.get("destination_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDestinationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnLogGroup(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_logs.CfnLogGroup",
):
    '''The ``AWS::Logs::LogGroup`` resource specifies a log group.

    A log group defines common properties for log streams, such as their retention and access control rules. Each log stream must belong to one log group.

    You can create up to 1,000,000 log groups per Region per account. You must use the following guidelines when naming a log group:

    - Log group names must be unique within a Region for an AWS account.
    - Log group names can be between 1 and 512 characters long.
    - Log group names consist of the following characters: a-z, A-Z, 0-9, '_' (underscore), '-' (hyphen), '/' (forward slash), and '.' (period).

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loggroup.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_logs as logs
        
        # data_protection_policy: Any
        
        cfn_log_group = logs.CfnLogGroup(self, "MyCfnLogGroup",
            data_protection_policy=data_protection_policy,
            kms_key_id="kmsKeyId",
            log_group_name="logGroupName",
            retention_in_days=123,
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
        data_protection_policy: typing.Any = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        log_group_name: typing.Optional[builtins.str] = None,
        retention_in_days: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param data_protection_policy: Creates a data protection policy and assigns it to the log group. A data protection policy can help safeguard sensitive data that's ingested by the log group by auditing and masking the sensitive log data. When a user who does not have permission to view masked data views a log event that includes masked data, the sensitive data is replaced by asterisks. For more information, including a list of types of data that can be audited and masked, see `Protect sensitive log data with masking <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/mask-sensitive-log-data.html>`_ .
        :param kms_key_id: The Amazon Resource Name (ARN) of the AWS KMS key to use when encrypting log data. To associate an AWS KMS key with the log group, specify the ARN of that KMS key here. If you do so, ingested data is encrypted using this key. This association is stored as long as the data encrypted with the KMS key is still within CloudWatch Logs . This enables CloudWatch Logs to decrypt this data whenever it is requested. If you attempt to associate a KMS key with the log group but the KMS key doesn't exist or is deactivated, you will receive an ``InvalidParameterException`` error. Log group data is always encrypted in CloudWatch Logs . If you omit this key, the encryption does not use AWS KMS . For more information, see `Encrypt log data in CloudWatch Logs using AWS Key Management Service <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/encrypt-log-data-kms.html>`_
        :param log_group_name: The name of the log group. If you don't specify a name, AWS CloudFormation generates a unique ID for the log group.
        :param retention_in_days: The number of days to retain the log events in the specified log group. Possible values are: 1, 3, 5, 7, 14, 30, 60, 90, 120, 150, 180, 365, 400, 545, 731, 1096, 1827, 2192, 2557, 2922, 3288, and 3653. To set a log group so that its log events do not expire, use `DeleteRetentionPolicy <https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DeleteRetentionPolicy.html>`_ .
        :param tags: An array of key-value pairs to apply to the log group. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e283e76ec168d67513d106f9413697672f161b29f03fa9b13486e96b13319c0)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnLogGroupProps(
            data_protection_policy=data_protection_policy,
            kms_key_id=kms_key_id,
            log_group_name=log_group_name,
            retention_in_days=retention_in_days,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c5bac0ef7ae74529e652cc24b33213b3432954607a3665dd72bd69b68490c7c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__167d66406821a4fe8a6ca05ec99424e7c4abd7946ba6eb30ee37e04443759ddc)
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
        '''The ARN of the log group, such as ``arn:aws:logs:us-west-1:123456789012:log-group:/mystack-testgroup-12ABC1AB12A1:*``.

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
    @jsii.member(jsii_name="dataProtectionPolicy")
    def data_protection_policy(self) -> typing.Any:
        '''Creates a data protection policy and assigns it to the log group.'''
        return typing.cast(typing.Any, jsii.get(self, "dataProtectionPolicy"))

    @data_protection_policy.setter
    def data_protection_policy(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__427539e290b46019fba84ec8aa72f953c2d26dfe978de85330819964c3cea37e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataProtectionPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the AWS KMS key to use when encrypting log data.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0fc22b518f14684135ca2ffa0556628df055b32df3a769085c35ae8ef72d5677)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="logGroupName")
    def log_group_name(self) -> typing.Optional[builtins.str]:
        '''The name of the log group.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logGroupName"))

    @log_group_name.setter
    def log_group_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08bea1f6b59cbce316d19aa0ff5db07ed0da20b04cc322eb41788ce24f8f2d31)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="retentionInDays")
    def retention_in_days(self) -> typing.Optional[jsii.Number]:
        '''The number of days to retain the log events in the specified log group.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retentionInDays"))

    @retention_in_days.setter
    def retention_in_days(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d977a18b9031aeb9d37e4baf6f3eccb9ebf070ad2e33a30cfba9f69fbaf62408)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retentionInDays", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to the log group.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ea9a0a37724d334e68ee325d75e901df12c6765b4c229366a1cef4038c07187)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.CfnLogGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "data_protection_policy": "dataProtectionPolicy",
        "kms_key_id": "kmsKeyId",
        "log_group_name": "logGroupName",
        "retention_in_days": "retentionInDays",
        "tags": "tags",
    },
)
class CfnLogGroupProps:
    def __init__(
        self,
        *,
        data_protection_policy: typing.Any = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        log_group_name: typing.Optional[builtins.str] = None,
        retention_in_days: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnLogGroup``.

        :param data_protection_policy: Creates a data protection policy and assigns it to the log group. A data protection policy can help safeguard sensitive data that's ingested by the log group by auditing and masking the sensitive log data. When a user who does not have permission to view masked data views a log event that includes masked data, the sensitive data is replaced by asterisks. For more information, including a list of types of data that can be audited and masked, see `Protect sensitive log data with masking <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/mask-sensitive-log-data.html>`_ .
        :param kms_key_id: The Amazon Resource Name (ARN) of the AWS KMS key to use when encrypting log data. To associate an AWS KMS key with the log group, specify the ARN of that KMS key here. If you do so, ingested data is encrypted using this key. This association is stored as long as the data encrypted with the KMS key is still within CloudWatch Logs . This enables CloudWatch Logs to decrypt this data whenever it is requested. If you attempt to associate a KMS key with the log group but the KMS key doesn't exist or is deactivated, you will receive an ``InvalidParameterException`` error. Log group data is always encrypted in CloudWatch Logs . If you omit this key, the encryption does not use AWS KMS . For more information, see `Encrypt log data in CloudWatch Logs using AWS Key Management Service <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/encrypt-log-data-kms.html>`_
        :param log_group_name: The name of the log group. If you don't specify a name, AWS CloudFormation generates a unique ID for the log group.
        :param retention_in_days: The number of days to retain the log events in the specified log group. Possible values are: 1, 3, 5, 7, 14, 30, 60, 90, 120, 150, 180, 365, 400, 545, 731, 1096, 1827, 2192, 2557, 2922, 3288, and 3653. To set a log group so that its log events do not expire, use `DeleteRetentionPolicy <https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DeleteRetentionPolicy.html>`_ .
        :param tags: An array of key-value pairs to apply to the log group. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loggroup.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_logs as logs
            
            # data_protection_policy: Any
            
            cfn_log_group_props = logs.CfnLogGroupProps(
                data_protection_policy=data_protection_policy,
                kms_key_id="kmsKeyId",
                log_group_name="logGroupName",
                retention_in_days=123,
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a2ba122502a64b05bea3e56f15389c84f127761b660b1d06de3ea638b95f816)
            check_type(argname="argument data_protection_policy", value=data_protection_policy, expected_type=type_hints["data_protection_policy"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            check_type(argname="argument log_group_name", value=log_group_name, expected_type=type_hints["log_group_name"])
            check_type(argname="argument retention_in_days", value=retention_in_days, expected_type=type_hints["retention_in_days"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if data_protection_policy is not None:
            self._values["data_protection_policy"] = data_protection_policy
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if log_group_name is not None:
            self._values["log_group_name"] = log_group_name
        if retention_in_days is not None:
            self._values["retention_in_days"] = retention_in_days
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def data_protection_policy(self) -> typing.Any:
        '''Creates a data protection policy and assigns it to the log group.

        A data protection policy can help safeguard sensitive data that's ingested by the log group by auditing and masking the sensitive log data. When a user who does not have permission to view masked data views a log event that includes masked data, the sensitive data is replaced by asterisks.

        For more information, including a list of types of data that can be audited and masked, see `Protect sensitive log data with masking <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/mask-sensitive-log-data.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loggroup.html#cfn-logs-loggroup-dataprotectionpolicy
        '''
        result = self._values.get("data_protection_policy")
        return typing.cast(typing.Any, result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the AWS KMS key to use when encrypting log data.

        To associate an AWS KMS key with the log group, specify the ARN of that KMS key here. If you do so, ingested data is encrypted using this key. This association is stored as long as the data encrypted with the KMS key is still within CloudWatch Logs . This enables CloudWatch Logs to decrypt this data whenever it is requested.

        If you attempt to associate a KMS key with the log group but the KMS key doesn't exist or is deactivated, you will receive an ``InvalidParameterException`` error.

        Log group data is always encrypted in CloudWatch Logs . If you omit this key, the encryption does not use AWS KMS . For more information, see `Encrypt log data in CloudWatch Logs using AWS Key Management Service <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/encrypt-log-data-kms.html>`_

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loggroup.html#cfn-logs-loggroup-kmskeyid
        '''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_group_name(self) -> typing.Optional[builtins.str]:
        '''The name of the log group.

        If you don't specify a name, AWS CloudFormation generates a unique ID for the log group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loggroup.html#cfn-logs-loggroup-loggroupname
        '''
        result = self._values.get("log_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def retention_in_days(self) -> typing.Optional[jsii.Number]:
        '''The number of days to retain the log events in the specified log group.

        Possible values are: 1, 3, 5, 7, 14, 30, 60, 90, 120, 150, 180, 365, 400, 545, 731, 1096, 1827, 2192, 2557, 2922, 3288, and 3653.

        To set a log group so that its log events do not expire, use `DeleteRetentionPolicy <https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DeleteRetentionPolicy.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loggroup.html#cfn-logs-loggroup-retentionindays
        '''
        result = self._values.get("retention_in_days")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to the log group.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loggroup.html#cfn-logs-loggroup-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLogGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnLogStream(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_logs.CfnLogStream",
):
    '''The ``AWS::Logs::LogStream`` resource specifies an Amazon CloudWatch Logs log stream in a specific log group.

    A log stream represents the sequence of events coming from an application instance or resource that you are monitoring.

    There is no limit on the number of log streams that you can create for a log group.

    You must use the following guidelines when naming a log stream:

    - Log stream names must be unique within the log group.
    - Log stream names can be between 1 and 512 characters long.
    - The ':' (colon) and '*' (asterisk) characters are not allowed.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-logstream.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_logs as logs
        
        cfn_log_stream = logs.CfnLogStream(self, "MyCfnLogStream",
            log_group_name="logGroupName",
        
            # the properties below are optional
            log_stream_name="logStreamName"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        log_group_name: builtins.str,
        log_stream_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param log_group_name: The name of the log group where the log stream is created.
        :param log_stream_name: The name of the log stream. The name must be unique within the log group.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68392ef44019b9b5ee681acb5bd13c481e1cc999bc1f1773e84c70b5a04190b7)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnLogStreamProps(
            log_group_name=log_group_name, log_stream_name=log_stream_name
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64fb9d8e354f9197a9998608e06c1be2deb6b929ddb7835470385c91e16d110a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2ec4cadc779471f71fa1f1b77d2bda5c706e530b0ead1517f46ec34940fee5da)
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
    @jsii.member(jsii_name="logGroupName")
    def log_group_name(self) -> builtins.str:
        '''The name of the log group where the log stream is created.'''
        return typing.cast(builtins.str, jsii.get(self, "logGroupName"))

    @log_group_name.setter
    def log_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28f49c7b712326ca2be5a290a29a4430589b6c15c4da1f34afb773fcc0456112)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="logStreamName")
    def log_stream_name(self) -> typing.Optional[builtins.str]:
        '''The name of the log stream.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logStreamName"))

    @log_stream_name.setter
    def log_stream_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e3f8ff96c3dac6c45a8d31d07a3223b27eebb1e1c6aa1676d6cf0cfc0bcacb8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logStreamName", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.CfnLogStreamProps",
    jsii_struct_bases=[],
    name_mapping={
        "log_group_name": "logGroupName",
        "log_stream_name": "logStreamName",
    },
)
class CfnLogStreamProps:
    def __init__(
        self,
        *,
        log_group_name: builtins.str,
        log_stream_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnLogStream``.

        :param log_group_name: The name of the log group where the log stream is created.
        :param log_stream_name: The name of the log stream. The name must be unique within the log group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-logstream.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_logs as logs
            
            cfn_log_stream_props = logs.CfnLogStreamProps(
                log_group_name="logGroupName",
            
                # the properties below are optional
                log_stream_name="logStreamName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab2d708d8a8c684eb8753554b20ecf7de790ffc112520d594cacb903aff379ea)
            check_type(argname="argument log_group_name", value=log_group_name, expected_type=type_hints["log_group_name"])
            check_type(argname="argument log_stream_name", value=log_stream_name, expected_type=type_hints["log_stream_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "log_group_name": log_group_name,
        }
        if log_stream_name is not None:
            self._values["log_stream_name"] = log_stream_name

    @builtins.property
    def log_group_name(self) -> builtins.str:
        '''The name of the log group where the log stream is created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-logstream.html#cfn-logs-logstream-loggroupname
        '''
        result = self._values.get("log_group_name")
        assert result is not None, "Required property 'log_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def log_stream_name(self) -> typing.Optional[builtins.str]:
        '''The name of the log stream.

        The name must be unique within the log group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-logstream.html#cfn-logs-logstream-logstreamname
        '''
        result = self._values.get("log_stream_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLogStreamProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnMetricFilter(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_logs.CfnMetricFilter",
):
    '''The ``AWS::Logs::MetricFilter`` resource specifies a metric filter that describes how CloudWatch Logs extracts information from logs and transforms it into Amazon CloudWatch metrics.

    If you have multiple metric filters that are associated with a log group, all the filters are applied to the log streams in that group.

    The maximum number of metric filters that can be associated with a log group is 100.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-metricfilter.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_logs as logs
        
        cfn_metric_filter = logs.CfnMetricFilter(self, "MyCfnMetricFilter",
            filter_pattern="filterPattern",
            log_group_name="logGroupName",
            metric_transformations=[logs.CfnMetricFilter.MetricTransformationProperty(
                metric_name="metricName",
                metric_namespace="metricNamespace",
                metric_value="metricValue",
        
                # the properties below are optional
                default_value=123,
                dimensions=[logs.CfnMetricFilter.DimensionProperty(
                    key="key",
                    value="value"
                )],
                unit="unit"
            )],
        
            # the properties below are optional
            filter_name="filterName"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        filter_pattern: builtins.str,
        log_group_name: builtins.str,
        metric_transformations: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMetricFilter.MetricTransformationProperty", typing.Dict[builtins.str, typing.Any]]]]],
        filter_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param filter_pattern: A filter pattern for extracting metric data out of ingested log events. For more information, see `Filter and Pattern Syntax <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html>`_ .
        :param log_group_name: The name of an existing log group that you want to associate with this metric filter.
        :param metric_transformations: The metric transformations.
        :param filter_name: The name of the metric filter.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aaa6a2018a5f10ec1a79f547b81a628d6f434d037b49c5975131bba2d6fd2786)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnMetricFilterProps(
            filter_pattern=filter_pattern,
            log_group_name=log_group_name,
            metric_transformations=metric_transformations,
            filter_name=filter_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa5f65c3d38181c3265e71ca5f37737480594a08405697ef96fc18254e2a9899)
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
            type_hints = typing.get_type_hints(_typecheckingstub__aed2b5842b90369a626b9acdfbfb87dab07b9debcde1b1964b8b0dabb330ea2e)
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
    @jsii.member(jsii_name="filterPattern")
    def filter_pattern(self) -> builtins.str:
        '''A filter pattern for extracting metric data out of ingested log events.'''
        return typing.cast(builtins.str, jsii.get(self, "filterPattern"))

    @filter_pattern.setter
    def filter_pattern(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9fdc6521987ce3f017024e20e1e0fb59a35415aa424ed169b346a59793c88b73)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filterPattern", value)

    @builtins.property
    @jsii.member(jsii_name="logGroupName")
    def log_group_name(self) -> builtins.str:
        '''The name of an existing log group that you want to associate with this metric filter.'''
        return typing.cast(builtins.str, jsii.get(self, "logGroupName"))

    @log_group_name.setter
    def log_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae16ea786b9d9ed9d5bfe824932074163b1aa6379bed22eb2671f3ed0818bf26)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="metricTransformations")
    def metric_transformations(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnMetricFilter.MetricTransformationProperty"]]]:
        '''The metric transformations.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnMetricFilter.MetricTransformationProperty"]]], jsii.get(self, "metricTransformations"))

    @metric_transformations.setter
    def metric_transformations(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnMetricFilter.MetricTransformationProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e42e8a9e143351ba28d452f886abff3c46adff74b2c2fc8876dc18aabf51dcba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricTransformations", value)

    @builtins.property
    @jsii.member(jsii_name="filterName")
    def filter_name(self) -> typing.Optional[builtins.str]:
        '''The name of the metric filter.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "filterName"))

    @filter_name.setter
    def filter_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed6515d6733ea675274296cf9952fb0b41bd1778277ae74bde9739d81a205382)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filterName", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_logs.CfnMetricFilter.DimensionProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class DimensionProperty:
        def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
            '''Specifies the CloudWatch metric dimensions to publish with this metric.

            Because dimensions are part of the unique identifier for a metric, whenever a unique dimension name/value pair is extracted from your logs, you are creating a new variation of that metric.

            For more information about publishing dimensions with metrics created by metric filters, see `Publishing dimensions with metrics from values in JSON or space-delimited log events <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html#logs-metric-filters-dimensions>`_ .
            .. epigraph::

               Metrics extracted from log events are charged as custom metrics. To prevent unexpected high charges, do not specify high-cardinality fields such as ``IPAddress`` or ``requestID`` as dimensions. Each different value found for a dimension is treated as a separate metric and accrues charges as a separate custom metric.

               To help prevent accidental high charges, Amazon disables a metric filter if it generates 1000 different name/value pairs for the dimensions that you have specified within a certain amount of time.

               You can also set up a billing alarm to alert you if your charges are higher than expected. For more information, see `Creating a Billing Alarm to Monitor Your Estimated AWS Charges <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/monitor_estimated_charges_with_cloudwatch.html>`_ .

            :param key: The name for the CloudWatch metric dimension that the metric filter creates. Dimension names must contain only ASCII characters, must include at least one non-whitespace character, and cannot start with a colon (:).
            :param value: The log event field that will contain the value for this dimension. This dimension will only be published for a metric if the value is found in the log event. For example, ``$.eventType`` for JSON log events, or ``$server`` for space-delimited log events.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-metricfilter-dimension.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_logs as logs
                
                dimension_property = logs.CfnMetricFilter.DimensionProperty(
                    key="key",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9fad5f3c7dec2c3bafa74c42e2398a046d9cc8c861abfac39c6e9e77c2b65b41)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "key": key,
                "value": value,
            }

        @builtins.property
        def key(self) -> builtins.str:
            '''The name for the CloudWatch metric dimension that the metric filter creates.

            Dimension names must contain only ASCII characters, must include at least one non-whitespace character, and cannot start with a colon (:).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-metricfilter-dimension.html#cfn-logs-metricfilter-dimension-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''The log event field that will contain the value for this dimension.

            This dimension will only be published for a metric if the value is found in the log event. For example, ``$.eventType`` for JSON log events, or ``$server`` for space-delimited log events.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-metricfilter-dimension.html#cfn-logs-metricfilter-dimension-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DimensionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_logs.CfnMetricFilter.MetricTransformationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "metric_name": "metricName",
            "metric_namespace": "metricNamespace",
            "metric_value": "metricValue",
            "default_value": "defaultValue",
            "dimensions": "dimensions",
            "unit": "unit",
        },
    )
    class MetricTransformationProperty:
        def __init__(
            self,
            *,
            metric_name: builtins.str,
            metric_namespace: builtins.str,
            metric_value: builtins.str,
            default_value: typing.Optional[jsii.Number] = None,
            dimensions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMetricFilter.DimensionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            unit: typing.Optional[builtins.str] = None,
        ) -> None:
            '''``MetricTransformation`` is a property of the ``AWS::Logs::MetricFilter`` resource that describes how to transform log streams into a CloudWatch metric.

            :param metric_name: The name of the CloudWatch metric.
            :param metric_namespace: A custom namespace to contain your metric in CloudWatch. Use namespaces to group together metrics that are similar. For more information, see `Namespaces <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Namespace>`_ .
            :param metric_value: The value that is published to the CloudWatch metric. For example, if you're counting the occurrences of a particular term like ``Error`` , specify 1 for the metric value. If you're counting the number of bytes transferred, reference the value that is in the log event by using $. followed by the name of the field that you specified in the filter pattern, such as ``$.size`` .
            :param default_value: (Optional) The value to emit when a filter pattern does not match a log event. This value can be null.
            :param dimensions: The fields to use as dimensions for the metric. One metric filter can include as many as three dimensions. .. epigraph:: Metrics extracted from log events are charged as custom metrics. To prevent unexpected high charges, do not specify high-cardinality fields such as ``IPAddress`` or ``requestID`` as dimensions. Each different value found for a dimension is treated as a separate metric and accrues charges as a separate custom metric. CloudWatch Logs disables a metric filter if it generates 1000 different name/value pairs for your specified dimensions within a certain amount of time. This helps to prevent accidental high charges. You can also set up a billing alarm to alert you if your charges are higher than expected. For more information, see `Creating a Billing Alarm to Monitor Your Estimated AWS Charges <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/monitor_estimated_charges_with_cloudwatch.html>`_ .
            :param unit: The unit to assign to the metric. If you omit this, the unit is set as ``None`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-metricfilter-metrictransformation.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_logs as logs
                
                metric_transformation_property = logs.CfnMetricFilter.MetricTransformationProperty(
                    metric_name="metricName",
                    metric_namespace="metricNamespace",
                    metric_value="metricValue",
                
                    # the properties below are optional
                    default_value=123,
                    dimensions=[logs.CfnMetricFilter.DimensionProperty(
                        key="key",
                        value="value"
                    )],
                    unit="unit"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8989e36bc84de1e18d069af1bb22845cf409685cbd8a8fe22cd131474e0d7958)
                check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
                check_type(argname="argument metric_namespace", value=metric_namespace, expected_type=type_hints["metric_namespace"])
                check_type(argname="argument metric_value", value=metric_value, expected_type=type_hints["metric_value"])
                check_type(argname="argument default_value", value=default_value, expected_type=type_hints["default_value"])
                check_type(argname="argument dimensions", value=dimensions, expected_type=type_hints["dimensions"])
                check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "metric_name": metric_name,
                "metric_namespace": metric_namespace,
                "metric_value": metric_value,
            }
            if default_value is not None:
                self._values["default_value"] = default_value
            if dimensions is not None:
                self._values["dimensions"] = dimensions
            if unit is not None:
                self._values["unit"] = unit

        @builtins.property
        def metric_name(self) -> builtins.str:
            '''The name of the CloudWatch metric.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-metricfilter-metrictransformation.html#cfn-logs-metricfilter-metrictransformation-metricname
            '''
            result = self._values.get("metric_name")
            assert result is not None, "Required property 'metric_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def metric_namespace(self) -> builtins.str:
            '''A custom namespace to contain your metric in CloudWatch.

            Use namespaces to group together metrics that are similar. For more information, see `Namespaces <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Namespace>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-metricfilter-metrictransformation.html#cfn-logs-metricfilter-metrictransformation-metricnamespace
            '''
            result = self._values.get("metric_namespace")
            assert result is not None, "Required property 'metric_namespace' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def metric_value(self) -> builtins.str:
            '''The value that is published to the CloudWatch metric.

            For example, if you're counting the occurrences of a particular term like ``Error`` , specify 1 for the metric value. If you're counting the number of bytes transferred, reference the value that is in the log event by using $. followed by the name of the field that you specified in the filter pattern, such as ``$.size`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-metricfilter-metrictransformation.html#cfn-logs-metricfilter-metrictransformation-metricvalue
            '''
            result = self._values.get("metric_value")
            assert result is not None, "Required property 'metric_value' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def default_value(self) -> typing.Optional[jsii.Number]:
            '''(Optional) The value to emit when a filter pattern does not match a log event.

            This value can be null.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-metricfilter-metrictransformation.html#cfn-logs-metricfilter-metrictransformation-defaultvalue
            '''
            result = self._values.get("default_value")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def dimensions(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnMetricFilter.DimensionProperty"]]]]:
            '''The fields to use as dimensions for the metric. One metric filter can include as many as three dimensions.

            .. epigraph::

               Metrics extracted from log events are charged as custom metrics. To prevent unexpected high charges, do not specify high-cardinality fields such as ``IPAddress`` or ``requestID`` as dimensions. Each different value found for a dimension is treated as a separate metric and accrues charges as a separate custom metric.

               CloudWatch Logs disables a metric filter if it generates 1000 different name/value pairs for your specified dimensions within a certain amount of time. This helps to prevent accidental high charges.

               You can also set up a billing alarm to alert you if your charges are higher than expected. For more information, see `Creating a Billing Alarm to Monitor Your Estimated AWS Charges <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/monitor_estimated_charges_with_cloudwatch.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-metricfilter-metrictransformation.html#cfn-logs-metricfilter-metrictransformation-dimensions
            '''
            result = self._values.get("dimensions")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnMetricFilter.DimensionProperty"]]]], result)

        @builtins.property
        def unit(self) -> typing.Optional[builtins.str]:
            '''The unit to assign to the metric.

            If you omit this, the unit is set as ``None`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-metricfilter-metrictransformation.html#cfn-logs-metricfilter-metrictransformation-unit
            '''
            result = self._values.get("unit")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MetricTransformationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.CfnMetricFilterProps",
    jsii_struct_bases=[],
    name_mapping={
        "filter_pattern": "filterPattern",
        "log_group_name": "logGroupName",
        "metric_transformations": "metricTransformations",
        "filter_name": "filterName",
    },
)
class CfnMetricFilterProps:
    def __init__(
        self,
        *,
        filter_pattern: builtins.str,
        log_group_name: builtins.str,
        metric_transformations: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMetricFilter.MetricTransformationProperty, typing.Dict[builtins.str, typing.Any]]]]],
        filter_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnMetricFilter``.

        :param filter_pattern: A filter pattern for extracting metric data out of ingested log events. For more information, see `Filter and Pattern Syntax <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html>`_ .
        :param log_group_name: The name of an existing log group that you want to associate with this metric filter.
        :param metric_transformations: The metric transformations.
        :param filter_name: The name of the metric filter.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-metricfilter.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_logs as logs
            
            cfn_metric_filter_props = logs.CfnMetricFilterProps(
                filter_pattern="filterPattern",
                log_group_name="logGroupName",
                metric_transformations=[logs.CfnMetricFilter.MetricTransformationProperty(
                    metric_name="metricName",
                    metric_namespace="metricNamespace",
                    metric_value="metricValue",
            
                    # the properties below are optional
                    default_value=123,
                    dimensions=[logs.CfnMetricFilter.DimensionProperty(
                        key="key",
                        value="value"
                    )],
                    unit="unit"
                )],
            
                # the properties below are optional
                filter_name="filterName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__524e2e94ad4843f66081953f516426a1396490f271842ac0c5ca7c7ecb84011e)
            check_type(argname="argument filter_pattern", value=filter_pattern, expected_type=type_hints["filter_pattern"])
            check_type(argname="argument log_group_name", value=log_group_name, expected_type=type_hints["log_group_name"])
            check_type(argname="argument metric_transformations", value=metric_transformations, expected_type=type_hints["metric_transformations"])
            check_type(argname="argument filter_name", value=filter_name, expected_type=type_hints["filter_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "filter_pattern": filter_pattern,
            "log_group_name": log_group_name,
            "metric_transformations": metric_transformations,
        }
        if filter_name is not None:
            self._values["filter_name"] = filter_name

    @builtins.property
    def filter_pattern(self) -> builtins.str:
        '''A filter pattern for extracting metric data out of ingested log events.

        For more information, see `Filter and Pattern Syntax <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-metricfilter.html#cfn-logs-metricfilter-filterpattern
        '''
        result = self._values.get("filter_pattern")
        assert result is not None, "Required property 'filter_pattern' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def log_group_name(self) -> builtins.str:
        '''The name of an existing log group that you want to associate with this metric filter.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-metricfilter.html#cfn-logs-metricfilter-loggroupname
        '''
        result = self._values.get("log_group_name")
        assert result is not None, "Required property 'log_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def metric_transformations(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnMetricFilter.MetricTransformationProperty]]]:
        '''The metric transformations.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-metricfilter.html#cfn-logs-metricfilter-metrictransformations
        '''
        result = self._values.get("metric_transformations")
        assert result is not None, "Required property 'metric_transformations' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnMetricFilter.MetricTransformationProperty]]], result)

    @builtins.property
    def filter_name(self) -> typing.Optional[builtins.str]:
        '''The name of the metric filter.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-metricfilter.html#cfn-logs-metricfilter-filtername
        '''
        result = self._values.get("filter_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMetricFilterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnQueryDefinition(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_logs.CfnQueryDefinition",
):
    '''Creates a query definition for CloudWatch Logs Insights.

    For more information, see `Analyzing Log Data with CloudWatch Logs Insights <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-querydefinition.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_logs as logs
        
        cfn_query_definition = logs.CfnQueryDefinition(self, "MyCfnQueryDefinition",
            name="name",
            query_string="queryString",
        
            # the properties below are optional
            log_group_names=["logGroupNames"]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        query_string: builtins.str,
        log_group_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: A name for the query definition.
        :param query_string: The query string to use for this query definition. For more information, see `CloudWatch Logs Insights Query Syntax <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax.html>`_ .
        :param log_group_names: Use this parameter if you want the query to query only certain log groups.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d10075ae036bdf9f4049570cf68ab72c79ee717f007f45628b52d2ea5aa64ae)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnQueryDefinitionProps(
            name=name, query_string=query_string, log_group_names=log_group_names
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1dd626642ab8510fa9005787d00adbbd508a543616e89979ad57ba0be9f38bad)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d445c0915cb40f09b489a0802b2b2b0c035e244acf419b2452990fd8568900fe)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrQueryDefinitionId")
    def attr_query_definition_id(self) -> builtins.str:
        '''The ID of the query definition.

        :cloudformationAttribute: QueryDefinitionId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrQueryDefinitionId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''A name for the query definition.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a970de5992ab8622f5a1c04c70c2066cfaee94719e9aba8c8edbe863ddcce298)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="queryString")
    def query_string(self) -> builtins.str:
        '''The query string to use for this query definition.'''
        return typing.cast(builtins.str, jsii.get(self, "queryString"))

    @query_string.setter
    def query_string(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__005c13f188808f7829e17c5ce9ca7e9ae473e50b0b0b1ed4f95b8e35cfd6a6df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryString", value)

    @builtins.property
    @jsii.member(jsii_name="logGroupNames")
    def log_group_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Use this parameter if you want the query to query only certain log groups.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "logGroupNames"))

    @log_group_names.setter
    def log_group_names(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1d922394643a9758400b7e596dd6c6fe61ab7e1fb96d4a93a7061d0e3b5c39d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logGroupNames", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.CfnQueryDefinitionProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "query_string": "queryString",
        "log_group_names": "logGroupNames",
    },
)
class CfnQueryDefinitionProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        query_string: builtins.str,
        log_group_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnQueryDefinition``.

        :param name: A name for the query definition.
        :param query_string: The query string to use for this query definition. For more information, see `CloudWatch Logs Insights Query Syntax <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax.html>`_ .
        :param log_group_names: Use this parameter if you want the query to query only certain log groups.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-querydefinition.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_logs as logs
            
            cfn_query_definition_props = logs.CfnQueryDefinitionProps(
                name="name",
                query_string="queryString",
            
                # the properties below are optional
                log_group_names=["logGroupNames"]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd7180e50961abf6b838dfc21ba186cc5b2c551eae8357613767f891abe51780)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument query_string", value=query_string, expected_type=type_hints["query_string"])
            check_type(argname="argument log_group_names", value=log_group_names, expected_type=type_hints["log_group_names"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "query_string": query_string,
        }
        if log_group_names is not None:
            self._values["log_group_names"] = log_group_names

    @builtins.property
    def name(self) -> builtins.str:
        '''A name for the query definition.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-querydefinition.html#cfn-logs-querydefinition-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def query_string(self) -> builtins.str:
        '''The query string to use for this query definition.

        For more information, see `CloudWatch Logs Insights Query Syntax <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-querydefinition.html#cfn-logs-querydefinition-querystring
        '''
        result = self._values.get("query_string")
        assert result is not None, "Required property 'query_string' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def log_group_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Use this parameter if you want the query to query only certain log groups.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-querydefinition.html#cfn-logs-querydefinition-loggroupnames
        '''
        result = self._values.get("log_group_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQueryDefinitionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnResourcePolicy(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_logs.CfnResourcePolicy",
):
    '''Creates or updates a resource policy that allows other AWS services to put log events to this account.

    An account can have up to 10 resource policies per AWS Region.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-resourcepolicy.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_logs as logs
        
        cfn_resource_policy = logs.CfnResourcePolicy(self, "MyCfnResourcePolicy",
            policy_document="policyDocument",
            policy_name="policyName"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        policy_document: builtins.str,
        policy_name: builtins.str,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param policy_document: The details of the policy. It must be formatted in JSON, and you must use backslashes to escape characters that need to be escaped in JSON strings, such as double quote marks.
        :param policy_name: The name of the resource policy.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96eb8f500492c7ddcaba9f292d2aa1c488941affca3b4911cd4ce9636c1ce721)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnResourcePolicyProps(
            policy_document=policy_document, policy_name=policy_name
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a2e3f9cc2e418bf4cc4f8f63fc54eed1907f2c1b38483cc8c59d2f8b653c69f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__94bd685f258ef991a46514a1b4f58ba0b0bf9314fc8055746b8652c965857253)
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
    def policy_document(self) -> builtins.str:
        '''The details of the policy.'''
        return typing.cast(builtins.str, jsii.get(self, "policyDocument"))

    @policy_document.setter
    def policy_document(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3fd3f538cb966d97639dd18283329cf7c5f581a2f069d6d37e7cd0ab5cedb7fd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyDocument", value)

    @builtins.property
    @jsii.member(jsii_name="policyName")
    def policy_name(self) -> builtins.str:
        '''The name of the resource policy.'''
        return typing.cast(builtins.str, jsii.get(self, "policyName"))

    @policy_name.setter
    def policy_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de9476941a8f893fee016885d888db6d17d101f4ad44646ba809adde15261aed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyName", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.CfnResourcePolicyProps",
    jsii_struct_bases=[],
    name_mapping={"policy_document": "policyDocument", "policy_name": "policyName"},
)
class CfnResourcePolicyProps:
    def __init__(
        self,
        *,
        policy_document: builtins.str,
        policy_name: builtins.str,
    ) -> None:
        '''Properties for defining a ``CfnResourcePolicy``.

        :param policy_document: The details of the policy. It must be formatted in JSON, and you must use backslashes to escape characters that need to be escaped in JSON strings, such as double quote marks.
        :param policy_name: The name of the resource policy.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-resourcepolicy.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_logs as logs
            
            cfn_resource_policy_props = logs.CfnResourcePolicyProps(
                policy_document="policyDocument",
                policy_name="policyName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ab184a479fd32db068d45168ec1b6bf45cf1a4a3d64847b519a088388c84df8)
            check_type(argname="argument policy_document", value=policy_document, expected_type=type_hints["policy_document"])
            check_type(argname="argument policy_name", value=policy_name, expected_type=type_hints["policy_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "policy_document": policy_document,
            "policy_name": policy_name,
        }

    @builtins.property
    def policy_document(self) -> builtins.str:
        '''The details of the policy.

        It must be formatted in JSON, and you must use backslashes to escape characters that need to be escaped in JSON strings, such as double quote marks.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-resourcepolicy.html#cfn-logs-resourcepolicy-policydocument
        '''
        result = self._values.get("policy_document")
        assert result is not None, "Required property 'policy_document' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def policy_name(self) -> builtins.str:
        '''The name of the resource policy.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-resourcepolicy.html#cfn-logs-resourcepolicy-policyname
        '''
        result = self._values.get("policy_name")
        assert result is not None, "Required property 'policy_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResourcePolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnSubscriptionFilter(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_logs.CfnSubscriptionFilter",
):
    '''The ``AWS::Logs::SubscriptionFilter`` resource specifies a subscription filter and associates it with the specified log group.

    Subscription filters allow you to subscribe to a real-time stream of log events and have them delivered to a specific destination. Currently, the supported destinations are:

    - An Amazon Kinesis data stream belonging to the same account as the subscription filter, for same-account delivery.
    - A logical destination that belongs to a different account, for cross-account delivery.
    - An Amazon Kinesis Firehose delivery stream that belongs to the same account as the subscription filter, for same-account delivery.
    - An AWS Lambda function that belongs to the same account as the subscription filter, for same-account delivery.

    There can be as many as two subscription filters associated with a log group.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-subscriptionfilter.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_logs as logs
        
        cfn_subscription_filter = logs.CfnSubscriptionFilter(self, "MyCfnSubscriptionFilter",
            destination_arn="destinationArn",
            filter_pattern="filterPattern",
            log_group_name="logGroupName",
        
            # the properties below are optional
            distribution="distribution",
            filter_name="filterName",
            role_arn="roleArn"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        destination_arn: builtins.str,
        filter_pattern: builtins.str,
        log_group_name: builtins.str,
        distribution: typing.Optional[builtins.str] = None,
        filter_name: typing.Optional[builtins.str] = None,
        role_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param destination_arn: The Amazon Resource Name (ARN) of the destination.
        :param filter_pattern: The filtering expressions that restrict what gets delivered to the destination AWS resource. For more information about the filter pattern syntax, see `Filter and Pattern Syntax <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html>`_ .
        :param log_group_name: The log group to associate with the subscription filter. All log events that are uploaded to this log group are filtered and delivered to the specified AWS resource if the filter pattern matches the log events.
        :param distribution: The method used to distribute log data to the destination, which can be either random or grouped by log stream.
        :param filter_name: The name of the subscription filter.
        :param role_arn: The ARN of an IAM role that grants CloudWatch Logs permissions to deliver ingested log events to the destination stream. You don't need to provide the ARN when you are working with a logical destination for cross-account delivery.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c7a154450656ee0f7e524d596c7e140faad893a71a7c8b9b8a85fe730a1dcf9)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSubscriptionFilterProps(
            destination_arn=destination_arn,
            filter_pattern=filter_pattern,
            log_group_name=log_group_name,
            distribution=distribution,
            filter_name=filter_name,
            role_arn=role_arn,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4fd7a0e99337509280da552b557b613a8fcb858acf9e84e9aacbe572366bca99)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0c7e4c15a871de67a808634e0ce4138af489acd8a95e0b0e5e5cb1829aa66805)
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
    @jsii.member(jsii_name="destinationArn")
    def destination_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the destination.'''
        return typing.cast(builtins.str, jsii.get(self, "destinationArn"))

    @destination_arn.setter
    def destination_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dcf92dedad133b23741e31710f66784d3728a1a96f5d9b514b8a80f012d7b84c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationArn", value)

    @builtins.property
    @jsii.member(jsii_name="filterPattern")
    def filter_pattern(self) -> builtins.str:
        '''The filtering expressions that restrict what gets delivered to the destination AWS resource.'''
        return typing.cast(builtins.str, jsii.get(self, "filterPattern"))

    @filter_pattern.setter
    def filter_pattern(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5af0335707946ab6b7311049c978104cfb68f9d36688e1bf25585706ebcbb08a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filterPattern", value)

    @builtins.property
    @jsii.member(jsii_name="logGroupName")
    def log_group_name(self) -> builtins.str:
        '''The log group to associate with the subscription filter.'''
        return typing.cast(builtins.str, jsii.get(self, "logGroupName"))

    @log_group_name.setter
    def log_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cfa4dbdd67c0f388eefe38fe86bae9148a44785d56910a1951619c1205e4eb56)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="distribution")
    def distribution(self) -> typing.Optional[builtins.str]:
        '''The method used to distribute log data to the destination, which can be either random or grouped by log stream.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "distribution"))

    @distribution.setter
    def distribution(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4730d6086a07b6e1f3b3d7251138c936aa909d17834505b0c341ec6b421adf19)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "distribution", value)

    @builtins.property
    @jsii.member(jsii_name="filterName")
    def filter_name(self) -> typing.Optional[builtins.str]:
        '''The name of the subscription filter.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "filterName"))

    @filter_name.setter
    def filter_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ccf855abfc15a31ed667e6619b6f1711fc4ef753c64ec0b754421d81c8edb75)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filterName", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of an IAM role that grants CloudWatch Logs permissions to deliver ingested log events to the destination stream.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1cdca0b99d7b39060b314b323073c0a48e25972ff085f24a455a00339addb4ee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.CfnSubscriptionFilterProps",
    jsii_struct_bases=[],
    name_mapping={
        "destination_arn": "destinationArn",
        "filter_pattern": "filterPattern",
        "log_group_name": "logGroupName",
        "distribution": "distribution",
        "filter_name": "filterName",
        "role_arn": "roleArn",
    },
)
class CfnSubscriptionFilterProps:
    def __init__(
        self,
        *,
        destination_arn: builtins.str,
        filter_pattern: builtins.str,
        log_group_name: builtins.str,
        distribution: typing.Optional[builtins.str] = None,
        filter_name: typing.Optional[builtins.str] = None,
        role_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnSubscriptionFilter``.

        :param destination_arn: The Amazon Resource Name (ARN) of the destination.
        :param filter_pattern: The filtering expressions that restrict what gets delivered to the destination AWS resource. For more information about the filter pattern syntax, see `Filter and Pattern Syntax <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html>`_ .
        :param log_group_name: The log group to associate with the subscription filter. All log events that are uploaded to this log group are filtered and delivered to the specified AWS resource if the filter pattern matches the log events.
        :param distribution: The method used to distribute log data to the destination, which can be either random or grouped by log stream.
        :param filter_name: The name of the subscription filter.
        :param role_arn: The ARN of an IAM role that grants CloudWatch Logs permissions to deliver ingested log events to the destination stream. You don't need to provide the ARN when you are working with a logical destination for cross-account delivery.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-subscriptionfilter.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_logs as logs
            
            cfn_subscription_filter_props = logs.CfnSubscriptionFilterProps(
                destination_arn="destinationArn",
                filter_pattern="filterPattern",
                log_group_name="logGroupName",
            
                # the properties below are optional
                distribution="distribution",
                filter_name="filterName",
                role_arn="roleArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1250ecc947a5eb57e428cd8fedeb9ae0f6da4eb03c22d674fa019a076ee8b507)
            check_type(argname="argument destination_arn", value=destination_arn, expected_type=type_hints["destination_arn"])
            check_type(argname="argument filter_pattern", value=filter_pattern, expected_type=type_hints["filter_pattern"])
            check_type(argname="argument log_group_name", value=log_group_name, expected_type=type_hints["log_group_name"])
            check_type(argname="argument distribution", value=distribution, expected_type=type_hints["distribution"])
            check_type(argname="argument filter_name", value=filter_name, expected_type=type_hints["filter_name"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "destination_arn": destination_arn,
            "filter_pattern": filter_pattern,
            "log_group_name": log_group_name,
        }
        if distribution is not None:
            self._values["distribution"] = distribution
        if filter_name is not None:
            self._values["filter_name"] = filter_name
        if role_arn is not None:
            self._values["role_arn"] = role_arn

    @builtins.property
    def destination_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the destination.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-subscriptionfilter.html#cfn-logs-subscriptionfilter-destinationarn
        '''
        result = self._values.get("destination_arn")
        assert result is not None, "Required property 'destination_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def filter_pattern(self) -> builtins.str:
        '''The filtering expressions that restrict what gets delivered to the destination AWS resource.

        For more information about the filter pattern syntax, see `Filter and Pattern Syntax <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-subscriptionfilter.html#cfn-logs-subscriptionfilter-filterpattern
        '''
        result = self._values.get("filter_pattern")
        assert result is not None, "Required property 'filter_pattern' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def log_group_name(self) -> builtins.str:
        '''The log group to associate with the subscription filter.

        All log events that are uploaded to this log group are filtered and delivered to the specified AWS resource if the filter pattern matches the log events.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-subscriptionfilter.html#cfn-logs-subscriptionfilter-loggroupname
        '''
        result = self._values.get("log_group_name")
        assert result is not None, "Required property 'log_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def distribution(self) -> typing.Optional[builtins.str]:
        '''The method used to distribute log data to the destination, which can be either random or grouped by log stream.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-subscriptionfilter.html#cfn-logs-subscriptionfilter-distribution
        '''
        result = self._values.get("distribution")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def filter_name(self) -> typing.Optional[builtins.str]:
        '''The name of the subscription filter.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-subscriptionfilter.html#cfn-logs-subscriptionfilter-filtername
        '''
        result = self._values.get("filter_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of an IAM role that grants CloudWatch Logs permissions to deliver ingested log events to the destination stream.

        You don't need to provide the ARN when you are working with a logical destination for cross-account delivery.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-subscriptionfilter.html#cfn-logs-subscriptionfilter-rolearn
        '''
        result = self._values.get("role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSubscriptionFilterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.ColumnRestriction",
    jsii_struct_bases=[],
    name_mapping={
        "comparison": "comparison",
        "number_value": "numberValue",
        "string_value": "stringValue",
    },
)
class ColumnRestriction:
    def __init__(
        self,
        *,
        comparison: builtins.str,
        number_value: typing.Optional[jsii.Number] = None,
        string_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param comparison: Comparison operator to use.
        :param number_value: Number value to compare to. Exactly one of 'stringValue' and 'numberValue' must be set.
        :param string_value: String value to compare to. Exactly one of 'stringValue' and 'numberValue' must be set.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_logs as logs
            
            column_restriction = logs.ColumnRestriction(
                comparison="comparison",
            
                # the properties below are optional
                number_value=123,
                string_value="stringValue"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c2766fe6d7d19a8737daff90dd79e476a2d4dcde95605b7656e40b088fdf6e64)
            check_type(argname="argument comparison", value=comparison, expected_type=type_hints["comparison"])
            check_type(argname="argument number_value", value=number_value, expected_type=type_hints["number_value"])
            check_type(argname="argument string_value", value=string_value, expected_type=type_hints["string_value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "comparison": comparison,
        }
        if number_value is not None:
            self._values["number_value"] = number_value
        if string_value is not None:
            self._values["string_value"] = string_value

    @builtins.property
    def comparison(self) -> builtins.str:
        '''Comparison operator to use.'''
        result = self._values.get("comparison")
        assert result is not None, "Required property 'comparison' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def number_value(self) -> typing.Optional[jsii.Number]:
        '''Number value to compare to.

        Exactly one of 'stringValue' and 'numberValue' must be set.
        '''
        result = self._values.get("number_value")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def string_value(self) -> typing.Optional[builtins.str]:
        '''String value to compare to.

        Exactly one of 'stringValue' and 'numberValue' must be set.
        '''
        result = self._values.get("string_value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ColumnRestriction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.CrossAccountDestinationProps",
    jsii_struct_bases=[],
    name_mapping={
        "role": "role",
        "target_arn": "targetArn",
        "destination_name": "destinationName",
    },
)
class CrossAccountDestinationProps:
    def __init__(
        self,
        *,
        role: _IRole_235f5d8e,
        target_arn: builtins.str,
        destination_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for a CrossAccountDestination.

        :param role: The role to assume that grants permissions to write to 'target'. The role must be assumable by 'logs.{REGION}.amazonaws.com'.
        :param target_arn: The log destination target's ARN.
        :param destination_name: The name of the log destination. Default: Automatically generated

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iam as iam
            from aws_cdk import aws_logs as logs
            
            # role: iam.Role
            
            cross_account_destination_props = logs.CrossAccountDestinationProps(
                role=role,
                target_arn="targetArn",
            
                # the properties below are optional
                destination_name="destinationName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4be07d68ab857f5ae6300c8382cb03fbeec1052d13af65659f773e30196e8c1)
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument target_arn", value=target_arn, expected_type=type_hints["target_arn"])
            check_type(argname="argument destination_name", value=destination_name, expected_type=type_hints["destination_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "role": role,
            "target_arn": target_arn,
        }
        if destination_name is not None:
            self._values["destination_name"] = destination_name

    @builtins.property
    def role(self) -> _IRole_235f5d8e:
        '''The role to assume that grants permissions to write to 'target'.

        The role must be assumable by 'logs.{REGION}.amazonaws.com'.
        '''
        result = self._values.get("role")
        assert result is not None, "Required property 'role' is missing"
        return typing.cast(_IRole_235f5d8e, result)

    @builtins.property
    def target_arn(self) -> builtins.str:
        '''The log destination target's ARN.'''
        result = self._values.get("target_arn")
        assert result is not None, "Required property 'target_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def destination_name(self) -> typing.Optional[builtins.str]:
        '''The name of the log destination.

        :default: Automatically generated
        '''
        result = self._values.get("destination_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CrossAccountDestinationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataIdentifier(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_logs.DataIdentifier",
):
    '''A data protection identifier.

    If an identifier is supported but not in this class, it can be passed in the constructor instead.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_kinesisfirehose_alpha as kinesisfirehose
        import aws_cdk.aws_kinesisfirehose_destinations_alpha as destinations
        
        
        log_group_destination = logs.LogGroup(self, "LogGroupLambdaAudit",
            log_group_name="auditDestinationForCDK"
        )
        
        bucket = s3.Bucket(self, "audit-bucket")
        s3_destination = destinations.S3Bucket(bucket)
        
        delivery_stream = kinesisfirehose.DeliveryStream(self, "Delivery Stream",
            destinations=[s3_destination]
        )
        
        data_protection_policy = logs.DataProtectionPolicy(
            name="data protection policy",
            description="policy description",
            identifiers=[logs.DataIdentifier.DRIVERSLICENSE_US, logs.DataIdentifier("EmailAddress")],
            log_group_audit_destination=log_group_destination,
            s3_bucket_audit_destination=bucket,
            delivery_stream_name_audit_destination=delivery_stream.delivery_stream_name
        )
        
        logs.LogGroup(self, "LogGroupLambda",
            log_group_name="cdkIntegLogGroup",
            data_protection_policy=data_protection_policy
        )
    '''

    def __init__(self, identifier: builtins.str) -> None:
        '''
        :param identifier: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15f2f9a4aba70e88d25dcda444a45fe96535b0317fb974d64d2b70c8e6982915)
            check_type(argname="argument identifier", value=identifier, expected_type=type_hints["identifier"])
        jsii.create(self.__class__, self, [identifier])

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.invoke(self, "toString", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ADDRESS")
    def ADDRESS(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "ADDRESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWSSECRETKEY")
    def AWSSECRETKEY(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "AWSSECRETKEY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="BANKACCOUNTNUMBER_DE")
    def BANKACCOUNTNUMBER_DE(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "BANKACCOUNTNUMBER_DE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="BANKACCOUNTNUMBER_ES")
    def BANKACCOUNTNUMBER_ES(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "BANKACCOUNTNUMBER_ES"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="BANKACCOUNTNUMBER_FR")
    def BANKACCOUNTNUMBER_FR(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "BANKACCOUNTNUMBER_FR"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="BANKACCOUNTNUMBER_GB")
    def BANKACCOUNTNUMBER_GB(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "BANKACCOUNTNUMBER_GB"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="BANKACCOUNTNUMBER_IT")
    def BANKACCOUNTNUMBER_IT(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "BANKACCOUNTNUMBER_IT"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="BANKACCOUNTNUMBER_US")
    def BANKACCOUNTNUMBER_US(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "BANKACCOUNTNUMBER_US"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CEPCODE_BR")
    def CEPCODE_BR(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "CEPCODE_BR"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CNPJ_BR")
    def CNPJ_BR(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "CNPJ_BR"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CPFCODE_BR")
    def CPFCODE_BR(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "CPFCODE_BR"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CREDITCARDEXPIRATION")
    def CREDITCARDEXPIRATION(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "CREDITCARDEXPIRATION"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CREDITCARDNUMBER")
    def CREDITCARDNUMBER(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "CREDITCARDNUMBER"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CREDITCARDSECURITYCODE")
    def CREDITCARDSECURITYCODE(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "CREDITCARDSECURITYCODE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DRIVERSLICENSE_AT")
    def DRIVERSLICENSE_AT(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "DRIVERSLICENSE_AT"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DRIVERSLICENSE_AU")
    def DRIVERSLICENSE_AU(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "DRIVERSLICENSE_AU"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DRIVERSLICENSE_BE")
    def DRIVERSLICENSE_BE(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "DRIVERSLICENSE_BE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DRIVERSLICENSE_BG")
    def DRIVERSLICENSE_BG(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "DRIVERSLICENSE_BG"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DRIVERSLICENSE_CA")
    def DRIVERSLICENSE_CA(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "DRIVERSLICENSE_CA"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DRIVERSLICENSE_CY")
    def DRIVERSLICENSE_CY(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "DRIVERSLICENSE_CY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DRIVERSLICENSE_CZ")
    def DRIVERSLICENSE_CZ(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "DRIVERSLICENSE_CZ"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DRIVERSLICENSE_DE")
    def DRIVERSLICENSE_DE(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "DRIVERSLICENSE_DE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DRIVERSLICENSE_DK")
    def DRIVERSLICENSE_DK(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "DRIVERSLICENSE_DK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DRIVERSLICENSE_EE")
    def DRIVERSLICENSE_EE(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "DRIVERSLICENSE_EE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DRIVERSLICENSE_ES")
    def DRIVERSLICENSE_ES(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "DRIVERSLICENSE_ES"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DRIVERSLICENSE_FI")
    def DRIVERSLICENSE_FI(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "DRIVERSLICENSE_FI"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DRIVERSLICENSE_FR")
    def DRIVERSLICENSE_FR(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "DRIVERSLICENSE_FR"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DRIVERSLICENSE_GB")
    def DRIVERSLICENSE_GB(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "DRIVERSLICENSE_GB"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DRIVERSLICENSE_GR")
    def DRIVERSLICENSE_GR(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "DRIVERSLICENSE_GR"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DRIVERSLICENSE_HR")
    def DRIVERSLICENSE_HR(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "DRIVERSLICENSE_HR"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DRIVERSLICENSE_HU")
    def DRIVERSLICENSE_HU(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "DRIVERSLICENSE_HU"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DRIVERSLICENSE_IE")
    def DRIVERSLICENSE_IE(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "DRIVERSLICENSE_IE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DRIVERSLICENSE_IT")
    def DRIVERSLICENSE_IT(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "DRIVERSLICENSE_IT"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DRIVERSLICENSE_LT")
    def DRIVERSLICENSE_LT(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "DRIVERSLICENSE_LT"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DRIVERSLICENSE_LU")
    def DRIVERSLICENSE_LU(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "DRIVERSLICENSE_LU"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DRIVERSLICENSE_LV")
    def DRIVERSLICENSE_LV(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "DRIVERSLICENSE_LV"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DRIVERSLICENSE_MT")
    def DRIVERSLICENSE_MT(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "DRIVERSLICENSE_MT"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DRIVERSLICENSE_NL")
    def DRIVERSLICENSE_NL(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "DRIVERSLICENSE_NL"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DRIVERSLICENSE_PL")
    def DRIVERSLICENSE_PL(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "DRIVERSLICENSE_PL"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DRIVERSLICENSE_PT")
    def DRIVERSLICENSE_PT(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "DRIVERSLICENSE_PT"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DRIVERSLICENSE_RO")
    def DRIVERSLICENSE_RO(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "DRIVERSLICENSE_RO"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DRIVERSLICENSE_SE")
    def DRIVERSLICENSE_SE(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "DRIVERSLICENSE_SE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DRIVERSLICENSE_SI")
    def DRIVERSLICENSE_SI(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "DRIVERSLICENSE_SI"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DRIVERSLICENSE_SK")
    def DRIVERSLICENSE_SK(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "DRIVERSLICENSE_SK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DRIVERSLICENSE_US")
    def DRIVERSLICENSE_US(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "DRIVERSLICENSE_US"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DRUGENFORCEMENTAGENCYNUMBER_US")
    def DRUGENFORCEMENTAGENCYNUMBER_US(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "DRUGENFORCEMENTAGENCYNUMBER_US"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELECTORALROLLNUMBER_GB")
    def ELECTORALROLLNUMBER_GB(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "ELECTORALROLLNUMBER_GB"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EMAILADDRESS")
    def EMAILADDRESS(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "EMAILADDRESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="HEALTHCAREPROCEDURECODE_US")
    def HEALTHCAREPROCEDURECODE_US(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "HEALTHCAREPROCEDURECODE_US"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="HEALTHINSURANCECARDNUMBER_EU")
    def HEALTHINSURANCECARDNUMBER_EU(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "HEALTHINSURANCECARDNUMBER_EU"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="HEALTHINSURANCECLAIMNUMBER_US")
    def HEALTHINSURANCECLAIMNUMBER_US(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "HEALTHINSURANCECLAIMNUMBER_US"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="HEALTHINSURANCENUMBER_FR")
    def HEALTHINSURANCENUMBER_FR(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "HEALTHINSURANCENUMBER_FR"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="INDIVIDUALTAXIDENTIFICATIONNUMBER_US")
    def INDIVIDUALTAXIDENTIFICATIONNUMBER_US(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "INDIVIDUALTAXIDENTIFICATIONNUMBER_US"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="INSEECODE_FR")
    def INSEECODE_FR(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "INSEECODE_FR"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IPADDRESS")
    def IPADDRESS(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "IPADDRESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="LATLONG")
    def LATLONG(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "LATLONG"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="MEDICAREBENEFICIARYNUMBER_US")
    def MEDICAREBENEFICIARYNUMBER_US(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "MEDICAREBENEFICIARYNUMBER_US"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="NAME")
    def NAME(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "NAME"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="NATIONALDRUGCODE_US")
    def NATIONALDRUGCODE_US(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "NATIONALDRUGCODE_US"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="NATIONALIDENTIFICATIONNUMBER_DE")
    def NATIONALIDENTIFICATIONNUMBER_DE(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "NATIONALIDENTIFICATIONNUMBER_DE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="NATIONALIDENTIFICATIONNUMBER_ES")
    def NATIONALIDENTIFICATIONNUMBER_ES(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "NATIONALIDENTIFICATIONNUMBER_ES"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="NATIONALIDENTIFICATIONNUMBER_IT")
    def NATIONALIDENTIFICATIONNUMBER_IT(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "NATIONALIDENTIFICATIONNUMBER_IT"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="NATIONALINSURANCENUMBER_GB")
    def NATIONALINSURANCENUMBER_GB(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "NATIONALINSURANCENUMBER_GB"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="NATIONALPROVIDERID_US")
    def NATIONALPROVIDERID_US(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "NATIONALPROVIDERID_US"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="NHSNUMBER_GB")
    def NHSNUMBER_GB(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "NHSNUMBER_GB"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="NIENUMBER_ES")
    def NIENUMBER_ES(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "NIENUMBER_ES"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="NIFNUMBER_ES")
    def NIFNUMBER_ES(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "NIFNUMBER_ES"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="OPENSSHPRIVATEKEY")
    def OPENSSHPRIVATEKEY(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "OPENSSHPRIVATEKEY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PASSPORTNUMBER_CA")
    def PASSPORTNUMBER_CA(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "PASSPORTNUMBER_CA"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PASSPORTNUMBER_DE")
    def PASSPORTNUMBER_DE(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "PASSPORTNUMBER_DE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PASSPORTNUMBER_ES")
    def PASSPORTNUMBER_ES(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "PASSPORTNUMBER_ES"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PASSPORTNUMBER_FR")
    def PASSPORTNUMBER_FR(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "PASSPORTNUMBER_FR"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PASSPORTNUMBER_GB")
    def PASSPORTNUMBER_GB(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "PASSPORTNUMBER_GB"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PASSPORTNUMBER_IT")
    def PASSPORTNUMBER_IT(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "PASSPORTNUMBER_IT"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PASSPORTNUMBER_US")
    def PASSPORTNUMBER_US(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "PASSPORTNUMBER_US"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PERMANENTRESIDENCENUMBER_CA")
    def PERMANENTRESIDENCENUMBER_CA(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "PERMANENTRESIDENCENUMBER_CA"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PERSONALHEALTHNUMBER_CA")
    def PERSONALHEALTHNUMBER_CA(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "PERSONALHEALTHNUMBER_CA"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PGPPRIVATEKEY")
    def PGPPRIVATEKEY(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "PGPPRIVATEKEY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PHONENUMBER")
    def PHONENUMBER(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "PHONENUMBER"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PHONENUMBER_BR")
    def PHONENUMBER_BR(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "PHONENUMBER_BR"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PHONENUMBER_DE")
    def PHONENUMBER_DE(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "PHONENUMBER_DE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PHONENUMBER_ES")
    def PHONENUMBER_ES(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "PHONENUMBER_ES"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PHONENUMBER_FR")
    def PHONENUMBER_FR(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "PHONENUMBER_FR"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PHONENUMBER_GB")
    def PHONENUMBER_GB(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "PHONENUMBER_GB"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PHONENUMBER_IT")
    def PHONENUMBER_IT(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "PHONENUMBER_IT"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PHONENUMBER_US")
    def PHONENUMBER_US(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "PHONENUMBER_US"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PKCSPRIVATEKEY")
    def PKCSPRIVATEKEY(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "PKCSPRIVATEKEY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="POSTALCODE_CA")
    def POSTALCODE_CA(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "POSTALCODE_CA"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PUTTYPRIVATEKEY")
    def PUTTYPRIVATEKEY(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "PUTTYPRIVATEKEY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="RGNUMBER_BR")
    def RGNUMBER_BR(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "RGNUMBER_BR"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SOCIALINSURANCENUMBER_CA")
    def SOCIALINSURANCENUMBER_CA(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "SOCIALINSURANCENUMBER_CA"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SSN_ES")
    def SSN_ES(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "SSN_ES"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SSN_US")
    def SSN_US(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "SSN_US"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="TAXID_DE")
    def TAXID_DE(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "TAXID_DE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="TAXID_ES")
    def TAXID_ES(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "TAXID_ES"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="TAXID_FR")
    def TAXID_FR(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "TAXID_FR"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="TAXID_GB")
    def TAXID_GB(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "TAXID_GB"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="VEHICLEIDENTIFICATIONNUMBER")
    def VEHICLEIDENTIFICATIONNUMBER(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "VEHICLEIDENTIFICATIONNUMBER"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ZIPCODE_US")
    def ZIPCODE_US(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "ZIPCODE_US"))


class DataProtectionPolicy(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_logs.DataProtectionPolicy",
):
    '''Creates a data protection policy for CloudWatch Logs log groups.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_kinesisfirehose_alpha as kinesisfirehose
        import aws_cdk.aws_kinesisfirehose_destinations_alpha as destinations
        
        
        log_group_destination = logs.LogGroup(self, "LogGroupLambdaAudit",
            log_group_name="auditDestinationForCDK"
        )
        
        bucket = s3.Bucket(self, "audit-bucket")
        s3_destination = destinations.S3Bucket(bucket)
        
        delivery_stream = kinesisfirehose.DeliveryStream(self, "Delivery Stream",
            destinations=[s3_destination]
        )
        
        data_protection_policy = logs.DataProtectionPolicy(
            name="data protection policy",
            description="policy description",
            identifiers=[logs.DataIdentifier.DRIVERSLICENSE_US, logs.DataIdentifier("EmailAddress")],
            log_group_audit_destination=log_group_destination,
            s3_bucket_audit_destination=bucket,
            delivery_stream_name_audit_destination=delivery_stream.delivery_stream_name
        )
        
        logs.LogGroup(self, "LogGroupLambda",
            log_group_name="cdkIntegLogGroup",
            data_protection_policy=data_protection_policy
        )
    '''

    def __init__(
        self,
        *,
        identifiers: typing.Sequence[DataIdentifier],
        delivery_stream_name_audit_destination: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        log_group_audit_destination: typing.Optional["ILogGroup"] = None,
        name: typing.Optional[builtins.str] = None,
        s3_bucket_audit_destination: typing.Optional[_IBucket_42e086fd] = None,
    ) -> None:
        '''
        :param identifiers: List of data protection identifiers. Must be in the following list: https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/protect-sensitive-log-data-types.html
        :param delivery_stream_name_audit_destination: Amazon Kinesis Data Firehose delivery stream to send audit findings to. The delivery stream must already exist. Default: - no firehose delivery stream audit destination
        :param description: Description of the data protection policy. Default: - 'cdk generated data protection policy'
        :param log_group_audit_destination: CloudWatch Logs log group to send audit findings to. The log group must already exist prior to creating the data protection policy. Default: - no CloudWatch Logs audit destination
        :param name: Name of the data protection policy. Default: - 'data-protection-policy-cdk'
        :param s3_bucket_audit_destination: S3 bucket to send audit findings to. The bucket must already exist. Default: - no S3 bucket audit destination
        '''
        props = DataProtectionPolicyProps(
            identifiers=identifiers,
            delivery_stream_name_audit_destination=delivery_stream_name_audit_destination,
            description=description,
            log_group_audit_destination=log_group_audit_destination,
            name=name,
            s3_bucket_audit_destination=s3_bucket_audit_destination,
        )

        jsii.create(self.__class__, self, [props])


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.DataProtectionPolicyConfig",
    jsii_struct_bases=[],
    name_mapping={
        "description": "description",
        "name": "name",
        "statement": "statement",
        "version": "version",
    },
)
class DataProtectionPolicyConfig:
    def __init__(
        self,
        *,
        description: builtins.str,
        name: builtins.str,
        statement: typing.Any,
        version: builtins.str,
    ) -> None:
        '''Interface representing a data protection policy.

        :param description: Description of the data protection policy. Default: - 'cdk generated data protection policy'
        :param name: Name of the data protection policy. Default: - 'data-protection-policy-cdk'
        :param statement: Statements within the data protection policy. Must contain one Audit and one Redact statement
        :param version: Version of the data protection policy.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_logs as logs
            
            # statement: Any
            
            data_protection_policy_config = logs.DataProtectionPolicyConfig(
                description="description",
                name="name",
                statement=statement,
                version="version"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__376464888d50baaad4ab20b9ef8766e9aa93a91c55c8662ab5ec2fafa8086822)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument statement", value=statement, expected_type=type_hints["statement"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "name": name,
            "statement": statement,
            "version": version,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''Description of the data protection policy.

        :default: - 'cdk generated data protection policy'
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the data protection policy.

        :default: - 'data-protection-policy-cdk'
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def statement(self) -> typing.Any:
        '''Statements within the data protection policy.

        Must contain one Audit and one Redact statement
        '''
        result = self._values.get("statement")
        assert result is not None, "Required property 'statement' is missing"
        return typing.cast(typing.Any, result)

    @builtins.property
    def version(self) -> builtins.str:
        '''Version of the data protection policy.'''
        result = self._values.get("version")
        assert result is not None, "Required property 'version' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataProtectionPolicyConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.DataProtectionPolicyProps",
    jsii_struct_bases=[],
    name_mapping={
        "identifiers": "identifiers",
        "delivery_stream_name_audit_destination": "deliveryStreamNameAuditDestination",
        "description": "description",
        "log_group_audit_destination": "logGroupAuditDestination",
        "name": "name",
        "s3_bucket_audit_destination": "s3BucketAuditDestination",
    },
)
class DataProtectionPolicyProps:
    def __init__(
        self,
        *,
        identifiers: typing.Sequence[DataIdentifier],
        delivery_stream_name_audit_destination: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        log_group_audit_destination: typing.Optional["ILogGroup"] = None,
        name: typing.Optional[builtins.str] = None,
        s3_bucket_audit_destination: typing.Optional[_IBucket_42e086fd] = None,
    ) -> None:
        '''Properties for creating a data protection policy.

        :param identifiers: List of data protection identifiers. Must be in the following list: https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/protect-sensitive-log-data-types.html
        :param delivery_stream_name_audit_destination: Amazon Kinesis Data Firehose delivery stream to send audit findings to. The delivery stream must already exist. Default: - no firehose delivery stream audit destination
        :param description: Description of the data protection policy. Default: - 'cdk generated data protection policy'
        :param log_group_audit_destination: CloudWatch Logs log group to send audit findings to. The log group must already exist prior to creating the data protection policy. Default: - no CloudWatch Logs audit destination
        :param name: Name of the data protection policy. Default: - 'data-protection-policy-cdk'
        :param s3_bucket_audit_destination: S3 bucket to send audit findings to. The bucket must already exist. Default: - no S3 bucket audit destination

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_kinesisfirehose_alpha as kinesisfirehose
            import aws_cdk.aws_kinesisfirehose_destinations_alpha as destinations
            
            
            log_group_destination = logs.LogGroup(self, "LogGroupLambdaAudit",
                log_group_name="auditDestinationForCDK"
            )
            
            bucket = s3.Bucket(self, "audit-bucket")
            s3_destination = destinations.S3Bucket(bucket)
            
            delivery_stream = kinesisfirehose.DeliveryStream(self, "Delivery Stream",
                destinations=[s3_destination]
            )
            
            data_protection_policy = logs.DataProtectionPolicy(
                name="data protection policy",
                description="policy description",
                identifiers=[logs.DataIdentifier.DRIVERSLICENSE_US, logs.DataIdentifier("EmailAddress")],
                log_group_audit_destination=log_group_destination,
                s3_bucket_audit_destination=bucket,
                delivery_stream_name_audit_destination=delivery_stream.delivery_stream_name
            )
            
            logs.LogGroup(self, "LogGroupLambda",
                log_group_name="cdkIntegLogGroup",
                data_protection_policy=data_protection_policy
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7783165e1d00e232a8ee35869f53b7ff500c9680f96b895f705e24475c7b6b2)
            check_type(argname="argument identifiers", value=identifiers, expected_type=type_hints["identifiers"])
            check_type(argname="argument delivery_stream_name_audit_destination", value=delivery_stream_name_audit_destination, expected_type=type_hints["delivery_stream_name_audit_destination"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument log_group_audit_destination", value=log_group_audit_destination, expected_type=type_hints["log_group_audit_destination"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument s3_bucket_audit_destination", value=s3_bucket_audit_destination, expected_type=type_hints["s3_bucket_audit_destination"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "identifiers": identifiers,
        }
        if delivery_stream_name_audit_destination is not None:
            self._values["delivery_stream_name_audit_destination"] = delivery_stream_name_audit_destination
        if description is not None:
            self._values["description"] = description
        if log_group_audit_destination is not None:
            self._values["log_group_audit_destination"] = log_group_audit_destination
        if name is not None:
            self._values["name"] = name
        if s3_bucket_audit_destination is not None:
            self._values["s3_bucket_audit_destination"] = s3_bucket_audit_destination

    @builtins.property
    def identifiers(self) -> typing.List[DataIdentifier]:
        '''List of data protection identifiers.

        Must be in the following list: https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/protect-sensitive-log-data-types.html
        '''
        result = self._values.get("identifiers")
        assert result is not None, "Required property 'identifiers' is missing"
        return typing.cast(typing.List[DataIdentifier], result)

    @builtins.property
    def delivery_stream_name_audit_destination(self) -> typing.Optional[builtins.str]:
        '''Amazon Kinesis Data Firehose delivery stream to send audit findings to.

        The delivery stream must already exist.

        :default: - no firehose delivery stream audit destination
        '''
        result = self._values.get("delivery_stream_name_audit_destination")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Description of the data protection policy.

        :default: - 'cdk generated data protection policy'
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_group_audit_destination(self) -> typing.Optional["ILogGroup"]:
        '''CloudWatch Logs log group to send audit findings to.

        The log group must already exist prior to creating the data protection policy.

        :default: - no CloudWatch Logs audit destination
        '''
        result = self._values.get("log_group_audit_destination")
        return typing.cast(typing.Optional["ILogGroup"], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the data protection policy.

        :default: - 'data-protection-policy-cdk'
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def s3_bucket_audit_destination(self) -> typing.Optional[_IBucket_42e086fd]:
        '''S3 bucket to send audit findings to.

        The bucket must already exist.

        :default: - no S3 bucket audit destination
        '''
        result = self._values.get("s3_bucket_audit_destination")
        return typing.cast(typing.Optional[_IBucket_42e086fd], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataProtectionPolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FilterPattern(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_logs.FilterPattern",
):
    '''A collection of static methods to generate appropriate ILogPatterns.

    :exampleMetadata: infused

    Example::

        # Search for all events where the component field is equal to
        # "HttpServer" and either error is true or the latency is higher
        # than 1000.
        pattern = logs.FilterPattern.all(
            logs.FilterPattern.string_value("$.component", "=", "HttpServer"),
            logs.FilterPattern.any(
                logs.FilterPattern.boolean_value("$.error", True),
                logs.FilterPattern.number_value("$.latency", ">", 1000)))
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="all")
    @builtins.classmethod
    def all(cls, *patterns: "JsonPattern") -> "JsonPattern":
        '''A JSON log pattern that matches if all given JSON log patterns match.

        :param patterns: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef6e7314c6a5197496584b4f3fc9dc8a24050e8d3d30eabb788540b98e00e4f0)
            check_type(argname="argument patterns", value=patterns, expected_type=typing.Tuple[type_hints["patterns"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast("JsonPattern", jsii.sinvoke(cls, "all", [*patterns]))

    @jsii.member(jsii_name="allEvents")
    @builtins.classmethod
    def all_events(cls) -> "IFilterPattern":
        '''A log pattern that matches all events.'''
        return typing.cast("IFilterPattern", jsii.sinvoke(cls, "allEvents", []))

    @jsii.member(jsii_name="allTerms")
    @builtins.classmethod
    def all_terms(cls, *terms: builtins.str) -> "IFilterPattern":
        '''A log pattern that matches if all the strings given appear in the event.

        :param terms: The words to search for. All terms must match.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c83797f363cc2a7f1bb9ea15ea4f4d7eeed745e9d300970e536e8df78633b0a6)
            check_type(argname="argument terms", value=terms, expected_type=typing.Tuple[type_hints["terms"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast("IFilterPattern", jsii.sinvoke(cls, "allTerms", [*terms]))

    @jsii.member(jsii_name="any")
    @builtins.classmethod
    def any(cls, *patterns: "JsonPattern") -> "JsonPattern":
        '''A JSON log pattern that matches if any of the given JSON log patterns match.

        :param patterns: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06cd0420e64a91321c2dbdcdb6fa54fa56bffd0eab770aa6aa4000670f1beec3)
            check_type(argname="argument patterns", value=patterns, expected_type=typing.Tuple[type_hints["patterns"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast("JsonPattern", jsii.sinvoke(cls, "any", [*patterns]))

    @jsii.member(jsii_name="anyTerm")
    @builtins.classmethod
    def any_term(cls, *terms: builtins.str) -> "IFilterPattern":
        '''A log pattern that matches if any of the strings given appear in the event.

        :param terms: The words to search for. Any terms must match.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b38181b10ed8fe5993dd7ec40690693fe0d164f997f37ddbf297f8b840de2b18)
            check_type(argname="argument terms", value=terms, expected_type=typing.Tuple[type_hints["terms"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast("IFilterPattern", jsii.sinvoke(cls, "anyTerm", [*terms]))

    @jsii.member(jsii_name="anyTermGroup")
    @builtins.classmethod
    def any_term_group(
        cls,
        *term_groups: typing.List[builtins.str],
    ) -> "IFilterPattern":
        '''A log pattern that matches if any of the given term groups matches the event.

        A term group matches an event if all the terms in it appear in the event string.

        :param term_groups: A list of term groups to search for. Any one of the clauses must match.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2623b46359820ca611b2cf65fab9b8e6c24ef2bd3d30bcebc3d022b2173b58ee)
            check_type(argname="argument term_groups", value=term_groups, expected_type=typing.Tuple[type_hints["term_groups"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast("IFilterPattern", jsii.sinvoke(cls, "anyTermGroup", [*term_groups]))

    @jsii.member(jsii_name="booleanValue")
    @builtins.classmethod
    def boolean_value(
        cls,
        json_field: builtins.str,
        value: builtins.bool,
    ) -> "JsonPattern":
        '''A JSON log pattern that matches if the field exists and equals the boolean value.

        :param json_field: Field inside JSON. Example: "$.myField"
        :param value: The value to match.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0e87f500ca69757a8ec1184452b5b2b45c68758c062a77bc2248afd2c3b793e)
            check_type(argname="argument json_field", value=json_field, expected_type=type_hints["json_field"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast("JsonPattern", jsii.sinvoke(cls, "booleanValue", [json_field, value]))

    @jsii.member(jsii_name="exists")
    @builtins.classmethod
    def exists(cls, json_field: builtins.str) -> "JsonPattern":
        '''A JSON log patter that matches if the field exists.

        This is a readable convenience wrapper over 'field = *'

        :param json_field: Field inside JSON. Example: "$.myField"
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56192ad48c0fbacd0f9f10fc26eebe8f311d8164217227e094a00a61f7c0d300)
            check_type(argname="argument json_field", value=json_field, expected_type=type_hints["json_field"])
        return typing.cast("JsonPattern", jsii.sinvoke(cls, "exists", [json_field]))

    @jsii.member(jsii_name="isNull")
    @builtins.classmethod
    def is_null(cls, json_field: builtins.str) -> "JsonPattern":
        '''A JSON log pattern that matches if the field exists and has the special value 'null'.

        :param json_field: Field inside JSON. Example: "$.myField"
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93deee33b43c0efbe360f5ef6a60ba3cd0c1af95d7ca176abb95a482e1be8748)
            check_type(argname="argument json_field", value=json_field, expected_type=type_hints["json_field"])
        return typing.cast("JsonPattern", jsii.sinvoke(cls, "isNull", [json_field]))

    @jsii.member(jsii_name="literal")
    @builtins.classmethod
    def literal(cls, log_pattern_string: builtins.str) -> "IFilterPattern":
        '''Use the given string as log pattern.

        See https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html
        for information on writing log patterns.

        :param log_pattern_string: The pattern string to use.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65d91e718fc9d96060c30c68dee958f370d2ae16fbb2e3cf8f0030e0408b3320)
            check_type(argname="argument log_pattern_string", value=log_pattern_string, expected_type=type_hints["log_pattern_string"])
        return typing.cast("IFilterPattern", jsii.sinvoke(cls, "literal", [log_pattern_string]))

    @jsii.member(jsii_name="notExists")
    @builtins.classmethod
    def not_exists(cls, json_field: builtins.str) -> "JsonPattern":
        '''A JSON log pattern that matches if the field does not exist.

        :param json_field: Field inside JSON. Example: "$.myField"
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a90c7e4fc8c86ca2759be152abbd3a44e4e78851d525cdb047698b1825283849)
            check_type(argname="argument json_field", value=json_field, expected_type=type_hints["json_field"])
        return typing.cast("JsonPattern", jsii.sinvoke(cls, "notExists", [json_field]))

    @jsii.member(jsii_name="numberValue")
    @builtins.classmethod
    def number_value(
        cls,
        json_field: builtins.str,
        comparison: builtins.str,
        value: jsii.Number,
    ) -> "JsonPattern":
        '''A JSON log pattern that compares numerical values.

        This pattern only matches if the event is a JSON event, and the indicated field inside
        compares with the value in the indicated way.

        Use '$' to indicate the root of the JSON structure. The comparison operator can only
        compare equality or inequality. The '*' wildcard may appear in the value may at the
        start or at the end.

        For more information, see:

        https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html

        :param json_field: Field inside JSON. Example: "$.myField"
        :param comparison: Comparison to carry out. One of =, !=, <, <=, >, >=.
        :param value: The numerical value to compare to.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1cb7dce1caa0866199f67de4ab23972e5d6dc3cd90ca77ce9a5f09f7dc2b1fa)
            check_type(argname="argument json_field", value=json_field, expected_type=type_hints["json_field"])
            check_type(argname="argument comparison", value=comparison, expected_type=type_hints["comparison"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast("JsonPattern", jsii.sinvoke(cls, "numberValue", [json_field, comparison, value]))

    @jsii.member(jsii_name="spaceDelimited")
    @builtins.classmethod
    def space_delimited(cls, *columns: builtins.str) -> "SpaceDelimitedTextPattern":
        '''A space delimited log pattern matcher.

        The log event is divided into space-delimited columns (optionally
        enclosed by "" or [] to capture spaces into column values), and names
        are given to each column.

        '...' may be specified once to match any number of columns.

        Afterwards, conditions may be added to individual columns.

        :param columns: The columns in the space-delimited log stream.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f5f56f60ccfd9dae1e3e3f54e54d87c6fb3e287c5bd2ad7924a4578ee4f8121)
            check_type(argname="argument columns", value=columns, expected_type=typing.Tuple[type_hints["columns"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast("SpaceDelimitedTextPattern", jsii.sinvoke(cls, "spaceDelimited", [*columns]))

    @jsii.member(jsii_name="stringValue")
    @builtins.classmethod
    def string_value(
        cls,
        json_field: builtins.str,
        comparison: builtins.str,
        value: builtins.str,
    ) -> "JsonPattern":
        '''A JSON log pattern that compares string values.

        This pattern only matches if the event is a JSON event, and the indicated field inside
        compares with the string value.

        Use '$' to indicate the root of the JSON structure. The comparison operator can only
        compare equality or inequality. The '*' wildcard may appear in the value may at the
        start or at the end.

        For more information, see:

        https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html

        :param json_field: Field inside JSON. Example: "$.myField"
        :param comparison: Comparison to carry out. Either = or !=.
        :param value: The string value to compare to. May use '*' as wildcard at start or end of string.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__31ecfe1cc2c14607ed9938dc33b51889185e1c9f4ea9e9e7ce494ae69f7d3374)
            check_type(argname="argument json_field", value=json_field, expected_type=type_hints["json_field"])
            check_type(argname="argument comparison", value=comparison, expected_type=type_hints["comparison"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast("JsonPattern", jsii.sinvoke(cls, "stringValue", [json_field, comparison, value]))


@jsii.interface(jsii_type="aws-cdk-lib.aws_logs.IFilterPattern")
class IFilterPattern(typing_extensions.Protocol):
    '''Interface for objects that can render themselves to log patterns.'''

    @builtins.property
    @jsii.member(jsii_name="logPatternString")
    def log_pattern_string(self) -> builtins.str:
        ...


class _IFilterPatternProxy:
    '''Interface for objects that can render themselves to log patterns.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_logs.IFilterPattern"

    @builtins.property
    @jsii.member(jsii_name="logPatternString")
    def log_pattern_string(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logPatternString"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFilterPattern).__jsii_proxy_class__ = lambda : _IFilterPatternProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_logs.ILogGroup")
class ILogGroup(_IResourceWithPolicy_720d64fc, typing_extensions.Protocol):
    @builtins.property
    @jsii.member(jsii_name="logGroupArn")
    def log_group_arn(self) -> builtins.str:
        '''The ARN of this log group, with ':*' appended.

        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="logGroupName")
    def log_group_name(self) -> builtins.str:
        '''The name of this log group.

        :attribute: true
        '''
        ...

    @jsii.member(jsii_name="addMetricFilter")
    def add_metric_filter(
        self,
        id: builtins.str,
        *,
        filter_pattern: IFilterPattern,
        metric_name: builtins.str,
        metric_namespace: builtins.str,
        default_value: typing.Optional[jsii.Number] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        filter_name: typing.Optional[builtins.str] = None,
        metric_value: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> "MetricFilter":
        '''Create a new Metric Filter on this Log Group.

        :param id: Unique identifier for the construct in its parent.
        :param filter_pattern: Pattern to search for log events.
        :param metric_name: The name of the metric to emit.
        :param metric_namespace: The namespace of the metric to emit.
        :param default_value: The value to emit if the pattern does not match a particular event. Default: No metric emitted.
        :param dimensions: The fields to use as dimensions for the metric. One metric filter can include as many as three dimensions. Default: - No dimensions attached to metrics.
        :param filter_name: The name of the metric filter. Default: - Cloudformation generated name.
        :param metric_value: The value to emit for the metric. Can either be a literal number (typically "1"), or the name of a field in the structure to take the value from the matched event. If you are using a field value, the field value must have been matched using the pattern. If you want to specify a field from a matched JSON structure, use '$.fieldName', and make sure the field is in the pattern (if only as '$.fieldName = *'). If you want to specify a field from a matched space-delimited structure, use '$fieldName'. Default: "1"
        :param unit: The unit to assign to the metric. Default: - No unit attached to metrics.
        '''
        ...

    @jsii.member(jsii_name="addStream")
    def add_stream(
        self,
        id: builtins.str,
        *,
        log_stream_name: typing.Optional[builtins.str] = None,
    ) -> "LogStream":
        '''Create a new Log Stream for this Log Group.

        :param id: Unique identifier for the construct in its parent.
        :param log_stream_name: The name of the log stream to create. The name must be unique within the log group. Default: Automatically generated
        '''
        ...

    @jsii.member(jsii_name="addSubscriptionFilter")
    def add_subscription_filter(
        self,
        id: builtins.str,
        *,
        destination: "ILogSubscriptionDestination",
        filter_pattern: IFilterPattern,
        filter_name: typing.Optional[builtins.str] = None,
    ) -> "SubscriptionFilter":
        '''Create a new Subscription Filter on this Log Group.

        :param id: Unique identifier for the construct in its parent.
        :param destination: The destination to send the filtered events to. For example, a Kinesis stream or a Lambda function.
        :param filter_pattern: Log events matching this pattern will be sent to the destination.
        :param filter_name: The name of the subscription filter. Default: Automatically generated
        '''
        ...

    @jsii.member(jsii_name="extractMetric")
    def extract_metric(
        self,
        json_field: builtins.str,
        metric_namespace: builtins.str,
        metric_name: builtins.str,
    ) -> _Metric_e396a4dc:
        '''Extract a metric from structured log events in the LogGroup.

        Creates a MetricFilter on this LogGroup that will extract the value
        of the indicated JSON field in all records where it occurs.

        The metric will be available in CloudWatch Metrics under the
        indicated namespace and name.

        :param json_field: JSON field to extract (example: '$.myfield').
        :param metric_namespace: Namespace to emit the metric under.
        :param metric_name: Name to emit the metric under.

        :return: A Metric object representing the extracted metric
        '''
        ...

    @jsii.member(jsii_name="grant")
    def grant(
        self,
        grantee: _IGrantable_71c4f5de,
        *actions: builtins.str,
    ) -> _Grant_a7ae64f8:
        '''Give the indicated permissions on this log group and all streams.

        :param grantee: -
        :param actions: -
        '''
        ...

    @jsii.member(jsii_name="grantRead")
    def grant_read(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Give permissions to read from this log group and streams.

        :param grantee: -
        '''
        ...

    @jsii.member(jsii_name="grantWrite")
    def grant_write(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Give permissions to write to create and write to streams in this log group.

        :param grantee: -
        '''
        ...

    @jsii.member(jsii_name="logGroupPhysicalName")
    def log_group_physical_name(self) -> builtins.str:
        '''Public method to get the physical name of this log group.'''
        ...


class _ILogGroupProxy(
    jsii.proxy_for(_IResourceWithPolicy_720d64fc), # type: ignore[misc]
):
    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_logs.ILogGroup"

    @builtins.property
    @jsii.member(jsii_name="logGroupArn")
    def log_group_arn(self) -> builtins.str:
        '''The ARN of this log group, with ':*' appended.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "logGroupArn"))

    @builtins.property
    @jsii.member(jsii_name="logGroupName")
    def log_group_name(self) -> builtins.str:
        '''The name of this log group.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "logGroupName"))

    @jsii.member(jsii_name="addMetricFilter")
    def add_metric_filter(
        self,
        id: builtins.str,
        *,
        filter_pattern: IFilterPattern,
        metric_name: builtins.str,
        metric_namespace: builtins.str,
        default_value: typing.Optional[jsii.Number] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        filter_name: typing.Optional[builtins.str] = None,
        metric_value: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> "MetricFilter":
        '''Create a new Metric Filter on this Log Group.

        :param id: Unique identifier for the construct in its parent.
        :param filter_pattern: Pattern to search for log events.
        :param metric_name: The name of the metric to emit.
        :param metric_namespace: The namespace of the metric to emit.
        :param default_value: The value to emit if the pattern does not match a particular event. Default: No metric emitted.
        :param dimensions: The fields to use as dimensions for the metric. One metric filter can include as many as three dimensions. Default: - No dimensions attached to metrics.
        :param filter_name: The name of the metric filter. Default: - Cloudformation generated name.
        :param metric_value: The value to emit for the metric. Can either be a literal number (typically "1"), or the name of a field in the structure to take the value from the matched event. If you are using a field value, the field value must have been matched using the pattern. If you want to specify a field from a matched JSON structure, use '$.fieldName', and make sure the field is in the pattern (if only as '$.fieldName = *'). If you want to specify a field from a matched space-delimited structure, use '$fieldName'. Default: "1"
        :param unit: The unit to assign to the metric. Default: - No unit attached to metrics.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c3910e9df11478e889b7f25e252df8a33e79b82dd18c304bf83e6be63f60c95)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = MetricFilterOptions(
            filter_pattern=filter_pattern,
            metric_name=metric_name,
            metric_namespace=metric_namespace,
            default_value=default_value,
            dimensions=dimensions,
            filter_name=filter_name,
            metric_value=metric_value,
            unit=unit,
        )

        return typing.cast("MetricFilter", jsii.invoke(self, "addMetricFilter", [id, props]))

    @jsii.member(jsii_name="addStream")
    def add_stream(
        self,
        id: builtins.str,
        *,
        log_stream_name: typing.Optional[builtins.str] = None,
    ) -> "LogStream":
        '''Create a new Log Stream for this Log Group.

        :param id: Unique identifier for the construct in its parent.
        :param log_stream_name: The name of the log stream to create. The name must be unique within the log group. Default: Automatically generated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad3db791d4d809f8716f4717b634e830370009e865e37f5c54e65cc5c5d57102)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = StreamOptions(log_stream_name=log_stream_name)

        return typing.cast("LogStream", jsii.invoke(self, "addStream", [id, props]))

    @jsii.member(jsii_name="addSubscriptionFilter")
    def add_subscription_filter(
        self,
        id: builtins.str,
        *,
        destination: "ILogSubscriptionDestination",
        filter_pattern: IFilterPattern,
        filter_name: typing.Optional[builtins.str] = None,
    ) -> "SubscriptionFilter":
        '''Create a new Subscription Filter on this Log Group.

        :param id: Unique identifier for the construct in its parent.
        :param destination: The destination to send the filtered events to. For example, a Kinesis stream or a Lambda function.
        :param filter_pattern: Log events matching this pattern will be sent to the destination.
        :param filter_name: The name of the subscription filter. Default: Automatically generated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3445e5a6f896ca9cd9e8a527d7229440b3a517fd59dc21bc08b64ef68e4f4eaa)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = SubscriptionFilterOptions(
            destination=destination,
            filter_pattern=filter_pattern,
            filter_name=filter_name,
        )

        return typing.cast("SubscriptionFilter", jsii.invoke(self, "addSubscriptionFilter", [id, props]))

    @jsii.member(jsii_name="extractMetric")
    def extract_metric(
        self,
        json_field: builtins.str,
        metric_namespace: builtins.str,
        metric_name: builtins.str,
    ) -> _Metric_e396a4dc:
        '''Extract a metric from structured log events in the LogGroup.

        Creates a MetricFilter on this LogGroup that will extract the value
        of the indicated JSON field in all records where it occurs.

        The metric will be available in CloudWatch Metrics under the
        indicated namespace and name.

        :param json_field: JSON field to extract (example: '$.myfield').
        :param metric_namespace: Namespace to emit the metric under.
        :param metric_name: Name to emit the metric under.

        :return: A Metric object representing the extracted metric
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9dc31b09300449039c7ac2db2c1e23ab325c60cc2fa2fa9ee5b513c2e1d62f7b)
            check_type(argname="argument json_field", value=json_field, expected_type=type_hints["json_field"])
            check_type(argname="argument metric_namespace", value=metric_namespace, expected_type=type_hints["metric_namespace"])
            check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "extractMetric", [json_field, metric_namespace, metric_name]))

    @jsii.member(jsii_name="grant")
    def grant(
        self,
        grantee: _IGrantable_71c4f5de,
        *actions: builtins.str,
    ) -> _Grant_a7ae64f8:
        '''Give the indicated permissions on this log group and all streams.

        :param grantee: -
        :param actions: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d45146324c9cc51983b9b92779906c83ea73e499386493771cdd256c131ca87)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
            check_type(argname="argument actions", value=actions, expected_type=typing.Tuple[type_hints["actions"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grant", [grantee, *actions]))

    @jsii.member(jsii_name="grantRead")
    def grant_read(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Give permissions to read from this log group and streams.

        :param grantee: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10f2b216c33139da1022d0b7d73974166dcf17c508e30913421c9f89375a9bb0)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantRead", [grantee]))

    @jsii.member(jsii_name="grantWrite")
    def grant_write(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Give permissions to write to create and write to streams in this log group.

        :param grantee: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__558c66823e9e8b21feeb1abd2b6534206c929fdf82184f3c0d1aff2942610538)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantWrite", [grantee]))

    @jsii.member(jsii_name="logGroupPhysicalName")
    def log_group_physical_name(self) -> builtins.str:
        '''Public method to get the physical name of this log group.'''
        return typing.cast(builtins.str, jsii.invoke(self, "logGroupPhysicalName", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILogGroup).__jsii_proxy_class__ = lambda : _ILogGroupProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_logs.ILogStream")
class ILogStream(_IResource_c80c4260, typing_extensions.Protocol):
    @builtins.property
    @jsii.member(jsii_name="logStreamName")
    def log_stream_name(self) -> builtins.str:
        '''The name of this log stream.

        :attribute: true
        '''
        ...


class _ILogStreamProxy(
    jsii.proxy_for(_IResource_c80c4260), # type: ignore[misc]
):
    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_logs.ILogStream"

    @builtins.property
    @jsii.member(jsii_name="logStreamName")
    def log_stream_name(self) -> builtins.str:
        '''The name of this log stream.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "logStreamName"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILogStream).__jsii_proxy_class__ = lambda : _ILogStreamProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_logs.ILogSubscriptionDestination")
class ILogSubscriptionDestination(typing_extensions.Protocol):
    '''Interface for classes that can be the destination of a log Subscription.'''

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        scope: _constructs_77d1e7e8.Construct,
        source_log_group: ILogGroup,
    ) -> "LogSubscriptionDestinationConfig":
        '''Return the properties required to send subscription events to this destination.

        If necessary, the destination can use the properties of the SubscriptionFilter
        object itself to configure its permissions to allow the subscription to write
        to it.

        The destination may reconfigure its own permissions in response to this
        function call.

        :param scope: -
        :param source_log_group: -
        '''
        ...


class _ILogSubscriptionDestinationProxy:
    '''Interface for classes that can be the destination of a log Subscription.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_logs.ILogSubscriptionDestination"

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        scope: _constructs_77d1e7e8.Construct,
        source_log_group: ILogGroup,
    ) -> "LogSubscriptionDestinationConfig":
        '''Return the properties required to send subscription events to this destination.

        If necessary, the destination can use the properties of the SubscriptionFilter
        object itself to configure its permissions to allow the subscription to write
        to it.

        The destination may reconfigure its own permissions in response to this
        function call.

        :param scope: -
        :param source_log_group: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d2d750464949100272f59f23f28dae31a40c84ad1d188b0cd44fdca6ca395d5)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument source_log_group", value=source_log_group, expected_type=type_hints["source_log_group"])
        return typing.cast("LogSubscriptionDestinationConfig", jsii.invoke(self, "bind", [scope, source_log_group]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILogSubscriptionDestination).__jsii_proxy_class__ = lambda : _ILogSubscriptionDestinationProxy


@jsii.implements(IFilterPattern)
class JsonPattern(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="aws-cdk-lib.aws_logs.JsonPattern",
):
    '''Base class for patterns that only match JSON log events.

    :exampleMetadata: infused

    Example::

        # Search for all events where the component field is equal to
        # "HttpServer" and either error is true or the latency is higher
        # than 1000.
        pattern = logs.FilterPattern.all(
            logs.FilterPattern.string_value("$.component", "=", "HttpServer"),
            logs.FilterPattern.any(
                logs.FilterPattern.boolean_value("$.error", True),
                logs.FilterPattern.number_value("$.latency", ">", 1000)))
    '''

    def __init__(self, json_pattern_string: builtins.str) -> None:
        '''
        :param json_pattern_string: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63b70184328854d0009cc9ba82f6a6720fd48ccf9458964b5cc75f6cfb653549)
            check_type(argname="argument json_pattern_string", value=json_pattern_string, expected_type=type_hints["json_pattern_string"])
        jsii.create(self.__class__, self, [json_pattern_string])

    @builtins.property
    @jsii.member(jsii_name="jsonPatternString")
    def json_pattern_string(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "jsonPatternString"))

    @builtins.property
    @jsii.member(jsii_name="logPatternString")
    def log_pattern_string(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logPatternString"))


class _JsonPatternProxy(JsonPattern):
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, JsonPattern).__jsii_proxy_class__ = lambda : _JsonPatternProxy


@jsii.implements(ILogGroup)
class LogGroup(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_logs.LogGroup",
):
    '''Define a CloudWatch Log Group.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_logs as logs
        
        
        log_group = logs.LogGroup(self, "Log Group")
        log_bucket = s3.Bucket(self, "S3 Bucket")
        
        tasks.EmrContainersStartJobRun(self, "EMR Containers Start Job Run",
            virtual_cluster=tasks.VirtualClusterInput.from_virtual_cluster_id("de92jdei2910fwedz"),
            release_label=tasks.ReleaseLabel.EMR_6_2_0,
            job_driver=tasks.JobDriver(
                spark_submit_job_driver=tasks.SparkSubmitJobDriver(
                    entry_point=sfn.TaskInput.from_text("local:///usr/lib/spark/examples/src/main/python/pi.py"),
                    spark_submit_parameters="--conf spark.executor.instances=2 --conf spark.executor.memory=2G --conf spark.executor.cores=2 --conf spark.driver.cores=1"
                )
            ),
            monitoring=tasks.Monitoring(
                log_group=log_group,
                log_bucket=log_bucket
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        data_protection_policy: typing.Optional[DataProtectionPolicy] = None,
        encryption_key: typing.Optional[_IKey_5f11635f] = None,
        log_group_name: typing.Optional[builtins.str] = None,
        removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
        retention: typing.Optional["RetentionDays"] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param data_protection_policy: Data Protection Policy for this log group. Default: - no data protection policy
        :param encryption_key: The KMS customer managed key to encrypt the log group with. Default: Server-side encrpytion managed by the CloudWatch Logs service
        :param log_group_name: Name of the log group. Default: Automatically generated
        :param removal_policy: Determine the removal policy of this log group. Normally you want to retain the log group so you can diagnose issues from logs even after a deployment that no longer includes the log group. In that case, use the normal date-based retention policy to age out your logs. Default: RemovalPolicy.Retain
        :param retention: How long, in days, the log contents will be retained. To retain all logs, set this value to RetentionDays.INFINITE. Default: RetentionDays.TWO_YEARS
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__308a02ff022bfc4531ef0c547fbfb8db809293b3cda70c61106c9bc271126e70)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = LogGroupProps(
            data_protection_policy=data_protection_policy,
            encryption_key=encryption_key,
            log_group_name=log_group_name,
            removal_policy=removal_policy,
            retention=retention,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromLogGroupArn")
    @builtins.classmethod
    def from_log_group_arn(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        log_group_arn: builtins.str,
    ) -> ILogGroup:
        '''Import an existing LogGroup given its ARN.

        :param scope: -
        :param id: -
        :param log_group_arn: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94bc59386fc670bf1438201199282e56f015468fe650487225ccaca3ae495cd7)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument log_group_arn", value=log_group_arn, expected_type=type_hints["log_group_arn"])
        return typing.cast(ILogGroup, jsii.sinvoke(cls, "fromLogGroupArn", [scope, id, log_group_arn]))

    @jsii.member(jsii_name="fromLogGroupName")
    @builtins.classmethod
    def from_log_group_name(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        log_group_name: builtins.str,
    ) -> ILogGroup:
        '''Import an existing LogGroup given its name.

        :param scope: -
        :param id: -
        :param log_group_name: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9988695c3237dc33d233c2bca8c1a32b8ca9135d661974af7b593667d7199d2)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument log_group_name", value=log_group_name, expected_type=type_hints["log_group_name"])
        return typing.cast(ILogGroup, jsii.sinvoke(cls, "fromLogGroupName", [scope, id, log_group_name]))

    @jsii.member(jsii_name="addMetricFilter")
    def add_metric_filter(
        self,
        id: builtins.str,
        *,
        filter_pattern: IFilterPattern,
        metric_name: builtins.str,
        metric_namespace: builtins.str,
        default_value: typing.Optional[jsii.Number] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        filter_name: typing.Optional[builtins.str] = None,
        metric_value: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> "MetricFilter":
        '''Create a new Metric Filter on this Log Group.

        :param id: Unique identifier for the construct in its parent.
        :param filter_pattern: Pattern to search for log events.
        :param metric_name: The name of the metric to emit.
        :param metric_namespace: The namespace of the metric to emit.
        :param default_value: The value to emit if the pattern does not match a particular event. Default: No metric emitted.
        :param dimensions: The fields to use as dimensions for the metric. One metric filter can include as many as three dimensions. Default: - No dimensions attached to metrics.
        :param filter_name: The name of the metric filter. Default: - Cloudformation generated name.
        :param metric_value: The value to emit for the metric. Can either be a literal number (typically "1"), or the name of a field in the structure to take the value from the matched event. If you are using a field value, the field value must have been matched using the pattern. If you want to specify a field from a matched JSON structure, use '$.fieldName', and make sure the field is in the pattern (if only as '$.fieldName = *'). If you want to specify a field from a matched space-delimited structure, use '$fieldName'. Default: "1"
        :param unit: The unit to assign to the metric. Default: - No unit attached to metrics.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60bdb647264d5f9edd37cf7e07a8b1cde70ce81f1ebb17eb131efa9d12a73e70)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = MetricFilterOptions(
            filter_pattern=filter_pattern,
            metric_name=metric_name,
            metric_namespace=metric_namespace,
            default_value=default_value,
            dimensions=dimensions,
            filter_name=filter_name,
            metric_value=metric_value,
            unit=unit,
        )

        return typing.cast("MetricFilter", jsii.invoke(self, "addMetricFilter", [id, props]))

    @jsii.member(jsii_name="addStream")
    def add_stream(
        self,
        id: builtins.str,
        *,
        log_stream_name: typing.Optional[builtins.str] = None,
    ) -> "LogStream":
        '''Create a new Log Stream for this Log Group.

        :param id: Unique identifier for the construct in its parent.
        :param log_stream_name: The name of the log stream to create. The name must be unique within the log group. Default: Automatically generated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a24d4a9b6baaaae57b481202eeb591bd2f9c75a23a136632347af1c7954e70d)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = StreamOptions(log_stream_name=log_stream_name)

        return typing.cast("LogStream", jsii.invoke(self, "addStream", [id, props]))

    @jsii.member(jsii_name="addSubscriptionFilter")
    def add_subscription_filter(
        self,
        id: builtins.str,
        *,
        destination: ILogSubscriptionDestination,
        filter_pattern: IFilterPattern,
        filter_name: typing.Optional[builtins.str] = None,
    ) -> "SubscriptionFilter":
        '''Create a new Subscription Filter on this Log Group.

        :param id: Unique identifier for the construct in its parent.
        :param destination: The destination to send the filtered events to. For example, a Kinesis stream or a Lambda function.
        :param filter_pattern: Log events matching this pattern will be sent to the destination.
        :param filter_name: The name of the subscription filter. Default: Automatically generated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a53e1c08918ff12981b248135756d8f20c9acc571a2cab87ee6a3504361564b6)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = SubscriptionFilterOptions(
            destination=destination,
            filter_pattern=filter_pattern,
            filter_name=filter_name,
        )

        return typing.cast("SubscriptionFilter", jsii.invoke(self, "addSubscriptionFilter", [id, props]))

    @jsii.member(jsii_name="addToResourcePolicy")
    def add_to_resource_policy(
        self,
        statement: _PolicyStatement_0fe33853,
    ) -> _AddToResourcePolicyResult_1d0a53ad:
        '''Adds a statement to the resource policy associated with this log group.

        A resource policy will be automatically created upon the first call to ``addToResourcePolicy``.

        Any ARN Principals inside of the statement will be converted into AWS Account ID strings
        because CloudWatch Logs Resource Policies do not accept ARN principals.

        :param statement: The policy statement to add.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f61b70f15ff76b195297fc3fa75909dc7046483a164b76160596773157f547f)
            check_type(argname="argument statement", value=statement, expected_type=type_hints["statement"])
        return typing.cast(_AddToResourcePolicyResult_1d0a53ad, jsii.invoke(self, "addToResourcePolicy", [statement]))

    @jsii.member(jsii_name="extractMetric")
    def extract_metric(
        self,
        json_field: builtins.str,
        metric_namespace: builtins.str,
        metric_name: builtins.str,
    ) -> _Metric_e396a4dc:
        '''Extract a metric from structured log events in the LogGroup.

        Creates a MetricFilter on this LogGroup that will extract the value
        of the indicated JSON field in all records where it occurs.

        The metric will be available in CloudWatch Metrics under the
        indicated namespace and name.

        :param json_field: JSON field to extract (example: '$.myfield').
        :param metric_namespace: Namespace to emit the metric under.
        :param metric_name: Name to emit the metric under.

        :return: A Metric object representing the extracted metric
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fec042a3492600efc8a11c082c58cb34995746a66ce985d97fd5c74ba47f0b96)
            check_type(argname="argument json_field", value=json_field, expected_type=type_hints["json_field"])
            check_type(argname="argument metric_namespace", value=metric_namespace, expected_type=type_hints["metric_namespace"])
            check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "extractMetric", [json_field, metric_namespace, metric_name]))

    @jsii.member(jsii_name="grant")
    def grant(
        self,
        grantee: _IGrantable_71c4f5de,
        *actions: builtins.str,
    ) -> _Grant_a7ae64f8:
        '''Give the indicated permissions on this log group and all streams.

        :param grantee: -
        :param actions: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9a9cb0e1cec11a01408a7a448100c7b05edddf5bb005abd006a834d3c923bb7)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
            check_type(argname="argument actions", value=actions, expected_type=typing.Tuple[type_hints["actions"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grant", [grantee, *actions]))

    @jsii.member(jsii_name="grantRead")
    def grant_read(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Give permissions to read and filter events from this log group.

        :param grantee: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__049a7f93ec71ef52ad5919516c695afd1e3f1185bfaadbf66b872fe23abae4db)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantRead", [grantee]))

    @jsii.member(jsii_name="grantWrite")
    def grant_write(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Give permissions to create and write to streams in this log group.

        :param grantee: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c97b414675dc468df60a1d999b2ddb74ddf42567d0d8ac3af19bb44f4022b1b0)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantWrite", [grantee]))

    @jsii.member(jsii_name="logGroupPhysicalName")
    def log_group_physical_name(self) -> builtins.str:
        '''Public method to get the physical name of this log group.

        :return: Physical name of log group
        '''
        return typing.cast(builtins.str, jsii.invoke(self, "logGroupPhysicalName", []))

    @builtins.property
    @jsii.member(jsii_name="logGroupArn")
    def log_group_arn(self) -> builtins.str:
        '''The ARN of this log group.'''
        return typing.cast(builtins.str, jsii.get(self, "logGroupArn"))

    @builtins.property
    @jsii.member(jsii_name="logGroupName")
    def log_group_name(self) -> builtins.str:
        '''The name of this log group.'''
        return typing.cast(builtins.str, jsii.get(self, "logGroupName"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.LogGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "data_protection_policy": "dataProtectionPolicy",
        "encryption_key": "encryptionKey",
        "log_group_name": "logGroupName",
        "removal_policy": "removalPolicy",
        "retention": "retention",
    },
)
class LogGroupProps:
    def __init__(
        self,
        *,
        data_protection_policy: typing.Optional[DataProtectionPolicy] = None,
        encryption_key: typing.Optional[_IKey_5f11635f] = None,
        log_group_name: typing.Optional[builtins.str] = None,
        removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
        retention: typing.Optional["RetentionDays"] = None,
    ) -> None:
        '''Properties for a LogGroup.

        :param data_protection_policy: Data Protection Policy for this log group. Default: - no data protection policy
        :param encryption_key: The KMS customer managed key to encrypt the log group with. Default: Server-side encrpytion managed by the CloudWatch Logs service
        :param log_group_name: Name of the log group. Default: Automatically generated
        :param removal_policy: Determine the removal policy of this log group. Normally you want to retain the log group so you can diagnose issues from logs even after a deployment that no longer includes the log group. In that case, use the normal date-based retention policy to age out your logs. Default: RemovalPolicy.Retain
        :param retention: How long, in days, the log contents will be retained. To retain all logs, set this value to RetentionDays.INFINITE. Default: RetentionDays.TWO_YEARS

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_kinesisfirehose_alpha as kinesisfirehose
            import aws_cdk.aws_kinesisfirehose_destinations_alpha as destinations
            
            
            log_group_destination = logs.LogGroup(self, "LogGroupLambdaAudit",
                log_group_name="auditDestinationForCDK"
            )
            
            bucket = s3.Bucket(self, "audit-bucket")
            s3_destination = destinations.S3Bucket(bucket)
            
            delivery_stream = kinesisfirehose.DeliveryStream(self, "Delivery Stream",
                destinations=[s3_destination]
            )
            
            data_protection_policy = logs.DataProtectionPolicy(
                name="data protection policy",
                description="policy description",
                identifiers=[logs.DataIdentifier.DRIVERSLICENSE_US, logs.DataIdentifier("EmailAddress")],
                log_group_audit_destination=log_group_destination,
                s3_bucket_audit_destination=bucket,
                delivery_stream_name_audit_destination=delivery_stream.delivery_stream_name
            )
            
            logs.LogGroup(self, "LogGroupLambda",
                log_group_name="cdkIntegLogGroup",
                data_protection_policy=data_protection_policy
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df51a93f7809d59dd37d78a60967e0071dab4876ea1cd5ecd658ac3c8eae1320)
            check_type(argname="argument data_protection_policy", value=data_protection_policy, expected_type=type_hints["data_protection_policy"])
            check_type(argname="argument encryption_key", value=encryption_key, expected_type=type_hints["encryption_key"])
            check_type(argname="argument log_group_name", value=log_group_name, expected_type=type_hints["log_group_name"])
            check_type(argname="argument removal_policy", value=removal_policy, expected_type=type_hints["removal_policy"])
            check_type(argname="argument retention", value=retention, expected_type=type_hints["retention"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if data_protection_policy is not None:
            self._values["data_protection_policy"] = data_protection_policy
        if encryption_key is not None:
            self._values["encryption_key"] = encryption_key
        if log_group_name is not None:
            self._values["log_group_name"] = log_group_name
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy
        if retention is not None:
            self._values["retention"] = retention

    @builtins.property
    def data_protection_policy(self) -> typing.Optional[DataProtectionPolicy]:
        '''Data Protection Policy for this log group.

        :default: - no data protection policy
        '''
        result = self._values.get("data_protection_policy")
        return typing.cast(typing.Optional[DataProtectionPolicy], result)

    @builtins.property
    def encryption_key(self) -> typing.Optional[_IKey_5f11635f]:
        '''The KMS customer managed key to encrypt the log group with.

        :default: Server-side encrpytion managed by the CloudWatch Logs service
        '''
        result = self._values.get("encryption_key")
        return typing.cast(typing.Optional[_IKey_5f11635f], result)

    @builtins.property
    def log_group_name(self) -> typing.Optional[builtins.str]:
        '''Name of the log group.

        :default: Automatically generated
        '''
        result = self._values.get("log_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def removal_policy(self) -> typing.Optional[_RemovalPolicy_9f93c814]:
        '''Determine the removal policy of this log group.

        Normally you want to retain the log group so you can diagnose issues
        from logs even after a deployment that no longer includes the log group.
        In that case, use the normal date-based retention policy to age out your
        logs.

        :default: RemovalPolicy.Retain
        '''
        result = self._values.get("removal_policy")
        return typing.cast(typing.Optional[_RemovalPolicy_9f93c814], result)

    @builtins.property
    def retention(self) -> typing.Optional["RetentionDays"]:
        '''How long, in days, the log contents will be retained.

        To retain all logs, set this value to RetentionDays.INFINITE.

        :default: RetentionDays.TWO_YEARS
        '''
        result = self._values.get("retention")
        return typing.cast(typing.Optional["RetentionDays"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LogRetention(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_logs.LogRetention",
):
    '''Creates a custom resource to control the retention policy of a CloudWatch Logs log group.

    The log group is created if it doesn't already exist. The policy
    is removed when ``retentionDays`` is ``undefined`` or equal to ``Infinity``.
    Log group can be created in the region that is different from stack region by
    specifying ``logGroupRegion``

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk as cdk
        from aws_cdk import aws_iam as iam
        from aws_cdk import aws_logs as logs
        
        # role: iam.Role
        
        log_retention = logs.LogRetention(self, "MyLogRetention",
            log_group_name="logGroupName",
            retention=logs.RetentionDays.ONE_DAY,
        
            # the properties below are optional
            log_group_region="logGroupRegion",
            log_retention_retry_options=logs.LogRetentionRetryOptions(
                base=cdk.Duration.minutes(30),
                max_retries=123
            ),
            removal_policy=cdk.RemovalPolicy.DESTROY,
            role=role
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        log_group_name: builtins.str,
        retention: "RetentionDays",
        log_group_region: typing.Optional[builtins.str] = None,
        log_retention_retry_options: typing.Optional[typing.Union["LogRetentionRetryOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param log_group_name: The log group name.
        :param retention: The number of days log events are kept in CloudWatch Logs.
        :param log_group_region: The region where the log group should be created. Default: - same region as the stack
        :param log_retention_retry_options: Retry options for all AWS API calls. Default: - AWS SDK default retry options
        :param removal_policy: The removalPolicy for the log group when the stack is deleted. Default: RemovalPolicy.RETAIN
        :param role: The IAM role for the Lambda function associated with the custom resource. Default: - A new role is created
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4507613a235a88592d0ebd7d0dbe61f494620068c75fef42db8c09f2dfde8cc)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = LogRetentionProps(
            log_group_name=log_group_name,
            retention=retention,
            log_group_region=log_group_region,
            log_retention_retry_options=log_retention_retry_options,
            removal_policy=removal_policy,
            role=role,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="logGroupArn")
    def log_group_arn(self) -> builtins.str:
        '''The ARN of the LogGroup.'''
        return typing.cast(builtins.str, jsii.get(self, "logGroupArn"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.LogRetentionProps",
    jsii_struct_bases=[],
    name_mapping={
        "log_group_name": "logGroupName",
        "retention": "retention",
        "log_group_region": "logGroupRegion",
        "log_retention_retry_options": "logRetentionRetryOptions",
        "removal_policy": "removalPolicy",
        "role": "role",
    },
)
class LogRetentionProps:
    def __init__(
        self,
        *,
        log_group_name: builtins.str,
        retention: "RetentionDays",
        log_group_region: typing.Optional[builtins.str] = None,
        log_retention_retry_options: typing.Optional[typing.Union["LogRetentionRetryOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
    ) -> None:
        '''Construction properties for a LogRetention.

        :param log_group_name: The log group name.
        :param retention: The number of days log events are kept in CloudWatch Logs.
        :param log_group_region: The region where the log group should be created. Default: - same region as the stack
        :param log_retention_retry_options: Retry options for all AWS API calls. Default: - AWS SDK default retry options
        :param removal_policy: The removalPolicy for the log group when the stack is deleted. Default: RemovalPolicy.RETAIN
        :param role: The IAM role for the Lambda function associated with the custom resource. Default: - A new role is created

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk as cdk
            from aws_cdk import aws_iam as iam
            from aws_cdk import aws_logs as logs
            
            # role: iam.Role
            
            log_retention_props = logs.LogRetentionProps(
                log_group_name="logGroupName",
                retention=logs.RetentionDays.ONE_DAY,
            
                # the properties below are optional
                log_group_region="logGroupRegion",
                log_retention_retry_options=logs.LogRetentionRetryOptions(
                    base=cdk.Duration.minutes(30),
                    max_retries=123
                ),
                removal_policy=cdk.RemovalPolicy.DESTROY,
                role=role
            )
        '''
        if isinstance(log_retention_retry_options, dict):
            log_retention_retry_options = LogRetentionRetryOptions(**log_retention_retry_options)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__318a9234eb28bfd26692eac8fd1ea9c47cedbd175a0dc53714860906302a980b)
            check_type(argname="argument log_group_name", value=log_group_name, expected_type=type_hints["log_group_name"])
            check_type(argname="argument retention", value=retention, expected_type=type_hints["retention"])
            check_type(argname="argument log_group_region", value=log_group_region, expected_type=type_hints["log_group_region"])
            check_type(argname="argument log_retention_retry_options", value=log_retention_retry_options, expected_type=type_hints["log_retention_retry_options"])
            check_type(argname="argument removal_policy", value=removal_policy, expected_type=type_hints["removal_policy"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "log_group_name": log_group_name,
            "retention": retention,
        }
        if log_group_region is not None:
            self._values["log_group_region"] = log_group_region
        if log_retention_retry_options is not None:
            self._values["log_retention_retry_options"] = log_retention_retry_options
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy
        if role is not None:
            self._values["role"] = role

    @builtins.property
    def log_group_name(self) -> builtins.str:
        '''The log group name.'''
        result = self._values.get("log_group_name")
        assert result is not None, "Required property 'log_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def retention(self) -> "RetentionDays":
        '''The number of days log events are kept in CloudWatch Logs.'''
        result = self._values.get("retention")
        assert result is not None, "Required property 'retention' is missing"
        return typing.cast("RetentionDays", result)

    @builtins.property
    def log_group_region(self) -> typing.Optional[builtins.str]:
        '''The region where the log group should be created.

        :default: - same region as the stack
        '''
        result = self._values.get("log_group_region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_retention_retry_options(
        self,
    ) -> typing.Optional["LogRetentionRetryOptions"]:
        '''Retry options for all AWS API calls.

        :default: - AWS SDK default retry options
        '''
        result = self._values.get("log_retention_retry_options")
        return typing.cast(typing.Optional["LogRetentionRetryOptions"], result)

    @builtins.property
    def removal_policy(self) -> typing.Optional[_RemovalPolicy_9f93c814]:
        '''The removalPolicy for the log group when the stack is deleted.

        :default: RemovalPolicy.RETAIN
        '''
        result = self._values.get("removal_policy")
        return typing.cast(typing.Optional[_RemovalPolicy_9f93c814], result)

    @builtins.property
    def role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''The IAM role for the Lambda function associated with the custom resource.

        :default: - A new role is created
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogRetentionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.LogRetentionRetryOptions",
    jsii_struct_bases=[],
    name_mapping={"base": "base", "max_retries": "maxRetries"},
)
class LogRetentionRetryOptions:
    def __init__(
        self,
        *,
        base: typing.Optional[_Duration_4839e8c3] = None,
        max_retries: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Retry options for all AWS API calls.

        :param base: (deprecated) The base duration to use in the exponential backoff for operation retries. Default: - none, not used anymore
        :param max_retries: The maximum amount of retries. Default: 5

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk as cdk
            from aws_cdk import aws_logs as logs
            
            log_retention_retry_options = logs.LogRetentionRetryOptions(
                base=cdk.Duration.minutes(30),
                max_retries=123
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9636a1cfdc99034fff1c4ef9550b1c380d0f51a19f14b506c85c32184b950d42)
            check_type(argname="argument base", value=base, expected_type=type_hints["base"])
            check_type(argname="argument max_retries", value=max_retries, expected_type=type_hints["max_retries"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if base is not None:
            self._values["base"] = base
        if max_retries is not None:
            self._values["max_retries"] = max_retries

    @builtins.property
    def base(self) -> typing.Optional[_Duration_4839e8c3]:
        '''(deprecated) The base duration to use in the exponential backoff for operation retries.

        :default: - none, not used anymore

        :deprecated: Unused since the upgrade to AWS SDK v3, which uses a different retry strategy

        :stability: deprecated
        '''
        result = self._values.get("base")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def max_retries(self) -> typing.Optional[jsii.Number]:
        '''The maximum amount of retries.

        :default: 5
        '''
        result = self._values.get("max_retries")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogRetentionRetryOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(ILogStream)
class LogStream(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_logs.LogStream",
):
    '''Define a Log Stream in a Log Group.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk as cdk
        from aws_cdk import aws_logs as logs
        
        # log_group: logs.LogGroup
        
        log_stream = logs.LogStream(self, "MyLogStream",
            log_group=log_group,
        
            # the properties below are optional
            log_stream_name="logStreamName",
            removal_policy=cdk.RemovalPolicy.DESTROY
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        log_group: ILogGroup,
        log_stream_name: typing.Optional[builtins.str] = None,
        removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param log_group: The log group to create a log stream for.
        :param log_stream_name: The name of the log stream to create. The name must be unique within the log group. Default: Automatically generated
        :param removal_policy: Determine what happens when the log stream resource is removed from the app. Normally you want to retain the log stream so you can diagnose issues from logs even after a deployment that no longer includes the log stream. The date-based retention policy of your log group will age out the logs after a certain time. Default: RemovalPolicy.Retain
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7b310f4ff2940ed4dffa21e4ffde6e0f0bb15bdf93db6bd6d34466158da5c47)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = LogStreamProps(
            log_group=log_group,
            log_stream_name=log_stream_name,
            removal_policy=removal_policy,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromLogStreamName")
    @builtins.classmethod
    def from_log_stream_name(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        log_stream_name: builtins.str,
    ) -> ILogStream:
        '''Import an existing LogGroup.

        :param scope: -
        :param id: -
        :param log_stream_name: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c90257c192f43807c3ca64b0dfd7f0d8f24a0e76af49b59d49ef0b271d7e85a0)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument log_stream_name", value=log_stream_name, expected_type=type_hints["log_stream_name"])
        return typing.cast(ILogStream, jsii.sinvoke(cls, "fromLogStreamName", [scope, id, log_stream_name]))

    @builtins.property
    @jsii.member(jsii_name="logStreamName")
    def log_stream_name(self) -> builtins.str:
        '''The name of this log stream.'''
        return typing.cast(builtins.str, jsii.get(self, "logStreamName"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.LogStreamProps",
    jsii_struct_bases=[],
    name_mapping={
        "log_group": "logGroup",
        "log_stream_name": "logStreamName",
        "removal_policy": "removalPolicy",
    },
)
class LogStreamProps:
    def __init__(
        self,
        *,
        log_group: ILogGroup,
        log_stream_name: typing.Optional[builtins.str] = None,
        removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    ) -> None:
        '''Properties for a LogStream.

        :param log_group: The log group to create a log stream for.
        :param log_stream_name: The name of the log stream to create. The name must be unique within the log group. Default: Automatically generated
        :param removal_policy: Determine what happens when the log stream resource is removed from the app. Normally you want to retain the log stream so you can diagnose issues from logs even after a deployment that no longer includes the log stream. The date-based retention policy of your log group will age out the logs after a certain time. Default: RemovalPolicy.Retain

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk as cdk
            from aws_cdk import aws_logs as logs
            
            # log_group: logs.LogGroup
            
            log_stream_props = logs.LogStreamProps(
                log_group=log_group,
            
                # the properties below are optional
                log_stream_name="logStreamName",
                removal_policy=cdk.RemovalPolicy.DESTROY
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f49a14f2b0eea132d7cea27db911c1bac5a2370d8c93686afb12d7bf18544ca)
            check_type(argname="argument log_group", value=log_group, expected_type=type_hints["log_group"])
            check_type(argname="argument log_stream_name", value=log_stream_name, expected_type=type_hints["log_stream_name"])
            check_type(argname="argument removal_policy", value=removal_policy, expected_type=type_hints["removal_policy"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "log_group": log_group,
        }
        if log_stream_name is not None:
            self._values["log_stream_name"] = log_stream_name
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy

    @builtins.property
    def log_group(self) -> ILogGroup:
        '''The log group to create a log stream for.'''
        result = self._values.get("log_group")
        assert result is not None, "Required property 'log_group' is missing"
        return typing.cast(ILogGroup, result)

    @builtins.property
    def log_stream_name(self) -> typing.Optional[builtins.str]:
        '''The name of the log stream to create.

        The name must be unique within the log group.

        :default: Automatically generated
        '''
        result = self._values.get("log_stream_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def removal_policy(self) -> typing.Optional[_RemovalPolicy_9f93c814]:
        '''Determine what happens when the log stream resource is removed from the app.

        Normally you want to retain the log stream so you can diagnose issues from
        logs even after a deployment that no longer includes the log stream.

        The date-based retention policy of your log group will age out the logs
        after a certain time.

        :default: RemovalPolicy.Retain
        '''
        result = self._values.get("removal_policy")
        return typing.cast(typing.Optional[_RemovalPolicy_9f93c814], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogStreamProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.LogSubscriptionDestinationConfig",
    jsii_struct_bases=[],
    name_mapping={"arn": "arn", "role": "role"},
)
class LogSubscriptionDestinationConfig:
    def __init__(
        self,
        *,
        arn: builtins.str,
        role: typing.Optional[_IRole_235f5d8e] = None,
    ) -> None:
        '''Properties returned by a Subscription destination.

        :param arn: The ARN of the subscription's destination.
        :param role: The role to assume to write log events to the destination. Default: No role assumed

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iam as iam
            from aws_cdk import aws_logs as logs
            
            # role: iam.Role
            
            log_subscription_destination_config = logs.LogSubscriptionDestinationConfig(
                arn="arn",
            
                # the properties below are optional
                role=role
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__396d59c2514d8bfe65a7a6f818257b42d5f5c9b200fa30ed27db93bc6e8328e0)
            check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "arn": arn,
        }
        if role is not None:
            self._values["role"] = role

    @builtins.property
    def arn(self) -> builtins.str:
        '''The ARN of the subscription's destination.'''
        result = self._values.get("arn")
        assert result is not None, "Required property 'arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''The role to assume to write log events to the destination.

        :default: No role assumed
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogSubscriptionDestinationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MetricFilter(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_logs.MetricFilter",
):
    '''A filter that extracts information from CloudWatch Logs and emits to CloudWatch Metrics.

    :exampleMetadata: lit=aws-logs/test/integ.metricfilter.lit.ts infused

    Example::

        MetricFilter(self, "MetricFilter",
            log_group=log_group,
            metric_namespace="MyApp",
            metric_name="Latency",
            filter_pattern=FilterPattern.exists("$.latency"),
            metric_value="$.latency"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        log_group: ILogGroup,
        filter_pattern: IFilterPattern,
        metric_name: builtins.str,
        metric_namespace: builtins.str,
        default_value: typing.Optional[jsii.Number] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        filter_name: typing.Optional[builtins.str] = None,
        metric_value: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param log_group: The log group to create the filter on.
        :param filter_pattern: Pattern to search for log events.
        :param metric_name: The name of the metric to emit.
        :param metric_namespace: The namespace of the metric to emit.
        :param default_value: The value to emit if the pattern does not match a particular event. Default: No metric emitted.
        :param dimensions: The fields to use as dimensions for the metric. One metric filter can include as many as three dimensions. Default: - No dimensions attached to metrics.
        :param filter_name: The name of the metric filter. Default: - Cloudformation generated name.
        :param metric_value: The value to emit for the metric. Can either be a literal number (typically "1"), or the name of a field in the structure to take the value from the matched event. If you are using a field value, the field value must have been matched using the pattern. If you want to specify a field from a matched JSON structure, use '$.fieldName', and make sure the field is in the pattern (if only as '$.fieldName = *'). If you want to specify a field from a matched space-delimited structure, use '$fieldName'. Default: "1"
        :param unit: The unit to assign to the metric. Default: - No unit attached to metrics.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d62ba20acf6180e35fd081efe9f21747bf2bd8765dd3a4a5c41cc0f41f079a1)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = MetricFilterProps(
            log_group=log_group,
            filter_pattern=filter_pattern,
            metric_name=metric_name,
            metric_namespace=metric_namespace,
            default_value=default_value,
            dimensions=dimensions,
            filter_name=filter_name,
            metric_value=metric_value,
            unit=unit,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="metric")
    def metric(
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
        '''Return the given named metric for this Metric Filter.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: avg over 5 minutes
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

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metric", [props]))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.MetricFilterOptions",
    jsii_struct_bases=[],
    name_mapping={
        "filter_pattern": "filterPattern",
        "metric_name": "metricName",
        "metric_namespace": "metricNamespace",
        "default_value": "defaultValue",
        "dimensions": "dimensions",
        "filter_name": "filterName",
        "metric_value": "metricValue",
        "unit": "unit",
    },
)
class MetricFilterOptions:
    def __init__(
        self,
        *,
        filter_pattern: IFilterPattern,
        metric_name: builtins.str,
        metric_namespace: builtins.str,
        default_value: typing.Optional[jsii.Number] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        filter_name: typing.Optional[builtins.str] = None,
        metric_value: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> None:
        '''Properties for a MetricFilter created from a LogGroup.

        :param filter_pattern: Pattern to search for log events.
        :param metric_name: The name of the metric to emit.
        :param metric_namespace: The namespace of the metric to emit.
        :param default_value: The value to emit if the pattern does not match a particular event. Default: No metric emitted.
        :param dimensions: The fields to use as dimensions for the metric. One metric filter can include as many as three dimensions. Default: - No dimensions attached to metrics.
        :param filter_name: The name of the metric filter. Default: - Cloudformation generated name.
        :param metric_value: The value to emit for the metric. Can either be a literal number (typically "1"), or the name of a field in the structure to take the value from the matched event. If you are using a field value, the field value must have been matched using the pattern. If you want to specify a field from a matched JSON structure, use '$.fieldName', and make sure the field is in the pattern (if only as '$.fieldName = *'). If you want to specify a field from a matched space-delimited structure, use '$fieldName'. Default: "1"
        :param unit: The unit to assign to the metric. Default: - No unit attached to metrics.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cloudwatch as cloudwatch
            from aws_cdk import aws_logs as logs
            
            # filter_pattern: logs.IFilterPattern
            
            metric_filter_options = logs.MetricFilterOptions(
                filter_pattern=filter_pattern,
                metric_name="metricName",
                metric_namespace="metricNamespace",
            
                # the properties below are optional
                default_value=123,
                dimensions={
                    "dimensions_key": "dimensions"
                },
                filter_name="filterName",
                metric_value="metricValue",
                unit=cloudwatch.Unit.SECONDS
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5bb9c8220568f1b3f6adf2d20dcfde3ada18ce4351110a49b3a0707812e51fe)
            check_type(argname="argument filter_pattern", value=filter_pattern, expected_type=type_hints["filter_pattern"])
            check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
            check_type(argname="argument metric_namespace", value=metric_namespace, expected_type=type_hints["metric_namespace"])
            check_type(argname="argument default_value", value=default_value, expected_type=type_hints["default_value"])
            check_type(argname="argument dimensions", value=dimensions, expected_type=type_hints["dimensions"])
            check_type(argname="argument filter_name", value=filter_name, expected_type=type_hints["filter_name"])
            check_type(argname="argument metric_value", value=metric_value, expected_type=type_hints["metric_value"])
            check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "filter_pattern": filter_pattern,
            "metric_name": metric_name,
            "metric_namespace": metric_namespace,
        }
        if default_value is not None:
            self._values["default_value"] = default_value
        if dimensions is not None:
            self._values["dimensions"] = dimensions
        if filter_name is not None:
            self._values["filter_name"] = filter_name
        if metric_value is not None:
            self._values["metric_value"] = metric_value
        if unit is not None:
            self._values["unit"] = unit

    @builtins.property
    def filter_pattern(self) -> IFilterPattern:
        '''Pattern to search for log events.'''
        result = self._values.get("filter_pattern")
        assert result is not None, "Required property 'filter_pattern' is missing"
        return typing.cast(IFilterPattern, result)

    @builtins.property
    def metric_name(self) -> builtins.str:
        '''The name of the metric to emit.'''
        result = self._values.get("metric_name")
        assert result is not None, "Required property 'metric_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def metric_namespace(self) -> builtins.str:
        '''The namespace of the metric to emit.'''
        result = self._values.get("metric_namespace")
        assert result is not None, "Required property 'metric_namespace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def default_value(self) -> typing.Optional[jsii.Number]:
        '''The value to emit if the pattern does not match a particular event.

        :default: No metric emitted.
        '''
        result = self._values.get("default_value")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def dimensions(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The fields to use as dimensions for the metric.

        One metric filter can include as many as three dimensions.

        :default: - No dimensions attached to metrics.

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-metricfilter-metrictransformation.html#cfn-logs-metricfilter-metrictransformation-dimensions
        '''
        result = self._values.get("dimensions")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def filter_name(self) -> typing.Optional[builtins.str]:
        '''The name of the metric filter.

        :default: - Cloudformation generated name.
        '''
        result = self._values.get("filter_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def metric_value(self) -> typing.Optional[builtins.str]:
        '''The value to emit for the metric.

        Can either be a literal number (typically "1"), or the name of a field in the structure
        to take the value from the matched event. If you are using a field value, the field
        value must have been matched using the pattern.

        If you want to specify a field from a matched JSON structure, use '$.fieldName',
        and make sure the field is in the pattern (if only as '$.fieldName = *').

        If you want to specify a field from a matched space-delimited structure,
        use '$fieldName'.

        :default: "1"
        '''
        result = self._values.get("metric_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def unit(self) -> typing.Optional[_Unit_61bc6f70]:
        '''The unit to assign to the metric.

        :default: - No unit attached to metrics.

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-metricfilter-metrictransformation.html#cfn-logs-metricfilter-metrictransformation-unit
        '''
        result = self._values.get("unit")
        return typing.cast(typing.Optional[_Unit_61bc6f70], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MetricFilterOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.MetricFilterProps",
    jsii_struct_bases=[MetricFilterOptions],
    name_mapping={
        "filter_pattern": "filterPattern",
        "metric_name": "metricName",
        "metric_namespace": "metricNamespace",
        "default_value": "defaultValue",
        "dimensions": "dimensions",
        "filter_name": "filterName",
        "metric_value": "metricValue",
        "unit": "unit",
        "log_group": "logGroup",
    },
)
class MetricFilterProps(MetricFilterOptions):
    def __init__(
        self,
        *,
        filter_pattern: IFilterPattern,
        metric_name: builtins.str,
        metric_namespace: builtins.str,
        default_value: typing.Optional[jsii.Number] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        filter_name: typing.Optional[builtins.str] = None,
        metric_value: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
        log_group: ILogGroup,
    ) -> None:
        '''Properties for a MetricFilter.

        :param filter_pattern: Pattern to search for log events.
        :param metric_name: The name of the metric to emit.
        :param metric_namespace: The namespace of the metric to emit.
        :param default_value: The value to emit if the pattern does not match a particular event. Default: No metric emitted.
        :param dimensions: The fields to use as dimensions for the metric. One metric filter can include as many as three dimensions. Default: - No dimensions attached to metrics.
        :param filter_name: The name of the metric filter. Default: - Cloudformation generated name.
        :param metric_value: The value to emit for the metric. Can either be a literal number (typically "1"), or the name of a field in the structure to take the value from the matched event. If you are using a field value, the field value must have been matched using the pattern. If you want to specify a field from a matched JSON structure, use '$.fieldName', and make sure the field is in the pattern (if only as '$.fieldName = *'). If you want to specify a field from a matched space-delimited structure, use '$fieldName'. Default: "1"
        :param unit: The unit to assign to the metric. Default: - No unit attached to metrics.
        :param log_group: The log group to create the filter on.

        :exampleMetadata: lit=aws-logs/test/integ.metricfilter.lit.ts infused

        Example::

            MetricFilter(self, "MetricFilter",
                log_group=log_group,
                metric_namespace="MyApp",
                metric_name="Latency",
                filter_pattern=FilterPattern.exists("$.latency"),
                metric_value="$.latency"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66722f3b881a30b7ce1b9efa7c76f2539915abe8fe84a770e1e2c47657d59d79)
            check_type(argname="argument filter_pattern", value=filter_pattern, expected_type=type_hints["filter_pattern"])
            check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
            check_type(argname="argument metric_namespace", value=metric_namespace, expected_type=type_hints["metric_namespace"])
            check_type(argname="argument default_value", value=default_value, expected_type=type_hints["default_value"])
            check_type(argname="argument dimensions", value=dimensions, expected_type=type_hints["dimensions"])
            check_type(argname="argument filter_name", value=filter_name, expected_type=type_hints["filter_name"])
            check_type(argname="argument metric_value", value=metric_value, expected_type=type_hints["metric_value"])
            check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
            check_type(argname="argument log_group", value=log_group, expected_type=type_hints["log_group"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "filter_pattern": filter_pattern,
            "metric_name": metric_name,
            "metric_namespace": metric_namespace,
            "log_group": log_group,
        }
        if default_value is not None:
            self._values["default_value"] = default_value
        if dimensions is not None:
            self._values["dimensions"] = dimensions
        if filter_name is not None:
            self._values["filter_name"] = filter_name
        if metric_value is not None:
            self._values["metric_value"] = metric_value
        if unit is not None:
            self._values["unit"] = unit

    @builtins.property
    def filter_pattern(self) -> IFilterPattern:
        '''Pattern to search for log events.'''
        result = self._values.get("filter_pattern")
        assert result is not None, "Required property 'filter_pattern' is missing"
        return typing.cast(IFilterPattern, result)

    @builtins.property
    def metric_name(self) -> builtins.str:
        '''The name of the metric to emit.'''
        result = self._values.get("metric_name")
        assert result is not None, "Required property 'metric_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def metric_namespace(self) -> builtins.str:
        '''The namespace of the metric to emit.'''
        result = self._values.get("metric_namespace")
        assert result is not None, "Required property 'metric_namespace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def default_value(self) -> typing.Optional[jsii.Number]:
        '''The value to emit if the pattern does not match a particular event.

        :default: No metric emitted.
        '''
        result = self._values.get("default_value")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def dimensions(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The fields to use as dimensions for the metric.

        One metric filter can include as many as three dimensions.

        :default: - No dimensions attached to metrics.

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-metricfilter-metrictransformation.html#cfn-logs-metricfilter-metrictransformation-dimensions
        '''
        result = self._values.get("dimensions")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def filter_name(self) -> typing.Optional[builtins.str]:
        '''The name of the metric filter.

        :default: - Cloudformation generated name.
        '''
        result = self._values.get("filter_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def metric_value(self) -> typing.Optional[builtins.str]:
        '''The value to emit for the metric.

        Can either be a literal number (typically "1"), or the name of a field in the structure
        to take the value from the matched event. If you are using a field value, the field
        value must have been matched using the pattern.

        If you want to specify a field from a matched JSON structure, use '$.fieldName',
        and make sure the field is in the pattern (if only as '$.fieldName = *').

        If you want to specify a field from a matched space-delimited structure,
        use '$fieldName'.

        :default: "1"
        '''
        result = self._values.get("metric_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def unit(self) -> typing.Optional[_Unit_61bc6f70]:
        '''The unit to assign to the metric.

        :default: - No unit attached to metrics.

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-metricfilter-metrictransformation.html#cfn-logs-metricfilter-metrictransformation-unit
        '''
        result = self._values.get("unit")
        return typing.cast(typing.Optional[_Unit_61bc6f70], result)

    @builtins.property
    def log_group(self) -> ILogGroup:
        '''The log group to create the filter on.'''
        result = self._values.get("log_group")
        assert result is not None, "Required property 'log_group' is missing"
        return typing.cast(ILogGroup, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MetricFilterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class QueryDefinition(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_logs.QueryDefinition",
):
    '''Define a query definition for CloudWatch Logs Insights.

    :exampleMetadata: infused

    Example::

        logs.QueryDefinition(self, "QueryDefinition",
            query_definition_name="MyQuery",
            query_string=logs.QueryString(
                fields=["@timestamp", "@message"],
                parse_statements=["@message \"[*] *\" as loggingType, loggingMessage", "@message \"<*>: *\" as differentLoggingType, differentLoggingMessage"
                ],
                filter_statements=["loggingType = \"ERROR\"", "loggingMessage = \"A very strange error occurred!\""
                ],
                sort="@timestamp desc",
                limit=20
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        query_definition_name: builtins.str,
        query_string: "QueryString",
        log_groups: typing.Optional[typing.Sequence[ILogGroup]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param query_definition_name: Name of the query definition.
        :param query_string: The query string to use for this query definition.
        :param log_groups: Specify certain log groups for the query definition. Default: - no specified log groups
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f7cb87fa9a91fccd75052278e9031242b20cab41bb53f8f18544b867e01e5d41)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = QueryDefinitionProps(
            query_definition_name=query_definition_name,
            query_string=query_string,
            log_groups=log_groups,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="queryDefinitionId")
    def query_definition_id(self) -> builtins.str:
        '''The ID of the query definition.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "queryDefinitionId"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.QueryDefinitionProps",
    jsii_struct_bases=[],
    name_mapping={
        "query_definition_name": "queryDefinitionName",
        "query_string": "queryString",
        "log_groups": "logGroups",
    },
)
class QueryDefinitionProps:
    def __init__(
        self,
        *,
        query_definition_name: builtins.str,
        query_string: "QueryString",
        log_groups: typing.Optional[typing.Sequence[ILogGroup]] = None,
    ) -> None:
        '''Properties for a QueryDefinition.

        :param query_definition_name: Name of the query definition.
        :param query_string: The query string to use for this query definition.
        :param log_groups: Specify certain log groups for the query definition. Default: - no specified log groups

        :exampleMetadata: infused

        Example::

            logs.QueryDefinition(self, "QueryDefinition",
                query_definition_name="MyQuery",
                query_string=logs.QueryString(
                    fields=["@timestamp", "@message"],
                    parse_statements=["@message \"[*] *\" as loggingType, loggingMessage", "@message \"<*>: *\" as differentLoggingType, differentLoggingMessage"
                    ],
                    filter_statements=["loggingType = \"ERROR\"", "loggingMessage = \"A very strange error occurred!\""
                    ],
                    sort="@timestamp desc",
                    limit=20
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__993712107c64f2acd19761e2b930e6e052534d1100257989bcf307bb6168b668)
            check_type(argname="argument query_definition_name", value=query_definition_name, expected_type=type_hints["query_definition_name"])
            check_type(argname="argument query_string", value=query_string, expected_type=type_hints["query_string"])
            check_type(argname="argument log_groups", value=log_groups, expected_type=type_hints["log_groups"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "query_definition_name": query_definition_name,
            "query_string": query_string,
        }
        if log_groups is not None:
            self._values["log_groups"] = log_groups

    @builtins.property
    def query_definition_name(self) -> builtins.str:
        '''Name of the query definition.'''
        result = self._values.get("query_definition_name")
        assert result is not None, "Required property 'query_definition_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def query_string(self) -> "QueryString":
        '''The query string to use for this query definition.'''
        result = self._values.get("query_string")
        assert result is not None, "Required property 'query_string' is missing"
        return typing.cast("QueryString", result)

    @builtins.property
    def log_groups(self) -> typing.Optional[typing.List[ILogGroup]]:
        '''Specify certain log groups for the query definition.

        :default: - no specified log groups
        '''
        result = self._values.get("log_groups")
        return typing.cast(typing.Optional[typing.List[ILogGroup]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "QueryDefinitionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class QueryString(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_logs.QueryString",
):
    '''Define a QueryString.

    :exampleMetadata: infused

    Example::

        logs.QueryDefinition(self, "QueryDefinition",
            query_definition_name="MyQuery",
            query_string=logs.QueryString(
                fields=["@timestamp", "@message"],
                parse_statements=["@message \"[*] *\" as loggingType, loggingMessage", "@message \"<*>: *\" as differentLoggingType, differentLoggingMessage"
                ],
                filter_statements=["loggingType = \"ERROR\"", "loggingMessage = \"A very strange error occurred!\""
                ],
                sort="@timestamp desc",
                limit=20
            )
        )
    '''

    def __init__(
        self,
        *,
        display: typing.Optional[builtins.str] = None,
        fields: typing.Optional[typing.Sequence[builtins.str]] = None,
        filter: typing.Optional[builtins.str] = None,
        filter_statements: typing.Optional[typing.Sequence[builtins.str]] = None,
        limit: typing.Optional[jsii.Number] = None,
        parse: typing.Optional[builtins.str] = None,
        parse_statements: typing.Optional[typing.Sequence[builtins.str]] = None,
        sort: typing.Optional[builtins.str] = None,
        stats: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param display: Specifies which fields to display in the query results. Default: - no display in QueryString
        :param fields: Retrieves the specified fields from log events for display. Default: - no fields in QueryString
        :param filter: (deprecated) A single statement for filtering the results of a query based on a boolean expression. Default: - no filter in QueryString
        :param filter_statements: An array of one or more statements for filtering the results of a query based on a boolean expression. Each provided statement generates a separate filter line in the query string. Note: If provided, this property overrides any value provided for the ``filter`` property. Default: - no filter in QueryString
        :param limit: Specifies the number of log events returned by the query. Default: - no limit in QueryString
        :param parse: (deprecated) A single statement for parsing data from a log field and creating ephemeral fields that can be processed further in the query. Default: - no parse in QueryString
        :param parse_statements: An array of one or more statements for parsing data from a log field and creating ephemeral fields that can be processed further in the query. Each provided statement generates a separate parse line in the query string. Note: If provided, this property overrides any value provided for the ``parse`` property. Default: - no parse in QueryString
        :param sort: Sorts the retrieved log events. Default: - no sort in QueryString
        :param stats: Uses log field values to calculate aggregate statistics. Default: - no stats in QueryString
        '''
        props = QueryStringProps(
            display=display,
            fields=fields,
            filter=filter,
            filter_statements=filter_statements,
            limit=limit,
            parse=parse,
            parse_statements=parse_statements,
            sort=sort,
            stats=stats,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        '''String representation of this QueryString.'''
        return typing.cast(builtins.str, jsii.invoke(self, "toString", []))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.QueryStringProps",
    jsii_struct_bases=[],
    name_mapping={
        "display": "display",
        "fields": "fields",
        "filter": "filter",
        "filter_statements": "filterStatements",
        "limit": "limit",
        "parse": "parse",
        "parse_statements": "parseStatements",
        "sort": "sort",
        "stats": "stats",
    },
)
class QueryStringProps:
    def __init__(
        self,
        *,
        display: typing.Optional[builtins.str] = None,
        fields: typing.Optional[typing.Sequence[builtins.str]] = None,
        filter: typing.Optional[builtins.str] = None,
        filter_statements: typing.Optional[typing.Sequence[builtins.str]] = None,
        limit: typing.Optional[jsii.Number] = None,
        parse: typing.Optional[builtins.str] = None,
        parse_statements: typing.Optional[typing.Sequence[builtins.str]] = None,
        sort: typing.Optional[builtins.str] = None,
        stats: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for a QueryString.

        :param display: Specifies which fields to display in the query results. Default: - no display in QueryString
        :param fields: Retrieves the specified fields from log events for display. Default: - no fields in QueryString
        :param filter: (deprecated) A single statement for filtering the results of a query based on a boolean expression. Default: - no filter in QueryString
        :param filter_statements: An array of one or more statements for filtering the results of a query based on a boolean expression. Each provided statement generates a separate filter line in the query string. Note: If provided, this property overrides any value provided for the ``filter`` property. Default: - no filter in QueryString
        :param limit: Specifies the number of log events returned by the query. Default: - no limit in QueryString
        :param parse: (deprecated) A single statement for parsing data from a log field and creating ephemeral fields that can be processed further in the query. Default: - no parse in QueryString
        :param parse_statements: An array of one or more statements for parsing data from a log field and creating ephemeral fields that can be processed further in the query. Each provided statement generates a separate parse line in the query string. Note: If provided, this property overrides any value provided for the ``parse`` property. Default: - no parse in QueryString
        :param sort: Sorts the retrieved log events. Default: - no sort in QueryString
        :param stats: Uses log field values to calculate aggregate statistics. Default: - no stats in QueryString

        :exampleMetadata: infused

        Example::

            logs.QueryDefinition(self, "QueryDefinition",
                query_definition_name="MyQuery",
                query_string=logs.QueryString(
                    fields=["@timestamp", "@message"],
                    parse_statements=["@message \"[*] *\" as loggingType, loggingMessage", "@message \"<*>: *\" as differentLoggingType, differentLoggingMessage"
                    ],
                    filter_statements=["loggingType = \"ERROR\"", "loggingMessage = \"A very strange error occurred!\""
                    ],
                    sort="@timestamp desc",
                    limit=20
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d205eb2ac9b46de0083e3387b95b00f2362e2ade91d5c581e5d8cde68293b28d)
            check_type(argname="argument display", value=display, expected_type=type_hints["display"])
            check_type(argname="argument fields", value=fields, expected_type=type_hints["fields"])
            check_type(argname="argument filter", value=filter, expected_type=type_hints["filter"])
            check_type(argname="argument filter_statements", value=filter_statements, expected_type=type_hints["filter_statements"])
            check_type(argname="argument limit", value=limit, expected_type=type_hints["limit"])
            check_type(argname="argument parse", value=parse, expected_type=type_hints["parse"])
            check_type(argname="argument parse_statements", value=parse_statements, expected_type=type_hints["parse_statements"])
            check_type(argname="argument sort", value=sort, expected_type=type_hints["sort"])
            check_type(argname="argument stats", value=stats, expected_type=type_hints["stats"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if display is not None:
            self._values["display"] = display
        if fields is not None:
            self._values["fields"] = fields
        if filter is not None:
            self._values["filter"] = filter
        if filter_statements is not None:
            self._values["filter_statements"] = filter_statements
        if limit is not None:
            self._values["limit"] = limit
        if parse is not None:
            self._values["parse"] = parse
        if parse_statements is not None:
            self._values["parse_statements"] = parse_statements
        if sort is not None:
            self._values["sort"] = sort
        if stats is not None:
            self._values["stats"] = stats

    @builtins.property
    def display(self) -> typing.Optional[builtins.str]:
        '''Specifies which fields to display in the query results.

        :default: - no display in QueryString
        '''
        result = self._values.get("display")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def fields(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Retrieves the specified fields from log events for display.

        :default: - no fields in QueryString
        '''
        result = self._values.get("fields")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def filter(self) -> typing.Optional[builtins.str]:
        '''(deprecated) A single statement for filtering the results of a query based on a boolean expression.

        :default: - no filter in QueryString

        :deprecated: Use ``filterStatements`` instead

        :stability: deprecated
        '''
        result = self._values.get("filter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def filter_statements(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of one or more statements for filtering the results of a query based on a boolean expression.

        Each provided statement generates a separate filter line in the query string.

        Note: If provided, this property overrides any value provided for the ``filter`` property.

        :default: - no filter in QueryString
        '''
        result = self._values.get("filter_statements")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def limit(self) -> typing.Optional[jsii.Number]:
        '''Specifies the number of log events returned by the query.

        :default: - no limit in QueryString
        '''
        result = self._values.get("limit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def parse(self) -> typing.Optional[builtins.str]:
        '''(deprecated) A single statement for parsing data from a log field and creating ephemeral fields that can be processed further in the query.

        :default: - no parse in QueryString

        :deprecated: Use ``parseStatements`` instead

        :stability: deprecated
        '''
        result = self._values.get("parse")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parse_statements(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of one or more statements for parsing data from a log field and creating ephemeral fields that can be processed further in the query.

        Each provided statement generates a separate
        parse line in the query string.

        Note: If provided, this property overrides any value provided for the ``parse`` property.

        :default: - no parse in QueryString
        '''
        result = self._values.get("parse_statements")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def sort(self) -> typing.Optional[builtins.str]:
        '''Sorts the retrieved log events.

        :default: - no sort in QueryString
        '''
        result = self._values.get("sort")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def stats(self) -> typing.Optional[builtins.str]:
        '''Uses log field values to calculate aggregate statistics.

        :default: - no stats in QueryString
        '''
        result = self._values.get("stats")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "QueryStringProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ResourcePolicy(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_logs.ResourcePolicy",
):
    '''Resource Policy for CloudWatch Log Groups.

    Policies define the operations that are allowed on this resource.

    You almost never need to define this construct directly.

    All AWS resources that support resource policies have a method called
    ``addToResourcePolicy()``, which will automatically create a new resource
    policy if one doesn't exist yet, otherwise it will add to the existing
    policy.

    Prefer to use ``addToResourcePolicy()`` instead.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iam as iam
        from aws_cdk import aws_logs as logs
        
        # policy_statement: iam.PolicyStatement
        
        resource_policy = logs.ResourcePolicy(self, "MyResourcePolicy",
            policy_statements=[policy_statement],
            resource_policy_name="resourcePolicyName"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        policy_statements: typing.Optional[typing.Sequence[_PolicyStatement_0fe33853]] = None,
        resource_policy_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param policy_statements: Initial statements to add to the resource policy. Default: - No statements
        :param resource_policy_name: Name of the log group resource policy. Default: - Uses a unique id based on the construct path
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__772b118f71acb9e446b4948b9aac7bf360262cdeddc09c1f28708795cdb48c74)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ResourcePolicyProps(
            policy_statements=policy_statements,
            resource_policy_name=resource_policy_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="document")
    def document(self) -> _PolicyDocument_3ac34393:
        '''The IAM policy document for this resource policy.'''
        return typing.cast(_PolicyDocument_3ac34393, jsii.get(self, "document"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.ResourcePolicyProps",
    jsii_struct_bases=[],
    name_mapping={
        "policy_statements": "policyStatements",
        "resource_policy_name": "resourcePolicyName",
    },
)
class ResourcePolicyProps:
    def __init__(
        self,
        *,
        policy_statements: typing.Optional[typing.Sequence[_PolicyStatement_0fe33853]] = None,
        resource_policy_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties to define Cloudwatch log group resource policy.

        :param policy_statements: Initial statements to add to the resource policy. Default: - No statements
        :param resource_policy_name: Name of the log group resource policy. Default: - Uses a unique id based on the construct path

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iam as iam
            from aws_cdk import aws_logs as logs
            
            # policy_statement: iam.PolicyStatement
            
            resource_policy_props = logs.ResourcePolicyProps(
                policy_statements=[policy_statement],
                resource_policy_name="resourcePolicyName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4f5108e8fcf5bafe964b9be836229eed1f4ac734a83be621801cd6304143286)
            check_type(argname="argument policy_statements", value=policy_statements, expected_type=type_hints["policy_statements"])
            check_type(argname="argument resource_policy_name", value=resource_policy_name, expected_type=type_hints["resource_policy_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if policy_statements is not None:
            self._values["policy_statements"] = policy_statements
        if resource_policy_name is not None:
            self._values["resource_policy_name"] = resource_policy_name

    @builtins.property
    def policy_statements(
        self,
    ) -> typing.Optional[typing.List[_PolicyStatement_0fe33853]]:
        '''Initial statements to add to the resource policy.

        :default: - No statements
        '''
        result = self._values.get("policy_statements")
        return typing.cast(typing.Optional[typing.List[_PolicyStatement_0fe33853]], result)

    @builtins.property
    def resource_policy_name(self) -> typing.Optional[builtins.str]:
        '''Name of the log group resource policy.

        :default: - Uses a unique id based on the construct path
        '''
        result = self._values.get("resource_policy_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ResourcePolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_logs.RetentionDays")
class RetentionDays(enum.Enum):
    '''How long, in days, the log contents will be retained.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_logs as logs
        # my_logs_publishing_role: iam.Role
        # vpc: ec2.Vpc
        
        
        # Exporting logs from a cluster
        cluster = rds.DatabaseCluster(self, "Database",
            engine=rds.DatabaseClusterEngine.aurora(
                version=rds.AuroraEngineVersion.VER_1_17_9
            ),
            writer=rds.ClusterInstance.provisioned("writer"),
            vpc=vpc,
            cloudwatch_logs_exports=["error", "general", "slowquery", "audit"],  # Export all available MySQL-based logs
            cloudwatch_logs_retention=logs.RetentionDays.THREE_MONTHS,  # Optional - default is to never expire logs
            cloudwatch_logs_retention_role=my_logs_publishing_role
        )
        
        # Exporting logs from an instance
        instance = rds.DatabaseInstance(self, "Instance",
            engine=rds.DatabaseInstanceEngine.postgres(
                version=rds.PostgresEngineVersion.VER_15_2
            ),
            vpc=vpc,
            cloudwatch_logs_exports=["postgresql"]
        )
    '''

    ONE_DAY = "ONE_DAY"
    '''1 day.'''
    THREE_DAYS = "THREE_DAYS"
    '''3 days.'''
    FIVE_DAYS = "FIVE_DAYS"
    '''5 days.'''
    ONE_WEEK = "ONE_WEEK"
    '''1 week.'''
    TWO_WEEKS = "TWO_WEEKS"
    '''2 weeks.'''
    ONE_MONTH = "ONE_MONTH"
    '''1 month.'''
    TWO_MONTHS = "TWO_MONTHS"
    '''2 months.'''
    THREE_MONTHS = "THREE_MONTHS"
    '''3 months.'''
    FOUR_MONTHS = "FOUR_MONTHS"
    '''4 months.'''
    FIVE_MONTHS = "FIVE_MONTHS"
    '''5 months.'''
    SIX_MONTHS = "SIX_MONTHS"
    '''6 months.'''
    ONE_YEAR = "ONE_YEAR"
    '''1 year.'''
    THIRTEEN_MONTHS = "THIRTEEN_MONTHS"
    '''13 months.'''
    EIGHTEEN_MONTHS = "EIGHTEEN_MONTHS"
    '''18 months.'''
    TWO_YEARS = "TWO_YEARS"
    '''2 years.'''
    THREE_YEARS = "THREE_YEARS"
    '''3 years.'''
    FIVE_YEARS = "FIVE_YEARS"
    '''5 years.'''
    SIX_YEARS = "SIX_YEARS"
    '''6 years.'''
    SEVEN_YEARS = "SEVEN_YEARS"
    '''7 years.'''
    EIGHT_YEARS = "EIGHT_YEARS"
    '''8 years.'''
    NINE_YEARS = "NINE_YEARS"
    '''9 years.'''
    TEN_YEARS = "TEN_YEARS"
    '''10 years.'''
    INFINITE = "INFINITE"
    '''Retain logs forever.'''


@jsii.implements(IFilterPattern)
class SpaceDelimitedTextPattern(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_logs.SpaceDelimitedTextPattern",
):
    '''Space delimited text pattern.

    :exampleMetadata: infused

    Example::

        # Search for all events where the component is "HttpServer" and the
        # result code is not equal to 200.
        pattern = logs.FilterPattern.space_delimited("time", "component", "...", "result_code", "latency").where_string("component", "=", "HttpServer").where_number("result_code", "!=", 200)
    '''

    def __init__(
        self,
        columns: typing.Sequence[builtins.str],
        restrictions: typing.Mapping[builtins.str, typing.Sequence[typing.Union[ColumnRestriction, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param columns: -
        :param restrictions: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b056cc11acf9eec747709139eb527ca4dbbf26be0a7b192c65f6ce27af65184)
            check_type(argname="argument columns", value=columns, expected_type=type_hints["columns"])
            check_type(argname="argument restrictions", value=restrictions, expected_type=type_hints["restrictions"])
        jsii.create(self.__class__, self, [columns, restrictions])

    @jsii.member(jsii_name="construct")
    @builtins.classmethod
    def construct(
        cls,
        columns: typing.Sequence[builtins.str],
    ) -> "SpaceDelimitedTextPattern":
        '''Construct a new instance of a space delimited text pattern.

        Since this class must be public, we can't rely on the user only creating it through
        the ``LogPattern.spaceDelimited()`` factory function. We must therefore validate the
        argument in the constructor. Since we're returning a copy on every mutation, and we
        don't want to re-validate the same things on every construction, we provide a limited
        set of mutator functions and only validate the new data every time.

        :param columns: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80d1e9e085756c1b7939b77b321d912811c1ae652d0160b5c494b0894d37e178)
            check_type(argname="argument columns", value=columns, expected_type=type_hints["columns"])
        return typing.cast("SpaceDelimitedTextPattern", jsii.sinvoke(cls, "construct", [columns]))

    @jsii.member(jsii_name="whereNumber")
    def where_number(
        self,
        column_name: builtins.str,
        comparison: builtins.str,
        value: jsii.Number,
    ) -> "SpaceDelimitedTextPattern":
        '''Restrict where the pattern applies.

        :param column_name: -
        :param comparison: -
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9837cdc1b4560186b7313c523de825a85b6c099daae328e79ce8c2a6fcc1431f)
            check_type(argname="argument column_name", value=column_name, expected_type=type_hints["column_name"])
            check_type(argname="argument comparison", value=comparison, expected_type=type_hints["comparison"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast("SpaceDelimitedTextPattern", jsii.invoke(self, "whereNumber", [column_name, comparison, value]))

    @jsii.member(jsii_name="whereString")
    def where_string(
        self,
        column_name: builtins.str,
        comparison: builtins.str,
        value: builtins.str,
    ) -> "SpaceDelimitedTextPattern":
        '''Restrict where the pattern applies.

        :param column_name: -
        :param comparison: -
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__071ad580f6d865947c2434ea9ce22e541c8aabe0aaf4f627b337988d5c6c6ccd)
            check_type(argname="argument column_name", value=column_name, expected_type=type_hints["column_name"])
            check_type(argname="argument comparison", value=comparison, expected_type=type_hints["comparison"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast("SpaceDelimitedTextPattern", jsii.invoke(self, "whereString", [column_name, comparison, value]))

    @builtins.property
    @jsii.member(jsii_name="logPatternString")
    def log_pattern_string(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logPatternString"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.StreamOptions",
    jsii_struct_bases=[],
    name_mapping={"log_stream_name": "logStreamName"},
)
class StreamOptions:
    def __init__(
        self,
        *,
        log_stream_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for a new LogStream created from a LogGroup.

        :param log_stream_name: The name of the log stream to create. The name must be unique within the log group. Default: Automatically generated

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_logs as logs
            
            stream_options = logs.StreamOptions(
                log_stream_name="logStreamName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__faa627faaa2e41610592354837a6717d48ec540f225e5fa931868e06dda19d5e)
            check_type(argname="argument log_stream_name", value=log_stream_name, expected_type=type_hints["log_stream_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if log_stream_name is not None:
            self._values["log_stream_name"] = log_stream_name

    @builtins.property
    def log_stream_name(self) -> typing.Optional[builtins.str]:
        '''The name of the log stream to create.

        The name must be unique within the log group.

        :default: Automatically generated
        '''
        result = self._values.get("log_stream_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StreamOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SubscriptionFilter(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_logs.SubscriptionFilter",
):
    '''A new Subscription on a CloudWatch log group.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_logs_destinations as destinations
        
        # fn: lambda.Function
        # log_group: logs.LogGroup
        
        
        logs.SubscriptionFilter(self, "Subscription",
            log_group=log_group,
            destination=destinations.LambdaDestination(fn),
            filter_pattern=logs.FilterPattern.all_terms("ERROR", "MainThread"),
            filter_name="ErrorInMainThread"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        log_group: ILogGroup,
        destination: ILogSubscriptionDestination,
        filter_pattern: IFilterPattern,
        filter_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param log_group: The log group to create the subscription on.
        :param destination: The destination to send the filtered events to. For example, a Kinesis stream or a Lambda function.
        :param filter_pattern: Log events matching this pattern will be sent to the destination.
        :param filter_name: The name of the subscription filter. Default: Automatically generated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3c78d3f905ddfb9bb1ff8466a0b030e7b262b0793c43d2667b561e420cbb3c7)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = SubscriptionFilterProps(
            log_group=log_group,
            destination=destination,
            filter_pattern=filter_pattern,
            filter_name=filter_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.SubscriptionFilterOptions",
    jsii_struct_bases=[],
    name_mapping={
        "destination": "destination",
        "filter_pattern": "filterPattern",
        "filter_name": "filterName",
    },
)
class SubscriptionFilterOptions:
    def __init__(
        self,
        *,
        destination: ILogSubscriptionDestination,
        filter_pattern: IFilterPattern,
        filter_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for a new SubscriptionFilter created from a LogGroup.

        :param destination: The destination to send the filtered events to. For example, a Kinesis stream or a Lambda function.
        :param filter_pattern: Log events matching this pattern will be sent to the destination.
        :param filter_name: The name of the subscription filter. Default: Automatically generated

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_logs as logs
            
            # filter_pattern: logs.IFilterPattern
            # log_subscription_destination: logs.ILogSubscriptionDestination
            
            subscription_filter_options = logs.SubscriptionFilterOptions(
                destination=log_subscription_destination,
                filter_pattern=filter_pattern,
            
                # the properties below are optional
                filter_name="filterName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__177a84e94bfd826b20adc1107770c972772c540b0a1ac8475f63476502450a73)
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
            check_type(argname="argument filter_pattern", value=filter_pattern, expected_type=type_hints["filter_pattern"])
            check_type(argname="argument filter_name", value=filter_name, expected_type=type_hints["filter_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "destination": destination,
            "filter_pattern": filter_pattern,
        }
        if filter_name is not None:
            self._values["filter_name"] = filter_name

    @builtins.property
    def destination(self) -> ILogSubscriptionDestination:
        '''The destination to send the filtered events to.

        For example, a Kinesis stream or a Lambda function.
        '''
        result = self._values.get("destination")
        assert result is not None, "Required property 'destination' is missing"
        return typing.cast(ILogSubscriptionDestination, result)

    @builtins.property
    def filter_pattern(self) -> IFilterPattern:
        '''Log events matching this pattern will be sent to the destination.'''
        result = self._values.get("filter_pattern")
        assert result is not None, "Required property 'filter_pattern' is missing"
        return typing.cast(IFilterPattern, result)

    @builtins.property
    def filter_name(self) -> typing.Optional[builtins.str]:
        '''The name of the subscription filter.

        :default: Automatically generated
        '''
        result = self._values.get("filter_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SubscriptionFilterOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.SubscriptionFilterProps",
    jsii_struct_bases=[SubscriptionFilterOptions],
    name_mapping={
        "destination": "destination",
        "filter_pattern": "filterPattern",
        "filter_name": "filterName",
        "log_group": "logGroup",
    },
)
class SubscriptionFilterProps(SubscriptionFilterOptions):
    def __init__(
        self,
        *,
        destination: ILogSubscriptionDestination,
        filter_pattern: IFilterPattern,
        filter_name: typing.Optional[builtins.str] = None,
        log_group: ILogGroup,
    ) -> None:
        '''Properties for a SubscriptionFilter.

        :param destination: The destination to send the filtered events to. For example, a Kinesis stream or a Lambda function.
        :param filter_pattern: Log events matching this pattern will be sent to the destination.
        :param filter_name: The name of the subscription filter. Default: Automatically generated
        :param log_group: The log group to create the subscription on.

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_logs_destinations as destinations
            
            # fn: lambda.Function
            # log_group: logs.LogGroup
            
            
            logs.SubscriptionFilter(self, "Subscription",
                log_group=log_group,
                destination=destinations.LambdaDestination(fn),
                filter_pattern=logs.FilterPattern.all_terms("ERROR", "MainThread"),
                filter_name="ErrorInMainThread"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb936c8dd6a8ee03c9e8f4ffbe991c19b4b98648bbdd91f03367a058de3e8268)
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
            check_type(argname="argument filter_pattern", value=filter_pattern, expected_type=type_hints["filter_pattern"])
            check_type(argname="argument filter_name", value=filter_name, expected_type=type_hints["filter_name"])
            check_type(argname="argument log_group", value=log_group, expected_type=type_hints["log_group"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "destination": destination,
            "filter_pattern": filter_pattern,
            "log_group": log_group,
        }
        if filter_name is not None:
            self._values["filter_name"] = filter_name

    @builtins.property
    def destination(self) -> ILogSubscriptionDestination:
        '''The destination to send the filtered events to.

        For example, a Kinesis stream or a Lambda function.
        '''
        result = self._values.get("destination")
        assert result is not None, "Required property 'destination' is missing"
        return typing.cast(ILogSubscriptionDestination, result)

    @builtins.property
    def filter_pattern(self) -> IFilterPattern:
        '''Log events matching this pattern will be sent to the destination.'''
        result = self._values.get("filter_pattern")
        assert result is not None, "Required property 'filter_pattern' is missing"
        return typing.cast(IFilterPattern, result)

    @builtins.property
    def filter_name(self) -> typing.Optional[builtins.str]:
        '''The name of the subscription filter.

        :default: Automatically generated
        '''
        result = self._values.get("filter_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_group(self) -> ILogGroup:
        '''The log group to create the subscription on.'''
        result = self._values.get("log_group")
        assert result is not None, "Required property 'log_group' is missing"
        return typing.cast(ILogGroup, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SubscriptionFilterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(ILogSubscriptionDestination)
class CrossAccountDestination(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_logs.CrossAccountDestination",
):
    '''A new CloudWatch Logs Destination for use in cross-account scenarios.

    CrossAccountDestinations are used to subscribe a Kinesis stream in a
    different account to a CloudWatch Subscription.

    Consumers will hardly ever need to use this class. Instead, directly
    subscribe a Kinesis stream using the integration class in the
    ``aws-cdk-lib/aws-logs-destinations`` package; if necessary, a
    ``CrossAccountDestination`` will be created automatically.

    :resource: AWS::Logs::Destination
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iam as iam
        from aws_cdk import aws_logs as logs
        
        # role: iam.Role
        
        cross_account_destination = logs.CrossAccountDestination(self, "MyCrossAccountDestination",
            role=role,
            target_arn="targetArn",
        
            # the properties below are optional
            destination_name="destinationName"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        role: _IRole_235f5d8e,
        target_arn: builtins.str,
        destination_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param role: The role to assume that grants permissions to write to 'target'. The role must be assumable by 'logs.{REGION}.amazonaws.com'.
        :param target_arn: The log destination target's ARN.
        :param destination_name: The name of the log destination. Default: Automatically generated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f78998ef1421583d87d205e0c66668e415d3a06be064cfc35682d8884a01ad56)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CrossAccountDestinationProps(
            role=role, target_arn=target_arn, destination_name=destination_name
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="addToPolicy")
    def add_to_policy(self, statement: _PolicyStatement_0fe33853) -> None:
        '''
        :param statement: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a3a6f7c79a2740b0e52fcc48d64fb4e96cfdc2abd91649f986c7d67b9d5ee67)
            check_type(argname="argument statement", value=statement, expected_type=type_hints["statement"])
        return typing.cast(None, jsii.invoke(self, "addToPolicy", [statement]))

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _scope: _constructs_77d1e7e8.Construct,
        _source_log_group: ILogGroup,
    ) -> LogSubscriptionDestinationConfig:
        '''Return the properties required to send subscription events to this destination.

        If necessary, the destination can use the properties of the SubscriptionFilter
        object itself to configure its permissions to allow the subscription to write
        to it.

        The destination may reconfigure its own permissions in response to this
        function call.

        :param _scope: -
        :param _source_log_group: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__901846e19d9ba5beee9ef4784401b7413f0b32b2034ea5700b5fa8a30a1c0394)
            check_type(argname="argument _scope", value=_scope, expected_type=type_hints["_scope"])
            check_type(argname="argument _source_log_group", value=_source_log_group, expected_type=type_hints["_source_log_group"])
        return typing.cast(LogSubscriptionDestinationConfig, jsii.invoke(self, "bind", [_scope, _source_log_group]))

    @builtins.property
    @jsii.member(jsii_name="destinationArn")
    def destination_arn(self) -> builtins.str:
        '''The ARN of this CrossAccountDestination object.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "destinationArn"))

    @builtins.property
    @jsii.member(jsii_name="destinationName")
    def destination_name(self) -> builtins.str:
        '''The name of this CrossAccountDestination object.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "destinationName"))

    @builtins.property
    @jsii.member(jsii_name="policyDocument")
    def policy_document(self) -> _PolicyDocument_3ac34393:
        '''Policy object of this CrossAccountDestination object.'''
        return typing.cast(_PolicyDocument_3ac34393, jsii.get(self, "policyDocument"))


__all__ = [
    "CfnAccountPolicy",
    "CfnAccountPolicyProps",
    "CfnDestination",
    "CfnDestinationProps",
    "CfnLogGroup",
    "CfnLogGroupProps",
    "CfnLogStream",
    "CfnLogStreamProps",
    "CfnMetricFilter",
    "CfnMetricFilterProps",
    "CfnQueryDefinition",
    "CfnQueryDefinitionProps",
    "CfnResourcePolicy",
    "CfnResourcePolicyProps",
    "CfnSubscriptionFilter",
    "CfnSubscriptionFilterProps",
    "ColumnRestriction",
    "CrossAccountDestination",
    "CrossAccountDestinationProps",
    "DataIdentifier",
    "DataProtectionPolicy",
    "DataProtectionPolicyConfig",
    "DataProtectionPolicyProps",
    "FilterPattern",
    "IFilterPattern",
    "ILogGroup",
    "ILogStream",
    "ILogSubscriptionDestination",
    "JsonPattern",
    "LogGroup",
    "LogGroupProps",
    "LogRetention",
    "LogRetentionProps",
    "LogRetentionRetryOptions",
    "LogStream",
    "LogStreamProps",
    "LogSubscriptionDestinationConfig",
    "MetricFilter",
    "MetricFilterOptions",
    "MetricFilterProps",
    "QueryDefinition",
    "QueryDefinitionProps",
    "QueryString",
    "QueryStringProps",
    "ResourcePolicy",
    "ResourcePolicyProps",
    "RetentionDays",
    "SpaceDelimitedTextPattern",
    "StreamOptions",
    "SubscriptionFilter",
    "SubscriptionFilterOptions",
    "SubscriptionFilterProps",
]

publication.publish()

def _typecheckingstub__125a77dd271c26d92d39f5fc5e47e588668423ade67a45afc5817e4df1ee8dd0(
    scope_: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    policy_document: builtins.str,
    policy_name: builtins.str,
    policy_type: builtins.str,
    scope: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ebfd4fb8cf24056dd4dacb27f135740e6f55ee47d01767451cebf21c25f0837a(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9fa52c452e9fe5605a874b3dd89e31ad16dc4f246300b4319af792307b4ae876(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c653a261ed47c5ebab7b21521ba00f1e039f43a3aee30163835cda4b9b741be(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a3c39fb59cb9806cbee8cf38c347eab7bc33fee8e2148f96faae887592ab14c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6152ad747f0f8c8124fd42f55dd6679b842c8faa8ef76cc08b3c59d43df9e9c1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a2b34c27c4f47efc3559774d8625b4374c145ac113ac7b65b32dbafd795a627(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e40dcebab5dfdd5fd816fda98a9c4e710aa8bc28c8bbd574a9451defb6d0d66(
    *,
    policy_document: builtins.str,
    policy_name: builtins.str,
    policy_type: builtins.str,
    scope: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44e37c6c2772abdacfbcd01df5c5418fca8937b435df3890a5a5cb3437b9bab5(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    destination_name: builtins.str,
    role_arn: builtins.str,
    target_arn: builtins.str,
    destination_policy: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96cb24255178be4bad07466bab77f2ccec3a7bf2f35acfe8bf018152eb28bb7e(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f9dedbbaf433f224026d220b3fb36706410370925367aeada047e8858f484ac(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5158605e72fe974296ad671ff50605f46d8a94d78d818e766756296254fa5758(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__908d4772c2472f7ef1a59ee7f794734117f87a8908ceda3def1feff5578217c1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90e291c0d065725c0ff62d5808258937a46aa7e3d79209721b2ffdb32fc0db6b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b0569830af0faea41307b4fd071b0ef86a0b49f3514f3050bfa53cc72d3ddee(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__faf2f9f88fd096e79a2445aab3efdc3a85509df7ba06ffc305c9faf39fa77a56(
    *,
    destination_name: builtins.str,
    role_arn: builtins.str,
    target_arn: builtins.str,
    destination_policy: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e283e76ec168d67513d106f9413697672f161b29f03fa9b13486e96b13319c0(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    data_protection_policy: typing.Any = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    log_group_name: typing.Optional[builtins.str] = None,
    retention_in_days: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c5bac0ef7ae74529e652cc24b33213b3432954607a3665dd72bd69b68490c7c(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__167d66406821a4fe8a6ca05ec99424e7c4abd7946ba6eb30ee37e04443759ddc(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__427539e290b46019fba84ec8aa72f953c2d26dfe978de85330819964c3cea37e(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0fc22b518f14684135ca2ffa0556628df055b32df3a769085c35ae8ef72d5677(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08bea1f6b59cbce316d19aa0ff5db07ed0da20b04cc322eb41788ce24f8f2d31(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d977a18b9031aeb9d37e4baf6f3eccb9ebf070ad2e33a30cfba9f69fbaf62408(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ea9a0a37724d334e68ee325d75e901df12c6765b4c229366a1cef4038c07187(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a2ba122502a64b05bea3e56f15389c84f127761b660b1d06de3ea638b95f816(
    *,
    data_protection_policy: typing.Any = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    log_group_name: typing.Optional[builtins.str] = None,
    retention_in_days: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68392ef44019b9b5ee681acb5bd13c481e1cc999bc1f1773e84c70b5a04190b7(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    log_group_name: builtins.str,
    log_stream_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64fb9d8e354f9197a9998608e06c1be2deb6b929ddb7835470385c91e16d110a(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ec4cadc779471f71fa1f1b77d2bda5c706e530b0ead1517f46ec34940fee5da(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28f49c7b712326ca2be5a290a29a4430589b6c15c4da1f34afb773fcc0456112(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e3f8ff96c3dac6c45a8d31d07a3223b27eebb1e1c6aa1676d6cf0cfc0bcacb8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab2d708d8a8c684eb8753554b20ecf7de790ffc112520d594cacb903aff379ea(
    *,
    log_group_name: builtins.str,
    log_stream_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aaa6a2018a5f10ec1a79f547b81a628d6f434d037b49c5975131bba2d6fd2786(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    filter_pattern: builtins.str,
    log_group_name: builtins.str,
    metric_transformations: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMetricFilter.MetricTransformationProperty, typing.Dict[builtins.str, typing.Any]]]]],
    filter_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa5f65c3d38181c3265e71ca5f37737480594a08405697ef96fc18254e2a9899(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aed2b5842b90369a626b9acdfbfb87dab07b9debcde1b1964b8b0dabb330ea2e(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9fdc6521987ce3f017024e20e1e0fb59a35415aa424ed169b346a59793c88b73(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae16ea786b9d9ed9d5bfe824932074163b1aa6379bed22eb2671f3ed0818bf26(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e42e8a9e143351ba28d452f886abff3c46adff74b2c2fc8876dc18aabf51dcba(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnMetricFilter.MetricTransformationProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed6515d6733ea675274296cf9952fb0b41bd1778277ae74bde9739d81a205382(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9fad5f3c7dec2c3bafa74c42e2398a046d9cc8c861abfac39c6e9e77c2b65b41(
    *,
    key: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8989e36bc84de1e18d069af1bb22845cf409685cbd8a8fe22cd131474e0d7958(
    *,
    metric_name: builtins.str,
    metric_namespace: builtins.str,
    metric_value: builtins.str,
    default_value: typing.Optional[jsii.Number] = None,
    dimensions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMetricFilter.DimensionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    unit: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__524e2e94ad4843f66081953f516426a1396490f271842ac0c5ca7c7ecb84011e(
    *,
    filter_pattern: builtins.str,
    log_group_name: builtins.str,
    metric_transformations: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMetricFilter.MetricTransformationProperty, typing.Dict[builtins.str, typing.Any]]]]],
    filter_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d10075ae036bdf9f4049570cf68ab72c79ee717f007f45628b52d2ea5aa64ae(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    query_string: builtins.str,
    log_group_names: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1dd626642ab8510fa9005787d00adbbd508a543616e89979ad57ba0be9f38bad(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d445c0915cb40f09b489a0802b2b2b0c035e244acf419b2452990fd8568900fe(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a970de5992ab8622f5a1c04c70c2066cfaee94719e9aba8c8edbe863ddcce298(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__005c13f188808f7829e17c5ce9ca7e9ae473e50b0b0b1ed4f95b8e35cfd6a6df(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1d922394643a9758400b7e596dd6c6fe61ab7e1fb96d4a93a7061d0e3b5c39d(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd7180e50961abf6b838dfc21ba186cc5b2c551eae8357613767f891abe51780(
    *,
    name: builtins.str,
    query_string: builtins.str,
    log_group_names: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96eb8f500492c7ddcaba9f292d2aa1c488941affca3b4911cd4ce9636c1ce721(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    policy_document: builtins.str,
    policy_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a2e3f9cc2e418bf4cc4f8f63fc54eed1907f2c1b38483cc8c59d2f8b653c69f(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94bd685f258ef991a46514a1b4f58ba0b0bf9314fc8055746b8652c965857253(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3fd3f538cb966d97639dd18283329cf7c5f581a2f069d6d37e7cd0ab5cedb7fd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de9476941a8f893fee016885d888db6d17d101f4ad44646ba809adde15261aed(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ab184a479fd32db068d45168ec1b6bf45cf1a4a3d64847b519a088388c84df8(
    *,
    policy_document: builtins.str,
    policy_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c7a154450656ee0f7e524d596c7e140faad893a71a7c8b9b8a85fe730a1dcf9(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    destination_arn: builtins.str,
    filter_pattern: builtins.str,
    log_group_name: builtins.str,
    distribution: typing.Optional[builtins.str] = None,
    filter_name: typing.Optional[builtins.str] = None,
    role_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4fd7a0e99337509280da552b557b613a8fcb858acf9e84e9aacbe572366bca99(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c7e4c15a871de67a808634e0ce4138af489acd8a95e0b0e5e5cb1829aa66805(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dcf92dedad133b23741e31710f66784d3728a1a96f5d9b514b8a80f012d7b84c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5af0335707946ab6b7311049c978104cfb68f9d36688e1bf25585706ebcbb08a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfa4dbdd67c0f388eefe38fe86bae9148a44785d56910a1951619c1205e4eb56(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4730d6086a07b6e1f3b3d7251138c936aa909d17834505b0c341ec6b421adf19(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ccf855abfc15a31ed667e6619b6f1711fc4ef753c64ec0b754421d81c8edb75(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1cdca0b99d7b39060b314b323073c0a48e25972ff085f24a455a00339addb4ee(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1250ecc947a5eb57e428cd8fedeb9ae0f6da4eb03c22d674fa019a076ee8b507(
    *,
    destination_arn: builtins.str,
    filter_pattern: builtins.str,
    log_group_name: builtins.str,
    distribution: typing.Optional[builtins.str] = None,
    filter_name: typing.Optional[builtins.str] = None,
    role_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2766fe6d7d19a8737daff90dd79e476a2d4dcde95605b7656e40b088fdf6e64(
    *,
    comparison: builtins.str,
    number_value: typing.Optional[jsii.Number] = None,
    string_value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4be07d68ab857f5ae6300c8382cb03fbeec1052d13af65659f773e30196e8c1(
    *,
    role: _IRole_235f5d8e,
    target_arn: builtins.str,
    destination_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15f2f9a4aba70e88d25dcda444a45fe96535b0317fb974d64d2b70c8e6982915(
    identifier: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__376464888d50baaad4ab20b9ef8766e9aa93a91c55c8662ab5ec2fafa8086822(
    *,
    description: builtins.str,
    name: builtins.str,
    statement: typing.Any,
    version: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7783165e1d00e232a8ee35869f53b7ff500c9680f96b895f705e24475c7b6b2(
    *,
    identifiers: typing.Sequence[DataIdentifier],
    delivery_stream_name_audit_destination: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    log_group_audit_destination: typing.Optional[ILogGroup] = None,
    name: typing.Optional[builtins.str] = None,
    s3_bucket_audit_destination: typing.Optional[_IBucket_42e086fd] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef6e7314c6a5197496584b4f3fc9dc8a24050e8d3d30eabb788540b98e00e4f0(
    *patterns: JsonPattern,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c83797f363cc2a7f1bb9ea15ea4f4d7eeed745e9d300970e536e8df78633b0a6(
    *terms: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06cd0420e64a91321c2dbdcdb6fa54fa56bffd0eab770aa6aa4000670f1beec3(
    *patterns: JsonPattern,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b38181b10ed8fe5993dd7ec40690693fe0d164f997f37ddbf297f8b840de2b18(
    *terms: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2623b46359820ca611b2cf65fab9b8e6c24ef2bd3d30bcebc3d022b2173b58ee(
    *term_groups: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0e87f500ca69757a8ec1184452b5b2b45c68758c062a77bc2248afd2c3b793e(
    json_field: builtins.str,
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56192ad48c0fbacd0f9f10fc26eebe8f311d8164217227e094a00a61f7c0d300(
    json_field: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93deee33b43c0efbe360f5ef6a60ba3cd0c1af95d7ca176abb95a482e1be8748(
    json_field: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65d91e718fc9d96060c30c68dee958f370d2ae16fbb2e3cf8f0030e0408b3320(
    log_pattern_string: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a90c7e4fc8c86ca2759be152abbd3a44e4e78851d525cdb047698b1825283849(
    json_field: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1cb7dce1caa0866199f67de4ab23972e5d6dc3cd90ca77ce9a5f09f7dc2b1fa(
    json_field: builtins.str,
    comparison: builtins.str,
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f5f56f60ccfd9dae1e3e3f54e54d87c6fb3e287c5bd2ad7924a4578ee4f8121(
    *columns: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31ecfe1cc2c14607ed9938dc33b51889185e1c9f4ea9e9e7ce494ae69f7d3374(
    json_field: builtins.str,
    comparison: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c3910e9df11478e889b7f25e252df8a33e79b82dd18c304bf83e6be63f60c95(
    id: builtins.str,
    *,
    filter_pattern: IFilterPattern,
    metric_name: builtins.str,
    metric_namespace: builtins.str,
    default_value: typing.Optional[jsii.Number] = None,
    dimensions: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    filter_name: typing.Optional[builtins.str] = None,
    metric_value: typing.Optional[builtins.str] = None,
    unit: typing.Optional[_Unit_61bc6f70] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad3db791d4d809f8716f4717b634e830370009e865e37f5c54e65cc5c5d57102(
    id: builtins.str,
    *,
    log_stream_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3445e5a6f896ca9cd9e8a527d7229440b3a517fd59dc21bc08b64ef68e4f4eaa(
    id: builtins.str,
    *,
    destination: ILogSubscriptionDestination,
    filter_pattern: IFilterPattern,
    filter_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9dc31b09300449039c7ac2db2c1e23ab325c60cc2fa2fa9ee5b513c2e1d62f7b(
    json_field: builtins.str,
    metric_namespace: builtins.str,
    metric_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d45146324c9cc51983b9b92779906c83ea73e499386493771cdd256c131ca87(
    grantee: _IGrantable_71c4f5de,
    *actions: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10f2b216c33139da1022d0b7d73974166dcf17c508e30913421c9f89375a9bb0(
    grantee: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__558c66823e9e8b21feeb1abd2b6534206c929fdf82184f3c0d1aff2942610538(
    grantee: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d2d750464949100272f59f23f28dae31a40c84ad1d188b0cd44fdca6ca395d5(
    scope: _constructs_77d1e7e8.Construct,
    source_log_group: ILogGroup,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63b70184328854d0009cc9ba82f6a6720fd48ccf9458964b5cc75f6cfb653549(
    json_pattern_string: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__308a02ff022bfc4531ef0c547fbfb8db809293b3cda70c61106c9bc271126e70(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    data_protection_policy: typing.Optional[DataProtectionPolicy] = None,
    encryption_key: typing.Optional[_IKey_5f11635f] = None,
    log_group_name: typing.Optional[builtins.str] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    retention: typing.Optional[RetentionDays] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94bc59386fc670bf1438201199282e56f015468fe650487225ccaca3ae495cd7(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    log_group_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9988695c3237dc33d233c2bca8c1a32b8ca9135d661974af7b593667d7199d2(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    log_group_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60bdb647264d5f9edd37cf7e07a8b1cde70ce81f1ebb17eb131efa9d12a73e70(
    id: builtins.str,
    *,
    filter_pattern: IFilterPattern,
    metric_name: builtins.str,
    metric_namespace: builtins.str,
    default_value: typing.Optional[jsii.Number] = None,
    dimensions: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    filter_name: typing.Optional[builtins.str] = None,
    metric_value: typing.Optional[builtins.str] = None,
    unit: typing.Optional[_Unit_61bc6f70] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a24d4a9b6baaaae57b481202eeb591bd2f9c75a23a136632347af1c7954e70d(
    id: builtins.str,
    *,
    log_stream_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a53e1c08918ff12981b248135756d8f20c9acc571a2cab87ee6a3504361564b6(
    id: builtins.str,
    *,
    destination: ILogSubscriptionDestination,
    filter_pattern: IFilterPattern,
    filter_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f61b70f15ff76b195297fc3fa75909dc7046483a164b76160596773157f547f(
    statement: _PolicyStatement_0fe33853,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fec042a3492600efc8a11c082c58cb34995746a66ce985d97fd5c74ba47f0b96(
    json_field: builtins.str,
    metric_namespace: builtins.str,
    metric_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9a9cb0e1cec11a01408a7a448100c7b05edddf5bb005abd006a834d3c923bb7(
    grantee: _IGrantable_71c4f5de,
    *actions: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__049a7f93ec71ef52ad5919516c695afd1e3f1185bfaadbf66b872fe23abae4db(
    grantee: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c97b414675dc468df60a1d999b2ddb74ddf42567d0d8ac3af19bb44f4022b1b0(
    grantee: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df51a93f7809d59dd37d78a60967e0071dab4876ea1cd5ecd658ac3c8eae1320(
    *,
    data_protection_policy: typing.Optional[DataProtectionPolicy] = None,
    encryption_key: typing.Optional[_IKey_5f11635f] = None,
    log_group_name: typing.Optional[builtins.str] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    retention: typing.Optional[RetentionDays] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4507613a235a88592d0ebd7d0dbe61f494620068c75fef42db8c09f2dfde8cc(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    log_group_name: builtins.str,
    retention: RetentionDays,
    log_group_region: typing.Optional[builtins.str] = None,
    log_retention_retry_options: typing.Optional[typing.Union[LogRetentionRetryOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__318a9234eb28bfd26692eac8fd1ea9c47cedbd175a0dc53714860906302a980b(
    *,
    log_group_name: builtins.str,
    retention: RetentionDays,
    log_group_region: typing.Optional[builtins.str] = None,
    log_retention_retry_options: typing.Optional[typing.Union[LogRetentionRetryOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9636a1cfdc99034fff1c4ef9550b1c380d0f51a19f14b506c85c32184b950d42(
    *,
    base: typing.Optional[_Duration_4839e8c3] = None,
    max_retries: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7b310f4ff2940ed4dffa21e4ffde6e0f0bb15bdf93db6bd6d34466158da5c47(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    log_group: ILogGroup,
    log_stream_name: typing.Optional[builtins.str] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c90257c192f43807c3ca64b0dfd7f0d8f24a0e76af49b59d49ef0b271d7e85a0(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    log_stream_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f49a14f2b0eea132d7cea27db911c1bac5a2370d8c93686afb12d7bf18544ca(
    *,
    log_group: ILogGroup,
    log_stream_name: typing.Optional[builtins.str] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__396d59c2514d8bfe65a7a6f818257b42d5f5c9b200fa30ed27db93bc6e8328e0(
    *,
    arn: builtins.str,
    role: typing.Optional[_IRole_235f5d8e] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d62ba20acf6180e35fd081efe9f21747bf2bd8765dd3a4a5c41cc0f41f079a1(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    log_group: ILogGroup,
    filter_pattern: IFilterPattern,
    metric_name: builtins.str,
    metric_namespace: builtins.str,
    default_value: typing.Optional[jsii.Number] = None,
    dimensions: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    filter_name: typing.Optional[builtins.str] = None,
    metric_value: typing.Optional[builtins.str] = None,
    unit: typing.Optional[_Unit_61bc6f70] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5bb9c8220568f1b3f6adf2d20dcfde3ada18ce4351110a49b3a0707812e51fe(
    *,
    filter_pattern: IFilterPattern,
    metric_name: builtins.str,
    metric_namespace: builtins.str,
    default_value: typing.Optional[jsii.Number] = None,
    dimensions: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    filter_name: typing.Optional[builtins.str] = None,
    metric_value: typing.Optional[builtins.str] = None,
    unit: typing.Optional[_Unit_61bc6f70] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66722f3b881a30b7ce1b9efa7c76f2539915abe8fe84a770e1e2c47657d59d79(
    *,
    filter_pattern: IFilterPattern,
    metric_name: builtins.str,
    metric_namespace: builtins.str,
    default_value: typing.Optional[jsii.Number] = None,
    dimensions: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    filter_name: typing.Optional[builtins.str] = None,
    metric_value: typing.Optional[builtins.str] = None,
    unit: typing.Optional[_Unit_61bc6f70] = None,
    log_group: ILogGroup,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7cb87fa9a91fccd75052278e9031242b20cab41bb53f8f18544b867e01e5d41(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    query_definition_name: builtins.str,
    query_string: QueryString,
    log_groups: typing.Optional[typing.Sequence[ILogGroup]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__993712107c64f2acd19761e2b930e6e052534d1100257989bcf307bb6168b668(
    *,
    query_definition_name: builtins.str,
    query_string: QueryString,
    log_groups: typing.Optional[typing.Sequence[ILogGroup]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d205eb2ac9b46de0083e3387b95b00f2362e2ade91d5c581e5d8cde68293b28d(
    *,
    display: typing.Optional[builtins.str] = None,
    fields: typing.Optional[typing.Sequence[builtins.str]] = None,
    filter: typing.Optional[builtins.str] = None,
    filter_statements: typing.Optional[typing.Sequence[builtins.str]] = None,
    limit: typing.Optional[jsii.Number] = None,
    parse: typing.Optional[builtins.str] = None,
    parse_statements: typing.Optional[typing.Sequence[builtins.str]] = None,
    sort: typing.Optional[builtins.str] = None,
    stats: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__772b118f71acb9e446b4948b9aac7bf360262cdeddc09c1f28708795cdb48c74(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    policy_statements: typing.Optional[typing.Sequence[_PolicyStatement_0fe33853]] = None,
    resource_policy_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4f5108e8fcf5bafe964b9be836229eed1f4ac734a83be621801cd6304143286(
    *,
    policy_statements: typing.Optional[typing.Sequence[_PolicyStatement_0fe33853]] = None,
    resource_policy_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b056cc11acf9eec747709139eb527ca4dbbf26be0a7b192c65f6ce27af65184(
    columns: typing.Sequence[builtins.str],
    restrictions: typing.Mapping[builtins.str, typing.Sequence[typing.Union[ColumnRestriction, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80d1e9e085756c1b7939b77b321d912811c1ae652d0160b5c494b0894d37e178(
    columns: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9837cdc1b4560186b7313c523de825a85b6c099daae328e79ce8c2a6fcc1431f(
    column_name: builtins.str,
    comparison: builtins.str,
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__071ad580f6d865947c2434ea9ce22e541c8aabe0aaf4f627b337988d5c6c6ccd(
    column_name: builtins.str,
    comparison: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__faa627faaa2e41610592354837a6717d48ec540f225e5fa931868e06dda19d5e(
    *,
    log_stream_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3c78d3f905ddfb9bb1ff8466a0b030e7b262b0793c43d2667b561e420cbb3c7(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    log_group: ILogGroup,
    destination: ILogSubscriptionDestination,
    filter_pattern: IFilterPattern,
    filter_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__177a84e94bfd826b20adc1107770c972772c540b0a1ac8475f63476502450a73(
    *,
    destination: ILogSubscriptionDestination,
    filter_pattern: IFilterPattern,
    filter_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb936c8dd6a8ee03c9e8f4ffbe991c19b4b98648bbdd91f03367a058de3e8268(
    *,
    destination: ILogSubscriptionDestination,
    filter_pattern: IFilterPattern,
    filter_name: typing.Optional[builtins.str] = None,
    log_group: ILogGroup,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f78998ef1421583d87d205e0c66668e415d3a06be064cfc35682d8884a01ad56(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    role: _IRole_235f5d8e,
    target_arn: builtins.str,
    destination_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a3a6f7c79a2740b0e52fcc48d64fb4e96cfdc2abd91649f986c7d67b9d5ee67(
    statement: _PolicyStatement_0fe33853,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__901846e19d9ba5beee9ef4784401b7413f0b32b2034ea5700b5fa8a30a1c0394(
    _scope: _constructs_77d1e7e8.Construct,
    _source_log_group: ILogGroup,
) -> None:
    """Type checking stubs"""
    pass
