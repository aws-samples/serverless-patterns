'''
# AWS Auto Scaling Construct Library

**Application AutoScaling** is used to configure autoscaling for all
services other than scaling EC2 instances. For example, you will use this to
scale ECS tasks, DynamoDB capacity, Spot Fleet sizes, Comprehend document classification endpoints, Lambda function provisioned concurrency and more.

As a CDK user, you will probably not have to interact with this library
directly; instead, it will be used by other construct libraries to
offer AutoScaling features for their own constructs.

This document will describe the general autoscaling features and concepts;
your particular service may offer only a subset of these.

## AutoScaling basics

Resources can offer one or more **attributes** to autoscale, typically
representing some capacity dimension of the underlying service. For example,
a DynamoDB Table offers autoscaling of the read and write capacity of the
table proper and its Global Secondary Indexes, an ECS Service offers
autoscaling of its task count, an RDS Aurora cluster offers scaling of its
replica count, and so on.

When you enable autoscaling for an attribute, you specify a minimum and a
maximum value for the capacity. AutoScaling policies that respond to metrics
will never go higher or lower than the indicated capacity (but scheduled
scaling actions might, see below).

There are three ways to scale your capacity:

* **In response to a metric** (also known as step scaling); for example, you
  might want to scale out if the CPU usage across your cluster starts to rise,
  and scale in when it drops again.
* **By trying to keep a certain metric around a given value** (also known as
  target tracking scaling); you might want to automatically scale out an in to
  keep your CPU usage around 50%.
* **On a schedule**; you might want to organize your scaling around traffic
  flows you expect, by scaling out in the morning and scaling in in the
  evening.

The general pattern of autoscaling will look like this:

```python
# resource: SomeScalableResource


capacity = resource.auto_scale_capacity(
    min_capacity=5,
    max_capacity=100
)
```

## Step Scaling

This type of scaling scales in and out in deterministic steps that you
configure, in response to metric values. For example, your scaling strategy
to scale in response to CPU usage might look like this:

```plaintext
 Scaling        -1          (no change)          +1       +3
            │        │                       │        │        │
            ├────────┼───────────────────────┼────────┼────────┤
            │        │                       │        │        │
CPU usage   0%      10%                     50%       70%     100%
```

(Note that this is not necessarily a recommended scaling strategy, but it's
a possible one. You will have to determine what thresholds are right for you).

You would configure it like this:

```python
# capacity: ScalableAttribute
# cpu_utilization: cloudwatch.Metric


capacity.scale_on_metric("ScaleToCPU",
    metric=cpu_utilization,
    scaling_steps=[appscaling.ScalingInterval(upper=10, change=-1), appscaling.ScalingInterval(lower=50, change=+1), appscaling.ScalingInterval(lower=70, change=+3)
    ],

    # Change this to AdjustmentType.PercentChangeInCapacity to interpret the
    # 'change' numbers before as percentages instead of capacity counts.
    adjustment_type=appscaling.AdjustmentType.CHANGE_IN_CAPACITY
)
```

The AutoScaling construct library will create the required CloudWatch alarms and
AutoScaling policies for you.

### Scaling based on multiple datapoints

The Step Scaling configuration above will initiate a scaling event when a single
datapoint of the scaling metric is breaching a scaling step breakpoint. In cases
where you might want to initiate scaling actions on a larger number of datapoints
(ie in order to smooth out randomness in the metric data), you can use the
optional `evaluationPeriods` and `datapointsToAlarm` properties:

```python
# capacity: ScalableAttribute
# cpu_utilization: cloudwatch.Metric


capacity.scale_on_metric("ScaleToCPUWithMultipleDatapoints",
    metric=cpu_utilization,
    scaling_steps=[appscaling.ScalingInterval(upper=10, change=-1), appscaling.ScalingInterval(lower=50, change=+1), appscaling.ScalingInterval(lower=70, change=+3)
    ],

    # if the cpuUtilization metric has a period of 1 minute, then data points
    # in the last 10 minutes will be evaluated
    evaluation_periods=10,

    # Only trigger a scaling action when 6 datapoints out of the last 10 are
    # breaching. If this is left unspecified, then ALL datapoints in the
    # evaluation period must be breaching to trigger a scaling action
    datapoints_to_alarm=6
)
```

## Target Tracking Scaling

This type of scaling scales in and out in order to keep a metric (typically
representing utilization) around a value you prefer. This type of scaling is
typically heavily service-dependent in what metric you can use, and so
different services will have different methods here to set up target tracking
scaling.

The following example configures the read capacity of a DynamoDB table
to be around 60% utilization:

```python
import aws_cdk.aws_dynamodb as dynamodb

# table: dynamodb.Table


read_capacity = table.auto_scale_read_capacity(
    min_capacity=10,
    max_capacity=1000
)
read_capacity.scale_on_utilization(
    target_utilization_percent=60
)
```

## Scheduled Scaling

This type of scaling is used to change capacities based on time. It works
by changing the `minCapacity` and `maxCapacity` of the attribute, and so
can be used for two purposes:

* Scale in and out on a schedule by setting the `minCapacity` high or
  the `maxCapacity` low.
* Still allow the regular scaling actions to do their job, but restrict
  the range they can scale over (by setting both `minCapacity` and
  `maxCapacity` but changing their range over time).

The following schedule expressions can be used:

* `at(yyyy-mm-ddThh:mm:ss)` -- scale at a particular moment in time
* `rate(value unit)` -- scale every minute/hour/day
* `cron(mm hh dd mm dow)` -- scale on arbitrary schedules

Of these, the cron expression is the most useful but also the most
complicated. A schedule is expressed as a cron expression. The `Schedule` class has a `cron` method to help build cron expressions.

The following example scales the fleet out in the morning, and lets natural
scaling take over at night:

```python
from aws_cdk import TimeZone
# resource: SomeScalableResource


capacity = resource.auto_scale_capacity(
    min_capacity=1,
    max_capacity=50
)

capacity.scale_on_schedule("PrescaleInTheMorning",
    schedule=appscaling.Schedule.cron(hour="8", minute="0"),
    min_capacity=20,
    time_zone=TimeZone.AMERICA_DENVER
)

capacity.scale_on_schedule("AllowDownscalingAtNight",
    schedule=appscaling.Schedule.cron(hour="20", minute="0"),
    min_capacity=1,
    time_zone=TimeZone.AMERICA_DENVER
)
```

## Examples

### Lambda Provisioned Concurrency Auto Scaling

```python
import aws_cdk.aws_lambda as lambda_

# code: lambda.Code


handler = lambda_.Function(self, "MyFunction",
    runtime=lambda_.Runtime.PYTHON_3_12,
    handler="index.handler",
    code=code,

    reserved_concurrent_executions=2
)

fn_ver = handler.current_version

target = appscaling.ScalableTarget(self, "ScalableTarget",
    service_namespace=appscaling.ServiceNamespace.LAMBDA,
    max_capacity=100,
    min_capacity=10,
    resource_id=f"function:{handler.functionName}:{fnVer.version}",
    scalable_dimension="lambda:function:ProvisionedConcurrency"
)

target.scale_to_track_metric("PceTracking",
    target_value=0.9,
    predefined_metric=appscaling.PredefinedMetric.LAMBDA_PROVISIONED_CONCURRENCY_UTILIZATION
)
```

### ElastiCache Redis shards scaling with target value

```python
shards_scalable_target = appscaling.ScalableTarget(self, "ElastiCacheRedisShardsScalableTarget",
    service_namespace=appscaling.ServiceNamespace.ELASTICACHE,
    scalable_dimension="elasticache:replication-group:NodeGroups",
    min_capacity=2,
    max_capacity=10,
    resource_id="replication-group/main-cluster"
)

shards_scalable_target.scale_to_track_metric("ElastiCacheRedisShardsCPUUtilization",
    target_value=20,
    predefined_metric=appscaling.PredefinedMetric.ELASTICACHE_PRIMARY_ENGINE_CPU_UTILIZATION
)
```

### SageMaker variant provisioned concurrency utilization with target value

```python
target = appscaling.ScalableTarget(self, "SageMakerVariantScalableTarget",
    service_namespace=appscaling.ServiceNamespace.SAGEMAKER,
    scalable_dimension="sagemaker:variant:DesiredProvisionedConcurrency",
    min_capacity=2,
    max_capacity=10,
    resource_id="endpoint/MyEndpoint/variant/MyVariant"
)

target.scale_to_track_metric("SageMakerVariantProvisionedConcurrencyUtilization",
    target_value=0.9,
    predefined_metric=appscaling.PredefinedMetric.SAGEMAKER_VARIANT_PROVISIONED_CONCURRENCY_UTILIZATION
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
    Duration as _Duration_4839e8c3,
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    IResource as _IResource_c80c4260,
    Resource as _Resource_45bc6135,
    TimeZone as _TimeZone_cdd72ac9,
    TreeInspector as _TreeInspector_488e0dd5,
)
from ..aws_cloudwatch import Alarm as _Alarm_9fbab1f1, IMetric as _IMetric_c7fd29de
from ..aws_iam import (
    IRole as _IRole_235f5d8e, PolicyStatement as _PolicyStatement_0fe33853
)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_applicationautoscaling.AdjustmentTier",
    jsii_struct_bases=[],
    name_mapping={
        "adjustment": "adjustment",
        "lower_bound": "lowerBound",
        "upper_bound": "upperBound",
    },
)
class AdjustmentTier:
    def __init__(
        self,
        *,
        adjustment: jsii.Number,
        lower_bound: typing.Optional[jsii.Number] = None,
        upper_bound: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''An adjustment.

        :param adjustment: What number to adjust the capacity with. The number is interpeted as an added capacity, a new fixed capacity or an added percentage depending on the AdjustmentType value of the StepScalingPolicy. Can be positive or negative.
        :param lower_bound: Lower bound where this scaling tier applies. The scaling tier applies if the difference between the metric value and its alarm threshold is higher than this value. Default: -Infinity if this is the first tier, otherwise the upperBound of the previous tier
        :param upper_bound: Upper bound where this scaling tier applies. The scaling tier applies if the difference between the metric value and its alarm threshold is lower than this value. Default: +Infinity

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_applicationautoscaling as appscaling
            
            adjustment_tier = appscaling.AdjustmentTier(
                adjustment=123,
            
                # the properties below are optional
                lower_bound=123,
                upper_bound=123
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e92856d6925eb7a98c28e5624a5be0c6b4b99fe091967d8069251411469217fd)
            check_type(argname="argument adjustment", value=adjustment, expected_type=type_hints["adjustment"])
            check_type(argname="argument lower_bound", value=lower_bound, expected_type=type_hints["lower_bound"])
            check_type(argname="argument upper_bound", value=upper_bound, expected_type=type_hints["upper_bound"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "adjustment": adjustment,
        }
        if lower_bound is not None:
            self._values["lower_bound"] = lower_bound
        if upper_bound is not None:
            self._values["upper_bound"] = upper_bound

    @builtins.property
    def adjustment(self) -> jsii.Number:
        '''What number to adjust the capacity with.

        The number is interpeted as an added capacity, a new fixed capacity or an
        added percentage depending on the AdjustmentType value of the
        StepScalingPolicy.

        Can be positive or negative.
        '''
        result = self._values.get("adjustment")
        assert result is not None, "Required property 'adjustment' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def lower_bound(self) -> typing.Optional[jsii.Number]:
        '''Lower bound where this scaling tier applies.

        The scaling tier applies if the difference between the metric
        value and its alarm threshold is higher than this value.

        :default: -Infinity if this is the first tier, otherwise the upperBound of the previous tier
        '''
        result = self._values.get("lower_bound")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def upper_bound(self) -> typing.Optional[jsii.Number]:
        '''Upper bound where this scaling tier applies.

        The scaling tier applies if the difference between the metric
        value and its alarm threshold is lower than this value.

        :default: +Infinity
        '''
        result = self._values.get("upper_bound")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AdjustmentTier(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_applicationautoscaling.AdjustmentType")
class AdjustmentType(enum.Enum):
    '''How adjustment numbers are interpreted.

    :exampleMetadata: infused

    Example::

        # capacity: ScalableAttribute
        # cpu_utilization: cloudwatch.Metric
        
        
        capacity.scale_on_metric("ScaleToCPU",
            metric=cpu_utilization,
            scaling_steps=[appscaling.ScalingInterval(upper=10, change=-1), appscaling.ScalingInterval(lower=50, change=+1), appscaling.ScalingInterval(lower=70, change=+3)
            ],
        
            # Change this to AdjustmentType.PercentChangeInCapacity to interpret the
            # 'change' numbers before as percentages instead of capacity counts.
            adjustment_type=appscaling.AdjustmentType.CHANGE_IN_CAPACITY
        )
    '''

    CHANGE_IN_CAPACITY = "CHANGE_IN_CAPACITY"
    '''Add the adjustment number to the current capacity.

    A positive number increases capacity, a negative number decreases capacity.
    '''
    PERCENT_CHANGE_IN_CAPACITY = "PERCENT_CHANGE_IN_CAPACITY"
    '''Add this percentage of the current capacity to itself.

    The number must be between -100 and 100; a positive number increases
    capacity and a negative number decreases it.
    '''
    EXACT_CAPACITY = "EXACT_CAPACITY"
    '''Make the capacity equal to the exact number given.'''


class BaseScalableAttribute(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="aws-cdk-lib.aws_applicationautoscaling.BaseScalableAttribute",
):
    '''Represent an attribute for which autoscaling can be configured.

    This class is basically a light wrapper around ScalableTarget, but with
    all methods protected instead of public so they can be selectively
    exposed and/or more specific versions of them can be exposed by derived
    classes for individual services support autoscaling.

    Typical use cases:

    - Hide away the PredefinedMetric enum for target tracking policies.
    - Don't expose all scaling methods (for example Dynamo tables don't support
      Step Scaling, so the Dynamo subclass won't expose this method).
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        dimension: builtins.str,
        resource_id: builtins.str,
        role: _IRole_235f5d8e,
        service_namespace: "ServiceNamespace",
        max_capacity: jsii.Number,
        min_capacity: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param dimension: Scalable dimension of the attribute.
        :param resource_id: Resource ID of the attribute.
        :param role: Role to use for scaling.
        :param service_namespace: Service namespace of the scalable attribute.
        :param max_capacity: Maximum capacity to scale to.
        :param min_capacity: Minimum capacity to scale to. Default: 1
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8600affa38d3ad7a26371cf54d8508b09daff72f32b8b1da067e86834ec3575c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = BaseScalableAttributeProps(
            dimension=dimension,
            resource_id=resource_id,
            role=role,
            service_namespace=service_namespace,
            max_capacity=max_capacity,
            min_capacity=min_capacity,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="doScaleOnMetric")
    def _do_scale_on_metric(
        self,
        id: builtins.str,
        *,
        metric: _IMetric_c7fd29de,
        scaling_steps: typing.Sequence[typing.Union["ScalingInterval", typing.Dict[builtins.str, typing.Any]]],
        adjustment_type: typing.Optional[AdjustmentType] = None,
        cooldown: typing.Optional[_Duration_4839e8c3] = None,
        datapoints_to_alarm: typing.Optional[jsii.Number] = None,
        evaluation_periods: typing.Optional[jsii.Number] = None,
        metric_aggregation_type: typing.Optional["MetricAggregationType"] = None,
        min_adjustment_magnitude: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Scale out or in based on a metric value.

        :param id: -
        :param metric: Metric to scale on.
        :param scaling_steps: The intervals for scaling. Maps a range of metric values to a particular scaling behavior. Must be between 2 and 40 steps.
        :param adjustment_type: How the adjustment numbers inside 'intervals' are interpreted. Default: ChangeInCapacity
        :param cooldown: Grace period after scaling activity. Subsequent scale outs during the cooldown period are squashed so that only the biggest scale out happens. Subsequent scale ins during the cooldown period are ignored. Default: No cooldown period
        :param datapoints_to_alarm: The number of data points out of the evaluation periods that must be breaching to trigger a scaling action. Creates an "M out of N" alarm, where this property is the M and the value set for ``evaluationPeriods`` is the N value. Only has meaning if ``evaluationPeriods != 1``. Default: - Same as ``evaluationPeriods``
        :param evaluation_periods: How many evaluation periods of the metric to wait before triggering a scaling action. Raising this value can be used to smooth out the metric, at the expense of slower response times. If ``datapointsToAlarm`` is not set, then all data points in the evaluation period must meet the criteria to trigger a scaling action. Default: 1
        :param metric_aggregation_type: Aggregation to apply to all data points over the evaluation periods. Only has meaning if ``evaluationPeriods != 1``. Default: - The statistic from the metric if applicable (MIN, MAX, AVERAGE), otherwise AVERAGE.
        :param min_adjustment_magnitude: Minimum absolute number to adjust capacity with as result of percentage scaling. Only when using AdjustmentType = PercentChangeInCapacity, this number controls the minimum absolute effect size. Default: No minimum scaling effect
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f860eecb918f3d194ec191f1e14f6db4e310f7d65df849bae6100f4b122fb99)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = BasicStepScalingPolicyProps(
            metric=metric,
            scaling_steps=scaling_steps,
            adjustment_type=adjustment_type,
            cooldown=cooldown,
            datapoints_to_alarm=datapoints_to_alarm,
            evaluation_periods=evaluation_periods,
            metric_aggregation_type=metric_aggregation_type,
            min_adjustment_magnitude=min_adjustment_magnitude,
        )

        return typing.cast(None, jsii.invoke(self, "doScaleOnMetric", [id, props]))

    @jsii.member(jsii_name="doScaleOnSchedule")
    def _do_scale_on_schedule(
        self,
        id: builtins.str,
        *,
        schedule: "Schedule",
        end_time: typing.Optional[datetime.datetime] = None,
        max_capacity: typing.Optional[jsii.Number] = None,
        min_capacity: typing.Optional[jsii.Number] = None,
        start_time: typing.Optional[datetime.datetime] = None,
        time_zone: typing.Optional[_TimeZone_cdd72ac9] = None,
    ) -> None:
        '''Scale out or in based on time.

        :param id: -
        :param schedule: When to perform this action.
        :param end_time: When this scheduled action expires. Default: The rule never expires.
        :param max_capacity: The new maximum capacity. During the scheduled time, the current capacity is above the maximum capacity, Application Auto Scaling scales in to the maximum capacity. At least one of maxCapacity and minCapacity must be supplied. Default: No new maximum capacity
        :param min_capacity: The new minimum capacity. During the scheduled time, if the current capacity is below the minimum capacity, Application Auto Scaling scales out to the minimum capacity. At least one of maxCapacity and minCapacity must be supplied. Default: No new minimum capacity
        :param start_time: When this scheduled action becomes active. Default: The rule is activate immediately
        :param time_zone: The time zone used when referring to the date and time of a scheduled action, when the scheduled action uses an at or cron expression. Default: - UTC
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82bcc29e64984d150edcca413653e7216fd0245b92c71db37506d1a93e054222)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ScalingSchedule(
            schedule=schedule,
            end_time=end_time,
            max_capacity=max_capacity,
            min_capacity=min_capacity,
            start_time=start_time,
            time_zone=time_zone,
        )

        return typing.cast(None, jsii.invoke(self, "doScaleOnSchedule", [id, props]))

    @jsii.member(jsii_name="doScaleToTrackMetric")
    def _do_scale_to_track_metric(
        self,
        id: builtins.str,
        *,
        target_value: jsii.Number,
        custom_metric: typing.Optional[_IMetric_c7fd29de] = None,
        predefined_metric: typing.Optional["PredefinedMetric"] = None,
        resource_label: typing.Optional[builtins.str] = None,
        disable_scale_in: typing.Optional[builtins.bool] = None,
        policy_name: typing.Optional[builtins.str] = None,
        scale_in_cooldown: typing.Optional[_Duration_4839e8c3] = None,
        scale_out_cooldown: typing.Optional[_Duration_4839e8c3] = None,
    ) -> None:
        '''Scale out or in in order to keep a metric around a target value.

        :param id: -
        :param target_value: The target value for the metric.
        :param custom_metric: A custom metric for application autoscaling. The metric must track utilization. Scaling out will happen if the metric is higher than the target value, scaling in will happen in the metric is lower than the target value. Exactly one of customMetric or predefinedMetric must be specified. Default: - No custom metric.
        :param predefined_metric: A predefined metric for application autoscaling. The metric must track utilization. Scaling out will happen if the metric is higher than the target value, scaling in will happen in the metric is lower than the target value. Exactly one of customMetric or predefinedMetric must be specified. Default: - No predefined metrics.
        :param resource_label: Identify the resource associated with the metric type. Only used for predefined metric ALBRequestCountPerTarget. Example value: ``app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>`` Default: - No resource label.
        :param disable_scale_in: Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won't remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the scalable resource. Default: false
        :param policy_name: A name for the scaling policy. Default: - Automatically generated name.
        :param scale_in_cooldown: Period after a scale in activity completes before another scale in activity can start. Default: Duration.seconds(300) for the following scalable targets: ECS services, Spot Fleet requests, EMR clusters, AppStream 2.0 fleets, Aurora DB clusters, Amazon SageMaker endpoint variants, Custom resources. For all other scalable targets, the default value is Duration.seconds(0): DynamoDB tables, DynamoDB global secondary indexes, Amazon Comprehend document classification endpoints, Lambda provisioned concurrency
        :param scale_out_cooldown: Period after a scale out activity completes before another scale out activity can start. Default: Duration.seconds(300) for the following scalable targets: ECS services, Spot Fleet requests, EMR clusters, AppStream 2.0 fleets, Aurora DB clusters, Amazon SageMaker endpoint variants, Custom resources. For all other scalable targets, the default value is Duration.seconds(0): DynamoDB tables, DynamoDB global secondary indexes, Amazon Comprehend document classification endpoints, Lambda provisioned concurrency
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d955311dd160aaa4e3b40a01c140d69bad0856804ffd0b3dbff8b52a628ab88f)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = BasicTargetTrackingScalingPolicyProps(
            target_value=target_value,
            custom_metric=custom_metric,
            predefined_metric=predefined_metric,
            resource_label=resource_label,
            disable_scale_in=disable_scale_in,
            policy_name=policy_name,
            scale_in_cooldown=scale_in_cooldown,
            scale_out_cooldown=scale_out_cooldown,
        )

        return typing.cast(None, jsii.invoke(self, "doScaleToTrackMetric", [id, props]))

    @builtins.property
    @jsii.member(jsii_name="props")
    def _props(self) -> "BaseScalableAttributeProps":
        return typing.cast("BaseScalableAttributeProps", jsii.get(self, "props"))


class _BaseScalableAttributeProxy(BaseScalableAttribute):
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, BaseScalableAttribute).__jsii_proxy_class__ = lambda : _BaseScalableAttributeProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_applicationautoscaling.BaseTargetTrackingProps",
    jsii_struct_bases=[],
    name_mapping={
        "disable_scale_in": "disableScaleIn",
        "policy_name": "policyName",
        "scale_in_cooldown": "scaleInCooldown",
        "scale_out_cooldown": "scaleOutCooldown",
    },
)
class BaseTargetTrackingProps:
    def __init__(
        self,
        *,
        disable_scale_in: typing.Optional[builtins.bool] = None,
        policy_name: typing.Optional[builtins.str] = None,
        scale_in_cooldown: typing.Optional[_Duration_4839e8c3] = None,
        scale_out_cooldown: typing.Optional[_Duration_4839e8c3] = None,
    ) -> None:
        '''Base interface for target tracking props.

        Contains the attributes that are common to target tracking policies,
        except the ones relating to the metric and to the scalable target.

        This interface is reused by more specific target tracking props objects
        in other services.

        :param disable_scale_in: Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won't remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the scalable resource. Default: false
        :param policy_name: A name for the scaling policy. Default: - Automatically generated name.
        :param scale_in_cooldown: Period after a scale in activity completes before another scale in activity can start. Default: Duration.seconds(300) for the following scalable targets: ECS services, Spot Fleet requests, EMR clusters, AppStream 2.0 fleets, Aurora DB clusters, Amazon SageMaker endpoint variants, Custom resources. For all other scalable targets, the default value is Duration.seconds(0): DynamoDB tables, DynamoDB global secondary indexes, Amazon Comprehend document classification endpoints, Lambda provisioned concurrency
        :param scale_out_cooldown: Period after a scale out activity completes before another scale out activity can start. Default: Duration.seconds(300) for the following scalable targets: ECS services, Spot Fleet requests, EMR clusters, AppStream 2.0 fleets, Aurora DB clusters, Amazon SageMaker endpoint variants, Custom resources. For all other scalable targets, the default value is Duration.seconds(0): DynamoDB tables, DynamoDB global secondary indexes, Amazon Comprehend document classification endpoints, Lambda provisioned concurrency

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk as cdk
            from aws_cdk import aws_applicationautoscaling as appscaling
            
            base_target_tracking_props = appscaling.BaseTargetTrackingProps(
                disable_scale_in=False,
                policy_name="policyName",
                scale_in_cooldown=cdk.Duration.minutes(30),
                scale_out_cooldown=cdk.Duration.minutes(30)
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99ba5c9c979402884414e9574843c640de78dc18e7837b243b496ed4c150a1b1)
            check_type(argname="argument disable_scale_in", value=disable_scale_in, expected_type=type_hints["disable_scale_in"])
            check_type(argname="argument policy_name", value=policy_name, expected_type=type_hints["policy_name"])
            check_type(argname="argument scale_in_cooldown", value=scale_in_cooldown, expected_type=type_hints["scale_in_cooldown"])
            check_type(argname="argument scale_out_cooldown", value=scale_out_cooldown, expected_type=type_hints["scale_out_cooldown"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if disable_scale_in is not None:
            self._values["disable_scale_in"] = disable_scale_in
        if policy_name is not None:
            self._values["policy_name"] = policy_name
        if scale_in_cooldown is not None:
            self._values["scale_in_cooldown"] = scale_in_cooldown
        if scale_out_cooldown is not None:
            self._values["scale_out_cooldown"] = scale_out_cooldown

    @builtins.property
    def disable_scale_in(self) -> typing.Optional[builtins.bool]:
        '''Indicates whether scale in by the target tracking policy is disabled.

        If the value is true, scale in is disabled and the target tracking policy
        won't remove capacity from the scalable resource. Otherwise, scale in is
        enabled and the target tracking policy can remove capacity from the
        scalable resource.

        :default: false
        '''
        result = self._values.get("disable_scale_in")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def policy_name(self) -> typing.Optional[builtins.str]:
        '''A name for the scaling policy.

        :default: - Automatically generated name.
        '''
        result = self._values.get("policy_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scale_in_cooldown(self) -> typing.Optional[_Duration_4839e8c3]:
        '''Period after a scale in activity completes before another scale in activity can start.

        :default:

        Duration.seconds(300) for the following scalable targets: ECS services,
        Spot Fleet requests, EMR clusters, AppStream 2.0 fleets, Aurora DB clusters,
        Amazon SageMaker endpoint variants, Custom resources. For all other scalable
        targets, the default value is Duration.seconds(0): DynamoDB tables, DynamoDB
        global secondary indexes, Amazon Comprehend document classification endpoints,
        Lambda provisioned concurrency
        '''
        result = self._values.get("scale_in_cooldown")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def scale_out_cooldown(self) -> typing.Optional[_Duration_4839e8c3]:
        '''Period after a scale out activity completes before another scale out activity can start.

        :default:

        Duration.seconds(300) for the following scalable targets: ECS services,
        Spot Fleet requests, EMR clusters, AppStream 2.0 fleets, Aurora DB clusters,
        Amazon SageMaker endpoint variants, Custom resources. For all other scalable
        targets, the default value is Duration.seconds(0): DynamoDB tables, DynamoDB
        global secondary indexes, Amazon Comprehend document classification endpoints,
        Lambda provisioned concurrency
        '''
        result = self._values.get("scale_out_cooldown")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BaseTargetTrackingProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_applicationautoscaling.BasicStepScalingPolicyProps",
    jsii_struct_bases=[],
    name_mapping={
        "metric": "metric",
        "scaling_steps": "scalingSteps",
        "adjustment_type": "adjustmentType",
        "cooldown": "cooldown",
        "datapoints_to_alarm": "datapointsToAlarm",
        "evaluation_periods": "evaluationPeriods",
        "metric_aggregation_type": "metricAggregationType",
        "min_adjustment_magnitude": "minAdjustmentMagnitude",
    },
)
class BasicStepScalingPolicyProps:
    def __init__(
        self,
        *,
        metric: _IMetric_c7fd29de,
        scaling_steps: typing.Sequence[typing.Union["ScalingInterval", typing.Dict[builtins.str, typing.Any]]],
        adjustment_type: typing.Optional[AdjustmentType] = None,
        cooldown: typing.Optional[_Duration_4839e8c3] = None,
        datapoints_to_alarm: typing.Optional[jsii.Number] = None,
        evaluation_periods: typing.Optional[jsii.Number] = None,
        metric_aggregation_type: typing.Optional["MetricAggregationType"] = None,
        min_adjustment_magnitude: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param metric: Metric to scale on.
        :param scaling_steps: The intervals for scaling. Maps a range of metric values to a particular scaling behavior. Must be between 2 and 40 steps.
        :param adjustment_type: How the adjustment numbers inside 'intervals' are interpreted. Default: ChangeInCapacity
        :param cooldown: Grace period after scaling activity. Subsequent scale outs during the cooldown period are squashed so that only the biggest scale out happens. Subsequent scale ins during the cooldown period are ignored. Default: No cooldown period
        :param datapoints_to_alarm: The number of data points out of the evaluation periods that must be breaching to trigger a scaling action. Creates an "M out of N" alarm, where this property is the M and the value set for ``evaluationPeriods`` is the N value. Only has meaning if ``evaluationPeriods != 1``. Default: - Same as ``evaluationPeriods``
        :param evaluation_periods: How many evaluation periods of the metric to wait before triggering a scaling action. Raising this value can be used to smooth out the metric, at the expense of slower response times. If ``datapointsToAlarm`` is not set, then all data points in the evaluation period must meet the criteria to trigger a scaling action. Default: 1
        :param metric_aggregation_type: Aggregation to apply to all data points over the evaluation periods. Only has meaning if ``evaluationPeriods != 1``. Default: - The statistic from the metric if applicable (MIN, MAX, AVERAGE), otherwise AVERAGE.
        :param min_adjustment_magnitude: Minimum absolute number to adjust capacity with as result of percentage scaling. Only when using AdjustmentType = PercentChangeInCapacity, this number controls the minimum absolute effect size. Default: No minimum scaling effect

        :exampleMetadata: infused

        Example::

            # capacity: ScalableAttribute
            # cpu_utilization: cloudwatch.Metric
            
            
            capacity.scale_on_metric("ScaleToCPU",
                metric=cpu_utilization,
                scaling_steps=[appscaling.ScalingInterval(upper=10, change=-1), appscaling.ScalingInterval(lower=50, change=+1), appscaling.ScalingInterval(lower=70, change=+3)
                ],
            
                # Change this to AdjustmentType.PercentChangeInCapacity to interpret the
                # 'change' numbers before as percentages instead of capacity counts.
                adjustment_type=appscaling.AdjustmentType.CHANGE_IN_CAPACITY
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85315ee41e5c634ea9c93ccb7019a42d1823a8b52cb598aba6a6c93df29956ec)
            check_type(argname="argument metric", value=metric, expected_type=type_hints["metric"])
            check_type(argname="argument scaling_steps", value=scaling_steps, expected_type=type_hints["scaling_steps"])
            check_type(argname="argument adjustment_type", value=adjustment_type, expected_type=type_hints["adjustment_type"])
            check_type(argname="argument cooldown", value=cooldown, expected_type=type_hints["cooldown"])
            check_type(argname="argument datapoints_to_alarm", value=datapoints_to_alarm, expected_type=type_hints["datapoints_to_alarm"])
            check_type(argname="argument evaluation_periods", value=evaluation_periods, expected_type=type_hints["evaluation_periods"])
            check_type(argname="argument metric_aggregation_type", value=metric_aggregation_type, expected_type=type_hints["metric_aggregation_type"])
            check_type(argname="argument min_adjustment_magnitude", value=min_adjustment_magnitude, expected_type=type_hints["min_adjustment_magnitude"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "metric": metric,
            "scaling_steps": scaling_steps,
        }
        if adjustment_type is not None:
            self._values["adjustment_type"] = adjustment_type
        if cooldown is not None:
            self._values["cooldown"] = cooldown
        if datapoints_to_alarm is not None:
            self._values["datapoints_to_alarm"] = datapoints_to_alarm
        if evaluation_periods is not None:
            self._values["evaluation_periods"] = evaluation_periods
        if metric_aggregation_type is not None:
            self._values["metric_aggregation_type"] = metric_aggregation_type
        if min_adjustment_magnitude is not None:
            self._values["min_adjustment_magnitude"] = min_adjustment_magnitude

    @builtins.property
    def metric(self) -> _IMetric_c7fd29de:
        '''Metric to scale on.'''
        result = self._values.get("metric")
        assert result is not None, "Required property 'metric' is missing"
        return typing.cast(_IMetric_c7fd29de, result)

    @builtins.property
    def scaling_steps(self) -> typing.List["ScalingInterval"]:
        '''The intervals for scaling.

        Maps a range of metric values to a particular scaling behavior.

        Must be between 2 and 40 steps.
        '''
        result = self._values.get("scaling_steps")
        assert result is not None, "Required property 'scaling_steps' is missing"
        return typing.cast(typing.List["ScalingInterval"], result)

    @builtins.property
    def adjustment_type(self) -> typing.Optional[AdjustmentType]:
        '''How the adjustment numbers inside 'intervals' are interpreted.

        :default: ChangeInCapacity
        '''
        result = self._values.get("adjustment_type")
        return typing.cast(typing.Optional[AdjustmentType], result)

    @builtins.property
    def cooldown(self) -> typing.Optional[_Duration_4839e8c3]:
        '''Grace period after scaling activity.

        Subsequent scale outs during the cooldown period are squashed so that only
        the biggest scale out happens.

        Subsequent scale ins during the cooldown period are ignored.

        :default: No cooldown period

        :see: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_StepScalingPolicyConfiguration.html
        '''
        result = self._values.get("cooldown")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def datapoints_to_alarm(self) -> typing.Optional[jsii.Number]:
        '''The number of data points out of the evaluation periods that must be breaching to trigger a scaling action.

        Creates an "M out of N" alarm, where this property is the M and the value set for
        ``evaluationPeriods`` is the N value.

        Only has meaning if ``evaluationPeriods != 1``.

        :default: - Same as ``evaluationPeriods``
        '''
        result = self._values.get("datapoints_to_alarm")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def evaluation_periods(self) -> typing.Optional[jsii.Number]:
        '''How many evaluation periods of the metric to wait before triggering a scaling action.

        Raising this value can be used to smooth out the metric, at the expense
        of slower response times.

        If ``datapointsToAlarm`` is not set, then all data points in the evaluation period
        must meet the criteria to trigger a scaling action.

        :default: 1
        '''
        result = self._values.get("evaluation_periods")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def metric_aggregation_type(self) -> typing.Optional["MetricAggregationType"]:
        '''Aggregation to apply to all data points over the evaluation periods.

        Only has meaning if ``evaluationPeriods != 1``.

        :default: - The statistic from the metric if applicable (MIN, MAX, AVERAGE), otherwise AVERAGE.
        '''
        result = self._values.get("metric_aggregation_type")
        return typing.cast(typing.Optional["MetricAggregationType"], result)

    @builtins.property
    def min_adjustment_magnitude(self) -> typing.Optional[jsii.Number]:
        '''Minimum absolute number to adjust capacity with as result of percentage scaling.

        Only when using AdjustmentType = PercentChangeInCapacity, this number controls
        the minimum absolute effect size.

        :default: No minimum scaling effect
        '''
        result = self._values.get("min_adjustment_magnitude")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BasicStepScalingPolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_applicationautoscaling.BasicTargetTrackingScalingPolicyProps",
    jsii_struct_bases=[BaseTargetTrackingProps],
    name_mapping={
        "disable_scale_in": "disableScaleIn",
        "policy_name": "policyName",
        "scale_in_cooldown": "scaleInCooldown",
        "scale_out_cooldown": "scaleOutCooldown",
        "target_value": "targetValue",
        "custom_metric": "customMetric",
        "predefined_metric": "predefinedMetric",
        "resource_label": "resourceLabel",
    },
)
class BasicTargetTrackingScalingPolicyProps(BaseTargetTrackingProps):
    def __init__(
        self,
        *,
        disable_scale_in: typing.Optional[builtins.bool] = None,
        policy_name: typing.Optional[builtins.str] = None,
        scale_in_cooldown: typing.Optional[_Duration_4839e8c3] = None,
        scale_out_cooldown: typing.Optional[_Duration_4839e8c3] = None,
        target_value: jsii.Number,
        custom_metric: typing.Optional[_IMetric_c7fd29de] = None,
        predefined_metric: typing.Optional["PredefinedMetric"] = None,
        resource_label: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for a Target Tracking policy that include the metric but exclude the target.

        :param disable_scale_in: Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won't remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the scalable resource. Default: false
        :param policy_name: A name for the scaling policy. Default: - Automatically generated name.
        :param scale_in_cooldown: Period after a scale in activity completes before another scale in activity can start. Default: Duration.seconds(300) for the following scalable targets: ECS services, Spot Fleet requests, EMR clusters, AppStream 2.0 fleets, Aurora DB clusters, Amazon SageMaker endpoint variants, Custom resources. For all other scalable targets, the default value is Duration.seconds(0): DynamoDB tables, DynamoDB global secondary indexes, Amazon Comprehend document classification endpoints, Lambda provisioned concurrency
        :param scale_out_cooldown: Period after a scale out activity completes before another scale out activity can start. Default: Duration.seconds(300) for the following scalable targets: ECS services, Spot Fleet requests, EMR clusters, AppStream 2.0 fleets, Aurora DB clusters, Amazon SageMaker endpoint variants, Custom resources. For all other scalable targets, the default value is Duration.seconds(0): DynamoDB tables, DynamoDB global secondary indexes, Amazon Comprehend document classification endpoints, Lambda provisioned concurrency
        :param target_value: The target value for the metric.
        :param custom_metric: A custom metric for application autoscaling. The metric must track utilization. Scaling out will happen if the metric is higher than the target value, scaling in will happen in the metric is lower than the target value. Exactly one of customMetric or predefinedMetric must be specified. Default: - No custom metric.
        :param predefined_metric: A predefined metric for application autoscaling. The metric must track utilization. Scaling out will happen if the metric is higher than the target value, scaling in will happen in the metric is lower than the target value. Exactly one of customMetric or predefinedMetric must be specified. Default: - No predefined metrics.
        :param resource_label: Identify the resource associated with the metric type. Only used for predefined metric ALBRequestCountPerTarget. Example value: ``app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>`` Default: - No resource label.

        :exampleMetadata: infused

        Example::

            shards_scalable_target = appscaling.ScalableTarget(self, "ElastiCacheRedisShardsScalableTarget",
                service_namespace=appscaling.ServiceNamespace.ELASTICACHE,
                scalable_dimension="elasticache:replication-group:NodeGroups",
                min_capacity=2,
                max_capacity=10,
                resource_id="replication-group/main-cluster"
            )
            
            shards_scalable_target.scale_to_track_metric("ElastiCacheRedisShardsCPUUtilization",
                target_value=20,
                predefined_metric=appscaling.PredefinedMetric.ELASTICACHE_PRIMARY_ENGINE_CPU_UTILIZATION
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9c62810084b1b26b891f3d2a3faa25ac5bb982334bd2e6b42e142d8a7402689)
            check_type(argname="argument disable_scale_in", value=disable_scale_in, expected_type=type_hints["disable_scale_in"])
            check_type(argname="argument policy_name", value=policy_name, expected_type=type_hints["policy_name"])
            check_type(argname="argument scale_in_cooldown", value=scale_in_cooldown, expected_type=type_hints["scale_in_cooldown"])
            check_type(argname="argument scale_out_cooldown", value=scale_out_cooldown, expected_type=type_hints["scale_out_cooldown"])
            check_type(argname="argument target_value", value=target_value, expected_type=type_hints["target_value"])
            check_type(argname="argument custom_metric", value=custom_metric, expected_type=type_hints["custom_metric"])
            check_type(argname="argument predefined_metric", value=predefined_metric, expected_type=type_hints["predefined_metric"])
            check_type(argname="argument resource_label", value=resource_label, expected_type=type_hints["resource_label"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "target_value": target_value,
        }
        if disable_scale_in is not None:
            self._values["disable_scale_in"] = disable_scale_in
        if policy_name is not None:
            self._values["policy_name"] = policy_name
        if scale_in_cooldown is not None:
            self._values["scale_in_cooldown"] = scale_in_cooldown
        if scale_out_cooldown is not None:
            self._values["scale_out_cooldown"] = scale_out_cooldown
        if custom_metric is not None:
            self._values["custom_metric"] = custom_metric
        if predefined_metric is not None:
            self._values["predefined_metric"] = predefined_metric
        if resource_label is not None:
            self._values["resource_label"] = resource_label

    @builtins.property
    def disable_scale_in(self) -> typing.Optional[builtins.bool]:
        '''Indicates whether scale in by the target tracking policy is disabled.

        If the value is true, scale in is disabled and the target tracking policy
        won't remove capacity from the scalable resource. Otherwise, scale in is
        enabled and the target tracking policy can remove capacity from the
        scalable resource.

        :default: false
        '''
        result = self._values.get("disable_scale_in")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def policy_name(self) -> typing.Optional[builtins.str]:
        '''A name for the scaling policy.

        :default: - Automatically generated name.
        '''
        result = self._values.get("policy_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scale_in_cooldown(self) -> typing.Optional[_Duration_4839e8c3]:
        '''Period after a scale in activity completes before another scale in activity can start.

        :default:

        Duration.seconds(300) for the following scalable targets: ECS services,
        Spot Fleet requests, EMR clusters, AppStream 2.0 fleets, Aurora DB clusters,
        Amazon SageMaker endpoint variants, Custom resources. For all other scalable
        targets, the default value is Duration.seconds(0): DynamoDB tables, DynamoDB
        global secondary indexes, Amazon Comprehend document classification endpoints,
        Lambda provisioned concurrency
        '''
        result = self._values.get("scale_in_cooldown")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def scale_out_cooldown(self) -> typing.Optional[_Duration_4839e8c3]:
        '''Period after a scale out activity completes before another scale out activity can start.

        :default:

        Duration.seconds(300) for the following scalable targets: ECS services,
        Spot Fleet requests, EMR clusters, AppStream 2.0 fleets, Aurora DB clusters,
        Amazon SageMaker endpoint variants, Custom resources. For all other scalable
        targets, the default value is Duration.seconds(0): DynamoDB tables, DynamoDB
        global secondary indexes, Amazon Comprehend document classification endpoints,
        Lambda provisioned concurrency
        '''
        result = self._values.get("scale_out_cooldown")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def target_value(self) -> jsii.Number:
        '''The target value for the metric.'''
        result = self._values.get("target_value")
        assert result is not None, "Required property 'target_value' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def custom_metric(self) -> typing.Optional[_IMetric_c7fd29de]:
        '''A custom metric for application autoscaling.

        The metric must track utilization. Scaling out will happen if the metric is higher than
        the target value, scaling in will happen in the metric is lower than the target value.

        Exactly one of customMetric or predefinedMetric must be specified.

        :default: - No custom metric.
        '''
        result = self._values.get("custom_metric")
        return typing.cast(typing.Optional[_IMetric_c7fd29de], result)

    @builtins.property
    def predefined_metric(self) -> typing.Optional["PredefinedMetric"]:
        '''A predefined metric for application autoscaling.

        The metric must track utilization. Scaling out will happen if the metric is higher than
        the target value, scaling in will happen in the metric is lower than the target value.

        Exactly one of customMetric or predefinedMetric must be specified.

        :default: - No predefined metrics.
        '''
        result = self._values.get("predefined_metric")
        return typing.cast(typing.Optional["PredefinedMetric"], result)

    @builtins.property
    def resource_label(self) -> typing.Optional[builtins.str]:
        '''Identify the resource associated with the metric type.

        Only used for predefined metric ALBRequestCountPerTarget.

        Example value: ``app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>``

        :default: - No resource label.
        '''
        result = self._values.get("resource_label")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BasicTargetTrackingScalingPolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnScalableTarget(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_applicationautoscaling.CfnScalableTarget",
):
    '''The ``AWS::ApplicationAutoScaling::ScalableTarget`` resource specifies a resource that Application Auto Scaling can scale, such as an AWS::DynamoDB::Table or AWS::ECS::Service resource.

    For more information, see `Getting started <https://docs.aws.amazon.com/autoscaling/application/userguide/getting-started.html>`_ in the *Application Auto Scaling User Guide* .
    .. epigraph::

       If the resource that you want Application Auto Scaling to scale is not yet created in your account, add a dependency on the resource when registering it as a scalable target using the `DependsOn <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-dependson.html>`_ attribute.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html
    :cloudformationResource: AWS::ApplicationAutoScaling::ScalableTarget
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_applicationautoscaling as appscaling
        
        cfn_scalable_target = appscaling.CfnScalableTarget(self, "MyCfnScalableTarget",
            max_capacity=123,
            min_capacity=123,
            resource_id="resourceId",
            scalable_dimension="scalableDimension",
            service_namespace="serviceNamespace",
        
            # the properties below are optional
            role_arn="roleArn",
            scheduled_actions=[appscaling.CfnScalableTarget.ScheduledActionProperty(
                schedule="schedule",
                scheduled_action_name="scheduledActionName",
        
                # the properties below are optional
                end_time=Date(),
                scalable_target_action=appscaling.CfnScalableTarget.ScalableTargetActionProperty(
                    max_capacity=123,
                    min_capacity=123
                ),
                start_time=Date(),
                timezone="timezone"
            )],
            suspended_state=appscaling.CfnScalableTarget.SuspendedStateProperty(
                dynamic_scaling_in_suspended=False,
                dynamic_scaling_out_suspended=False,
                scheduled_scaling_suspended=False
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        max_capacity: jsii.Number,
        min_capacity: jsii.Number,
        resource_id: builtins.str,
        scalable_dimension: builtins.str,
        service_namespace: builtins.str,
        role_arn: typing.Optional[builtins.str] = None,
        scheduled_actions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnScalableTarget.ScheduledActionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        suspended_state: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnScalableTarget.SuspendedStateProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param max_capacity: The maximum value that you plan to scale out to. When a scaling policy is in effect, Application Auto Scaling can scale out (expand) as needed to the maximum capacity limit in response to changing demand.
        :param min_capacity: The minimum value that you plan to scale in to. When a scaling policy is in effect, Application Auto Scaling can scale in (contract) as needed to the minimum capacity limit in response to changing demand.
        :param resource_id: The identifier of the resource associated with the scalable target. This string consists of the resource type and unique identifier. - ECS service - The resource type is ``service`` and the unique identifier is the cluster name and service name. Example: ``service/my-cluster/my-service`` . - Spot Fleet - The resource type is ``spot-fleet-request`` and the unique identifier is the Spot Fleet request ID. Example: ``spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`` . - EMR cluster - The resource type is ``instancegroup`` and the unique identifier is the cluster ID and instance group ID. Example: ``instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0`` . - AppStream 2.0 fleet - The resource type is ``fleet`` and the unique identifier is the fleet name. Example: ``fleet/sample-fleet`` . - DynamoDB table - The resource type is ``table`` and the unique identifier is the table name. Example: ``table/my-table`` . - DynamoDB global secondary index - The resource type is ``index`` and the unique identifier is the index name. Example: ``table/my-table/index/my-table-index`` . - Aurora DB cluster - The resource type is ``cluster`` and the unique identifier is the cluster name. Example: ``cluster:my-db-cluster`` . - SageMaker endpoint variant - The resource type is ``variant`` and the unique identifier is the resource ID. Example: ``endpoint/my-end-point/variant/KMeansClustering`` . - Custom resources are not supported with a resource type. This parameter must specify the ``OutputValue`` from the CloudFormation template stack used to access the resources. The unique identifier is defined by the service provider. More information is available in our `GitHub repository <https://docs.aws.amazon.com/https://github.com/aws/aws-auto-scaling-custom-resource>`_ . - Amazon Comprehend document classification endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: ``arn:aws:comprehend:us-west-2:123456789012:document-classifier-endpoint/EXAMPLE`` . - Amazon Comprehend entity recognizer endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: ``arn:aws:comprehend:us-west-2:123456789012:entity-recognizer-endpoint/EXAMPLE`` . - Lambda provisioned concurrency - The resource type is ``function`` and the unique identifier is the function name with a function version or alias name suffix that is not ``$LATEST`` . Example: ``function:my-function:prod`` or ``function:my-function:1`` . - Amazon Keyspaces table - The resource type is ``table`` and the unique identifier is the table name. Example: ``keyspace/mykeyspace/table/mytable`` . - Amazon MSK cluster - The resource type and unique identifier are specified using the cluster ARN. Example: ``arn:aws:kafka:us-east-1:123456789012:cluster/demo-cluster-1/6357e0b2-0e6a-4b86-a0b4-70df934c2e31-5`` . - Amazon ElastiCache replication group - The resource type is ``replication-group`` and the unique identifier is the replication group name. Example: ``replication-group/mycluster`` . - Neptune cluster - The resource type is ``cluster`` and the unique identifier is the cluster name. Example: ``cluster:mycluster`` . - SageMaker serverless endpoint - The resource type is ``variant`` and the unique identifier is the resource ID. Example: ``endpoint/my-end-point/variant/KMeansClustering`` . - SageMaker inference component - The resource type is ``inference-component`` and the unique identifier is the resource ID. Example: ``inference-component/my-inference-component`` .
        :param scalable_dimension: The scalable dimension associated with the scalable target. This string consists of the service namespace, resource type, and scaling property. - ``ecs:service:DesiredCount`` - The desired task count of an ECS service. - ``elasticmapreduce:instancegroup:InstanceCount`` - The instance count of an EMR Instance Group. - ``ec2:spot-fleet-request:TargetCapacity`` - The target capacity of a Spot Fleet. - ``appstream:fleet:DesiredCapacity`` - The desired capacity of an AppStream 2.0 fleet. - ``dynamodb:table:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB table. - ``dynamodb:table:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB table. - ``dynamodb:index:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB global secondary index. - ``dynamodb:index:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB global secondary index. - ``rds:cluster:ReadReplicaCount`` - The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition and Aurora PostgreSQL-compatible edition. - ``sagemaker:variant:DesiredInstanceCount`` - The number of EC2 instances for a SageMaker model endpoint variant. - ``custom-resource:ResourceType:Property`` - The scalable dimension for a custom resource provided by your own application or service. - ``comprehend:document-classifier-endpoint:DesiredInferenceUnits`` - The number of inference units for an Amazon Comprehend document classification endpoint. - ``comprehend:entity-recognizer-endpoint:DesiredInferenceUnits`` - The number of inference units for an Amazon Comprehend entity recognizer endpoint. - ``lambda:function:ProvisionedConcurrency`` - The provisioned concurrency for a Lambda function. - ``cassandra:table:ReadCapacityUnits`` - The provisioned read capacity for an Amazon Keyspaces table. - ``cassandra:table:WriteCapacityUnits`` - The provisioned write capacity for an Amazon Keyspaces table. - ``kafka:broker-storage:VolumeSize`` - The provisioned volume size (in GiB) for brokers in an Amazon MSK cluster. - ``elasticache:replication-group:NodeGroups`` - The number of node groups for an Amazon ElastiCache replication group. - ``elasticache:replication-group:Replicas`` - The number of replicas per node group for an Amazon ElastiCache replication group. - ``neptune:cluster:ReadReplicaCount`` - The count of read replicas in an Amazon Neptune DB cluster. - ``sagemaker:variant:DesiredProvisionedConcurrency`` - The provisioned concurrency for a SageMaker serverless endpoint. - ``sagemaker:inference-component:DesiredCopyCount`` - The number of copies across an endpoint for a SageMaker inference component.
        :param service_namespace: The namespace of the AWS service that provides the resource, or a ``custom-resource`` .
        :param role_arn: Specify the Amazon Resource Name (ARN) of an Identity and Access Management (IAM) role that allows Application Auto Scaling to modify the scalable target on your behalf. This can be either an IAM service role that Application Auto Scaling can assume to make calls to other AWS resources on your behalf, or a service-linked role for the specified service. For more information, see `How Application Auto Scaling works with IAM <https://docs.aws.amazon.com/autoscaling/application/userguide/security_iam_service-with-iam.html>`_ in the *Application Auto Scaling User Guide* . To automatically create a service-linked role (recommended), specify the full ARN of the service-linked role in your stack template. To find the exact ARN of the service-linked role for your AWS or custom resource, see the `Service-linked roles <https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-service-linked-roles.html>`_ topic in the *Application Auto Scaling User Guide* . Look for the ARN in the table at the bottom of the page.
        :param scheduled_actions: The scheduled actions for the scalable target. Duplicates aren't allowed.
        :param suspended_state: An embedded object that contains attributes and attribute values that are used to suspend and resume automatic scaling. Setting the value of an attribute to ``true`` suspends the specified scaling activities. Setting it to ``false`` (default) resumes the specified scaling activities. *Suspension Outcomes* - For ``DynamicScalingInSuspended`` , while a suspension is in effect, all scale-in activities that are triggered by a scaling policy are suspended. - For ``DynamicScalingOutSuspended`` , while a suspension is in effect, all scale-out activities that are triggered by a scaling policy are suspended. - For ``ScheduledScalingSuspended`` , while a suspension is in effect, all scaling activities that involve scheduled actions are suspended.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b7828d7eb81c45c73ed70f9ac7ffe26699d8745e54d9a892440a20af1276437)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnScalableTargetProps(
            max_capacity=max_capacity,
            min_capacity=min_capacity,
            resource_id=resource_id,
            scalable_dimension=scalable_dimension,
            service_namespace=service_namespace,
            role_arn=role_arn,
            scheduled_actions=scheduled_actions,
            suspended_state=suspended_state,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7eab92548702648ed3d9193a8bedd481f01db8b59f68de00b0454143553b1539)
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
            type_hints = typing.get_type_hints(_typecheckingstub__dccf12738190780b1bb59e6433978f722516b4294053fe3cea7472b03fd1db9b)
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
    @jsii.member(jsii_name="maxCapacity")
    def max_capacity(self) -> jsii.Number:
        '''The maximum value that you plan to scale out to.'''
        return typing.cast(jsii.Number, jsii.get(self, "maxCapacity"))

    @max_capacity.setter
    def max_capacity(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aab88caece6d64e8566905de6661b92b1df09b9d335e0e8c0754b34f44d246e2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="minCapacity")
    def min_capacity(self) -> jsii.Number:
        '''The minimum value that you plan to scale in to.'''
        return typing.cast(jsii.Number, jsii.get(self, "minCapacity"))

    @min_capacity.setter
    def min_capacity(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b73964fa80587244137f97f906081898d6add27e7ac5c4b1110b5960dfbf7f8c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="resourceId")
    def resource_id(self) -> builtins.str:
        '''The identifier of the resource associated with the scalable target.'''
        return typing.cast(builtins.str, jsii.get(self, "resourceId"))

    @resource_id.setter
    def resource_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6222d448bf139000d6495103f3869076bae6b8c46711066c25270c8d2a240f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceId", value)

    @builtins.property
    @jsii.member(jsii_name="scalableDimension")
    def scalable_dimension(self) -> builtins.str:
        '''The scalable dimension associated with the scalable target.'''
        return typing.cast(builtins.str, jsii.get(self, "scalableDimension"))

    @scalable_dimension.setter
    def scalable_dimension(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4fae2c8cfacd2c2f1c7b6ce18c73fe5d382c388861da42afb198ead30adb892)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scalableDimension", value)

    @builtins.property
    @jsii.member(jsii_name="serviceNamespace")
    def service_namespace(self) -> builtins.str:
        '''The namespace of the AWS service that provides the resource, or a ``custom-resource`` .'''
        return typing.cast(builtins.str, jsii.get(self, "serviceNamespace"))

    @service_namespace.setter
    def service_namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5baa82fd6ad58564620316e191b3085f34068537274501c2ae16cef617b55152)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceNamespace", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''Specify the Amazon Resource Name (ARN) of an Identity and Access Management (IAM) role that allows Application Auto Scaling to modify the scalable target on your behalf.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9252d029d6d32f1b045421b6b1cde1f523488cdc4808bee1892014e6bd4dc0b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="scheduledActions")
    def scheduled_actions(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnScalableTarget.ScheduledActionProperty"]]]]:
        '''The scheduled actions for the scalable target.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnScalableTarget.ScheduledActionProperty"]]]], jsii.get(self, "scheduledActions"))

    @scheduled_actions.setter
    def scheduled_actions(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnScalableTarget.ScheduledActionProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1adb9fa5e86479f2f4514b089b4fcee3b8718c5f7874ca0fe66105630e3636f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scheduledActions", value)

    @builtins.property
    @jsii.member(jsii_name="suspendedState")
    def suspended_state(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnScalableTarget.SuspendedStateProperty"]]:
        '''An embedded object that contains attributes and attribute values that are used to suspend and resume automatic scaling.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnScalableTarget.SuspendedStateProperty"]], jsii.get(self, "suspendedState"))

    @suspended_state.setter
    def suspended_state(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnScalableTarget.SuspendedStateProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0bbb1dcd1d81de0e4c36de9ea045348b3724df3d549254eef9a20300325fc117)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "suspendedState", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_applicationautoscaling.CfnScalableTarget.ScalableTargetActionProperty",
        jsii_struct_bases=[],
        name_mapping={"max_capacity": "maxCapacity", "min_capacity": "minCapacity"},
    )
    class ScalableTargetActionProperty:
        def __init__(
            self,
            *,
            max_capacity: typing.Optional[jsii.Number] = None,
            min_capacity: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''``ScalableTargetAction`` specifies the minimum and maximum capacity for the ``ScalableTargetAction`` property of the `AWS::ApplicationAutoScaling::ScalableTarget ScheduledAction <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-scheduledaction.html>`_ property type.

            :param max_capacity: The maximum capacity.
            :param min_capacity: The minimum capacity.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-scalabletargetaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_applicationautoscaling as appscaling
                
                scalable_target_action_property = appscaling.CfnScalableTarget.ScalableTargetActionProperty(
                    max_capacity=123,
                    min_capacity=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__235dfc5c99fa3d515e24a56ba2af8e45cb7d6acefe812056f71abe1f48bd20ad)
                check_type(argname="argument max_capacity", value=max_capacity, expected_type=type_hints["max_capacity"])
                check_type(argname="argument min_capacity", value=min_capacity, expected_type=type_hints["min_capacity"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if max_capacity is not None:
                self._values["max_capacity"] = max_capacity
            if min_capacity is not None:
                self._values["min_capacity"] = min_capacity

        @builtins.property
        def max_capacity(self) -> typing.Optional[jsii.Number]:
            '''The maximum capacity.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-scalabletargetaction.html#cfn-applicationautoscaling-scalabletarget-scalabletargetaction-maxcapacity
            '''
            result = self._values.get("max_capacity")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def min_capacity(self) -> typing.Optional[jsii.Number]:
            '''The minimum capacity.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-scalabletargetaction.html#cfn-applicationautoscaling-scalabletarget-scalabletargetaction-mincapacity
            '''
            result = self._values.get("min_capacity")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScalableTargetActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_applicationautoscaling.CfnScalableTarget.ScheduledActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "schedule": "schedule",
            "scheduled_action_name": "scheduledActionName",
            "end_time": "endTime",
            "scalable_target_action": "scalableTargetAction",
            "start_time": "startTime",
            "timezone": "timezone",
        },
    )
    class ScheduledActionProperty:
        def __init__(
            self,
            *,
            schedule: builtins.str,
            scheduled_action_name: builtins.str,
            end_time: typing.Optional[typing.Union[_IResolvable_da3f097b, datetime.datetime]] = None,
            scalable_target_action: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnScalableTarget.ScalableTargetActionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            start_time: typing.Optional[typing.Union[_IResolvable_da3f097b, datetime.datetime]] = None,
            timezone: typing.Optional[builtins.str] = None,
        ) -> None:
            '''``ScheduledAction`` is a property of the `AWS::ApplicationAutoScaling::ScalableTarget <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html>`_ resource that specifies a scheduled action for a scalable target.

            For more information, see `Scheduled scaling <https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-scheduled-scaling.html>`_ in the *Application Auto Scaling User Guide* .

            :param schedule: The schedule for this action. The following formats are supported:. - At expressions - " ``at( *yyyy* - *mm* - *dd* T *hh* : *mm* : *ss* )`` " - Rate expressions - " ``rate( *value* *unit* )`` " - Cron expressions - " ``cron( *fields* )`` " At expressions are useful for one-time schedules. Cron expressions are useful for scheduled actions that run periodically at a specified date and time, and rate expressions are useful for scheduled actions that run at a regular interval. At and cron expressions use Universal Coordinated Time (UTC) by default. The cron format consists of six fields separated by white spaces: [Minutes] [Hours] [Day_of_Month] [Month] [Day_of_Week] [Year]. For rate expressions, *value* is a positive integer and *unit* is ``minute`` | ``minutes`` | ``hour`` | ``hours`` | ``day`` | ``days`` .
            :param scheduled_action_name: The name of the scheduled action. This name must be unique among all other scheduled actions on the specified scalable target.
            :param end_time: The date and time that the action is scheduled to end, in UTC.
            :param scalable_target_action: The new minimum and maximum capacity. You can set both values or just one. At the scheduled time, if the current capacity is below the minimum capacity, Application Auto Scaling scales out to the minimum capacity. If the current capacity is above the maximum capacity, Application Auto Scaling scales in to the maximum capacity.
            :param start_time: The date and time that the action is scheduled to begin, in UTC.
            :param timezone: The time zone used when referring to the date and time of a scheduled action, when the scheduled action uses an at or cron expression.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-scheduledaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_applicationautoscaling as appscaling
                
                scheduled_action_property = appscaling.CfnScalableTarget.ScheduledActionProperty(
                    schedule="schedule",
                    scheduled_action_name="scheduledActionName",
                
                    # the properties below are optional
                    end_time=Date(),
                    scalable_target_action=appscaling.CfnScalableTarget.ScalableTargetActionProperty(
                        max_capacity=123,
                        min_capacity=123
                    ),
                    start_time=Date(),
                    timezone="timezone"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__602ff955f286e3df520d04ef3c033f033ea91710efbf10e64903936bd464753d)
                check_type(argname="argument schedule", value=schedule, expected_type=type_hints["schedule"])
                check_type(argname="argument scheduled_action_name", value=scheduled_action_name, expected_type=type_hints["scheduled_action_name"])
                check_type(argname="argument end_time", value=end_time, expected_type=type_hints["end_time"])
                check_type(argname="argument scalable_target_action", value=scalable_target_action, expected_type=type_hints["scalable_target_action"])
                check_type(argname="argument start_time", value=start_time, expected_type=type_hints["start_time"])
                check_type(argname="argument timezone", value=timezone, expected_type=type_hints["timezone"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "schedule": schedule,
                "scheduled_action_name": scheduled_action_name,
            }
            if end_time is not None:
                self._values["end_time"] = end_time
            if scalable_target_action is not None:
                self._values["scalable_target_action"] = scalable_target_action
            if start_time is not None:
                self._values["start_time"] = start_time
            if timezone is not None:
                self._values["timezone"] = timezone

        @builtins.property
        def schedule(self) -> builtins.str:
            '''The schedule for this action. The following formats are supported:.

            - At expressions - " ``at( *yyyy* - *mm* - *dd* T *hh* : *mm* : *ss* )`` "
            - Rate expressions - " ``rate( *value* *unit* )`` "
            - Cron expressions - " ``cron( *fields* )`` "

            At expressions are useful for one-time schedules. Cron expressions are useful for scheduled actions that run periodically at a specified date and time, and rate expressions are useful for scheduled actions that run at a regular interval.

            At and cron expressions use Universal Coordinated Time (UTC) by default.

            The cron format consists of six fields separated by white spaces: [Minutes] [Hours] [Day_of_Month] [Month] [Day_of_Week] [Year].

            For rate expressions, *value* is a positive integer and *unit* is ``minute`` | ``minutes`` | ``hour`` | ``hours`` | ``day`` | ``days`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-scheduledaction.html#cfn-applicationautoscaling-scalabletarget-scheduledaction-schedule
            '''
            result = self._values.get("schedule")
            assert result is not None, "Required property 'schedule' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def scheduled_action_name(self) -> builtins.str:
            '''The name of the scheduled action.

            This name must be unique among all other scheduled actions on the specified scalable target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-scheduledaction.html#cfn-applicationautoscaling-scalabletarget-scheduledaction-scheduledactionname
            '''
            result = self._values.get("scheduled_action_name")
            assert result is not None, "Required property 'scheduled_action_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def end_time(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, datetime.datetime]]:
            '''The date and time that the action is scheduled to end, in UTC.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-scheduledaction.html#cfn-applicationautoscaling-scalabletarget-scheduledaction-endtime
            '''
            result = self._values.get("end_time")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, datetime.datetime]], result)

        @builtins.property
        def scalable_target_action(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnScalableTarget.ScalableTargetActionProperty"]]:
            '''The new minimum and maximum capacity.

            You can set both values or just one. At the scheduled time, if the current capacity is below the minimum capacity, Application Auto Scaling scales out to the minimum capacity. If the current capacity is above the maximum capacity, Application Auto Scaling scales in to the maximum capacity.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-scheduledaction.html#cfn-applicationautoscaling-scalabletarget-scheduledaction-scalabletargetaction
            '''
            result = self._values.get("scalable_target_action")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnScalableTarget.ScalableTargetActionProperty"]], result)

        @builtins.property
        def start_time(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, datetime.datetime]]:
            '''The date and time that the action is scheduled to begin, in UTC.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-scheduledaction.html#cfn-applicationautoscaling-scalabletarget-scheduledaction-starttime
            '''
            result = self._values.get("start_time")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, datetime.datetime]], result)

        @builtins.property
        def timezone(self) -> typing.Optional[builtins.str]:
            '''The time zone used when referring to the date and time of a scheduled action, when the scheduled action uses an at or cron expression.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-scheduledaction.html#cfn-applicationautoscaling-scalabletarget-scheduledaction-timezone
            '''
            result = self._values.get("timezone")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScheduledActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_applicationautoscaling.CfnScalableTarget.SuspendedStateProperty",
        jsii_struct_bases=[],
        name_mapping={
            "dynamic_scaling_in_suspended": "dynamicScalingInSuspended",
            "dynamic_scaling_out_suspended": "dynamicScalingOutSuspended",
            "scheduled_scaling_suspended": "scheduledScalingSuspended",
        },
    )
    class SuspendedStateProperty:
        def __init__(
            self,
            *,
            dynamic_scaling_in_suspended: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            dynamic_scaling_out_suspended: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            scheduled_scaling_suspended: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''``SuspendedState`` is a property of the `AWS::ApplicationAutoScaling::ScalableTarget <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html>`_ resource that specifies whether the scaling activities for a scalable target are in a suspended state.

            For more information, see `Suspending and resuming scaling <https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-suspend-resume-scaling.html>`_ in the *Application Auto Scaling User Guide* .

            :param dynamic_scaling_in_suspended: Whether scale in by a target tracking scaling policy or a step scaling policy is suspended. Set the value to ``true`` if you don't want Application Auto Scaling to remove capacity when a scaling policy is triggered. The default is ``false`` .
            :param dynamic_scaling_out_suspended: Whether scale out by a target tracking scaling policy or a step scaling policy is suspended. Set the value to ``true`` if you don't want Application Auto Scaling to add capacity when a scaling policy is triggered. The default is ``false`` .
            :param scheduled_scaling_suspended: Whether scheduled scaling is suspended. Set the value to ``true`` if you don't want Application Auto Scaling to add or remove capacity by initiating scheduled actions. The default is ``false`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-suspendedstate.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_applicationautoscaling as appscaling
                
                suspended_state_property = appscaling.CfnScalableTarget.SuspendedStateProperty(
                    dynamic_scaling_in_suspended=False,
                    dynamic_scaling_out_suspended=False,
                    scheduled_scaling_suspended=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1ec14b8e7471a97b7fc6a29eb82a7c1e0a63a4103237cfc54c79485673df1718)
                check_type(argname="argument dynamic_scaling_in_suspended", value=dynamic_scaling_in_suspended, expected_type=type_hints["dynamic_scaling_in_suspended"])
                check_type(argname="argument dynamic_scaling_out_suspended", value=dynamic_scaling_out_suspended, expected_type=type_hints["dynamic_scaling_out_suspended"])
                check_type(argname="argument scheduled_scaling_suspended", value=scheduled_scaling_suspended, expected_type=type_hints["scheduled_scaling_suspended"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if dynamic_scaling_in_suspended is not None:
                self._values["dynamic_scaling_in_suspended"] = dynamic_scaling_in_suspended
            if dynamic_scaling_out_suspended is not None:
                self._values["dynamic_scaling_out_suspended"] = dynamic_scaling_out_suspended
            if scheduled_scaling_suspended is not None:
                self._values["scheduled_scaling_suspended"] = scheduled_scaling_suspended

        @builtins.property
        def dynamic_scaling_in_suspended(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Whether scale in by a target tracking scaling policy or a step scaling policy is suspended.

            Set the value to ``true`` if you don't want Application Auto Scaling to remove capacity when a scaling policy is triggered. The default is ``false`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-suspendedstate.html#cfn-applicationautoscaling-scalabletarget-suspendedstate-dynamicscalinginsuspended
            '''
            result = self._values.get("dynamic_scaling_in_suspended")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def dynamic_scaling_out_suspended(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Whether scale out by a target tracking scaling policy or a step scaling policy is suspended.

            Set the value to ``true`` if you don't want Application Auto Scaling to add capacity when a scaling policy is triggered. The default is ``false`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-suspendedstate.html#cfn-applicationautoscaling-scalabletarget-suspendedstate-dynamicscalingoutsuspended
            '''
            result = self._values.get("dynamic_scaling_out_suspended")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def scheduled_scaling_suspended(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Whether scheduled scaling is suspended.

            Set the value to ``true`` if you don't want Application Auto Scaling to add or remove capacity by initiating scheduled actions. The default is ``false`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-suspendedstate.html#cfn-applicationautoscaling-scalabletarget-suspendedstate-scheduledscalingsuspended
            '''
            result = self._values.get("scheduled_scaling_suspended")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SuspendedStateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_applicationautoscaling.CfnScalableTargetProps",
    jsii_struct_bases=[],
    name_mapping={
        "max_capacity": "maxCapacity",
        "min_capacity": "minCapacity",
        "resource_id": "resourceId",
        "scalable_dimension": "scalableDimension",
        "service_namespace": "serviceNamespace",
        "role_arn": "roleArn",
        "scheduled_actions": "scheduledActions",
        "suspended_state": "suspendedState",
    },
)
class CfnScalableTargetProps:
    def __init__(
        self,
        *,
        max_capacity: jsii.Number,
        min_capacity: jsii.Number,
        resource_id: builtins.str,
        scalable_dimension: builtins.str,
        service_namespace: builtins.str,
        role_arn: typing.Optional[builtins.str] = None,
        scheduled_actions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnScalableTarget.ScheduledActionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        suspended_state: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnScalableTarget.SuspendedStateProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnScalableTarget``.

        :param max_capacity: The maximum value that you plan to scale out to. When a scaling policy is in effect, Application Auto Scaling can scale out (expand) as needed to the maximum capacity limit in response to changing demand.
        :param min_capacity: The minimum value that you plan to scale in to. When a scaling policy is in effect, Application Auto Scaling can scale in (contract) as needed to the minimum capacity limit in response to changing demand.
        :param resource_id: The identifier of the resource associated with the scalable target. This string consists of the resource type and unique identifier. - ECS service - The resource type is ``service`` and the unique identifier is the cluster name and service name. Example: ``service/my-cluster/my-service`` . - Spot Fleet - The resource type is ``spot-fleet-request`` and the unique identifier is the Spot Fleet request ID. Example: ``spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`` . - EMR cluster - The resource type is ``instancegroup`` and the unique identifier is the cluster ID and instance group ID. Example: ``instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0`` . - AppStream 2.0 fleet - The resource type is ``fleet`` and the unique identifier is the fleet name. Example: ``fleet/sample-fleet`` . - DynamoDB table - The resource type is ``table`` and the unique identifier is the table name. Example: ``table/my-table`` . - DynamoDB global secondary index - The resource type is ``index`` and the unique identifier is the index name. Example: ``table/my-table/index/my-table-index`` . - Aurora DB cluster - The resource type is ``cluster`` and the unique identifier is the cluster name. Example: ``cluster:my-db-cluster`` . - SageMaker endpoint variant - The resource type is ``variant`` and the unique identifier is the resource ID. Example: ``endpoint/my-end-point/variant/KMeansClustering`` . - Custom resources are not supported with a resource type. This parameter must specify the ``OutputValue`` from the CloudFormation template stack used to access the resources. The unique identifier is defined by the service provider. More information is available in our `GitHub repository <https://docs.aws.amazon.com/https://github.com/aws/aws-auto-scaling-custom-resource>`_ . - Amazon Comprehend document classification endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: ``arn:aws:comprehend:us-west-2:123456789012:document-classifier-endpoint/EXAMPLE`` . - Amazon Comprehend entity recognizer endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: ``arn:aws:comprehend:us-west-2:123456789012:entity-recognizer-endpoint/EXAMPLE`` . - Lambda provisioned concurrency - The resource type is ``function`` and the unique identifier is the function name with a function version or alias name suffix that is not ``$LATEST`` . Example: ``function:my-function:prod`` or ``function:my-function:1`` . - Amazon Keyspaces table - The resource type is ``table`` and the unique identifier is the table name. Example: ``keyspace/mykeyspace/table/mytable`` . - Amazon MSK cluster - The resource type and unique identifier are specified using the cluster ARN. Example: ``arn:aws:kafka:us-east-1:123456789012:cluster/demo-cluster-1/6357e0b2-0e6a-4b86-a0b4-70df934c2e31-5`` . - Amazon ElastiCache replication group - The resource type is ``replication-group`` and the unique identifier is the replication group name. Example: ``replication-group/mycluster`` . - Neptune cluster - The resource type is ``cluster`` and the unique identifier is the cluster name. Example: ``cluster:mycluster`` . - SageMaker serverless endpoint - The resource type is ``variant`` and the unique identifier is the resource ID. Example: ``endpoint/my-end-point/variant/KMeansClustering`` . - SageMaker inference component - The resource type is ``inference-component`` and the unique identifier is the resource ID. Example: ``inference-component/my-inference-component`` .
        :param scalable_dimension: The scalable dimension associated with the scalable target. This string consists of the service namespace, resource type, and scaling property. - ``ecs:service:DesiredCount`` - The desired task count of an ECS service. - ``elasticmapreduce:instancegroup:InstanceCount`` - The instance count of an EMR Instance Group. - ``ec2:spot-fleet-request:TargetCapacity`` - The target capacity of a Spot Fleet. - ``appstream:fleet:DesiredCapacity`` - The desired capacity of an AppStream 2.0 fleet. - ``dynamodb:table:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB table. - ``dynamodb:table:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB table. - ``dynamodb:index:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB global secondary index. - ``dynamodb:index:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB global secondary index. - ``rds:cluster:ReadReplicaCount`` - The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition and Aurora PostgreSQL-compatible edition. - ``sagemaker:variant:DesiredInstanceCount`` - The number of EC2 instances for a SageMaker model endpoint variant. - ``custom-resource:ResourceType:Property`` - The scalable dimension for a custom resource provided by your own application or service. - ``comprehend:document-classifier-endpoint:DesiredInferenceUnits`` - The number of inference units for an Amazon Comprehend document classification endpoint. - ``comprehend:entity-recognizer-endpoint:DesiredInferenceUnits`` - The number of inference units for an Amazon Comprehend entity recognizer endpoint. - ``lambda:function:ProvisionedConcurrency`` - The provisioned concurrency for a Lambda function. - ``cassandra:table:ReadCapacityUnits`` - The provisioned read capacity for an Amazon Keyspaces table. - ``cassandra:table:WriteCapacityUnits`` - The provisioned write capacity for an Amazon Keyspaces table. - ``kafka:broker-storage:VolumeSize`` - The provisioned volume size (in GiB) for brokers in an Amazon MSK cluster. - ``elasticache:replication-group:NodeGroups`` - The number of node groups for an Amazon ElastiCache replication group. - ``elasticache:replication-group:Replicas`` - The number of replicas per node group for an Amazon ElastiCache replication group. - ``neptune:cluster:ReadReplicaCount`` - The count of read replicas in an Amazon Neptune DB cluster. - ``sagemaker:variant:DesiredProvisionedConcurrency`` - The provisioned concurrency for a SageMaker serverless endpoint. - ``sagemaker:inference-component:DesiredCopyCount`` - The number of copies across an endpoint for a SageMaker inference component.
        :param service_namespace: The namespace of the AWS service that provides the resource, or a ``custom-resource`` .
        :param role_arn: Specify the Amazon Resource Name (ARN) of an Identity and Access Management (IAM) role that allows Application Auto Scaling to modify the scalable target on your behalf. This can be either an IAM service role that Application Auto Scaling can assume to make calls to other AWS resources on your behalf, or a service-linked role for the specified service. For more information, see `How Application Auto Scaling works with IAM <https://docs.aws.amazon.com/autoscaling/application/userguide/security_iam_service-with-iam.html>`_ in the *Application Auto Scaling User Guide* . To automatically create a service-linked role (recommended), specify the full ARN of the service-linked role in your stack template. To find the exact ARN of the service-linked role for your AWS or custom resource, see the `Service-linked roles <https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-service-linked-roles.html>`_ topic in the *Application Auto Scaling User Guide* . Look for the ARN in the table at the bottom of the page.
        :param scheduled_actions: The scheduled actions for the scalable target. Duplicates aren't allowed.
        :param suspended_state: An embedded object that contains attributes and attribute values that are used to suspend and resume automatic scaling. Setting the value of an attribute to ``true`` suspends the specified scaling activities. Setting it to ``false`` (default) resumes the specified scaling activities. *Suspension Outcomes* - For ``DynamicScalingInSuspended`` , while a suspension is in effect, all scale-in activities that are triggered by a scaling policy are suspended. - For ``DynamicScalingOutSuspended`` , while a suspension is in effect, all scale-out activities that are triggered by a scaling policy are suspended. - For ``ScheduledScalingSuspended`` , while a suspension is in effect, all scaling activities that involve scheduled actions are suspended.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_applicationautoscaling as appscaling
            
            cfn_scalable_target_props = appscaling.CfnScalableTargetProps(
                max_capacity=123,
                min_capacity=123,
                resource_id="resourceId",
                scalable_dimension="scalableDimension",
                service_namespace="serviceNamespace",
            
                # the properties below are optional
                role_arn="roleArn",
                scheduled_actions=[appscaling.CfnScalableTarget.ScheduledActionProperty(
                    schedule="schedule",
                    scheduled_action_name="scheduledActionName",
            
                    # the properties below are optional
                    end_time=Date(),
                    scalable_target_action=appscaling.CfnScalableTarget.ScalableTargetActionProperty(
                        max_capacity=123,
                        min_capacity=123
                    ),
                    start_time=Date(),
                    timezone="timezone"
                )],
                suspended_state=appscaling.CfnScalableTarget.SuspendedStateProperty(
                    dynamic_scaling_in_suspended=False,
                    dynamic_scaling_out_suspended=False,
                    scheduled_scaling_suspended=False
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0aca5d6a38a10d55ae89247bf02288adc86be9fd694d2a88c8aaf7d40e74818c)
            check_type(argname="argument max_capacity", value=max_capacity, expected_type=type_hints["max_capacity"])
            check_type(argname="argument min_capacity", value=min_capacity, expected_type=type_hints["min_capacity"])
            check_type(argname="argument resource_id", value=resource_id, expected_type=type_hints["resource_id"])
            check_type(argname="argument scalable_dimension", value=scalable_dimension, expected_type=type_hints["scalable_dimension"])
            check_type(argname="argument service_namespace", value=service_namespace, expected_type=type_hints["service_namespace"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument scheduled_actions", value=scheduled_actions, expected_type=type_hints["scheduled_actions"])
            check_type(argname="argument suspended_state", value=suspended_state, expected_type=type_hints["suspended_state"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "max_capacity": max_capacity,
            "min_capacity": min_capacity,
            "resource_id": resource_id,
            "scalable_dimension": scalable_dimension,
            "service_namespace": service_namespace,
        }
        if role_arn is not None:
            self._values["role_arn"] = role_arn
        if scheduled_actions is not None:
            self._values["scheduled_actions"] = scheduled_actions
        if suspended_state is not None:
            self._values["suspended_state"] = suspended_state

    @builtins.property
    def max_capacity(self) -> jsii.Number:
        '''The maximum value that you plan to scale out to.

        When a scaling policy is in effect, Application Auto Scaling can scale out (expand) as needed to the maximum capacity limit in response to changing demand.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html#cfn-applicationautoscaling-scalabletarget-maxcapacity
        '''
        result = self._values.get("max_capacity")
        assert result is not None, "Required property 'max_capacity' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def min_capacity(self) -> jsii.Number:
        '''The minimum value that you plan to scale in to.

        When a scaling policy is in effect, Application Auto Scaling can scale in (contract) as needed to the minimum capacity limit in response to changing demand.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html#cfn-applicationautoscaling-scalabletarget-mincapacity
        '''
        result = self._values.get("min_capacity")
        assert result is not None, "Required property 'min_capacity' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def resource_id(self) -> builtins.str:
        '''The identifier of the resource associated with the scalable target.

        This string consists of the resource type and unique identifier.

        - ECS service - The resource type is ``service`` and the unique identifier is the cluster name and service name. Example: ``service/my-cluster/my-service`` .
        - Spot Fleet - The resource type is ``spot-fleet-request`` and the unique identifier is the Spot Fleet request ID. Example: ``spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`` .
        - EMR cluster - The resource type is ``instancegroup`` and the unique identifier is the cluster ID and instance group ID. Example: ``instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0`` .
        - AppStream 2.0 fleet - The resource type is ``fleet`` and the unique identifier is the fleet name. Example: ``fleet/sample-fleet`` .
        - DynamoDB table - The resource type is ``table`` and the unique identifier is the table name. Example: ``table/my-table`` .
        - DynamoDB global secondary index - The resource type is ``index`` and the unique identifier is the index name. Example: ``table/my-table/index/my-table-index`` .
        - Aurora DB cluster - The resource type is ``cluster`` and the unique identifier is the cluster name. Example: ``cluster:my-db-cluster`` .
        - SageMaker endpoint variant - The resource type is ``variant`` and the unique identifier is the resource ID. Example: ``endpoint/my-end-point/variant/KMeansClustering`` .
        - Custom resources are not supported with a resource type. This parameter must specify the ``OutputValue`` from the CloudFormation template stack used to access the resources. The unique identifier is defined by the service provider. More information is available in our `GitHub repository <https://docs.aws.amazon.com/https://github.com/aws/aws-auto-scaling-custom-resource>`_ .
        - Amazon Comprehend document classification endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: ``arn:aws:comprehend:us-west-2:123456789012:document-classifier-endpoint/EXAMPLE`` .
        - Amazon Comprehend entity recognizer endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: ``arn:aws:comprehend:us-west-2:123456789012:entity-recognizer-endpoint/EXAMPLE`` .
        - Lambda provisioned concurrency - The resource type is ``function`` and the unique identifier is the function name with a function version or alias name suffix that is not ``$LATEST`` . Example: ``function:my-function:prod`` or ``function:my-function:1`` .
        - Amazon Keyspaces table - The resource type is ``table`` and the unique identifier is the table name. Example: ``keyspace/mykeyspace/table/mytable`` .
        - Amazon MSK cluster - The resource type and unique identifier are specified using the cluster ARN. Example: ``arn:aws:kafka:us-east-1:123456789012:cluster/demo-cluster-1/6357e0b2-0e6a-4b86-a0b4-70df934c2e31-5`` .
        - Amazon ElastiCache replication group - The resource type is ``replication-group`` and the unique identifier is the replication group name. Example: ``replication-group/mycluster`` .
        - Neptune cluster - The resource type is ``cluster`` and the unique identifier is the cluster name. Example: ``cluster:mycluster`` .
        - SageMaker serverless endpoint - The resource type is ``variant`` and the unique identifier is the resource ID. Example: ``endpoint/my-end-point/variant/KMeansClustering`` .
        - SageMaker inference component - The resource type is ``inference-component`` and the unique identifier is the resource ID. Example: ``inference-component/my-inference-component`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html#cfn-applicationautoscaling-scalabletarget-resourceid
        '''
        result = self._values.get("resource_id")
        assert result is not None, "Required property 'resource_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def scalable_dimension(self) -> builtins.str:
        '''The scalable dimension associated with the scalable target.

        This string consists of the service namespace, resource type, and scaling property.

        - ``ecs:service:DesiredCount`` - The desired task count of an ECS service.
        - ``elasticmapreduce:instancegroup:InstanceCount`` - The instance count of an EMR Instance Group.
        - ``ec2:spot-fleet-request:TargetCapacity`` - The target capacity of a Spot Fleet.
        - ``appstream:fleet:DesiredCapacity`` - The desired capacity of an AppStream 2.0 fleet.
        - ``dynamodb:table:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB table.
        - ``dynamodb:table:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB table.
        - ``dynamodb:index:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB global secondary index.
        - ``dynamodb:index:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB global secondary index.
        - ``rds:cluster:ReadReplicaCount`` - The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition and Aurora PostgreSQL-compatible edition.
        - ``sagemaker:variant:DesiredInstanceCount`` - The number of EC2 instances for a SageMaker model endpoint variant.
        - ``custom-resource:ResourceType:Property`` - The scalable dimension for a custom resource provided by your own application or service.
        - ``comprehend:document-classifier-endpoint:DesiredInferenceUnits`` - The number of inference units for an Amazon Comprehend document classification endpoint.
        - ``comprehend:entity-recognizer-endpoint:DesiredInferenceUnits`` - The number of inference units for an Amazon Comprehend entity recognizer endpoint.
        - ``lambda:function:ProvisionedConcurrency`` - The provisioned concurrency for a Lambda function.
        - ``cassandra:table:ReadCapacityUnits`` - The provisioned read capacity for an Amazon Keyspaces table.
        - ``cassandra:table:WriteCapacityUnits`` - The provisioned write capacity for an Amazon Keyspaces table.
        - ``kafka:broker-storage:VolumeSize`` - The provisioned volume size (in GiB) for brokers in an Amazon MSK cluster.
        - ``elasticache:replication-group:NodeGroups`` - The number of node groups for an Amazon ElastiCache replication group.
        - ``elasticache:replication-group:Replicas`` - The number of replicas per node group for an Amazon ElastiCache replication group.
        - ``neptune:cluster:ReadReplicaCount`` - The count of read replicas in an Amazon Neptune DB cluster.
        - ``sagemaker:variant:DesiredProvisionedConcurrency`` - The provisioned concurrency for a SageMaker serverless endpoint.
        - ``sagemaker:inference-component:DesiredCopyCount`` - The number of copies across an endpoint for a SageMaker inference component.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html#cfn-applicationautoscaling-scalabletarget-scalabledimension
        '''
        result = self._values.get("scalable_dimension")
        assert result is not None, "Required property 'scalable_dimension' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_namespace(self) -> builtins.str:
        '''The namespace of the AWS service that provides the resource, or a ``custom-resource`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html#cfn-applicationautoscaling-scalabletarget-servicenamespace
        '''
        result = self._values.get("service_namespace")
        assert result is not None, "Required property 'service_namespace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''Specify the Amazon Resource Name (ARN) of an Identity and Access Management (IAM) role that allows Application Auto Scaling to modify the scalable target on your behalf.

        This can be either an IAM service role that Application Auto Scaling can assume to make calls to other AWS resources on your behalf, or a service-linked role for the specified service. For more information, see `How Application Auto Scaling works with IAM <https://docs.aws.amazon.com/autoscaling/application/userguide/security_iam_service-with-iam.html>`_ in the *Application Auto Scaling User Guide* .

        To automatically create a service-linked role (recommended), specify the full ARN of the service-linked role in your stack template. To find the exact ARN of the service-linked role for your AWS or custom resource, see the `Service-linked roles <https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-service-linked-roles.html>`_ topic in the *Application Auto Scaling User Guide* . Look for the ARN in the table at the bottom of the page.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html#cfn-applicationautoscaling-scalabletarget-rolearn
        '''
        result = self._values.get("role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scheduled_actions(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnScalableTarget.ScheduledActionProperty]]]]:
        '''The scheduled actions for the scalable target.

        Duplicates aren't allowed.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html#cfn-applicationautoscaling-scalabletarget-scheduledactions
        '''
        result = self._values.get("scheduled_actions")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnScalableTarget.ScheduledActionProperty]]]], result)

    @builtins.property
    def suspended_state(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnScalableTarget.SuspendedStateProperty]]:
        '''An embedded object that contains attributes and attribute values that are used to suspend and resume automatic scaling.

        Setting the value of an attribute to ``true`` suspends the specified scaling activities. Setting it to ``false`` (default) resumes the specified scaling activities.

        *Suspension Outcomes*

        - For ``DynamicScalingInSuspended`` , while a suspension is in effect, all scale-in activities that are triggered by a scaling policy are suspended.
        - For ``DynamicScalingOutSuspended`` , while a suspension is in effect, all scale-out activities that are triggered by a scaling policy are suspended.
        - For ``ScheduledScalingSuspended`` , while a suspension is in effect, all scaling activities that involve scheduled actions are suspended.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html#cfn-applicationautoscaling-scalabletarget-suspendedstate
        '''
        result = self._values.get("suspended_state")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnScalableTarget.SuspendedStateProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnScalableTargetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnScalingPolicy(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_applicationautoscaling.CfnScalingPolicy",
):
    '''The ``AWS::ApplicationAutoScaling::ScalingPolicy`` resource defines a scaling policy that Application Auto Scaling uses to adjust the capacity of a scalable target.

    For more information, see `Target tracking scaling policies <https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-target-tracking.html>`_ and `Step scaling policies <https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-step-scaling-policies.html>`_ in the *Application Auto Scaling User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html
    :cloudformationResource: AWS::ApplicationAutoScaling::ScalingPolicy
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_applicationautoscaling as appscaling
        
        cfn_scaling_policy = appscaling.CfnScalingPolicy(self, "MyCfnScalingPolicy",
            policy_name="policyName",
            policy_type="policyType",
        
            # the properties below are optional
            resource_id="resourceId",
            scalable_dimension="scalableDimension",
            scaling_target_id="scalingTargetId",
            service_namespace="serviceNamespace",
            step_scaling_policy_configuration=appscaling.CfnScalingPolicy.StepScalingPolicyConfigurationProperty(
                adjustment_type="adjustmentType",
                cooldown=123,
                metric_aggregation_type="metricAggregationType",
                min_adjustment_magnitude=123,
                step_adjustments=[appscaling.CfnScalingPolicy.StepAdjustmentProperty(
                    scaling_adjustment=123,
        
                    # the properties below are optional
                    metric_interval_lower_bound=123,
                    metric_interval_upper_bound=123
                )]
            ),
            target_tracking_scaling_policy_configuration=appscaling.CfnScalingPolicy.TargetTrackingScalingPolicyConfigurationProperty(
                target_value=123,
        
                # the properties below are optional
                customized_metric_specification=appscaling.CfnScalingPolicy.CustomizedMetricSpecificationProperty(
                    dimensions=[appscaling.CfnScalingPolicy.MetricDimensionProperty(
                        name="name",
                        value="value"
                    )],
                    metric_name="metricName",
                    metrics=[appscaling.CfnScalingPolicy.TargetTrackingMetricDataQueryProperty(
                        expression="expression",
                        id="id",
                        label="label",
                        metric_stat=appscaling.CfnScalingPolicy.TargetTrackingMetricStatProperty(
                            metric=appscaling.CfnScalingPolicy.TargetTrackingMetricProperty(
                                dimensions=[appscaling.CfnScalingPolicy.TargetTrackingMetricDimensionProperty(
                                    name="name",
                                    value="value"
                                )],
                                metric_name="metricName",
                                namespace="namespace"
                            ),
                            stat="stat",
                            unit="unit"
                        ),
                        return_data=False
                    )],
                    namespace="namespace",
                    statistic="statistic",
                    unit="unit"
                ),
                disable_scale_in=False,
                predefined_metric_specification=appscaling.CfnScalingPolicy.PredefinedMetricSpecificationProperty(
                    predefined_metric_type="predefinedMetricType",
        
                    # the properties below are optional
                    resource_label="resourceLabel"
                ),
                scale_in_cooldown=123,
                scale_out_cooldown=123
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        policy_name: builtins.str,
        policy_type: builtins.str,
        resource_id: typing.Optional[builtins.str] = None,
        scalable_dimension: typing.Optional[builtins.str] = None,
        scaling_target_id: typing.Optional[builtins.str] = None,
        service_namespace: typing.Optional[builtins.str] = None,
        step_scaling_policy_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnScalingPolicy.StepScalingPolicyConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        target_tracking_scaling_policy_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnScalingPolicy.TargetTrackingScalingPolicyConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param policy_name: The name of the scaling policy. Updates to the name of a target tracking scaling policy are not supported, unless you also update the metric used for scaling. To change only a target tracking scaling policy's name, first delete the policy by removing the existing ``AWS::ApplicationAutoScaling::ScalingPolicy`` resource from the template and updating the stack. Then, recreate the resource with the same settings and a different name.
        :param policy_type: The scaling policy type. The following policy types are supported: ``TargetTrackingScaling`` —Not supported for Amazon EMR ``StepScaling`` —Not supported for DynamoDB, Amazon Comprehend, Lambda, Amazon Keyspaces, Amazon MSK, Amazon ElastiCache, or Neptune.
        :param resource_id: The identifier of the resource associated with the scaling policy. This string consists of the resource type and unique identifier. - ECS service - The resource type is ``service`` and the unique identifier is the cluster name and service name. Example: ``service/my-cluster/my-service`` . - Spot Fleet - The resource type is ``spot-fleet-request`` and the unique identifier is the Spot Fleet request ID. Example: ``spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`` . - EMR cluster - The resource type is ``instancegroup`` and the unique identifier is the cluster ID and instance group ID. Example: ``instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0`` . - AppStream 2.0 fleet - The resource type is ``fleet`` and the unique identifier is the fleet name. Example: ``fleet/sample-fleet`` . - DynamoDB table - The resource type is ``table`` and the unique identifier is the table name. Example: ``table/my-table`` . - DynamoDB global secondary index - The resource type is ``index`` and the unique identifier is the index name. Example: ``table/my-table/index/my-table-index`` . - Aurora DB cluster - The resource type is ``cluster`` and the unique identifier is the cluster name. Example: ``cluster:my-db-cluster`` . - SageMaker endpoint variant - The resource type is ``variant`` and the unique identifier is the resource ID. Example: ``endpoint/my-end-point/variant/KMeansClustering`` . - Custom resources are not supported with a resource type. This parameter must specify the ``OutputValue`` from the CloudFormation template stack used to access the resources. The unique identifier is defined by the service provider. More information is available in our `GitHub repository <https://docs.aws.amazon.com/https://github.com/aws/aws-auto-scaling-custom-resource>`_ . - Amazon Comprehend document classification endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: ``arn:aws:comprehend:us-west-2:123456789012:document-classifier-endpoint/EXAMPLE`` . - Amazon Comprehend entity recognizer endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: ``arn:aws:comprehend:us-west-2:123456789012:entity-recognizer-endpoint/EXAMPLE`` . - Lambda provisioned concurrency - The resource type is ``function`` and the unique identifier is the function name with a function version or alias name suffix that is not ``$LATEST`` . Example: ``function:my-function:prod`` or ``function:my-function:1`` . - Amazon Keyspaces table - The resource type is ``table`` and the unique identifier is the table name. Example: ``keyspace/mykeyspace/table/mytable`` . - Amazon MSK cluster - The resource type and unique identifier are specified using the cluster ARN. Example: ``arn:aws:kafka:us-east-1:123456789012:cluster/demo-cluster-1/6357e0b2-0e6a-4b86-a0b4-70df934c2e31-5`` . - Amazon ElastiCache replication group - The resource type is ``replication-group`` and the unique identifier is the replication group name. Example: ``replication-group/mycluster`` . - Neptune cluster - The resource type is ``cluster`` and the unique identifier is the cluster name. Example: ``cluster:mycluster`` . - SageMaker serverless endpoint - The resource type is ``variant`` and the unique identifier is the resource ID. Example: ``endpoint/my-end-point/variant/KMeansClustering`` . - SageMaker inference component - The resource type is ``inference-component`` and the unique identifier is the resource ID. Example: ``inference-component/my-inference-component`` .
        :param scalable_dimension: The scalable dimension. This string consists of the service namespace, resource type, and scaling property. - ``ecs:service:DesiredCount`` - The desired task count of an ECS service. - ``elasticmapreduce:instancegroup:InstanceCount`` - The instance count of an EMR Instance Group. - ``ec2:spot-fleet-request:TargetCapacity`` - The target capacity of a Spot Fleet. - ``appstream:fleet:DesiredCapacity`` - The desired capacity of an AppStream 2.0 fleet. - ``dynamodb:table:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB table. - ``dynamodb:table:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB table. - ``dynamodb:index:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB global secondary index. - ``dynamodb:index:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB global secondary index. - ``rds:cluster:ReadReplicaCount`` - The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition and Aurora PostgreSQL-compatible edition. - ``sagemaker:variant:DesiredInstanceCount`` - The number of EC2 instances for a SageMaker model endpoint variant. - ``custom-resource:ResourceType:Property`` - The scalable dimension for a custom resource provided by your own application or service. - ``comprehend:document-classifier-endpoint:DesiredInferenceUnits`` - The number of inference units for an Amazon Comprehend document classification endpoint. - ``comprehend:entity-recognizer-endpoint:DesiredInferenceUnits`` - The number of inference units for an Amazon Comprehend entity recognizer endpoint. - ``lambda:function:ProvisionedConcurrency`` - The provisioned concurrency for a Lambda function. - ``cassandra:table:ReadCapacityUnits`` - The provisioned read capacity for an Amazon Keyspaces table. - ``cassandra:table:WriteCapacityUnits`` - The provisioned write capacity for an Amazon Keyspaces table. - ``kafka:broker-storage:VolumeSize`` - The provisioned volume size (in GiB) for brokers in an Amazon MSK cluster. - ``elasticache:replication-group:NodeGroups`` - The number of node groups for an Amazon ElastiCache replication group. - ``elasticache:replication-group:Replicas`` - The number of replicas per node group for an Amazon ElastiCache replication group. - ``neptune:cluster:ReadReplicaCount`` - The count of read replicas in an Amazon Neptune DB cluster. - ``sagemaker:variant:DesiredProvisionedConcurrency`` - The provisioned concurrency for a SageMaker serverless endpoint. - ``sagemaker:inference-component:DesiredCopyCount`` - The number of copies across an endpoint for a SageMaker inference component.
        :param scaling_target_id: The CloudFormation-generated ID of an Application Auto Scaling scalable target. For more information about the ID, see the Return Value section of the ``AWS::ApplicationAutoScaling::ScalableTarget`` resource. .. epigraph:: You must specify either the ``ScalingTargetId`` property, or the ``ResourceId`` , ``ScalableDimension`` , and ``ServiceNamespace`` properties, but not both.
        :param service_namespace: The namespace of the AWS service that provides the resource, or a ``custom-resource`` .
        :param step_scaling_policy_configuration: A step scaling policy.
        :param target_tracking_scaling_policy_configuration: A target tracking scaling policy.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1fdbd49d0d5c8d10cb6dba70c50d20e471988b2d94237a064669be24bc1708e6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnScalingPolicyProps(
            policy_name=policy_name,
            policy_type=policy_type,
            resource_id=resource_id,
            scalable_dimension=scalable_dimension,
            scaling_target_id=scaling_target_id,
            service_namespace=service_namespace,
            step_scaling_policy_configuration=step_scaling_policy_configuration,
            target_tracking_scaling_policy_configuration=target_tracking_scaling_policy_configuration,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06b6ee36474194c74b31f66e6e4141f9c4e6b18bc220e2d7e386cb92c8c7ab4b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a136d66de9ef9614e63ed7ac6742e6389bf03e5cc8897d6d0ef331e7b20ac3ff)
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
        '''Returns the ARN of a scaling policy.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="policyName")
    def policy_name(self) -> builtins.str:
        '''The name of the scaling policy.'''
        return typing.cast(builtins.str, jsii.get(self, "policyName"))

    @policy_name.setter
    def policy_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c59722890877d8ddfaeabf8aced7cbcbac1e5b7bdc4bc14db89c2047881a540a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyName", value)

    @builtins.property
    @jsii.member(jsii_name="policyType")
    def policy_type(self) -> builtins.str:
        '''The scaling policy type.'''
        return typing.cast(builtins.str, jsii.get(self, "policyType"))

    @policy_type.setter
    def policy_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64ceb2a355ff27a664253fe046aa1782da96620b29bc51aeb4cc3d41e3e86c84)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyType", value)

    @builtins.property
    @jsii.member(jsii_name="resourceId")
    def resource_id(self) -> typing.Optional[builtins.str]:
        '''The identifier of the resource associated with the scaling policy.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceId"))

    @resource_id.setter
    def resource_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__471855b6df8fda8e34a03d46cd115dff8f7756d99f246dde133740f2be29f4c4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceId", value)

    @builtins.property
    @jsii.member(jsii_name="scalableDimension")
    def scalable_dimension(self) -> typing.Optional[builtins.str]:
        '''The scalable dimension.

        This string consists of the service namespace, resource type, and scaling property.
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scalableDimension"))

    @scalable_dimension.setter
    def scalable_dimension(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7c7fbf57e3d736c1fe088d47facb97643b88aa8c36fb8faed19ffa53682927f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scalableDimension", value)

    @builtins.property
    @jsii.member(jsii_name="scalingTargetId")
    def scaling_target_id(self) -> typing.Optional[builtins.str]:
        '''The CloudFormation-generated ID of an Application Auto Scaling scalable target.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scalingTargetId"))

    @scaling_target_id.setter
    def scaling_target_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f4fbea87ebb062bdc91ff07aec76f048538e421370633ef1c72dbf10223bf67)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scalingTargetId", value)

    @builtins.property
    @jsii.member(jsii_name="serviceNamespace")
    def service_namespace(self) -> typing.Optional[builtins.str]:
        '''The namespace of the AWS service that provides the resource, or a ``custom-resource`` .'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceNamespace"))

    @service_namespace.setter
    def service_namespace(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56b9fc2d37586eb8d15fe8d758af97dd8d88e8a7505bd07bc33f6daba1dfff42)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceNamespace", value)

    @builtins.property
    @jsii.member(jsii_name="stepScalingPolicyConfiguration")
    def step_scaling_policy_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnScalingPolicy.StepScalingPolicyConfigurationProperty"]]:
        '''A step scaling policy.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnScalingPolicy.StepScalingPolicyConfigurationProperty"]], jsii.get(self, "stepScalingPolicyConfiguration"))

    @step_scaling_policy_configuration.setter
    def step_scaling_policy_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnScalingPolicy.StepScalingPolicyConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ccee10df2369c02f2415d65418aa22f9f91b2dd5fab0700a4a452b640ae5db54)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stepScalingPolicyConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="targetTrackingScalingPolicyConfiguration")
    def target_tracking_scaling_policy_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnScalingPolicy.TargetTrackingScalingPolicyConfigurationProperty"]]:
        '''A target tracking scaling policy.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnScalingPolicy.TargetTrackingScalingPolicyConfigurationProperty"]], jsii.get(self, "targetTrackingScalingPolicyConfiguration"))

    @target_tracking_scaling_policy_configuration.setter
    def target_tracking_scaling_policy_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnScalingPolicy.TargetTrackingScalingPolicyConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d48220f9b4b78b76a3e0525fb18dc4772f5f73ecb26256ee41a09fa710c8be3a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetTrackingScalingPolicyConfiguration", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_applicationautoscaling.CfnScalingPolicy.CustomizedMetricSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "dimensions": "dimensions",
            "metric_name": "metricName",
            "metrics": "metrics",
            "namespace": "namespace",
            "statistic": "statistic",
            "unit": "unit",
        },
    )
    class CustomizedMetricSpecificationProperty:
        def __init__(
            self,
            *,
            dimensions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnScalingPolicy.MetricDimensionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            metric_name: typing.Optional[builtins.str] = None,
            metrics: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnScalingPolicy.TargetTrackingMetricDataQueryProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            namespace: typing.Optional[builtins.str] = None,
            statistic: typing.Optional[builtins.str] = None,
            unit: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Contains customized metric specification information for a target tracking scaling policy for Application Auto Scaling.

            For information about the available metrics for a service, see `AWS services that publish CloudWatch metrics <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/aws-services-cloudwatch-metrics.html>`_ in the *Amazon CloudWatch User Guide* .

            To create your customized metric specification:

            - Add values for each required parameter from CloudWatch. You can use an existing metric, or a new metric that you create. To use your own metric, you must first publish the metric to CloudWatch. For more information, see `Publish custom metrics <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html>`_ in the *Amazon CloudWatch User Guide* .
            - Choose a metric that changes proportionally with capacity. The value of the metric should increase or decrease in inverse proportion to the number of capacity units. That is, the value of the metric should decrease when capacity increases, and increase when capacity decreases.

            For an example of how creating new metrics can be useful, see `Scaling based on Amazon SQS <https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-using-sqs-queue.html>`_ in the *Amazon EC2 Auto Scaling User Guide* . This topic mentions Auto Scaling groups, but the same scenario for Amazon SQS can apply to the target tracking scaling policies that you create for a Spot Fleet by using Application Auto Scaling.

            For more information about the CloudWatch terminology below, see `Amazon CloudWatch concepts <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html>`_ .

            ``CustomizedMetricSpecification`` is a property of the `AWS::ApplicationAutoScaling::ScalingPolicy TargetTrackingScalingPolicyConfiguration <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration.html>`_ property type.

            :param dimensions: The dimensions of the metric. Conditional: If you published your metric with dimensions, you must specify the same dimensions in your scaling policy.
            :param metric_name: The name of the metric. To get the exact metric name, namespace, and dimensions, inspect the `Metric <https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_Metric.html>`_ object that's returned by a call to `ListMetrics <https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ListMetrics.html>`_ .
            :param metrics: The metrics to include in the target tracking scaling policy, as a metric data query. This can include both raw metric and metric math expressions.
            :param namespace: The namespace of the metric.
            :param statistic: The statistic of the metric.
            :param unit: The unit of the metric. For a complete list of the units that CloudWatch supports, see the `MetricDatum <https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_MetricDatum.html>`_ data type in the *Amazon CloudWatch API Reference* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-customizedmetricspecification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_applicationautoscaling as appscaling
                
                customized_metric_specification_property = appscaling.CfnScalingPolicy.CustomizedMetricSpecificationProperty(
                    dimensions=[appscaling.CfnScalingPolicy.MetricDimensionProperty(
                        name="name",
                        value="value"
                    )],
                    metric_name="metricName",
                    metrics=[appscaling.CfnScalingPolicy.TargetTrackingMetricDataQueryProperty(
                        expression="expression",
                        id="id",
                        label="label",
                        metric_stat=appscaling.CfnScalingPolicy.TargetTrackingMetricStatProperty(
                            metric=appscaling.CfnScalingPolicy.TargetTrackingMetricProperty(
                                dimensions=[appscaling.CfnScalingPolicy.TargetTrackingMetricDimensionProperty(
                                    name="name",
                                    value="value"
                                )],
                                metric_name="metricName",
                                namespace="namespace"
                            ),
                            stat="stat",
                            unit="unit"
                        ),
                        return_data=False
                    )],
                    namespace="namespace",
                    statistic="statistic",
                    unit="unit"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5f60b1265cbe9bf1a766a1e08801c1216e450695c574c54d2a3c2906a3e7a111)
                check_type(argname="argument dimensions", value=dimensions, expected_type=type_hints["dimensions"])
                check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
                check_type(argname="argument metrics", value=metrics, expected_type=type_hints["metrics"])
                check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
                check_type(argname="argument statistic", value=statistic, expected_type=type_hints["statistic"])
                check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if dimensions is not None:
                self._values["dimensions"] = dimensions
            if metric_name is not None:
                self._values["metric_name"] = metric_name
            if metrics is not None:
                self._values["metrics"] = metrics
            if namespace is not None:
                self._values["namespace"] = namespace
            if statistic is not None:
                self._values["statistic"] = statistic
            if unit is not None:
                self._values["unit"] = unit

        @builtins.property
        def dimensions(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnScalingPolicy.MetricDimensionProperty"]]]]:
            '''The dimensions of the metric.

            Conditional: If you published your metric with dimensions, you must specify the same dimensions in your scaling policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-customizedmetricspecification.html#cfn-applicationautoscaling-scalingpolicy-customizedmetricspecification-dimensions
            '''
            result = self._values.get("dimensions")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnScalingPolicy.MetricDimensionProperty"]]]], result)

        @builtins.property
        def metric_name(self) -> typing.Optional[builtins.str]:
            '''The name of the metric.

            To get the exact metric name, namespace, and dimensions, inspect the `Metric <https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_Metric.html>`_ object that's returned by a call to `ListMetrics <https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ListMetrics.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-customizedmetricspecification.html#cfn-applicationautoscaling-scalingpolicy-customizedmetricspecification-metricname
            '''
            result = self._values.get("metric_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def metrics(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnScalingPolicy.TargetTrackingMetricDataQueryProperty"]]]]:
            '''The metrics to include in the target tracking scaling policy, as a metric data query.

            This can include both raw metric and metric math expressions.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-customizedmetricspecification.html#cfn-applicationautoscaling-scalingpolicy-customizedmetricspecification-metrics
            '''
            result = self._values.get("metrics")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnScalingPolicy.TargetTrackingMetricDataQueryProperty"]]]], result)

        @builtins.property
        def namespace(self) -> typing.Optional[builtins.str]:
            '''The namespace of the metric.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-customizedmetricspecification.html#cfn-applicationautoscaling-scalingpolicy-customizedmetricspecification-namespace
            '''
            result = self._values.get("namespace")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def statistic(self) -> typing.Optional[builtins.str]:
            '''The statistic of the metric.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-customizedmetricspecification.html#cfn-applicationautoscaling-scalingpolicy-customizedmetricspecification-statistic
            '''
            result = self._values.get("statistic")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def unit(self) -> typing.Optional[builtins.str]:
            '''The unit of the metric.

            For a complete list of the units that CloudWatch supports, see the `MetricDatum <https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_MetricDatum.html>`_ data type in the *Amazon CloudWatch API Reference* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-customizedmetricspecification.html#cfn-applicationautoscaling-scalingpolicy-customizedmetricspecification-unit
            '''
            result = self._values.get("unit")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomizedMetricSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_applicationautoscaling.CfnScalingPolicy.MetricDimensionProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "value": "value"},
    )
    class MetricDimensionProperty:
        def __init__(self, *, name: builtins.str, value: builtins.str) -> None:
            '''``MetricDimension`` specifies a name/value pair that is part of the identity of a CloudWatch metric for the ``Dimensions`` property of the `AWS::ApplicationAutoScaling::ScalingPolicy CustomizedMetricSpecification <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-customizedmetricspecification.html>`_ property type. Duplicate dimensions are not allowed.

            :param name: The name of the dimension.
            :param value: The value of the dimension.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-metricdimension.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_applicationautoscaling as appscaling
                
                metric_dimension_property = appscaling.CfnScalingPolicy.MetricDimensionProperty(
                    name="name",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2bbab6c71eac87b44a87976e9ec88ca8fb9d041a349eeb47474fae5790b2b304)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
                "value": value,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the dimension.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-metricdimension.html#cfn-applicationautoscaling-scalingpolicy-metricdimension-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''The value of the dimension.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-metricdimension.html#cfn-applicationautoscaling-scalingpolicy-metricdimension-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MetricDimensionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_applicationautoscaling.CfnScalingPolicy.PredefinedMetricSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "predefined_metric_type": "predefinedMetricType",
            "resource_label": "resourceLabel",
        },
    )
    class PredefinedMetricSpecificationProperty:
        def __init__(
            self,
            *,
            predefined_metric_type: builtins.str,
            resource_label: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Contains predefined metric specification information for a target tracking scaling policy for Application Auto Scaling.

            ``PredefinedMetricSpecification`` is a property of the `AWS::ApplicationAutoScaling::ScalingPolicy TargetTrackingScalingPolicyConfiguration <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration.html>`_ property type.

            :param predefined_metric_type: The metric type. The ``ALBRequestCountPerTarget`` metric type applies only to Spot fleet requests and ECS services.
            :param resource_label: Identifies the resource associated with the metric type. You can't specify a resource label unless the metric type is ``ALBRequestCountPerTarget`` and there is a target group attached to the Spot Fleet or ECS service. You create the resource label by appending the final portion of the load balancer ARN and the final portion of the target group ARN into a single value, separated by a forward slash (/). The format of the resource label is: ``app/my-alb/778d41231b141a0f/targetgroup/my-alb-target-group/943f017f100becff`` . Where: - app// is the final portion of the load balancer ARN - targetgroup// is the final portion of the target group ARN. To find the ARN for an Application Load Balancer, use the `DescribeLoadBalancers <https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeLoadBalancers.html>`_ API operation. To find the ARN for the target group, use the `DescribeTargetGroups <https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeTargetGroups.html>`_ API operation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-predefinedmetricspecification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_applicationautoscaling as appscaling
                
                predefined_metric_specification_property = appscaling.CfnScalingPolicy.PredefinedMetricSpecificationProperty(
                    predefined_metric_type="predefinedMetricType",
                
                    # the properties below are optional
                    resource_label="resourceLabel"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__006a90e58fd47516fb147d13d14740fcdcd4c98e1ffcee20b2746e63c245c11a)
                check_type(argname="argument predefined_metric_type", value=predefined_metric_type, expected_type=type_hints["predefined_metric_type"])
                check_type(argname="argument resource_label", value=resource_label, expected_type=type_hints["resource_label"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "predefined_metric_type": predefined_metric_type,
            }
            if resource_label is not None:
                self._values["resource_label"] = resource_label

        @builtins.property
        def predefined_metric_type(self) -> builtins.str:
            '''The metric type.

            The ``ALBRequestCountPerTarget`` metric type applies only to Spot fleet requests and ECS services.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-predefinedmetricspecification.html#cfn-applicationautoscaling-scalingpolicy-predefinedmetricspecification-predefinedmetrictype
            '''
            result = self._values.get("predefined_metric_type")
            assert result is not None, "Required property 'predefined_metric_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def resource_label(self) -> typing.Optional[builtins.str]:
            '''Identifies the resource associated with the metric type.

            You can't specify a resource label unless the metric type is ``ALBRequestCountPerTarget`` and there is a target group attached to the Spot Fleet or ECS service.

            You create the resource label by appending the final portion of the load balancer ARN and the final portion of the target group ARN into a single value, separated by a forward slash (/). The format of the resource label is:

            ``app/my-alb/778d41231b141a0f/targetgroup/my-alb-target-group/943f017f100becff`` .

            Where:

            - app// is the final portion of the load balancer ARN
            - targetgroup// is the final portion of the target group ARN.

            To find the ARN for an Application Load Balancer, use the `DescribeLoadBalancers <https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeLoadBalancers.html>`_ API operation. To find the ARN for the target group, use the `DescribeTargetGroups <https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeTargetGroups.html>`_ API operation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-predefinedmetricspecification.html#cfn-applicationautoscaling-scalingpolicy-predefinedmetricspecification-resourcelabel
            '''
            result = self._values.get("resource_label")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PredefinedMetricSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_applicationautoscaling.CfnScalingPolicy.StepAdjustmentProperty",
        jsii_struct_bases=[],
        name_mapping={
            "scaling_adjustment": "scalingAdjustment",
            "metric_interval_lower_bound": "metricIntervalLowerBound",
            "metric_interval_upper_bound": "metricIntervalUpperBound",
        },
    )
    class StepAdjustmentProperty:
        def __init__(
            self,
            *,
            scaling_adjustment: jsii.Number,
            metric_interval_lower_bound: typing.Optional[jsii.Number] = None,
            metric_interval_upper_bound: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''``StepAdjustment`` specifies a step adjustment for the ``StepAdjustments`` property of the `AWS::ApplicationAutoScaling::ScalingPolicy StepScalingPolicyConfiguration <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration.html>`_ property type.

            For the following examples, suppose that you have an alarm with a breach threshold of 50:

            - To trigger a step adjustment when the metric is greater than or equal to 50 and less than 60, specify a lower bound of 0 and an upper bound of 10.
            - To trigger a step adjustment when the metric is greater than 40 and less than or equal to 50, specify a lower bound of -10 and an upper bound of 0.

            For more information, see `Step adjustments <https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-step-scaling-policies.html#as-scaling-steps>`_ in the *Application Auto Scaling User Guide* .

            You can find a sample template snippet in the `Examples <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#aws-resource-applicationautoscaling-scalingpolicy--examples>`_ section of the ``AWS::ApplicationAutoScaling::ScalingPolicy`` documentation.

            :param scaling_adjustment: The amount by which to scale. The adjustment is based on the value that you specified in the ``AdjustmentType`` property (either an absolute number or a percentage). A positive value adds to the current capacity and a negative number subtracts from the current capacity.
            :param metric_interval_lower_bound: The lower bound for the difference between the alarm threshold and the CloudWatch metric. If the metric value is above the breach threshold, the lower bound is inclusive (the metric must be greater than or equal to the threshold plus the lower bound). Otherwise, it is exclusive (the metric must be greater than the threshold plus the lower bound). A null value indicates negative infinity. You must specify at least one upper or lower bound.
            :param metric_interval_upper_bound: The upper bound for the difference between the alarm threshold and the CloudWatch metric. If the metric value is above the breach threshold, the upper bound is exclusive (the metric must be less than the threshold plus the upper bound). Otherwise, it is inclusive (the metric must be less than or equal to the threshold plus the upper bound). A null value indicates positive infinity. You must specify at least one upper or lower bound.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepadjustment.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_applicationautoscaling as appscaling
                
                step_adjustment_property = appscaling.CfnScalingPolicy.StepAdjustmentProperty(
                    scaling_adjustment=123,
                
                    # the properties below are optional
                    metric_interval_lower_bound=123,
                    metric_interval_upper_bound=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3a06f512f9ba96f90127c3ef28f9aaa4ff2dd9349ab6fe34199dccd68563dfbe)
                check_type(argname="argument scaling_adjustment", value=scaling_adjustment, expected_type=type_hints["scaling_adjustment"])
                check_type(argname="argument metric_interval_lower_bound", value=metric_interval_lower_bound, expected_type=type_hints["metric_interval_lower_bound"])
                check_type(argname="argument metric_interval_upper_bound", value=metric_interval_upper_bound, expected_type=type_hints["metric_interval_upper_bound"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "scaling_adjustment": scaling_adjustment,
            }
            if metric_interval_lower_bound is not None:
                self._values["metric_interval_lower_bound"] = metric_interval_lower_bound
            if metric_interval_upper_bound is not None:
                self._values["metric_interval_upper_bound"] = metric_interval_upper_bound

        @builtins.property
        def scaling_adjustment(self) -> jsii.Number:
            '''The amount by which to scale.

            The adjustment is based on the value that you specified in the ``AdjustmentType`` property (either an absolute number or a percentage). A positive value adds to the current capacity and a negative number subtracts from the current capacity.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepadjustment.html#cfn-applicationautoscaling-scalingpolicy-stepadjustment-scalingadjustment
            '''
            result = self._values.get("scaling_adjustment")
            assert result is not None, "Required property 'scaling_adjustment' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def metric_interval_lower_bound(self) -> typing.Optional[jsii.Number]:
            '''The lower bound for the difference between the alarm threshold and the CloudWatch metric.

            If the metric value is above the breach threshold, the lower bound is inclusive (the metric must be greater than or equal to the threshold plus the lower bound). Otherwise, it is exclusive (the metric must be greater than the threshold plus the lower bound). A null value indicates negative infinity.

            You must specify at least one upper or lower bound.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepadjustment.html#cfn-applicationautoscaling-scalingpolicy-stepadjustment-metricintervallowerbound
            '''
            result = self._values.get("metric_interval_lower_bound")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def metric_interval_upper_bound(self) -> typing.Optional[jsii.Number]:
            '''The upper bound for the difference between the alarm threshold and the CloudWatch metric.

            If the metric value is above the breach threshold, the upper bound is exclusive (the metric must be less than the threshold plus the upper bound). Otherwise, it is inclusive (the metric must be less than or equal to the threshold plus the upper bound). A null value indicates positive infinity.

            You must specify at least one upper or lower bound.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepadjustment.html#cfn-applicationautoscaling-scalingpolicy-stepadjustment-metricintervalupperbound
            '''
            result = self._values.get("metric_interval_upper_bound")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StepAdjustmentProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_applicationautoscaling.CfnScalingPolicy.StepScalingPolicyConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "adjustment_type": "adjustmentType",
            "cooldown": "cooldown",
            "metric_aggregation_type": "metricAggregationType",
            "min_adjustment_magnitude": "minAdjustmentMagnitude",
            "step_adjustments": "stepAdjustments",
        },
    )
    class StepScalingPolicyConfigurationProperty:
        def __init__(
            self,
            *,
            adjustment_type: typing.Optional[builtins.str] = None,
            cooldown: typing.Optional[jsii.Number] = None,
            metric_aggregation_type: typing.Optional[builtins.str] = None,
            min_adjustment_magnitude: typing.Optional[jsii.Number] = None,
            step_adjustments: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnScalingPolicy.StepAdjustmentProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''``StepScalingPolicyConfiguration`` is a property of the `AWS::ApplicationAutoScaling::ScalingPolicy <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html>`_ resource that specifies a step scaling policy configuration for Application Auto Scaling.

            For more information, see `Step scaling policies <https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-step-scaling-policies.html>`_ in the *Application Auto Scaling User Guide* .

            :param adjustment_type: Specifies whether the ``ScalingAdjustment`` value in the ``StepAdjustment`` property is an absolute number or a percentage of the current capacity.
            :param cooldown: The amount of time, in seconds, to wait for a previous scaling activity to take effect. If not specified, the default value is 300. For more information, see `Cooldown period <https://docs.aws.amazon.com/autoscaling/application/userguide/step-scaling-policy-overview.html#step-scaling-cooldown>`_ in the *Application Auto Scaling User Guide* .
            :param metric_aggregation_type: The aggregation type for the CloudWatch metrics. Valid values are ``Minimum`` , ``Maximum`` , and ``Average`` . If the aggregation type is null, the value is treated as ``Average`` .
            :param min_adjustment_magnitude: The minimum value to scale by when the adjustment type is ``PercentChangeInCapacity`` . For example, suppose that you create a step scaling policy to scale out an Amazon ECS service by 25 percent and you specify a ``MinAdjustmentMagnitude`` of 2. If the service has 4 tasks and the scaling policy is performed, 25 percent of 4 is 1. However, because you specified a ``MinAdjustmentMagnitude`` of 2, Application Auto Scaling scales out the service by 2 tasks.
            :param step_adjustments: A set of adjustments that enable you to scale based on the size of the alarm breach. At least one step adjustment is required if you are adding a new step scaling policy configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_applicationautoscaling as appscaling
                
                step_scaling_policy_configuration_property = appscaling.CfnScalingPolicy.StepScalingPolicyConfigurationProperty(
                    adjustment_type="adjustmentType",
                    cooldown=123,
                    metric_aggregation_type="metricAggregationType",
                    min_adjustment_magnitude=123,
                    step_adjustments=[appscaling.CfnScalingPolicy.StepAdjustmentProperty(
                        scaling_adjustment=123,
                
                        # the properties below are optional
                        metric_interval_lower_bound=123,
                        metric_interval_upper_bound=123
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b0a66ea72967d0887e041501633c1f1033a5f00e71021336a89d0a3e26ad2f04)
                check_type(argname="argument adjustment_type", value=adjustment_type, expected_type=type_hints["adjustment_type"])
                check_type(argname="argument cooldown", value=cooldown, expected_type=type_hints["cooldown"])
                check_type(argname="argument metric_aggregation_type", value=metric_aggregation_type, expected_type=type_hints["metric_aggregation_type"])
                check_type(argname="argument min_adjustment_magnitude", value=min_adjustment_magnitude, expected_type=type_hints["min_adjustment_magnitude"])
                check_type(argname="argument step_adjustments", value=step_adjustments, expected_type=type_hints["step_adjustments"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if adjustment_type is not None:
                self._values["adjustment_type"] = adjustment_type
            if cooldown is not None:
                self._values["cooldown"] = cooldown
            if metric_aggregation_type is not None:
                self._values["metric_aggregation_type"] = metric_aggregation_type
            if min_adjustment_magnitude is not None:
                self._values["min_adjustment_magnitude"] = min_adjustment_magnitude
            if step_adjustments is not None:
                self._values["step_adjustments"] = step_adjustments

        @builtins.property
        def adjustment_type(self) -> typing.Optional[builtins.str]:
            '''Specifies whether the ``ScalingAdjustment`` value in the ``StepAdjustment`` property is an absolute number or a percentage of the current capacity.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration-adjustmenttype
            '''
            result = self._values.get("adjustment_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def cooldown(self) -> typing.Optional[jsii.Number]:
            '''The amount of time, in seconds, to wait for a previous scaling activity to take effect.

            If not specified, the default value is 300. For more information, see `Cooldown period <https://docs.aws.amazon.com/autoscaling/application/userguide/step-scaling-policy-overview.html#step-scaling-cooldown>`_ in the *Application Auto Scaling User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration-cooldown
            '''
            result = self._values.get("cooldown")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def metric_aggregation_type(self) -> typing.Optional[builtins.str]:
            '''The aggregation type for the CloudWatch metrics.

            Valid values are ``Minimum`` , ``Maximum`` , and ``Average`` . If the aggregation type is null, the value is treated as ``Average`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration-metricaggregationtype
            '''
            result = self._values.get("metric_aggregation_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def min_adjustment_magnitude(self) -> typing.Optional[jsii.Number]:
            '''The minimum value to scale by when the adjustment type is ``PercentChangeInCapacity`` .

            For example, suppose that you create a step scaling policy to scale out an Amazon ECS service by 25 percent and you specify a ``MinAdjustmentMagnitude`` of 2. If the service has 4 tasks and the scaling policy is performed, 25 percent of 4 is 1. However, because you specified a ``MinAdjustmentMagnitude`` of 2, Application Auto Scaling scales out the service by 2 tasks.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration-minadjustmentmagnitude
            '''
            result = self._values.get("min_adjustment_magnitude")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def step_adjustments(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnScalingPolicy.StepAdjustmentProperty"]]]]:
            '''A set of adjustments that enable you to scale based on the size of the alarm breach.

            At least one step adjustment is required if you are adding a new step scaling policy configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration-stepadjustments
            '''
            result = self._values.get("step_adjustments")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnScalingPolicy.StepAdjustmentProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StepScalingPolicyConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_applicationautoscaling.CfnScalingPolicy.TargetTrackingMetricDataQueryProperty",
        jsii_struct_bases=[],
        name_mapping={
            "expression": "expression",
            "id": "id",
            "label": "label",
            "metric_stat": "metricStat",
            "return_data": "returnData",
        },
    )
    class TargetTrackingMetricDataQueryProperty:
        def __init__(
            self,
            *,
            expression: typing.Optional[builtins.str] = None,
            id: typing.Optional[builtins.str] = None,
            label: typing.Optional[builtins.str] = None,
            metric_stat: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnScalingPolicy.TargetTrackingMetricStatProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            return_data: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''The metric data to return.

            Also defines whether this call is returning data for one metric only, or whether it is performing a math expression on the values of returned metric statistics to create a new time series. A time series is a series of data points, each of which is associated with a timestamp.

            You can call for a single metric or perform math expressions on multiple metrics. Any expressions used in a metric specification must eventually return a single time series.

            For more information and examples, see `Create a target tracking scaling policy for Application Auto Scaling using metric math <https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-target-tracking-metric-math.html>`_ in the *Application Auto Scaling User Guide* .

            ``TargetTrackingMetricDataQuery`` is a property of the `AWS::ApplicationAutoScaling::ScalingPolicy CustomizedMetricSpecification <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-customizedmetricspecification.html>`_ property type.

            :param expression: The math expression to perform on the returned data, if this object is performing a math expression. This expression can use the ``Id`` of the other metrics to refer to those metrics, and can also use the ``Id`` of other expressions to use the result of those expressions. Conditional: Within each ``TargetTrackingMetricDataQuery`` object, you must specify either ``Expression`` or ``MetricStat`` , but not both.
            :param id: A short name that identifies the object's results in the response. This name must be unique among all ``MetricDataQuery`` objects specified for a single scaling policy. If you are performing math expressions on this set of data, this name represents that data and can serve as a variable in the mathematical expression. The valid characters are letters, numbers, and underscores. The first character must be a lowercase letter.
            :param label: A human-readable label for this metric or expression. This is especially useful if this is a math expression, so that you know what the value represents.
            :param metric_stat: Information about the metric data to return. Conditional: Within each ``MetricDataQuery`` object, you must specify either ``Expression`` or ``MetricStat`` , but not both.
            :param return_data: Indicates whether to return the timestamps and raw data values of this metric. If you use any math expressions, specify ``true`` for this value for only the final math expression that the metric specification is based on. You must specify ``false`` for ``ReturnData`` for all the other metrics and expressions used in the metric specification. If you are only retrieving metrics and not performing any math expressions, do not specify anything for ``ReturnData`` . This sets it to its default ( ``true`` ).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingmetricdataquery.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_applicationautoscaling as appscaling
                
                target_tracking_metric_data_query_property = appscaling.CfnScalingPolicy.TargetTrackingMetricDataQueryProperty(
                    expression="expression",
                    id="id",
                    label="label",
                    metric_stat=appscaling.CfnScalingPolicy.TargetTrackingMetricStatProperty(
                        metric=appscaling.CfnScalingPolicy.TargetTrackingMetricProperty(
                            dimensions=[appscaling.CfnScalingPolicy.TargetTrackingMetricDimensionProperty(
                                name="name",
                                value="value"
                            )],
                            metric_name="metricName",
                            namespace="namespace"
                        ),
                        stat="stat",
                        unit="unit"
                    ),
                    return_data=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__50ed4be037740c44e4f261f3a2c559cf993db7b21e79e7a222e38614cb9f3f1a)
                check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
                check_type(argname="argument id", value=id, expected_type=type_hints["id"])
                check_type(argname="argument label", value=label, expected_type=type_hints["label"])
                check_type(argname="argument metric_stat", value=metric_stat, expected_type=type_hints["metric_stat"])
                check_type(argname="argument return_data", value=return_data, expected_type=type_hints["return_data"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if expression is not None:
                self._values["expression"] = expression
            if id is not None:
                self._values["id"] = id
            if label is not None:
                self._values["label"] = label
            if metric_stat is not None:
                self._values["metric_stat"] = metric_stat
            if return_data is not None:
                self._values["return_data"] = return_data

        @builtins.property
        def expression(self) -> typing.Optional[builtins.str]:
            '''The math expression to perform on the returned data, if this object is performing a math expression.

            This expression can use the ``Id`` of the other metrics to refer to those metrics, and can also use the ``Id`` of other expressions to use the result of those expressions.

            Conditional: Within each ``TargetTrackingMetricDataQuery`` object, you must specify either ``Expression`` or ``MetricStat`` , but not both.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingmetricdataquery.html#cfn-applicationautoscaling-scalingpolicy-targettrackingmetricdataquery-expression
            '''
            result = self._values.get("expression")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def id(self) -> typing.Optional[builtins.str]:
            '''A short name that identifies the object's results in the response.

            This name must be unique among all ``MetricDataQuery`` objects specified for a single scaling policy. If you are performing math expressions on this set of data, this name represents that data and can serve as a variable in the mathematical expression. The valid characters are letters, numbers, and underscores. The first character must be a lowercase letter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingmetricdataquery.html#cfn-applicationautoscaling-scalingpolicy-targettrackingmetricdataquery-id
            '''
            result = self._values.get("id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def label(self) -> typing.Optional[builtins.str]:
            '''A human-readable label for this metric or expression.

            This is especially useful if this is a math expression, so that you know what the value represents.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingmetricdataquery.html#cfn-applicationautoscaling-scalingpolicy-targettrackingmetricdataquery-label
            '''
            result = self._values.get("label")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def metric_stat(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnScalingPolicy.TargetTrackingMetricStatProperty"]]:
            '''Information about the metric data to return.

            Conditional: Within each ``MetricDataQuery`` object, you must specify either ``Expression`` or ``MetricStat`` , but not both.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingmetricdataquery.html#cfn-applicationautoscaling-scalingpolicy-targettrackingmetricdataquery-metricstat
            '''
            result = self._values.get("metric_stat")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnScalingPolicy.TargetTrackingMetricStatProperty"]], result)

        @builtins.property
        def return_data(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates whether to return the timestamps and raw data values of this metric.

            If you use any math expressions, specify ``true`` for this value for only the final math expression that the metric specification is based on. You must specify ``false`` for ``ReturnData`` for all the other metrics and expressions used in the metric specification.

            If you are only retrieving metrics and not performing any math expressions, do not specify anything for ``ReturnData`` . This sets it to its default ( ``true`` ).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingmetricdataquery.html#cfn-applicationautoscaling-scalingpolicy-targettrackingmetricdataquery-returndata
            '''
            result = self._values.get("return_data")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TargetTrackingMetricDataQueryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_applicationautoscaling.CfnScalingPolicy.TargetTrackingMetricDimensionProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "value": "value"},
    )
    class TargetTrackingMetricDimensionProperty:
        def __init__(
            self,
            *,
            name: typing.Optional[builtins.str] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''``TargetTrackingMetricDimension`` specifies a name/value pair that is part of the identity of a CloudWatch metric for the ``Dimensions`` property of the `AWS::ApplicationAutoScaling::ScalingPolicy TargetTrackingMetric <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingmetric.html>`_ property type. Duplicate dimensions are not allowed.

            :param name: The name of the dimension.
            :param value: The value of the dimension.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingmetricdimension.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_applicationautoscaling as appscaling
                
                target_tracking_metric_dimension_property = appscaling.CfnScalingPolicy.TargetTrackingMetricDimensionProperty(
                    name="name",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d6c4fd40c2db7c3177dd019ca0cf15a886d8d3ccd5e0c55cb3d038c3c235eb53)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if name is not None:
                self._values["name"] = name
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the dimension.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingmetricdimension.html#cfn-applicationautoscaling-scalingpolicy-targettrackingmetricdimension-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''The value of the dimension.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingmetricdimension.html#cfn-applicationautoscaling-scalingpolicy-targettrackingmetricdimension-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TargetTrackingMetricDimensionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_applicationautoscaling.CfnScalingPolicy.TargetTrackingMetricProperty",
        jsii_struct_bases=[],
        name_mapping={
            "dimensions": "dimensions",
            "metric_name": "metricName",
            "namespace": "namespace",
        },
    )
    class TargetTrackingMetricProperty:
        def __init__(
            self,
            *,
            dimensions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnScalingPolicy.TargetTrackingMetricDimensionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            metric_name: typing.Optional[builtins.str] = None,
            namespace: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Represents a specific metric for a target tracking scaling policy for Application Auto Scaling.

            Metric is a property of the `AWS::ApplicationAutoScaling::ScalingPolicy TargetTrackingMetricStat <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingmetricstat.html>`_ property type.

            :param dimensions: The dimensions for the metric. For the list of available dimensions, see the AWS documentation available from the table in `AWS services that publish CloudWatch metrics <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/aws-services-cloudwatch-metrics.html>`_ in the *Amazon CloudWatch User Guide* . Conditional: If you published your metric with dimensions, you must specify the same dimensions in your scaling policy.
            :param metric_name: The name of the metric.
            :param namespace: The namespace of the metric. For more information, see the table in `AWS services that publish CloudWatch metrics <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/aws-services-cloudwatch-metrics.html>`_ in the *Amazon CloudWatch User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingmetric.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_applicationautoscaling as appscaling
                
                target_tracking_metric_property = appscaling.CfnScalingPolicy.TargetTrackingMetricProperty(
                    dimensions=[appscaling.CfnScalingPolicy.TargetTrackingMetricDimensionProperty(
                        name="name",
                        value="value"
                    )],
                    metric_name="metricName",
                    namespace="namespace"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a50f07815ea8e711dbbeffa9e2d6ba43154a828c897de162bf209d78b6ce79c6)
                check_type(argname="argument dimensions", value=dimensions, expected_type=type_hints["dimensions"])
                check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
                check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if dimensions is not None:
                self._values["dimensions"] = dimensions
            if metric_name is not None:
                self._values["metric_name"] = metric_name
            if namespace is not None:
                self._values["namespace"] = namespace

        @builtins.property
        def dimensions(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnScalingPolicy.TargetTrackingMetricDimensionProperty"]]]]:
            '''The dimensions for the metric.

            For the list of available dimensions, see the AWS documentation available from the table in `AWS services that publish CloudWatch metrics <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/aws-services-cloudwatch-metrics.html>`_ in the *Amazon CloudWatch User Guide* .

            Conditional: If you published your metric with dimensions, you must specify the same dimensions in your scaling policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingmetric.html#cfn-applicationautoscaling-scalingpolicy-targettrackingmetric-dimensions
            '''
            result = self._values.get("dimensions")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnScalingPolicy.TargetTrackingMetricDimensionProperty"]]]], result)

        @builtins.property
        def metric_name(self) -> typing.Optional[builtins.str]:
            '''The name of the metric.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingmetric.html#cfn-applicationautoscaling-scalingpolicy-targettrackingmetric-metricname
            '''
            result = self._values.get("metric_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def namespace(self) -> typing.Optional[builtins.str]:
            '''The namespace of the metric.

            For more information, see the table in `AWS services that publish CloudWatch metrics <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/aws-services-cloudwatch-metrics.html>`_ in the *Amazon CloudWatch User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingmetric.html#cfn-applicationautoscaling-scalingpolicy-targettrackingmetric-namespace
            '''
            result = self._values.get("namespace")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TargetTrackingMetricProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_applicationautoscaling.CfnScalingPolicy.TargetTrackingMetricStatProperty",
        jsii_struct_bases=[],
        name_mapping={"metric": "metric", "stat": "stat", "unit": "unit"},
    )
    class TargetTrackingMetricStatProperty:
        def __init__(
            self,
            *,
            metric: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnScalingPolicy.TargetTrackingMetricProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            stat: typing.Optional[builtins.str] = None,
            unit: typing.Optional[builtins.str] = None,
        ) -> None:
            '''This structure defines the CloudWatch metric to return, along with the statistic and unit.

            ``TargetTrackingMetricStat`` is a property of the `AWS::ApplicationAutoScaling::ScalingPolicy TargetTrackingMetricDataQuery <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingmetricdataquery.html>`_ property type.

            For more information about the CloudWatch terminology below, see `Amazon CloudWatch concepts <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html>`_ in the *Amazon CloudWatch User Guide* .

            :param metric: The CloudWatch metric to return, including the metric name, namespace, and dimensions. To get the exact metric name, namespace, and dimensions, inspect the `Metric <https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_Metric.html>`_ object that is returned by a call to `ListMetrics <https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ListMetrics.html>`_ .
            :param stat: The statistic to return. It can include any CloudWatch statistic or extended statistic. For a list of valid values, see the table in `Statistics <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Statistic>`_ in the *Amazon CloudWatch User Guide* . The most commonly used metric for scaling is ``Average`` .
            :param unit: The unit to use for the returned data points. For a complete list of the units that CloudWatch supports, see the `MetricDatum <https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_MetricDatum.html>`_ data type in the *Amazon CloudWatch API Reference* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingmetricstat.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_applicationautoscaling as appscaling
                
                target_tracking_metric_stat_property = appscaling.CfnScalingPolicy.TargetTrackingMetricStatProperty(
                    metric=appscaling.CfnScalingPolicy.TargetTrackingMetricProperty(
                        dimensions=[appscaling.CfnScalingPolicy.TargetTrackingMetricDimensionProperty(
                            name="name",
                            value="value"
                        )],
                        metric_name="metricName",
                        namespace="namespace"
                    ),
                    stat="stat",
                    unit="unit"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__82b9cd8a8d1359a0e0fa7d4aef2938489da73589171a3927e18618a9db7d28c5)
                check_type(argname="argument metric", value=metric, expected_type=type_hints["metric"])
                check_type(argname="argument stat", value=stat, expected_type=type_hints["stat"])
                check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if metric is not None:
                self._values["metric"] = metric
            if stat is not None:
                self._values["stat"] = stat
            if unit is not None:
                self._values["unit"] = unit

        @builtins.property
        def metric(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnScalingPolicy.TargetTrackingMetricProperty"]]:
            '''The CloudWatch metric to return, including the metric name, namespace, and dimensions.

            To get the exact metric name, namespace, and dimensions, inspect the `Metric <https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_Metric.html>`_ object that is returned by a call to `ListMetrics <https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ListMetrics.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingmetricstat.html#cfn-applicationautoscaling-scalingpolicy-targettrackingmetricstat-metric
            '''
            result = self._values.get("metric")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnScalingPolicy.TargetTrackingMetricProperty"]], result)

        @builtins.property
        def stat(self) -> typing.Optional[builtins.str]:
            '''The statistic to return.

            It can include any CloudWatch statistic or extended statistic. For a list of valid values, see the table in `Statistics <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Statistic>`_ in the *Amazon CloudWatch User Guide* .

            The most commonly used metric for scaling is ``Average`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingmetricstat.html#cfn-applicationautoscaling-scalingpolicy-targettrackingmetricstat-stat
            '''
            result = self._values.get("stat")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def unit(self) -> typing.Optional[builtins.str]:
            '''The unit to use for the returned data points.

            For a complete list of the units that CloudWatch supports, see the `MetricDatum <https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_MetricDatum.html>`_ data type in the *Amazon CloudWatch API Reference* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingmetricstat.html#cfn-applicationautoscaling-scalingpolicy-targettrackingmetricstat-unit
            '''
            result = self._values.get("unit")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TargetTrackingMetricStatProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_applicationautoscaling.CfnScalingPolicy.TargetTrackingScalingPolicyConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "target_value": "targetValue",
            "customized_metric_specification": "customizedMetricSpecification",
            "disable_scale_in": "disableScaleIn",
            "predefined_metric_specification": "predefinedMetricSpecification",
            "scale_in_cooldown": "scaleInCooldown",
            "scale_out_cooldown": "scaleOutCooldown",
        },
    )
    class TargetTrackingScalingPolicyConfigurationProperty:
        def __init__(
            self,
            *,
            target_value: jsii.Number,
            customized_metric_specification: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnScalingPolicy.CustomizedMetricSpecificationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            disable_scale_in: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            predefined_metric_specification: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnScalingPolicy.PredefinedMetricSpecificationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            scale_in_cooldown: typing.Optional[jsii.Number] = None,
            scale_out_cooldown: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''``TargetTrackingScalingPolicyConfiguration`` is a property of the `AWS::ApplicationAutoScaling::ScalingPolicy <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html>`_ resource that specifies a target tracking scaling policy configuration for Application Auto Scaling. Use a target tracking scaling policy to adjust the capacity of the specified scalable target in response to actual workloads, so that resource utilization remains at or near the target utilization value.

            For more information, see `Target tracking scaling policies <https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-target-tracking.html>`_ in the *Application Auto Scaling User Guide* .

            :param target_value: The target value for the metric. Although this property accepts numbers of type Double, it won't accept values that are either too small or too large. Values must be in the range of -2^360 to 2^360. The value must be a valid number based on the choice of metric. For example, if the metric is CPU utilization, then the target value is a percent value that represents how much of the CPU can be used before scaling out.
            :param customized_metric_specification: A customized metric. You can specify either a predefined metric or a customized metric.
            :param disable_scale_in: Indicates whether scale in by the target tracking scaling policy is disabled. If the value is ``true`` , scale in is disabled and the target tracking scaling policy won't remove capacity from the scalable target. Otherwise, scale in is enabled and the target tracking scaling policy can remove capacity from the scalable target. The default value is ``false`` .
            :param predefined_metric_specification: A predefined metric. You can specify either a predefined metric or a customized metric.
            :param scale_in_cooldown: The amount of time, in seconds, after a scale-in activity completes before another scale-in activity can start. For more information and for default values, see `Define cooldown periods <https://docs.aws.amazon.com/autoscaling/application/userguide/target-tracking-scaling-policy-overview.html#target-tracking-cooldown>`_ in the *Application Auto Scaling User Guide* .
            :param scale_out_cooldown: The amount of time, in seconds, to wait for a previous scale-out activity to take effect. For more information and for default values, see `Define cooldown periods <https://docs.aws.amazon.com/autoscaling/application/userguide/target-tracking-scaling-policy-overview.html#target-tracking-cooldown>`_ in the *Application Auto Scaling User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_applicationautoscaling as appscaling
                
                target_tracking_scaling_policy_configuration_property = appscaling.CfnScalingPolicy.TargetTrackingScalingPolicyConfigurationProperty(
                    target_value=123,
                
                    # the properties below are optional
                    customized_metric_specification=appscaling.CfnScalingPolicy.CustomizedMetricSpecificationProperty(
                        dimensions=[appscaling.CfnScalingPolicy.MetricDimensionProperty(
                            name="name",
                            value="value"
                        )],
                        metric_name="metricName",
                        metrics=[appscaling.CfnScalingPolicy.TargetTrackingMetricDataQueryProperty(
                            expression="expression",
                            id="id",
                            label="label",
                            metric_stat=appscaling.CfnScalingPolicy.TargetTrackingMetricStatProperty(
                                metric=appscaling.CfnScalingPolicy.TargetTrackingMetricProperty(
                                    dimensions=[appscaling.CfnScalingPolicy.TargetTrackingMetricDimensionProperty(
                                        name="name",
                                        value="value"
                                    )],
                                    metric_name="metricName",
                                    namespace="namespace"
                                ),
                                stat="stat",
                                unit="unit"
                            ),
                            return_data=False
                        )],
                        namespace="namespace",
                        statistic="statistic",
                        unit="unit"
                    ),
                    disable_scale_in=False,
                    predefined_metric_specification=appscaling.CfnScalingPolicy.PredefinedMetricSpecificationProperty(
                        predefined_metric_type="predefinedMetricType",
                
                        # the properties below are optional
                        resource_label="resourceLabel"
                    ),
                    scale_in_cooldown=123,
                    scale_out_cooldown=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5d9326d5963b2f7c66feebec5211250ac93b956fe269a70f64aeb370aa662e58)
                check_type(argname="argument target_value", value=target_value, expected_type=type_hints["target_value"])
                check_type(argname="argument customized_metric_specification", value=customized_metric_specification, expected_type=type_hints["customized_metric_specification"])
                check_type(argname="argument disable_scale_in", value=disable_scale_in, expected_type=type_hints["disable_scale_in"])
                check_type(argname="argument predefined_metric_specification", value=predefined_metric_specification, expected_type=type_hints["predefined_metric_specification"])
                check_type(argname="argument scale_in_cooldown", value=scale_in_cooldown, expected_type=type_hints["scale_in_cooldown"])
                check_type(argname="argument scale_out_cooldown", value=scale_out_cooldown, expected_type=type_hints["scale_out_cooldown"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "target_value": target_value,
            }
            if customized_metric_specification is not None:
                self._values["customized_metric_specification"] = customized_metric_specification
            if disable_scale_in is not None:
                self._values["disable_scale_in"] = disable_scale_in
            if predefined_metric_specification is not None:
                self._values["predefined_metric_specification"] = predefined_metric_specification
            if scale_in_cooldown is not None:
                self._values["scale_in_cooldown"] = scale_in_cooldown
            if scale_out_cooldown is not None:
                self._values["scale_out_cooldown"] = scale_out_cooldown

        @builtins.property
        def target_value(self) -> jsii.Number:
            '''The target value for the metric.

            Although this property accepts numbers of type Double, it won't accept values that are either too small or too large. Values must be in the range of -2^360 to 2^360. The value must be a valid number based on the choice of metric. For example, if the metric is CPU utilization, then the target value is a percent value that represents how much of the CPU can be used before scaling out.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration-targetvalue
            '''
            result = self._values.get("target_value")
            assert result is not None, "Required property 'target_value' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def customized_metric_specification(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnScalingPolicy.CustomizedMetricSpecificationProperty"]]:
            '''A customized metric.

            You can specify either a predefined metric or a customized metric.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration-customizedmetricspecification
            '''
            result = self._values.get("customized_metric_specification")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnScalingPolicy.CustomizedMetricSpecificationProperty"]], result)

        @builtins.property
        def disable_scale_in(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates whether scale in by the target tracking scaling policy is disabled.

            If the value is ``true`` , scale in is disabled and the target tracking scaling policy won't remove capacity from the scalable target. Otherwise, scale in is enabled and the target tracking scaling policy can remove capacity from the scalable target. The default value is ``false`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration-disablescalein
            '''
            result = self._values.get("disable_scale_in")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def predefined_metric_specification(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnScalingPolicy.PredefinedMetricSpecificationProperty"]]:
            '''A predefined metric.

            You can specify either a predefined metric or a customized metric.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration-predefinedmetricspecification
            '''
            result = self._values.get("predefined_metric_specification")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnScalingPolicy.PredefinedMetricSpecificationProperty"]], result)

        @builtins.property
        def scale_in_cooldown(self) -> typing.Optional[jsii.Number]:
            '''The amount of time, in seconds, after a scale-in activity completes before another scale-in activity can start.

            For more information and for default values, see `Define cooldown periods <https://docs.aws.amazon.com/autoscaling/application/userguide/target-tracking-scaling-policy-overview.html#target-tracking-cooldown>`_ in the *Application Auto Scaling User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration-scaleincooldown
            '''
            result = self._values.get("scale_in_cooldown")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def scale_out_cooldown(self) -> typing.Optional[jsii.Number]:
            '''The amount of time, in seconds, to wait for a previous scale-out activity to take effect.

            For more information and for default values, see `Define cooldown periods <https://docs.aws.amazon.com/autoscaling/application/userguide/target-tracking-scaling-policy-overview.html#target-tracking-cooldown>`_ in the *Application Auto Scaling User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration.html#cfn-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration-scaleoutcooldown
            '''
            result = self._values.get("scale_out_cooldown")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TargetTrackingScalingPolicyConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_applicationautoscaling.CfnScalingPolicyProps",
    jsii_struct_bases=[],
    name_mapping={
        "policy_name": "policyName",
        "policy_type": "policyType",
        "resource_id": "resourceId",
        "scalable_dimension": "scalableDimension",
        "scaling_target_id": "scalingTargetId",
        "service_namespace": "serviceNamespace",
        "step_scaling_policy_configuration": "stepScalingPolicyConfiguration",
        "target_tracking_scaling_policy_configuration": "targetTrackingScalingPolicyConfiguration",
    },
)
class CfnScalingPolicyProps:
    def __init__(
        self,
        *,
        policy_name: builtins.str,
        policy_type: builtins.str,
        resource_id: typing.Optional[builtins.str] = None,
        scalable_dimension: typing.Optional[builtins.str] = None,
        scaling_target_id: typing.Optional[builtins.str] = None,
        service_namespace: typing.Optional[builtins.str] = None,
        step_scaling_policy_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnScalingPolicy.StepScalingPolicyConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        target_tracking_scaling_policy_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnScalingPolicy.TargetTrackingScalingPolicyConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnScalingPolicy``.

        :param policy_name: The name of the scaling policy. Updates to the name of a target tracking scaling policy are not supported, unless you also update the metric used for scaling. To change only a target tracking scaling policy's name, first delete the policy by removing the existing ``AWS::ApplicationAutoScaling::ScalingPolicy`` resource from the template and updating the stack. Then, recreate the resource with the same settings and a different name.
        :param policy_type: The scaling policy type. The following policy types are supported: ``TargetTrackingScaling`` —Not supported for Amazon EMR ``StepScaling`` —Not supported for DynamoDB, Amazon Comprehend, Lambda, Amazon Keyspaces, Amazon MSK, Amazon ElastiCache, or Neptune.
        :param resource_id: The identifier of the resource associated with the scaling policy. This string consists of the resource type and unique identifier. - ECS service - The resource type is ``service`` and the unique identifier is the cluster name and service name. Example: ``service/my-cluster/my-service`` . - Spot Fleet - The resource type is ``spot-fleet-request`` and the unique identifier is the Spot Fleet request ID. Example: ``spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`` . - EMR cluster - The resource type is ``instancegroup`` and the unique identifier is the cluster ID and instance group ID. Example: ``instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0`` . - AppStream 2.0 fleet - The resource type is ``fleet`` and the unique identifier is the fleet name. Example: ``fleet/sample-fleet`` . - DynamoDB table - The resource type is ``table`` and the unique identifier is the table name. Example: ``table/my-table`` . - DynamoDB global secondary index - The resource type is ``index`` and the unique identifier is the index name. Example: ``table/my-table/index/my-table-index`` . - Aurora DB cluster - The resource type is ``cluster`` and the unique identifier is the cluster name. Example: ``cluster:my-db-cluster`` . - SageMaker endpoint variant - The resource type is ``variant`` and the unique identifier is the resource ID. Example: ``endpoint/my-end-point/variant/KMeansClustering`` . - Custom resources are not supported with a resource type. This parameter must specify the ``OutputValue`` from the CloudFormation template stack used to access the resources. The unique identifier is defined by the service provider. More information is available in our `GitHub repository <https://docs.aws.amazon.com/https://github.com/aws/aws-auto-scaling-custom-resource>`_ . - Amazon Comprehend document classification endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: ``arn:aws:comprehend:us-west-2:123456789012:document-classifier-endpoint/EXAMPLE`` . - Amazon Comprehend entity recognizer endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: ``arn:aws:comprehend:us-west-2:123456789012:entity-recognizer-endpoint/EXAMPLE`` . - Lambda provisioned concurrency - The resource type is ``function`` and the unique identifier is the function name with a function version or alias name suffix that is not ``$LATEST`` . Example: ``function:my-function:prod`` or ``function:my-function:1`` . - Amazon Keyspaces table - The resource type is ``table`` and the unique identifier is the table name. Example: ``keyspace/mykeyspace/table/mytable`` . - Amazon MSK cluster - The resource type and unique identifier are specified using the cluster ARN. Example: ``arn:aws:kafka:us-east-1:123456789012:cluster/demo-cluster-1/6357e0b2-0e6a-4b86-a0b4-70df934c2e31-5`` . - Amazon ElastiCache replication group - The resource type is ``replication-group`` and the unique identifier is the replication group name. Example: ``replication-group/mycluster`` . - Neptune cluster - The resource type is ``cluster`` and the unique identifier is the cluster name. Example: ``cluster:mycluster`` . - SageMaker serverless endpoint - The resource type is ``variant`` and the unique identifier is the resource ID. Example: ``endpoint/my-end-point/variant/KMeansClustering`` . - SageMaker inference component - The resource type is ``inference-component`` and the unique identifier is the resource ID. Example: ``inference-component/my-inference-component`` .
        :param scalable_dimension: The scalable dimension. This string consists of the service namespace, resource type, and scaling property. - ``ecs:service:DesiredCount`` - The desired task count of an ECS service. - ``elasticmapreduce:instancegroup:InstanceCount`` - The instance count of an EMR Instance Group. - ``ec2:spot-fleet-request:TargetCapacity`` - The target capacity of a Spot Fleet. - ``appstream:fleet:DesiredCapacity`` - The desired capacity of an AppStream 2.0 fleet. - ``dynamodb:table:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB table. - ``dynamodb:table:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB table. - ``dynamodb:index:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB global secondary index. - ``dynamodb:index:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB global secondary index. - ``rds:cluster:ReadReplicaCount`` - The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition and Aurora PostgreSQL-compatible edition. - ``sagemaker:variant:DesiredInstanceCount`` - The number of EC2 instances for a SageMaker model endpoint variant. - ``custom-resource:ResourceType:Property`` - The scalable dimension for a custom resource provided by your own application or service. - ``comprehend:document-classifier-endpoint:DesiredInferenceUnits`` - The number of inference units for an Amazon Comprehend document classification endpoint. - ``comprehend:entity-recognizer-endpoint:DesiredInferenceUnits`` - The number of inference units for an Amazon Comprehend entity recognizer endpoint. - ``lambda:function:ProvisionedConcurrency`` - The provisioned concurrency for a Lambda function. - ``cassandra:table:ReadCapacityUnits`` - The provisioned read capacity for an Amazon Keyspaces table. - ``cassandra:table:WriteCapacityUnits`` - The provisioned write capacity for an Amazon Keyspaces table. - ``kafka:broker-storage:VolumeSize`` - The provisioned volume size (in GiB) for brokers in an Amazon MSK cluster. - ``elasticache:replication-group:NodeGroups`` - The number of node groups for an Amazon ElastiCache replication group. - ``elasticache:replication-group:Replicas`` - The number of replicas per node group for an Amazon ElastiCache replication group. - ``neptune:cluster:ReadReplicaCount`` - The count of read replicas in an Amazon Neptune DB cluster. - ``sagemaker:variant:DesiredProvisionedConcurrency`` - The provisioned concurrency for a SageMaker serverless endpoint. - ``sagemaker:inference-component:DesiredCopyCount`` - The number of copies across an endpoint for a SageMaker inference component.
        :param scaling_target_id: The CloudFormation-generated ID of an Application Auto Scaling scalable target. For more information about the ID, see the Return Value section of the ``AWS::ApplicationAutoScaling::ScalableTarget`` resource. .. epigraph:: You must specify either the ``ScalingTargetId`` property, or the ``ResourceId`` , ``ScalableDimension`` , and ``ServiceNamespace`` properties, but not both.
        :param service_namespace: The namespace of the AWS service that provides the resource, or a ``custom-resource`` .
        :param step_scaling_policy_configuration: A step scaling policy.
        :param target_tracking_scaling_policy_configuration: A target tracking scaling policy.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_applicationautoscaling as appscaling
            
            cfn_scaling_policy_props = appscaling.CfnScalingPolicyProps(
                policy_name="policyName",
                policy_type="policyType",
            
                # the properties below are optional
                resource_id="resourceId",
                scalable_dimension="scalableDimension",
                scaling_target_id="scalingTargetId",
                service_namespace="serviceNamespace",
                step_scaling_policy_configuration=appscaling.CfnScalingPolicy.StepScalingPolicyConfigurationProperty(
                    adjustment_type="adjustmentType",
                    cooldown=123,
                    metric_aggregation_type="metricAggregationType",
                    min_adjustment_magnitude=123,
                    step_adjustments=[appscaling.CfnScalingPolicy.StepAdjustmentProperty(
                        scaling_adjustment=123,
            
                        # the properties below are optional
                        metric_interval_lower_bound=123,
                        metric_interval_upper_bound=123
                    )]
                ),
                target_tracking_scaling_policy_configuration=appscaling.CfnScalingPolicy.TargetTrackingScalingPolicyConfigurationProperty(
                    target_value=123,
            
                    # the properties below are optional
                    customized_metric_specification=appscaling.CfnScalingPolicy.CustomizedMetricSpecificationProperty(
                        dimensions=[appscaling.CfnScalingPolicy.MetricDimensionProperty(
                            name="name",
                            value="value"
                        )],
                        metric_name="metricName",
                        metrics=[appscaling.CfnScalingPolicy.TargetTrackingMetricDataQueryProperty(
                            expression="expression",
                            id="id",
                            label="label",
                            metric_stat=appscaling.CfnScalingPolicy.TargetTrackingMetricStatProperty(
                                metric=appscaling.CfnScalingPolicy.TargetTrackingMetricProperty(
                                    dimensions=[appscaling.CfnScalingPolicy.TargetTrackingMetricDimensionProperty(
                                        name="name",
                                        value="value"
                                    )],
                                    metric_name="metricName",
                                    namespace="namespace"
                                ),
                                stat="stat",
                                unit="unit"
                            ),
                            return_data=False
                        )],
                        namespace="namespace",
                        statistic="statistic",
                        unit="unit"
                    ),
                    disable_scale_in=False,
                    predefined_metric_specification=appscaling.CfnScalingPolicy.PredefinedMetricSpecificationProperty(
                        predefined_metric_type="predefinedMetricType",
            
                        # the properties below are optional
                        resource_label="resourceLabel"
                    ),
                    scale_in_cooldown=123,
                    scale_out_cooldown=123
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eabc9b9cdfb95f21a9439a9250c214148ffe31ecc08a87e6125ff826c886f42c)
            check_type(argname="argument policy_name", value=policy_name, expected_type=type_hints["policy_name"])
            check_type(argname="argument policy_type", value=policy_type, expected_type=type_hints["policy_type"])
            check_type(argname="argument resource_id", value=resource_id, expected_type=type_hints["resource_id"])
            check_type(argname="argument scalable_dimension", value=scalable_dimension, expected_type=type_hints["scalable_dimension"])
            check_type(argname="argument scaling_target_id", value=scaling_target_id, expected_type=type_hints["scaling_target_id"])
            check_type(argname="argument service_namespace", value=service_namespace, expected_type=type_hints["service_namespace"])
            check_type(argname="argument step_scaling_policy_configuration", value=step_scaling_policy_configuration, expected_type=type_hints["step_scaling_policy_configuration"])
            check_type(argname="argument target_tracking_scaling_policy_configuration", value=target_tracking_scaling_policy_configuration, expected_type=type_hints["target_tracking_scaling_policy_configuration"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "policy_name": policy_name,
            "policy_type": policy_type,
        }
        if resource_id is not None:
            self._values["resource_id"] = resource_id
        if scalable_dimension is not None:
            self._values["scalable_dimension"] = scalable_dimension
        if scaling_target_id is not None:
            self._values["scaling_target_id"] = scaling_target_id
        if service_namespace is not None:
            self._values["service_namespace"] = service_namespace
        if step_scaling_policy_configuration is not None:
            self._values["step_scaling_policy_configuration"] = step_scaling_policy_configuration
        if target_tracking_scaling_policy_configuration is not None:
            self._values["target_tracking_scaling_policy_configuration"] = target_tracking_scaling_policy_configuration

    @builtins.property
    def policy_name(self) -> builtins.str:
        '''The name of the scaling policy.

        Updates to the name of a target tracking scaling policy are not supported, unless you also update the metric used for scaling. To change only a target tracking scaling policy's name, first delete the policy by removing the existing ``AWS::ApplicationAutoScaling::ScalingPolicy`` resource from the template and updating the stack. Then, recreate the resource with the same settings and a different name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#cfn-applicationautoscaling-scalingpolicy-policyname
        '''
        result = self._values.get("policy_name")
        assert result is not None, "Required property 'policy_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def policy_type(self) -> builtins.str:
        '''The scaling policy type.

        The following policy types are supported:

        ``TargetTrackingScaling`` —Not supported for Amazon EMR

        ``StepScaling`` —Not supported for DynamoDB, Amazon Comprehend, Lambda, Amazon Keyspaces, Amazon MSK, Amazon ElastiCache, or Neptune.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#cfn-applicationautoscaling-scalingpolicy-policytype
        '''
        result = self._values.get("policy_type")
        assert result is not None, "Required property 'policy_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_id(self) -> typing.Optional[builtins.str]:
        '''The identifier of the resource associated with the scaling policy.

        This string consists of the resource type and unique identifier.

        - ECS service - The resource type is ``service`` and the unique identifier is the cluster name and service name. Example: ``service/my-cluster/my-service`` .
        - Spot Fleet - The resource type is ``spot-fleet-request`` and the unique identifier is the Spot Fleet request ID. Example: ``spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`` .
        - EMR cluster - The resource type is ``instancegroup`` and the unique identifier is the cluster ID and instance group ID. Example: ``instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0`` .
        - AppStream 2.0 fleet - The resource type is ``fleet`` and the unique identifier is the fleet name. Example: ``fleet/sample-fleet`` .
        - DynamoDB table - The resource type is ``table`` and the unique identifier is the table name. Example: ``table/my-table`` .
        - DynamoDB global secondary index - The resource type is ``index`` and the unique identifier is the index name. Example: ``table/my-table/index/my-table-index`` .
        - Aurora DB cluster - The resource type is ``cluster`` and the unique identifier is the cluster name. Example: ``cluster:my-db-cluster`` .
        - SageMaker endpoint variant - The resource type is ``variant`` and the unique identifier is the resource ID. Example: ``endpoint/my-end-point/variant/KMeansClustering`` .
        - Custom resources are not supported with a resource type. This parameter must specify the ``OutputValue`` from the CloudFormation template stack used to access the resources. The unique identifier is defined by the service provider. More information is available in our `GitHub repository <https://docs.aws.amazon.com/https://github.com/aws/aws-auto-scaling-custom-resource>`_ .
        - Amazon Comprehend document classification endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: ``arn:aws:comprehend:us-west-2:123456789012:document-classifier-endpoint/EXAMPLE`` .
        - Amazon Comprehend entity recognizer endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: ``arn:aws:comprehend:us-west-2:123456789012:entity-recognizer-endpoint/EXAMPLE`` .
        - Lambda provisioned concurrency - The resource type is ``function`` and the unique identifier is the function name with a function version or alias name suffix that is not ``$LATEST`` . Example: ``function:my-function:prod`` or ``function:my-function:1`` .
        - Amazon Keyspaces table - The resource type is ``table`` and the unique identifier is the table name. Example: ``keyspace/mykeyspace/table/mytable`` .
        - Amazon MSK cluster - The resource type and unique identifier are specified using the cluster ARN. Example: ``arn:aws:kafka:us-east-1:123456789012:cluster/demo-cluster-1/6357e0b2-0e6a-4b86-a0b4-70df934c2e31-5`` .
        - Amazon ElastiCache replication group - The resource type is ``replication-group`` and the unique identifier is the replication group name. Example: ``replication-group/mycluster`` .
        - Neptune cluster - The resource type is ``cluster`` and the unique identifier is the cluster name. Example: ``cluster:mycluster`` .
        - SageMaker serverless endpoint - The resource type is ``variant`` and the unique identifier is the resource ID. Example: ``endpoint/my-end-point/variant/KMeansClustering`` .
        - SageMaker inference component - The resource type is ``inference-component`` and the unique identifier is the resource ID. Example: ``inference-component/my-inference-component`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#cfn-applicationautoscaling-scalingpolicy-resourceid
        '''
        result = self._values.get("resource_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scalable_dimension(self) -> typing.Optional[builtins.str]:
        '''The scalable dimension. This string consists of the service namespace, resource type, and scaling property.

        - ``ecs:service:DesiredCount`` - The desired task count of an ECS service.
        - ``elasticmapreduce:instancegroup:InstanceCount`` - The instance count of an EMR Instance Group.
        - ``ec2:spot-fleet-request:TargetCapacity`` - The target capacity of a Spot Fleet.
        - ``appstream:fleet:DesiredCapacity`` - The desired capacity of an AppStream 2.0 fleet.
        - ``dynamodb:table:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB table.
        - ``dynamodb:table:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB table.
        - ``dynamodb:index:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB global secondary index.
        - ``dynamodb:index:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB global secondary index.
        - ``rds:cluster:ReadReplicaCount`` - The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition and Aurora PostgreSQL-compatible edition.
        - ``sagemaker:variant:DesiredInstanceCount`` - The number of EC2 instances for a SageMaker model endpoint variant.
        - ``custom-resource:ResourceType:Property`` - The scalable dimension for a custom resource provided by your own application or service.
        - ``comprehend:document-classifier-endpoint:DesiredInferenceUnits`` - The number of inference units for an Amazon Comprehend document classification endpoint.
        - ``comprehend:entity-recognizer-endpoint:DesiredInferenceUnits`` - The number of inference units for an Amazon Comprehend entity recognizer endpoint.
        - ``lambda:function:ProvisionedConcurrency`` - The provisioned concurrency for a Lambda function.
        - ``cassandra:table:ReadCapacityUnits`` - The provisioned read capacity for an Amazon Keyspaces table.
        - ``cassandra:table:WriteCapacityUnits`` - The provisioned write capacity for an Amazon Keyspaces table.
        - ``kafka:broker-storage:VolumeSize`` - The provisioned volume size (in GiB) for brokers in an Amazon MSK cluster.
        - ``elasticache:replication-group:NodeGroups`` - The number of node groups for an Amazon ElastiCache replication group.
        - ``elasticache:replication-group:Replicas`` - The number of replicas per node group for an Amazon ElastiCache replication group.
        - ``neptune:cluster:ReadReplicaCount`` - The count of read replicas in an Amazon Neptune DB cluster.
        - ``sagemaker:variant:DesiredProvisionedConcurrency`` - The provisioned concurrency for a SageMaker serverless endpoint.
        - ``sagemaker:inference-component:DesiredCopyCount`` - The number of copies across an endpoint for a SageMaker inference component.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#cfn-applicationautoscaling-scalingpolicy-scalabledimension
        '''
        result = self._values.get("scalable_dimension")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scaling_target_id(self) -> typing.Optional[builtins.str]:
        '''The CloudFormation-generated ID of an Application Auto Scaling scalable target.

        For more information about the ID, see the Return Value section of the ``AWS::ApplicationAutoScaling::ScalableTarget`` resource.
        .. epigraph::

           You must specify either the ``ScalingTargetId`` property, or the ``ResourceId`` , ``ScalableDimension`` , and ``ServiceNamespace`` properties, but not both.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#cfn-applicationautoscaling-scalingpolicy-scalingtargetid
        '''
        result = self._values.get("scaling_target_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_namespace(self) -> typing.Optional[builtins.str]:
        '''The namespace of the AWS service that provides the resource, or a ``custom-resource`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#cfn-applicationautoscaling-scalingpolicy-servicenamespace
        '''
        result = self._values.get("service_namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def step_scaling_policy_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnScalingPolicy.StepScalingPolicyConfigurationProperty]]:
        '''A step scaling policy.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#cfn-applicationautoscaling-scalingpolicy-stepscalingpolicyconfiguration
        '''
        result = self._values.get("step_scaling_policy_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnScalingPolicy.StepScalingPolicyConfigurationProperty]], result)

    @builtins.property
    def target_tracking_scaling_policy_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnScalingPolicy.TargetTrackingScalingPolicyConfigurationProperty]]:
        '''A target tracking scaling policy.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html#cfn-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration
        '''
        result = self._values.get("target_tracking_scaling_policy_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnScalingPolicy.TargetTrackingScalingPolicyConfigurationProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnScalingPolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_applicationautoscaling.CronOptions",
    jsii_struct_bases=[],
    name_mapping={
        "day": "day",
        "hour": "hour",
        "minute": "minute",
        "month": "month",
        "week_day": "weekDay",
        "year": "year",
    },
)
class CronOptions:
    def __init__(
        self,
        *,
        day: typing.Optional[builtins.str] = None,
        hour: typing.Optional[builtins.str] = None,
        minute: typing.Optional[builtins.str] = None,
        month: typing.Optional[builtins.str] = None,
        week_day: typing.Optional[builtins.str] = None,
        year: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Options to configure a cron expression.

        All fields are strings so you can use complex expressions. Absence of
        a field implies '*' or '?', whichever one is appropriate.

        :param day: The day of the month to run this rule at. Default: - Every day of the month
        :param hour: The hour to run this rule at. Default: - Every hour
        :param minute: The minute to run this rule at. Default: - Every minute
        :param month: The month to run this rule at. Default: - Every month
        :param week_day: The day of the week to run this rule at. Default: - Any day of the week
        :param year: The year to run this rule at. Default: - Every year

        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html#CronExpressions
        :exampleMetadata: infused

        Example::

            # cluster: ecs.Cluster
            
            load_balanced_fargate_service = ecs_patterns.ApplicationLoadBalancedFargateService(self, "Service",
                cluster=cluster,
                memory_limit_mi_b=1024,
                desired_count=1,
                cpu=512,
                task_image_options=ecsPatterns.ApplicationLoadBalancedTaskImageOptions(
                    image=ecs.ContainerImage.from_registry("amazon/amazon-ecs-sample")
                )
            )
            
            scalable_target = load_balanced_fargate_service.service.auto_scale_task_count(
                min_capacity=5,
                max_capacity=20
            )
            
            scalable_target.scale_on_schedule("DaytimeScaleDown",
                schedule=appscaling.Schedule.cron(hour="8", minute="0"),
                min_capacity=1
            )
            
            scalable_target.scale_on_schedule("EveningRushScaleUp",
                schedule=appscaling.Schedule.cron(hour="20", minute="0"),
                min_capacity=10
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6de063595e26cfdffe8cc2657f923bb73bea86791277de8f39a31cb702a88687)
            check_type(argname="argument day", value=day, expected_type=type_hints["day"])
            check_type(argname="argument hour", value=hour, expected_type=type_hints["hour"])
            check_type(argname="argument minute", value=minute, expected_type=type_hints["minute"])
            check_type(argname="argument month", value=month, expected_type=type_hints["month"])
            check_type(argname="argument week_day", value=week_day, expected_type=type_hints["week_day"])
            check_type(argname="argument year", value=year, expected_type=type_hints["year"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if day is not None:
            self._values["day"] = day
        if hour is not None:
            self._values["hour"] = hour
        if minute is not None:
            self._values["minute"] = minute
        if month is not None:
            self._values["month"] = month
        if week_day is not None:
            self._values["week_day"] = week_day
        if year is not None:
            self._values["year"] = year

    @builtins.property
    def day(self) -> typing.Optional[builtins.str]:
        '''The day of the month to run this rule at.

        :default: - Every day of the month
        '''
        result = self._values.get("day")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def hour(self) -> typing.Optional[builtins.str]:
        '''The hour to run this rule at.

        :default: - Every hour
        '''
        result = self._values.get("hour")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def minute(self) -> typing.Optional[builtins.str]:
        '''The minute to run this rule at.

        :default: - Every minute
        '''
        result = self._values.get("minute")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def month(self) -> typing.Optional[builtins.str]:
        '''The month to run this rule at.

        :default: - Every month
        '''
        result = self._values.get("month")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def week_day(self) -> typing.Optional[builtins.str]:
        '''The day of the week to run this rule at.

        :default: - Any day of the week
        '''
        result = self._values.get("week_day")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def year(self) -> typing.Optional[builtins.str]:
        '''The year to run this rule at.

        :default: - Every year
        '''
        result = self._values.get("year")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CronOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_applicationautoscaling.EnableScalingProps",
    jsii_struct_bases=[],
    name_mapping={"max_capacity": "maxCapacity", "min_capacity": "minCapacity"},
)
class EnableScalingProps:
    def __init__(
        self,
        *,
        max_capacity: jsii.Number,
        min_capacity: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Properties for enabling Application Auto Scaling.

        :param max_capacity: Maximum capacity to scale to.
        :param min_capacity: Minimum capacity to scale to. Default: 1

        :exampleMetadata: infused

        Example::

            # cluster: ecs.Cluster
            
            load_balanced_fargate_service = ecs_patterns.ApplicationLoadBalancedFargateService(self, "Service",
                cluster=cluster,
                memory_limit_mi_b=1024,
                desired_count=1,
                cpu=512,
                task_image_options=ecsPatterns.ApplicationLoadBalancedTaskImageOptions(
                    image=ecs.ContainerImage.from_registry("amazon/amazon-ecs-sample")
                )
            )
            
            scalable_target = load_balanced_fargate_service.service.auto_scale_task_count(
                min_capacity=1,
                max_capacity=20
            )
            
            scalable_target.scale_on_cpu_utilization("CpuScaling",
                target_utilization_percent=50
            )
            
            scalable_target.scale_on_memory_utilization("MemoryScaling",
                target_utilization_percent=50
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4c0cc0d56669ed17f3d9a93a8b999330c5c8ca16d7b5113495d4c0580beb45e)
            check_type(argname="argument max_capacity", value=max_capacity, expected_type=type_hints["max_capacity"])
            check_type(argname="argument min_capacity", value=min_capacity, expected_type=type_hints["min_capacity"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "max_capacity": max_capacity,
        }
        if min_capacity is not None:
            self._values["min_capacity"] = min_capacity

    @builtins.property
    def max_capacity(self) -> jsii.Number:
        '''Maximum capacity to scale to.'''
        result = self._values.get("max_capacity")
        assert result is not None, "Required property 'max_capacity' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def min_capacity(self) -> typing.Optional[jsii.Number]:
        '''Minimum capacity to scale to.

        :default: 1
        '''
        result = self._values.get("min_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EnableScalingProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.aws_applicationautoscaling.IScalableTarget")
class IScalableTarget(_IResource_c80c4260, typing_extensions.Protocol):
    @builtins.property
    @jsii.member(jsii_name="scalableTargetId")
    def scalable_target_id(self) -> builtins.str:
        '''
        :attribute: true
        '''
        ...


class _IScalableTargetProxy(
    jsii.proxy_for(_IResource_c80c4260), # type: ignore[misc]
):
    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_applicationautoscaling.IScalableTarget"

    @builtins.property
    @jsii.member(jsii_name="scalableTargetId")
    def scalable_target_id(self) -> builtins.str:
        '''
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "scalableTargetId"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IScalableTarget).__jsii_proxy_class__ = lambda : _IScalableTargetProxy


@jsii.enum(jsii_type="aws-cdk-lib.aws_applicationautoscaling.MetricAggregationType")
class MetricAggregationType(enum.Enum):
    '''How the scaling metric is going to be aggregated.'''

    AVERAGE = "AVERAGE"
    '''Average.'''
    MINIMUM = "MINIMUM"
    '''Minimum.'''
    MAXIMUM = "MAXIMUM"
    '''Maximum.'''


@jsii.enum(jsii_type="aws-cdk-lib.aws_applicationautoscaling.PredefinedMetric")
class PredefinedMetric(enum.Enum):
    '''One of the predefined autoscaling metrics.

    :exampleMetadata: infused

    Example::

        shards_scalable_target = appscaling.ScalableTarget(self, "ElastiCacheRedisShardsScalableTarget",
            service_namespace=appscaling.ServiceNamespace.ELASTICACHE,
            scalable_dimension="elasticache:replication-group:NodeGroups",
            min_capacity=2,
            max_capacity=10,
            resource_id="replication-group/main-cluster"
        )
        
        shards_scalable_target.scale_to_track_metric("ElastiCacheRedisShardsCPUUtilization",
            target_value=20,
            predefined_metric=appscaling.PredefinedMetric.ELASTICACHE_PRIMARY_ENGINE_CPU_UTILIZATION
        )
    '''

    APPSTREAM_AVERAGE_CAPACITY_UTILIZATION = "APPSTREAM_AVERAGE_CAPACITY_UTILIZATION"
    '''Average percentage of instances in an AppStream fleet that are being used.'''
    CASSANDRA_READ_CAPACITY_UTILIZATION = "CASSANDRA_READ_CAPACITY_UTILIZATION"
    '''Percentage of provisioned read capacity units utilized by a Keyspaces table.'''
    CASSANDRA_WRITE_CAPACITY_UTILIZATION = "CASSANDRA_WRITE_CAPACITY_UTILIZATION"
    '''Percentage of provisioned write capacity units utilized by a Keyspaces table.'''
    COMPREHEND_INFERENCE_UTILIZATION = "COMPREHEND_INFERENCE_UTILIZATION"
    '''Percentage of provisioned inference units utilized by a Comprehend endpoint.'''
    NEPTURE_READER_AVERAGE_CPU_UTILIZATION = "NEPTURE_READER_AVERAGE_CPU_UTILIZATION"
    '''Average CPU Utilization of read replica instances in a Neptune DB cluster.'''
    DYNAMODB_READ_CAPACITY_UTILIZATION = "DYNAMODB_READ_CAPACITY_UTILIZATION"
    '''Percentage of provisioned read capacity units consumed by a DynamoDB table.'''
    DYNAMODB_WRITE_CAPACITY_UTILIZATION = "DYNAMODB_WRITE_CAPACITY_UTILIZATION"
    '''Percentage of provisioned write capacity units consumed by a DynamoDB table.

    Suffix ``dummy`` is necessary due to jsii bug (https://github.com/aws/jsii/issues/2782).
    Duplicate values will be dropped, so this suffix is added as a workaround.
    The value will be replaced when this enum is used.

    :see: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PredefinedMetricSpecification.html
    '''
    DYANMODB_WRITE_CAPACITY_UTILIZATION = "DYANMODB_WRITE_CAPACITY_UTILIZATION"
    '''(deprecated) DYANMODB_WRITE_CAPACITY_UTILIZATION.

    :deprecated: use ``PredefinedMetric.DYNAMODB_WRITE_CAPACITY_UTILIZATION``

    :see: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PredefinedMetricSpecification.html
    :stability: deprecated
    '''
    ALB_REQUEST_COUNT_PER_TARGET = "ALB_REQUEST_COUNT_PER_TARGET"
    '''ALB_REQUEST_COUNT_PER_TARGET.

    :see: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PredefinedMetricSpecification.html
    '''
    RDS_READER_AVERAGE_CPU_UTILIZATION = "RDS_READER_AVERAGE_CPU_UTILIZATION"
    '''RDS_READER_AVERAGE_CPU_UTILIZATION.

    :see: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PredefinedMetricSpecification.html
    '''
    RDS_READER_AVERAGE_DATABASE_CONNECTIONS = "RDS_READER_AVERAGE_DATABASE_CONNECTIONS"
    '''RDS_READER_AVERAGE_DATABASE_CONNECTIONS.

    :see: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PredefinedMetricSpecification.html
    '''
    EC2_SPOT_FLEET_REQUEST_AVERAGE_CPU_UTILIZATION = "EC2_SPOT_FLEET_REQUEST_AVERAGE_CPU_UTILIZATION"
    '''EC2_SPOT_FLEET_REQUEST_AVERAGE_CPU_UTILIZATION.

    :see: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PredefinedMetricSpecification.html
    '''
    EC2_SPOT_FLEET_REQUEST_AVERAGE_NETWORK_IN = "EC2_SPOT_FLEET_REQUEST_AVERAGE_NETWORK_IN"
    '''EC2_SPOT_FLEET_REQUEST_AVERAGE_NETWORK_IN.

    :see: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PredefinedMetricSpecification.html
    '''
    EC2_SPOT_FLEET_REQUEST_AVERAGE_NETWORK_OUT = "EC2_SPOT_FLEET_REQUEST_AVERAGE_NETWORK_OUT"
    '''EC2_SPOT_FLEET_REQUEST_AVERAGE_NETWORK_OUT.

    :see: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PredefinedMetricSpecification.html
    '''
    SAGEMAKER_VARIANT_INVOCATIONS_PER_INSTANCE = "SAGEMAKER_VARIANT_INVOCATIONS_PER_INSTANCE"
    '''SAGEMAKER_VARIANT_INVOCATIONS_PER_INSTANCE.

    :see: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PredefinedMetricSpecification.html
    '''
    SAGEMAKER_VARIANT_PROVISIONED_CONCURRENCY_UTILIZATION = "SAGEMAKER_VARIANT_PROVISIONED_CONCURRENCY_UTILIZATION"
    '''SAGEMAKER_VARIANT_PROVISIONED_CONCURRENCY_UTILIZATION.

    :see: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PredefinedMetricSpecification.html
    '''
    SAGEMAKER_INFERENCE_COMPONENT_INVOCATIONS_PER_COPY = "SAGEMAKER_INFERENCE_COMPONENT_INVOCATIONS_PER_COPY"
    '''SAGEMAKER_INFERENCE_COMPONENT_INVOCATIONS_PER_COPY.

    :see: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PredefinedMetricSpecification.html
    '''
    ECS_SERVICE_AVERAGE_CPU_UTILIZATION = "ECS_SERVICE_AVERAGE_CPU_UTILIZATION"
    '''ECS_SERVICE_AVERAGE_CPU_UTILIZATION.

    :see: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PredefinedMetricSpecification.html
    '''
    ECS_SERVICE_AVERAGE_MEMORY_UTILIZATION = "ECS_SERVICE_AVERAGE_MEMORY_UTILIZATION"
    '''ECS_SERVICE_AVERAGE_MEMORY_UTILIZATION.

    :see: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PredefinedMetricSpecification.html
    '''
    LAMBDA_PROVISIONED_CONCURRENCY_UTILIZATION = "LAMBDA_PROVISIONED_CONCURRENCY_UTILIZATION"
    '''LAMBDA_PROVISIONED_CONCURRENCY_UTILIZATION.

    :see: https://docs.aws.amazon.com/lambda/latest/dg/monitoring-metrics.html#monitoring-metrics-concurrency
    '''
    KAFKA_BROKER_STORAGE_UTILIZATION = "KAFKA_BROKER_STORAGE_UTILIZATION"
    '''KAFKA_BROKER_STORAGE_UTILIZATION.

    :see: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PredefinedMetricSpecification.html
    '''
    ELASTICACHE_PRIMARY_ENGINE_CPU_UTILIZATION = "ELASTICACHE_PRIMARY_ENGINE_CPU_UTILIZATION"
    '''ELASTICACHE_PRIMARY_ENGINE_CPU_UTILIZATION.

    :see: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PredefinedMetricSpecification.html
    '''
    ELASTICACHE_REPLICA_ENGINE_CPU_UTILIZATION = "ELASTICACHE_REPLICA_ENGINE_CPU_UTILIZATION"
    '''ELASTICACHE_REPLICA_ENGINE_CPU_UTILIZATION.

    :see: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PredefinedMetricSpecification.html
    '''
    ELASTICACHE_DATABASE_MEMORY_USAGE_COUNTED_FOR_EVICT_PERCENTAGE = "ELASTICACHE_DATABASE_MEMORY_USAGE_COUNTED_FOR_EVICT_PERCENTAGE"
    '''ELASTICACHE_DATABASE_MEMORY_USAGE_COUNTED_FOR_EVICT_PERCENTAGE.

    :see: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PredefinedMetricSpecification.html
    '''
    ELASTICACHE_DATABASE_CAPACITY_USAGE_COUNTED_FOR_EVICT_PERCENTAGE = "ELASTICACHE_DATABASE_CAPACITY_USAGE_COUNTED_FOR_EVICT_PERCENTAGE"
    '''ELASTICACHE_DATABASE_CAPACITY_USAGE_COUNTED_FOR_EVICT_PERCENTAGE.

    :see: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PredefinedMetricSpecification.html
    '''


@jsii.implements(IScalableTarget)
class ScalableTarget(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_applicationautoscaling.ScalableTarget",
):
    '''Define a scalable target.

    :exampleMetadata: infused

    Example::

        shards_scalable_target = appscaling.ScalableTarget(self, "ElastiCacheRedisShardsScalableTarget",
            service_namespace=appscaling.ServiceNamespace.ELASTICACHE,
            scalable_dimension="elasticache:replication-group:NodeGroups",
            min_capacity=2,
            max_capacity=10,
            resource_id="replication-group/main-cluster"
        )
        
        shards_scalable_target.scale_to_track_metric("ElastiCacheRedisShardsCPUUtilization",
            target_value=20,
            predefined_metric=appscaling.PredefinedMetric.ELASTICACHE_PRIMARY_ENGINE_CPU_UTILIZATION
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        max_capacity: jsii.Number,
        min_capacity: jsii.Number,
        resource_id: builtins.str,
        scalable_dimension: builtins.str,
        service_namespace: "ServiceNamespace",
        role: typing.Optional[_IRole_235f5d8e] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param max_capacity: The maximum value that Application Auto Scaling can use to scale a target during a scaling activity.
        :param min_capacity: The minimum value that Application Auto Scaling can use to scale a target during a scaling activity.
        :param resource_id: The resource identifier to associate with this scalable target. This string consists of the resource type and unique identifier. Example value: ``service/ecsStack-MyECSCluster-AB12CDE3F4GH/ecsStack-MyECSService-AB12CDE3F4GH``
        :param scalable_dimension: The scalable dimension that's associated with the scalable target. Specify the service namespace, resource type, and scaling property. Example value: ``ecs:service:DesiredCount``
        :param service_namespace: The namespace of the AWS service that provides the resource or custom-resource for a resource provided by your own application or service. For valid AWS service namespace values, see the RegisterScalableTarget action in the Application Auto Scaling API Reference.
        :param role: Role that allows Application Auto Scaling to modify your scalable target. Default: A role is automatically created
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8491b1f534a6fef90c954e5a091a74102f414f9194833de06be45e1870c155d1)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ScalableTargetProps(
            max_capacity=max_capacity,
            min_capacity=min_capacity,
            resource_id=resource_id,
            scalable_dimension=scalable_dimension,
            service_namespace=service_namespace,
            role=role,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromScalableTargetId")
    @builtins.classmethod
    def from_scalable_target_id(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        scalable_target_id: builtins.str,
    ) -> IScalableTarget:
        '''
        :param scope: -
        :param id: -
        :param scalable_target_id: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f478630191026eccd5282b715948991fc462028ebdcd6fe204c039659399c45f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument scalable_target_id", value=scalable_target_id, expected_type=type_hints["scalable_target_id"])
        return typing.cast(IScalableTarget, jsii.sinvoke(cls, "fromScalableTargetId", [scope, id, scalable_target_id]))

    @jsii.member(jsii_name="addToRolePolicy")
    def add_to_role_policy(self, statement: _PolicyStatement_0fe33853) -> None:
        '''Add a policy statement to the role's policy.

        :param statement: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53861afb9c89932c9e82e744d09e1f97e6015c7c2739481f75097c0c3e60e60e)
            check_type(argname="argument statement", value=statement, expected_type=type_hints["statement"])
        return typing.cast(None, jsii.invoke(self, "addToRolePolicy", [statement]))

    @jsii.member(jsii_name="scaleOnMetric")
    def scale_on_metric(
        self,
        id: builtins.str,
        *,
        metric: _IMetric_c7fd29de,
        scaling_steps: typing.Sequence[typing.Union["ScalingInterval", typing.Dict[builtins.str, typing.Any]]],
        adjustment_type: typing.Optional[AdjustmentType] = None,
        cooldown: typing.Optional[_Duration_4839e8c3] = None,
        datapoints_to_alarm: typing.Optional[jsii.Number] = None,
        evaluation_periods: typing.Optional[jsii.Number] = None,
        metric_aggregation_type: typing.Optional[MetricAggregationType] = None,
        min_adjustment_magnitude: typing.Optional[jsii.Number] = None,
    ) -> "StepScalingPolicy":
        '''Scale out or in, in response to a metric.

        :param id: -
        :param metric: Metric to scale on.
        :param scaling_steps: The intervals for scaling. Maps a range of metric values to a particular scaling behavior. Must be between 2 and 40 steps.
        :param adjustment_type: How the adjustment numbers inside 'intervals' are interpreted. Default: ChangeInCapacity
        :param cooldown: Grace period after scaling activity. Subsequent scale outs during the cooldown period are squashed so that only the biggest scale out happens. Subsequent scale ins during the cooldown period are ignored. Default: No cooldown period
        :param datapoints_to_alarm: The number of data points out of the evaluation periods that must be breaching to trigger a scaling action. Creates an "M out of N" alarm, where this property is the M and the value set for ``evaluationPeriods`` is the N value. Only has meaning if ``evaluationPeriods != 1``. Default: - Same as ``evaluationPeriods``
        :param evaluation_periods: How many evaluation periods of the metric to wait before triggering a scaling action. Raising this value can be used to smooth out the metric, at the expense of slower response times. If ``datapointsToAlarm`` is not set, then all data points in the evaluation period must meet the criteria to trigger a scaling action. Default: 1
        :param metric_aggregation_type: Aggregation to apply to all data points over the evaluation periods. Only has meaning if ``evaluationPeriods != 1``. Default: - The statistic from the metric if applicable (MIN, MAX, AVERAGE), otherwise AVERAGE.
        :param min_adjustment_magnitude: Minimum absolute number to adjust capacity with as result of percentage scaling. Only when using AdjustmentType = PercentChangeInCapacity, this number controls the minimum absolute effect size. Default: No minimum scaling effect
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43ded9798fe3fbe40d7c97e40d4e8364a71e47cda844521e2013ac9a7c39a26a)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = BasicStepScalingPolicyProps(
            metric=metric,
            scaling_steps=scaling_steps,
            adjustment_type=adjustment_type,
            cooldown=cooldown,
            datapoints_to_alarm=datapoints_to_alarm,
            evaluation_periods=evaluation_periods,
            metric_aggregation_type=metric_aggregation_type,
            min_adjustment_magnitude=min_adjustment_magnitude,
        )

        return typing.cast("StepScalingPolicy", jsii.invoke(self, "scaleOnMetric", [id, props]))

    @jsii.member(jsii_name="scaleOnSchedule")
    def scale_on_schedule(
        self,
        id: builtins.str,
        *,
        schedule: "Schedule",
        end_time: typing.Optional[datetime.datetime] = None,
        max_capacity: typing.Optional[jsii.Number] = None,
        min_capacity: typing.Optional[jsii.Number] = None,
        start_time: typing.Optional[datetime.datetime] = None,
        time_zone: typing.Optional[_TimeZone_cdd72ac9] = None,
    ) -> None:
        '''Scale out or in based on time.

        :param id: -
        :param schedule: When to perform this action.
        :param end_time: When this scheduled action expires. Default: The rule never expires.
        :param max_capacity: The new maximum capacity. During the scheduled time, the current capacity is above the maximum capacity, Application Auto Scaling scales in to the maximum capacity. At least one of maxCapacity and minCapacity must be supplied. Default: No new maximum capacity
        :param min_capacity: The new minimum capacity. During the scheduled time, if the current capacity is below the minimum capacity, Application Auto Scaling scales out to the minimum capacity. At least one of maxCapacity and minCapacity must be supplied. Default: No new minimum capacity
        :param start_time: When this scheduled action becomes active. Default: The rule is activate immediately
        :param time_zone: The time zone used when referring to the date and time of a scheduled action, when the scheduled action uses an at or cron expression. Default: - UTC
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00b07b46a599f1f6e690aeeada38ac26bba7017192a30ed324e7c437647bb46b)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        action = ScalingSchedule(
            schedule=schedule,
            end_time=end_time,
            max_capacity=max_capacity,
            min_capacity=min_capacity,
            start_time=start_time,
            time_zone=time_zone,
        )

        return typing.cast(None, jsii.invoke(self, "scaleOnSchedule", [id, action]))

    @jsii.member(jsii_name="scaleToTrackMetric")
    def scale_to_track_metric(
        self,
        id: builtins.str,
        *,
        target_value: jsii.Number,
        custom_metric: typing.Optional[_IMetric_c7fd29de] = None,
        predefined_metric: typing.Optional[PredefinedMetric] = None,
        resource_label: typing.Optional[builtins.str] = None,
        disable_scale_in: typing.Optional[builtins.bool] = None,
        policy_name: typing.Optional[builtins.str] = None,
        scale_in_cooldown: typing.Optional[_Duration_4839e8c3] = None,
        scale_out_cooldown: typing.Optional[_Duration_4839e8c3] = None,
    ) -> "TargetTrackingScalingPolicy":
        '''Scale out or in in order to keep a metric around a target value.

        :param id: -
        :param target_value: The target value for the metric.
        :param custom_metric: A custom metric for application autoscaling. The metric must track utilization. Scaling out will happen if the metric is higher than the target value, scaling in will happen in the metric is lower than the target value. Exactly one of customMetric or predefinedMetric must be specified. Default: - No custom metric.
        :param predefined_metric: A predefined metric for application autoscaling. The metric must track utilization. Scaling out will happen if the metric is higher than the target value, scaling in will happen in the metric is lower than the target value. Exactly one of customMetric or predefinedMetric must be specified. Default: - No predefined metrics.
        :param resource_label: Identify the resource associated with the metric type. Only used for predefined metric ALBRequestCountPerTarget. Example value: ``app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>`` Default: - No resource label.
        :param disable_scale_in: Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won't remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the scalable resource. Default: false
        :param policy_name: A name for the scaling policy. Default: - Automatically generated name.
        :param scale_in_cooldown: Period after a scale in activity completes before another scale in activity can start. Default: Duration.seconds(300) for the following scalable targets: ECS services, Spot Fleet requests, EMR clusters, AppStream 2.0 fleets, Aurora DB clusters, Amazon SageMaker endpoint variants, Custom resources. For all other scalable targets, the default value is Duration.seconds(0): DynamoDB tables, DynamoDB global secondary indexes, Amazon Comprehend document classification endpoints, Lambda provisioned concurrency
        :param scale_out_cooldown: Period after a scale out activity completes before another scale out activity can start. Default: Duration.seconds(300) for the following scalable targets: ECS services, Spot Fleet requests, EMR clusters, AppStream 2.0 fleets, Aurora DB clusters, Amazon SageMaker endpoint variants, Custom resources. For all other scalable targets, the default value is Duration.seconds(0): DynamoDB tables, DynamoDB global secondary indexes, Amazon Comprehend document classification endpoints, Lambda provisioned concurrency
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05dc12c8c78cbf6f9c0c66c5c142f63e0590f2157107bdf2505a0852a4f4a4b2)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = BasicTargetTrackingScalingPolicyProps(
            target_value=target_value,
            custom_metric=custom_metric,
            predefined_metric=predefined_metric,
            resource_label=resource_label,
            disable_scale_in=disable_scale_in,
            policy_name=policy_name,
            scale_in_cooldown=scale_in_cooldown,
            scale_out_cooldown=scale_out_cooldown,
        )

        return typing.cast("TargetTrackingScalingPolicy", jsii.invoke(self, "scaleToTrackMetric", [id, props]))

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> _IRole_235f5d8e:
        '''The role used to give AutoScaling permissions to your resource.'''
        return typing.cast(_IRole_235f5d8e, jsii.get(self, "role"))

    @builtins.property
    @jsii.member(jsii_name="scalableTargetId")
    def scalable_target_id(self) -> builtins.str:
        '''ID of the Scalable Target.

        Example value: ``service/ecsStack-MyECSCluster-AB12CDE3F4GH/ecsStack-MyECSService-AB12CDE3F4GH|ecs:service:DesiredCount|ecs``

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "scalableTargetId"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_applicationautoscaling.ScalableTargetProps",
    jsii_struct_bases=[],
    name_mapping={
        "max_capacity": "maxCapacity",
        "min_capacity": "minCapacity",
        "resource_id": "resourceId",
        "scalable_dimension": "scalableDimension",
        "service_namespace": "serviceNamespace",
        "role": "role",
    },
)
class ScalableTargetProps:
    def __init__(
        self,
        *,
        max_capacity: jsii.Number,
        min_capacity: jsii.Number,
        resource_id: builtins.str,
        scalable_dimension: builtins.str,
        service_namespace: "ServiceNamespace",
        role: typing.Optional[_IRole_235f5d8e] = None,
    ) -> None:
        '''Properties for a scalable target.

        :param max_capacity: The maximum value that Application Auto Scaling can use to scale a target during a scaling activity.
        :param min_capacity: The minimum value that Application Auto Scaling can use to scale a target during a scaling activity.
        :param resource_id: The resource identifier to associate with this scalable target. This string consists of the resource type and unique identifier. Example value: ``service/ecsStack-MyECSCluster-AB12CDE3F4GH/ecsStack-MyECSService-AB12CDE3F4GH``
        :param scalable_dimension: The scalable dimension that's associated with the scalable target. Specify the service namespace, resource type, and scaling property. Example value: ``ecs:service:DesiredCount``
        :param service_namespace: The namespace of the AWS service that provides the resource or custom-resource for a resource provided by your own application or service. For valid AWS service namespace values, see the RegisterScalableTarget action in the Application Auto Scaling API Reference.
        :param role: Role that allows Application Auto Scaling to modify your scalable target. Default: A role is automatically created

        :exampleMetadata: infused

        Example::

            shards_scalable_target = appscaling.ScalableTarget(self, "ElastiCacheRedisShardsScalableTarget",
                service_namespace=appscaling.ServiceNamespace.ELASTICACHE,
                scalable_dimension="elasticache:replication-group:NodeGroups",
                min_capacity=2,
                max_capacity=10,
                resource_id="replication-group/main-cluster"
            )
            
            shards_scalable_target.scale_to_track_metric("ElastiCacheRedisShardsCPUUtilization",
                target_value=20,
                predefined_metric=appscaling.PredefinedMetric.ELASTICACHE_PRIMARY_ENGINE_CPU_UTILIZATION
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad90959b199a68084c2e639ade21bf66df6004347d16c00dd766d667b4e2a529)
            check_type(argname="argument max_capacity", value=max_capacity, expected_type=type_hints["max_capacity"])
            check_type(argname="argument min_capacity", value=min_capacity, expected_type=type_hints["min_capacity"])
            check_type(argname="argument resource_id", value=resource_id, expected_type=type_hints["resource_id"])
            check_type(argname="argument scalable_dimension", value=scalable_dimension, expected_type=type_hints["scalable_dimension"])
            check_type(argname="argument service_namespace", value=service_namespace, expected_type=type_hints["service_namespace"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "max_capacity": max_capacity,
            "min_capacity": min_capacity,
            "resource_id": resource_id,
            "scalable_dimension": scalable_dimension,
            "service_namespace": service_namespace,
        }
        if role is not None:
            self._values["role"] = role

    @builtins.property
    def max_capacity(self) -> jsii.Number:
        '''The maximum value that Application Auto Scaling can use to scale a target during a scaling activity.'''
        result = self._values.get("max_capacity")
        assert result is not None, "Required property 'max_capacity' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def min_capacity(self) -> jsii.Number:
        '''The minimum value that Application Auto Scaling can use to scale a target during a scaling activity.'''
        result = self._values.get("min_capacity")
        assert result is not None, "Required property 'min_capacity' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def resource_id(self) -> builtins.str:
        '''The resource identifier to associate with this scalable target.

        This string consists of the resource type and unique identifier.

        Example value: ``service/ecsStack-MyECSCluster-AB12CDE3F4GH/ecsStack-MyECSService-AB12CDE3F4GH``

        :see: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_RegisterScalableTarget.html
        '''
        result = self._values.get("resource_id")
        assert result is not None, "Required property 'resource_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def scalable_dimension(self) -> builtins.str:
        '''The scalable dimension that's associated with the scalable target.

        Specify the service namespace, resource type, and scaling property.

        Example value: ``ecs:service:DesiredCount``

        :see: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_ScalingPolicy.html
        '''
        result = self._values.get("scalable_dimension")
        assert result is not None, "Required property 'scalable_dimension' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_namespace(self) -> "ServiceNamespace":
        '''The namespace of the AWS service that provides the resource or custom-resource for a resource provided by your own application or service.

        For valid AWS service namespace values, see the RegisterScalableTarget
        action in the Application Auto Scaling API Reference.

        :see: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_RegisterScalableTarget.html
        '''
        result = self._values.get("service_namespace")
        assert result is not None, "Required property 'service_namespace' is missing"
        return typing.cast("ServiceNamespace", result)

    @builtins.property
    def role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''Role that allows Application Auto Scaling to modify your scalable target.

        :default: A role is automatically created
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ScalableTargetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_applicationautoscaling.ScalingInterval",
    jsii_struct_bases=[],
    name_mapping={"change": "change", "lower": "lower", "upper": "upper"},
)
class ScalingInterval:
    def __init__(
        self,
        *,
        change: jsii.Number,
        lower: typing.Optional[jsii.Number] = None,
        upper: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''A range of metric values in which to apply a certain scaling operation.

        :param change: The capacity adjustment to apply in this interval. The number is interpreted differently based on AdjustmentType: - ChangeInCapacity: add the adjustment to the current capacity. The number can be positive or negative. - PercentChangeInCapacity: add or remove the given percentage of the current capacity to itself. The number can be in the range [-100..100]. - ExactCapacity: set the capacity to this number. The number must be positive.
        :param lower: The lower bound of the interval. The scaling adjustment will be applied if the metric is higher than this value. Default: Threshold automatically derived from neighbouring intervals
        :param upper: The upper bound of the interval. The scaling adjustment will be applied if the metric is lower than this value. Default: Threshold automatically derived from neighbouring intervals

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_applicationautoscaling as appscaling
            
            scaling_interval = appscaling.ScalingInterval(
                change=123,
            
                # the properties below are optional
                lower=123,
                upper=123
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6f6165efad90911203a00e6a29dd5b27c5e8a4d5bca2d5e0edab9a421d7368d)
            check_type(argname="argument change", value=change, expected_type=type_hints["change"])
            check_type(argname="argument lower", value=lower, expected_type=type_hints["lower"])
            check_type(argname="argument upper", value=upper, expected_type=type_hints["upper"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "change": change,
        }
        if lower is not None:
            self._values["lower"] = lower
        if upper is not None:
            self._values["upper"] = upper

    @builtins.property
    def change(self) -> jsii.Number:
        '''The capacity adjustment to apply in this interval.

        The number is interpreted differently based on AdjustmentType:

        - ChangeInCapacity: add the adjustment to the current capacity.
          The number can be positive or negative.
        - PercentChangeInCapacity: add or remove the given percentage of the current
          capacity to itself. The number can be in the range [-100..100].
        - ExactCapacity: set the capacity to this number. The number must
          be positive.
        '''
        result = self._values.get("change")
        assert result is not None, "Required property 'change' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def lower(self) -> typing.Optional[jsii.Number]:
        '''The lower bound of the interval.

        The scaling adjustment will be applied if the metric is higher than this value.

        :default: Threshold automatically derived from neighbouring intervals
        '''
        result = self._values.get("lower")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def upper(self) -> typing.Optional[jsii.Number]:
        '''The upper bound of the interval.

        The scaling adjustment will be applied if the metric is lower than this value.

        :default: Threshold automatically derived from neighbouring intervals
        '''
        result = self._values.get("upper")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ScalingInterval(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_applicationautoscaling.ScalingSchedule",
    jsii_struct_bases=[],
    name_mapping={
        "schedule": "schedule",
        "end_time": "endTime",
        "max_capacity": "maxCapacity",
        "min_capacity": "minCapacity",
        "start_time": "startTime",
        "time_zone": "timeZone",
    },
)
class ScalingSchedule:
    def __init__(
        self,
        *,
        schedule: "Schedule",
        end_time: typing.Optional[datetime.datetime] = None,
        max_capacity: typing.Optional[jsii.Number] = None,
        min_capacity: typing.Optional[jsii.Number] = None,
        start_time: typing.Optional[datetime.datetime] = None,
        time_zone: typing.Optional[_TimeZone_cdd72ac9] = None,
    ) -> None:
        '''A scheduled scaling action.

        :param schedule: When to perform this action.
        :param end_time: When this scheduled action expires. Default: The rule never expires.
        :param max_capacity: The new maximum capacity. During the scheduled time, the current capacity is above the maximum capacity, Application Auto Scaling scales in to the maximum capacity. At least one of maxCapacity and minCapacity must be supplied. Default: No new maximum capacity
        :param min_capacity: The new minimum capacity. During the scheduled time, if the current capacity is below the minimum capacity, Application Auto Scaling scales out to the minimum capacity. At least one of maxCapacity and minCapacity must be supplied. Default: No new minimum capacity
        :param start_time: When this scheduled action becomes active. Default: The rule is activate immediately
        :param time_zone: The time zone used when referring to the date and time of a scheduled action, when the scheduled action uses an at or cron expression. Default: - UTC

        :exampleMetadata: infused

        Example::

            # cluster: ecs.Cluster
            
            load_balanced_fargate_service = ecs_patterns.ApplicationLoadBalancedFargateService(self, "Service",
                cluster=cluster,
                memory_limit_mi_b=1024,
                desired_count=1,
                cpu=512,
                task_image_options=ecsPatterns.ApplicationLoadBalancedTaskImageOptions(
                    image=ecs.ContainerImage.from_registry("amazon/amazon-ecs-sample")
                )
            )
            
            scalable_target = load_balanced_fargate_service.service.auto_scale_task_count(
                min_capacity=5,
                max_capacity=20
            )
            
            scalable_target.scale_on_schedule("DaytimeScaleDown",
                schedule=appscaling.Schedule.cron(hour="8", minute="0"),
                min_capacity=1
            )
            
            scalable_target.scale_on_schedule("EveningRushScaleUp",
                schedule=appscaling.Schedule.cron(hour="20", minute="0"),
                min_capacity=10
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57aef750eb5141016e0f252e7b49eacfa61419872935a6645e358d0c9484bb06)
            check_type(argname="argument schedule", value=schedule, expected_type=type_hints["schedule"])
            check_type(argname="argument end_time", value=end_time, expected_type=type_hints["end_time"])
            check_type(argname="argument max_capacity", value=max_capacity, expected_type=type_hints["max_capacity"])
            check_type(argname="argument min_capacity", value=min_capacity, expected_type=type_hints["min_capacity"])
            check_type(argname="argument start_time", value=start_time, expected_type=type_hints["start_time"])
            check_type(argname="argument time_zone", value=time_zone, expected_type=type_hints["time_zone"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "schedule": schedule,
        }
        if end_time is not None:
            self._values["end_time"] = end_time
        if max_capacity is not None:
            self._values["max_capacity"] = max_capacity
        if min_capacity is not None:
            self._values["min_capacity"] = min_capacity
        if start_time is not None:
            self._values["start_time"] = start_time
        if time_zone is not None:
            self._values["time_zone"] = time_zone

    @builtins.property
    def schedule(self) -> "Schedule":
        '''When to perform this action.'''
        result = self._values.get("schedule")
        assert result is not None, "Required property 'schedule' is missing"
        return typing.cast("Schedule", result)

    @builtins.property
    def end_time(self) -> typing.Optional[datetime.datetime]:
        '''When this scheduled action expires.

        :default: The rule never expires.
        '''
        result = self._values.get("end_time")
        return typing.cast(typing.Optional[datetime.datetime], result)

    @builtins.property
    def max_capacity(self) -> typing.Optional[jsii.Number]:
        '''The new maximum capacity.

        During the scheduled time, the current capacity is above the maximum
        capacity, Application Auto Scaling scales in to the maximum capacity.

        At least one of maxCapacity and minCapacity must be supplied.

        :default: No new maximum capacity
        '''
        result = self._values.get("max_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_capacity(self) -> typing.Optional[jsii.Number]:
        '''The new minimum capacity.

        During the scheduled time, if the current capacity is below the minimum
        capacity, Application Auto Scaling scales out to the minimum capacity.

        At least one of maxCapacity and minCapacity must be supplied.

        :default: No new minimum capacity
        '''
        result = self._values.get("min_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def start_time(self) -> typing.Optional[datetime.datetime]:
        '''When this scheduled action becomes active.

        :default: The rule is activate immediately
        '''
        result = self._values.get("start_time")
        return typing.cast(typing.Optional[datetime.datetime], result)

    @builtins.property
    def time_zone(self) -> typing.Optional[_TimeZone_cdd72ac9]:
        '''The time zone used when referring to the date and time of a scheduled action, when the scheduled action uses an at or cron expression.

        :default: - UTC
        '''
        result = self._values.get("time_zone")
        return typing.cast(typing.Optional[_TimeZone_cdd72ac9], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ScalingSchedule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Schedule(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="aws-cdk-lib.aws_applicationautoscaling.Schedule",
):
    '''Schedule for scheduled scaling actions.

    :exampleMetadata: infused

    Example::

        from aws_cdk import TimeZone
        # resource: SomeScalableResource
        
        
        capacity = resource.auto_scale_capacity(
            min_capacity=1,
            max_capacity=50
        )
        
        capacity.scale_on_schedule("PrescaleInTheMorning",
            schedule=appscaling.Schedule.cron(hour="8", minute="0"),
            min_capacity=20,
            time_zone=TimeZone.AMERICA_DENVER
        )
        
        capacity.scale_on_schedule("AllowDownscalingAtNight",
            schedule=appscaling.Schedule.cron(hour="20", minute="0"),
            min_capacity=1,
            time_zone=TimeZone.AMERICA_DENVER
        )
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="at")
    @builtins.classmethod
    def at(cls, moment: datetime.datetime) -> "Schedule":
        '''Construct a Schedule from a moment in time.

        :param moment: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b6d7fda9383aedbe53cc8d8ade34a64e19233e11096bdf1844196644aa79458)
            check_type(argname="argument moment", value=moment, expected_type=type_hints["moment"])
        return typing.cast("Schedule", jsii.sinvoke(cls, "at", [moment]))

    @jsii.member(jsii_name="cron")
    @builtins.classmethod
    def cron(
        cls,
        *,
        day: typing.Optional[builtins.str] = None,
        hour: typing.Optional[builtins.str] = None,
        minute: typing.Optional[builtins.str] = None,
        month: typing.Optional[builtins.str] = None,
        week_day: typing.Optional[builtins.str] = None,
        year: typing.Optional[builtins.str] = None,
    ) -> "Schedule":
        '''Create a schedule from a set of cron fields.

        :param day: The day of the month to run this rule at. Default: - Every day of the month
        :param hour: The hour to run this rule at. Default: - Every hour
        :param minute: The minute to run this rule at. Default: - Every minute
        :param month: The month to run this rule at. Default: - Every month
        :param week_day: The day of the week to run this rule at. Default: - Any day of the week
        :param year: The year to run this rule at. Default: - Every year
        '''
        options = CronOptions(
            day=day,
            hour=hour,
            minute=minute,
            month=month,
            week_day=week_day,
            year=year,
        )

        return typing.cast("Schedule", jsii.sinvoke(cls, "cron", [options]))

    @jsii.member(jsii_name="expression")
    @builtins.classmethod
    def expression(cls, expression: builtins.str) -> "Schedule":
        '''Construct a schedule from a literal schedule expression.

        :param expression: The expression to use. Must be in a format that Application AutoScaling will recognize
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e25a6639f36857385bcf857e79dd3e959c720c58729794a75fde1193754cc9d)
            check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
        return typing.cast("Schedule", jsii.sinvoke(cls, "expression", [expression]))

    @jsii.member(jsii_name="rate")
    @builtins.classmethod
    def rate(cls, duration: _Duration_4839e8c3) -> "Schedule":
        '''Construct a schedule from an interval and a time unit.

        :param duration: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80021ca00d4dfc7e5d3749ddcb1a82c455470cb51699456caee089bcc2970257)
            check_type(argname="argument duration", value=duration, expected_type=type_hints["duration"])
        return typing.cast("Schedule", jsii.sinvoke(cls, "rate", [duration]))

    @builtins.property
    @jsii.member(jsii_name="expressionString")
    @abc.abstractmethod
    def expression_string(self) -> builtins.str:
        '''Retrieve the expression for this schedule.'''
        ...


class _ScheduleProxy(Schedule):
    @builtins.property
    @jsii.member(jsii_name="expressionString")
    def expression_string(self) -> builtins.str:
        '''Retrieve the expression for this schedule.'''
        return typing.cast(builtins.str, jsii.get(self, "expressionString"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, Schedule).__jsii_proxy_class__ = lambda : _ScheduleProxy


@jsii.enum(jsii_type="aws-cdk-lib.aws_applicationautoscaling.ServiceNamespace")
class ServiceNamespace(enum.Enum):
    '''The service that supports Application AutoScaling.

    :exampleMetadata: infused

    Example::

        shards_scalable_target = appscaling.ScalableTarget(self, "ElastiCacheRedisShardsScalableTarget",
            service_namespace=appscaling.ServiceNamespace.ELASTICACHE,
            scalable_dimension="elasticache:replication-group:NodeGroups",
            min_capacity=2,
            max_capacity=10,
            resource_id="replication-group/main-cluster"
        )
        
        shards_scalable_target.scale_to_track_metric("ElastiCacheRedisShardsCPUUtilization",
            target_value=20,
            predefined_metric=appscaling.PredefinedMetric.ELASTICACHE_PRIMARY_ENGINE_CPU_UTILIZATION
        )
    '''

    ECS = "ECS"
    '''Elastic Container Service.'''
    ELASTIC_MAP_REDUCE = "ELASTIC_MAP_REDUCE"
    '''Elastic Map Reduce.'''
    EC2 = "EC2"
    '''Elastic Compute Cloud.'''
    APPSTREAM = "APPSTREAM"
    '''App Stream.'''
    DYNAMODB = "DYNAMODB"
    '''Dynamo DB.'''
    RDS = "RDS"
    '''Relational Database Service.'''
    SAGEMAKER = "SAGEMAKER"
    '''SageMaker.'''
    CUSTOM_RESOURCE = "CUSTOM_RESOURCE"
    '''Custom Resource.'''
    LAMBDA = "LAMBDA"
    '''Lambda.'''
    COMPREHEND = "COMPREHEND"
    '''Comprehend.'''
    KAFKA = "KAFKA"
    '''Kafka.'''
    ELASTICACHE = "ELASTICACHE"
    '''ElastiCache.'''
    NEPTUNE = "NEPTUNE"
    '''Neptune.'''


class StepScalingAction(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_applicationautoscaling.StepScalingAction",
):
    '''Define a step scaling action.

    This kind of scaling policy adjusts the target capacity in configurable
    steps. The size of the step is configurable based on the metric's distance
    to its alarm threshold.

    This Action must be used as the target of a CloudWatch alarm to take effect.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk as cdk
        from aws_cdk import aws_applicationautoscaling as appscaling
        
        # scalable_target: appscaling.ScalableTarget
        
        step_scaling_action = appscaling.StepScalingAction(self, "MyStepScalingAction",
            scaling_target=scalable_target,
        
            # the properties below are optional
            adjustment_type=appscaling.AdjustmentType.CHANGE_IN_CAPACITY,
            cooldown=cdk.Duration.minutes(30),
            metric_aggregation_type=appscaling.MetricAggregationType.AVERAGE,
            min_adjustment_magnitude=123,
            policy_name="policyName"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        scaling_target: IScalableTarget,
        adjustment_type: typing.Optional[AdjustmentType] = None,
        cooldown: typing.Optional[_Duration_4839e8c3] = None,
        metric_aggregation_type: typing.Optional[MetricAggregationType] = None,
        min_adjustment_magnitude: typing.Optional[jsii.Number] = None,
        policy_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param scaling_target: The scalable target.
        :param adjustment_type: How the adjustment numbers are interpreted. Default: ChangeInCapacity
        :param cooldown: Grace period after scaling activity. For scale out policies, multiple scale outs during the cooldown period are squashed so that only the biggest scale out happens. For scale in policies, subsequent scale ins during the cooldown period are ignored. Default: No cooldown period
        :param metric_aggregation_type: The aggregation type for the CloudWatch metrics. Default: Average
        :param min_adjustment_magnitude: Minimum absolute number to adjust capacity with as result of percentage scaling. Only when using AdjustmentType = PercentChangeInCapacity, this number controls the minimum absolute effect size. Default: No minimum scaling effect
        :param policy_name: A name for the scaling policy. Default: Automatically generated name
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ebea522c756d3475869e6f400a5bb4b68ea539cce554df0d9e91d7341299f80)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = StepScalingActionProps(
            scaling_target=scaling_target,
            adjustment_type=adjustment_type,
            cooldown=cooldown,
            metric_aggregation_type=metric_aggregation_type,
            min_adjustment_magnitude=min_adjustment_magnitude,
            policy_name=policy_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="addAdjustment")
    def add_adjustment(
        self,
        *,
        adjustment: jsii.Number,
        lower_bound: typing.Optional[jsii.Number] = None,
        upper_bound: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Add an adjusment interval to the ScalingAction.

        :param adjustment: What number to adjust the capacity with. The number is interpeted as an added capacity, a new fixed capacity or an added percentage depending on the AdjustmentType value of the StepScalingPolicy. Can be positive or negative.
        :param lower_bound: Lower bound where this scaling tier applies. The scaling tier applies if the difference between the metric value and its alarm threshold is higher than this value. Default: -Infinity if this is the first tier, otherwise the upperBound of the previous tier
        :param upper_bound: Upper bound where this scaling tier applies. The scaling tier applies if the difference between the metric value and its alarm threshold is lower than this value. Default: +Infinity
        '''
        adjustment_ = AdjustmentTier(
            adjustment=adjustment, lower_bound=lower_bound, upper_bound=upper_bound
        )

        return typing.cast(None, jsii.invoke(self, "addAdjustment", [adjustment_]))

    @builtins.property
    @jsii.member(jsii_name="scalingPolicyArn")
    def scaling_policy_arn(self) -> builtins.str:
        '''ARN of the scaling policy.'''
        return typing.cast(builtins.str, jsii.get(self, "scalingPolicyArn"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_applicationautoscaling.StepScalingActionProps",
    jsii_struct_bases=[],
    name_mapping={
        "scaling_target": "scalingTarget",
        "adjustment_type": "adjustmentType",
        "cooldown": "cooldown",
        "metric_aggregation_type": "metricAggregationType",
        "min_adjustment_magnitude": "minAdjustmentMagnitude",
        "policy_name": "policyName",
    },
)
class StepScalingActionProps:
    def __init__(
        self,
        *,
        scaling_target: IScalableTarget,
        adjustment_type: typing.Optional[AdjustmentType] = None,
        cooldown: typing.Optional[_Duration_4839e8c3] = None,
        metric_aggregation_type: typing.Optional[MetricAggregationType] = None,
        min_adjustment_magnitude: typing.Optional[jsii.Number] = None,
        policy_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for a scaling policy.

        :param scaling_target: The scalable target.
        :param adjustment_type: How the adjustment numbers are interpreted. Default: ChangeInCapacity
        :param cooldown: Grace period after scaling activity. For scale out policies, multiple scale outs during the cooldown period are squashed so that only the biggest scale out happens. For scale in policies, subsequent scale ins during the cooldown period are ignored. Default: No cooldown period
        :param metric_aggregation_type: The aggregation type for the CloudWatch metrics. Default: Average
        :param min_adjustment_magnitude: Minimum absolute number to adjust capacity with as result of percentage scaling. Only when using AdjustmentType = PercentChangeInCapacity, this number controls the minimum absolute effect size. Default: No minimum scaling effect
        :param policy_name: A name for the scaling policy. Default: Automatically generated name

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk as cdk
            from aws_cdk import aws_applicationautoscaling as appscaling
            
            # scalable_target: appscaling.ScalableTarget
            
            step_scaling_action_props = appscaling.StepScalingActionProps(
                scaling_target=scalable_target,
            
                # the properties below are optional
                adjustment_type=appscaling.AdjustmentType.CHANGE_IN_CAPACITY,
                cooldown=cdk.Duration.minutes(30),
                metric_aggregation_type=appscaling.MetricAggregationType.AVERAGE,
                min_adjustment_magnitude=123,
                policy_name="policyName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__749520e5db8349113a00c486486d4029b1458a70e0520261f218726bd60fcb37)
            check_type(argname="argument scaling_target", value=scaling_target, expected_type=type_hints["scaling_target"])
            check_type(argname="argument adjustment_type", value=adjustment_type, expected_type=type_hints["adjustment_type"])
            check_type(argname="argument cooldown", value=cooldown, expected_type=type_hints["cooldown"])
            check_type(argname="argument metric_aggregation_type", value=metric_aggregation_type, expected_type=type_hints["metric_aggregation_type"])
            check_type(argname="argument min_adjustment_magnitude", value=min_adjustment_magnitude, expected_type=type_hints["min_adjustment_magnitude"])
            check_type(argname="argument policy_name", value=policy_name, expected_type=type_hints["policy_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "scaling_target": scaling_target,
        }
        if adjustment_type is not None:
            self._values["adjustment_type"] = adjustment_type
        if cooldown is not None:
            self._values["cooldown"] = cooldown
        if metric_aggregation_type is not None:
            self._values["metric_aggregation_type"] = metric_aggregation_type
        if min_adjustment_magnitude is not None:
            self._values["min_adjustment_magnitude"] = min_adjustment_magnitude
        if policy_name is not None:
            self._values["policy_name"] = policy_name

    @builtins.property
    def scaling_target(self) -> IScalableTarget:
        '''The scalable target.'''
        result = self._values.get("scaling_target")
        assert result is not None, "Required property 'scaling_target' is missing"
        return typing.cast(IScalableTarget, result)

    @builtins.property
    def adjustment_type(self) -> typing.Optional[AdjustmentType]:
        '''How the adjustment numbers are interpreted.

        :default: ChangeInCapacity
        '''
        result = self._values.get("adjustment_type")
        return typing.cast(typing.Optional[AdjustmentType], result)

    @builtins.property
    def cooldown(self) -> typing.Optional[_Duration_4839e8c3]:
        '''Grace period after scaling activity.

        For scale out policies, multiple scale outs during the cooldown period are
        squashed so that only the biggest scale out happens.

        For scale in policies, subsequent scale ins during the cooldown period are
        ignored.

        :default: No cooldown period

        :see: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_StepScalingPolicyConfiguration.html
        '''
        result = self._values.get("cooldown")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def metric_aggregation_type(self) -> typing.Optional[MetricAggregationType]:
        '''The aggregation type for the CloudWatch metrics.

        :default: Average
        '''
        result = self._values.get("metric_aggregation_type")
        return typing.cast(typing.Optional[MetricAggregationType], result)

    @builtins.property
    def min_adjustment_magnitude(self) -> typing.Optional[jsii.Number]:
        '''Minimum absolute number to adjust capacity with as result of percentage scaling.

        Only when using AdjustmentType = PercentChangeInCapacity, this number controls
        the minimum absolute effect size.

        :default: No minimum scaling effect
        '''
        result = self._values.get("min_adjustment_magnitude")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def policy_name(self) -> typing.Optional[builtins.str]:
        '''A name for the scaling policy.

        :default: Automatically generated name
        '''
        result = self._values.get("policy_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StepScalingActionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StepScalingPolicy(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_applicationautoscaling.StepScalingPolicy",
):
    '''Define a scaling strategy which scales depending on absolute values of some metric.

    You can specify the scaling behavior for various values of the metric.

    Implemented using one or more CloudWatch alarms and Step Scaling Policies.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk as cdk
        from aws_cdk import aws_applicationautoscaling as appscaling
        from aws_cdk import aws_cloudwatch as cloudwatch
        
        # metric: cloudwatch.Metric
        # scalable_target: appscaling.ScalableTarget
        
        step_scaling_policy = appscaling.StepScalingPolicy(self, "MyStepScalingPolicy",
            metric=metric,
            scaling_steps=[appscaling.ScalingInterval(
                change=123,
        
                # the properties below are optional
                lower=123,
                upper=123
            )],
            scaling_target=scalable_target,
        
            # the properties below are optional
            adjustment_type=appscaling.AdjustmentType.CHANGE_IN_CAPACITY,
            cooldown=cdk.Duration.minutes(30),
            datapoints_to_alarm=123,
            evaluation_periods=123,
            metric_aggregation_type=appscaling.MetricAggregationType.AVERAGE,
            min_adjustment_magnitude=123
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        scaling_target: IScalableTarget,
        metric: _IMetric_c7fd29de,
        scaling_steps: typing.Sequence[typing.Union[ScalingInterval, typing.Dict[builtins.str, typing.Any]]],
        adjustment_type: typing.Optional[AdjustmentType] = None,
        cooldown: typing.Optional[_Duration_4839e8c3] = None,
        datapoints_to_alarm: typing.Optional[jsii.Number] = None,
        evaluation_periods: typing.Optional[jsii.Number] = None,
        metric_aggregation_type: typing.Optional[MetricAggregationType] = None,
        min_adjustment_magnitude: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param scaling_target: The scaling target.
        :param metric: Metric to scale on.
        :param scaling_steps: The intervals for scaling. Maps a range of metric values to a particular scaling behavior. Must be between 2 and 40 steps.
        :param adjustment_type: How the adjustment numbers inside 'intervals' are interpreted. Default: ChangeInCapacity
        :param cooldown: Grace period after scaling activity. Subsequent scale outs during the cooldown period are squashed so that only the biggest scale out happens. Subsequent scale ins during the cooldown period are ignored. Default: No cooldown period
        :param datapoints_to_alarm: The number of data points out of the evaluation periods that must be breaching to trigger a scaling action. Creates an "M out of N" alarm, where this property is the M and the value set for ``evaluationPeriods`` is the N value. Only has meaning if ``evaluationPeriods != 1``. Default: - Same as ``evaluationPeriods``
        :param evaluation_periods: How many evaluation periods of the metric to wait before triggering a scaling action. Raising this value can be used to smooth out the metric, at the expense of slower response times. If ``datapointsToAlarm`` is not set, then all data points in the evaluation period must meet the criteria to trigger a scaling action. Default: 1
        :param metric_aggregation_type: Aggregation to apply to all data points over the evaluation periods. Only has meaning if ``evaluationPeriods != 1``. Default: - The statistic from the metric if applicable (MIN, MAX, AVERAGE), otherwise AVERAGE.
        :param min_adjustment_magnitude: Minimum absolute number to adjust capacity with as result of percentage scaling. Only when using AdjustmentType = PercentChangeInCapacity, this number controls the minimum absolute effect size. Default: No minimum scaling effect
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05f13291938a9d6d13d60ff41322988d2435145fc2b8137754016700734b81b7)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = StepScalingPolicyProps(
            scaling_target=scaling_target,
            metric=metric,
            scaling_steps=scaling_steps,
            adjustment_type=adjustment_type,
            cooldown=cooldown,
            datapoints_to_alarm=datapoints_to_alarm,
            evaluation_periods=evaluation_periods,
            metric_aggregation_type=metric_aggregation_type,
            min_adjustment_magnitude=min_adjustment_magnitude,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="lowerAction")
    def lower_action(self) -> typing.Optional[StepScalingAction]:
        return typing.cast(typing.Optional[StepScalingAction], jsii.get(self, "lowerAction"))

    @builtins.property
    @jsii.member(jsii_name="lowerAlarm")
    def lower_alarm(self) -> typing.Optional[_Alarm_9fbab1f1]:
        return typing.cast(typing.Optional[_Alarm_9fbab1f1], jsii.get(self, "lowerAlarm"))

    @builtins.property
    @jsii.member(jsii_name="upperAction")
    def upper_action(self) -> typing.Optional[StepScalingAction]:
        return typing.cast(typing.Optional[StepScalingAction], jsii.get(self, "upperAction"))

    @builtins.property
    @jsii.member(jsii_name="upperAlarm")
    def upper_alarm(self) -> typing.Optional[_Alarm_9fbab1f1]:
        return typing.cast(typing.Optional[_Alarm_9fbab1f1], jsii.get(self, "upperAlarm"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_applicationautoscaling.StepScalingPolicyProps",
    jsii_struct_bases=[BasicStepScalingPolicyProps],
    name_mapping={
        "metric": "metric",
        "scaling_steps": "scalingSteps",
        "adjustment_type": "adjustmentType",
        "cooldown": "cooldown",
        "datapoints_to_alarm": "datapointsToAlarm",
        "evaluation_periods": "evaluationPeriods",
        "metric_aggregation_type": "metricAggregationType",
        "min_adjustment_magnitude": "minAdjustmentMagnitude",
        "scaling_target": "scalingTarget",
    },
)
class StepScalingPolicyProps(BasicStepScalingPolicyProps):
    def __init__(
        self,
        *,
        metric: _IMetric_c7fd29de,
        scaling_steps: typing.Sequence[typing.Union[ScalingInterval, typing.Dict[builtins.str, typing.Any]]],
        adjustment_type: typing.Optional[AdjustmentType] = None,
        cooldown: typing.Optional[_Duration_4839e8c3] = None,
        datapoints_to_alarm: typing.Optional[jsii.Number] = None,
        evaluation_periods: typing.Optional[jsii.Number] = None,
        metric_aggregation_type: typing.Optional[MetricAggregationType] = None,
        min_adjustment_magnitude: typing.Optional[jsii.Number] = None,
        scaling_target: IScalableTarget,
    ) -> None:
        '''
        :param metric: Metric to scale on.
        :param scaling_steps: The intervals for scaling. Maps a range of metric values to a particular scaling behavior. Must be between 2 and 40 steps.
        :param adjustment_type: How the adjustment numbers inside 'intervals' are interpreted. Default: ChangeInCapacity
        :param cooldown: Grace period after scaling activity. Subsequent scale outs during the cooldown period are squashed so that only the biggest scale out happens. Subsequent scale ins during the cooldown period are ignored. Default: No cooldown period
        :param datapoints_to_alarm: The number of data points out of the evaluation periods that must be breaching to trigger a scaling action. Creates an "M out of N" alarm, where this property is the M and the value set for ``evaluationPeriods`` is the N value. Only has meaning if ``evaluationPeriods != 1``. Default: - Same as ``evaluationPeriods``
        :param evaluation_periods: How many evaluation periods of the metric to wait before triggering a scaling action. Raising this value can be used to smooth out the metric, at the expense of slower response times. If ``datapointsToAlarm`` is not set, then all data points in the evaluation period must meet the criteria to trigger a scaling action. Default: 1
        :param metric_aggregation_type: Aggregation to apply to all data points over the evaluation periods. Only has meaning if ``evaluationPeriods != 1``. Default: - The statistic from the metric if applicable (MIN, MAX, AVERAGE), otherwise AVERAGE.
        :param min_adjustment_magnitude: Minimum absolute number to adjust capacity with as result of percentage scaling. Only when using AdjustmentType = PercentChangeInCapacity, this number controls the minimum absolute effect size. Default: No minimum scaling effect
        :param scaling_target: The scaling target.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk as cdk
            from aws_cdk import aws_applicationautoscaling as appscaling
            from aws_cdk import aws_cloudwatch as cloudwatch
            
            # metric: cloudwatch.Metric
            # scalable_target: appscaling.ScalableTarget
            
            step_scaling_policy_props = appscaling.StepScalingPolicyProps(
                metric=metric,
                scaling_steps=[appscaling.ScalingInterval(
                    change=123,
            
                    # the properties below are optional
                    lower=123,
                    upper=123
                )],
                scaling_target=scalable_target,
            
                # the properties below are optional
                adjustment_type=appscaling.AdjustmentType.CHANGE_IN_CAPACITY,
                cooldown=cdk.Duration.minutes(30),
                datapoints_to_alarm=123,
                evaluation_periods=123,
                metric_aggregation_type=appscaling.MetricAggregationType.AVERAGE,
                min_adjustment_magnitude=123
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5fb811fbae284660a73659f831a4a4abee74e6e6ca7a1b7e9971a7c43e39fb16)
            check_type(argname="argument metric", value=metric, expected_type=type_hints["metric"])
            check_type(argname="argument scaling_steps", value=scaling_steps, expected_type=type_hints["scaling_steps"])
            check_type(argname="argument adjustment_type", value=adjustment_type, expected_type=type_hints["adjustment_type"])
            check_type(argname="argument cooldown", value=cooldown, expected_type=type_hints["cooldown"])
            check_type(argname="argument datapoints_to_alarm", value=datapoints_to_alarm, expected_type=type_hints["datapoints_to_alarm"])
            check_type(argname="argument evaluation_periods", value=evaluation_periods, expected_type=type_hints["evaluation_periods"])
            check_type(argname="argument metric_aggregation_type", value=metric_aggregation_type, expected_type=type_hints["metric_aggregation_type"])
            check_type(argname="argument min_adjustment_magnitude", value=min_adjustment_magnitude, expected_type=type_hints["min_adjustment_magnitude"])
            check_type(argname="argument scaling_target", value=scaling_target, expected_type=type_hints["scaling_target"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "metric": metric,
            "scaling_steps": scaling_steps,
            "scaling_target": scaling_target,
        }
        if adjustment_type is not None:
            self._values["adjustment_type"] = adjustment_type
        if cooldown is not None:
            self._values["cooldown"] = cooldown
        if datapoints_to_alarm is not None:
            self._values["datapoints_to_alarm"] = datapoints_to_alarm
        if evaluation_periods is not None:
            self._values["evaluation_periods"] = evaluation_periods
        if metric_aggregation_type is not None:
            self._values["metric_aggregation_type"] = metric_aggregation_type
        if min_adjustment_magnitude is not None:
            self._values["min_adjustment_magnitude"] = min_adjustment_magnitude

    @builtins.property
    def metric(self) -> _IMetric_c7fd29de:
        '''Metric to scale on.'''
        result = self._values.get("metric")
        assert result is not None, "Required property 'metric' is missing"
        return typing.cast(_IMetric_c7fd29de, result)

    @builtins.property
    def scaling_steps(self) -> typing.List[ScalingInterval]:
        '''The intervals for scaling.

        Maps a range of metric values to a particular scaling behavior.

        Must be between 2 and 40 steps.
        '''
        result = self._values.get("scaling_steps")
        assert result is not None, "Required property 'scaling_steps' is missing"
        return typing.cast(typing.List[ScalingInterval], result)

    @builtins.property
    def adjustment_type(self) -> typing.Optional[AdjustmentType]:
        '''How the adjustment numbers inside 'intervals' are interpreted.

        :default: ChangeInCapacity
        '''
        result = self._values.get("adjustment_type")
        return typing.cast(typing.Optional[AdjustmentType], result)

    @builtins.property
    def cooldown(self) -> typing.Optional[_Duration_4839e8c3]:
        '''Grace period after scaling activity.

        Subsequent scale outs during the cooldown period are squashed so that only
        the biggest scale out happens.

        Subsequent scale ins during the cooldown period are ignored.

        :default: No cooldown period

        :see: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_StepScalingPolicyConfiguration.html
        '''
        result = self._values.get("cooldown")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def datapoints_to_alarm(self) -> typing.Optional[jsii.Number]:
        '''The number of data points out of the evaluation periods that must be breaching to trigger a scaling action.

        Creates an "M out of N" alarm, where this property is the M and the value set for
        ``evaluationPeriods`` is the N value.

        Only has meaning if ``evaluationPeriods != 1``.

        :default: - Same as ``evaluationPeriods``
        '''
        result = self._values.get("datapoints_to_alarm")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def evaluation_periods(self) -> typing.Optional[jsii.Number]:
        '''How many evaluation periods of the metric to wait before triggering a scaling action.

        Raising this value can be used to smooth out the metric, at the expense
        of slower response times.

        If ``datapointsToAlarm`` is not set, then all data points in the evaluation period
        must meet the criteria to trigger a scaling action.

        :default: 1
        '''
        result = self._values.get("evaluation_periods")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def metric_aggregation_type(self) -> typing.Optional[MetricAggregationType]:
        '''Aggregation to apply to all data points over the evaluation periods.

        Only has meaning if ``evaluationPeriods != 1``.

        :default: - The statistic from the metric if applicable (MIN, MAX, AVERAGE), otherwise AVERAGE.
        '''
        result = self._values.get("metric_aggregation_type")
        return typing.cast(typing.Optional[MetricAggregationType], result)

    @builtins.property
    def min_adjustment_magnitude(self) -> typing.Optional[jsii.Number]:
        '''Minimum absolute number to adjust capacity with as result of percentage scaling.

        Only when using AdjustmentType = PercentChangeInCapacity, this number controls
        the minimum absolute effect size.

        :default: No minimum scaling effect
        '''
        result = self._values.get("min_adjustment_magnitude")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def scaling_target(self) -> IScalableTarget:
        '''The scaling target.'''
        result = self._values.get("scaling_target")
        assert result is not None, "Required property 'scaling_target' is missing"
        return typing.cast(IScalableTarget, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StepScalingPolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TargetTrackingScalingPolicy(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_applicationautoscaling.TargetTrackingScalingPolicy",
):
    '''
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk as cdk
        from aws_cdk import aws_applicationautoscaling as appscaling
        from aws_cdk import aws_cloudwatch as cloudwatch
        
        # metric: cloudwatch.Metric
        # scalable_target: appscaling.ScalableTarget
        
        target_tracking_scaling_policy = appscaling.TargetTrackingScalingPolicy(self, "MyTargetTrackingScalingPolicy",
            scaling_target=scalable_target,
            target_value=123,
        
            # the properties below are optional
            custom_metric=metric,
            disable_scale_in=False,
            policy_name="policyName",
            predefined_metric=appscaling.PredefinedMetric.APPSTREAM_AVERAGE_CAPACITY_UTILIZATION,
            resource_label="resourceLabel",
            scale_in_cooldown=cdk.Duration.minutes(30),
            scale_out_cooldown=cdk.Duration.minutes(30)
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        scaling_target: IScalableTarget,
        target_value: jsii.Number,
        custom_metric: typing.Optional[_IMetric_c7fd29de] = None,
        predefined_metric: typing.Optional[PredefinedMetric] = None,
        resource_label: typing.Optional[builtins.str] = None,
        disable_scale_in: typing.Optional[builtins.bool] = None,
        policy_name: typing.Optional[builtins.str] = None,
        scale_in_cooldown: typing.Optional[_Duration_4839e8c3] = None,
        scale_out_cooldown: typing.Optional[_Duration_4839e8c3] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param scaling_target: 
        :param target_value: The target value for the metric.
        :param custom_metric: A custom metric for application autoscaling. The metric must track utilization. Scaling out will happen if the metric is higher than the target value, scaling in will happen in the metric is lower than the target value. Exactly one of customMetric or predefinedMetric must be specified. Default: - No custom metric.
        :param predefined_metric: A predefined metric for application autoscaling. The metric must track utilization. Scaling out will happen if the metric is higher than the target value, scaling in will happen in the metric is lower than the target value. Exactly one of customMetric or predefinedMetric must be specified. Default: - No predefined metrics.
        :param resource_label: Identify the resource associated with the metric type. Only used for predefined metric ALBRequestCountPerTarget. Example value: ``app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>`` Default: - No resource label.
        :param disable_scale_in: Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won't remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the scalable resource. Default: false
        :param policy_name: A name for the scaling policy. Default: - Automatically generated name.
        :param scale_in_cooldown: Period after a scale in activity completes before another scale in activity can start. Default: Duration.seconds(300) for the following scalable targets: ECS services, Spot Fleet requests, EMR clusters, AppStream 2.0 fleets, Aurora DB clusters, Amazon SageMaker endpoint variants, Custom resources. For all other scalable targets, the default value is Duration.seconds(0): DynamoDB tables, DynamoDB global secondary indexes, Amazon Comprehend document classification endpoints, Lambda provisioned concurrency
        :param scale_out_cooldown: Period after a scale out activity completes before another scale out activity can start. Default: Duration.seconds(300) for the following scalable targets: ECS services, Spot Fleet requests, EMR clusters, AppStream 2.0 fleets, Aurora DB clusters, Amazon SageMaker endpoint variants, Custom resources. For all other scalable targets, the default value is Duration.seconds(0): DynamoDB tables, DynamoDB global secondary indexes, Amazon Comprehend document classification endpoints, Lambda provisioned concurrency
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7be0faf4183aa8856518e373c609ce23a62f4ca392f7caaafd9b0d195902c2c4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = TargetTrackingScalingPolicyProps(
            scaling_target=scaling_target,
            target_value=target_value,
            custom_metric=custom_metric,
            predefined_metric=predefined_metric,
            resource_label=resource_label,
            disable_scale_in=disable_scale_in,
            policy_name=policy_name,
            scale_in_cooldown=scale_in_cooldown,
            scale_out_cooldown=scale_out_cooldown,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="scalingPolicyArn")
    def scaling_policy_arn(self) -> builtins.str:
        '''ARN of the scaling policy.'''
        return typing.cast(builtins.str, jsii.get(self, "scalingPolicyArn"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_applicationautoscaling.TargetTrackingScalingPolicyProps",
    jsii_struct_bases=[BasicTargetTrackingScalingPolicyProps],
    name_mapping={
        "disable_scale_in": "disableScaleIn",
        "policy_name": "policyName",
        "scale_in_cooldown": "scaleInCooldown",
        "scale_out_cooldown": "scaleOutCooldown",
        "target_value": "targetValue",
        "custom_metric": "customMetric",
        "predefined_metric": "predefinedMetric",
        "resource_label": "resourceLabel",
        "scaling_target": "scalingTarget",
    },
)
class TargetTrackingScalingPolicyProps(BasicTargetTrackingScalingPolicyProps):
    def __init__(
        self,
        *,
        disable_scale_in: typing.Optional[builtins.bool] = None,
        policy_name: typing.Optional[builtins.str] = None,
        scale_in_cooldown: typing.Optional[_Duration_4839e8c3] = None,
        scale_out_cooldown: typing.Optional[_Duration_4839e8c3] = None,
        target_value: jsii.Number,
        custom_metric: typing.Optional[_IMetric_c7fd29de] = None,
        predefined_metric: typing.Optional[PredefinedMetric] = None,
        resource_label: typing.Optional[builtins.str] = None,
        scaling_target: IScalableTarget,
    ) -> None:
        '''Properties for a concrete TargetTrackingPolicy.

        Adds the scalingTarget.

        :param disable_scale_in: Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won't remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the scalable resource. Default: false
        :param policy_name: A name for the scaling policy. Default: - Automatically generated name.
        :param scale_in_cooldown: Period after a scale in activity completes before another scale in activity can start. Default: Duration.seconds(300) for the following scalable targets: ECS services, Spot Fleet requests, EMR clusters, AppStream 2.0 fleets, Aurora DB clusters, Amazon SageMaker endpoint variants, Custom resources. For all other scalable targets, the default value is Duration.seconds(0): DynamoDB tables, DynamoDB global secondary indexes, Amazon Comprehend document classification endpoints, Lambda provisioned concurrency
        :param scale_out_cooldown: Period after a scale out activity completes before another scale out activity can start. Default: Duration.seconds(300) for the following scalable targets: ECS services, Spot Fleet requests, EMR clusters, AppStream 2.0 fleets, Aurora DB clusters, Amazon SageMaker endpoint variants, Custom resources. For all other scalable targets, the default value is Duration.seconds(0): DynamoDB tables, DynamoDB global secondary indexes, Amazon Comprehend document classification endpoints, Lambda provisioned concurrency
        :param target_value: The target value for the metric.
        :param custom_metric: A custom metric for application autoscaling. The metric must track utilization. Scaling out will happen if the metric is higher than the target value, scaling in will happen in the metric is lower than the target value. Exactly one of customMetric or predefinedMetric must be specified. Default: - No custom metric.
        :param predefined_metric: A predefined metric for application autoscaling. The metric must track utilization. Scaling out will happen if the metric is higher than the target value, scaling in will happen in the metric is lower than the target value. Exactly one of customMetric or predefinedMetric must be specified. Default: - No predefined metrics.
        :param resource_label: Identify the resource associated with the metric type. Only used for predefined metric ALBRequestCountPerTarget. Example value: ``app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>`` Default: - No resource label.
        :param scaling_target: 

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk as cdk
            from aws_cdk import aws_applicationautoscaling as appscaling
            from aws_cdk import aws_cloudwatch as cloudwatch
            
            # metric: cloudwatch.Metric
            # scalable_target: appscaling.ScalableTarget
            
            target_tracking_scaling_policy_props = appscaling.TargetTrackingScalingPolicyProps(
                scaling_target=scalable_target,
                target_value=123,
            
                # the properties below are optional
                custom_metric=metric,
                disable_scale_in=False,
                policy_name="policyName",
                predefined_metric=appscaling.PredefinedMetric.APPSTREAM_AVERAGE_CAPACITY_UTILIZATION,
                resource_label="resourceLabel",
                scale_in_cooldown=cdk.Duration.minutes(30),
                scale_out_cooldown=cdk.Duration.minutes(30)
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae7c2297352d4eb6a4dcaf3fd8ac527fdce1e50808e395744304db46aaedbc96)
            check_type(argname="argument disable_scale_in", value=disable_scale_in, expected_type=type_hints["disable_scale_in"])
            check_type(argname="argument policy_name", value=policy_name, expected_type=type_hints["policy_name"])
            check_type(argname="argument scale_in_cooldown", value=scale_in_cooldown, expected_type=type_hints["scale_in_cooldown"])
            check_type(argname="argument scale_out_cooldown", value=scale_out_cooldown, expected_type=type_hints["scale_out_cooldown"])
            check_type(argname="argument target_value", value=target_value, expected_type=type_hints["target_value"])
            check_type(argname="argument custom_metric", value=custom_metric, expected_type=type_hints["custom_metric"])
            check_type(argname="argument predefined_metric", value=predefined_metric, expected_type=type_hints["predefined_metric"])
            check_type(argname="argument resource_label", value=resource_label, expected_type=type_hints["resource_label"])
            check_type(argname="argument scaling_target", value=scaling_target, expected_type=type_hints["scaling_target"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "target_value": target_value,
            "scaling_target": scaling_target,
        }
        if disable_scale_in is not None:
            self._values["disable_scale_in"] = disable_scale_in
        if policy_name is not None:
            self._values["policy_name"] = policy_name
        if scale_in_cooldown is not None:
            self._values["scale_in_cooldown"] = scale_in_cooldown
        if scale_out_cooldown is not None:
            self._values["scale_out_cooldown"] = scale_out_cooldown
        if custom_metric is not None:
            self._values["custom_metric"] = custom_metric
        if predefined_metric is not None:
            self._values["predefined_metric"] = predefined_metric
        if resource_label is not None:
            self._values["resource_label"] = resource_label

    @builtins.property
    def disable_scale_in(self) -> typing.Optional[builtins.bool]:
        '''Indicates whether scale in by the target tracking policy is disabled.

        If the value is true, scale in is disabled and the target tracking policy
        won't remove capacity from the scalable resource. Otherwise, scale in is
        enabled and the target tracking policy can remove capacity from the
        scalable resource.

        :default: false
        '''
        result = self._values.get("disable_scale_in")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def policy_name(self) -> typing.Optional[builtins.str]:
        '''A name for the scaling policy.

        :default: - Automatically generated name.
        '''
        result = self._values.get("policy_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scale_in_cooldown(self) -> typing.Optional[_Duration_4839e8c3]:
        '''Period after a scale in activity completes before another scale in activity can start.

        :default:

        Duration.seconds(300) for the following scalable targets: ECS services,
        Spot Fleet requests, EMR clusters, AppStream 2.0 fleets, Aurora DB clusters,
        Amazon SageMaker endpoint variants, Custom resources. For all other scalable
        targets, the default value is Duration.seconds(0): DynamoDB tables, DynamoDB
        global secondary indexes, Amazon Comprehend document classification endpoints,
        Lambda provisioned concurrency
        '''
        result = self._values.get("scale_in_cooldown")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def scale_out_cooldown(self) -> typing.Optional[_Duration_4839e8c3]:
        '''Period after a scale out activity completes before another scale out activity can start.

        :default:

        Duration.seconds(300) for the following scalable targets: ECS services,
        Spot Fleet requests, EMR clusters, AppStream 2.0 fleets, Aurora DB clusters,
        Amazon SageMaker endpoint variants, Custom resources. For all other scalable
        targets, the default value is Duration.seconds(0): DynamoDB tables, DynamoDB
        global secondary indexes, Amazon Comprehend document classification endpoints,
        Lambda provisioned concurrency
        '''
        result = self._values.get("scale_out_cooldown")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def target_value(self) -> jsii.Number:
        '''The target value for the metric.'''
        result = self._values.get("target_value")
        assert result is not None, "Required property 'target_value' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def custom_metric(self) -> typing.Optional[_IMetric_c7fd29de]:
        '''A custom metric for application autoscaling.

        The metric must track utilization. Scaling out will happen if the metric is higher than
        the target value, scaling in will happen in the metric is lower than the target value.

        Exactly one of customMetric or predefinedMetric must be specified.

        :default: - No custom metric.
        '''
        result = self._values.get("custom_metric")
        return typing.cast(typing.Optional[_IMetric_c7fd29de], result)

    @builtins.property
    def predefined_metric(self) -> typing.Optional[PredefinedMetric]:
        '''A predefined metric for application autoscaling.

        The metric must track utilization. Scaling out will happen if the metric is higher than
        the target value, scaling in will happen in the metric is lower than the target value.

        Exactly one of customMetric or predefinedMetric must be specified.

        :default: - No predefined metrics.
        '''
        result = self._values.get("predefined_metric")
        return typing.cast(typing.Optional[PredefinedMetric], result)

    @builtins.property
    def resource_label(self) -> typing.Optional[builtins.str]:
        '''Identify the resource associated with the metric type.

        Only used for predefined metric ALBRequestCountPerTarget.

        Example value: ``app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>``

        :default: - No resource label.
        '''
        result = self._values.get("resource_label")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scaling_target(self) -> IScalableTarget:
        result = self._values.get("scaling_target")
        assert result is not None, "Required property 'scaling_target' is missing"
        return typing.cast(IScalableTarget, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TargetTrackingScalingPolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_applicationautoscaling.BaseScalableAttributeProps",
    jsii_struct_bases=[EnableScalingProps],
    name_mapping={
        "max_capacity": "maxCapacity",
        "min_capacity": "minCapacity",
        "dimension": "dimension",
        "resource_id": "resourceId",
        "role": "role",
        "service_namespace": "serviceNamespace",
    },
)
class BaseScalableAttributeProps(EnableScalingProps):
    def __init__(
        self,
        *,
        max_capacity: jsii.Number,
        min_capacity: typing.Optional[jsii.Number] = None,
        dimension: builtins.str,
        resource_id: builtins.str,
        role: _IRole_235f5d8e,
        service_namespace: ServiceNamespace,
    ) -> None:
        '''Properties for a ScalableTableAttribute.

        :param max_capacity: Maximum capacity to scale to.
        :param min_capacity: Minimum capacity to scale to. Default: 1
        :param dimension: Scalable dimension of the attribute.
        :param resource_id: Resource ID of the attribute.
        :param role: Role to use for scaling.
        :param service_namespace: Service namespace of the scalable attribute.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_applicationautoscaling as appscaling
            from aws_cdk import aws_iam as iam
            
            # role: iam.Role
            
            base_scalable_attribute_props = appscaling.BaseScalableAttributeProps(
                dimension="dimension",
                max_capacity=123,
                resource_id="resourceId",
                role=role,
                service_namespace=appscaling.ServiceNamespace.ECS,
            
                # the properties below are optional
                min_capacity=123
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9fea2eb514ef1fe185d6e985d0d3f309fbd779395b2070d5a9d451d80c271d13)
            check_type(argname="argument max_capacity", value=max_capacity, expected_type=type_hints["max_capacity"])
            check_type(argname="argument min_capacity", value=min_capacity, expected_type=type_hints["min_capacity"])
            check_type(argname="argument dimension", value=dimension, expected_type=type_hints["dimension"])
            check_type(argname="argument resource_id", value=resource_id, expected_type=type_hints["resource_id"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument service_namespace", value=service_namespace, expected_type=type_hints["service_namespace"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "max_capacity": max_capacity,
            "dimension": dimension,
            "resource_id": resource_id,
            "role": role,
            "service_namespace": service_namespace,
        }
        if min_capacity is not None:
            self._values["min_capacity"] = min_capacity

    @builtins.property
    def max_capacity(self) -> jsii.Number:
        '''Maximum capacity to scale to.'''
        result = self._values.get("max_capacity")
        assert result is not None, "Required property 'max_capacity' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def min_capacity(self) -> typing.Optional[jsii.Number]:
        '''Minimum capacity to scale to.

        :default: 1
        '''
        result = self._values.get("min_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def dimension(self) -> builtins.str:
        '''Scalable dimension of the attribute.'''
        result = self._values.get("dimension")
        assert result is not None, "Required property 'dimension' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_id(self) -> builtins.str:
        '''Resource ID of the attribute.'''
        result = self._values.get("resource_id")
        assert result is not None, "Required property 'resource_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role(self) -> _IRole_235f5d8e:
        '''Role to use for scaling.'''
        result = self._values.get("role")
        assert result is not None, "Required property 'role' is missing"
        return typing.cast(_IRole_235f5d8e, result)

    @builtins.property
    def service_namespace(self) -> ServiceNamespace:
        '''Service namespace of the scalable attribute.'''
        result = self._values.get("service_namespace")
        assert result is not None, "Required property 'service_namespace' is missing"
        return typing.cast(ServiceNamespace, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BaseScalableAttributeProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AdjustmentTier",
    "AdjustmentType",
    "BaseScalableAttribute",
    "BaseScalableAttributeProps",
    "BaseTargetTrackingProps",
    "BasicStepScalingPolicyProps",
    "BasicTargetTrackingScalingPolicyProps",
    "CfnScalableTarget",
    "CfnScalableTargetProps",
    "CfnScalingPolicy",
    "CfnScalingPolicyProps",
    "CronOptions",
    "EnableScalingProps",
    "IScalableTarget",
    "MetricAggregationType",
    "PredefinedMetric",
    "ScalableTarget",
    "ScalableTargetProps",
    "ScalingInterval",
    "ScalingSchedule",
    "Schedule",
    "ServiceNamespace",
    "StepScalingAction",
    "StepScalingActionProps",
    "StepScalingPolicy",
    "StepScalingPolicyProps",
    "TargetTrackingScalingPolicy",
    "TargetTrackingScalingPolicyProps",
]

publication.publish()

def _typecheckingstub__e92856d6925eb7a98c28e5624a5be0c6b4b99fe091967d8069251411469217fd(
    *,
    adjustment: jsii.Number,
    lower_bound: typing.Optional[jsii.Number] = None,
    upper_bound: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8600affa38d3ad7a26371cf54d8508b09daff72f32b8b1da067e86834ec3575c(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    dimension: builtins.str,
    resource_id: builtins.str,
    role: _IRole_235f5d8e,
    service_namespace: ServiceNamespace,
    max_capacity: jsii.Number,
    min_capacity: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f860eecb918f3d194ec191f1e14f6db4e310f7d65df849bae6100f4b122fb99(
    id: builtins.str,
    *,
    metric: _IMetric_c7fd29de,
    scaling_steps: typing.Sequence[typing.Union[ScalingInterval, typing.Dict[builtins.str, typing.Any]]],
    adjustment_type: typing.Optional[AdjustmentType] = None,
    cooldown: typing.Optional[_Duration_4839e8c3] = None,
    datapoints_to_alarm: typing.Optional[jsii.Number] = None,
    evaluation_periods: typing.Optional[jsii.Number] = None,
    metric_aggregation_type: typing.Optional[MetricAggregationType] = None,
    min_adjustment_magnitude: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82bcc29e64984d150edcca413653e7216fd0245b92c71db37506d1a93e054222(
    id: builtins.str,
    *,
    schedule: Schedule,
    end_time: typing.Optional[datetime.datetime] = None,
    max_capacity: typing.Optional[jsii.Number] = None,
    min_capacity: typing.Optional[jsii.Number] = None,
    start_time: typing.Optional[datetime.datetime] = None,
    time_zone: typing.Optional[_TimeZone_cdd72ac9] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d955311dd160aaa4e3b40a01c140d69bad0856804ffd0b3dbff8b52a628ab88f(
    id: builtins.str,
    *,
    target_value: jsii.Number,
    custom_metric: typing.Optional[_IMetric_c7fd29de] = None,
    predefined_metric: typing.Optional[PredefinedMetric] = None,
    resource_label: typing.Optional[builtins.str] = None,
    disable_scale_in: typing.Optional[builtins.bool] = None,
    policy_name: typing.Optional[builtins.str] = None,
    scale_in_cooldown: typing.Optional[_Duration_4839e8c3] = None,
    scale_out_cooldown: typing.Optional[_Duration_4839e8c3] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99ba5c9c979402884414e9574843c640de78dc18e7837b243b496ed4c150a1b1(
    *,
    disable_scale_in: typing.Optional[builtins.bool] = None,
    policy_name: typing.Optional[builtins.str] = None,
    scale_in_cooldown: typing.Optional[_Duration_4839e8c3] = None,
    scale_out_cooldown: typing.Optional[_Duration_4839e8c3] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85315ee41e5c634ea9c93ccb7019a42d1823a8b52cb598aba6a6c93df29956ec(
    *,
    metric: _IMetric_c7fd29de,
    scaling_steps: typing.Sequence[typing.Union[ScalingInterval, typing.Dict[builtins.str, typing.Any]]],
    adjustment_type: typing.Optional[AdjustmentType] = None,
    cooldown: typing.Optional[_Duration_4839e8c3] = None,
    datapoints_to_alarm: typing.Optional[jsii.Number] = None,
    evaluation_periods: typing.Optional[jsii.Number] = None,
    metric_aggregation_type: typing.Optional[MetricAggregationType] = None,
    min_adjustment_magnitude: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9c62810084b1b26b891f3d2a3faa25ac5bb982334bd2e6b42e142d8a7402689(
    *,
    disable_scale_in: typing.Optional[builtins.bool] = None,
    policy_name: typing.Optional[builtins.str] = None,
    scale_in_cooldown: typing.Optional[_Duration_4839e8c3] = None,
    scale_out_cooldown: typing.Optional[_Duration_4839e8c3] = None,
    target_value: jsii.Number,
    custom_metric: typing.Optional[_IMetric_c7fd29de] = None,
    predefined_metric: typing.Optional[PredefinedMetric] = None,
    resource_label: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b7828d7eb81c45c73ed70f9ac7ffe26699d8745e54d9a892440a20af1276437(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    max_capacity: jsii.Number,
    min_capacity: jsii.Number,
    resource_id: builtins.str,
    scalable_dimension: builtins.str,
    service_namespace: builtins.str,
    role_arn: typing.Optional[builtins.str] = None,
    scheduled_actions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnScalableTarget.ScheduledActionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    suspended_state: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnScalableTarget.SuspendedStateProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7eab92548702648ed3d9193a8bedd481f01db8b59f68de00b0454143553b1539(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dccf12738190780b1bb59e6433978f722516b4294053fe3cea7472b03fd1db9b(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aab88caece6d64e8566905de6661b92b1df09b9d335e0e8c0754b34f44d246e2(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b73964fa80587244137f97f906081898d6add27e7ac5c4b1110b5960dfbf7f8c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6222d448bf139000d6495103f3869076bae6b8c46711066c25270c8d2a240f4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4fae2c8cfacd2c2f1c7b6ce18c73fe5d382c388861da42afb198ead30adb892(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5baa82fd6ad58564620316e191b3085f34068537274501c2ae16cef617b55152(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9252d029d6d32f1b045421b6b1cde1f523488cdc4808bee1892014e6bd4dc0b1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1adb9fa5e86479f2f4514b089b4fcee3b8718c5f7874ca0fe66105630e3636f(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnScalableTarget.ScheduledActionProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0bbb1dcd1d81de0e4c36de9ea045348b3724df3d549254eef9a20300325fc117(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnScalableTarget.SuspendedStateProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__235dfc5c99fa3d515e24a56ba2af8e45cb7d6acefe812056f71abe1f48bd20ad(
    *,
    max_capacity: typing.Optional[jsii.Number] = None,
    min_capacity: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__602ff955f286e3df520d04ef3c033f033ea91710efbf10e64903936bd464753d(
    *,
    schedule: builtins.str,
    scheduled_action_name: builtins.str,
    end_time: typing.Optional[typing.Union[_IResolvable_da3f097b, datetime.datetime]] = None,
    scalable_target_action: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnScalableTarget.ScalableTargetActionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    start_time: typing.Optional[typing.Union[_IResolvable_da3f097b, datetime.datetime]] = None,
    timezone: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ec14b8e7471a97b7fc6a29eb82a7c1e0a63a4103237cfc54c79485673df1718(
    *,
    dynamic_scaling_in_suspended: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    dynamic_scaling_out_suspended: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    scheduled_scaling_suspended: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0aca5d6a38a10d55ae89247bf02288adc86be9fd694d2a88c8aaf7d40e74818c(
    *,
    max_capacity: jsii.Number,
    min_capacity: jsii.Number,
    resource_id: builtins.str,
    scalable_dimension: builtins.str,
    service_namespace: builtins.str,
    role_arn: typing.Optional[builtins.str] = None,
    scheduled_actions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnScalableTarget.ScheduledActionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    suspended_state: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnScalableTarget.SuspendedStateProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1fdbd49d0d5c8d10cb6dba70c50d20e471988b2d94237a064669be24bc1708e6(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    policy_name: builtins.str,
    policy_type: builtins.str,
    resource_id: typing.Optional[builtins.str] = None,
    scalable_dimension: typing.Optional[builtins.str] = None,
    scaling_target_id: typing.Optional[builtins.str] = None,
    service_namespace: typing.Optional[builtins.str] = None,
    step_scaling_policy_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnScalingPolicy.StepScalingPolicyConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    target_tracking_scaling_policy_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnScalingPolicy.TargetTrackingScalingPolicyConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06b6ee36474194c74b31f66e6e4141f9c4e6b18bc220e2d7e386cb92c8c7ab4b(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a136d66de9ef9614e63ed7ac6742e6389bf03e5cc8897d6d0ef331e7b20ac3ff(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c59722890877d8ddfaeabf8aced7cbcbac1e5b7bdc4bc14db89c2047881a540a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64ceb2a355ff27a664253fe046aa1782da96620b29bc51aeb4cc3d41e3e86c84(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__471855b6df8fda8e34a03d46cd115dff8f7756d99f246dde133740f2be29f4c4(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7c7fbf57e3d736c1fe088d47facb97643b88aa8c36fb8faed19ffa53682927f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f4fbea87ebb062bdc91ff07aec76f048538e421370633ef1c72dbf10223bf67(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56b9fc2d37586eb8d15fe8d758af97dd8d88e8a7505bd07bc33f6daba1dfff42(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ccee10df2369c02f2415d65418aa22f9f91b2dd5fab0700a4a452b640ae5db54(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnScalingPolicy.StepScalingPolicyConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d48220f9b4b78b76a3e0525fb18dc4772f5f73ecb26256ee41a09fa710c8be3a(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnScalingPolicy.TargetTrackingScalingPolicyConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f60b1265cbe9bf1a766a1e08801c1216e450695c574c54d2a3c2906a3e7a111(
    *,
    dimensions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnScalingPolicy.MetricDimensionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    metric_name: typing.Optional[builtins.str] = None,
    metrics: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnScalingPolicy.TargetTrackingMetricDataQueryProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    namespace: typing.Optional[builtins.str] = None,
    statistic: typing.Optional[builtins.str] = None,
    unit: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2bbab6c71eac87b44a87976e9ec88ca8fb9d041a349eeb47474fae5790b2b304(
    *,
    name: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__006a90e58fd47516fb147d13d14740fcdcd4c98e1ffcee20b2746e63c245c11a(
    *,
    predefined_metric_type: builtins.str,
    resource_label: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a06f512f9ba96f90127c3ef28f9aaa4ff2dd9349ab6fe34199dccd68563dfbe(
    *,
    scaling_adjustment: jsii.Number,
    metric_interval_lower_bound: typing.Optional[jsii.Number] = None,
    metric_interval_upper_bound: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0a66ea72967d0887e041501633c1f1033a5f00e71021336a89d0a3e26ad2f04(
    *,
    adjustment_type: typing.Optional[builtins.str] = None,
    cooldown: typing.Optional[jsii.Number] = None,
    metric_aggregation_type: typing.Optional[builtins.str] = None,
    min_adjustment_magnitude: typing.Optional[jsii.Number] = None,
    step_adjustments: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnScalingPolicy.StepAdjustmentProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50ed4be037740c44e4f261f3a2c559cf993db7b21e79e7a222e38614cb9f3f1a(
    *,
    expression: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    label: typing.Optional[builtins.str] = None,
    metric_stat: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnScalingPolicy.TargetTrackingMetricStatProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    return_data: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6c4fd40c2db7c3177dd019ca0cf15a886d8d3ccd5e0c55cb3d038c3c235eb53(
    *,
    name: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a50f07815ea8e711dbbeffa9e2d6ba43154a828c897de162bf209d78b6ce79c6(
    *,
    dimensions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnScalingPolicy.TargetTrackingMetricDimensionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    metric_name: typing.Optional[builtins.str] = None,
    namespace: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82b9cd8a8d1359a0e0fa7d4aef2938489da73589171a3927e18618a9db7d28c5(
    *,
    metric: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnScalingPolicy.TargetTrackingMetricProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    stat: typing.Optional[builtins.str] = None,
    unit: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d9326d5963b2f7c66feebec5211250ac93b956fe269a70f64aeb370aa662e58(
    *,
    target_value: jsii.Number,
    customized_metric_specification: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnScalingPolicy.CustomizedMetricSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    disable_scale_in: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    predefined_metric_specification: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnScalingPolicy.PredefinedMetricSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    scale_in_cooldown: typing.Optional[jsii.Number] = None,
    scale_out_cooldown: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eabc9b9cdfb95f21a9439a9250c214148ffe31ecc08a87e6125ff826c886f42c(
    *,
    policy_name: builtins.str,
    policy_type: builtins.str,
    resource_id: typing.Optional[builtins.str] = None,
    scalable_dimension: typing.Optional[builtins.str] = None,
    scaling_target_id: typing.Optional[builtins.str] = None,
    service_namespace: typing.Optional[builtins.str] = None,
    step_scaling_policy_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnScalingPolicy.StepScalingPolicyConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    target_tracking_scaling_policy_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnScalingPolicy.TargetTrackingScalingPolicyConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6de063595e26cfdffe8cc2657f923bb73bea86791277de8f39a31cb702a88687(
    *,
    day: typing.Optional[builtins.str] = None,
    hour: typing.Optional[builtins.str] = None,
    minute: typing.Optional[builtins.str] = None,
    month: typing.Optional[builtins.str] = None,
    week_day: typing.Optional[builtins.str] = None,
    year: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4c0cc0d56669ed17f3d9a93a8b999330c5c8ca16d7b5113495d4c0580beb45e(
    *,
    max_capacity: jsii.Number,
    min_capacity: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8491b1f534a6fef90c954e5a091a74102f414f9194833de06be45e1870c155d1(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    max_capacity: jsii.Number,
    min_capacity: jsii.Number,
    resource_id: builtins.str,
    scalable_dimension: builtins.str,
    service_namespace: ServiceNamespace,
    role: typing.Optional[_IRole_235f5d8e] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f478630191026eccd5282b715948991fc462028ebdcd6fe204c039659399c45f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    scalable_target_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53861afb9c89932c9e82e744d09e1f97e6015c7c2739481f75097c0c3e60e60e(
    statement: _PolicyStatement_0fe33853,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43ded9798fe3fbe40d7c97e40d4e8364a71e47cda844521e2013ac9a7c39a26a(
    id: builtins.str,
    *,
    metric: _IMetric_c7fd29de,
    scaling_steps: typing.Sequence[typing.Union[ScalingInterval, typing.Dict[builtins.str, typing.Any]]],
    adjustment_type: typing.Optional[AdjustmentType] = None,
    cooldown: typing.Optional[_Duration_4839e8c3] = None,
    datapoints_to_alarm: typing.Optional[jsii.Number] = None,
    evaluation_periods: typing.Optional[jsii.Number] = None,
    metric_aggregation_type: typing.Optional[MetricAggregationType] = None,
    min_adjustment_magnitude: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00b07b46a599f1f6e690aeeada38ac26bba7017192a30ed324e7c437647bb46b(
    id: builtins.str,
    *,
    schedule: Schedule,
    end_time: typing.Optional[datetime.datetime] = None,
    max_capacity: typing.Optional[jsii.Number] = None,
    min_capacity: typing.Optional[jsii.Number] = None,
    start_time: typing.Optional[datetime.datetime] = None,
    time_zone: typing.Optional[_TimeZone_cdd72ac9] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05dc12c8c78cbf6f9c0c66c5c142f63e0590f2157107bdf2505a0852a4f4a4b2(
    id: builtins.str,
    *,
    target_value: jsii.Number,
    custom_metric: typing.Optional[_IMetric_c7fd29de] = None,
    predefined_metric: typing.Optional[PredefinedMetric] = None,
    resource_label: typing.Optional[builtins.str] = None,
    disable_scale_in: typing.Optional[builtins.bool] = None,
    policy_name: typing.Optional[builtins.str] = None,
    scale_in_cooldown: typing.Optional[_Duration_4839e8c3] = None,
    scale_out_cooldown: typing.Optional[_Duration_4839e8c3] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad90959b199a68084c2e639ade21bf66df6004347d16c00dd766d667b4e2a529(
    *,
    max_capacity: jsii.Number,
    min_capacity: jsii.Number,
    resource_id: builtins.str,
    scalable_dimension: builtins.str,
    service_namespace: ServiceNamespace,
    role: typing.Optional[_IRole_235f5d8e] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6f6165efad90911203a00e6a29dd5b27c5e8a4d5bca2d5e0edab9a421d7368d(
    *,
    change: jsii.Number,
    lower: typing.Optional[jsii.Number] = None,
    upper: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57aef750eb5141016e0f252e7b49eacfa61419872935a6645e358d0c9484bb06(
    *,
    schedule: Schedule,
    end_time: typing.Optional[datetime.datetime] = None,
    max_capacity: typing.Optional[jsii.Number] = None,
    min_capacity: typing.Optional[jsii.Number] = None,
    start_time: typing.Optional[datetime.datetime] = None,
    time_zone: typing.Optional[_TimeZone_cdd72ac9] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b6d7fda9383aedbe53cc8d8ade34a64e19233e11096bdf1844196644aa79458(
    moment: datetime.datetime,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e25a6639f36857385bcf857e79dd3e959c720c58729794a75fde1193754cc9d(
    expression: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80021ca00d4dfc7e5d3749ddcb1a82c455470cb51699456caee089bcc2970257(
    duration: _Duration_4839e8c3,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ebea522c756d3475869e6f400a5bb4b68ea539cce554df0d9e91d7341299f80(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    scaling_target: IScalableTarget,
    adjustment_type: typing.Optional[AdjustmentType] = None,
    cooldown: typing.Optional[_Duration_4839e8c3] = None,
    metric_aggregation_type: typing.Optional[MetricAggregationType] = None,
    min_adjustment_magnitude: typing.Optional[jsii.Number] = None,
    policy_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__749520e5db8349113a00c486486d4029b1458a70e0520261f218726bd60fcb37(
    *,
    scaling_target: IScalableTarget,
    adjustment_type: typing.Optional[AdjustmentType] = None,
    cooldown: typing.Optional[_Duration_4839e8c3] = None,
    metric_aggregation_type: typing.Optional[MetricAggregationType] = None,
    min_adjustment_magnitude: typing.Optional[jsii.Number] = None,
    policy_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05f13291938a9d6d13d60ff41322988d2435145fc2b8137754016700734b81b7(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    scaling_target: IScalableTarget,
    metric: _IMetric_c7fd29de,
    scaling_steps: typing.Sequence[typing.Union[ScalingInterval, typing.Dict[builtins.str, typing.Any]]],
    adjustment_type: typing.Optional[AdjustmentType] = None,
    cooldown: typing.Optional[_Duration_4839e8c3] = None,
    datapoints_to_alarm: typing.Optional[jsii.Number] = None,
    evaluation_periods: typing.Optional[jsii.Number] = None,
    metric_aggregation_type: typing.Optional[MetricAggregationType] = None,
    min_adjustment_magnitude: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5fb811fbae284660a73659f831a4a4abee74e6e6ca7a1b7e9971a7c43e39fb16(
    *,
    metric: _IMetric_c7fd29de,
    scaling_steps: typing.Sequence[typing.Union[ScalingInterval, typing.Dict[builtins.str, typing.Any]]],
    adjustment_type: typing.Optional[AdjustmentType] = None,
    cooldown: typing.Optional[_Duration_4839e8c3] = None,
    datapoints_to_alarm: typing.Optional[jsii.Number] = None,
    evaluation_periods: typing.Optional[jsii.Number] = None,
    metric_aggregation_type: typing.Optional[MetricAggregationType] = None,
    min_adjustment_magnitude: typing.Optional[jsii.Number] = None,
    scaling_target: IScalableTarget,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7be0faf4183aa8856518e373c609ce23a62f4ca392f7caaafd9b0d195902c2c4(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    scaling_target: IScalableTarget,
    target_value: jsii.Number,
    custom_metric: typing.Optional[_IMetric_c7fd29de] = None,
    predefined_metric: typing.Optional[PredefinedMetric] = None,
    resource_label: typing.Optional[builtins.str] = None,
    disable_scale_in: typing.Optional[builtins.bool] = None,
    policy_name: typing.Optional[builtins.str] = None,
    scale_in_cooldown: typing.Optional[_Duration_4839e8c3] = None,
    scale_out_cooldown: typing.Optional[_Duration_4839e8c3] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae7c2297352d4eb6a4dcaf3fd8ac527fdce1e50808e395744304db46aaedbc96(
    *,
    disable_scale_in: typing.Optional[builtins.bool] = None,
    policy_name: typing.Optional[builtins.str] = None,
    scale_in_cooldown: typing.Optional[_Duration_4839e8c3] = None,
    scale_out_cooldown: typing.Optional[_Duration_4839e8c3] = None,
    target_value: jsii.Number,
    custom_metric: typing.Optional[_IMetric_c7fd29de] = None,
    predefined_metric: typing.Optional[PredefinedMetric] = None,
    resource_label: typing.Optional[builtins.str] = None,
    scaling_target: IScalableTarget,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9fea2eb514ef1fe185d6e985d0d3f309fbd779395b2070d5a9d451d80c271d13(
    *,
    max_capacity: jsii.Number,
    min_capacity: typing.Optional[jsii.Number] = None,
    dimension: builtins.str,
    resource_id: builtins.str,
    role: _IRole_235f5d8e,
    service_namespace: ServiceNamespace,
) -> None:
    """Type checking stubs"""
    pass
