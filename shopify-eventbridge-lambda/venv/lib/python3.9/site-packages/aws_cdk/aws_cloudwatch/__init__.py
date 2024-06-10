'''
# Amazon CloudWatch Construct Library

## Metric objects

Metric objects represent a metric that is emitted by AWS services or your own
application, such as `CPUUsage`, `FailureCount` or `Bandwidth`.

Metric objects can be constructed directly or are exposed by resources as
attributes. Resources that expose metrics will have functions that look
like `metricXxx()` which will return a Metric object, initialized with defaults
that make sense.

For example, `lambda.Function` objects have the `fn.metricErrors()` method, which
represents the amount of errors reported by that Lambda function:

```python
# fn: lambda.Function


errors = fn.metric_errors()
```

`Metric` objects can be account and region aware. You can specify `account` and `region` as properties of the metric, or use the `metric.attachTo(Construct)` method. `metric.attachTo()` will automatically copy the `region` and `account` fields of the `Construct`, which can come from anywhere in the Construct tree.

You can also instantiate `Metric` objects to reference any
[published metric](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/aws-services-cloudwatch-metrics.html)
that's not exposed using a convenience method on the CDK construct.
For example:

```python
hosted_zone = route53.HostedZone(self, "MyHostedZone", zone_name="example.org")
metric = cloudwatch.Metric(
    namespace="AWS/Route53",
    metric_name="DNSQueries",
    dimensions_map={
        "HostedZoneId": hosted_zone.hosted_zone_id
    }
)
```

### Instantiating a new Metric object

If you want to reference a metric that is not yet exposed by an existing construct,
you can instantiate a `Metric` object to represent it. For example:

```python
metric = cloudwatch.Metric(
    namespace="MyNamespace",
    metric_name="MyMetric",
    dimensions_map={
        "ProcessingStep": "Download"
    }
)
```

### Metric Math

Math expressions are supported by instantiating the `MathExpression` class.
For example, a math expression that sums two other metrics looks like this:

```python
# fn: lambda.Function


all_problems = cloudwatch.MathExpression(
    expression="errors + throttles",
    using_metrics={
        "errors": fn.metric_errors(),
        "throttles": fn.metric_throttles()
    }
)
```

You can use `MathExpression` objects like any other metric, including using
them in other math expressions:

```python
# fn: lambda.Function
# all_problems: cloudwatch.MathExpression


problem_percentage = cloudwatch.MathExpression(
    expression="(problems / invocations) * 100",
    using_metrics={
        "problems": all_problems,
        "invocations": fn.metric_invocations()
    }
)
```

### Search Expressions

Math expressions also support search expressions. For example, the following
search expression returns all CPUUtilization metrics that it finds, with the
graph showing the Average statistic with an aggregation period of 5 minutes:

```python
cpu_utilization = cloudwatch.MathExpression(
    expression="SEARCH('{AWS/EC2,InstanceId} MetricName=\"CPUUtilization\"', 'Average', 300)",

    # Specifying '' as the label suppresses the default behavior
    # of using the expression as metric label. This is especially appropriate
    # when using expressions that return multiple time series (like SEARCH()
    # or METRICS()), to show the labels of the retrieved metrics only.
    label=""
)
```

Cross-account and cross-region search expressions are also supported. Use
the `searchAccount` and `searchRegion` properties to specify the account
and/or region to evaluate the search expression against.

### Aggregation

To graph or alarm on metrics you must aggregate them first, using a function
like `Average` or a percentile function like `P99`. By default, most Metric objects
returned by CDK libraries will be configured as `Average` over `300 seconds` (5 minutes).
The exception is if the metric represents a count of discrete events, such as
failures. In that case, the Metric object will be configured as `Sum` over `300 seconds`, i.e. it represents the number of times that event occurred over the
time period.

If you want to change the default aggregation of the Metric object (for example,
the function or the period), you can do so by passing additional parameters
to the metric function call:

```python
# fn: lambda.Function


minute_error_rate = fn.metric_errors(
    statistic=cloudwatch.Stats.AVERAGE,
    period=Duration.minutes(1),
    label="Lambda failure rate"
)
```

The `statistic` field accepts a `string`; the `cloudwatch.Stats` object has a
number of predefined factory functions that help you constructs strings that are
appropriate for CloudWatch. The `metricErrors` function also allows changing the
metric label or color, which will be useful when embedding them in graphs (see
below).

> Rates versus Sums
>
> The reason for using `Sum` to count discrete events is that *some* events are
> emitted as either `0` or `1` (for example `Errors` for a Lambda) and some are
> only emitted as `1` (for example `NumberOfMessagesPublished` for an SNS
> topic).
>
> In case `0`-metrics are emitted, it makes sense to take the `Average` of this
> metric: the result will be the fraction of errors over all executions.
>
> If `0`-metrics are not emitted, the `Average` will always be equal to `1`,
> and not be very useful.
>
> In order to simplify the mental model of `Metric` objects, we default to
> aggregating using `Sum`, which will be the same for both metrics types. If you
> happen to know the Metric you want to alarm on makes sense as a rate
> (`Average`) you can always choose to change the statistic.

### Available Aggregation Statistics

For your metrics aggregation, you can use the following statistics:

| Statistic                |    Short format     |                 Long format                  | Factory name         |
| ------------------------ | :-----------------: | :------------------------------------------: | -------------------- |
| SampleCount (n)          |         ❌          |                      ❌                      | `Stats.SAMPLE_COUNT` |
| Average (avg)            |         ❌          |                      ❌                      | `Stats.AVERAGE`      |
| Sum                      |         ❌          |                      ❌                      | `Stats.SUM`          |
| Minimum (min)            |         ❌          |                      ❌                      | `Stats.MINIMUM`      |
| Maximum (max)            |         ❌          |                      ❌                      | `Stats.MAXIMUM`      |
| Interquartile mean (IQM) |         ❌          |                      ❌                      | `Stats.IQM`          |
| Percentile (p)           |        `p99`        |                      ❌                      | `Stats.p(99)`        |
| Winsorized mean (WM)     | `wm99` = `WM(:99%)` | `WM(x:y) \| WM(x%:y%) \| WM(x%:) \| WM(:y%)` | `Stats.wm(10, 90)`   |
| Trimmed count (TC)       | `tc99` = `TC(:99%)` | `TC(x:y) \| TC(x%:y%) \| TC(x%:) \| TC(:y%)` | `Stats.tc(10, 90)`   |
| Trimmed sum (TS)         | `ts99` = `TS(:99%)` | `TS(x:y) \| TS(x%:y%) \| TS(x%:) \| TS(:y%)` | `Stats.ts(10, 90)`   |
| Percentile rank (PR)     |         ❌          |        `PR(x:y) \| PR(x:) \| PR(:y)`         | `Stats.pr(10, 5000)` |

The most common values are provided in the `cloudwatch.Stats` class. You can provide any string if your statistic is not in the class.

Read more at [CloudWatch statistics definitions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Statistics-definitions.html).

```python
# hosted_zone: route53.HostedZone


cloudwatch.Metric(
    namespace="AWS/Route53",
    metric_name="DNSQueries",
    dimensions_map={
        "HostedZoneId": hosted_zone.hosted_zone_id
    },
    statistic=cloudwatch.Stats.SAMPLE_COUNT,
    period=Duration.minutes(5)
)

cloudwatch.Metric(
    namespace="AWS/Route53",
    metric_name="DNSQueries",
    dimensions_map={
        "HostedZoneId": hosted_zone.hosted_zone_id
    },
    statistic=cloudwatch.Stats.p(99),
    period=Duration.minutes(5)
)

cloudwatch.Metric(
    namespace="AWS/Route53",
    metric_name="DNSQueries",
    dimensions_map={
        "HostedZoneId": hosted_zone.hosted_zone_id
    },
    statistic="TS(7.5%:90%)",
    period=Duration.minutes(5)
)
```

### Labels

Metric labels are displayed in the legend of graphs that include the metrics.

You can use [dynamic labels](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html)
to show summary information about the displayed time series
in the legend. For example, if you use:

```python
# fn: lambda.Function


minute_error_rate = fn.metric_errors(
    statistic=cloudwatch.Stats.SUM,
    period=Duration.hours(1),

    # Show the maximum hourly error count in the legend
    label="[max: ${MAX}] Lambda failure rate"
)
```

As the metric label, the maximum value in the visible range will
be shown next to the time series name in the graph's legend.

If the metric is a math expression producing more than one time series, the
maximum will be individually calculated and shown for each time series produce
by the math expression.

## Alarms

Alarms can be created on metrics in one of two ways. Either create an `Alarm`
object, passing the `Metric` object to set the alarm on:

```python
# fn: lambda.Function


cloudwatch.Alarm(self, "Alarm",
    metric=fn.metric_errors(),
    threshold=100,
    evaluation_periods=2
)
```

Alternatively, you can call `metric.createAlarm()`:

```python
# fn: lambda.Function


fn.metric_errors().create_alarm(self, "Alarm",
    threshold=100,
    evaluation_periods=2
)
```

The most important properties to set while creating an Alarms are:

* `threshold`: the value to compare the metric against.
* `comparisonOperator`: the comparison operation to use, defaults to `metric >= threshold`.
* `evaluationPeriods`: how many consecutive periods the metric has to be
  breaching the threshold for the alarm to trigger.

To create a cross-account alarm, make sure you have enabled [cross-account functionality](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Cross-Account-Cross-Region.html) in CloudWatch. Then, set the `account` property in the `Metric` object either manually or via the `metric.attachTo()` method.

Please note that it is **not possible** to:

* Create a cross-Account alarm that has `evaluateLowSampleCountPercentile: "ignore"`. The reason is that the only
  way to pass an AccountID is to use the [`Metrics` field of the Alarm resource](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-alarm.html#cfn-cloudwatch-alarm-metrics). If we use the `Metrics` field, the CloudWatch event that is
  used to evaluate the Alarm doesn't have a `SampleCount` field anymore ("[When CloudWatch evaluates alarms, periods are aggregated into single data points](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Create-alarm-on-metric-math-expression.html)"). The result is that the Alarm cannot evaluate at all.
* Create a cross-Region alarm ([source](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Cross-Account-Cross-Region.html)).

### Alarm Actions

To add actions to an alarm, use the integration classes from the
`aws-cdk-lib/aws-cloudwatch-actions` package. For example, to post a message to
an SNS topic when an alarm breaches, do the following:

```python
import aws_cdk.aws_cloudwatch_actions as cw_actions
# alarm: cloudwatch.Alarm


topic = sns.Topic(self, "Topic")
alarm.add_alarm_action(cw_actions.SnsAction(topic))
```

#### Notification formats

Alarms can be created in one of two "formats":

* With "top-level parameters" (these are the classic style of CloudWatch Alarms).
* With a list of metrics specifications (these are the modern style of CloudWatch Alarms).

For backwards compatibility, CDK will try to create classic, top-level CloudWatch alarms
as much as possible, unless you are using features that cannot be expressed in that format.
Features that require the new-style alarm format are:

* Metric math
* Cross-account metrics
* Labels

The difference between these two does not impact the functionality of the alarm
in any way, *except* that the format of the notifications the Alarm generates is
different between them. This affects both the notifications sent out over SNS,
as well as the EventBridge events generated by this Alarm. If you are writing
code to consume these notifications, be sure to handle both formats.

### Composite Alarms

[Composite Alarms](https://aws.amazon.com/about-aws/whats-new/2020/03/amazon-cloudwatch-now-allows-you-to-combine-multiple-alarms/)
can be created from existing Alarm resources.

```python
# alarm1: cloudwatch.Alarm
# alarm2: cloudwatch.Alarm
# alarm3: cloudwatch.Alarm
# alarm4: cloudwatch.Alarm


alarm_rule = cloudwatch.AlarmRule.any_of(
    cloudwatch.AlarmRule.all_of(
        cloudwatch.AlarmRule.any_of(alarm1,
            cloudwatch.AlarmRule.from_alarm(alarm2, cloudwatch.AlarmState.OK), alarm3),
        cloudwatch.AlarmRule.not(cloudwatch.AlarmRule.from_alarm(alarm4, cloudwatch.AlarmState.INSUFFICIENT_DATA))),
    cloudwatch.AlarmRule.from_boolean(False))

cloudwatch.CompositeAlarm(self, "MyAwesomeCompositeAlarm",
    alarm_rule=alarm_rule
)
```

#### Actions Suppressor

If you want to disable actions of a Composite Alarm based on a certain condition, you can use [Actions Suppression](https://www.amazonaws.cn/en/new/2022/amazon-cloudwatch-supports-composite-alarm-actions-suppression/).

```python
# alarm1: cloudwatch.Alarm
# alarm2: cloudwatch.Alarm
# on_alarm_action: cloudwatch.IAlarmAction
# on_ok_action: cloudwatch.IAlarmAction
# actions_suppressor: cloudwatch.Alarm


alarm_rule = cloudwatch.AlarmRule.any_of(alarm1, alarm2)

my_composite_alarm = cloudwatch.CompositeAlarm(self, "MyAwesomeCompositeAlarm",
    alarm_rule=alarm_rule,
    actions_suppressor=actions_suppressor
)
my_composite_alarm.add_alarm_action(on_alarm_action)
my_composite_alarm.add_ok_action(on_ok_action)
```

In the provided example, if `actionsSuppressor` is in `ALARM` state, `onAlarmAction` won't be triggered even if `myCompositeAlarm` goes into `ALARM` state.
Similar, if `actionsSuppressor` is in `ALARM` state and `myCompositeAlarm` goes from `ALARM` into `OK` state, `onOkAction` won't be triggered.

### A note on units

In CloudWatch, Metrics datums are emitted with units, such as `seconds` or
`bytes`. When `Metric` objects are given a `unit` attribute, it will be used to
*filter* the stream of metric datums for datums emitted using the same `unit`
attribute.

In particular, the `unit` field is *not* used to rescale datums or alarm threshold
values (for example, it cannot be used to specify an alarm threshold in
*Megabytes* if the metric stream is being emitted as *bytes*).

You almost certainly don't want to specify the `unit` property when creating
`Metric` objects (which will retrieve all datums regardless of their unit),
unless you have very specific requirements. Note that in any case, CloudWatch
only supports filtering by `unit` for Alarms, not in Dashboard graphs.

Please see the following GitHub issue for a discussion on real unit
calculations in CDK: https://github.com/aws/aws-cdk/issues/5595

## Dashboards

Dashboards are set of Widgets stored server-side which can be accessed quickly
from the AWS console. Available widgets are graphs of a metric over time, the
current value of a metric, or a static piece of Markdown which explains what the
graphs mean.

The following widgets are available:

* `GraphWidget` -- shows any number of metrics on both the left and right
  vertical axes.
* `AlarmWidget` -- shows the graph and alarm line for a single alarm.
* `SingleValueWidget` -- shows the current value of a set of metrics.
* `TextWidget` -- shows some static Markdown.
* `AlarmStatusWidget` -- shows the status of your alarms in a grid view.

### Graph widget

A graph widget can display any number of metrics on either the `left` or
`right` vertical axis:

```python
# dashboard: cloudwatch.Dashboard
# execution_count_metric: cloudwatch.Metric
# error_count_metric: cloudwatch.Metric


dashboard.add_widgets(cloudwatch.GraphWidget(
    title="Executions vs error rate",

    left=[execution_count_metric],

    right=[error_count_metric.with(
        statistic=cloudwatch.Stats.AVERAGE,
        label="Error rate",
        color=cloudwatch.Color.GREEN
    )]
))
```

Using the methods `addLeftMetric()` and `addRightMetric()` you can add metrics to a graph widget later on.

Graph widgets can also display annotations attached to the left or right y-axis or the x-axis.

```python
# dashboard: cloudwatch.Dashboard


dashboard.add_widgets(cloudwatch.GraphWidget(
    # ...

    left_annotations=[cloudwatch.HorizontalAnnotation(value=1800, label=Duration.minutes(30).to_human_string(), color=cloudwatch.Color.RED), cloudwatch.HorizontalAnnotation(value=3600, label="1 hour", color="#2ca02c")
    ],
    vertical_annotations=[cloudwatch.VerticalAnnotation(date="2022-10-19T00:00:00Z", label="Deployment", color=cloudwatch.Color.RED)
    ]
))
```

The graph legend can be adjusted from the default position at bottom of the widget.

```python
# dashboard: cloudwatch.Dashboard


dashboard.add_widgets(cloudwatch.GraphWidget(
    # ...

    legend_position=cloudwatch.LegendPosition.RIGHT
))
```

The graph can publish live data within the last minute that has not been fully aggregated.

```python
# dashboard: cloudwatch.Dashboard


dashboard.add_widgets(cloudwatch.GraphWidget(
    # ...

    live_data=True
))
```

The graph view can be changed from default 'timeSeries' to 'bar' or 'pie'.

```python
# dashboard: cloudwatch.Dashboard


dashboard.add_widgets(cloudwatch.GraphWidget(
    # ...

    view=cloudwatch.GraphWidgetView.BAR
))
```

The `start` and `end` properties can be used to specify the time range for each graph widget independently from those of the dashboard.
The parameters can be specified at `GraphWidget`, `GaugeWidget`, and `SingleValueWidget`.

```python
# dashboard: cloudwatch.Dashboard


dashboard.add_widgets(cloudwatch.GraphWidget(
    # ...

    start="-P7D",
    end="2018-12-17T06:00:00.000Z"
))
```

### Table Widget

A `TableWidget` can display any number of metrics in tabular form.

```python
# dashboard: cloudwatch.Dashboard
# execution_count_metric: cloudwatch.Metric


dashboard.add_widgets(cloudwatch.TableWidget(
    title="Executions",
    metrics=[execution_count_metric]
))
```

The `layout` property can be used to invert the rows and columns of the table.
The default `cloudwatch.TableLayout.HORIZONTAL` means that metrics are shown in rows and datapoints in columns.
`cloudwatch.TableLayout.VERTICAL` means that metrics are shown in columns and datapoints in rows.

```python
# dashboard: cloudwatch.Dashboard


dashboard.add_widgets(cloudwatch.TableWidget(
    # ...

    layout=cloudwatch.TableLayout.VERTICAL
))
```

The `summary` property allows customizing the table to show summary columns (`columns` sub property),
whether to make the summary columns sticky remaining in view while scrolling (`sticky` sub property),
and to optionally only present summary columns (`hideNonSummaryColumns` sub property).

```python
# dashboard: cloudwatch.Dashboard


dashboard.add_widgets(cloudwatch.TableWidget(
    # ...

    summary=cloudwatch.TableSummaryProps(
        columns=[cloudwatch.TableSummaryColumn.AVERAGE],
        hide_non_summary_columns=True,
        sticky=True
    )
))
```

The `thresholds` property can be used to highlight cells with a color when the datapoint value falls within the threshold.

```python
# dashboard: cloudwatch.Dashboard


dashboard.add_widgets(cloudwatch.TableWidget(
    # ...

    thresholds=[
        cloudwatch.TableThreshold.above(1000, cloudwatch.Color.RED),
        cloudwatch.TableThreshold.between(500, 1000, cloudwatch.Color.ORANGE),
        cloudwatch.TableThreshold.below(500, cloudwatch.Color.GREEN)
    ]
))
```

The `showUnitsInLabel` property can be used to display what unit is associated with a metric in the label column.

```python
# dashboard: cloudwatch.Dashboard


dashboard.add_widgets(cloudwatch.TableWidget(
    # ...

    show_units_in_label=True
))
```

The `fullPrecision` property can be used to show as many digits as can fit in a cell, before rounding.

```python
# dashboard: cloudwatch.Dashboard


dashboard.add_widgets(cloudwatch.TableWidget(
    # ...

    full_precision=True
))
```

### Gauge widget

Gauge graph requires the max and min value of the left Y axis, if no value is informed the limits will be from 0 to 100.

```python
# dashboard: cloudwatch.Dashboard
# error_alarm: cloudwatch.Alarm
# gauge_metric: cloudwatch.Metric


dashboard.add_widgets(cloudwatch.GaugeWidget(
    metrics=[gauge_metric],
    left_yAxis=cloudwatch.YAxisProps(
        min=0,
        max=1000
    )
))
```

### Alarm widget

An alarm widget shows the graph and the alarm line of a single alarm:

```python
# dashboard: cloudwatch.Dashboard
# error_alarm: cloudwatch.Alarm


dashboard.add_widgets(cloudwatch.AlarmWidget(
    title="Errors",
    alarm=error_alarm
))
```

### Single value widget

A single-value widget shows the latest value of a set of metrics (as opposed
to a graph of the value over time):

```python
# dashboard: cloudwatch.Dashboard
# visitor_count: cloudwatch.Metric
# purchase_count: cloudwatch.Metric


dashboard.add_widgets(cloudwatch.SingleValueWidget(
    metrics=[visitor_count, purchase_count]
))
```

Show as many digits as can fit, before rounding.

```python
# dashboard: cloudwatch.Dashboard


dashboard.add_widgets(cloudwatch.SingleValueWidget(
    metrics=[],

    full_precision=True
))
```

Sparkline allows you to glance the trend of a metric by displaying a simplified linegraph below the value. You can't use `sparkline: true` together with `setPeriodToTimeRange: true`

```python
# dashboard: cloudwatch.Dashboard


dashboard.add_widgets(cloudwatch.SingleValueWidget(
    metrics=[],

    sparkline=True
))
```

Period allows you to set the default period for the widget:

```python
# dashboard: cloudwatch.Dashboard


dashboard.add_widgets(cloudwatch.SingleValueWidget(
    metrics=[],

    period=Duration.minutes(15)
))
```

### Text widget

A text widget shows an arbitrary piece of MarkDown. Use this to add explanations
to your dashboard:

```python
# dashboard: cloudwatch.Dashboard


dashboard.add_widgets(cloudwatch.TextWidget(
    markdown="# Key Performance Indicators"
))
```

Optionally set the TextWidget background to be transparent

```python
# dashboard: cloudwatch.Dashboard


dashboard.add_widgets(cloudwatch.TextWidget(
    markdown="# Key Performance Indicators",
    background=cloudwatch.TextWidgetBackground.TRANSPARENT
))
```

### Alarm Status widget

An alarm status widget displays instantly the status of any type of alarms and gives the
ability to aggregate one or more alarms together in a small surface.

```python
# dashboard: cloudwatch.Dashboard
# error_alarm: cloudwatch.Alarm


dashboard.add_widgets(
    cloudwatch.AlarmStatusWidget(
        alarms=[error_alarm]
    ))
```

An alarm status widget only showing firing alarms, sorted by state and timestamp:

```python
# dashboard: cloudwatch.Dashboard
# error_alarm: cloudwatch.Alarm


dashboard.add_widgets(cloudwatch.AlarmStatusWidget(
    title="Errors",
    alarms=[error_alarm],
    sort_by=cloudwatch.AlarmStatusWidgetSortBy.STATE_UPDATED_TIMESTAMP,
    states=[cloudwatch.AlarmState.ALARM]
))
```

### Query results widget

A `LogQueryWidget` shows the results of a query from Logs Insights:

```python
# dashboard: cloudwatch.Dashboard


dashboard.add_widgets(cloudwatch.LogQueryWidget(
    log_group_names=["my-log-group"],
    view=cloudwatch.LogQueryVisualizationType.TABLE,
    # The lines will be automatically combined using '\n|'.
    query_lines=["fields @message", "filter @message like /Error/"
    ]
))
```

### Custom widget

A `CustomWidget` shows the result of an AWS Lambda function:

```python
# dashboard: cloudwatch.Dashboard


# Import or create a lambda function
fn = lambda_.Function.from_function_arn(dashboard, "Function", "arn:aws:lambda:us-east-1:123456789012:function:MyFn")

dashboard.add_widgets(cloudwatch.CustomWidget(
    function_arn=fn.function_arn,
    title="My lambda baked widget"
))
```

You can learn more about custom widgets in the [Amazon Cloudwatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/add_custom_widget_dashboard.html).

### Dashboard Layout

The widgets on a dashboard are visually laid out in a grid that is 24 columns
wide. Normally you specify X and Y coordinates for the widgets on a Dashboard,
but because this is inconvenient to do manually, the library contains a simple
layout system to help you lay out your dashboards the way you want them to.

Widgets have a `width` and `height` property, and they will be automatically
laid out either horizontally or vertically stacked to fill out the available
space.

Widgets are added to a Dashboard by calling `add(widget1, widget2, ...)`.
Widgets given in the same call will be laid out horizontally. Widgets given
in different calls will be laid out vertically. To make more complex layouts,
you can use the following widgets to pack widgets together in different ways:

* `Column`: stack two or more widgets vertically.
* `Row`: lay out two or more widgets horizontally.
* `Spacer`: take up empty space

### Column widget

A column widget contains other widgets and they will be laid out in a
vertical column. Widgets will be put one after another in order.

```python
# widget_a: cloudwatch.IWidget
# widget_b: cloudwatch.IWidget


cloudwatch.Column(widget_a, widget_b)
```

You can add a widget after object instantiation with the method
`addWidget()`. Each new widget will be put at the bottom of the column.

### Row widget

A row widget contains other widgets and they will be laid out in a
horizontal row. Widgets will be put one after another in order.
If the total width of the row exceeds the max width of the grid of 24
columns, the row will wrap automatically and adapt its height.

```python
# widget_a: cloudwatch.IWidget
# widget_b: cloudwatch.IWidget


cloudwatch.Row(widget_a, widget_b)
```

You can add a widget after object instantiation with the method
`addWidget()`.

### Interval duration for dashboard

Interval duration for metrics in dashboard. You can specify `defaultInterval` with
the relative time(eg. 7 days) as `Duration.days(7)`.

```python
import aws_cdk.aws_cloudwatch as cw


dashboard = cw.Dashboard(self, "Dash",
    default_interval=Duration.days(7)
)
```

Here, the dashboard would show the metrics for the last 7 days.

### Dashboard variables

Dashboard variables are a convenient way to create flexible dashboards that display different content depending
on the value of an input field within a dashboard. They create a dashboard on which it's possible to quickly switch between
different Lambda functions, Amazon EC2 instances, etc.

You can learn more about Dashboard variables in the [Amazon Cloudwatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_dashboard_variables.html)

There are two types of dashboard variables available: a property variable and a pattern variable.

* Property variables can change any JSON property in the JSON source of a dashboard like `region`. It can also change the dimension name for a metric.
* Pattern variables use a regular expression pattern to change all or part of a JSON property.

A use case of a **property variable** is a dashboard with the ability to toggle the `region` property to see the same dashboard in different regions:

```python
import aws_cdk.aws_cloudwatch as cw


dashboard = cw.Dashboard(self, "Dash",
    default_interval=Duration.days(7),
    variables=[cw.DashboardVariable(
        id="region",
        type=cw.VariableType.PROPERTY,
        label="Region",
        input_type=cw.VariableInputType.RADIO,
        value="region",
        values=cw.Values.from_values(cw.VariableValue(label="IAD", value="us-east-1"), label="DUB", value="us-west-2"),
        default_value=cw.DefaultValue.value("us-east-1"),
        visible=True
    )]
)
```

This example shows how to change `region` everywhere, assuming the current dashboard is showing region `us-east-1` already, by using **pattern variable**

```python
import aws_cdk.aws_cloudwatch as cw


dashboard = cw.Dashboard(self, "Dash",
    default_interval=Duration.days(7),
    variables=[cw.DashboardVariable(
        id="region2",
        type=cw.VariableType.PATTERN,
        label="RegionPattern",
        input_type=cw.VariableInputType.INPUT,
        value="us-east-1",
        default_value=cw.DefaultValue.value("us-east-1"),
        visible=True
    )]
)
```

The following example generates a Lambda function variable, with a radio button for each function. Functions are discovered by a metric query search.
The `values` with `cw.Values.fromSearchComponents` indicates that the values will be populated from `FunctionName` values retrieved from the search expression `{AWS/Lambda,FunctionName} MetricName=\"Duration\"`.
The `defaultValue` with `cw.DefaultValue.FIRST` indicates that the default value will be the first value returned from the search.

```python
import aws_cdk.aws_cloudwatch as cw


dashboard = cw.Dashboard(self, "Dash",
    default_interval=Duration.days(7),
    variables=[cw.DashboardVariable(
        id="functionName",
        type=cw.VariableType.PATTERN,
        label="Function",
        input_type=cw.VariableInputType.RADIO,
        value="originalFuncNameInDashboard",
        # equivalent to cw.Values.fromSearch('{AWS/Lambda,FunctionName} MetricName=\"Duration\"', 'FunctionName')
        values=cw.Values.from_search_components(
            namespace="AWS/Lambda",
            dimensions=["FunctionName"],
            metric_name="Duration",
            populate_from="FunctionName"
        ),
        default_value=cw.DefaultValue.FIRST,
        visible=True
    )]
)
```

You can add a variable after object instantiation with the method `dashboard.addVariable()`.
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
    ITaggableV2 as _ITaggableV2_4e6798f8,
    Resource as _Resource_45bc6135,
    ResourceProps as _ResourceProps_15a65b4e,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)
from ..aws_iam import Grant as _Grant_a7ae64f8, IGrantable as _IGrantable_71c4f5de


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudwatch.AlarmActionConfig",
    jsii_struct_bases=[],
    name_mapping={"alarm_action_arn": "alarmActionArn"},
)
class AlarmActionConfig:
    def __init__(self, *, alarm_action_arn: builtins.str) -> None:
        '''Properties for an alarm action.

        :param alarm_action_arn: Return the ARN that should be used for a CloudWatch Alarm action.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cloudwatch as cloudwatch
            
            alarm_action_config = cloudwatch.AlarmActionConfig(
                alarm_action_arn="alarmActionArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f1ff7030413de3d64c1ba15be58b5993bda266f09d078a54ade9ac8b5a2c478)
            check_type(argname="argument alarm_action_arn", value=alarm_action_arn, expected_type=type_hints["alarm_action_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "alarm_action_arn": alarm_action_arn,
        }

    @builtins.property
    def alarm_action_arn(self) -> builtins.str:
        '''Return the ARN that should be used for a CloudWatch Alarm action.'''
        result = self._values.get("alarm_action_arn")
        assert result is not None, "Required property 'alarm_action_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AlarmActionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AlarmRule(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudwatch.AlarmRule",
):
    '''Class with static functions to build AlarmRule for Composite Alarms.

    :exampleMetadata: infused

    Example::

        # alarm1: cloudwatch.Alarm
        # alarm2: cloudwatch.Alarm
        # alarm3: cloudwatch.Alarm
        # alarm4: cloudwatch.Alarm
        
        
        alarm_rule = cloudwatch.AlarmRule.any_of(
            cloudwatch.AlarmRule.all_of(
                cloudwatch.AlarmRule.any_of(alarm1,
                    cloudwatch.AlarmRule.from_alarm(alarm2, cloudwatch.AlarmState.OK), alarm3),
                cloudwatch.AlarmRule.not(cloudwatch.AlarmRule.from_alarm(alarm4, cloudwatch.AlarmState.INSUFFICIENT_DATA))),
            cloudwatch.AlarmRule.from_boolean(False))
        
        cloudwatch.CompositeAlarm(self, "MyAwesomeCompositeAlarm",
            alarm_rule=alarm_rule
        )
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="allOf")
    @builtins.classmethod
    def all_of(cls, *operands: "IAlarmRule") -> "IAlarmRule":
        '''function to join all provided AlarmRules with AND operator.

        :param operands: IAlarmRules to be joined with AND operator.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a73fcf7d7f6f71bc46cabb994493848ff6474356a6f35fb7c178bc77e7b4bf0b)
            check_type(argname="argument operands", value=operands, expected_type=typing.Tuple[type_hints["operands"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast("IAlarmRule", jsii.sinvoke(cls, "allOf", [*operands]))

    @jsii.member(jsii_name="anyOf")
    @builtins.classmethod
    def any_of(cls, *operands: "IAlarmRule") -> "IAlarmRule":
        '''function to join all provided AlarmRules with OR operator.

        :param operands: IAlarmRules to be joined with OR operator.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c83f7a2932bb0e6ad7daedb63c82a736735f725c8596adb65d2dd0358464ade)
            check_type(argname="argument operands", value=operands, expected_type=typing.Tuple[type_hints["operands"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast("IAlarmRule", jsii.sinvoke(cls, "anyOf", [*operands]))

    @jsii.member(jsii_name="fromAlarm")
    @builtins.classmethod
    def from_alarm(cls, alarm: "IAlarm", alarm_state: "AlarmState") -> "IAlarmRule":
        '''function to build Rule Expression for given IAlarm and AlarmState.

        :param alarm: IAlarm to be used in Rule Expression.
        :param alarm_state: AlarmState to be used in Rule Expression.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7dd0ffc30f4ddc0cb0621fdae0fe1af07770e9fd504527c4df1f6e9ed2032cc)
            check_type(argname="argument alarm", value=alarm, expected_type=type_hints["alarm"])
            check_type(argname="argument alarm_state", value=alarm_state, expected_type=type_hints["alarm_state"])
        return typing.cast("IAlarmRule", jsii.sinvoke(cls, "fromAlarm", [alarm, alarm_state]))

    @jsii.member(jsii_name="fromBoolean")
    @builtins.classmethod
    def from_boolean(cls, value: builtins.bool) -> "IAlarmRule":
        '''function to build TRUE/FALSE intent for Rule Expression.

        :param value: boolean value to be used in rule expression.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4a2328411f3cd1f101e6ec1cb8b2e99fc902ce06552b8b213d9cab093ad51cc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast("IAlarmRule", jsii.sinvoke(cls, "fromBoolean", [value]))

    @jsii.member(jsii_name="fromString")
    @builtins.classmethod
    def from_string(cls, alarm_rule: builtins.str) -> "IAlarmRule":
        '''function to build Rule Expression for given Alarm Rule string.

        :param alarm_rule: string to be used in Rule Expression.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ab510b22518be75f8aa37082e6a3eb8a0352f4b78b509de75bac3e2651e7909)
            check_type(argname="argument alarm_rule", value=alarm_rule, expected_type=type_hints["alarm_rule"])
        return typing.cast("IAlarmRule", jsii.sinvoke(cls, "fromString", [alarm_rule]))

    @jsii.member(jsii_name="not")
    @builtins.classmethod
    def not_(cls, operand: "IAlarmRule") -> "IAlarmRule":
        '''function to wrap provided AlarmRule in NOT operator.

        :param operand: IAlarmRule to be wrapped in NOT operator.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__130f148217f9842e34a2de59608585cc9ab66211fa42610aa323425b1f214b0a)
            check_type(argname="argument operand", value=operand, expected_type=type_hints["operand"])
        return typing.cast("IAlarmRule", jsii.sinvoke(cls, "not", [operand]))


@jsii.enum(jsii_type="aws-cdk-lib.aws_cloudwatch.AlarmState")
class AlarmState(enum.Enum):
    '''Enumeration indicates state of Alarm used in building Alarm Rule.

    :exampleMetadata: infused

    Example::

        # dashboard: cloudwatch.Dashboard
        # error_alarm: cloudwatch.Alarm
        
        
        dashboard.add_widgets(cloudwatch.AlarmStatusWidget(
            title="Errors",
            alarms=[error_alarm],
            sort_by=cloudwatch.AlarmStatusWidgetSortBy.STATE_UPDATED_TIMESTAMP,
            states=[cloudwatch.AlarmState.ALARM]
        ))
    '''

    ALARM = "ALARM"
    '''State indicates resource is in ALARM.'''
    OK = "OK"
    '''State indicates resource is not in ALARM.'''
    INSUFFICIENT_DATA = "INSUFFICIENT_DATA"
    '''State indicates there is not enough data to determine is resource is in ALARM.'''


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudwatch.AlarmStatusWidgetProps",
    jsii_struct_bases=[],
    name_mapping={
        "alarms": "alarms",
        "height": "height",
        "sort_by": "sortBy",
        "states": "states",
        "title": "title",
        "width": "width",
    },
)
class AlarmStatusWidgetProps:
    def __init__(
        self,
        *,
        alarms: typing.Sequence["IAlarm"],
        height: typing.Optional[jsii.Number] = None,
        sort_by: typing.Optional["AlarmStatusWidgetSortBy"] = None,
        states: typing.Optional[typing.Sequence[AlarmState]] = None,
        title: typing.Optional[builtins.str] = None,
        width: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Properties for an Alarm Status Widget.

        :param alarms: CloudWatch Alarms to show in widget.
        :param height: Height of the widget. Default: 3
        :param sort_by: Specifies how to sort the alarms in the widget. Default: - alphabetical order
        :param states: Use this field to filter the list of alarms displayed in the widget to only those alarms currently in the specified states. You can specify one or more alarm states in the value for this field. The alarm states that you can specify are ALARM, INSUFFICIENT_DATA, and OK. If you omit this field or specify an empty array, all the alarms specifed in alarms are displayed. Default: - all the alarms specified in alarms are displayed.
        :param title: The title of the widget. Default: 'Alarm Status'
        :param width: Width of the widget, in a grid of 24 units wide. Default: 6

        :exampleMetadata: infused

        Example::

            # dashboard: cloudwatch.Dashboard
            # error_alarm: cloudwatch.Alarm
            
            
            dashboard.add_widgets(
                cloudwatch.AlarmStatusWidget(
                    alarms=[error_alarm]
                ))
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b487d6400a85492ffe968131ec5a7294320f90cef90f0505f02beffc7d3055a1)
            check_type(argname="argument alarms", value=alarms, expected_type=type_hints["alarms"])
            check_type(argname="argument height", value=height, expected_type=type_hints["height"])
            check_type(argname="argument sort_by", value=sort_by, expected_type=type_hints["sort_by"])
            check_type(argname="argument states", value=states, expected_type=type_hints["states"])
            check_type(argname="argument title", value=title, expected_type=type_hints["title"])
            check_type(argname="argument width", value=width, expected_type=type_hints["width"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "alarms": alarms,
        }
        if height is not None:
            self._values["height"] = height
        if sort_by is not None:
            self._values["sort_by"] = sort_by
        if states is not None:
            self._values["states"] = states
        if title is not None:
            self._values["title"] = title
        if width is not None:
            self._values["width"] = width

    @builtins.property
    def alarms(self) -> typing.List["IAlarm"]:
        '''CloudWatch Alarms to show in widget.'''
        result = self._values.get("alarms")
        assert result is not None, "Required property 'alarms' is missing"
        return typing.cast(typing.List["IAlarm"], result)

    @builtins.property
    def height(self) -> typing.Optional[jsii.Number]:
        '''Height of the widget.

        :default: 3
        '''
        result = self._values.get("height")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def sort_by(self) -> typing.Optional["AlarmStatusWidgetSortBy"]:
        '''Specifies how to sort the alarms in the widget.

        :default: - alphabetical order
        '''
        result = self._values.get("sort_by")
        return typing.cast(typing.Optional["AlarmStatusWidgetSortBy"], result)

    @builtins.property
    def states(self) -> typing.Optional[typing.List[AlarmState]]:
        '''Use this field to filter the list of alarms displayed in the widget to only those alarms currently in the specified states.

        You can specify one or more alarm states in the value for this field.
        The alarm states that you can specify are ALARM, INSUFFICIENT_DATA, and OK.

        If you omit this field or specify an empty array, all the alarms specifed in alarms are displayed.

        :default: - all the alarms specified in alarms are displayed.
        '''
        result = self._values.get("states")
        return typing.cast(typing.Optional[typing.List[AlarmState]], result)

    @builtins.property
    def title(self) -> typing.Optional[builtins.str]:
        '''The title of the widget.

        :default: 'Alarm Status'
        '''
        result = self._values.get("title")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def width(self) -> typing.Optional[jsii.Number]:
        '''Width of the widget, in a grid of 24 units wide.

        :default: 6
        '''
        result = self._values.get("width")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AlarmStatusWidgetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_cloudwatch.AlarmStatusWidgetSortBy")
class AlarmStatusWidgetSortBy(enum.Enum):
    '''The sort possibilities for AlarmStatusWidgets.

    :exampleMetadata: infused

    Example::

        # dashboard: cloudwatch.Dashboard
        # error_alarm: cloudwatch.Alarm
        
        
        dashboard.add_widgets(cloudwatch.AlarmStatusWidget(
            title="Errors",
            alarms=[error_alarm],
            sort_by=cloudwatch.AlarmStatusWidgetSortBy.STATE_UPDATED_TIMESTAMP,
            states=[cloudwatch.AlarmState.ALARM]
        ))
    '''

    DEFAULT = "DEFAULT"
    '''Choose DEFAULT to sort them in alphabetical order by alarm name.'''
    STATE_UPDATED_TIMESTAMP = "STATE_UPDATED_TIMESTAMP"
    '''Choose STATE_UPDATED_TIMESTAMP to sort them first by alarm state, with alarms in ALARM state first, INSUFFICIENT_DATA alarms next, and OK alarms last.

    Within each group, the alarms are sorted by when they last changed state, with more recent state changes listed first.
    '''
    TIMESTAMP = "TIMESTAMP"
    '''Choose TIMESTAMP to sort them by the time when the alarms most recently changed state, no matter the current alarm state.

    The alarm that changed state most recently is listed first.
    '''


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnAlarm(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudwatch.CfnAlarm",
):
    '''The ``AWS::CloudWatch::Alarm`` type specifies an alarm and associates it with the specified metric or metric math expression.

    When this operation creates an alarm, the alarm state is immediately set to ``INSUFFICIENT_DATA`` . The alarm is then evaluated and its state is set appropriately. Any actions associated with the new state are then executed.

    When you update an existing alarm, its state is left unchanged, but the update completely overwrites the previous configuration of the alarm.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-alarm.html
    :cloudformationResource: AWS::CloudWatch::Alarm
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_cloudwatch as cloudwatch
        
        cfn_alarm = cloudwatch.CfnAlarm(self, "MyCfnAlarm",
            comparison_operator="comparisonOperator",
            evaluation_periods=123,
        
            # the properties below are optional
            actions_enabled=False,
            alarm_actions=["alarmActions"],
            alarm_description="alarmDescription",
            alarm_name="alarmName",
            datapoints_to_alarm=123,
            dimensions=[cloudwatch.CfnAlarm.DimensionProperty(
                name="name",
                value="value"
            )],
            evaluate_low_sample_count_percentile="evaluateLowSampleCountPercentile",
            extended_statistic="extendedStatistic",
            insufficient_data_actions=["insufficientDataActions"],
            metric_name="metricName",
            metrics=[cloudwatch.CfnAlarm.MetricDataQueryProperty(
                id="id",
        
                # the properties below are optional
                account_id="accountId",
                expression="expression",
                label="label",
                metric_stat=cloudwatch.CfnAlarm.MetricStatProperty(
                    metric=cloudwatch.CfnAlarm.MetricProperty(
                        dimensions=[cloudwatch.CfnAlarm.DimensionProperty(
                            name="name",
                            value="value"
                        )],
                        metric_name="metricName",
                        namespace="namespace"
                    ),
                    period=123,
                    stat="stat",
        
                    # the properties below are optional
                    unit="unit"
                ),
                period=123,
                return_data=False
            )],
            namespace="namespace",
            ok_actions=["okActions"],
            period=123,
            statistic="statistic",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            threshold=123,
            threshold_metric_id="thresholdMetricId",
            treat_missing_data="treatMissingData",
            unit="unit"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        comparison_operator: builtins.str,
        evaluation_periods: jsii.Number,
        actions_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        alarm_actions: typing.Optional[typing.Sequence[builtins.str]] = None,
        alarm_description: typing.Optional[builtins.str] = None,
        alarm_name: typing.Optional[builtins.str] = None,
        datapoints_to_alarm: typing.Optional[jsii.Number] = None,
        dimensions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAlarm.DimensionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        evaluate_low_sample_count_percentile: typing.Optional[builtins.str] = None,
        extended_statistic: typing.Optional[builtins.str] = None,
        insufficient_data_actions: typing.Optional[typing.Sequence[builtins.str]] = None,
        metric_name: typing.Optional[builtins.str] = None,
        metrics: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAlarm.MetricDataQueryProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        namespace: typing.Optional[builtins.str] = None,
        ok_actions: typing.Optional[typing.Sequence[builtins.str]] = None,
        period: typing.Optional[jsii.Number] = None,
        statistic: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        threshold: typing.Optional[jsii.Number] = None,
        threshold_metric_id: typing.Optional[builtins.str] = None,
        treat_missing_data: typing.Optional[builtins.str] = None,
        unit: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param comparison_operator: The arithmetic operation to use when comparing the specified statistic and threshold. The specified statistic value is used as the first operand.
        :param evaluation_periods: The number of periods over which data is compared to the specified threshold. If you are setting an alarm that requires that a number of consecutive data points be breaching to trigger the alarm, this value specifies that number. If you are setting an "M out of N" alarm, this value is the N, and ``DatapointsToAlarm`` is the M. For more information, see `Evaluating an Alarm <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#alarm-evaluation>`_ in the *Amazon CloudWatch User Guide* .
        :param actions_enabled: Indicates whether actions should be executed during any changes to the alarm state. The default is TRUE. Default: - true
        :param alarm_actions: The list of actions to execute when this alarm transitions into an ALARM state from any other state. Specify each action as an Amazon Resource Name (ARN). For more information about creating alarms and the actions that you can specify, see `PutMetricAlarm <https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutMetricAlarm.html>`_ in the *Amazon CloudWatch API Reference* .
        :param alarm_description: The description of the alarm.
        :param alarm_name: The name of the alarm. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the alarm name. .. epigraph:: If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.
        :param datapoints_to_alarm: The number of datapoints that must be breaching to trigger the alarm. This is used only if you are setting an "M out of N" alarm. In that case, this value is the M, and the value that you set for ``EvaluationPeriods`` is the N value. For more information, see `Evaluating an Alarm <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#alarm-evaluation>`_ in the *Amazon CloudWatch User Guide* . If you omit this parameter, CloudWatch uses the same value here that you set for ``EvaluationPeriods`` , and the alarm goes to alarm state if that many consecutive periods are breaching.
        :param dimensions: The dimensions for the metric associated with the alarm. For an alarm based on a math expression, you can't specify ``Dimensions`` . Instead, you use ``Metrics`` .
        :param evaluate_low_sample_count_percentile: Used only for alarms based on percentiles. If ``ignore`` , the alarm state does not change during periods with too few data points to be statistically significant. If ``evaluate`` or this parameter is not used, the alarm is always evaluated and possibly changes state no matter how many data points are available.
        :param extended_statistic: The percentile statistic for the metric associated with the alarm. Specify a value between p0.0 and p100. For an alarm based on a metric, you must specify either ``Statistic`` or ``ExtendedStatistic`` but not both. For an alarm based on a math expression, you can't specify ``ExtendedStatistic`` . Instead, you use ``Metrics`` .
        :param insufficient_data_actions: The actions to execute when this alarm transitions to the ``INSUFFICIENT_DATA`` state from any other state. Each action is specified as an Amazon Resource Name (ARN).
        :param metric_name: The name of the metric associated with the alarm. This is required for an alarm based on a metric. For an alarm based on a math expression, you use ``Metrics`` instead and you can't specify ``MetricName`` .
        :param metrics: An array that enables you to create an alarm based on the result of a metric math expression. Each item in the array either retrieves a metric or performs a math expression. If you specify the ``Metrics`` parameter, you cannot specify ``MetricName`` , ``Dimensions`` , ``Period`` , ``Namespace`` , ``Statistic`` , ``ExtendedStatistic`` , or ``Unit`` .
        :param namespace: The namespace of the metric associated with the alarm. This is required for an alarm based on a metric. For an alarm based on a math expression, you can't specify ``Namespace`` and you use ``Metrics`` instead. For a list of namespaces for metrics from AWS services, see `AWS Services That Publish CloudWatch Metrics. <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/aws-services-cloudwatch-metrics.html>`_
        :param ok_actions: The actions to execute when this alarm transitions to the ``OK`` state from any other state. Each action is specified as an Amazon Resource Name (ARN).
        :param period: The period, in seconds, over which the statistic is applied. This is required for an alarm based on a metric. Valid values are 10, 30, 60, and any multiple of 60. For an alarm based on a math expression, you can't specify ``Period`` , and instead you use the ``Metrics`` parameter. *Minimum:* 10
        :param statistic: The statistic for the metric associated with the alarm, other than percentile. For percentile statistics, use ``ExtendedStatistic`` . For an alarm based on a metric, you must specify either ``Statistic`` or ``ExtendedStatistic`` but not both. For an alarm based on a math expression, you can't specify ``Statistic`` . Instead, you use ``Metrics`` .
        :param tags: A list of key-value pairs to associate with the alarm. You can associate as many as 50 tags with an alarm. To be able to associate tags with the alarm when you create the alarm, you must have the ``cloudwatch:TagResource`` permission. Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.
        :param threshold: The value to compare with the specified statistic.
        :param threshold_metric_id: In an alarm based on an anomaly detection model, this is the ID of the ``ANOMALY_DETECTION_BAND`` function used as the threshold for the alarm.
        :param treat_missing_data: Sets how this alarm is to handle missing data points. Valid values are ``breaching`` , ``notBreaching`` , ``ignore`` , and ``missing`` . For more information, see `Configuring How CloudWatch Alarms Treat Missing Data <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#alarms-and-missing-data>`_ in the *Amazon CloudWatch User Guide* . If you omit this parameter, the default behavior of ``missing`` is used.
        :param unit: The unit of the metric associated with the alarm. Specify this only if you are creating an alarm based on a single metric. Do not specify this if you are specifying a ``Metrics`` array. You can specify the following values: Seconds, Microseconds, Milliseconds, Bytes, Kilobytes, Megabytes, Gigabytes, Terabytes, Bits, Kilobits, Megabits, Gigabits, Terabits, Percent, Count, Bytes/Second, Kilobytes/Second, Megabytes/Second, Gigabytes/Second, Terabytes/Second, Bits/Second, Kilobits/Second, Megabits/Second, Gigabits/Second, Terabits/Second, Count/Second, or None.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5adc477b9cef758736625389f1a51dec08eb7b348be35f42b0e37d6d4d1f1b68)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAlarmProps(
            comparison_operator=comparison_operator,
            evaluation_periods=evaluation_periods,
            actions_enabled=actions_enabled,
            alarm_actions=alarm_actions,
            alarm_description=alarm_description,
            alarm_name=alarm_name,
            datapoints_to_alarm=datapoints_to_alarm,
            dimensions=dimensions,
            evaluate_low_sample_count_percentile=evaluate_low_sample_count_percentile,
            extended_statistic=extended_statistic,
            insufficient_data_actions=insufficient_data_actions,
            metric_name=metric_name,
            metrics=metrics,
            namespace=namespace,
            ok_actions=ok_actions,
            period=period,
            statistic=statistic,
            tags=tags,
            threshold=threshold,
            threshold_metric_id=threshold_metric_id,
            treat_missing_data=treat_missing_data,
            unit=unit,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83bef261115d965bc301e33589e4c9b4a854da5d951fb8e2186758fba16c7f57)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a8443d72766166ac6ee22ecc2f730f3a6b9fd8414ecf17bbd95ef7e5baf82310)
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
        '''The ARN of the CloudWatch alarm, such as ``arn:aws:cloudwatch:us-west-2:123456789012:alarm:myCloudWatchAlarm-CPUAlarm-UXMMZK36R55Z`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="cdkTagManager")
    def cdk_tag_manager(self) -> _TagManager_0a598cb3:
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "cdkTagManager"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="comparisonOperator")
    def comparison_operator(self) -> builtins.str:
        '''The arithmetic operation to use when comparing the specified statistic and threshold.'''
        return typing.cast(builtins.str, jsii.get(self, "comparisonOperator"))

    @comparison_operator.setter
    def comparison_operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b70639e8f0bfbbc34ad2338567df4a5d70d17215776eb7aa3581fbe2e40cd29)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c080be98f630293bbc63f05942376d4ca0d4a15c82eb9cee4cb1c32b2740abc4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "evaluationPeriods", value)

    @builtins.property
    @jsii.member(jsii_name="actionsEnabled")
    def actions_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Indicates whether actions should be executed during any changes to the alarm state.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "actionsEnabled"))

    @actions_enabled.setter
    def actions_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__605b7067b394998a8071adbf9755ea958792836f86023d0ef23df99b8ee52bcb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "actionsEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="alarmActions")
    def alarm_actions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of actions to execute when this alarm transitions into an ALARM state from any other state.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "alarmActions"))

    @alarm_actions.setter
    def alarm_actions(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ecc41a9526c2e2c0867e81a362f65327319d216e7659dca4b3860ae75753c28a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alarmActions", value)

    @builtins.property
    @jsii.member(jsii_name="alarmDescription")
    def alarm_description(self) -> typing.Optional[builtins.str]:
        '''The description of the alarm.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alarmDescription"))

    @alarm_description.setter
    def alarm_description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae70f62af2cc75616247d133c6c848bc3a0216db1566dcd494bdbf08a99c4638)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alarmDescription", value)

    @builtins.property
    @jsii.member(jsii_name="alarmName")
    def alarm_name(self) -> typing.Optional[builtins.str]:
        '''The name of the alarm.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alarmName"))

    @alarm_name.setter
    def alarm_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23c8c04504dd76a6623e461e9b6448e0dbf5a2092e2c1aed4d8ecbff1f899de1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alarmName", value)

    @builtins.property
    @jsii.member(jsii_name="datapointsToAlarm")
    def datapoints_to_alarm(self) -> typing.Optional[jsii.Number]:
        '''The number of datapoints that must be breaching to trigger the alarm.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "datapointsToAlarm"))

    @datapoints_to_alarm.setter
    def datapoints_to_alarm(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8ecc192776c2ee14846f714a390af6c702ed6e634dd57dd26288202304a0796)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datapointsToAlarm", value)

    @builtins.property
    @jsii.member(jsii_name="dimensions")
    def dimensions(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAlarm.DimensionProperty"]]]]:
        '''The dimensions for the metric associated with the alarm.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAlarm.DimensionProperty"]]]], jsii.get(self, "dimensions"))

    @dimensions.setter
    def dimensions(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAlarm.DimensionProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6076cadb3051943abe05b65350e48c7b75b471794dd9cdc8472d1758a7b8cd4e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dimensions", value)

    @builtins.property
    @jsii.member(jsii_name="evaluateLowSampleCountPercentile")
    def evaluate_low_sample_count_percentile(self) -> typing.Optional[builtins.str]:
        '''Used only for alarms based on percentiles.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "evaluateLowSampleCountPercentile"))

    @evaluate_low_sample_count_percentile.setter
    def evaluate_low_sample_count_percentile(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aec0314071d83d4872fc9ec8f90d1938e3aa18c267eaf43f637379b01d86c684)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "evaluateLowSampleCountPercentile", value)

    @builtins.property
    @jsii.member(jsii_name="extendedStatistic")
    def extended_statistic(self) -> typing.Optional[builtins.str]:
        '''The percentile statistic for the metric associated with the alarm.

        Specify a value between p0.0 and p100.
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "extendedStatistic"))

    @extended_statistic.setter
    def extended_statistic(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__888f8bf20de080b19a46eb68471ca6b6923449631ab8135ff7aa454a9f07b7e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "extendedStatistic", value)

    @builtins.property
    @jsii.member(jsii_name="insufficientDataActions")
    def insufficient_data_actions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The actions to execute when this alarm transitions to the ``INSUFFICIENT_DATA`` state from any other state.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "insufficientDataActions"))

    @insufficient_data_actions.setter
    def insufficient_data_actions(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5eda8d8bf828721d6f8004c5a122ff02b8cf461eca3fe5dc711411c966cf3f14)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "insufficientDataActions", value)

    @builtins.property
    @jsii.member(jsii_name="metricName")
    def metric_name(self) -> typing.Optional[builtins.str]:
        '''The name of the metric associated with the alarm.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metricName"))

    @metric_name.setter
    def metric_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71f82ca7521ace9dd7ff6c8ef3a9d77edf1d69fcd526f9d5535ff804be3e3d3f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricName", value)

    @builtins.property
    @jsii.member(jsii_name="metrics")
    def metrics(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAlarm.MetricDataQueryProperty"]]]]:
        '''An array that enables you to create an alarm based on the result of a metric math expression.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAlarm.MetricDataQueryProperty"]]]], jsii.get(self, "metrics"))

    @metrics.setter
    def metrics(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAlarm.MetricDataQueryProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13ee627a7bc97218488ea85296e024a4aa67101fe00623848363348c246cc493)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metrics", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> typing.Optional[builtins.str]:
        '''The namespace of the metric associated with the alarm.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c788f613b67dd11d2bae1b2a09b80da6e70c30f1037ed4dad770b721c5a5fc9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="okActions")
    def ok_actions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The actions to execute when this alarm transitions to the ``OK`` state from any other state.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "okActions"))

    @ok_actions.setter
    def ok_actions(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e122d784f2d44eb64ddfad9117d6763bb7f170c7d3e0dc4a96dc353d55ac374d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "okActions", value)

    @builtins.property
    @jsii.member(jsii_name="period")
    def period(self) -> typing.Optional[jsii.Number]:
        '''The period, in seconds, over which the statistic is applied.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "period"))

    @period.setter
    def period(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__628a5231423fe29bcf97062014bb2e10fb13ab9ea4e1008de39270a9520ab6a4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "period", value)

    @builtins.property
    @jsii.member(jsii_name="statistic")
    def statistic(self) -> typing.Optional[builtins.str]:
        '''The statistic for the metric associated with the alarm, other than percentile.

        For percentile statistics, use ``ExtendedStatistic`` .
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statistic"))

    @statistic.setter
    def statistic(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__233ab7996f3717f1bae1d0b9c6063cfa83de67875ac91777906dbd68693e81a3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "statistic", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of key-value pairs to associate with the alarm.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__895712e62b896ed30b8848bddfdb970fd334934c19393e2eb8ad06392ecf8af9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="threshold")
    def threshold(self) -> typing.Optional[jsii.Number]:
        '''The value to compare with the specified statistic.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "threshold"))

    @threshold.setter
    def threshold(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5fbcb41a59e8a1cba566cf0b26b3129b32d1bb58de6d5fcb5045e9d2ddf908de)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "threshold", value)

    @builtins.property
    @jsii.member(jsii_name="thresholdMetricId")
    def threshold_metric_id(self) -> typing.Optional[builtins.str]:
        '''In an alarm based on an anomaly detection model, this is the ID of the ``ANOMALY_DETECTION_BAND`` function used as the threshold for the alarm.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "thresholdMetricId"))

    @threshold_metric_id.setter
    def threshold_metric_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0dea69dd6b9252440a0712cbe34f23c9bf1cc751d0b8326af6517cd05d511fc3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "thresholdMetricId", value)

    @builtins.property
    @jsii.member(jsii_name="treatMissingData")
    def treat_missing_data(self) -> typing.Optional[builtins.str]:
        '''Sets how this alarm is to handle missing data points.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "treatMissingData"))

    @treat_missing_data.setter
    def treat_missing_data(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__daed33fabd0003672d13ed63fe7c6c290e186f469fb0feb75842f06ec413f25a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "treatMissingData", value)

    @builtins.property
    @jsii.member(jsii_name="unit")
    def unit(self) -> typing.Optional[builtins.str]:
        '''The unit of the metric associated with the alarm.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "unit"))

    @unit.setter
    def unit(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c2311746224e8eb79c889c7ea604776c607667cdabb1ca67c2b7b269c33749d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unit", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cloudwatch.CfnAlarm.DimensionProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "value": "value"},
    )
    class DimensionProperty:
        def __init__(self, *, name: builtins.str, value: builtins.str) -> None:
            '''Dimension is an embedded property of the ``AWS::CloudWatch::Alarm`` type.

            Dimensions are name/value pairs that can be associated with a CloudWatch metric. You can specify a maximum of 10 dimensions for a given metric.

            :param name: The name of the dimension, from 1–255 characters in length. This dimension name must have been included when the metric was published.
            :param value: The value for the dimension, from 1–255 characters in length.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-dimension.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cloudwatch as cloudwatch
                
                dimension_property = cloudwatch.CfnAlarm.DimensionProperty(
                    name="name",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__caa951097684de7785a360ff0dd7dd52b38193dd6abedc429031dbeef388a48b)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
                "value": value,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the dimension, from 1–255 characters in length.

            This dimension name must have been included when the metric was published.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-dimension.html#cfn-cloudwatch-alarm-dimension-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''The value for the dimension, from 1–255 characters in length.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-dimension.html#cfn-cloudwatch-alarm-dimension-value
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
        jsii_type="aws-cdk-lib.aws_cloudwatch.CfnAlarm.MetricDataQueryProperty",
        jsii_struct_bases=[],
        name_mapping={
            "id": "id",
            "account_id": "accountId",
            "expression": "expression",
            "label": "label",
            "metric_stat": "metricStat",
            "period": "period",
            "return_data": "returnData",
        },
    )
    class MetricDataQueryProperty:
        def __init__(
            self,
            *,
            id: builtins.str,
            account_id: typing.Optional[builtins.str] = None,
            expression: typing.Optional[builtins.str] = None,
            label: typing.Optional[builtins.str] = None,
            metric_stat: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAlarm.MetricStatProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            period: typing.Optional[jsii.Number] = None,
            return_data: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''The ``MetricDataQuery`` property type specifies the metric data to return, and whether this call is just retrieving a batch set of data for one metric, or is performing a math expression on metric data.

            Any expression used must return a single time series. For more information, see `Metric Math Syntax and Functions <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html#metric-math-syntax>`_ in the *Amazon CloudWatch User Guide* .

            :param id: A short name used to tie this object to the results in the response. This name must be unique within a single call to ``GetMetricData`` . If you are performing math expressions on this set of data, this name represents that data and can serve as a variable in the mathematical expression. The valid characters are letters, numbers, and underscore. The first character must be a lowercase letter.
            :param account_id: The ID of the account where the metrics are located, if this is a cross-account alarm.
            :param expression: The math expression to be performed on the returned data, if this object is performing a math expression. This expression can use the ``Id`` of the other metrics to refer to those metrics, and can also use the ``Id`` of other expressions to use the result of those expressions. For more information about metric math expressions, see `Metric Math Syntax and Functions <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html#metric-math-syntax>`_ in the *Amazon CloudWatch User Guide* . Within each MetricDataQuery object, you must specify either ``Expression`` or ``MetricStat`` but not both.
            :param label: A human-readable label for this metric or expression. This is especially useful if this is an expression, so that you know what the value represents. If the metric or expression is shown in a CloudWatch dashboard widget, the label is shown. If ``Label`` is omitted, CloudWatch generates a default.
            :param metric_stat: The metric to be returned, along with statistics, period, and units. Use this parameter only if this object is retrieving a metric and not performing a math expression on returned data. Within one MetricDataQuery object, you must specify either ``Expression`` or ``MetricStat`` but not both.
            :param period: The granularity, in seconds, of the returned data points. For metrics with regular resolution, a period can be as short as one minute (60 seconds) and must be a multiple of 60. For high-resolution metrics that are collected at intervals of less than one minute, the period can be 1, 5, 10, 30, 60, or any multiple of 60. High-resolution metrics are those metrics stored by a ``PutMetricData`` operation that includes a ``StorageResolution of 1 second`` .
            :param return_data: This option indicates whether to return the timestamps and raw data values of this metric. When you create an alarm based on a metric math expression, specify ``True`` for this value for only the one math expression that the alarm is based on. You must specify ``False`` for ``ReturnData`` for all the other metrics and expressions used in the alarm. This field is required.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metricdataquery.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cloudwatch as cloudwatch
                
                metric_data_query_property = cloudwatch.CfnAlarm.MetricDataQueryProperty(
                    id="id",
                
                    # the properties below are optional
                    account_id="accountId",
                    expression="expression",
                    label="label",
                    metric_stat=cloudwatch.CfnAlarm.MetricStatProperty(
                        metric=cloudwatch.CfnAlarm.MetricProperty(
                            dimensions=[cloudwatch.CfnAlarm.DimensionProperty(
                                name="name",
                                value="value"
                            )],
                            metric_name="metricName",
                            namespace="namespace"
                        ),
                        period=123,
                        stat="stat",
                
                        # the properties below are optional
                        unit="unit"
                    ),
                    period=123,
                    return_data=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__44202067ada87cd47b3af31a51714a781d59c3a94ffe7a34b1e426ddaa87372f)
                check_type(argname="argument id", value=id, expected_type=type_hints["id"])
                check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
                check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
                check_type(argname="argument label", value=label, expected_type=type_hints["label"])
                check_type(argname="argument metric_stat", value=metric_stat, expected_type=type_hints["metric_stat"])
                check_type(argname="argument period", value=period, expected_type=type_hints["period"])
                check_type(argname="argument return_data", value=return_data, expected_type=type_hints["return_data"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "id": id,
            }
            if account_id is not None:
                self._values["account_id"] = account_id
            if expression is not None:
                self._values["expression"] = expression
            if label is not None:
                self._values["label"] = label
            if metric_stat is not None:
                self._values["metric_stat"] = metric_stat
            if period is not None:
                self._values["period"] = period
            if return_data is not None:
                self._values["return_data"] = return_data

        @builtins.property
        def id(self) -> builtins.str:
            '''A short name used to tie this object to the results in the response.

            This name must be unique within a single call to ``GetMetricData`` . If you are performing math expressions on this set of data, this name represents that data and can serve as a variable in the mathematical expression. The valid characters are letters, numbers, and underscore. The first character must be a lowercase letter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metricdataquery.html#cfn-cloudwatch-alarm-metricdataquery-id
            '''
            result = self._values.get("id")
            assert result is not None, "Required property 'id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def account_id(self) -> typing.Optional[builtins.str]:
            '''The ID of the account where the metrics are located, if this is a cross-account alarm.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metricdataquery.html#cfn-cloudwatch-alarm-metricdataquery-accountid
            '''
            result = self._values.get("account_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def expression(self) -> typing.Optional[builtins.str]:
            '''The math expression to be performed on the returned data, if this object is performing a math expression.

            This expression can use the ``Id`` of the other metrics to refer to those metrics, and can also use the ``Id`` of other expressions to use the result of those expressions. For more information about metric math expressions, see `Metric Math Syntax and Functions <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html#metric-math-syntax>`_ in the *Amazon CloudWatch User Guide* .

            Within each MetricDataQuery object, you must specify either ``Expression`` or ``MetricStat`` but not both.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metricdataquery.html#cfn-cloudwatch-alarm-metricdataquery-expression
            '''
            result = self._values.get("expression")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def label(self) -> typing.Optional[builtins.str]:
            '''A human-readable label for this metric or expression.

            This is especially useful if this is an expression, so that you know what the value represents. If the metric or expression is shown in a CloudWatch dashboard widget, the label is shown. If ``Label`` is omitted, CloudWatch generates a default.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metricdataquery.html#cfn-cloudwatch-alarm-metricdataquery-label
            '''
            result = self._values.get("label")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def metric_stat(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAlarm.MetricStatProperty"]]:
            '''The metric to be returned, along with statistics, period, and units.

            Use this parameter only if this object is retrieving a metric and not performing a math expression on returned data.

            Within one MetricDataQuery object, you must specify either ``Expression`` or ``MetricStat`` but not both.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metricdataquery.html#cfn-cloudwatch-alarm-metricdataquery-metricstat
            '''
            result = self._values.get("metric_stat")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAlarm.MetricStatProperty"]], result)

        @builtins.property
        def period(self) -> typing.Optional[jsii.Number]:
            '''The granularity, in seconds, of the returned data points.

            For metrics with regular resolution, a period can be as short as one minute (60 seconds) and must be a multiple of 60. For high-resolution metrics that are collected at intervals of less than one minute, the period can be 1, 5, 10, 30, 60, or any multiple of 60. High-resolution metrics are those metrics stored by a ``PutMetricData`` operation that includes a ``StorageResolution of 1 second`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metricdataquery.html#cfn-cloudwatch-alarm-metricdataquery-period
            '''
            result = self._values.get("period")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def return_data(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''This option indicates whether to return the timestamps and raw data values of this metric.

            When you create an alarm based on a metric math expression, specify ``True`` for this value for only the one math expression that the alarm is based on. You must specify ``False`` for ``ReturnData`` for all the other metrics and expressions used in the alarm.

            This field is required.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metricdataquery.html#cfn-cloudwatch-alarm-metricdataquery-returndata
            '''
            result = self._values.get("return_data")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MetricDataQueryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cloudwatch.CfnAlarm.MetricProperty",
        jsii_struct_bases=[],
        name_mapping={
            "dimensions": "dimensions",
            "metric_name": "metricName",
            "namespace": "namespace",
        },
    )
    class MetricProperty:
        def __init__(
            self,
            *,
            dimensions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAlarm.DimensionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            metric_name: typing.Optional[builtins.str] = None,
            namespace: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ``Metric`` property type represents a specific metric.

            ``Metric`` is a property of the `MetricStat <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metricstat.html>`_ property type.

            :param dimensions: The metric dimensions that you want to be used for the metric that the alarm will watch.
            :param metric_name: The name of the metric that you want the alarm to watch. This is a required field.
            :param namespace: The namespace of the metric that the alarm will watch.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metric.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cloudwatch as cloudwatch
                
                metric_property = cloudwatch.CfnAlarm.MetricProperty(
                    dimensions=[cloudwatch.CfnAlarm.DimensionProperty(
                        name="name",
                        value="value"
                    )],
                    metric_name="metricName",
                    namespace="namespace"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f25dbc8a0f576b492c27e93b80f26a025e8007e3b69752a846bae6af97ce55cf)
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
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAlarm.DimensionProperty"]]]]:
            '''The metric dimensions that you want to be used for the metric that the alarm will watch.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metric.html#cfn-cloudwatch-alarm-metric-dimensions
            '''
            result = self._values.get("dimensions")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAlarm.DimensionProperty"]]]], result)

        @builtins.property
        def metric_name(self) -> typing.Optional[builtins.str]:
            '''The name of the metric that you want the alarm to watch.

            This is a required field.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metric.html#cfn-cloudwatch-alarm-metric-metricname
            '''
            result = self._values.get("metric_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def namespace(self) -> typing.Optional[builtins.str]:
            '''The namespace of the metric that the alarm will watch.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metric.html#cfn-cloudwatch-alarm-metric-namespace
            '''
            result = self._values.get("namespace")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MetricProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cloudwatch.CfnAlarm.MetricStatProperty",
        jsii_struct_bases=[],
        name_mapping={
            "metric": "metric",
            "period": "period",
            "stat": "stat",
            "unit": "unit",
        },
    )
    class MetricStatProperty:
        def __init__(
            self,
            *,
            metric: typing.Union[_IResolvable_da3f097b, typing.Union["CfnAlarm.MetricProperty", typing.Dict[builtins.str, typing.Any]]],
            period: jsii.Number,
            stat: builtins.str,
            unit: typing.Optional[builtins.str] = None,
        ) -> None:
            '''This structure defines the metric to be returned, along with the statistics, period, and units.

            ``MetricStat`` is a property of the `MetricDataQuery <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metricdataquery.html>`_ property type.

            :param metric: The metric to return, including the metric name, namespace, and dimensions.
            :param period: The granularity, in seconds, of the returned data points. For metrics with regular resolution, a period can be as short as one minute (60 seconds) and must be a multiple of 60. For high-resolution metrics that are collected at intervals of less than one minute, the period can be 1, 5, 10, 30, 60, or any multiple of 60. High-resolution metrics are those metrics stored by a ``PutMetricData`` call that includes a ``StorageResolution`` of 1 second. If the ``StartTime`` parameter specifies a time stamp that is greater than 3 hours ago, you must specify the period as follows or no data points in that time range is returned: - Start time between 3 hours and 15 days ago - Use a multiple of 60 seconds (1 minute). - Start time between 15 and 63 days ago - Use a multiple of 300 seconds (5 minutes). - Start time greater than 63 days ago - Use a multiple of 3600 seconds (1 hour).
            :param stat: The statistic to return. It can include any CloudWatch statistic or extended statistic. For a list of valid values, see the table in `Statistics <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Statistic>`_ in the *Amazon CloudWatch User Guide* .
            :param unit: The unit to use for the returned data points. Valid values are: Seconds, Microseconds, Milliseconds, Bytes, Kilobytes, Megabytes, Gigabytes, Terabytes, Bits, Kilobits, Megabits, Gigabits, Terabits, Percent, Count, Bytes/Second, Kilobytes/Second, Megabytes/Second, Gigabytes/Second, Terabytes/Second, Bits/Second, Kilobits/Second, Megabits/Second, Gigabits/Second, Terabits/Second, Count/Second, or None.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metricstat.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cloudwatch as cloudwatch
                
                metric_stat_property = cloudwatch.CfnAlarm.MetricStatProperty(
                    metric=cloudwatch.CfnAlarm.MetricProperty(
                        dimensions=[cloudwatch.CfnAlarm.DimensionProperty(
                            name="name",
                            value="value"
                        )],
                        metric_name="metricName",
                        namespace="namespace"
                    ),
                    period=123,
                    stat="stat",
                
                    # the properties below are optional
                    unit="unit"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1dccb5e7c21aab3526dfa08bb25fc1fac8540f50228147e0db89d426f59d20fe)
                check_type(argname="argument metric", value=metric, expected_type=type_hints["metric"])
                check_type(argname="argument period", value=period, expected_type=type_hints["period"])
                check_type(argname="argument stat", value=stat, expected_type=type_hints["stat"])
                check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "metric": metric,
                "period": period,
                "stat": stat,
            }
            if unit is not None:
                self._values["unit"] = unit

        @builtins.property
        def metric(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnAlarm.MetricProperty"]:
            '''The metric to return, including the metric name, namespace, and dimensions.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metricstat.html#cfn-cloudwatch-alarm-metricstat-metric
            '''
            result = self._values.get("metric")
            assert result is not None, "Required property 'metric' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnAlarm.MetricProperty"], result)

        @builtins.property
        def period(self) -> jsii.Number:
            '''The granularity, in seconds, of the returned data points.

            For metrics with regular resolution, a period can be as short as one minute (60 seconds) and must be a multiple of 60. For high-resolution metrics that are collected at intervals of less than one minute, the period can be 1, 5, 10, 30, 60, or any multiple of 60. High-resolution metrics are those metrics stored by a ``PutMetricData`` call that includes a ``StorageResolution`` of 1 second.

            If the ``StartTime`` parameter specifies a time stamp that is greater than 3 hours ago, you must specify the period as follows or no data points in that time range is returned:

            - Start time between 3 hours and 15 days ago - Use a multiple of 60 seconds (1 minute).
            - Start time between 15 and 63 days ago - Use a multiple of 300 seconds (5 minutes).
            - Start time greater than 63 days ago - Use a multiple of 3600 seconds (1 hour).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metricstat.html#cfn-cloudwatch-alarm-metricstat-period
            '''
            result = self._values.get("period")
            assert result is not None, "Required property 'period' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def stat(self) -> builtins.str:
            '''The statistic to return.

            It can include any CloudWatch statistic or extended statistic. For a list of valid values, see the table in `Statistics <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Statistic>`_ in the *Amazon CloudWatch User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metricstat.html#cfn-cloudwatch-alarm-metricstat-stat
            '''
            result = self._values.get("stat")
            assert result is not None, "Required property 'stat' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def unit(self) -> typing.Optional[builtins.str]:
            '''The unit to use for the returned data points.

            Valid values are: Seconds, Microseconds, Milliseconds, Bytes, Kilobytes, Megabytes, Gigabytes, Terabytes, Bits, Kilobits, Megabits, Gigabits, Terabits, Percent, Count, Bytes/Second, Kilobytes/Second, Megabytes/Second, Gigabytes/Second, Terabytes/Second, Bits/Second, Kilobits/Second, Megabits/Second, Gigabits/Second, Terabits/Second, Count/Second, or None.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-metricstat.html#cfn-cloudwatch-alarm-metricstat-unit
            '''
            result = self._values.get("unit")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MetricStatProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudwatch.CfnAlarmProps",
    jsii_struct_bases=[],
    name_mapping={
        "comparison_operator": "comparisonOperator",
        "evaluation_periods": "evaluationPeriods",
        "actions_enabled": "actionsEnabled",
        "alarm_actions": "alarmActions",
        "alarm_description": "alarmDescription",
        "alarm_name": "alarmName",
        "datapoints_to_alarm": "datapointsToAlarm",
        "dimensions": "dimensions",
        "evaluate_low_sample_count_percentile": "evaluateLowSampleCountPercentile",
        "extended_statistic": "extendedStatistic",
        "insufficient_data_actions": "insufficientDataActions",
        "metric_name": "metricName",
        "metrics": "metrics",
        "namespace": "namespace",
        "ok_actions": "okActions",
        "period": "period",
        "statistic": "statistic",
        "tags": "tags",
        "threshold": "threshold",
        "threshold_metric_id": "thresholdMetricId",
        "treat_missing_data": "treatMissingData",
        "unit": "unit",
    },
)
class CfnAlarmProps:
    def __init__(
        self,
        *,
        comparison_operator: builtins.str,
        evaluation_periods: jsii.Number,
        actions_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        alarm_actions: typing.Optional[typing.Sequence[builtins.str]] = None,
        alarm_description: typing.Optional[builtins.str] = None,
        alarm_name: typing.Optional[builtins.str] = None,
        datapoints_to_alarm: typing.Optional[jsii.Number] = None,
        dimensions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAlarm.DimensionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        evaluate_low_sample_count_percentile: typing.Optional[builtins.str] = None,
        extended_statistic: typing.Optional[builtins.str] = None,
        insufficient_data_actions: typing.Optional[typing.Sequence[builtins.str]] = None,
        metric_name: typing.Optional[builtins.str] = None,
        metrics: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAlarm.MetricDataQueryProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        namespace: typing.Optional[builtins.str] = None,
        ok_actions: typing.Optional[typing.Sequence[builtins.str]] = None,
        period: typing.Optional[jsii.Number] = None,
        statistic: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        threshold: typing.Optional[jsii.Number] = None,
        threshold_metric_id: typing.Optional[builtins.str] = None,
        treat_missing_data: typing.Optional[builtins.str] = None,
        unit: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnAlarm``.

        :param comparison_operator: The arithmetic operation to use when comparing the specified statistic and threshold. The specified statistic value is used as the first operand.
        :param evaluation_periods: The number of periods over which data is compared to the specified threshold. If you are setting an alarm that requires that a number of consecutive data points be breaching to trigger the alarm, this value specifies that number. If you are setting an "M out of N" alarm, this value is the N, and ``DatapointsToAlarm`` is the M. For more information, see `Evaluating an Alarm <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#alarm-evaluation>`_ in the *Amazon CloudWatch User Guide* .
        :param actions_enabled: Indicates whether actions should be executed during any changes to the alarm state. The default is TRUE. Default: - true
        :param alarm_actions: The list of actions to execute when this alarm transitions into an ALARM state from any other state. Specify each action as an Amazon Resource Name (ARN). For more information about creating alarms and the actions that you can specify, see `PutMetricAlarm <https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutMetricAlarm.html>`_ in the *Amazon CloudWatch API Reference* .
        :param alarm_description: The description of the alarm.
        :param alarm_name: The name of the alarm. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the alarm name. .. epigraph:: If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.
        :param datapoints_to_alarm: The number of datapoints that must be breaching to trigger the alarm. This is used only if you are setting an "M out of N" alarm. In that case, this value is the M, and the value that you set for ``EvaluationPeriods`` is the N value. For more information, see `Evaluating an Alarm <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#alarm-evaluation>`_ in the *Amazon CloudWatch User Guide* . If you omit this parameter, CloudWatch uses the same value here that you set for ``EvaluationPeriods`` , and the alarm goes to alarm state if that many consecutive periods are breaching.
        :param dimensions: The dimensions for the metric associated with the alarm. For an alarm based on a math expression, you can't specify ``Dimensions`` . Instead, you use ``Metrics`` .
        :param evaluate_low_sample_count_percentile: Used only for alarms based on percentiles. If ``ignore`` , the alarm state does not change during periods with too few data points to be statistically significant. If ``evaluate`` or this parameter is not used, the alarm is always evaluated and possibly changes state no matter how many data points are available.
        :param extended_statistic: The percentile statistic for the metric associated with the alarm. Specify a value between p0.0 and p100. For an alarm based on a metric, you must specify either ``Statistic`` or ``ExtendedStatistic`` but not both. For an alarm based on a math expression, you can't specify ``ExtendedStatistic`` . Instead, you use ``Metrics`` .
        :param insufficient_data_actions: The actions to execute when this alarm transitions to the ``INSUFFICIENT_DATA`` state from any other state. Each action is specified as an Amazon Resource Name (ARN).
        :param metric_name: The name of the metric associated with the alarm. This is required for an alarm based on a metric. For an alarm based on a math expression, you use ``Metrics`` instead and you can't specify ``MetricName`` .
        :param metrics: An array that enables you to create an alarm based on the result of a metric math expression. Each item in the array either retrieves a metric or performs a math expression. If you specify the ``Metrics`` parameter, you cannot specify ``MetricName`` , ``Dimensions`` , ``Period`` , ``Namespace`` , ``Statistic`` , ``ExtendedStatistic`` , or ``Unit`` .
        :param namespace: The namespace of the metric associated with the alarm. This is required for an alarm based on a metric. For an alarm based on a math expression, you can't specify ``Namespace`` and you use ``Metrics`` instead. For a list of namespaces for metrics from AWS services, see `AWS Services That Publish CloudWatch Metrics. <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/aws-services-cloudwatch-metrics.html>`_
        :param ok_actions: The actions to execute when this alarm transitions to the ``OK`` state from any other state. Each action is specified as an Amazon Resource Name (ARN).
        :param period: The period, in seconds, over which the statistic is applied. This is required for an alarm based on a metric. Valid values are 10, 30, 60, and any multiple of 60. For an alarm based on a math expression, you can't specify ``Period`` , and instead you use the ``Metrics`` parameter. *Minimum:* 10
        :param statistic: The statistic for the metric associated with the alarm, other than percentile. For percentile statistics, use ``ExtendedStatistic`` . For an alarm based on a metric, you must specify either ``Statistic`` or ``ExtendedStatistic`` but not both. For an alarm based on a math expression, you can't specify ``Statistic`` . Instead, you use ``Metrics`` .
        :param tags: A list of key-value pairs to associate with the alarm. You can associate as many as 50 tags with an alarm. To be able to associate tags with the alarm when you create the alarm, you must have the ``cloudwatch:TagResource`` permission. Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.
        :param threshold: The value to compare with the specified statistic.
        :param threshold_metric_id: In an alarm based on an anomaly detection model, this is the ID of the ``ANOMALY_DETECTION_BAND`` function used as the threshold for the alarm.
        :param treat_missing_data: Sets how this alarm is to handle missing data points. Valid values are ``breaching`` , ``notBreaching`` , ``ignore`` , and ``missing`` . For more information, see `Configuring How CloudWatch Alarms Treat Missing Data <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#alarms-and-missing-data>`_ in the *Amazon CloudWatch User Guide* . If you omit this parameter, the default behavior of ``missing`` is used.
        :param unit: The unit of the metric associated with the alarm. Specify this only if you are creating an alarm based on a single metric. Do not specify this if you are specifying a ``Metrics`` array. You can specify the following values: Seconds, Microseconds, Milliseconds, Bytes, Kilobytes, Megabytes, Gigabytes, Terabytes, Bits, Kilobits, Megabits, Gigabits, Terabits, Percent, Count, Bytes/Second, Kilobytes/Second, Megabytes/Second, Gigabytes/Second, Terabytes/Second, Bits/Second, Kilobits/Second, Megabits/Second, Gigabits/Second, Terabits/Second, Count/Second, or None.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-alarm.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cloudwatch as cloudwatch
            
            cfn_alarm_props = cloudwatch.CfnAlarmProps(
                comparison_operator="comparisonOperator",
                evaluation_periods=123,
            
                # the properties below are optional
                actions_enabled=False,
                alarm_actions=["alarmActions"],
                alarm_description="alarmDescription",
                alarm_name="alarmName",
                datapoints_to_alarm=123,
                dimensions=[cloudwatch.CfnAlarm.DimensionProperty(
                    name="name",
                    value="value"
                )],
                evaluate_low_sample_count_percentile="evaluateLowSampleCountPercentile",
                extended_statistic="extendedStatistic",
                insufficient_data_actions=["insufficientDataActions"],
                metric_name="metricName",
                metrics=[cloudwatch.CfnAlarm.MetricDataQueryProperty(
                    id="id",
            
                    # the properties below are optional
                    account_id="accountId",
                    expression="expression",
                    label="label",
                    metric_stat=cloudwatch.CfnAlarm.MetricStatProperty(
                        metric=cloudwatch.CfnAlarm.MetricProperty(
                            dimensions=[cloudwatch.CfnAlarm.DimensionProperty(
                                name="name",
                                value="value"
                            )],
                            metric_name="metricName",
                            namespace="namespace"
                        ),
                        period=123,
                        stat="stat",
            
                        # the properties below are optional
                        unit="unit"
                    ),
                    period=123,
                    return_data=False
                )],
                namespace="namespace",
                ok_actions=["okActions"],
                period=123,
                statistic="statistic",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                threshold=123,
                threshold_metric_id="thresholdMetricId",
                treat_missing_data="treatMissingData",
                unit="unit"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc643fb1b5f1f1f0e0d9896a5988171163c1f79adc28d1e921bdf85f14782517)
            check_type(argname="argument comparison_operator", value=comparison_operator, expected_type=type_hints["comparison_operator"])
            check_type(argname="argument evaluation_periods", value=evaluation_periods, expected_type=type_hints["evaluation_periods"])
            check_type(argname="argument actions_enabled", value=actions_enabled, expected_type=type_hints["actions_enabled"])
            check_type(argname="argument alarm_actions", value=alarm_actions, expected_type=type_hints["alarm_actions"])
            check_type(argname="argument alarm_description", value=alarm_description, expected_type=type_hints["alarm_description"])
            check_type(argname="argument alarm_name", value=alarm_name, expected_type=type_hints["alarm_name"])
            check_type(argname="argument datapoints_to_alarm", value=datapoints_to_alarm, expected_type=type_hints["datapoints_to_alarm"])
            check_type(argname="argument dimensions", value=dimensions, expected_type=type_hints["dimensions"])
            check_type(argname="argument evaluate_low_sample_count_percentile", value=evaluate_low_sample_count_percentile, expected_type=type_hints["evaluate_low_sample_count_percentile"])
            check_type(argname="argument extended_statistic", value=extended_statistic, expected_type=type_hints["extended_statistic"])
            check_type(argname="argument insufficient_data_actions", value=insufficient_data_actions, expected_type=type_hints["insufficient_data_actions"])
            check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
            check_type(argname="argument metrics", value=metrics, expected_type=type_hints["metrics"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument ok_actions", value=ok_actions, expected_type=type_hints["ok_actions"])
            check_type(argname="argument period", value=period, expected_type=type_hints["period"])
            check_type(argname="argument statistic", value=statistic, expected_type=type_hints["statistic"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument threshold", value=threshold, expected_type=type_hints["threshold"])
            check_type(argname="argument threshold_metric_id", value=threshold_metric_id, expected_type=type_hints["threshold_metric_id"])
            check_type(argname="argument treat_missing_data", value=treat_missing_data, expected_type=type_hints["treat_missing_data"])
            check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "comparison_operator": comparison_operator,
            "evaluation_periods": evaluation_periods,
        }
        if actions_enabled is not None:
            self._values["actions_enabled"] = actions_enabled
        if alarm_actions is not None:
            self._values["alarm_actions"] = alarm_actions
        if alarm_description is not None:
            self._values["alarm_description"] = alarm_description
        if alarm_name is not None:
            self._values["alarm_name"] = alarm_name
        if datapoints_to_alarm is not None:
            self._values["datapoints_to_alarm"] = datapoints_to_alarm
        if dimensions is not None:
            self._values["dimensions"] = dimensions
        if evaluate_low_sample_count_percentile is not None:
            self._values["evaluate_low_sample_count_percentile"] = evaluate_low_sample_count_percentile
        if extended_statistic is not None:
            self._values["extended_statistic"] = extended_statistic
        if insufficient_data_actions is not None:
            self._values["insufficient_data_actions"] = insufficient_data_actions
        if metric_name is not None:
            self._values["metric_name"] = metric_name
        if metrics is not None:
            self._values["metrics"] = metrics
        if namespace is not None:
            self._values["namespace"] = namespace
        if ok_actions is not None:
            self._values["ok_actions"] = ok_actions
        if period is not None:
            self._values["period"] = period
        if statistic is not None:
            self._values["statistic"] = statistic
        if tags is not None:
            self._values["tags"] = tags
        if threshold is not None:
            self._values["threshold"] = threshold
        if threshold_metric_id is not None:
            self._values["threshold_metric_id"] = threshold_metric_id
        if treat_missing_data is not None:
            self._values["treat_missing_data"] = treat_missing_data
        if unit is not None:
            self._values["unit"] = unit

    @builtins.property
    def comparison_operator(self) -> builtins.str:
        '''The arithmetic operation to use when comparing the specified statistic and threshold.

        The specified statistic value is used as the first operand.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-alarm.html#cfn-cloudwatch-alarm-comparisonoperator
        '''
        result = self._values.get("comparison_operator")
        assert result is not None, "Required property 'comparison_operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def evaluation_periods(self) -> jsii.Number:
        '''The number of periods over which data is compared to the specified threshold.

        If you are setting an alarm that requires that a number of consecutive data points be breaching to trigger the alarm, this value specifies that number. If you are setting an "M out of N" alarm, this value is the N, and ``DatapointsToAlarm`` is the M.

        For more information, see `Evaluating an Alarm <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#alarm-evaluation>`_ in the *Amazon CloudWatch User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-alarm.html#cfn-cloudwatch-alarm-evaluationperiods
        '''
        result = self._values.get("evaluation_periods")
        assert result is not None, "Required property 'evaluation_periods' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def actions_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Indicates whether actions should be executed during any changes to the alarm state.

        The default is TRUE.

        :default: - true

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-alarm.html#cfn-cloudwatch-alarm-actionsenabled
        '''
        result = self._values.get("actions_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def alarm_actions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of actions to execute when this alarm transitions into an ALARM state from any other state.

        Specify each action as an Amazon Resource Name (ARN). For more information about creating alarms and the actions that you can specify, see `PutMetricAlarm <https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutMetricAlarm.html>`_ in the *Amazon CloudWatch API Reference* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-alarm.html#cfn-cloudwatch-alarm-alarmactions
        '''
        result = self._values.get("alarm_actions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def alarm_description(self) -> typing.Optional[builtins.str]:
        '''The description of the alarm.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-alarm.html#cfn-cloudwatch-alarm-alarmdescription
        '''
        result = self._values.get("alarm_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def alarm_name(self) -> typing.Optional[builtins.str]:
        '''The name of the alarm.

        If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the alarm name.
        .. epigraph::

           If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-alarm.html#cfn-cloudwatch-alarm-alarmname
        '''
        result = self._values.get("alarm_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def datapoints_to_alarm(self) -> typing.Optional[jsii.Number]:
        '''The number of datapoints that must be breaching to trigger the alarm.

        This is used only if you are setting an "M out of N" alarm. In that case, this value is the M, and the value that you set for ``EvaluationPeriods`` is the N value. For more information, see `Evaluating an Alarm <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#alarm-evaluation>`_ in the *Amazon CloudWatch User Guide* .

        If you omit this parameter, CloudWatch uses the same value here that you set for ``EvaluationPeriods`` , and the alarm goes to alarm state if that many consecutive periods are breaching.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-alarm.html#cfn-cloudwatch-alarm-datapointstoalarm
        '''
        result = self._values.get("datapoints_to_alarm")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def dimensions(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnAlarm.DimensionProperty]]]]:
        '''The dimensions for the metric associated with the alarm.

        For an alarm based on a math expression, you can't specify ``Dimensions`` . Instead, you use ``Metrics`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-alarm.html#cfn-cloudwatch-alarm-dimensions
        '''
        result = self._values.get("dimensions")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnAlarm.DimensionProperty]]]], result)

    @builtins.property
    def evaluate_low_sample_count_percentile(self) -> typing.Optional[builtins.str]:
        '''Used only for alarms based on percentiles.

        If ``ignore`` , the alarm state does not change during periods with too few data points to be statistically significant. If ``evaluate`` or this parameter is not used, the alarm is always evaluated and possibly changes state no matter how many data points are available.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-alarm.html#cfn-cloudwatch-alarm-evaluatelowsamplecountpercentile
        '''
        result = self._values.get("evaluate_low_sample_count_percentile")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def extended_statistic(self) -> typing.Optional[builtins.str]:
        '''The percentile statistic for the metric associated with the alarm. Specify a value between p0.0 and p100.

        For an alarm based on a metric, you must specify either ``Statistic`` or ``ExtendedStatistic`` but not both.

        For an alarm based on a math expression, you can't specify ``ExtendedStatistic`` . Instead, you use ``Metrics`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-alarm.html#cfn-cloudwatch-alarm-extendedstatistic
        '''
        result = self._values.get("extended_statistic")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def insufficient_data_actions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The actions to execute when this alarm transitions to the ``INSUFFICIENT_DATA`` state from any other state.

        Each action is specified as an Amazon Resource Name (ARN).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-alarm.html#cfn-cloudwatch-alarm-insufficientdataactions
        '''
        result = self._values.get("insufficient_data_actions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def metric_name(self) -> typing.Optional[builtins.str]:
        '''The name of the metric associated with the alarm.

        This is required for an alarm based on a metric. For an alarm based on a math expression, you use ``Metrics`` instead and you can't specify ``MetricName`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-alarm.html#cfn-cloudwatch-alarm-metricname
        '''
        result = self._values.get("metric_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def metrics(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnAlarm.MetricDataQueryProperty]]]]:
        '''An array that enables you to create an alarm based on the result of a metric math expression.

        Each item in the array either retrieves a metric or performs a math expression.

        If you specify the ``Metrics`` parameter, you cannot specify ``MetricName`` , ``Dimensions`` , ``Period`` , ``Namespace`` , ``Statistic`` , ``ExtendedStatistic`` , or ``Unit`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-alarm.html#cfn-cloudwatch-alarm-metrics
        '''
        result = self._values.get("metrics")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnAlarm.MetricDataQueryProperty]]]], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''The namespace of the metric associated with the alarm.

        This is required for an alarm based on a metric. For an alarm based on a math expression, you can't specify ``Namespace`` and you use ``Metrics`` instead.

        For a list of namespaces for metrics from AWS services, see `AWS Services That Publish CloudWatch Metrics. <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/aws-services-cloudwatch-metrics.html>`_

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-alarm.html#cfn-cloudwatch-alarm-namespace
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ok_actions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The actions to execute when this alarm transitions to the ``OK`` state from any other state.

        Each action is specified as an Amazon Resource Name (ARN).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-alarm.html#cfn-cloudwatch-alarm-okactions
        '''
        result = self._values.get("ok_actions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def period(self) -> typing.Optional[jsii.Number]:
        '''The period, in seconds, over which the statistic is applied.

        This is required for an alarm based on a metric. Valid values are 10, 30, 60, and any multiple of 60.

        For an alarm based on a math expression, you can't specify ``Period`` , and instead you use the ``Metrics`` parameter.

        *Minimum:* 10

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-alarm.html#cfn-cloudwatch-alarm-period
        '''
        result = self._values.get("period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def statistic(self) -> typing.Optional[builtins.str]:
        '''The statistic for the metric associated with the alarm, other than percentile. For percentile statistics, use ``ExtendedStatistic`` .

        For an alarm based on a metric, you must specify either ``Statistic`` or ``ExtendedStatistic`` but not both.

        For an alarm based on a math expression, you can't specify ``Statistic`` . Instead, you use ``Metrics`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-alarm.html#cfn-cloudwatch-alarm-statistic
        '''
        result = self._values.get("statistic")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of key-value pairs to associate with the alarm.

        You can associate as many as 50 tags with an alarm. To be able to associate tags with the alarm when you create the alarm, you must have the ``cloudwatch:TagResource`` permission.

        Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-alarm.html#cfn-cloudwatch-alarm-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def threshold(self) -> typing.Optional[jsii.Number]:
        '''The value to compare with the specified statistic.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-alarm.html#cfn-cloudwatch-alarm-threshold
        '''
        result = self._values.get("threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def threshold_metric_id(self) -> typing.Optional[builtins.str]:
        '''In an alarm based on an anomaly detection model, this is the ID of the ``ANOMALY_DETECTION_BAND`` function used as the threshold for the alarm.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-alarm.html#cfn-cloudwatch-alarm-thresholdmetricid
        '''
        result = self._values.get("threshold_metric_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def treat_missing_data(self) -> typing.Optional[builtins.str]:
        '''Sets how this alarm is to handle missing data points.

        Valid values are ``breaching`` , ``notBreaching`` , ``ignore`` , and ``missing`` . For more information, see `Configuring How CloudWatch Alarms Treat Missing Data <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#alarms-and-missing-data>`_ in the *Amazon CloudWatch User Guide* .

        If you omit this parameter, the default behavior of ``missing`` is used.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-alarm.html#cfn-cloudwatch-alarm-treatmissingdata
        '''
        result = self._values.get("treat_missing_data")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def unit(self) -> typing.Optional[builtins.str]:
        '''The unit of the metric associated with the alarm.

        Specify this only if you are creating an alarm based on a single metric. Do not specify this if you are specifying a ``Metrics`` array.

        You can specify the following values: Seconds, Microseconds, Milliseconds, Bytes, Kilobytes, Megabytes, Gigabytes, Terabytes, Bits, Kilobits, Megabits, Gigabits, Terabits, Percent, Count, Bytes/Second, Kilobytes/Second, Megabytes/Second, Gigabytes/Second, Terabytes/Second, Bits/Second, Kilobits/Second, Megabits/Second, Gigabits/Second, Terabits/Second, Count/Second, or None.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-alarm.html#cfn-cloudwatch-alarm-unit
        '''
        result = self._values.get("unit")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAlarmProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnAnomalyDetector(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudwatch.CfnAnomalyDetector",
):
    '''The ``AWS::CloudWatch::AnomalyDetector`` type specifies an anomaly detection band for a certain metric and statistic.

    The band represents the expected "normal" range for the metric values. Anomaly detection bands can be used for visualization of a metric's expected values, and for alarms.

    For more information see `Using CloudWatch anomaly detection. <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-anomalydetector.html
    :cloudformationResource: AWS::CloudWatch::AnomalyDetector
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_cloudwatch as cloudwatch
        
        cfn_anomaly_detector = cloudwatch.CfnAnomalyDetector(self, "MyCfnAnomalyDetector",
            configuration=cloudwatch.CfnAnomalyDetector.ConfigurationProperty(
                excluded_time_ranges=[cloudwatch.CfnAnomalyDetector.RangeProperty(
                    end_time="endTime",
                    start_time="startTime"
                )],
                metric_time_zone="metricTimeZone"
            ),
            dimensions=[cloudwatch.CfnAnomalyDetector.DimensionProperty(
                name="name",
                value="value"
            )],
            metric_characteristics=cloudwatch.CfnAnomalyDetector.MetricCharacteristicsProperty(
                periodic_spikes=False
            ),
            metric_math_anomaly_detector=cloudwatch.CfnAnomalyDetector.MetricMathAnomalyDetectorProperty(
                metric_data_queries=[cloudwatch.CfnAnomalyDetector.MetricDataQueryProperty(
                    id="id",
        
                    # the properties below are optional
                    account_id="accountId",
                    expression="expression",
                    label="label",
                    metric_stat=cloudwatch.CfnAnomalyDetector.MetricStatProperty(
                        metric=cloudwatch.CfnAnomalyDetector.MetricProperty(
                            metric_name="metricName",
                            namespace="namespace",
        
                            # the properties below are optional
                            dimensions=[cloudwatch.CfnAnomalyDetector.DimensionProperty(
                                name="name",
                                value="value"
                            )]
                        ),
                        period=123,
                        stat="stat",
        
                        # the properties below are optional
                        unit="unit"
                    ),
                    period=123,
                    return_data=False
                )]
            ),
            metric_name="metricName",
            namespace="namespace",
            single_metric_anomaly_detector=cloudwatch.CfnAnomalyDetector.SingleMetricAnomalyDetectorProperty(
                account_id="accountId",
                dimensions=[cloudwatch.CfnAnomalyDetector.DimensionProperty(
                    name="name",
                    value="value"
                )],
                metric_name="metricName",
                namespace="namespace",
                stat="stat"
            ),
            stat="stat"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAnomalyDetector.ConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        dimensions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAnomalyDetector.DimensionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        metric_characteristics: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAnomalyDetector.MetricCharacteristicsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        metric_math_anomaly_detector: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAnomalyDetector.MetricMathAnomalyDetectorProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        metric_name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
        single_metric_anomaly_detector: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAnomalyDetector.SingleMetricAnomalyDetectorProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        stat: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param configuration: Specifies details about how the anomaly detection model is to be trained, including time ranges to exclude when training and updating the model. The configuration can also include the time zone to use for the metric.
        :param dimensions: The dimensions of the metric associated with the anomaly detection band.
        :param metric_characteristics: Use this object to include parameters to provide information about your metric to CloudWatch to help it build more accurate anomaly detection models. Currently, it includes the ``PeriodicSpikes`` parameter.
        :param metric_math_anomaly_detector: The CloudWatch metric math expression for this anomaly detector.
        :param metric_name: The name of the metric associated with the anomaly detection band.
        :param namespace: The namespace of the metric associated with the anomaly detection band.
        :param single_metric_anomaly_detector: The CloudWatch metric and statistic for this anomaly detector.
        :param stat: The statistic of the metric associated with the anomaly detection band.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09a2ebaa31c6ab1b46831db515c9eec0f049e129318fe5ad32dd73c9e596659a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAnomalyDetectorProps(
            configuration=configuration,
            dimensions=dimensions,
            metric_characteristics=metric_characteristics,
            metric_math_anomaly_detector=metric_math_anomaly_detector,
            metric_name=metric_name,
            namespace=namespace,
            single_metric_anomaly_detector=single_metric_anomaly_detector,
            stat=stat,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3e4e45621b2bf2b69c3fe98b2cba7744a560f297c63ceb4f36a9522a03416fb)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5d95740790e1f93b73e8f89f80ba917c53d59b96d60ce701fb57c17eaeafdc94)
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
    @jsii.member(jsii_name="configuration")
    def configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAnomalyDetector.ConfigurationProperty"]]:
        '''Specifies details about how the anomaly detection model is to be trained, including time ranges to exclude when training and updating the model.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAnomalyDetector.ConfigurationProperty"]], jsii.get(self, "configuration"))

    @configuration.setter
    def configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAnomalyDetector.ConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4577cb9dfe92537d1cc8e64146892876070d141d09590038417ae6ad98c7b32a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configuration", value)

    @builtins.property
    @jsii.member(jsii_name="dimensions")
    def dimensions(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAnomalyDetector.DimensionProperty"]]]]:
        '''The dimensions of the metric associated with the anomaly detection band.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAnomalyDetector.DimensionProperty"]]]], jsii.get(self, "dimensions"))

    @dimensions.setter
    def dimensions(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAnomalyDetector.DimensionProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa81b524032f55c8d3aa5c261568d608ed375b489e67451c339cda6dff9fdd55)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dimensions", value)

    @builtins.property
    @jsii.member(jsii_name="metricCharacteristics")
    def metric_characteristics(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAnomalyDetector.MetricCharacteristicsProperty"]]:
        '''Use this object to include parameters to provide information about your metric to CloudWatch to help it build more accurate anomaly detection models.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAnomalyDetector.MetricCharacteristicsProperty"]], jsii.get(self, "metricCharacteristics"))

    @metric_characteristics.setter
    def metric_characteristics(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAnomalyDetector.MetricCharacteristicsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__730fad039b3befd0235c3dce81008e3d9f65ab635fe956e8ed48f3ba7060aaba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricCharacteristics", value)

    @builtins.property
    @jsii.member(jsii_name="metricMathAnomalyDetector")
    def metric_math_anomaly_detector(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAnomalyDetector.MetricMathAnomalyDetectorProperty"]]:
        '''The CloudWatch metric math expression for this anomaly detector.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAnomalyDetector.MetricMathAnomalyDetectorProperty"]], jsii.get(self, "metricMathAnomalyDetector"))

    @metric_math_anomaly_detector.setter
    def metric_math_anomaly_detector(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAnomalyDetector.MetricMathAnomalyDetectorProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8f418300bad7bba64cba09c0d26246445ca23587310af02c4b72408240a1db4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricMathAnomalyDetector", value)

    @builtins.property
    @jsii.member(jsii_name="metricName")
    def metric_name(self) -> typing.Optional[builtins.str]:
        '''The name of the metric associated with the anomaly detection band.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metricName"))

    @metric_name.setter
    def metric_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62529ca050619ba994a39e1006e0e31850759c9d38fecaa7680c69fed8dfa964)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricName", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> typing.Optional[builtins.str]:
        '''The namespace of the metric associated with the anomaly detection band.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__773837afe915f1d5b355e30c8993ab753a19fdd128100f68379277738d9ce6f3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="singleMetricAnomalyDetector")
    def single_metric_anomaly_detector(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAnomalyDetector.SingleMetricAnomalyDetectorProperty"]]:
        '''The CloudWatch metric and statistic for this anomaly detector.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAnomalyDetector.SingleMetricAnomalyDetectorProperty"]], jsii.get(self, "singleMetricAnomalyDetector"))

    @single_metric_anomaly_detector.setter
    def single_metric_anomaly_detector(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAnomalyDetector.SingleMetricAnomalyDetectorProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f79f6e93c8bc8ee29709af3c665820fb1e16318cf78b4220c7fd5bcb8a1148b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "singleMetricAnomalyDetector", value)

    @builtins.property
    @jsii.member(jsii_name="stat")
    def stat(self) -> typing.Optional[builtins.str]:
        '''The statistic of the metric associated with the anomaly detection band.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stat"))

    @stat.setter
    def stat(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7812721bb3336919f3fffca23d863b6f1d266a939ca4c3862657da872edd822)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stat", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cloudwatch.CfnAnomalyDetector.ConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "excluded_time_ranges": "excludedTimeRanges",
            "metric_time_zone": "metricTimeZone",
        },
    )
    class ConfigurationProperty:
        def __init__(
            self,
            *,
            excluded_time_ranges: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAnomalyDetector.RangeProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            metric_time_zone: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies details about how the anomaly detection model is to be trained, including time ranges to exclude when training and updating the model.

            The configuration can also include the time zone to use for the metric.

            :param excluded_time_ranges: Specifies an array of time ranges to exclude from use when the anomaly detection model is trained and updated. Use this to make sure that events that could cause unusual values for the metric, such as deployments, aren't used when CloudWatch creates or updates the model.
            :param metric_time_zone: The time zone to use for the metric. This is useful to enable the model to automatically account for daylight savings time changes if the metric is sensitive to such time changes. To specify a time zone, use the name of the time zone as specified in the standard tz database. For more information, see `tz database <https://docs.aws.amazon.com/https://en.wikipedia.org/wiki/Tz_database>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-configuration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cloudwatch as cloudwatch
                
                configuration_property = cloudwatch.CfnAnomalyDetector.ConfigurationProperty(
                    excluded_time_ranges=[cloudwatch.CfnAnomalyDetector.RangeProperty(
                        end_time="endTime",
                        start_time="startTime"
                    )],
                    metric_time_zone="metricTimeZone"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__67352ac72587eb41e06664f1e6dbbc18d0b51da2732f4318f403896a70102121)
                check_type(argname="argument excluded_time_ranges", value=excluded_time_ranges, expected_type=type_hints["excluded_time_ranges"])
                check_type(argname="argument metric_time_zone", value=metric_time_zone, expected_type=type_hints["metric_time_zone"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if excluded_time_ranges is not None:
                self._values["excluded_time_ranges"] = excluded_time_ranges
            if metric_time_zone is not None:
                self._values["metric_time_zone"] = metric_time_zone

        @builtins.property
        def excluded_time_ranges(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAnomalyDetector.RangeProperty"]]]]:
            '''Specifies an array of time ranges to exclude from use when the anomaly detection model is trained and updated.

            Use this to make sure that events that could cause unusual values for the metric, such as deployments, aren't used when CloudWatch creates or updates the model.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-configuration.html#cfn-cloudwatch-anomalydetector-configuration-excludedtimeranges
            '''
            result = self._values.get("excluded_time_ranges")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAnomalyDetector.RangeProperty"]]]], result)

        @builtins.property
        def metric_time_zone(self) -> typing.Optional[builtins.str]:
            '''The time zone to use for the metric.

            This is useful to enable the model to automatically account for daylight savings time changes if the metric is sensitive to such time changes.

            To specify a time zone, use the name of the time zone as specified in the standard tz database. For more information, see `tz database <https://docs.aws.amazon.com/https://en.wikipedia.org/wiki/Tz_database>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-configuration.html#cfn-cloudwatch-anomalydetector-configuration-metrictimezone
            '''
            result = self._values.get("metric_time_zone")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cloudwatch.CfnAnomalyDetector.DimensionProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "value": "value"},
    )
    class DimensionProperty:
        def __init__(self, *, name: builtins.str, value: builtins.str) -> None:
            '''A dimension is a name/value pair that is part of the identity of a metric.

            Because dimensions are part of the unique identifier for a metric, whenever you add a unique name/value pair to one of your metrics, you are creating a new variation of that metric. For example, many Amazon EC2 metrics publish ``InstanceId`` as a dimension name, and the actual instance ID as the value for that dimension.

            You can assign up to 30 dimensions to a metric.

            :param name: The name of the dimension.
            :param value: The value of the dimension. Dimension values must contain only ASCII characters and must include at least one non-whitespace character. ASCII control characters are not supported as part of dimension values.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-dimension.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cloudwatch as cloudwatch
                
                dimension_property = cloudwatch.CfnAnomalyDetector.DimensionProperty(
                    name="name",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__621384455c6fe008d1544e799a687e205dfd7c831d4d16758c94209b7b77dac9)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
                "value": value,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the dimension.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-dimension.html#cfn-cloudwatch-anomalydetector-dimension-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''The value of the dimension.

            Dimension values must contain only ASCII characters and must include at least one non-whitespace character. ASCII control characters are not supported as part of dimension values.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-dimension.html#cfn-cloudwatch-anomalydetector-dimension-value
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
        jsii_type="aws-cdk-lib.aws_cloudwatch.CfnAnomalyDetector.MetricCharacteristicsProperty",
        jsii_struct_bases=[],
        name_mapping={"periodic_spikes": "periodicSpikes"},
    )
    class MetricCharacteristicsProperty:
        def __init__(
            self,
            *,
            periodic_spikes: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''This object includes parameters that you can use to provide information to CloudWatch to help it build more accurate anomaly detection models.

            :param periodic_spikes: Set this parameter to true if values for this metric consistently include spikes that should not be considered to be anomalies. With this set to true, CloudWatch will expect to see spikes that occurred consistently during the model training period, and won't flag future similar spikes as anomalies.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metriccharacteristics.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cloudwatch as cloudwatch
                
                metric_characteristics_property = cloudwatch.CfnAnomalyDetector.MetricCharacteristicsProperty(
                    periodic_spikes=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__782bb184e35a5f89f30dd279aa12cf0d77b7069596cc47017cd113eb386bfa0b)
                check_type(argname="argument periodic_spikes", value=periodic_spikes, expected_type=type_hints["periodic_spikes"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if periodic_spikes is not None:
                self._values["periodic_spikes"] = periodic_spikes

        @builtins.property
        def periodic_spikes(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Set this parameter to true if values for this metric consistently include spikes that should not be considered to be anomalies.

            With this set to true, CloudWatch will expect to see spikes that occurred consistently during the model training period, and won't flag future similar spikes as anomalies.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metriccharacteristics.html#cfn-cloudwatch-anomalydetector-metriccharacteristics-periodicspikes
            '''
            result = self._values.get("periodic_spikes")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MetricCharacteristicsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cloudwatch.CfnAnomalyDetector.MetricDataQueryProperty",
        jsii_struct_bases=[],
        name_mapping={
            "id": "id",
            "account_id": "accountId",
            "expression": "expression",
            "label": "label",
            "metric_stat": "metricStat",
            "period": "period",
            "return_data": "returnData",
        },
    )
    class MetricDataQueryProperty:
        def __init__(
            self,
            *,
            id: builtins.str,
            account_id: typing.Optional[builtins.str] = None,
            expression: typing.Optional[builtins.str] = None,
            label: typing.Optional[builtins.str] = None,
            metric_stat: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAnomalyDetector.MetricStatProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            period: typing.Optional[jsii.Number] = None,
            return_data: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''This structure is used in both ``GetMetricData`` and ``PutMetricAlarm`` .

            The supported use of this structure is different for those two operations.

            When used in ``GetMetricData`` , it indicates the metric data to return, and whether this call is just retrieving a batch set of data for one metric, or is performing a Metrics Insights query or a math expression. A single ``GetMetricData`` call can include up to 500 ``MetricDataQuery`` structures.

            When used in ``PutMetricAlarm`` , it enables you to create an alarm based on a metric math expression. Each ``MetricDataQuery`` in the array specifies either a metric to retrieve, or a math expression to be performed on retrieved metrics. A single ``PutMetricAlarm`` call can include up to 20 ``MetricDataQuery`` structures in the array. The 20 structures can include as many as 10 structures that contain a ``MetricStat`` parameter to retrieve a metric, and as many as 10 structures that contain the ``Expression`` parameter to perform a math expression. Of those ``Expression`` structures, one must have ``true`` as the value for ``ReturnData`` . The result of this expression is the value the alarm watches.

            Any expression used in a ``PutMetricAlarm`` operation must return a single time series. For more information, see `Metric Math Syntax and Functions <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html#metric-math-syntax>`_ in the *Amazon CloudWatch User Guide* .

            Some of the parameters of this structure also have different uses whether you are using this structure in a ``GetMetricData`` operation or a ``PutMetricAlarm`` operation. These differences are explained in the following parameter list.

            :param id: A short name used to tie this object to the results in the response. This name must be unique within a single call to ``GetMetricData`` . If you are performing math expressions on this set of data, this name represents that data and can serve as a variable in the mathematical expression. The valid characters are letters, numbers, and underscore. The first character must be a lowercase letter.
            :param account_id: The ID of the account where the metrics are located. If you are performing a ``GetMetricData`` operation in a monitoring account, use this to specify which account to retrieve this metric from. If you are performing a ``PutMetricAlarm`` operation, use this to specify which account contains the metric that the alarm is watching.
            :param expression: This field can contain either a Metrics Insights query, or a metric math expression to be performed on the returned data. For more information about Metrics Insights queries, see `Metrics Insights query components and syntax <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-metrics-insights-querylanguage>`_ in the *Amazon CloudWatch User Guide* . A math expression can use the ``Id`` of the other metrics or queries to refer to those metrics, and can also use the ``Id`` of other expressions to use the result of those expressions. For more information about metric math expressions, see `Metric Math Syntax and Functions <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html#metric-math-syntax>`_ in the *Amazon CloudWatch User Guide* . Within each MetricDataQuery object, you must specify either ``Expression`` or ``MetricStat`` but not both.
            :param label: A human-readable label for this metric or expression. This is especially useful if this is an expression, so that you know what the value represents. If the metric or expression is shown in a CloudWatch dashboard widget, the label is shown. If Label is omitted, CloudWatch generates a default. You can put dynamic expressions into a label, so that it is more descriptive. For more information, see `Using Dynamic Labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ .
            :param metric_stat: The metric to be returned, along with statistics, period, and units. Use this parameter only if this object is retrieving a metric and not performing a math expression on returned data. Within one MetricDataQuery object, you must specify either ``Expression`` or ``MetricStat`` but not both.
            :param period: The granularity, in seconds, of the returned data points. For metrics with regular resolution, a period can be as short as one minute (60 seconds) and must be a multiple of 60. For high-resolution metrics that are collected at intervals of less than one minute, the period can be 1, 5, 10, 30, 60, or any multiple of 60. High-resolution metrics are those metrics stored by a ``PutMetricData`` operation that includes a ``StorageResolution of 1 second`` .
            :param return_data: When used in ``GetMetricData`` , this option indicates whether to return the timestamps and raw data values of this metric. If you are performing this call just to do math expressions and do not also need the raw data returned, you can specify ``false`` . If you omit this, the default of ``true`` is used. When used in ``PutMetricAlarm`` , specify ``true`` for the one expression result to use as the alarm. For all other metrics and expressions in the same ``PutMetricAlarm`` operation, specify ``ReturnData`` as False.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricdataquery.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cloudwatch as cloudwatch
                
                metric_data_query_property = cloudwatch.CfnAnomalyDetector.MetricDataQueryProperty(
                    id="id",
                
                    # the properties below are optional
                    account_id="accountId",
                    expression="expression",
                    label="label",
                    metric_stat=cloudwatch.CfnAnomalyDetector.MetricStatProperty(
                        metric=cloudwatch.CfnAnomalyDetector.MetricProperty(
                            metric_name="metricName",
                            namespace="namespace",
                
                            # the properties below are optional
                            dimensions=[cloudwatch.CfnAnomalyDetector.DimensionProperty(
                                name="name",
                                value="value"
                            )]
                        ),
                        period=123,
                        stat="stat",
                
                        # the properties below are optional
                        unit="unit"
                    ),
                    period=123,
                    return_data=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d07af40dc753cdda4381651fa3711189e996a0d1ada4554c36c730242ecee721)
                check_type(argname="argument id", value=id, expected_type=type_hints["id"])
                check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
                check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
                check_type(argname="argument label", value=label, expected_type=type_hints["label"])
                check_type(argname="argument metric_stat", value=metric_stat, expected_type=type_hints["metric_stat"])
                check_type(argname="argument period", value=period, expected_type=type_hints["period"])
                check_type(argname="argument return_data", value=return_data, expected_type=type_hints["return_data"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "id": id,
            }
            if account_id is not None:
                self._values["account_id"] = account_id
            if expression is not None:
                self._values["expression"] = expression
            if label is not None:
                self._values["label"] = label
            if metric_stat is not None:
                self._values["metric_stat"] = metric_stat
            if period is not None:
                self._values["period"] = period
            if return_data is not None:
                self._values["return_data"] = return_data

        @builtins.property
        def id(self) -> builtins.str:
            '''A short name used to tie this object to the results in the response.

            This name must be unique within a single call to ``GetMetricData`` . If you are performing math expressions on this set of data, this name represents that data and can serve as a variable in the mathematical expression. The valid characters are letters, numbers, and underscore. The first character must be a lowercase letter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricdataquery.html#cfn-cloudwatch-anomalydetector-metricdataquery-id
            '''
            result = self._values.get("id")
            assert result is not None, "Required property 'id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def account_id(self) -> typing.Optional[builtins.str]:
            '''The ID of the account where the metrics are located.

            If you are performing a ``GetMetricData`` operation in a monitoring account, use this to specify which account to retrieve this metric from.

            If you are performing a ``PutMetricAlarm`` operation, use this to specify which account contains the metric that the alarm is watching.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricdataquery.html#cfn-cloudwatch-anomalydetector-metricdataquery-accountid
            '''
            result = self._values.get("account_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def expression(self) -> typing.Optional[builtins.str]:
            '''This field can contain either a Metrics Insights query, or a metric math expression to be performed on the returned data.

            For more information about Metrics Insights queries, see `Metrics Insights query components and syntax <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-metrics-insights-querylanguage>`_ in the *Amazon CloudWatch User Guide* .

            A math expression can use the ``Id`` of the other metrics or queries to refer to those metrics, and can also use the ``Id`` of other expressions to use the result of those expressions. For more information about metric math expressions, see `Metric Math Syntax and Functions <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html#metric-math-syntax>`_ in the *Amazon CloudWatch User Guide* .

            Within each MetricDataQuery object, you must specify either ``Expression`` or ``MetricStat`` but not both.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricdataquery.html#cfn-cloudwatch-anomalydetector-metricdataquery-expression
            '''
            result = self._values.get("expression")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def label(self) -> typing.Optional[builtins.str]:
            '''A human-readable label for this metric or expression.

            This is especially useful if this is an expression, so that you know what the value represents. If the metric or expression is shown in a CloudWatch dashboard widget, the label is shown. If Label is omitted, CloudWatch generates a default.

            You can put dynamic expressions into a label, so that it is more descriptive. For more information, see `Using Dynamic Labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricdataquery.html#cfn-cloudwatch-anomalydetector-metricdataquery-label
            '''
            result = self._values.get("label")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def metric_stat(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAnomalyDetector.MetricStatProperty"]]:
            '''The metric to be returned, along with statistics, period, and units.

            Use this parameter only if this object is retrieving a metric and not performing a math expression on returned data.

            Within one MetricDataQuery object, you must specify either ``Expression`` or ``MetricStat`` but not both.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricdataquery.html#cfn-cloudwatch-anomalydetector-metricdataquery-metricstat
            '''
            result = self._values.get("metric_stat")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAnomalyDetector.MetricStatProperty"]], result)

        @builtins.property
        def period(self) -> typing.Optional[jsii.Number]:
            '''The granularity, in seconds, of the returned data points.

            For metrics with regular resolution, a period can be as short as one minute (60 seconds) and must be a multiple of 60. For high-resolution metrics that are collected at intervals of less than one minute, the period can be 1, 5, 10, 30, 60, or any multiple of 60. High-resolution metrics are those metrics stored by a ``PutMetricData`` operation that includes a ``StorageResolution of 1 second`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricdataquery.html#cfn-cloudwatch-anomalydetector-metricdataquery-period
            '''
            result = self._values.get("period")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def return_data(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''When used in ``GetMetricData`` , this option indicates whether to return the timestamps and raw data values of this metric.

            If you are performing this call just to do math expressions and do not also need the raw data returned, you can specify ``false`` . If you omit this, the default of ``true`` is used.

            When used in ``PutMetricAlarm`` , specify ``true`` for the one expression result to use as the alarm. For all other metrics and expressions in the same ``PutMetricAlarm`` operation, specify ``ReturnData`` as False.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricdataquery.html#cfn-cloudwatch-anomalydetector-metricdataquery-returndata
            '''
            result = self._values.get("return_data")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MetricDataQueryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cloudwatch.CfnAnomalyDetector.MetricMathAnomalyDetectorProperty",
        jsii_struct_bases=[],
        name_mapping={"metric_data_queries": "metricDataQueries"},
    )
    class MetricMathAnomalyDetectorProperty:
        def __init__(
            self,
            *,
            metric_data_queries: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAnomalyDetector.MetricDataQueryProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Indicates the CloudWatch math expression that provides the time series the anomaly detector uses as input.

            The designated math expression must return a single time series.

            :param metric_data_queries: An array of metric data query structures that enables you to create an anomaly detector based on the result of a metric math expression. Each item in ``MetricDataQueries`` gets a metric or performs a math expression. One item in ``MetricDataQueries`` is the expression that provides the time series that the anomaly detector uses as input. Designate the expression by setting ``ReturnData`` to ``true`` for this object in the array. For all other expressions and metrics, set ``ReturnData`` to ``false`` . The designated expression must return a single time series.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricmathanomalydetector.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cloudwatch as cloudwatch
                
                metric_math_anomaly_detector_property = cloudwatch.CfnAnomalyDetector.MetricMathAnomalyDetectorProperty(
                    metric_data_queries=[cloudwatch.CfnAnomalyDetector.MetricDataQueryProperty(
                        id="id",
                
                        # the properties below are optional
                        account_id="accountId",
                        expression="expression",
                        label="label",
                        metric_stat=cloudwatch.CfnAnomalyDetector.MetricStatProperty(
                            metric=cloudwatch.CfnAnomalyDetector.MetricProperty(
                                metric_name="metricName",
                                namespace="namespace",
                
                                # the properties below are optional
                                dimensions=[cloudwatch.CfnAnomalyDetector.DimensionProperty(
                                    name="name",
                                    value="value"
                                )]
                            ),
                            period=123,
                            stat="stat",
                
                            # the properties below are optional
                            unit="unit"
                        ),
                        period=123,
                        return_data=False
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fe2d23d029852cd64aa565c80080a904e189f6017f7ab50f0c89da36d7c772bb)
                check_type(argname="argument metric_data_queries", value=metric_data_queries, expected_type=type_hints["metric_data_queries"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if metric_data_queries is not None:
                self._values["metric_data_queries"] = metric_data_queries

        @builtins.property
        def metric_data_queries(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAnomalyDetector.MetricDataQueryProperty"]]]]:
            '''An array of metric data query structures that enables you to create an anomaly detector based on the result of a metric math expression.

            Each item in ``MetricDataQueries`` gets a metric or performs a math expression. One item in ``MetricDataQueries`` is the expression that provides the time series that the anomaly detector uses as input. Designate the expression by setting ``ReturnData`` to ``true`` for this object in the array. For all other expressions and metrics, set ``ReturnData`` to ``false`` . The designated expression must return a single time series.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricmathanomalydetector.html#cfn-cloudwatch-anomalydetector-metricmathanomalydetector-metricdataqueries
            '''
            result = self._values.get("metric_data_queries")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAnomalyDetector.MetricDataQueryProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MetricMathAnomalyDetectorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cloudwatch.CfnAnomalyDetector.MetricProperty",
        jsii_struct_bases=[],
        name_mapping={
            "metric_name": "metricName",
            "namespace": "namespace",
            "dimensions": "dimensions",
        },
    )
    class MetricProperty:
        def __init__(
            self,
            *,
            metric_name: builtins.str,
            namespace: builtins.str,
            dimensions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAnomalyDetector.DimensionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Represents a specific metric.

            :param metric_name: The name of the metric. This is a required field.
            :param namespace: The namespace of the metric.
            :param dimensions: The dimensions for the metric.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metric.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cloudwatch as cloudwatch
                
                metric_property = cloudwatch.CfnAnomalyDetector.MetricProperty(
                    metric_name="metricName",
                    namespace="namespace",
                
                    # the properties below are optional
                    dimensions=[cloudwatch.CfnAnomalyDetector.DimensionProperty(
                        name="name",
                        value="value"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0b189668a1a93615dfd113ac1c4798293f70acd463c9a2519156d29af0bf0392)
                check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
                check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
                check_type(argname="argument dimensions", value=dimensions, expected_type=type_hints["dimensions"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "metric_name": metric_name,
                "namespace": namespace,
            }
            if dimensions is not None:
                self._values["dimensions"] = dimensions

        @builtins.property
        def metric_name(self) -> builtins.str:
            '''The name of the metric.

            This is a required field.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metric.html#cfn-cloudwatch-anomalydetector-metric-metricname
            '''
            result = self._values.get("metric_name")
            assert result is not None, "Required property 'metric_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def namespace(self) -> builtins.str:
            '''The namespace of the metric.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metric.html#cfn-cloudwatch-anomalydetector-metric-namespace
            '''
            result = self._values.get("namespace")
            assert result is not None, "Required property 'namespace' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def dimensions(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAnomalyDetector.DimensionProperty"]]]]:
            '''The dimensions for the metric.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metric.html#cfn-cloudwatch-anomalydetector-metric-dimensions
            '''
            result = self._values.get("dimensions")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAnomalyDetector.DimensionProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MetricProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cloudwatch.CfnAnomalyDetector.MetricStatProperty",
        jsii_struct_bases=[],
        name_mapping={
            "metric": "metric",
            "period": "period",
            "stat": "stat",
            "unit": "unit",
        },
    )
    class MetricStatProperty:
        def __init__(
            self,
            *,
            metric: typing.Union[_IResolvable_da3f097b, typing.Union["CfnAnomalyDetector.MetricProperty", typing.Dict[builtins.str, typing.Any]]],
            period: jsii.Number,
            stat: builtins.str,
            unit: typing.Optional[builtins.str] = None,
        ) -> None:
            '''This structure defines the metric to be returned, along with the statistics, period, and units.

            :param metric: The metric to return, including the metric name, namespace, and dimensions.
            :param period: The granularity, in seconds, of the returned data points. For metrics with regular resolution, a period can be as short as one minute (60 seconds) and must be a multiple of 60. For high-resolution metrics that are collected at intervals of less than one minute, the period can be 1, 5, 10, 30, 60, or any multiple of 60. High-resolution metrics are those metrics stored by a ``PutMetricData`` call that includes a ``StorageResolution`` of 1 second. If the ``StartTime`` parameter specifies a time stamp that is greater than 3 hours ago, you must specify the period as follows or no data points in that time range is returned: - Start time between 3 hours and 15 days ago - Use a multiple of 60 seconds (1 minute). - Start time between 15 and 63 days ago - Use a multiple of 300 seconds (5 minutes). - Start time greater than 63 days ago - Use a multiple of 3600 seconds (1 hour).
            :param stat: The statistic to return. It can include any CloudWatch statistic or extended statistic.
            :param unit: When you are using a ``Put`` operation, this defines what unit you want to use when storing the metric. In a ``Get`` operation, if you omit ``Unit`` then all data that was collected with any unit is returned, along with the corresponding units that were specified when the data was reported to CloudWatch. If you specify a unit, the operation returns only data that was collected with that unit specified. If you specify a unit that does not match the data collected, the results of the operation are null. CloudWatch does not perform unit conversions.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricstat.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cloudwatch as cloudwatch
                
                metric_stat_property = cloudwatch.CfnAnomalyDetector.MetricStatProperty(
                    metric=cloudwatch.CfnAnomalyDetector.MetricProperty(
                        metric_name="metricName",
                        namespace="namespace",
                
                        # the properties below are optional
                        dimensions=[cloudwatch.CfnAnomalyDetector.DimensionProperty(
                            name="name",
                            value="value"
                        )]
                    ),
                    period=123,
                    stat="stat",
                
                    # the properties below are optional
                    unit="unit"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5b3d65b4810e6974d2b03459fe0fd3d8db280dcecbf37190a36d9be3e039913c)
                check_type(argname="argument metric", value=metric, expected_type=type_hints["metric"])
                check_type(argname="argument period", value=period, expected_type=type_hints["period"])
                check_type(argname="argument stat", value=stat, expected_type=type_hints["stat"])
                check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "metric": metric,
                "period": period,
                "stat": stat,
            }
            if unit is not None:
                self._values["unit"] = unit

        @builtins.property
        def metric(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnAnomalyDetector.MetricProperty"]:
            '''The metric to return, including the metric name, namespace, and dimensions.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricstat.html#cfn-cloudwatch-anomalydetector-metricstat-metric
            '''
            result = self._values.get("metric")
            assert result is not None, "Required property 'metric' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnAnomalyDetector.MetricProperty"], result)

        @builtins.property
        def period(self) -> jsii.Number:
            '''The granularity, in seconds, of the returned data points.

            For metrics with regular resolution, a period can be as short as one minute (60 seconds) and must be a multiple of 60. For high-resolution metrics that are collected at intervals of less than one minute, the period can be 1, 5, 10, 30, 60, or any multiple of 60. High-resolution metrics are those metrics stored by a ``PutMetricData`` call that includes a ``StorageResolution`` of 1 second.

            If the ``StartTime`` parameter specifies a time stamp that is greater than 3 hours ago, you must specify the period as follows or no data points in that time range is returned:

            - Start time between 3 hours and 15 days ago - Use a multiple of 60 seconds (1 minute).
            - Start time between 15 and 63 days ago - Use a multiple of 300 seconds (5 minutes).
            - Start time greater than 63 days ago - Use a multiple of 3600 seconds (1 hour).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricstat.html#cfn-cloudwatch-anomalydetector-metricstat-period
            '''
            result = self._values.get("period")
            assert result is not None, "Required property 'period' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def stat(self) -> builtins.str:
            '''The statistic to return.

            It can include any CloudWatch statistic or extended statistic.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricstat.html#cfn-cloudwatch-anomalydetector-metricstat-stat
            '''
            result = self._values.get("stat")
            assert result is not None, "Required property 'stat' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def unit(self) -> typing.Optional[builtins.str]:
            '''When you are using a ``Put`` operation, this defines what unit you want to use when storing the metric.

            In a ``Get`` operation, if you omit ``Unit`` then all data that was collected with any unit is returned, along with the corresponding units that were specified when the data was reported to CloudWatch. If you specify a unit, the operation returns only data that was collected with that unit specified. If you specify a unit that does not match the data collected, the results of the operation are null. CloudWatch does not perform unit conversions.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricstat.html#cfn-cloudwatch-anomalydetector-metricstat-unit
            '''
            result = self._values.get("unit")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MetricStatProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cloudwatch.CfnAnomalyDetector.RangeProperty",
        jsii_struct_bases=[],
        name_mapping={"end_time": "endTime", "start_time": "startTime"},
    )
    class RangeProperty:
        def __init__(self, *, end_time: builtins.str, start_time: builtins.str) -> None:
            '''Each ``Range`` specifies one range of days or times to exclude from use for training or updating an anomaly detection model.

            :param end_time: The end time of the range to exclude. The format is ``yyyy-MM-dd'T'HH:mm:ss`` . For example, ``2019-07-01T23:59:59`` .
            :param start_time: The start time of the range to exclude. The format is ``yyyy-MM-dd'T'HH:mm:ss`` . For example, ``2019-07-01T23:59:59`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-range.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cloudwatch as cloudwatch
                
                range_property = cloudwatch.CfnAnomalyDetector.RangeProperty(
                    end_time="endTime",
                    start_time="startTime"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9bc80976f2b683f55d7e2d50a80f5b0ac541edd875fa1a1062846959cb4afa0b)
                check_type(argname="argument end_time", value=end_time, expected_type=type_hints["end_time"])
                check_type(argname="argument start_time", value=start_time, expected_type=type_hints["start_time"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "end_time": end_time,
                "start_time": start_time,
            }

        @builtins.property
        def end_time(self) -> builtins.str:
            '''The end time of the range to exclude.

            The format is ``yyyy-MM-dd'T'HH:mm:ss`` . For example, ``2019-07-01T23:59:59`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-range.html#cfn-cloudwatch-anomalydetector-range-endtime
            '''
            result = self._values.get("end_time")
            assert result is not None, "Required property 'end_time' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def start_time(self) -> builtins.str:
            '''The start time of the range to exclude.

            The format is ``yyyy-MM-dd'T'HH:mm:ss`` . For example, ``2019-07-01T23:59:59`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-range.html#cfn-cloudwatch-anomalydetector-range-starttime
            '''
            result = self._values.get("start_time")
            assert result is not None, "Required property 'start_time' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RangeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cloudwatch.CfnAnomalyDetector.SingleMetricAnomalyDetectorProperty",
        jsii_struct_bases=[],
        name_mapping={
            "account_id": "accountId",
            "dimensions": "dimensions",
            "metric_name": "metricName",
            "namespace": "namespace",
            "stat": "stat",
        },
    )
    class SingleMetricAnomalyDetectorProperty:
        def __init__(
            self,
            *,
            account_id: typing.Optional[builtins.str] = None,
            dimensions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAnomalyDetector.DimensionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            metric_name: typing.Optional[builtins.str] = None,
            namespace: typing.Optional[builtins.str] = None,
            stat: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Designates the CloudWatch metric and statistic that provides the time series the anomaly detector uses as input.

            If you have enabled unified cross-account observability, and this account is a monitoring account, the metric can be in the same account or a source account.

            :param account_id: If the CloudWatch metric that provides the time series that the anomaly detector uses as input is in another account, specify that account ID here. If you omit this parameter, the current account is used.
            :param dimensions: The metric dimensions to create the anomaly detection model for.
            :param metric_name: The name of the metric to create the anomaly detection model for.
            :param namespace: The namespace of the metric to create the anomaly detection model for.
            :param stat: The statistic to use for the metric and anomaly detection model.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-singlemetricanomalydetector.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cloudwatch as cloudwatch
                
                single_metric_anomaly_detector_property = cloudwatch.CfnAnomalyDetector.SingleMetricAnomalyDetectorProperty(
                    account_id="accountId",
                    dimensions=[cloudwatch.CfnAnomalyDetector.DimensionProperty(
                        name="name",
                        value="value"
                    )],
                    metric_name="metricName",
                    namespace="namespace",
                    stat="stat"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2a262a607da9d06ac67c27003b22dd869da37f8dcb73d7c6f1f5c7524458adf0)
                check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
                check_type(argname="argument dimensions", value=dimensions, expected_type=type_hints["dimensions"])
                check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
                check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
                check_type(argname="argument stat", value=stat, expected_type=type_hints["stat"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if account_id is not None:
                self._values["account_id"] = account_id
            if dimensions is not None:
                self._values["dimensions"] = dimensions
            if metric_name is not None:
                self._values["metric_name"] = metric_name
            if namespace is not None:
                self._values["namespace"] = namespace
            if stat is not None:
                self._values["stat"] = stat

        @builtins.property
        def account_id(self) -> typing.Optional[builtins.str]:
            '''If the CloudWatch metric that provides the time series that the anomaly detector uses as input is in another account, specify that account ID here.

            If you omit this parameter, the current account is used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-singlemetricanomalydetector.html#cfn-cloudwatch-anomalydetector-singlemetricanomalydetector-accountid
            '''
            result = self._values.get("account_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def dimensions(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAnomalyDetector.DimensionProperty"]]]]:
            '''The metric dimensions to create the anomaly detection model for.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-singlemetricanomalydetector.html#cfn-cloudwatch-anomalydetector-singlemetricanomalydetector-dimensions
            '''
            result = self._values.get("dimensions")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAnomalyDetector.DimensionProperty"]]]], result)

        @builtins.property
        def metric_name(self) -> typing.Optional[builtins.str]:
            '''The name of the metric to create the anomaly detection model for.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-singlemetricanomalydetector.html#cfn-cloudwatch-anomalydetector-singlemetricanomalydetector-metricname
            '''
            result = self._values.get("metric_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def namespace(self) -> typing.Optional[builtins.str]:
            '''The namespace of the metric to create the anomaly detection model for.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-singlemetricanomalydetector.html#cfn-cloudwatch-anomalydetector-singlemetricanomalydetector-namespace
            '''
            result = self._values.get("namespace")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def stat(self) -> typing.Optional[builtins.str]:
            '''The statistic to use for the metric and anomaly detection model.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-singlemetricanomalydetector.html#cfn-cloudwatch-anomalydetector-singlemetricanomalydetector-stat
            '''
            result = self._values.get("stat")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SingleMetricAnomalyDetectorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudwatch.CfnAnomalyDetectorProps",
    jsii_struct_bases=[],
    name_mapping={
        "configuration": "configuration",
        "dimensions": "dimensions",
        "metric_characteristics": "metricCharacteristics",
        "metric_math_anomaly_detector": "metricMathAnomalyDetector",
        "metric_name": "metricName",
        "namespace": "namespace",
        "single_metric_anomaly_detector": "singleMetricAnomalyDetector",
        "stat": "stat",
    },
)
class CfnAnomalyDetectorProps:
    def __init__(
        self,
        *,
        configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnomalyDetector.ConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        dimensions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnomalyDetector.DimensionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        metric_characteristics: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnomalyDetector.MetricCharacteristicsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        metric_math_anomaly_detector: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnomalyDetector.MetricMathAnomalyDetectorProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        metric_name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
        single_metric_anomaly_detector: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnomalyDetector.SingleMetricAnomalyDetectorProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        stat: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnAnomalyDetector``.

        :param configuration: Specifies details about how the anomaly detection model is to be trained, including time ranges to exclude when training and updating the model. The configuration can also include the time zone to use for the metric.
        :param dimensions: The dimensions of the metric associated with the anomaly detection band.
        :param metric_characteristics: Use this object to include parameters to provide information about your metric to CloudWatch to help it build more accurate anomaly detection models. Currently, it includes the ``PeriodicSpikes`` parameter.
        :param metric_math_anomaly_detector: The CloudWatch metric math expression for this anomaly detector.
        :param metric_name: The name of the metric associated with the anomaly detection band.
        :param namespace: The namespace of the metric associated with the anomaly detection band.
        :param single_metric_anomaly_detector: The CloudWatch metric and statistic for this anomaly detector.
        :param stat: The statistic of the metric associated with the anomaly detection band.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-anomalydetector.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cloudwatch as cloudwatch
            
            cfn_anomaly_detector_props = cloudwatch.CfnAnomalyDetectorProps(
                configuration=cloudwatch.CfnAnomalyDetector.ConfigurationProperty(
                    excluded_time_ranges=[cloudwatch.CfnAnomalyDetector.RangeProperty(
                        end_time="endTime",
                        start_time="startTime"
                    )],
                    metric_time_zone="metricTimeZone"
                ),
                dimensions=[cloudwatch.CfnAnomalyDetector.DimensionProperty(
                    name="name",
                    value="value"
                )],
                metric_characteristics=cloudwatch.CfnAnomalyDetector.MetricCharacteristicsProperty(
                    periodic_spikes=False
                ),
                metric_math_anomaly_detector=cloudwatch.CfnAnomalyDetector.MetricMathAnomalyDetectorProperty(
                    metric_data_queries=[cloudwatch.CfnAnomalyDetector.MetricDataQueryProperty(
                        id="id",
            
                        # the properties below are optional
                        account_id="accountId",
                        expression="expression",
                        label="label",
                        metric_stat=cloudwatch.CfnAnomalyDetector.MetricStatProperty(
                            metric=cloudwatch.CfnAnomalyDetector.MetricProperty(
                                metric_name="metricName",
                                namespace="namespace",
            
                                # the properties below are optional
                                dimensions=[cloudwatch.CfnAnomalyDetector.DimensionProperty(
                                    name="name",
                                    value="value"
                                )]
                            ),
                            period=123,
                            stat="stat",
            
                            # the properties below are optional
                            unit="unit"
                        ),
                        period=123,
                        return_data=False
                    )]
                ),
                metric_name="metricName",
                namespace="namespace",
                single_metric_anomaly_detector=cloudwatch.CfnAnomalyDetector.SingleMetricAnomalyDetectorProperty(
                    account_id="accountId",
                    dimensions=[cloudwatch.CfnAnomalyDetector.DimensionProperty(
                        name="name",
                        value="value"
                    )],
                    metric_name="metricName",
                    namespace="namespace",
                    stat="stat"
                ),
                stat="stat"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__929a09b64f3cc2009ffca4b74d148c42dfbbc7531a49bc66cb58443f8870fba2)
            check_type(argname="argument configuration", value=configuration, expected_type=type_hints["configuration"])
            check_type(argname="argument dimensions", value=dimensions, expected_type=type_hints["dimensions"])
            check_type(argname="argument metric_characteristics", value=metric_characteristics, expected_type=type_hints["metric_characteristics"])
            check_type(argname="argument metric_math_anomaly_detector", value=metric_math_anomaly_detector, expected_type=type_hints["metric_math_anomaly_detector"])
            check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument single_metric_anomaly_detector", value=single_metric_anomaly_detector, expected_type=type_hints["single_metric_anomaly_detector"])
            check_type(argname="argument stat", value=stat, expected_type=type_hints["stat"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if configuration is not None:
            self._values["configuration"] = configuration
        if dimensions is not None:
            self._values["dimensions"] = dimensions
        if metric_characteristics is not None:
            self._values["metric_characteristics"] = metric_characteristics
        if metric_math_anomaly_detector is not None:
            self._values["metric_math_anomaly_detector"] = metric_math_anomaly_detector
        if metric_name is not None:
            self._values["metric_name"] = metric_name
        if namespace is not None:
            self._values["namespace"] = namespace
        if single_metric_anomaly_detector is not None:
            self._values["single_metric_anomaly_detector"] = single_metric_anomaly_detector
        if stat is not None:
            self._values["stat"] = stat

    @builtins.property
    def configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAnomalyDetector.ConfigurationProperty]]:
        '''Specifies details about how the anomaly detection model is to be trained, including time ranges to exclude when training and updating the model.

        The configuration can also include the time zone to use for the metric.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-anomalydetector.html#cfn-cloudwatch-anomalydetector-configuration
        '''
        result = self._values.get("configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAnomalyDetector.ConfigurationProperty]], result)

    @builtins.property
    def dimensions(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnAnomalyDetector.DimensionProperty]]]]:
        '''The dimensions of the metric associated with the anomaly detection band.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-anomalydetector.html#cfn-cloudwatch-anomalydetector-dimensions
        '''
        result = self._values.get("dimensions")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnAnomalyDetector.DimensionProperty]]]], result)

    @builtins.property
    def metric_characteristics(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAnomalyDetector.MetricCharacteristicsProperty]]:
        '''Use this object to include parameters to provide information about your metric to CloudWatch to help it build more accurate anomaly detection models.

        Currently, it includes the ``PeriodicSpikes`` parameter.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-anomalydetector.html#cfn-cloudwatch-anomalydetector-metriccharacteristics
        '''
        result = self._values.get("metric_characteristics")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAnomalyDetector.MetricCharacteristicsProperty]], result)

    @builtins.property
    def metric_math_anomaly_detector(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAnomalyDetector.MetricMathAnomalyDetectorProperty]]:
        '''The CloudWatch metric math expression for this anomaly detector.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-anomalydetector.html#cfn-cloudwatch-anomalydetector-metricmathanomalydetector
        '''
        result = self._values.get("metric_math_anomaly_detector")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAnomalyDetector.MetricMathAnomalyDetectorProperty]], result)

    @builtins.property
    def metric_name(self) -> typing.Optional[builtins.str]:
        '''The name of the metric associated with the anomaly detection band.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-anomalydetector.html#cfn-cloudwatch-anomalydetector-metricname
        '''
        result = self._values.get("metric_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''The namespace of the metric associated with the anomaly detection band.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-anomalydetector.html#cfn-cloudwatch-anomalydetector-namespace
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def single_metric_anomaly_detector(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAnomalyDetector.SingleMetricAnomalyDetectorProperty]]:
        '''The CloudWatch metric and statistic for this anomaly detector.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-anomalydetector.html#cfn-cloudwatch-anomalydetector-singlemetricanomalydetector
        '''
        result = self._values.get("single_metric_anomaly_detector")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAnomalyDetector.SingleMetricAnomalyDetectorProperty]], result)

    @builtins.property
    def stat(self) -> typing.Optional[builtins.str]:
        '''The statistic of the metric associated with the anomaly detection band.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-anomalydetector.html#cfn-cloudwatch-anomalydetector-stat
        '''
        result = self._values.get("stat")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAnomalyDetectorProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnCompositeAlarm(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudwatch.CfnCompositeAlarm",
):
    '''The ``AWS::CloudWatch::CompositeAlarm`` type creates or updates a composite alarm.

    When you create a composite alarm, you specify a rule expression for the alarm that takes into account the alarm states of other alarms that you have created. The composite alarm goes into ALARM state only if all conditions of the rule are met.

    The alarms specified in a composite alarm's rule expression can include metric alarms and other composite alarms.

    Using composite alarms can reduce alarm noise. You can create multiple metric alarms, and also create a composite alarm and set up alerts only for the composite alarm. For example, you could create a composite alarm that goes into ALARM state only when more than one of the underlying metric alarms are in ALARM state.

    When this operation creates an alarm, the alarm state is immediately set to INSUFFICIENT_DATA. The alarm is then evaluated and its state is set appropriately. Any actions associated with the new state are then executed. For a composite alarm, this initial time after creation is the only time that the alarm can be in INSUFFICIENT_DATA state.

    When you update an existing alarm, its state is left unchanged, but the update completely overwrites the previous configuration of the alarm.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-compositealarm.html
    :cloudformationResource: AWS::CloudWatch::CompositeAlarm
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_cloudwatch as cloudwatch
        
        cfn_composite_alarm = cloudwatch.CfnCompositeAlarm(self, "MyCfnCompositeAlarm",
            alarm_rule="alarmRule",
        
            # the properties below are optional
            actions_enabled=False,
            actions_suppressor="actionsSuppressor",
            actions_suppressor_extension_period=123,
            actions_suppressor_wait_period=123,
            alarm_actions=["alarmActions"],
            alarm_description="alarmDescription",
            alarm_name="alarmName",
            insufficient_data_actions=["insufficientDataActions"],
            ok_actions=["okActions"],
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
        alarm_rule: builtins.str,
        actions_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        actions_suppressor: typing.Optional[builtins.str] = None,
        actions_suppressor_extension_period: typing.Optional[jsii.Number] = None,
        actions_suppressor_wait_period: typing.Optional[jsii.Number] = None,
        alarm_actions: typing.Optional[typing.Sequence[builtins.str]] = None,
        alarm_description: typing.Optional[builtins.str] = None,
        alarm_name: typing.Optional[builtins.str] = None,
        insufficient_data_actions: typing.Optional[typing.Sequence[builtins.str]] = None,
        ok_actions: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param alarm_rule: An expression that specifies which other alarms are to be evaluated to determine this composite alarm's state. For each alarm that you reference, you designate a function that specifies whether that alarm needs to be in ALARM state, OK state, or INSUFFICIENT_DATA state. You can use operators (AND, OR and NOT) to combine multiple functions in a single expression. You can use parenthesis to logically group the functions in your expression. You can use either alarm names or ARNs to reference the other alarms that are to be evaluated. Functions can include the following: - ALARM("alarm-name or alarm-ARN") is TRUE if the named alarm is in ALARM state. - OK("alarm-name or alarm-ARN") is TRUE if the named alarm is in OK state. - INSUFFICIENT_DATA("alarm-name or alarm-ARN") is TRUE if the named alarm is in INSUFFICIENT_DATA state. - TRUE always evaluates to TRUE. - FALSE always evaluates to FALSE. TRUE and FALSE are useful for testing a complex AlarmRule structure, and for testing your alarm actions. For more information about ``AlarmRule`` syntax, see `PutCompositeAlarm <https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutCompositeAlarm.html>`_ in the *Amazon CloudWatch API Reference* .
        :param actions_enabled: Indicates whether actions should be executed during any changes to the alarm state of the composite alarm. The default is TRUE.
        :param actions_suppressor: Actions will be suppressed if the suppressor alarm is in the ``ALARM`` state. ``ActionsSuppressor`` can be an AlarmName or an Amazon Resource Name (ARN) from an existing alarm.
        :param actions_suppressor_extension_period: The maximum time in seconds that the composite alarm waits after suppressor alarm goes out of the ``ALARM`` state. After this time, the composite alarm performs its actions. .. epigraph:: ``ExtensionPeriod`` is required only when ``ActionsSuppressor`` is specified.
        :param actions_suppressor_wait_period: The maximum time in seconds that the composite alarm waits for the suppressor alarm to go into the ``ALARM`` state. After this time, the composite alarm performs its actions. .. epigraph:: ``WaitPeriod`` is required only when ``ActionsSuppressor`` is specified.
        :param alarm_actions: The actions to execute when this alarm transitions to the ALARM state from any other state. Each action is specified as an Amazon Resource Name (ARN). For more information about creating alarms and the actions that you can specify, see `PutCompositeAlarm <https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutCompositeAlarm.html>`_ in the *Amazon CloudWatch API Reference* .
        :param alarm_description: The description for the composite alarm.
        :param alarm_name: The name for the composite alarm. This name must be unique within your AWS account.
        :param insufficient_data_actions: The actions to execute when this alarm transitions to the INSUFFICIENT_DATA state from any other state. Each action is specified as an Amazon Resource Name (ARN). For more information about creating alarms and the actions that you can specify, see `PutCompositeAlarm <https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutCompositeAlarm.html>`_ in the *Amazon CloudWatch API Reference* .
        :param ok_actions: The actions to execute when this alarm transitions to the OK state from any other state. Each action is specified as an Amazon Resource Name (ARN). For more information about creating alarms and the actions that you can specify, see `PutCompositeAlarm <https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutCompositeAlarm.html>`_ in the *Amazon CloudWatch API Reference* .
        :param tags: A list of key-value pairs to associate with the alarm. You can associate as many as 50 tags with an alarm. To be able to associate tags with the alarm when you create the alarm, you must have the ``cloudwatch:TagResource`` permission. Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c24d10326e3cd470724ecbde5d50ff23fdf44dc88f809d9a181a5cd867e5cf3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCompositeAlarmProps(
            alarm_rule=alarm_rule,
            actions_enabled=actions_enabled,
            actions_suppressor=actions_suppressor,
            actions_suppressor_extension_period=actions_suppressor_extension_period,
            actions_suppressor_wait_period=actions_suppressor_wait_period,
            alarm_actions=alarm_actions,
            alarm_description=alarm_description,
            alarm_name=alarm_name,
            insufficient_data_actions=insufficient_data_actions,
            ok_actions=ok_actions,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__399fd96f9e0939b1087102f4b90094a74c88e8fdf84dcd24f4f9a6faf0d9ee93)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c792f92e772e604ae78dfb7743ace896d51e15317ab3c7188cb3c3f01b50a12a)
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
        '''The ARN of the composite alarm, such as ``arn:aws:cloudwatch:us-west-2:123456789012:alarm/CompositeAlarmName`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="cdkTagManager")
    def cdk_tag_manager(self) -> _TagManager_0a598cb3:
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "cdkTagManager"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="alarmRule")
    def alarm_rule(self) -> builtins.str:
        '''An expression that specifies which other alarms are to be evaluated to determine this composite alarm's state.'''
        return typing.cast(builtins.str, jsii.get(self, "alarmRule"))

    @alarm_rule.setter
    def alarm_rule(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e343637dcbb025d59f785b38d36b2f01ca3c7a48777520e981849e0b80fefcb7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alarmRule", value)

    @builtins.property
    @jsii.member(jsii_name="actionsEnabled")
    def actions_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Indicates whether actions should be executed during any changes to the alarm state of the composite alarm.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "actionsEnabled"))

    @actions_enabled.setter
    def actions_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43ce9ab8aaafd96e9ff146e41c5e3921be5380953cea24e5da817be9a65afdcb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "actionsEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="actionsSuppressor")
    def actions_suppressor(self) -> typing.Optional[builtins.str]:
        '''Actions will be suppressed if the suppressor alarm is in the ``ALARM`` state.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionsSuppressor"))

    @actions_suppressor.setter
    def actions_suppressor(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec17e197e4085501e80806e6a6281d3058abe5cef41136d5b9adb00c43ad208a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "actionsSuppressor", value)

    @builtins.property
    @jsii.member(jsii_name="actionsSuppressorExtensionPeriod")
    def actions_suppressor_extension_period(self) -> typing.Optional[jsii.Number]:
        '''The maximum time in seconds that the composite alarm waits after suppressor alarm goes out of the ``ALARM`` state.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "actionsSuppressorExtensionPeriod"))

    @actions_suppressor_extension_period.setter
    def actions_suppressor_extension_period(
        self,
        value: typing.Optional[jsii.Number],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f59b02bf7b3f38f8619d99d396adb8a199f811d2b0b285ea883b46dbc6c8093a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "actionsSuppressorExtensionPeriod", value)

    @builtins.property
    @jsii.member(jsii_name="actionsSuppressorWaitPeriod")
    def actions_suppressor_wait_period(self) -> typing.Optional[jsii.Number]:
        '''The maximum time in seconds that the composite alarm waits for the suppressor alarm to go into the ``ALARM`` state.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "actionsSuppressorWaitPeriod"))

    @actions_suppressor_wait_period.setter
    def actions_suppressor_wait_period(
        self,
        value: typing.Optional[jsii.Number],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc105b69ef4e4fb77cafb9a01fd07d05e35906a88000902617ddd4ff60098ce4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "actionsSuppressorWaitPeriod", value)

    @builtins.property
    @jsii.member(jsii_name="alarmActions")
    def alarm_actions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The actions to execute when this alarm transitions to the ALARM state from any other state.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "alarmActions"))

    @alarm_actions.setter
    def alarm_actions(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68f13f2cdd6512362166f971941eb93e413522e0a7f50732f11be4849a0314b5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alarmActions", value)

    @builtins.property
    @jsii.member(jsii_name="alarmDescription")
    def alarm_description(self) -> typing.Optional[builtins.str]:
        '''The description for the composite alarm.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alarmDescription"))

    @alarm_description.setter
    def alarm_description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba7d39bfc4a33f1e068842cf86eda6b8b89a710218c633e611c70f1c8daa97ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alarmDescription", value)

    @builtins.property
    @jsii.member(jsii_name="alarmName")
    def alarm_name(self) -> typing.Optional[builtins.str]:
        '''The name for the composite alarm.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alarmName"))

    @alarm_name.setter
    def alarm_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bae9a025d5364aad3383cb09745b81ba3d0a684c7d80304295a0b7f668d191b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alarmName", value)

    @builtins.property
    @jsii.member(jsii_name="insufficientDataActions")
    def insufficient_data_actions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The actions to execute when this alarm transitions to the INSUFFICIENT_DATA state from any other state.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "insufficientDataActions"))

    @insufficient_data_actions.setter
    def insufficient_data_actions(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3202031aa3ce5a8e5bb11c41944febb49ef69bfd275589ad920d63e8166038bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "insufficientDataActions", value)

    @builtins.property
    @jsii.member(jsii_name="okActions")
    def ok_actions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The actions to execute when this alarm transitions to the OK state from any other state.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "okActions"))

    @ok_actions.setter
    def ok_actions(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f061adaf1332cbeeb6cedda66357d6a65aea2023583d23de2ed9b9c193d8e7e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "okActions", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of key-value pairs to associate with the alarm.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__457680b612885bf2c4b88aebcb2510b437690fdf7d6235bf00d83846c1ee3452)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudwatch.CfnCompositeAlarmProps",
    jsii_struct_bases=[],
    name_mapping={
        "alarm_rule": "alarmRule",
        "actions_enabled": "actionsEnabled",
        "actions_suppressor": "actionsSuppressor",
        "actions_suppressor_extension_period": "actionsSuppressorExtensionPeriod",
        "actions_suppressor_wait_period": "actionsSuppressorWaitPeriod",
        "alarm_actions": "alarmActions",
        "alarm_description": "alarmDescription",
        "alarm_name": "alarmName",
        "insufficient_data_actions": "insufficientDataActions",
        "ok_actions": "okActions",
        "tags": "tags",
    },
)
class CfnCompositeAlarmProps:
    def __init__(
        self,
        *,
        alarm_rule: builtins.str,
        actions_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        actions_suppressor: typing.Optional[builtins.str] = None,
        actions_suppressor_extension_period: typing.Optional[jsii.Number] = None,
        actions_suppressor_wait_period: typing.Optional[jsii.Number] = None,
        alarm_actions: typing.Optional[typing.Sequence[builtins.str]] = None,
        alarm_description: typing.Optional[builtins.str] = None,
        alarm_name: typing.Optional[builtins.str] = None,
        insufficient_data_actions: typing.Optional[typing.Sequence[builtins.str]] = None,
        ok_actions: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnCompositeAlarm``.

        :param alarm_rule: An expression that specifies which other alarms are to be evaluated to determine this composite alarm's state. For each alarm that you reference, you designate a function that specifies whether that alarm needs to be in ALARM state, OK state, or INSUFFICIENT_DATA state. You can use operators (AND, OR and NOT) to combine multiple functions in a single expression. You can use parenthesis to logically group the functions in your expression. You can use either alarm names or ARNs to reference the other alarms that are to be evaluated. Functions can include the following: - ALARM("alarm-name or alarm-ARN") is TRUE if the named alarm is in ALARM state. - OK("alarm-name or alarm-ARN") is TRUE if the named alarm is in OK state. - INSUFFICIENT_DATA("alarm-name or alarm-ARN") is TRUE if the named alarm is in INSUFFICIENT_DATA state. - TRUE always evaluates to TRUE. - FALSE always evaluates to FALSE. TRUE and FALSE are useful for testing a complex AlarmRule structure, and for testing your alarm actions. For more information about ``AlarmRule`` syntax, see `PutCompositeAlarm <https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutCompositeAlarm.html>`_ in the *Amazon CloudWatch API Reference* .
        :param actions_enabled: Indicates whether actions should be executed during any changes to the alarm state of the composite alarm. The default is TRUE.
        :param actions_suppressor: Actions will be suppressed if the suppressor alarm is in the ``ALARM`` state. ``ActionsSuppressor`` can be an AlarmName or an Amazon Resource Name (ARN) from an existing alarm.
        :param actions_suppressor_extension_period: The maximum time in seconds that the composite alarm waits after suppressor alarm goes out of the ``ALARM`` state. After this time, the composite alarm performs its actions. .. epigraph:: ``ExtensionPeriod`` is required only when ``ActionsSuppressor`` is specified.
        :param actions_suppressor_wait_period: The maximum time in seconds that the composite alarm waits for the suppressor alarm to go into the ``ALARM`` state. After this time, the composite alarm performs its actions. .. epigraph:: ``WaitPeriod`` is required only when ``ActionsSuppressor`` is specified.
        :param alarm_actions: The actions to execute when this alarm transitions to the ALARM state from any other state. Each action is specified as an Amazon Resource Name (ARN). For more information about creating alarms and the actions that you can specify, see `PutCompositeAlarm <https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutCompositeAlarm.html>`_ in the *Amazon CloudWatch API Reference* .
        :param alarm_description: The description for the composite alarm.
        :param alarm_name: The name for the composite alarm. This name must be unique within your AWS account.
        :param insufficient_data_actions: The actions to execute when this alarm transitions to the INSUFFICIENT_DATA state from any other state. Each action is specified as an Amazon Resource Name (ARN). For more information about creating alarms and the actions that you can specify, see `PutCompositeAlarm <https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutCompositeAlarm.html>`_ in the *Amazon CloudWatch API Reference* .
        :param ok_actions: The actions to execute when this alarm transitions to the OK state from any other state. Each action is specified as an Amazon Resource Name (ARN). For more information about creating alarms and the actions that you can specify, see `PutCompositeAlarm <https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutCompositeAlarm.html>`_ in the *Amazon CloudWatch API Reference* .
        :param tags: A list of key-value pairs to associate with the alarm. You can associate as many as 50 tags with an alarm. To be able to associate tags with the alarm when you create the alarm, you must have the ``cloudwatch:TagResource`` permission. Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-compositealarm.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cloudwatch as cloudwatch
            
            cfn_composite_alarm_props = cloudwatch.CfnCompositeAlarmProps(
                alarm_rule="alarmRule",
            
                # the properties below are optional
                actions_enabled=False,
                actions_suppressor="actionsSuppressor",
                actions_suppressor_extension_period=123,
                actions_suppressor_wait_period=123,
                alarm_actions=["alarmActions"],
                alarm_description="alarmDescription",
                alarm_name="alarmName",
                insufficient_data_actions=["insufficientDataActions"],
                ok_actions=["okActions"],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f61e2b790710dde8e1d3a57752c99da295b632afeb42e0870113583f0277be2c)
            check_type(argname="argument alarm_rule", value=alarm_rule, expected_type=type_hints["alarm_rule"])
            check_type(argname="argument actions_enabled", value=actions_enabled, expected_type=type_hints["actions_enabled"])
            check_type(argname="argument actions_suppressor", value=actions_suppressor, expected_type=type_hints["actions_suppressor"])
            check_type(argname="argument actions_suppressor_extension_period", value=actions_suppressor_extension_period, expected_type=type_hints["actions_suppressor_extension_period"])
            check_type(argname="argument actions_suppressor_wait_period", value=actions_suppressor_wait_period, expected_type=type_hints["actions_suppressor_wait_period"])
            check_type(argname="argument alarm_actions", value=alarm_actions, expected_type=type_hints["alarm_actions"])
            check_type(argname="argument alarm_description", value=alarm_description, expected_type=type_hints["alarm_description"])
            check_type(argname="argument alarm_name", value=alarm_name, expected_type=type_hints["alarm_name"])
            check_type(argname="argument insufficient_data_actions", value=insufficient_data_actions, expected_type=type_hints["insufficient_data_actions"])
            check_type(argname="argument ok_actions", value=ok_actions, expected_type=type_hints["ok_actions"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "alarm_rule": alarm_rule,
        }
        if actions_enabled is not None:
            self._values["actions_enabled"] = actions_enabled
        if actions_suppressor is not None:
            self._values["actions_suppressor"] = actions_suppressor
        if actions_suppressor_extension_period is not None:
            self._values["actions_suppressor_extension_period"] = actions_suppressor_extension_period
        if actions_suppressor_wait_period is not None:
            self._values["actions_suppressor_wait_period"] = actions_suppressor_wait_period
        if alarm_actions is not None:
            self._values["alarm_actions"] = alarm_actions
        if alarm_description is not None:
            self._values["alarm_description"] = alarm_description
        if alarm_name is not None:
            self._values["alarm_name"] = alarm_name
        if insufficient_data_actions is not None:
            self._values["insufficient_data_actions"] = insufficient_data_actions
        if ok_actions is not None:
            self._values["ok_actions"] = ok_actions
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def alarm_rule(self) -> builtins.str:
        '''An expression that specifies which other alarms are to be evaluated to determine this composite alarm's state.

        For each alarm that you reference, you designate a function that specifies whether that alarm needs to be in ALARM state, OK state, or INSUFFICIENT_DATA state. You can use operators (AND, OR and NOT) to combine multiple functions in a single expression. You can use parenthesis to logically group the functions in your expression.

        You can use either alarm names or ARNs to reference the other alarms that are to be evaluated.

        Functions can include the following:

        - ALARM("alarm-name or alarm-ARN") is TRUE if the named alarm is in ALARM state.
        - OK("alarm-name or alarm-ARN") is TRUE if the named alarm is in OK state.
        - INSUFFICIENT_DATA("alarm-name or alarm-ARN") is TRUE if the named alarm is in INSUFFICIENT_DATA state.
        - TRUE always evaluates to TRUE.
        - FALSE always evaluates to FALSE.

        TRUE and FALSE are useful for testing a complex AlarmRule structure, and for testing your alarm actions.

        For more information about ``AlarmRule`` syntax, see `PutCompositeAlarm <https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutCompositeAlarm.html>`_ in the *Amazon CloudWatch API Reference* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-compositealarm.html#cfn-cloudwatch-compositealarm-alarmrule
        '''
        result = self._values.get("alarm_rule")
        assert result is not None, "Required property 'alarm_rule' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def actions_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Indicates whether actions should be executed during any changes to the alarm state of the composite alarm.

        The default is TRUE.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-compositealarm.html#cfn-cloudwatch-compositealarm-actionsenabled
        '''
        result = self._values.get("actions_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def actions_suppressor(self) -> typing.Optional[builtins.str]:
        '''Actions will be suppressed if the suppressor alarm is in the ``ALARM`` state.

        ``ActionsSuppressor`` can be an AlarmName or an Amazon Resource Name (ARN) from an existing alarm.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-compositealarm.html#cfn-cloudwatch-compositealarm-actionssuppressor
        '''
        result = self._values.get("actions_suppressor")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def actions_suppressor_extension_period(self) -> typing.Optional[jsii.Number]:
        '''The maximum time in seconds that the composite alarm waits after suppressor alarm goes out of the ``ALARM`` state.

        After this time, the composite alarm performs its actions.
        .. epigraph::

           ``ExtensionPeriod`` is required only when ``ActionsSuppressor`` is specified.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-compositealarm.html#cfn-cloudwatch-compositealarm-actionssuppressorextensionperiod
        '''
        result = self._values.get("actions_suppressor_extension_period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def actions_suppressor_wait_period(self) -> typing.Optional[jsii.Number]:
        '''The maximum time in seconds that the composite alarm waits for the suppressor alarm to go into the ``ALARM`` state.

        After this time, the composite alarm performs its actions.
        .. epigraph::

           ``WaitPeriod`` is required only when ``ActionsSuppressor`` is specified.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-compositealarm.html#cfn-cloudwatch-compositealarm-actionssuppressorwaitperiod
        '''
        result = self._values.get("actions_suppressor_wait_period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def alarm_actions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The actions to execute when this alarm transitions to the ALARM state from any other state.

        Each action is specified as an Amazon Resource Name (ARN). For more information about creating alarms and the actions that you can specify, see `PutCompositeAlarm <https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutCompositeAlarm.html>`_ in the *Amazon CloudWatch API Reference* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-compositealarm.html#cfn-cloudwatch-compositealarm-alarmactions
        '''
        result = self._values.get("alarm_actions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def alarm_description(self) -> typing.Optional[builtins.str]:
        '''The description for the composite alarm.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-compositealarm.html#cfn-cloudwatch-compositealarm-alarmdescription
        '''
        result = self._values.get("alarm_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def alarm_name(self) -> typing.Optional[builtins.str]:
        '''The name for the composite alarm.

        This name must be unique within your AWS account.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-compositealarm.html#cfn-cloudwatch-compositealarm-alarmname
        '''
        result = self._values.get("alarm_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def insufficient_data_actions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The actions to execute when this alarm transitions to the INSUFFICIENT_DATA state from any other state.

        Each action is specified as an Amazon Resource Name (ARN). For more information about creating alarms and the actions that you can specify, see `PutCompositeAlarm <https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutCompositeAlarm.html>`_ in the *Amazon CloudWatch API Reference* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-compositealarm.html#cfn-cloudwatch-compositealarm-insufficientdataactions
        '''
        result = self._values.get("insufficient_data_actions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def ok_actions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The actions to execute when this alarm transitions to the OK state from any other state.

        Each action is specified as an Amazon Resource Name (ARN). For more information about creating alarms and the actions that you can specify, see `PutCompositeAlarm <https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutCompositeAlarm.html>`_ in the *Amazon CloudWatch API Reference* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-compositealarm.html#cfn-cloudwatch-compositealarm-okactions
        '''
        result = self._values.get("ok_actions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of key-value pairs to associate with the alarm.

        You can associate as many as 50 tags with an alarm. To be able to associate tags with the alarm when you create the alarm, you must have the ``cloudwatch:TagResource`` permission.

        Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-compositealarm.html#cfn-cloudwatch-compositealarm-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCompositeAlarmProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnDashboard(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudwatch.CfnDashboard",
):
    '''The ``AWS::CloudWatch::Dashboard`` resource specifies an Amazon CloudWatch dashboard.

    A dashboard is a customizable home page in the CloudWatch console that you can use to monitor your AWS resources in a single view.

    All dashboards in your account are global, not region-specific.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-dashboard.html
    :cloudformationResource: AWS::CloudWatch::Dashboard
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_cloudwatch as cloudwatch
        
        cfn_dashboard = cloudwatch.CfnDashboard(self, "MyCfnDashboard",
            dashboard_body="dashboardBody",
        
            # the properties below are optional
            dashboard_name="dashboardName"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        dashboard_body: builtins.str,
        dashboard_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param dashboard_body: The detailed information about the dashboard in JSON format, including the widgets to include and their location on the dashboard. This parameter is required. For more information about the syntax, see `Dashboard Body Structure and Syntax <https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/CloudWatch-Dashboard-Body-Structure.html>`_ .
        :param dashboard_name: The name of the dashboard. The name must be between 1 and 255 characters. If you do not specify a name, one will be generated automatically.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5add67d5fc6c551e627bade2623b719ee8c8de03ff6216bc3471bbe529821b66)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDashboardProps(
            dashboard_body=dashboard_body, dashboard_name=dashboard_name
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea2b521a69d5f78d24dc5aba9c387baa4fc450da2dc68bb876531861ee0929b2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2ce11f5733e6656fe8931f571c3719842e64f032f829682b3282f6a1b8f67e06)
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
    @jsii.member(jsii_name="dashboardBody")
    def dashboard_body(self) -> builtins.str:
        '''The detailed information about the dashboard in JSON format, including the widgets to include and their location on the dashboard.'''
        return typing.cast(builtins.str, jsii.get(self, "dashboardBody"))

    @dashboard_body.setter
    def dashboard_body(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a865365ce6c92cb381923f9ec71606f45f52c25334fd65ce166ec545a411b9d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dashboardBody", value)

    @builtins.property
    @jsii.member(jsii_name="dashboardName")
    def dashboard_name(self) -> typing.Optional[builtins.str]:
        '''The name of the dashboard.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dashboardName"))

    @dashboard_name.setter
    def dashboard_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07330e06be9439e4eb97f9c714be0b2c8c09a55b7ef93d990e58a14e431f65eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dashboardName", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudwatch.CfnDashboardProps",
    jsii_struct_bases=[],
    name_mapping={
        "dashboard_body": "dashboardBody",
        "dashboard_name": "dashboardName",
    },
)
class CfnDashboardProps:
    def __init__(
        self,
        *,
        dashboard_body: builtins.str,
        dashboard_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnDashboard``.

        :param dashboard_body: The detailed information about the dashboard in JSON format, including the widgets to include and their location on the dashboard. This parameter is required. For more information about the syntax, see `Dashboard Body Structure and Syntax <https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/CloudWatch-Dashboard-Body-Structure.html>`_ .
        :param dashboard_name: The name of the dashboard. The name must be between 1 and 255 characters. If you do not specify a name, one will be generated automatically.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-dashboard.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cloudwatch as cloudwatch
            
            cfn_dashboard_props = cloudwatch.CfnDashboardProps(
                dashboard_body="dashboardBody",
            
                # the properties below are optional
                dashboard_name="dashboardName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42d47a219edd6b2c040597f718bfa93d023a9554d8079e5c8295ecd47caee4ca)
            check_type(argname="argument dashboard_body", value=dashboard_body, expected_type=type_hints["dashboard_body"])
            check_type(argname="argument dashboard_name", value=dashboard_name, expected_type=type_hints["dashboard_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "dashboard_body": dashboard_body,
        }
        if dashboard_name is not None:
            self._values["dashboard_name"] = dashboard_name

    @builtins.property
    def dashboard_body(self) -> builtins.str:
        '''The detailed information about the dashboard in JSON format, including the widgets to include and their location on the dashboard.

        This parameter is required.

        For more information about the syntax, see `Dashboard Body Structure and Syntax <https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/CloudWatch-Dashboard-Body-Structure.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-dashboard.html#cfn-cloudwatch-dashboard-dashboardbody
        '''
        result = self._values.get("dashboard_body")
        assert result is not None, "Required property 'dashboard_body' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dashboard_name(self) -> typing.Optional[builtins.str]:
        '''The name of the dashboard.

        The name must be between 1 and 255 characters. If you do not specify a name, one will be generated automatically.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-dashboard.html#cfn-cloudwatch-dashboard-dashboardname
        '''
        result = self._values.get("dashboard_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDashboardProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnInsightRule(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudwatch.CfnInsightRule",
):
    '''Creates or updates a Contributor Insights rule.

    Rules evaluate log events in a CloudWatch Logs log group, enabling you to find contributor data for the log events in that log group. For more information, see `Using Contributor Insights to Analyze High-Cardinality Data <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContributorInsights.html>`_ in the *Amazon CloudWatch User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-insightrule.html
    :cloudformationResource: AWS::CloudWatch::InsightRule
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_cloudwatch as cloudwatch
        
        cfn_insight_rule = cloudwatch.CfnInsightRule(self, "MyCfnInsightRule",
            rule_body="ruleBody",
            rule_name="ruleName",
            rule_state="ruleState",
        
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
        rule_body: builtins.str,
        rule_name: builtins.str,
        rule_state: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param rule_body: The definition of the rule, as a JSON object. For details about the syntax, see `Contributor Insights Rule Syntax <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContributorInsights-RuleSyntax.html>`_ in the *Amazon CloudWatch User Guide* .
        :param rule_name: The name of the rule.
        :param rule_state: The current state of the rule. Valid values are ``ENABLED`` and ``DISABLED`` .
        :param tags: A list of key-value pairs to associate with the Contributor Insights rule. You can associate as many as 50 tags with a rule. Tags can help you organize and categorize your resources. For more information, see `Tagging Your Amazon CloudWatch Resources <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Tagging.html>`_ . To be able to associate tags with a rule, you must have the ``cloudwatch:TagResource`` permission in addition to the ``cloudwatch:PutInsightRule`` permission.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d177572b447b5b9761effd52cd14b4510ca4c8fc8607968bdc5e0bd8deae855)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnInsightRuleProps(
            rule_body=rule_body, rule_name=rule_name, rule_state=rule_state, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cba00200e260114593f7b73e5266f02b1427404baba75fd95d8aed05d7f2b685)
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
            type_hints = typing.get_type_hints(_typecheckingstub__85b06cd7db59c69ce5f4eeed03813e201c4d3359daf90d04d6607b73d60e27cb)
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
        '''The ARN of the Contributor Insights rule, such as ``arn:aws:cloudwatch:us-west-2:123456789012:insight-rule/MyInsightRuleName`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrRuleName")
    def attr_rule_name(self) -> builtins.str:
        '''The name of the Contributor Insights rule.

        :cloudformationAttribute: RuleName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRuleName"))

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
    @jsii.member(jsii_name="ruleBody")
    def rule_body(self) -> builtins.str:
        '''The definition of the rule, as a JSON object.'''
        return typing.cast(builtins.str, jsii.get(self, "ruleBody"))

    @rule_body.setter
    def rule_body(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e43a5d364bdee89deaa1521057666bc0592788c8b09eb4a4a1368a9983955ab9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleBody", value)

    @builtins.property
    @jsii.member(jsii_name="ruleName")
    def rule_name(self) -> builtins.str:
        '''The name of the rule.'''
        return typing.cast(builtins.str, jsii.get(self, "ruleName"))

    @rule_name.setter
    def rule_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb020ce7ae390a51012545e5480226be8351f5fa9dd387e75ff1ee669883417a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleName", value)

    @builtins.property
    @jsii.member(jsii_name="ruleState")
    def rule_state(self) -> builtins.str:
        '''The current state of the rule.'''
        return typing.cast(builtins.str, jsii.get(self, "ruleState"))

    @rule_state.setter
    def rule_state(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45517418d6e99e8c2af45e33f2d1375212c73bac3d2c9599691ac383edef3c3b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleState", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of key-value pairs to associate with the Contributor Insights rule.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d330e494e47f68df8f1753b4e301d3df252f832725f14292abf5fa4ee104054)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudwatch.CfnInsightRuleProps",
    jsii_struct_bases=[],
    name_mapping={
        "rule_body": "ruleBody",
        "rule_name": "ruleName",
        "rule_state": "ruleState",
        "tags": "tags",
    },
)
class CfnInsightRuleProps:
    def __init__(
        self,
        *,
        rule_body: builtins.str,
        rule_name: builtins.str,
        rule_state: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnInsightRule``.

        :param rule_body: The definition of the rule, as a JSON object. For details about the syntax, see `Contributor Insights Rule Syntax <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContributorInsights-RuleSyntax.html>`_ in the *Amazon CloudWatch User Guide* .
        :param rule_name: The name of the rule.
        :param rule_state: The current state of the rule. Valid values are ``ENABLED`` and ``DISABLED`` .
        :param tags: A list of key-value pairs to associate with the Contributor Insights rule. You can associate as many as 50 tags with a rule. Tags can help you organize and categorize your resources. For more information, see `Tagging Your Amazon CloudWatch Resources <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Tagging.html>`_ . To be able to associate tags with a rule, you must have the ``cloudwatch:TagResource`` permission in addition to the ``cloudwatch:PutInsightRule`` permission.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-insightrule.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cloudwatch as cloudwatch
            
            cfn_insight_rule_props = cloudwatch.CfnInsightRuleProps(
                rule_body="ruleBody",
                rule_name="ruleName",
                rule_state="ruleState",
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea720192b6c423ff900f4b69425db7a31e90fed21a852500910edce4589cfb7c)
            check_type(argname="argument rule_body", value=rule_body, expected_type=type_hints["rule_body"])
            check_type(argname="argument rule_name", value=rule_name, expected_type=type_hints["rule_name"])
            check_type(argname="argument rule_state", value=rule_state, expected_type=type_hints["rule_state"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "rule_body": rule_body,
            "rule_name": rule_name,
            "rule_state": rule_state,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def rule_body(self) -> builtins.str:
        '''The definition of the rule, as a JSON object.

        For details about the syntax, see `Contributor Insights Rule Syntax <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContributorInsights-RuleSyntax.html>`_ in the *Amazon CloudWatch User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-insightrule.html#cfn-cloudwatch-insightrule-rulebody
        '''
        result = self._values.get("rule_body")
        assert result is not None, "Required property 'rule_body' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rule_name(self) -> builtins.str:
        '''The name of the rule.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-insightrule.html#cfn-cloudwatch-insightrule-rulename
        '''
        result = self._values.get("rule_name")
        assert result is not None, "Required property 'rule_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rule_state(self) -> builtins.str:
        '''The current state of the rule.

        Valid values are ``ENABLED`` and ``DISABLED`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-insightrule.html#cfn-cloudwatch-insightrule-rulestate
        '''
        result = self._values.get("rule_state")
        assert result is not None, "Required property 'rule_state' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of key-value pairs to associate with the Contributor Insights rule.

        You can associate as many as 50 tags with a rule.

        Tags can help you organize and categorize your resources. For more information, see `Tagging Your Amazon CloudWatch Resources <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Tagging.html>`_ .

        To be able to associate tags with a rule, you must have the ``cloudwatch:TagResource`` permission in addition to the ``cloudwatch:PutInsightRule`` permission.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-insightrule.html#cfn-cloudwatch-insightrule-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnInsightRuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnMetricStream(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudwatch.CfnMetricStream",
):
    '''Creates or updates a metric stream.

    Metrics streams can automatically stream CloudWatch metrics to AWS destinations including Amazon S3 and to many third-party solutions. For more information, see `Metric streams <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Metric-Streams.html>`_ .

    To create a metric stream, you must be logged on to an account that has the ``iam:PassRole`` permission and either the *CloudWatchFullAccess* policy or the ``cloudwatch:PutMetricStream`` permission.

    When you create or update a metric stream, you choose one of the following:

    - Stream metrics from all metric namespaces in the account.
    - Stream metrics from all metric namespaces in the account, except for the namespaces that you list in ``ExcludeFilters`` .
    - Stream metrics from only the metric namespaces that you list in ``IncludeFilters`` .

    When you create a metric stream, the stream is created in the ``running`` state. If you update an existing metric stream, the state does not change.

    If you create a metric stream in an account that has been set up as a monitoring account in CloudWatch cross-account observability, you can choose whether to include metrics from linked source accounts in the metric stream.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-metricstream.html
    :cloudformationResource: AWS::CloudWatch::MetricStream
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_cloudwatch as cloudwatch
        
        cfn_metric_stream = cloudwatch.CfnMetricStream(self, "MyCfnMetricStream",
            firehose_arn="firehoseArn",
            output_format="outputFormat",
            role_arn="roleArn",
        
            # the properties below are optional
            exclude_filters=[cloudwatch.CfnMetricStream.MetricStreamFilterProperty(
                namespace="namespace",
        
                # the properties below are optional
                metric_names=["metricNames"]
            )],
            include_filters=[cloudwatch.CfnMetricStream.MetricStreamFilterProperty(
                namespace="namespace",
        
                # the properties below are optional
                metric_names=["metricNames"]
            )],
            include_linked_accounts_metrics=False,
            name="name",
            statistics_configurations=[cloudwatch.CfnMetricStream.MetricStreamStatisticsConfigurationProperty(
                additional_statistics=["additionalStatistics"],
                include_metrics=[cloudwatch.CfnMetricStream.MetricStreamStatisticsMetricProperty(
                    metric_name="metricName",
                    namespace="namespace"
                )]
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
        firehose_arn: builtins.str,
        output_format: builtins.str,
        role_arn: builtins.str,
        exclude_filters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMetricStream.MetricStreamFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        include_filters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMetricStream.MetricStreamFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        include_linked_accounts_metrics: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        name: typing.Optional[builtins.str] = None,
        statistics_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMetricStream.MetricStreamStatisticsConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param firehose_arn: The ARN of the Amazon Kinesis Firehose delivery stream to use for this metric stream. This Amazon Kinesis Firehose delivery stream must already exist and must be in the same account as the metric stream.
        :param output_format: The output format for the stream. Valid values are ``json`` , ``opentelemetry1.0`` and ``opentelemetry0.7`` For more information about metric stream output formats, see `Metric streams output formats <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-metric-streams-formats.html>`_ . This parameter is required.
        :param role_arn: The ARN of an IAM role that this metric stream will use to access Amazon Kinesis Firehose resources. This IAM role must already exist and must be in the same account as the metric stream. This IAM role must include the ``firehose:PutRecord`` and ``firehose:PutRecordBatch`` permissions.
        :param exclude_filters: If you specify this parameter, the stream sends metrics from all metric namespaces except for the namespaces that you specify here. You cannot specify both ``IncludeFilters`` and ``ExcludeFilters`` in the same metric stream. When you modify the ``IncludeFilters`` or ``ExcludeFilters`` of an existing metric stream in any way, the metric stream is effectively restarted, so after such a change you will get only the datapoints that have a timestamp after the time of the update.
        :param include_filters: If you specify this parameter, the stream sends only the metrics from the metric namespaces that you specify here. You cannot specify both ``IncludeFilters`` and ``ExcludeFilters`` in the same metric stream. When you modify the ``IncludeFilters`` or ``ExcludeFilters`` of an existing metric stream in any way, the metric stream is effectively restarted, so after such a change you will get only the datapoints that have a timestamp after the time of the update.
        :param include_linked_accounts_metrics: If you are creating a metric stream in a monitoring account, specify ``true`` to include metrics from source accounts that are linked to this monitoring account, in the metric stream. The default is ``false`` . For more information about linking accounts, see `CloudWatch cross-account observability <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html>`_
        :param name: If you are creating a new metric stream, this is the name for the new stream. The name must be different than the names of other metric streams in this account and Region. If you are updating a metric stream, specify the name of that stream here.
        :param statistics_configurations: By default, a metric stream always sends the MAX, MIN, SUM, and SAMPLECOUNT statistics for each metric that is streamed. You can use this parameter to have the metric stream also send additional statistics in the stream. This array can have up to 100 members. For each entry in this array, you specify one or more metrics and the list of additional statistics to stream for those metrics. The additional statistics that you can stream depend on the stream's ``OutputFormat`` . If the ``OutputFormat`` is ``json`` , you can stream any additional statistic that is supported by CloudWatch , listed in `CloudWatch statistics definitions <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Statistics-definitions.html>`_ . If the ``OutputFormat`` is OpenTelemetry, you can stream percentile statistics.
        :param tags: An array of key-value pairs to apply to the metric stream. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__324083d9d1c11bed8d2cf8d1d0cab6adbcb8194552cea34115b984457ef131eb)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnMetricStreamProps(
            firehose_arn=firehose_arn,
            output_format=output_format,
            role_arn=role_arn,
            exclude_filters=exclude_filters,
            include_filters=include_filters,
            include_linked_accounts_metrics=include_linked_accounts_metrics,
            name=name,
            statistics_configurations=statistics_configurations,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d75d145801429f4f9f0daaae66adb695e6690f2bd7b00a62aedff30952bef4c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__bc4e04abbe7c420d426a886e2590972a98723e1abf197bd044bef66ef0f366ca)
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
        '''The ARN of the metric stream.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreationDate")
    def attr_creation_date(self) -> builtins.str:
        '''The date that the metric stream was originally created.

        :cloudformationAttribute: CreationDate
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationDate"))

    @builtins.property
    @jsii.member(jsii_name="attrLastUpdateDate")
    def attr_last_update_date(self) -> builtins.str:
        '''The date that the metric stream was most recently updated.

        :cloudformationAttribute: LastUpdateDate
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastUpdateDate"))

    @builtins.property
    @jsii.member(jsii_name="attrState")
    def attr_state(self) -> builtins.str:
        '''The state of the metric stream, either ``running`` or ``stopped`` .

        :cloudformationAttribute: State
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrState"))

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
    @jsii.member(jsii_name="firehoseArn")
    def firehose_arn(self) -> builtins.str:
        '''The ARN of the Amazon Kinesis Firehose delivery stream to use for this metric stream.'''
        return typing.cast(builtins.str, jsii.get(self, "firehoseArn"))

    @firehose_arn.setter
    def firehose_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__303acca869f0b2f0dd33e2a704edc1c9841d282e2c5d6fefab0857984b4a7a14)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "firehoseArn", value)

    @builtins.property
    @jsii.member(jsii_name="outputFormat")
    def output_format(self) -> builtins.str:
        '''The output format for the stream.'''
        return typing.cast(builtins.str, jsii.get(self, "outputFormat"))

    @output_format.setter
    def output_format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7e65744c47b6274b336b0cab06cc0e6fd616351335054e76423aa5e24f60fdb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "outputFormat", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''The ARN of an IAM role that this metric stream will use to access Amazon Kinesis Firehose resources.'''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84ed2e0742cbeea084c4b032aceb0bc50b5b099cfab1446baec0d7580228eda5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="excludeFilters")
    def exclude_filters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnMetricStream.MetricStreamFilterProperty"]]]]:
        '''If you specify this parameter, the stream sends metrics from all metric namespaces except for the namespaces that you specify here.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnMetricStream.MetricStreamFilterProperty"]]]], jsii.get(self, "excludeFilters"))

    @exclude_filters.setter
    def exclude_filters(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnMetricStream.MetricStreamFilterProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8a010b725b9721d5a0070180f728cef097b885a9247729c230c1e48162efb49)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "excludeFilters", value)

    @builtins.property
    @jsii.member(jsii_name="includeFilters")
    def include_filters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnMetricStream.MetricStreamFilterProperty"]]]]:
        '''If you specify this parameter, the stream sends only the metrics from the metric namespaces that you specify here.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnMetricStream.MetricStreamFilterProperty"]]]], jsii.get(self, "includeFilters"))

    @include_filters.setter
    def include_filters(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnMetricStream.MetricStreamFilterProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9fd63e599d47997efeead98c50e00925a352821609b2a35cc5d8286cc277d16d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeFilters", value)

    @builtins.property
    @jsii.member(jsii_name="includeLinkedAccountsMetrics")
    def include_linked_accounts_metrics(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''If you are creating a metric stream in a monitoring account, specify ``true`` to include metrics from source accounts that are linked to this monitoring account, in the metric stream.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "includeLinkedAccountsMetrics"))

    @include_linked_accounts_metrics.setter
    def include_linked_accounts_metrics(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db935a48c332f03a24316c2a8a9a44ae9aee2c31a0f66ccbca7f9645b7f6f148)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeLinkedAccountsMetrics", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''If you are creating a new metric stream, this is the name for the new stream.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ecec6f0d2b2483e898160ef393fb18ddcf4dd3fc4d302c943abaa1e538f6e3f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="statisticsConfigurations")
    def statistics_configurations(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnMetricStream.MetricStreamStatisticsConfigurationProperty"]]]]:
        '''By default, a metric stream always sends the MAX, MIN, SUM, and SAMPLECOUNT statistics for each metric that is streamed.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnMetricStream.MetricStreamStatisticsConfigurationProperty"]]]], jsii.get(self, "statisticsConfigurations"))

    @statistics_configurations.setter
    def statistics_configurations(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnMetricStream.MetricStreamStatisticsConfigurationProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5fccdc8e5b648171c23d1254144728db070b30ea4ff96cea910d95125b8aab0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "statisticsConfigurations", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to the metric stream.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ff12b171ab408aef715723528314a6f2877123297d21c2d3c0cf73a13965ffe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cloudwatch.CfnMetricStream.MetricStreamFilterProperty",
        jsii_struct_bases=[],
        name_mapping={"namespace": "namespace", "metric_names": "metricNames"},
    )
    class MetricStreamFilterProperty:
        def __init__(
            self,
            *,
            namespace: builtins.str,
            metric_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''This structure contains a metric namespace and optionally, a list of metric names, to either include in a metric ' stream or exclude from a metric stream.

            A metric stream's filters can include up to 1000 total names. This limit applies to the sum of namespace names and metric names in the filters. For example, this could include 10 metric namespace filters with 99 metrics each, or 20 namespace filters with 49 metrics specified in each filter.

            :param namespace: The name of the metric namespace in the filter. The namespace can contain only ASCII printable characters (ASCII range 32 through 126). It must contain at least one non-whitespace character.
            :param metric_names: The names of the metrics to either include or exclude from the metric stream. If you omit this parameter, all metrics in the namespace are included or excluded, depending on whether this filter is specified as an exclude filter or an include filter. Each metric name can contain only ASCII printable characters (ASCII range 32 through 126). Each metric name must contain at least one non-whitespace character.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-metricstream-metricstreamfilter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cloudwatch as cloudwatch
                
                metric_stream_filter_property = cloudwatch.CfnMetricStream.MetricStreamFilterProperty(
                    namespace="namespace",
                
                    # the properties below are optional
                    metric_names=["metricNames"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4de34777618ee8ff0a4cfe901b94bf76a91e50ee6a29cf6a17d55887c3348025)
                check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
                check_type(argname="argument metric_names", value=metric_names, expected_type=type_hints["metric_names"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "namespace": namespace,
            }
            if metric_names is not None:
                self._values["metric_names"] = metric_names

        @builtins.property
        def namespace(self) -> builtins.str:
            '''The name of the metric namespace in the filter.

            The namespace can contain only ASCII printable characters (ASCII range 32 through 126). It must contain at least one non-whitespace character.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-metricstream-metricstreamfilter.html#cfn-cloudwatch-metricstream-metricstreamfilter-namespace
            '''
            result = self._values.get("namespace")
            assert result is not None, "Required property 'namespace' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def metric_names(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The names of the metrics to either include or exclude from the metric stream.

            If you omit this parameter, all metrics in the namespace are included or excluded, depending on whether this filter is specified as an exclude filter or an include filter.

            Each metric name can contain only ASCII printable characters (ASCII range 32 through 126). Each metric name must contain at least one non-whitespace character.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-metricstream-metricstreamfilter.html#cfn-cloudwatch-metricstream-metricstreamfilter-metricnames
            '''
            result = self._values.get("metric_names")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MetricStreamFilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cloudwatch.CfnMetricStream.MetricStreamStatisticsConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "additional_statistics": "additionalStatistics",
            "include_metrics": "includeMetrics",
        },
    )
    class MetricStreamStatisticsConfigurationProperty:
        def __init__(
            self,
            *,
            additional_statistics: typing.Sequence[builtins.str],
            include_metrics: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMetricStream.MetricStreamStatisticsMetricProperty", typing.Dict[builtins.str, typing.Any]]]]],
        ) -> None:
            '''This structure specifies a list of additional statistics to stream, and the metrics to stream those additional statistics for.

            All metrics that match the combination of metric name and namespace will be streamed with the additional statistics, no matter their dimensions.

            :param additional_statistics: The additional statistics to stream for the metrics listed in ``IncludeMetrics`` .
            :param include_metrics: An array that defines the metrics that are to have additional statistics streamed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-metricstream-metricstreamstatisticsconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cloudwatch as cloudwatch
                
                metric_stream_statistics_configuration_property = cloudwatch.CfnMetricStream.MetricStreamStatisticsConfigurationProperty(
                    additional_statistics=["additionalStatistics"],
                    include_metrics=[cloudwatch.CfnMetricStream.MetricStreamStatisticsMetricProperty(
                        metric_name="metricName",
                        namespace="namespace"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__014629a07843af45b16fe266381194e9a273db3a2b42bae461f897e5c6c957a9)
                check_type(argname="argument additional_statistics", value=additional_statistics, expected_type=type_hints["additional_statistics"])
                check_type(argname="argument include_metrics", value=include_metrics, expected_type=type_hints["include_metrics"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "additional_statistics": additional_statistics,
                "include_metrics": include_metrics,
            }

        @builtins.property
        def additional_statistics(self) -> typing.List[builtins.str]:
            '''The additional statistics to stream for the metrics listed in ``IncludeMetrics`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-metricstream-metricstreamstatisticsconfiguration.html#cfn-cloudwatch-metricstream-metricstreamstatisticsconfiguration-additionalstatistics
            '''
            result = self._values.get("additional_statistics")
            assert result is not None, "Required property 'additional_statistics' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def include_metrics(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnMetricStream.MetricStreamStatisticsMetricProperty"]]]:
            '''An array that defines the metrics that are to have additional statistics streamed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-metricstream-metricstreamstatisticsconfiguration.html#cfn-cloudwatch-metricstream-metricstreamstatisticsconfiguration-includemetrics
            '''
            result = self._values.get("include_metrics")
            assert result is not None, "Required property 'include_metrics' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnMetricStream.MetricStreamStatisticsMetricProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MetricStreamStatisticsConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cloudwatch.CfnMetricStream.MetricStreamStatisticsMetricProperty",
        jsii_struct_bases=[],
        name_mapping={"metric_name": "metricName", "namespace": "namespace"},
    )
    class MetricStreamStatisticsMetricProperty:
        def __init__(
            self,
            *,
            metric_name: builtins.str,
            namespace: builtins.str,
        ) -> None:
            '''A structure that specifies the metric name and namespace for one metric that is going to have additional statistics included in the stream.

            :param metric_name: The name of the metric.
            :param namespace: The namespace of the metric.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-metricstream-metricstreamstatisticsmetric.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cloudwatch as cloudwatch
                
                metric_stream_statistics_metric_property = cloudwatch.CfnMetricStream.MetricStreamStatisticsMetricProperty(
                    metric_name="metricName",
                    namespace="namespace"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__dd6943836e019c7fb3dffa95c2ffb1b7cb9db587bd9c145bf9373c8ff342926b)
                check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
                check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "metric_name": metric_name,
                "namespace": namespace,
            }

        @builtins.property
        def metric_name(self) -> builtins.str:
            '''The name of the metric.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-metricstream-metricstreamstatisticsmetric.html#cfn-cloudwatch-metricstream-metricstreamstatisticsmetric-metricname
            '''
            result = self._values.get("metric_name")
            assert result is not None, "Required property 'metric_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def namespace(self) -> builtins.str:
            '''The namespace of the metric.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-metricstream-metricstreamstatisticsmetric.html#cfn-cloudwatch-metricstream-metricstreamstatisticsmetric-namespace
            '''
            result = self._values.get("namespace")
            assert result is not None, "Required property 'namespace' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MetricStreamStatisticsMetricProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudwatch.CfnMetricStreamProps",
    jsii_struct_bases=[],
    name_mapping={
        "firehose_arn": "firehoseArn",
        "output_format": "outputFormat",
        "role_arn": "roleArn",
        "exclude_filters": "excludeFilters",
        "include_filters": "includeFilters",
        "include_linked_accounts_metrics": "includeLinkedAccountsMetrics",
        "name": "name",
        "statistics_configurations": "statisticsConfigurations",
        "tags": "tags",
    },
)
class CfnMetricStreamProps:
    def __init__(
        self,
        *,
        firehose_arn: builtins.str,
        output_format: builtins.str,
        role_arn: builtins.str,
        exclude_filters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMetricStream.MetricStreamFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        include_filters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMetricStream.MetricStreamFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        include_linked_accounts_metrics: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        name: typing.Optional[builtins.str] = None,
        statistics_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMetricStream.MetricStreamStatisticsConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnMetricStream``.

        :param firehose_arn: The ARN of the Amazon Kinesis Firehose delivery stream to use for this metric stream. This Amazon Kinesis Firehose delivery stream must already exist and must be in the same account as the metric stream.
        :param output_format: The output format for the stream. Valid values are ``json`` , ``opentelemetry1.0`` and ``opentelemetry0.7`` For more information about metric stream output formats, see `Metric streams output formats <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-metric-streams-formats.html>`_ . This parameter is required.
        :param role_arn: The ARN of an IAM role that this metric stream will use to access Amazon Kinesis Firehose resources. This IAM role must already exist and must be in the same account as the metric stream. This IAM role must include the ``firehose:PutRecord`` and ``firehose:PutRecordBatch`` permissions.
        :param exclude_filters: If you specify this parameter, the stream sends metrics from all metric namespaces except for the namespaces that you specify here. You cannot specify both ``IncludeFilters`` and ``ExcludeFilters`` in the same metric stream. When you modify the ``IncludeFilters`` or ``ExcludeFilters`` of an existing metric stream in any way, the metric stream is effectively restarted, so after such a change you will get only the datapoints that have a timestamp after the time of the update.
        :param include_filters: If you specify this parameter, the stream sends only the metrics from the metric namespaces that you specify here. You cannot specify both ``IncludeFilters`` and ``ExcludeFilters`` in the same metric stream. When you modify the ``IncludeFilters`` or ``ExcludeFilters`` of an existing metric stream in any way, the metric stream is effectively restarted, so after such a change you will get only the datapoints that have a timestamp after the time of the update.
        :param include_linked_accounts_metrics: If you are creating a metric stream in a monitoring account, specify ``true`` to include metrics from source accounts that are linked to this monitoring account, in the metric stream. The default is ``false`` . For more information about linking accounts, see `CloudWatch cross-account observability <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html>`_
        :param name: If you are creating a new metric stream, this is the name for the new stream. The name must be different than the names of other metric streams in this account and Region. If you are updating a metric stream, specify the name of that stream here.
        :param statistics_configurations: By default, a metric stream always sends the MAX, MIN, SUM, and SAMPLECOUNT statistics for each metric that is streamed. You can use this parameter to have the metric stream also send additional statistics in the stream. This array can have up to 100 members. For each entry in this array, you specify one or more metrics and the list of additional statistics to stream for those metrics. The additional statistics that you can stream depend on the stream's ``OutputFormat`` . If the ``OutputFormat`` is ``json`` , you can stream any additional statistic that is supported by CloudWatch , listed in `CloudWatch statistics definitions <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Statistics-definitions.html>`_ . If the ``OutputFormat`` is OpenTelemetry, you can stream percentile statistics.
        :param tags: An array of key-value pairs to apply to the metric stream. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-metricstream.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cloudwatch as cloudwatch
            
            cfn_metric_stream_props = cloudwatch.CfnMetricStreamProps(
                firehose_arn="firehoseArn",
                output_format="outputFormat",
                role_arn="roleArn",
            
                # the properties below are optional
                exclude_filters=[cloudwatch.CfnMetricStream.MetricStreamFilterProperty(
                    namespace="namespace",
            
                    # the properties below are optional
                    metric_names=["metricNames"]
                )],
                include_filters=[cloudwatch.CfnMetricStream.MetricStreamFilterProperty(
                    namespace="namespace",
            
                    # the properties below are optional
                    metric_names=["metricNames"]
                )],
                include_linked_accounts_metrics=False,
                name="name",
                statistics_configurations=[cloudwatch.CfnMetricStream.MetricStreamStatisticsConfigurationProperty(
                    additional_statistics=["additionalStatistics"],
                    include_metrics=[cloudwatch.CfnMetricStream.MetricStreamStatisticsMetricProperty(
                        metric_name="metricName",
                        namespace="namespace"
                    )]
                )],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3841eb4f0098d496658caf6739d964d8b08f872e67d2ad28362ac3882ccd7d74)
            check_type(argname="argument firehose_arn", value=firehose_arn, expected_type=type_hints["firehose_arn"])
            check_type(argname="argument output_format", value=output_format, expected_type=type_hints["output_format"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument exclude_filters", value=exclude_filters, expected_type=type_hints["exclude_filters"])
            check_type(argname="argument include_filters", value=include_filters, expected_type=type_hints["include_filters"])
            check_type(argname="argument include_linked_accounts_metrics", value=include_linked_accounts_metrics, expected_type=type_hints["include_linked_accounts_metrics"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument statistics_configurations", value=statistics_configurations, expected_type=type_hints["statistics_configurations"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "firehose_arn": firehose_arn,
            "output_format": output_format,
            "role_arn": role_arn,
        }
        if exclude_filters is not None:
            self._values["exclude_filters"] = exclude_filters
        if include_filters is not None:
            self._values["include_filters"] = include_filters
        if include_linked_accounts_metrics is not None:
            self._values["include_linked_accounts_metrics"] = include_linked_accounts_metrics
        if name is not None:
            self._values["name"] = name
        if statistics_configurations is not None:
            self._values["statistics_configurations"] = statistics_configurations
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def firehose_arn(self) -> builtins.str:
        '''The ARN of the Amazon Kinesis Firehose delivery stream to use for this metric stream.

        This Amazon Kinesis Firehose delivery stream must already exist and must be in the same account as the metric stream.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-metricstream.html#cfn-cloudwatch-metricstream-firehosearn
        '''
        result = self._values.get("firehose_arn")
        assert result is not None, "Required property 'firehose_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def output_format(self) -> builtins.str:
        '''The output format for the stream.

        Valid values are ``json`` , ``opentelemetry1.0`` and ``opentelemetry0.7`` For more information about metric stream output formats, see `Metric streams output formats <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-metric-streams-formats.html>`_ .

        This parameter is required.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-metricstream.html#cfn-cloudwatch-metricstream-outputformat
        '''
        result = self._values.get("output_format")
        assert result is not None, "Required property 'output_format' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''The ARN of an IAM role that this metric stream will use to access Amazon Kinesis Firehose resources.

        This IAM role must already exist and must be in the same account as the metric stream. This IAM role must include the ``firehose:PutRecord`` and ``firehose:PutRecordBatch`` permissions.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-metricstream.html#cfn-cloudwatch-metricstream-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def exclude_filters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnMetricStream.MetricStreamFilterProperty]]]]:
        '''If you specify this parameter, the stream sends metrics from all metric namespaces except for the namespaces that you specify here.

        You cannot specify both ``IncludeFilters`` and ``ExcludeFilters`` in the same metric stream.

        When you modify the ``IncludeFilters`` or ``ExcludeFilters`` of an existing metric stream in any way, the metric stream is effectively restarted, so after such a change you will get only the datapoints that have a timestamp after the time of the update.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-metricstream.html#cfn-cloudwatch-metricstream-excludefilters
        '''
        result = self._values.get("exclude_filters")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnMetricStream.MetricStreamFilterProperty]]]], result)

    @builtins.property
    def include_filters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnMetricStream.MetricStreamFilterProperty]]]]:
        '''If you specify this parameter, the stream sends only the metrics from the metric namespaces that you specify here.

        You cannot specify both ``IncludeFilters`` and ``ExcludeFilters`` in the same metric stream.

        When you modify the ``IncludeFilters`` or ``ExcludeFilters`` of an existing metric stream in any way, the metric stream is effectively restarted, so after such a change you will get only the datapoints that have a timestamp after the time of the update.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-metricstream.html#cfn-cloudwatch-metricstream-includefilters
        '''
        result = self._values.get("include_filters")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnMetricStream.MetricStreamFilterProperty]]]], result)

    @builtins.property
    def include_linked_accounts_metrics(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''If you are creating a metric stream in a monitoring account, specify ``true`` to include metrics from source accounts that are linked to this monitoring account, in the metric stream.

        The default is ``false`` .

        For more information about linking accounts, see `CloudWatch cross-account observability <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html>`_

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-metricstream.html#cfn-cloudwatch-metricstream-includelinkedaccountsmetrics
        '''
        result = self._values.get("include_linked_accounts_metrics")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''If you are creating a new metric stream, this is the name for the new stream.

        The name must be different than the names of other metric streams in this account and Region.

        If you are updating a metric stream, specify the name of that stream here.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-metricstream.html#cfn-cloudwatch-metricstream-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def statistics_configurations(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnMetricStream.MetricStreamStatisticsConfigurationProperty]]]]:
        '''By default, a metric stream always sends the MAX, MIN, SUM, and SAMPLECOUNT statistics for each metric that is streamed.

        You can use this parameter to have the metric stream also send additional statistics in the stream. This array can have up to 100 members.

        For each entry in this array, you specify one or more metrics and the list of additional statistics to stream for those metrics. The additional statistics that you can stream depend on the stream's ``OutputFormat`` . If the ``OutputFormat`` is ``json`` , you can stream any additional statistic that is supported by CloudWatch , listed in `CloudWatch statistics definitions <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Statistics-definitions.html>`_ . If the ``OutputFormat`` is OpenTelemetry, you can stream percentile statistics.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-metricstream.html#cfn-cloudwatch-metricstream-statisticsconfigurations
        '''
        result = self._values.get("statistics_configurations")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnMetricStream.MetricStreamStatisticsConfigurationProperty]]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to the metric stream.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-metricstream.html#cfn-cloudwatch-metricstream-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMetricStreamProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Color(metaclass=jsii.JSIIMeta, jsii_type="aws-cdk-lib.aws_cloudwatch.Color"):
    '''A set of standard colours that can be used in annotations in a GraphWidget.

    :exampleMetadata: infused

    Example::

        # dashboard: cloudwatch.Dashboard
        
        
        dashboard.add_widgets(cloudwatch.GraphWidget(
            # ...
        
            left_annotations=[cloudwatch.HorizontalAnnotation(value=1800, label=Duration.minutes(30).to_human_string(), color=cloudwatch.Color.RED), cloudwatch.HorizontalAnnotation(value=3600, label="1 hour", color="#2ca02c")
            ],
            vertical_annotations=[cloudwatch.VerticalAnnotation(date="2022-10-19T00:00:00Z", label="Deployment", color=cloudwatch.Color.RED)
            ]
        ))
    '''

    @jsii.python.classproperty
    @jsii.member(jsii_name="BLUE")
    def BLUE(cls) -> builtins.str:
        '''blue - hex #1f77b4.'''
        return typing.cast(builtins.str, jsii.sget(cls, "BLUE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="BROWN")
    def BROWN(cls) -> builtins.str:
        '''brown - hex #8c564b.'''
        return typing.cast(builtins.str, jsii.sget(cls, "BROWN"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="GREEN")
    def GREEN(cls) -> builtins.str:
        '''green - hex #2ca02c.'''
        return typing.cast(builtins.str, jsii.sget(cls, "GREEN"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="GREY")
    def GREY(cls) -> builtins.str:
        '''grey - hex #7f7f7f.'''
        return typing.cast(builtins.str, jsii.sget(cls, "GREY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ORANGE")
    def ORANGE(cls) -> builtins.str:
        '''orange - hex #ff7f0e.'''
        return typing.cast(builtins.str, jsii.sget(cls, "ORANGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PINK")
    def PINK(cls) -> builtins.str:
        '''pink - hex #e377c2.'''
        return typing.cast(builtins.str, jsii.sget(cls, "PINK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PURPLE")
    def PURPLE(cls) -> builtins.str:
        '''purple - hex #9467bd.'''
        return typing.cast(builtins.str, jsii.sget(cls, "PURPLE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="RED")
    def RED(cls) -> builtins.str:
        '''red - hex #d62728.'''
        return typing.cast(builtins.str, jsii.sget(cls, "RED"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudwatch.CommonMetricOptions",
    jsii_struct_bases=[],
    name_mapping={
        "account": "account",
        "color": "color",
        "dimensions_map": "dimensionsMap",
        "label": "label",
        "period": "period",
        "region": "region",
        "statistic": "statistic",
        "unit": "unit",
    },
)
class CommonMetricOptions:
    def __init__(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional["Unit"] = None,
    ) -> None:
        '''Options shared by most methods accepting metric options.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk as cdk
            from aws_cdk import aws_cloudwatch as cloudwatch
            
            common_metric_options = cloudwatch.CommonMetricOptions(
                account="account",
                color="color",
                dimensions_map={
                    "dimensions_map_key": "dimensionsMap"
                },
                label="label",
                period=cdk.Duration.minutes(30),
                region="region",
                statistic="statistic",
                unit=cloudwatch.Unit.SECONDS
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd18f372aac3bb8d4a678dd4ee7a3b5bd34447637695b896086139ee2b7b4a19)
            check_type(argname="argument account", value=account, expected_type=type_hints["account"])
            check_type(argname="argument color", value=color, expected_type=type_hints["color"])
            check_type(argname="argument dimensions_map", value=dimensions_map, expected_type=type_hints["dimensions_map"])
            check_type(argname="argument label", value=label, expected_type=type_hints["label"])
            check_type(argname="argument period", value=period, expected_type=type_hints["period"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument statistic", value=statistic, expected_type=type_hints["statistic"])
            check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if account is not None:
            self._values["account"] = account
        if color is not None:
            self._values["color"] = color
        if dimensions_map is not None:
            self._values["dimensions_map"] = dimensions_map
        if label is not None:
            self._values["label"] = label
        if period is not None:
            self._values["period"] = period
        if region is not None:
            self._values["region"] = region
        if statistic is not None:
            self._values["statistic"] = statistic
        if unit is not None:
            self._values["unit"] = unit

    @builtins.property
    def account(self) -> typing.Optional[builtins.str]:
        '''Account which this metric comes from.

        :default: - Deployment account.
        '''
        result = self._values.get("account")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def color(self) -> typing.Optional[builtins.str]:
        '''The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here.

        :default: - Automatic color
        '''
        result = self._values.get("color")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dimensions_map(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Dimensions of the metric.

        :default: - No dimensions.
        '''
        result = self._values.get("dimensions_map")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def label(self) -> typing.Optional[builtins.str]:
        '''Label for this metric when added to a Graph in a Dashboard.

        You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_
        to show summary information about the entire displayed time series
        in the legend. For example, if you use::

           [max: ${MAX}] MyMetric

        As the metric label, the maximum value in the visible range will
        be shown next to the time series name in the graph's legend.

        :default: - No label
        '''
        result = self._values.get("label")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def period(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The period over which the specified statistic is applied.

        :default: Duration.minutes(5)
        '''
        result = self._values.get("period")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''Region which this metric comes from.

        :default: - Deployment region.
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def statistic(self) -> typing.Optional[builtins.str]:
        '''What function to use for aggregating.

        Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings.

        Can be one of the following:

        - "Minimum" | "min"
        - "Maximum" | "max"
        - "Average" | "avg"
        - "Sum" | "sum"
        - "SampleCount | "n"
        - "pNN.NN"
        - "tmNN.NN" | "tm(NN.NN%:NN.NN%)"
        - "iqm"
        - "wmNN.NN" | "wm(NN.NN%:NN.NN%)"
        - "tcNN.NN" | "tc(NN.NN%:NN.NN%)"
        - "tsNN.NN" | "ts(NN.NN%:NN.NN%)"

        :default: Average
        '''
        result = self._values.get("statistic")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def unit(self) -> typing.Optional["Unit"]:
        '''Unit used to filter the metric stream.

        Only refer to datums emitted to the metric stream with the given unit and
        ignore all others. Only useful when datums are being emitted to the same
        metric stream under different units.

        The default is to use all matric datums in the stream, regardless of unit,
        which is recommended in nearly all cases.

        CloudWatch does not honor this property for graphs.

        :default: - All metric datums in the given metric stream
        '''
        result = self._values.get("unit")
        return typing.cast(typing.Optional["Unit"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CommonMetricOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_cloudwatch.ComparisonOperator")
class ComparisonOperator(enum.Enum):
    '''Comparison operator for evaluating alarms.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_cloudwatch as cloudwatch
        
        # my_hosted_zone: route53.HostedZone
        
        certificate = acm.Certificate(self, "Certificate",
            domain_name="hello.example.com",
            validation=acm.CertificateValidation.from_dns(my_hosted_zone)
        )
        certificate.metric_days_to_expiry().create_alarm(self, "Alarm",
            comparison_operator=cloudwatch.ComparisonOperator.LESS_THAN_THRESHOLD,
            evaluation_periods=1,
            threshold=45
        )
    '''

    GREATER_THAN_OR_EQUAL_TO_THRESHOLD = "GREATER_THAN_OR_EQUAL_TO_THRESHOLD"
    '''Specified statistic is greater than or equal to the threshold.'''
    GREATER_THAN_THRESHOLD = "GREATER_THAN_THRESHOLD"
    '''Specified statistic is strictly greater than the threshold.'''
    LESS_THAN_THRESHOLD = "LESS_THAN_THRESHOLD"
    '''Specified statistic is strictly less than the threshold.'''
    LESS_THAN_OR_EQUAL_TO_THRESHOLD = "LESS_THAN_OR_EQUAL_TO_THRESHOLD"
    '''Specified statistic is less than or equal to the threshold.'''
    LESS_THAN_LOWER_OR_GREATER_THAN_UPPER_THRESHOLD = "LESS_THAN_LOWER_OR_GREATER_THAN_UPPER_THRESHOLD"
    '''Specified statistic is lower than or greater than the anomaly model band.

    Used only for alarms based on anomaly detection models
    '''
    GREATER_THAN_UPPER_THRESHOLD = "GREATER_THAN_UPPER_THRESHOLD"
    '''Specified statistic is greater than the anomaly model band.

    Used only for alarms based on anomaly detection models
    '''
    LESS_THAN_LOWER_THRESHOLD = "LESS_THAN_LOWER_THRESHOLD"
    '''Specified statistic is lower than the anomaly model band.

    Used only for alarms based on anomaly detection models
    '''


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudwatch.CompositeAlarmProps",
    jsii_struct_bases=[],
    name_mapping={
        "alarm_rule": "alarmRule",
        "actions_enabled": "actionsEnabled",
        "actions_suppressor": "actionsSuppressor",
        "actions_suppressor_extension_period": "actionsSuppressorExtensionPeriod",
        "actions_suppressor_wait_period": "actionsSuppressorWaitPeriod",
        "alarm_description": "alarmDescription",
        "composite_alarm_name": "compositeAlarmName",
    },
)
class CompositeAlarmProps:
    def __init__(
        self,
        *,
        alarm_rule: "IAlarmRule",
        actions_enabled: typing.Optional[builtins.bool] = None,
        actions_suppressor: typing.Optional["IAlarm"] = None,
        actions_suppressor_extension_period: typing.Optional[_Duration_4839e8c3] = None,
        actions_suppressor_wait_period: typing.Optional[_Duration_4839e8c3] = None,
        alarm_description: typing.Optional[builtins.str] = None,
        composite_alarm_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for creating a Composite Alarm.

        :param alarm_rule: Expression that specifies which other alarms are to be evaluated to determine this composite alarm's state.
        :param actions_enabled: Whether the actions for this alarm are enabled. Default: true
        :param actions_suppressor: Actions will be suppressed if the suppressor alarm is in the ALARM state. Default: - alarm will not be suppressed.
        :param actions_suppressor_extension_period: The maximum duration that the composite alarm waits after suppressor alarm goes out of the ALARM state. After this time, the composite alarm performs its actions. Default: - 1 minute extension period will be set.
        :param actions_suppressor_wait_period: The maximum duration that the composite alarm waits for the suppressor alarm to go into the ALARM state. After this time, the composite alarm performs its actions. Default: - 1 minute wait period will be set.
        :param alarm_description: Description for the alarm. Default: - No description.
        :param composite_alarm_name: Name of the alarm. Default: - Automatically generated name.

        :exampleMetadata: infused

        Example::

            # alarm1: cloudwatch.Alarm
            # alarm2: cloudwatch.Alarm
            # alarm3: cloudwatch.Alarm
            # alarm4: cloudwatch.Alarm
            
            
            alarm_rule = cloudwatch.AlarmRule.any_of(
                cloudwatch.AlarmRule.all_of(
                    cloudwatch.AlarmRule.any_of(alarm1,
                        cloudwatch.AlarmRule.from_alarm(alarm2, cloudwatch.AlarmState.OK), alarm3),
                    cloudwatch.AlarmRule.not(cloudwatch.AlarmRule.from_alarm(alarm4, cloudwatch.AlarmState.INSUFFICIENT_DATA))),
                cloudwatch.AlarmRule.from_boolean(False))
            
            cloudwatch.CompositeAlarm(self, "MyAwesomeCompositeAlarm",
                alarm_rule=alarm_rule
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac3983e61925a8b50987e3b6213e939907d0c4bb41a5682e1321634d8b68675b)
            check_type(argname="argument alarm_rule", value=alarm_rule, expected_type=type_hints["alarm_rule"])
            check_type(argname="argument actions_enabled", value=actions_enabled, expected_type=type_hints["actions_enabled"])
            check_type(argname="argument actions_suppressor", value=actions_suppressor, expected_type=type_hints["actions_suppressor"])
            check_type(argname="argument actions_suppressor_extension_period", value=actions_suppressor_extension_period, expected_type=type_hints["actions_suppressor_extension_period"])
            check_type(argname="argument actions_suppressor_wait_period", value=actions_suppressor_wait_period, expected_type=type_hints["actions_suppressor_wait_period"])
            check_type(argname="argument alarm_description", value=alarm_description, expected_type=type_hints["alarm_description"])
            check_type(argname="argument composite_alarm_name", value=composite_alarm_name, expected_type=type_hints["composite_alarm_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "alarm_rule": alarm_rule,
        }
        if actions_enabled is not None:
            self._values["actions_enabled"] = actions_enabled
        if actions_suppressor is not None:
            self._values["actions_suppressor"] = actions_suppressor
        if actions_suppressor_extension_period is not None:
            self._values["actions_suppressor_extension_period"] = actions_suppressor_extension_period
        if actions_suppressor_wait_period is not None:
            self._values["actions_suppressor_wait_period"] = actions_suppressor_wait_period
        if alarm_description is not None:
            self._values["alarm_description"] = alarm_description
        if composite_alarm_name is not None:
            self._values["composite_alarm_name"] = composite_alarm_name

    @builtins.property
    def alarm_rule(self) -> "IAlarmRule":
        '''Expression that specifies which other alarms are to be evaluated to determine this composite alarm's state.'''
        result = self._values.get("alarm_rule")
        assert result is not None, "Required property 'alarm_rule' is missing"
        return typing.cast("IAlarmRule", result)

    @builtins.property
    def actions_enabled(self) -> typing.Optional[builtins.bool]:
        '''Whether the actions for this alarm are enabled.

        :default: true
        '''
        result = self._values.get("actions_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def actions_suppressor(self) -> typing.Optional["IAlarm"]:
        '''Actions will be suppressed if the suppressor alarm is in the ALARM state.

        :default: - alarm will not be suppressed.
        '''
        result = self._values.get("actions_suppressor")
        return typing.cast(typing.Optional["IAlarm"], result)

    @builtins.property
    def actions_suppressor_extension_period(
        self,
    ) -> typing.Optional[_Duration_4839e8c3]:
        '''The maximum duration that the composite alarm waits after suppressor alarm goes out of the ALARM state.

        After this time, the composite alarm performs its actions.

        :default: - 1 minute extension period will be set.
        '''
        result = self._values.get("actions_suppressor_extension_period")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def actions_suppressor_wait_period(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The maximum duration that the composite alarm waits for the suppressor alarm to go into the ALARM state.

        After this time, the composite alarm performs its actions.

        :default: - 1 minute wait period will be set.
        '''
        result = self._values.get("actions_suppressor_wait_period")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def alarm_description(self) -> typing.Optional[builtins.str]:
        '''Description for the alarm.

        :default: - No description.
        '''
        result = self._values.get("alarm_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def composite_alarm_name(self) -> typing.Optional[builtins.str]:
        '''Name of the alarm.

        :default: - Automatically generated name.
        '''
        result = self._values.get("composite_alarm_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CompositeAlarmProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudwatch.CreateAlarmOptions",
    jsii_struct_bases=[],
    name_mapping={
        "evaluation_periods": "evaluationPeriods",
        "threshold": "threshold",
        "actions_enabled": "actionsEnabled",
        "alarm_description": "alarmDescription",
        "alarm_name": "alarmName",
        "comparison_operator": "comparisonOperator",
        "datapoints_to_alarm": "datapointsToAlarm",
        "evaluate_low_sample_count_percentile": "evaluateLowSampleCountPercentile",
        "treat_missing_data": "treatMissingData",
    },
)
class CreateAlarmOptions:
    def __init__(
        self,
        *,
        evaluation_periods: jsii.Number,
        threshold: jsii.Number,
        actions_enabled: typing.Optional[builtins.bool] = None,
        alarm_description: typing.Optional[builtins.str] = None,
        alarm_name: typing.Optional[builtins.str] = None,
        comparison_operator: typing.Optional[ComparisonOperator] = None,
        datapoints_to_alarm: typing.Optional[jsii.Number] = None,
        evaluate_low_sample_count_percentile: typing.Optional[builtins.str] = None,
        treat_missing_data: typing.Optional["TreatMissingData"] = None,
    ) -> None:
        '''Properties needed to make an alarm from a metric.

        :param evaluation_periods: The number of periods over which data is compared to the specified threshold.
        :param threshold: The value against which the specified statistic is compared.
        :param actions_enabled: Whether the actions for this alarm are enabled. Default: true
        :param alarm_description: Description for the alarm. Default: No description
        :param alarm_name: Name of the alarm. Default: Automatically generated name
        :param comparison_operator: Comparison to use to check if metric is breaching. Default: GreaterThanOrEqualToThreshold
        :param datapoints_to_alarm: The number of datapoints that must be breaching to trigger the alarm. This is used only if you are setting an "M out of N" alarm. In that case, this value is the M. For more information, see Evaluating an Alarm in the Amazon CloudWatch User Guide. Default: ``evaluationPeriods``
        :param evaluate_low_sample_count_percentile: Specifies whether to evaluate the data and potentially change the alarm state if there are too few data points to be statistically significant. Used only for alarms that are based on percentiles. Default: - Not configured.
        :param treat_missing_data: Sets how this alarm is to handle missing data points. Default: TreatMissingData.Missing

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_cloudwatch as cloudwatch
            
            # my_hosted_zone: route53.HostedZone
            
            certificate = acm.Certificate(self, "Certificate",
                domain_name="hello.example.com",
                validation=acm.CertificateValidation.from_dns(my_hosted_zone)
            )
            certificate.metric_days_to_expiry().create_alarm(self, "Alarm",
                comparison_operator=cloudwatch.ComparisonOperator.LESS_THAN_THRESHOLD,
                evaluation_periods=1,
                threshold=45
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91617a8a8e9f459ae82e35cee9e72d7bc0040c89e7759483900a64aadd24ca0b)
            check_type(argname="argument evaluation_periods", value=evaluation_periods, expected_type=type_hints["evaluation_periods"])
            check_type(argname="argument threshold", value=threshold, expected_type=type_hints["threshold"])
            check_type(argname="argument actions_enabled", value=actions_enabled, expected_type=type_hints["actions_enabled"])
            check_type(argname="argument alarm_description", value=alarm_description, expected_type=type_hints["alarm_description"])
            check_type(argname="argument alarm_name", value=alarm_name, expected_type=type_hints["alarm_name"])
            check_type(argname="argument comparison_operator", value=comparison_operator, expected_type=type_hints["comparison_operator"])
            check_type(argname="argument datapoints_to_alarm", value=datapoints_to_alarm, expected_type=type_hints["datapoints_to_alarm"])
            check_type(argname="argument evaluate_low_sample_count_percentile", value=evaluate_low_sample_count_percentile, expected_type=type_hints["evaluate_low_sample_count_percentile"])
            check_type(argname="argument treat_missing_data", value=treat_missing_data, expected_type=type_hints["treat_missing_data"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "evaluation_periods": evaluation_periods,
            "threshold": threshold,
        }
        if actions_enabled is not None:
            self._values["actions_enabled"] = actions_enabled
        if alarm_description is not None:
            self._values["alarm_description"] = alarm_description
        if alarm_name is not None:
            self._values["alarm_name"] = alarm_name
        if comparison_operator is not None:
            self._values["comparison_operator"] = comparison_operator
        if datapoints_to_alarm is not None:
            self._values["datapoints_to_alarm"] = datapoints_to_alarm
        if evaluate_low_sample_count_percentile is not None:
            self._values["evaluate_low_sample_count_percentile"] = evaluate_low_sample_count_percentile
        if treat_missing_data is not None:
            self._values["treat_missing_data"] = treat_missing_data

    @builtins.property
    def evaluation_periods(self) -> jsii.Number:
        '''The number of periods over which data is compared to the specified threshold.'''
        result = self._values.get("evaluation_periods")
        assert result is not None, "Required property 'evaluation_periods' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def threshold(self) -> jsii.Number:
        '''The value against which the specified statistic is compared.'''
        result = self._values.get("threshold")
        assert result is not None, "Required property 'threshold' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def actions_enabled(self) -> typing.Optional[builtins.bool]:
        '''Whether the actions for this alarm are enabled.

        :default: true
        '''
        result = self._values.get("actions_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def alarm_description(self) -> typing.Optional[builtins.str]:
        '''Description for the alarm.

        :default: No description
        '''
        result = self._values.get("alarm_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def alarm_name(self) -> typing.Optional[builtins.str]:
        '''Name of the alarm.

        :default: Automatically generated name
        '''
        result = self._values.get("alarm_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def comparison_operator(self) -> typing.Optional[ComparisonOperator]:
        '''Comparison to use to check if metric is breaching.

        :default: GreaterThanOrEqualToThreshold
        '''
        result = self._values.get("comparison_operator")
        return typing.cast(typing.Optional[ComparisonOperator], result)

    @builtins.property
    def datapoints_to_alarm(self) -> typing.Optional[jsii.Number]:
        '''The number of datapoints that must be breaching to trigger the alarm.

        This is used only if you are setting an "M
        out of N" alarm. In that case, this value is the M. For more information, see Evaluating an Alarm in the Amazon
        CloudWatch User Guide.

        :default: ``evaluationPeriods``

        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#alarm-evaluation
        '''
        result = self._values.get("datapoints_to_alarm")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def evaluate_low_sample_count_percentile(self) -> typing.Optional[builtins.str]:
        '''Specifies whether to evaluate the data and potentially change the alarm state if there are too few data points to be statistically significant.

        Used only for alarms that are based on percentiles.

        :default: - Not configured.
        '''
        result = self._values.get("evaluate_low_sample_count_percentile")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def treat_missing_data(self) -> typing.Optional["TreatMissingData"]:
        '''Sets how this alarm is to handle missing data points.

        :default: TreatMissingData.Missing
        '''
        result = self._values.get("treat_missing_data")
        return typing.cast(typing.Optional["TreatMissingData"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CreateAlarmOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudwatch.CustomWidgetProps",
    jsii_struct_bases=[],
    name_mapping={
        "function_arn": "functionArn",
        "title": "title",
        "height": "height",
        "params": "params",
        "update_on_refresh": "updateOnRefresh",
        "update_on_resize": "updateOnResize",
        "update_on_time_range_change": "updateOnTimeRangeChange",
        "width": "width",
    },
)
class CustomWidgetProps:
    def __init__(
        self,
        *,
        function_arn: builtins.str,
        title: builtins.str,
        height: typing.Optional[jsii.Number] = None,
        params: typing.Any = None,
        update_on_refresh: typing.Optional[builtins.bool] = None,
        update_on_resize: typing.Optional[builtins.bool] = None,
        update_on_time_range_change: typing.Optional[builtins.bool] = None,
        width: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''The properties for a CustomWidget.

        :param function_arn: The Arn of the AWS Lambda function that returns HTML or JSON that will be displayed in the widget.
        :param title: The title of the widget.
        :param height: Height of the widget. Default: - 6 for Alarm and Graph widgets. 3 for single value widgets where most recent value of a metric is displayed.
        :param params: Parameters passed to the lambda function. Default: - no parameters are passed to the lambda function
        :param update_on_refresh: Update the widget on refresh. Default: true
        :param update_on_resize: Update the widget on resize. Default: true
        :param update_on_time_range_change: Update the widget on time range change. Default: true
        :param width: Width of the widget, in a grid of 24 units wide. Default: 6

        :exampleMetadata: infused

        Example::

            # dashboard: cloudwatch.Dashboard
            
            
            # Import or create a lambda function
            fn = lambda_.Function.from_function_arn(dashboard, "Function", "arn:aws:lambda:us-east-1:123456789012:function:MyFn")
            
            dashboard.add_widgets(cloudwatch.CustomWidget(
                function_arn=fn.function_arn,
                title="My lambda baked widget"
            ))
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d71374eb7e9e4cb8250337037e840a61230633064256eddde7401c0a174961c)
            check_type(argname="argument function_arn", value=function_arn, expected_type=type_hints["function_arn"])
            check_type(argname="argument title", value=title, expected_type=type_hints["title"])
            check_type(argname="argument height", value=height, expected_type=type_hints["height"])
            check_type(argname="argument params", value=params, expected_type=type_hints["params"])
            check_type(argname="argument update_on_refresh", value=update_on_refresh, expected_type=type_hints["update_on_refresh"])
            check_type(argname="argument update_on_resize", value=update_on_resize, expected_type=type_hints["update_on_resize"])
            check_type(argname="argument update_on_time_range_change", value=update_on_time_range_change, expected_type=type_hints["update_on_time_range_change"])
            check_type(argname="argument width", value=width, expected_type=type_hints["width"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "function_arn": function_arn,
            "title": title,
        }
        if height is not None:
            self._values["height"] = height
        if params is not None:
            self._values["params"] = params
        if update_on_refresh is not None:
            self._values["update_on_refresh"] = update_on_refresh
        if update_on_resize is not None:
            self._values["update_on_resize"] = update_on_resize
        if update_on_time_range_change is not None:
            self._values["update_on_time_range_change"] = update_on_time_range_change
        if width is not None:
            self._values["width"] = width

    @builtins.property
    def function_arn(self) -> builtins.str:
        '''The Arn of the AWS Lambda function that returns HTML or JSON that will be displayed in the widget.'''
        result = self._values.get("function_arn")
        assert result is not None, "Required property 'function_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def title(self) -> builtins.str:
        '''The title of the widget.'''
        result = self._values.get("title")
        assert result is not None, "Required property 'title' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def height(self) -> typing.Optional[jsii.Number]:
        '''Height of the widget.

        :default:

        - 6 for Alarm and Graph widgets.
        3 for single value widgets where most recent value of a metric is displayed.
        '''
        result = self._values.get("height")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def params(self) -> typing.Any:
        '''Parameters passed to the lambda function.

        :default: - no parameters are passed to the lambda function
        '''
        result = self._values.get("params")
        return typing.cast(typing.Any, result)

    @builtins.property
    def update_on_refresh(self) -> typing.Optional[builtins.bool]:
        '''Update the widget on refresh.

        :default: true
        '''
        result = self._values.get("update_on_refresh")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def update_on_resize(self) -> typing.Optional[builtins.bool]:
        '''Update the widget on resize.

        :default: true
        '''
        result = self._values.get("update_on_resize")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def update_on_time_range_change(self) -> typing.Optional[builtins.bool]:
        '''Update the widget on time range change.

        :default: true
        '''
        result = self._values.get("update_on_time_range_change")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def width(self) -> typing.Optional[jsii.Number]:
        '''Width of the widget, in a grid of 24 units wide.

        :default: 6
        '''
        result = self._values.get("width")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CustomWidgetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Dashboard(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudwatch.Dashboard",
):
    '''A CloudWatch dashboard.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_cloudwatch as cw
        
        
        dashboard = cw.Dashboard(self, "Dash",
            default_interval=Duration.days(7),
            variables=[cw.DashboardVariable(
                id="region2",
                type=cw.VariableType.PATTERN,
                label="RegionPattern",
                input_type=cw.VariableInputType.INPUT,
                value="us-east-1",
                default_value=cw.DefaultValue.value("us-east-1"),
                visible=True
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        dashboard_name: typing.Optional[builtins.str] = None,
        default_interval: typing.Optional[_Duration_4839e8c3] = None,
        end: typing.Optional[builtins.str] = None,
        period_override: typing.Optional["PeriodOverride"] = None,
        start: typing.Optional[builtins.str] = None,
        variables: typing.Optional[typing.Sequence["IVariable"]] = None,
        widgets: typing.Optional[typing.Sequence[typing.Sequence["IWidget"]]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param dashboard_name: Name of the dashboard. If set, must only contain alphanumerics, dash (-) and underscore (_) Default: - automatically generated name
        :param default_interval: Interval duration for metrics. You can specify defaultInterval with the relative time(eg. cdk.Duration.days(7)). Both properties ``defaultInterval`` and ``start`` cannot be set at once. Default: When the dashboard loads, the defaultInterval time will be the default time range.
        :param end: The end of the time range to use for each widget on the dashboard when the dashboard loads. If you specify a value for end, you must also specify a value for start. Specify an absolute time in the ISO 8601 format. For example, 2018-12-17T06:00:00.000Z. Default: When the dashboard loads, the end date will be the current time.
        :param period_override: Use this field to specify the period for the graphs when the dashboard loads. Specifying ``Auto`` causes the period of all graphs on the dashboard to automatically adapt to the time range of the dashboard. Specifying ``Inherit`` ensures that the period set for each graph is always obeyed. Default: Auto
        :param start: The start of the time range to use for each widget on the dashboard. You can specify start without specifying end to specify a relative time range that ends with the current time. In this case, the value of start must begin with -P, and you can use M, H, D, W and M as abbreviations for minutes, hours, days, weeks and months. For example, -PT8H shows the last 8 hours and -P3M shows the last three months. You can also use start along with an end field, to specify an absolute time range. When specifying an absolute time range, use the ISO 8601 format. For example, 2018-12-17T06:00:00.000Z. Both properties ``defaultInterval`` and ``start`` cannot be set at once. Default: When the dashboard loads, the start time will be the default time range.
        :param variables: A list of dashboard variables. Default: - No variables
        :param widgets: Initial set of widgets on the dashboard. One array represents a row of widgets. Default: - No widgets
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6fda01df790539d40ed9b476d4407925232861deff439705940e219dc8e29020)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = DashboardProps(
            dashboard_name=dashboard_name,
            default_interval=default_interval,
            end=end,
            period_override=period_override,
            start=start,
            variables=variables,
            widgets=widgets,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="addVariable")
    def add_variable(self, variable: "IVariable") -> None:
        '''Add a variable to the dashboard.

        :param variable: -

        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_dashboard_variables.html
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1da9fa9df70a5b921eac287c4fe08d6816d2514a66f72147b77e9feea1a8a606)
            check_type(argname="argument variable", value=variable, expected_type=type_hints["variable"])
        return typing.cast(None, jsii.invoke(self, "addVariable", [variable]))

    @jsii.member(jsii_name="addWidgets")
    def add_widgets(self, *widgets: "IWidget") -> None:
        '''Add a widget to the dashboard.

        Widgets given in multiple calls to add() will be laid out stacked on
        top of each other.

        Multiple widgets added in the same call to add() will be laid out next
        to each other.

        :param widgets: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e914386fa8a66a4e8e6cbeaa4a3f975f705962fc3be601de7228f8576e15c42d)
            check_type(argname="argument widgets", value=widgets, expected_type=typing.Tuple[type_hints["widgets"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "addWidgets", [*widgets]))

    @builtins.property
    @jsii.member(jsii_name="dashboardArn")
    def dashboard_arn(self) -> builtins.str:
        '''ARN of this dashboard.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "dashboardArn"))

    @builtins.property
    @jsii.member(jsii_name="dashboardName")
    def dashboard_name(self) -> builtins.str:
        '''The name of this dashboard.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "dashboardName"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudwatch.DashboardProps",
    jsii_struct_bases=[],
    name_mapping={
        "dashboard_name": "dashboardName",
        "default_interval": "defaultInterval",
        "end": "end",
        "period_override": "periodOverride",
        "start": "start",
        "variables": "variables",
        "widgets": "widgets",
    },
)
class DashboardProps:
    def __init__(
        self,
        *,
        dashboard_name: typing.Optional[builtins.str] = None,
        default_interval: typing.Optional[_Duration_4839e8c3] = None,
        end: typing.Optional[builtins.str] = None,
        period_override: typing.Optional["PeriodOverride"] = None,
        start: typing.Optional[builtins.str] = None,
        variables: typing.Optional[typing.Sequence["IVariable"]] = None,
        widgets: typing.Optional[typing.Sequence[typing.Sequence["IWidget"]]] = None,
    ) -> None:
        '''Properties for defining a CloudWatch Dashboard.

        :param dashboard_name: Name of the dashboard. If set, must only contain alphanumerics, dash (-) and underscore (_) Default: - automatically generated name
        :param default_interval: Interval duration for metrics. You can specify defaultInterval with the relative time(eg. cdk.Duration.days(7)). Both properties ``defaultInterval`` and ``start`` cannot be set at once. Default: When the dashboard loads, the defaultInterval time will be the default time range.
        :param end: The end of the time range to use for each widget on the dashboard when the dashboard loads. If you specify a value for end, you must also specify a value for start. Specify an absolute time in the ISO 8601 format. For example, 2018-12-17T06:00:00.000Z. Default: When the dashboard loads, the end date will be the current time.
        :param period_override: Use this field to specify the period for the graphs when the dashboard loads. Specifying ``Auto`` causes the period of all graphs on the dashboard to automatically adapt to the time range of the dashboard. Specifying ``Inherit`` ensures that the period set for each graph is always obeyed. Default: Auto
        :param start: The start of the time range to use for each widget on the dashboard. You can specify start without specifying end to specify a relative time range that ends with the current time. In this case, the value of start must begin with -P, and you can use M, H, D, W and M as abbreviations for minutes, hours, days, weeks and months. For example, -PT8H shows the last 8 hours and -P3M shows the last three months. You can also use start along with an end field, to specify an absolute time range. When specifying an absolute time range, use the ISO 8601 format. For example, 2018-12-17T06:00:00.000Z. Both properties ``defaultInterval`` and ``start`` cannot be set at once. Default: When the dashboard loads, the start time will be the default time range.
        :param variables: A list of dashboard variables. Default: - No variables
        :param widgets: Initial set of widgets on the dashboard. One array represents a row of widgets. Default: - No widgets

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_cloudwatch as cw
            
            
            dashboard = cw.Dashboard(self, "Dash",
                default_interval=Duration.days(7),
                variables=[cw.DashboardVariable(
                    id="region2",
                    type=cw.VariableType.PATTERN,
                    label="RegionPattern",
                    input_type=cw.VariableInputType.INPUT,
                    value="us-east-1",
                    default_value=cw.DefaultValue.value("us-east-1"),
                    visible=True
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c41d6a8494d12ab7a95fc9ee6638b207cc78fd0aa3e36ceec570a394588d6890)
            check_type(argname="argument dashboard_name", value=dashboard_name, expected_type=type_hints["dashboard_name"])
            check_type(argname="argument default_interval", value=default_interval, expected_type=type_hints["default_interval"])
            check_type(argname="argument end", value=end, expected_type=type_hints["end"])
            check_type(argname="argument period_override", value=period_override, expected_type=type_hints["period_override"])
            check_type(argname="argument start", value=start, expected_type=type_hints["start"])
            check_type(argname="argument variables", value=variables, expected_type=type_hints["variables"])
            check_type(argname="argument widgets", value=widgets, expected_type=type_hints["widgets"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if dashboard_name is not None:
            self._values["dashboard_name"] = dashboard_name
        if default_interval is not None:
            self._values["default_interval"] = default_interval
        if end is not None:
            self._values["end"] = end
        if period_override is not None:
            self._values["period_override"] = period_override
        if start is not None:
            self._values["start"] = start
        if variables is not None:
            self._values["variables"] = variables
        if widgets is not None:
            self._values["widgets"] = widgets

    @builtins.property
    def dashboard_name(self) -> typing.Optional[builtins.str]:
        '''Name of the dashboard.

        If set, must only contain alphanumerics, dash (-) and underscore (_)

        :default: - automatically generated name
        '''
        result = self._values.get("dashboard_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_interval(self) -> typing.Optional[_Duration_4839e8c3]:
        '''Interval duration for metrics. You can specify defaultInterval with the relative time(eg. cdk.Duration.days(7)).

        Both properties ``defaultInterval`` and ``start`` cannot be set at once.

        :default: When the dashboard loads, the defaultInterval time will be the default time range.
        '''
        result = self._values.get("default_interval")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def end(self) -> typing.Optional[builtins.str]:
        '''The end of the time range to use for each widget on the dashboard when the dashboard loads.

        If you specify a value for end, you must also specify a value for start.
        Specify an absolute time in the ISO 8601 format. For example, 2018-12-17T06:00:00.000Z.

        :default: When the dashboard loads, the end date will be the current time.
        '''
        result = self._values.get("end")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def period_override(self) -> typing.Optional["PeriodOverride"]:
        '''Use this field to specify the period for the graphs when the dashboard loads.

        Specifying ``Auto`` causes the period of all graphs on the dashboard to automatically adapt to the time range of the dashboard.
        Specifying ``Inherit`` ensures that the period set for each graph is always obeyed.

        :default: Auto
        '''
        result = self._values.get("period_override")
        return typing.cast(typing.Optional["PeriodOverride"], result)

    @builtins.property
    def start(self) -> typing.Optional[builtins.str]:
        '''The start of the time range to use for each widget on the dashboard.

        You can specify start without specifying end to specify a relative time range that ends with the current time.
        In this case, the value of start must begin with -P, and you can use M, H, D, W and M as abbreviations for
        minutes, hours, days, weeks and months. For example, -PT8H shows the last 8 hours and -P3M shows the last three months.
        You can also use start along with an end field, to specify an absolute time range.
        When specifying an absolute time range, use the ISO 8601 format. For example, 2018-12-17T06:00:00.000Z.

        Both properties ``defaultInterval`` and ``start`` cannot be set at once.

        :default: When the dashboard loads, the start time will be the default time range.
        '''
        result = self._values.get("start")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def variables(self) -> typing.Optional[typing.List["IVariable"]]:
        '''A list of dashboard variables.

        :default: - No variables

        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_dashboard_variables.html#cloudwatch_dashboard_variables_types
        '''
        result = self._values.get("variables")
        return typing.cast(typing.Optional[typing.List["IVariable"]], result)

    @builtins.property
    def widgets(self) -> typing.Optional[typing.List[typing.List["IWidget"]]]:
        '''Initial set of widgets on the dashboard.

        One array represents a row of widgets.

        :default: - No widgets
        '''
        result = self._values.get("widgets")
        return typing.cast(typing.Optional[typing.List[typing.List["IWidget"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DashboardProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudwatch.DashboardVariableOptions",
    jsii_struct_bases=[],
    name_mapping={
        "id": "id",
        "input_type": "inputType",
        "type": "type",
        "value": "value",
        "default_value": "defaultValue",
        "label": "label",
        "values": "values",
        "visible": "visible",
    },
)
class DashboardVariableOptions:
    def __init__(
        self,
        *,
        id: builtins.str,
        input_type: "VariableInputType",
        type: "VariableType",
        value: builtins.str,
        default_value: typing.Optional["DefaultValue"] = None,
        label: typing.Optional[builtins.str] = None,
        values: typing.Optional["Values"] = None,
        visible: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Options for {@link DashboardVariable}.

        :param id: Unique id.
        :param input_type: The way the variable value is selected.
        :param type: Type of the variable.
        :param value: Pattern or property value to replace.
        :param default_value: Optional default value. Default: - no default value is set
        :param label: Optional label in the toolbar. Default: - the variable's value
        :param values: Optional values (required for {@link VariableInputType.RADIO} and {@link VariableInputType.SELECT} dashboard variables). Default: - no values
        :param visible: Whether the variable is visible. Default: - true

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_cloudwatch as cw
            
            
            dashboard = cw.Dashboard(self, "Dash",
                default_interval=Duration.days(7),
                variables=[cw.DashboardVariable(
                    id="functionName",
                    type=cw.VariableType.PATTERN,
                    label="Function",
                    input_type=cw.VariableInputType.RADIO,
                    value="originalFuncNameInDashboard",
                    # equivalent to cw.Values.fromSearch('{AWS/Lambda,FunctionName} MetricName=\"Duration\"', 'FunctionName')
                    values=cw.Values.from_search_components(
                        namespace="AWS/Lambda",
                        dimensions=["FunctionName"],
                        metric_name="Duration",
                        populate_from="FunctionName"
                    ),
                    default_value=cw.DefaultValue.FIRST,
                    visible=True
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4da4c2a317eff8c9083c9e23732734166969be3616c35a7f51e21115e260cba6)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument input_type", value=input_type, expected_type=type_hints["input_type"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            check_type(argname="argument default_value", value=default_value, expected_type=type_hints["default_value"])
            check_type(argname="argument label", value=label, expected_type=type_hints["label"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
            check_type(argname="argument visible", value=visible, expected_type=type_hints["visible"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "id": id,
            "input_type": input_type,
            "type": type,
            "value": value,
        }
        if default_value is not None:
            self._values["default_value"] = default_value
        if label is not None:
            self._values["label"] = label
        if values is not None:
            self._values["values"] = values
        if visible is not None:
            self._values["visible"] = visible

    @builtins.property
    def id(self) -> builtins.str:
        '''Unique id.'''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def input_type(self) -> "VariableInputType":
        '''The way the variable value is selected.'''
        result = self._values.get("input_type")
        assert result is not None, "Required property 'input_type' is missing"
        return typing.cast("VariableInputType", result)

    @builtins.property
    def type(self) -> "VariableType":
        '''Type of the variable.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast("VariableType", result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Pattern or property value to replace.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def default_value(self) -> typing.Optional["DefaultValue"]:
        '''Optional default value.

        :default: - no default value is set
        '''
        result = self._values.get("default_value")
        return typing.cast(typing.Optional["DefaultValue"], result)

    @builtins.property
    def label(self) -> typing.Optional[builtins.str]:
        '''Optional label in the toolbar.

        :default: - the variable's value
        '''
        result = self._values.get("label")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def values(self) -> typing.Optional["Values"]:
        '''Optional values (required for {@link VariableInputType.RADIO} and {@link VariableInputType.SELECT} dashboard variables).

        :default: - no values
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional["Values"], result)

    @builtins.property
    def visible(self) -> typing.Optional[builtins.bool]:
        '''Whether the variable is visible.

        :default: - true
        '''
        result = self._values.get("visible")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DashboardVariableOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DefaultValue(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudwatch.DefaultValue",
):
    '''Default value for use in {@link DashboardVariableOptions}.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_cloudwatch as cw
        
        
        dashboard = cw.Dashboard(self, "Dash",
            default_interval=Duration.days(7),
            variables=[cw.DashboardVariable(
                id="functionName",
                type=cw.VariableType.PATTERN,
                label="Function",
                input_type=cw.VariableInputType.RADIO,
                value="originalFuncNameInDashboard",
                # equivalent to cw.Values.fromSearch('{AWS/Lambda,FunctionName} MetricName=\"Duration\"', 'FunctionName')
                values=cw.Values.from_search_components(
                    namespace="AWS/Lambda",
                    dimensions=["FunctionName"],
                    metric_name="Duration",
                    populate_from="FunctionName"
                ),
                default_value=cw.DefaultValue.FIRST,
                visible=True
            )]
        )
    '''

    @jsii.member(jsii_name="value")
    @builtins.classmethod
    def value(cls, value: typing.Any) -> "DefaultValue":
        '''Create a default value.

        :param value: the value to be used as default.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4f7631acc3b9fb4aea3e273751a2a20c7480f62e33d5789fd4938c009af2ec8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast("DefaultValue", jsii.sinvoke(cls, "value", [value]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="FIRST")
    def FIRST(cls) -> "DefaultValue":
        '''A special value for use with search expressions to have the default value be the first value returned from search.'''
        return typing.cast("DefaultValue", jsii.sget(cls, "FIRST"))

    @builtins.property
    @jsii.member(jsii_name="val")
    def val(self) -> typing.Any:
        return typing.cast(typing.Any, jsii.get(self, "val"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudwatch.Dimension",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "value": "value"},
)
class Dimension:
    def __init__(self, *, name: builtins.str, value: typing.Any) -> None:
        '''Metric dimension.

        :param name: Name of the dimension.
        :param value: Value of the dimension.

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-dimension.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cloudwatch as cloudwatch
            
            # value: Any
            
            dimension = cloudwatch.Dimension(
                name="name",
                value=value
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9f1a4bef1bc9e7080c21c9fd7656533f0a327837e2ebfcb35a0338efb47ad17)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "value": value,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the dimension.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> typing.Any:
        '''Value of the dimension.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Dimension(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_cloudwatch.GraphWidgetView")
class GraphWidgetView(enum.Enum):
    '''Types of view.

    :exampleMetadata: infused

    Example::

        # dashboard: cloudwatch.Dashboard
        
        
        dashboard.add_widgets(cloudwatch.GraphWidget(
            # ...
        
            view=cloudwatch.GraphWidgetView.BAR
        ))
    '''

    TIME_SERIES = "TIME_SERIES"
    '''Display as a line graph.'''
    BAR = "BAR"
    '''Display as a bar graph.'''
    PIE = "PIE"
    '''Display as a pie graph.'''


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudwatch.HorizontalAnnotation",
    jsii_struct_bases=[],
    name_mapping={
        "value": "value",
        "color": "color",
        "fill": "fill",
        "label": "label",
        "visible": "visible",
    },
)
class HorizontalAnnotation:
    def __init__(
        self,
        *,
        value: jsii.Number,
        color: typing.Optional[builtins.str] = None,
        fill: typing.Optional["Shading"] = None,
        label: typing.Optional[builtins.str] = None,
        visible: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Horizontal annotation to be added to a graph.

        :param value: The value of the annotation.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to be used for the annotation. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param fill: Add shading above or below the annotation. Default: No shading
        :param label: Label for the annotation. Default: - No label
        :param visible: Whether the annotation is visible. Default: true

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cloudwatch as cloudwatch
            
            horizontal_annotation = cloudwatch.HorizontalAnnotation(
                value=123,
            
                # the properties below are optional
                color="color",
                fill=cloudwatch.Shading.NONE,
                label="label",
                visible=False
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__590b09336dca786909b6d40a91a4108f1ce6787811718cd6151f7cd2d8e37be9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            check_type(argname="argument color", value=color, expected_type=type_hints["color"])
            check_type(argname="argument fill", value=fill, expected_type=type_hints["fill"])
            check_type(argname="argument label", value=label, expected_type=type_hints["label"])
            check_type(argname="argument visible", value=visible, expected_type=type_hints["visible"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "value": value,
        }
        if color is not None:
            self._values["color"] = color
        if fill is not None:
            self._values["fill"] = fill
        if label is not None:
            self._values["label"] = label
        if visible is not None:
            self._values["visible"] = visible

    @builtins.property
    def value(self) -> jsii.Number:
        '''The value of the annotation.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def color(self) -> typing.Optional[builtins.str]:
        '''The hex color code, prefixed with '#' (e.g. '#00ff00'), to be used for the annotation. The ``Color`` class has a set of standard colors that can be used here.

        :default: - Automatic color
        '''
        result = self._values.get("color")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def fill(self) -> typing.Optional["Shading"]:
        '''Add shading above or below the annotation.

        :default: No shading
        '''
        result = self._values.get("fill")
        return typing.cast(typing.Optional["Shading"], result)

    @builtins.property
    def label(self) -> typing.Optional[builtins.str]:
        '''Label for the annotation.

        :default: - No label
        '''
        result = self._values.get("label")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def visible(self) -> typing.Optional[builtins.bool]:
        '''Whether the annotation is visible.

        :default: true
        '''
        result = self._values.get("visible")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HorizontalAnnotation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.aws_cloudwatch.IAlarmAction")
class IAlarmAction(typing_extensions.Protocol):
    '''Interface for objects that can be the targets of CloudWatch alarm actions.'''

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        scope: _constructs_77d1e7e8.Construct,
        alarm: "IAlarm",
    ) -> AlarmActionConfig:
        '''Return the properties required to send alarm actions to this CloudWatch alarm.

        :param scope: root Construct that allows creating new Constructs.
        :param alarm: CloudWatch alarm that the action will target.
        '''
        ...


class _IAlarmActionProxy:
    '''Interface for objects that can be the targets of CloudWatch alarm actions.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_cloudwatch.IAlarmAction"

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        scope: _constructs_77d1e7e8.Construct,
        alarm: "IAlarm",
    ) -> AlarmActionConfig:
        '''Return the properties required to send alarm actions to this CloudWatch alarm.

        :param scope: root Construct that allows creating new Constructs.
        :param alarm: CloudWatch alarm that the action will target.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19a88cc904e70d7841abfa1406b71edcf34c316b173c37c2881e75702bc0c75a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument alarm", value=alarm, expected_type=type_hints["alarm"])
        return typing.cast(AlarmActionConfig, jsii.invoke(self, "bind", [scope, alarm]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAlarmAction).__jsii_proxy_class__ = lambda : _IAlarmActionProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_cloudwatch.IAlarmRule")
class IAlarmRule(typing_extensions.Protocol):
    '''Interface for Alarm Rule.'''

    @jsii.member(jsii_name="renderAlarmRule")
    def render_alarm_rule(self) -> builtins.str:
        '''serialized representation of Alarm Rule to be used when building the Composite Alarm resource.'''
        ...


class _IAlarmRuleProxy:
    '''Interface for Alarm Rule.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_cloudwatch.IAlarmRule"

    @jsii.member(jsii_name="renderAlarmRule")
    def render_alarm_rule(self) -> builtins.str:
        '''serialized representation of Alarm Rule to be used when building the Composite Alarm resource.'''
        return typing.cast(builtins.str, jsii.invoke(self, "renderAlarmRule", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAlarmRule).__jsii_proxy_class__ = lambda : _IAlarmRuleProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_cloudwatch.IMetric")
class IMetric(typing_extensions.Protocol):
    '''Interface for metrics.'''

    @builtins.property
    @jsii.member(jsii_name="warnings")
    def warnings(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(deprecated) Any warnings related to this metric.

        Should be attached to the consuming construct.

        :default: - None

        :deprecated: - use warningsV2

        :stability: deprecated
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="warningsV2")
    def warnings_v2(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Any warnings related to this metric.

        Should be attached to the consuming construct.

        :default: - None
        '''
        ...

    @jsii.member(jsii_name="toMetricConfig")
    def to_metric_config(self) -> "MetricConfig":
        '''Inspect the details of the metric object.'''
        ...


class _IMetricProxy:
    '''Interface for metrics.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_cloudwatch.IMetric"

    @builtins.property
    @jsii.member(jsii_name="warnings")
    def warnings(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(deprecated) Any warnings related to this metric.

        Should be attached to the consuming construct.

        :default: - None

        :deprecated: - use warningsV2

        :stability: deprecated
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "warnings"))

    @builtins.property
    @jsii.member(jsii_name="warningsV2")
    def warnings_v2(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Any warnings related to this metric.

        Should be attached to the consuming construct.

        :default: - None
        '''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "warningsV2"))

    @jsii.member(jsii_name="toMetricConfig")
    def to_metric_config(self) -> "MetricConfig":
        '''Inspect the details of the metric object.'''
        return typing.cast("MetricConfig", jsii.invoke(self, "toMetricConfig", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IMetric).__jsii_proxy_class__ = lambda : _IMetricProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_cloudwatch.IVariable")
class IVariable(typing_extensions.Protocol):
    '''A single dashboard variable.'''

    @jsii.member(jsii_name="toJson")
    def to_json(self) -> typing.Any:
        '''Return the variable JSON for use in the dashboard.'''
        ...


class _IVariableProxy:
    '''A single dashboard variable.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_cloudwatch.IVariable"

    @jsii.member(jsii_name="toJson")
    def to_json(self) -> typing.Any:
        '''Return the variable JSON for use in the dashboard.'''
        return typing.cast(typing.Any, jsii.invoke(self, "toJson", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IVariable).__jsii_proxy_class__ = lambda : _IVariableProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_cloudwatch.IWidget")
class IWidget(typing_extensions.Protocol):
    '''A single dashboard widget.'''

    @builtins.property
    @jsii.member(jsii_name="height")
    def height(self) -> jsii.Number:
        '''The amount of vertical grid units the widget will take up.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="width")
    def width(self) -> jsii.Number:
        '''The amount of horizontal grid units the widget will take up.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="warnings")
    def warnings(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(deprecated) Any warnings that are produced as a result of putting together this widget.

        :deprecated: - use warningsV2

        :stability: deprecated
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="warningsV2")
    def warnings_v2(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Any warnings that are produced as a result of putting together this widget.'''
        ...

    @jsii.member(jsii_name="position")
    def position(self, x: jsii.Number, y: jsii.Number) -> None:
        '''Place the widget at a given position.

        :param x: -
        :param y: -
        '''
        ...

    @jsii.member(jsii_name="toJson")
    def to_json(self) -> typing.List[typing.Any]:
        '''Return the widget JSON for use in the dashboard.'''
        ...


class _IWidgetProxy:
    '''A single dashboard widget.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_cloudwatch.IWidget"

    @builtins.property
    @jsii.member(jsii_name="height")
    def height(self) -> jsii.Number:
        '''The amount of vertical grid units the widget will take up.'''
        return typing.cast(jsii.Number, jsii.get(self, "height"))

    @builtins.property
    @jsii.member(jsii_name="width")
    def width(self) -> jsii.Number:
        '''The amount of horizontal grid units the widget will take up.'''
        return typing.cast(jsii.Number, jsii.get(self, "width"))

    @builtins.property
    @jsii.member(jsii_name="warnings")
    def warnings(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(deprecated) Any warnings that are produced as a result of putting together this widget.

        :deprecated: - use warningsV2

        :stability: deprecated
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "warnings"))

    @builtins.property
    @jsii.member(jsii_name="warningsV2")
    def warnings_v2(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Any warnings that are produced as a result of putting together this widget.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "warningsV2"))

    @jsii.member(jsii_name="position")
    def position(self, x: jsii.Number, y: jsii.Number) -> None:
        '''Place the widget at a given position.

        :param x: -
        :param y: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f09026a4cce4261b0c1f425d42f625c9bd8f0ba4495e11743f621a2cd44b00f8)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
            check_type(argname="argument y", value=y, expected_type=type_hints["y"])
        return typing.cast(None, jsii.invoke(self, "position", [x, y]))

    @jsii.member(jsii_name="toJson")
    def to_json(self) -> typing.List[typing.Any]:
        '''Return the widget JSON for use in the dashboard.'''
        return typing.cast(typing.List[typing.Any], jsii.invoke(self, "toJson", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IWidget).__jsii_proxy_class__ = lambda : _IWidgetProxy


@jsii.enum(jsii_type="aws-cdk-lib.aws_cloudwatch.LegendPosition")
class LegendPosition(enum.Enum):
    '''The position of the legend on a GraphWidget.

    :exampleMetadata: infused

    Example::

        # dashboard: cloudwatch.Dashboard
        
        
        dashboard.add_widgets(cloudwatch.GraphWidget(
            # ...
        
            legend_position=cloudwatch.LegendPosition.RIGHT
        ))
    '''

    BOTTOM = "BOTTOM"
    '''Legend appears below the graph (default).'''
    RIGHT = "RIGHT"
    '''Add shading above the annotation.'''
    HIDDEN = "HIDDEN"
    '''Add shading below the annotation.'''


@jsii.enum(jsii_type="aws-cdk-lib.aws_cloudwatch.LogQueryVisualizationType")
class LogQueryVisualizationType(enum.Enum):
    '''Types of view.

    :exampleMetadata: infused

    Example::

        # dashboard: cloudwatch.Dashboard
        
        
        dashboard.add_widgets(cloudwatch.LogQueryWidget(
            log_group_names=["my-log-group"],
            view=cloudwatch.LogQueryVisualizationType.TABLE,
            # The lines will be automatically combined using '\n|'.
            query_lines=["fields @message", "filter @message like /Error/"
            ]
        ))
    '''

    TABLE = "TABLE"
    '''Table view.'''
    LINE = "LINE"
    '''Line view.'''
    STACKEDAREA = "STACKEDAREA"
    '''Stacked area view.'''
    BAR = "BAR"
    '''Bar view.'''
    PIE = "PIE"
    '''Pie view.'''


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudwatch.LogQueryWidgetProps",
    jsii_struct_bases=[],
    name_mapping={
        "log_group_names": "logGroupNames",
        "height": "height",
        "query_lines": "queryLines",
        "query_string": "queryString",
        "region": "region",
        "title": "title",
        "view": "view",
        "width": "width",
    },
)
class LogQueryWidgetProps:
    def __init__(
        self,
        *,
        log_group_names: typing.Sequence[builtins.str],
        height: typing.Optional[jsii.Number] = None,
        query_lines: typing.Optional[typing.Sequence[builtins.str]] = None,
        query_string: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        title: typing.Optional[builtins.str] = None,
        view: typing.Optional[LogQueryVisualizationType] = None,
        width: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Properties for a Query widget.

        :param log_group_names: Names of log groups to query.
        :param height: Height of the widget. Default: 6
        :param query_lines: A sequence of lines to use to build the query. The query will be built by joining the lines together using ``\\n|``. Default: - Exactly one of ``queryString``, ``queryLines`` is required.
        :param query_string: Full query string for log insights. Be sure to prepend every new line with a newline and pipe character (``\\n|``). Default: - Exactly one of ``queryString``, ``queryLines`` is required.
        :param region: The region the metrics of this widget should be taken from. Default: Current region
        :param title: Title for the widget. Default: No title
        :param view: The type of view to use. Default: LogQueryVisualizationType.TABLE
        :param width: Width of the widget, in a grid of 24 units wide. Default: 6

        :exampleMetadata: infused

        Example::

            # dashboard: cloudwatch.Dashboard
            
            
            dashboard.add_widgets(cloudwatch.LogQueryWidget(
                log_group_names=["my-log-group"],
                view=cloudwatch.LogQueryVisualizationType.TABLE,
                # The lines will be automatically combined using '\n|'.
                query_lines=["fields @message", "filter @message like /Error/"
                ]
            ))
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7d4a308b1274696259a35b14b5ae833f34881f95eaba521bb47a74b3a80e8c0)
            check_type(argname="argument log_group_names", value=log_group_names, expected_type=type_hints["log_group_names"])
            check_type(argname="argument height", value=height, expected_type=type_hints["height"])
            check_type(argname="argument query_lines", value=query_lines, expected_type=type_hints["query_lines"])
            check_type(argname="argument query_string", value=query_string, expected_type=type_hints["query_string"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument title", value=title, expected_type=type_hints["title"])
            check_type(argname="argument view", value=view, expected_type=type_hints["view"])
            check_type(argname="argument width", value=width, expected_type=type_hints["width"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "log_group_names": log_group_names,
        }
        if height is not None:
            self._values["height"] = height
        if query_lines is not None:
            self._values["query_lines"] = query_lines
        if query_string is not None:
            self._values["query_string"] = query_string
        if region is not None:
            self._values["region"] = region
        if title is not None:
            self._values["title"] = title
        if view is not None:
            self._values["view"] = view
        if width is not None:
            self._values["width"] = width

    @builtins.property
    def log_group_names(self) -> typing.List[builtins.str]:
        '''Names of log groups to query.'''
        result = self._values.get("log_group_names")
        assert result is not None, "Required property 'log_group_names' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def height(self) -> typing.Optional[jsii.Number]:
        '''Height of the widget.

        :default: 6
        '''
        result = self._values.get("height")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def query_lines(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A sequence of lines to use to build the query.

        The query will be built by joining the lines together using ``\\n|``.

        :default: - Exactly one of ``queryString``, ``queryLines`` is required.
        '''
        result = self._values.get("query_lines")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def query_string(self) -> typing.Optional[builtins.str]:
        '''Full query string for log insights.

        Be sure to prepend every new line with a newline and pipe character
        (``\\n|``).

        :default: - Exactly one of ``queryString``, ``queryLines`` is required.
        '''
        result = self._values.get("query_string")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''The region the metrics of this widget should be taken from.

        :default: Current region
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def title(self) -> typing.Optional[builtins.str]:
        '''Title for the widget.

        :default: No title
        '''
        result = self._values.get("title")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def view(self) -> typing.Optional[LogQueryVisualizationType]:
        '''The type of view to use.

        :default: LogQueryVisualizationType.TABLE
        '''
        result = self._values.get("view")
        return typing.cast(typing.Optional[LogQueryVisualizationType], result)

    @builtins.property
    def width(self) -> typing.Optional[jsii.Number]:
        '''Width of the widget, in a grid of 24 units wide.

        :default: 6
        '''
        result = self._values.get("width")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogQueryWidgetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IMetric)
class MathExpression(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudwatch.MathExpression",
):
    '''A math expression built with metric(s) emitted by a service.

    The math expression is a combination of an expression (x+y) and metrics to apply expression on.
    It also contains metadata which is used only in graphs, such as color and label.
    It makes sense to embed this in here, so that compound constructs can attach
    that metadata to metrics they expose.

    MathExpression can also be used for search expressions. In this case,
    it also optionally accepts a searchRegion and searchAccount property for cross-environment
    search expressions.

    This class does not represent a resource, so hence is not a construct. Instead,
    MathExpression is an abstraction that makes it easy to specify metrics for use in both
    alarms and graphs.

    :exampleMetadata: infused

    Example::

        # fn: lambda.Function
        
        
        all_problems = cloudwatch.MathExpression(
            expression="errors + throttles",
            using_metrics={
                "errors": fn.metric_errors(),
                "throttles": fn.metric_throttles()
            }
        )
    '''

    def __init__(
        self,
        *,
        expression: builtins.str,
        using_metrics: typing.Optional[typing.Mapping[builtins.str, IMetric]] = None,
        color: typing.Optional[builtins.str] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        search_account: typing.Optional[builtins.str] = None,
        search_region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param expression: The expression defining the metric. When an expression contains a SEARCH function, it cannot be used within an Alarm.
        :param using_metrics: The metrics used in the expression, in a map. The key is the identifier that represents the given metric in the expression, and the value is the actual Metric object. Default: - Empty map.
        :param color: Color for this metric when added to a Graph in a Dashboard. Default: - Automatic color
        :param label: Label for this expression when added to a Graph in a Dashboard. If this expression evaluates to more than one time series (for example, through the use of ``METRICS()`` or ``SEARCH()`` expressions), each time series will appear in the graph using a combination of the expression label and the individual metric label. Specify the empty string (``''``) to suppress the expression label and only keep the metric label. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. If the math expression produces more than one time series, the maximum will be shown for each individual time series produce by this math expression. Default: - Expression value is used as label
        :param period: The period over which the expression's statistics are applied. This period overrides all periods in the metrics used in this math expression. Default: Duration.minutes(5)
        :param search_account: Account to evaluate search expressions within. Specifying a searchAccount has no effect to the account used for metrics within the expression (passed via usingMetrics). Default: - Deployment account.
        :param search_region: Region to evaluate search expressions within. Specifying a searchRegion has no effect to the region used for metrics within the expression (passed via usingMetrics). Default: - Deployment region.
        '''
        props = MathExpressionProps(
            expression=expression,
            using_metrics=using_metrics,
            color=color,
            label=label,
            period=period,
            search_account=search_account,
            search_region=search_region,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="createAlarm")
    def create_alarm(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        evaluation_periods: jsii.Number,
        threshold: jsii.Number,
        actions_enabled: typing.Optional[builtins.bool] = None,
        alarm_description: typing.Optional[builtins.str] = None,
        alarm_name: typing.Optional[builtins.str] = None,
        comparison_operator: typing.Optional[ComparisonOperator] = None,
        datapoints_to_alarm: typing.Optional[jsii.Number] = None,
        evaluate_low_sample_count_percentile: typing.Optional[builtins.str] = None,
        treat_missing_data: typing.Optional["TreatMissingData"] = None,
    ) -> "Alarm":
        '''Make a new Alarm for this metric.

        Combines both properties that may adjust the metric (aggregation) as well
        as alarm properties.

        :param scope: -
        :param id: -
        :param evaluation_periods: The number of periods over which data is compared to the specified threshold.
        :param threshold: The value against which the specified statistic is compared.
        :param actions_enabled: Whether the actions for this alarm are enabled. Default: true
        :param alarm_description: Description for the alarm. Default: No description
        :param alarm_name: Name of the alarm. Default: Automatically generated name
        :param comparison_operator: Comparison to use to check if metric is breaching. Default: GreaterThanOrEqualToThreshold
        :param datapoints_to_alarm: The number of datapoints that must be breaching to trigger the alarm. This is used only if you are setting an "M out of N" alarm. In that case, this value is the M. For more information, see Evaluating an Alarm in the Amazon CloudWatch User Guide. Default: ``evaluationPeriods``
        :param evaluate_low_sample_count_percentile: Specifies whether to evaluate the data and potentially change the alarm state if there are too few data points to be statistically significant. Used only for alarms that are based on percentiles. Default: - Not configured.
        :param treat_missing_data: Sets how this alarm is to handle missing data points. Default: TreatMissingData.Missing
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2288caf1bef913802628b6170f42c00c75c6fb8a67ec2e269d8e950bb21fbe4b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CreateAlarmOptions(
            evaluation_periods=evaluation_periods,
            threshold=threshold,
            actions_enabled=actions_enabled,
            alarm_description=alarm_description,
            alarm_name=alarm_name,
            comparison_operator=comparison_operator,
            datapoints_to_alarm=datapoints_to_alarm,
            evaluate_low_sample_count_percentile=evaluate_low_sample_count_percentile,
            treat_missing_data=treat_missing_data,
        )

        return typing.cast("Alarm", jsii.invoke(self, "createAlarm", [scope, id, props]))

    @jsii.member(jsii_name="toMetricConfig")
    def to_metric_config(self) -> "MetricConfig":
        '''Inspect the details of the metric object.'''
        return typing.cast("MetricConfig", jsii.invoke(self, "toMetricConfig", []))

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        '''Returns a string representation of an object.'''
        return typing.cast(builtins.str, jsii.invoke(self, "toString", []))

    @jsii.member(jsii_name="with")
    def with_(
        self,
        *,
        color: typing.Optional[builtins.str] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        search_account: typing.Optional[builtins.str] = None,
        search_region: typing.Optional[builtins.str] = None,
    ) -> "MathExpression":
        '''Return a copy of Metric with properties changed.

        All properties except namespace and metricName can be changed.

        :param color: Color for this metric when added to a Graph in a Dashboard. Default: - Automatic color
        :param label: Label for this expression when added to a Graph in a Dashboard. If this expression evaluates to more than one time series (for example, through the use of ``METRICS()`` or ``SEARCH()`` expressions), each time series will appear in the graph using a combination of the expression label and the individual metric label. Specify the empty string (``''``) to suppress the expression label and only keep the metric label. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. If the math expression produces more than one time series, the maximum will be shown for each individual time series produce by this math expression. Default: - Expression value is used as label
        :param period: The period over which the expression's statistics are applied. This period overrides all periods in the metrics used in this math expression. Default: Duration.minutes(5)
        :param search_account: Account to evaluate search expressions within. Specifying a searchAccount has no effect to the account used for metrics within the expression (passed via usingMetrics). Default: - Deployment account.
        :param search_region: Region to evaluate search expressions within. Specifying a searchRegion has no effect to the region used for metrics within the expression (passed via usingMetrics). Default: - Deployment region.
        '''
        props = MathExpressionOptions(
            color=color,
            label=label,
            period=period,
            search_account=search_account,
            search_region=search_region,
        )

        return typing.cast("MathExpression", jsii.invoke(self, "with", [props]))

    @builtins.property
    @jsii.member(jsii_name="expression")
    def expression(self) -> builtins.str:
        '''The expression defining the metric.'''
        return typing.cast(builtins.str, jsii.get(self, "expression"))

    @builtins.property
    @jsii.member(jsii_name="period")
    def period(self) -> _Duration_4839e8c3:
        '''Aggregation period of this metric.'''
        return typing.cast(_Duration_4839e8c3, jsii.get(self, "period"))

    @builtins.property
    @jsii.member(jsii_name="usingMetrics")
    def using_metrics(self) -> typing.Mapping[builtins.str, IMetric]:
        '''The metrics used in the expression as KeyValuePair <id, metric>.'''
        return typing.cast(typing.Mapping[builtins.str, IMetric], jsii.get(self, "usingMetrics"))

    @builtins.property
    @jsii.member(jsii_name="color")
    def color(self) -> typing.Optional[builtins.str]:
        '''The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "color"))

    @builtins.property
    @jsii.member(jsii_name="label")
    def label(self) -> typing.Optional[builtins.str]:
        '''Label for this metric when added to a Graph.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "label"))

    @builtins.property
    @jsii.member(jsii_name="searchAccount")
    def search_account(self) -> typing.Optional[builtins.str]:
        '''Account to evaluate search expressions within.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "searchAccount"))

    @builtins.property
    @jsii.member(jsii_name="searchRegion")
    def search_region(self) -> typing.Optional[builtins.str]:
        '''Region to evaluate search expressions within.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "searchRegion"))

    @builtins.property
    @jsii.member(jsii_name="warnings")
    def warnings(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(deprecated) Warnings generated by this math expression.

        :deprecated: - use warningsV2

        :stability: deprecated
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "warnings"))

    @builtins.property
    @jsii.member(jsii_name="warningsV2")
    def warnings_v2(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Warnings generated by this math expression.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "warningsV2"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudwatch.MathExpressionOptions",
    jsii_struct_bases=[],
    name_mapping={
        "color": "color",
        "label": "label",
        "period": "period",
        "search_account": "searchAccount",
        "search_region": "searchRegion",
    },
)
class MathExpressionOptions:
    def __init__(
        self,
        *,
        color: typing.Optional[builtins.str] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        search_account: typing.Optional[builtins.str] = None,
        search_region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Configurable options for MathExpressions.

        :param color: Color for this metric when added to a Graph in a Dashboard. Default: - Automatic color
        :param label: Label for this expression when added to a Graph in a Dashboard. If this expression evaluates to more than one time series (for example, through the use of ``METRICS()`` or ``SEARCH()`` expressions), each time series will appear in the graph using a combination of the expression label and the individual metric label. Specify the empty string (``''``) to suppress the expression label and only keep the metric label. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. If the math expression produces more than one time series, the maximum will be shown for each individual time series produce by this math expression. Default: - Expression value is used as label
        :param period: The period over which the expression's statistics are applied. This period overrides all periods in the metrics used in this math expression. Default: Duration.minutes(5)
        :param search_account: Account to evaluate search expressions within. Specifying a searchAccount has no effect to the account used for metrics within the expression (passed via usingMetrics). Default: - Deployment account.
        :param search_region: Region to evaluate search expressions within. Specifying a searchRegion has no effect to the region used for metrics within the expression (passed via usingMetrics). Default: - Deployment region.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk as cdk
            from aws_cdk import aws_cloudwatch as cloudwatch
            
            math_expression_options = cloudwatch.MathExpressionOptions(
                color="color",
                label="label",
                period=cdk.Duration.minutes(30),
                search_account="searchAccount",
                search_region="searchRegion"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f28a14de04cee7a41ccdb702d4444beec1719a2620a487cbc8e934b85c29a574)
            check_type(argname="argument color", value=color, expected_type=type_hints["color"])
            check_type(argname="argument label", value=label, expected_type=type_hints["label"])
            check_type(argname="argument period", value=period, expected_type=type_hints["period"])
            check_type(argname="argument search_account", value=search_account, expected_type=type_hints["search_account"])
            check_type(argname="argument search_region", value=search_region, expected_type=type_hints["search_region"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if color is not None:
            self._values["color"] = color
        if label is not None:
            self._values["label"] = label
        if period is not None:
            self._values["period"] = period
        if search_account is not None:
            self._values["search_account"] = search_account
        if search_region is not None:
            self._values["search_region"] = search_region

    @builtins.property
    def color(self) -> typing.Optional[builtins.str]:
        '''Color for this metric when added to a Graph in a Dashboard.

        :default: - Automatic color
        '''
        result = self._values.get("color")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def label(self) -> typing.Optional[builtins.str]:
        '''Label for this expression when added to a Graph in a Dashboard.

        If this expression evaluates to more than one time series (for
        example, through the use of ``METRICS()`` or ``SEARCH()`` expressions),
        each time series will appear in the graph using a combination of the
        expression label and the individual metric label. Specify the empty
        string (``''``) to suppress the expression label and only keep the
        metric label.

        You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_
        to show summary information about the displayed time series
        in the legend. For example, if you use::

           [max: ${MAX}] MyMetric

        As the metric label, the maximum value in the visible range will
        be shown next to the time series name in the graph's legend. If the
        math expression produces more than one time series, the maximum
        will be shown for each individual time series produce by this
        math expression.

        :default: - Expression value is used as label
        '''
        result = self._values.get("label")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def period(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The period over which the expression's statistics are applied.

        This period overrides all periods in the metrics used in this
        math expression.

        :default: Duration.minutes(5)
        '''
        result = self._values.get("period")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def search_account(self) -> typing.Optional[builtins.str]:
        '''Account to evaluate search expressions within.

        Specifying a searchAccount has no effect to the account used
        for metrics within the expression (passed via usingMetrics).

        :default: - Deployment account.
        '''
        result = self._values.get("search_account")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def search_region(self) -> typing.Optional[builtins.str]:
        '''Region to evaluate search expressions within.

        Specifying a searchRegion has no effect to the region used
        for metrics within the expression (passed via usingMetrics).

        :default: - Deployment region.
        '''
        result = self._values.get("search_region")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MathExpressionOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudwatch.MathExpressionProps",
    jsii_struct_bases=[MathExpressionOptions],
    name_mapping={
        "color": "color",
        "label": "label",
        "period": "period",
        "search_account": "searchAccount",
        "search_region": "searchRegion",
        "expression": "expression",
        "using_metrics": "usingMetrics",
    },
)
class MathExpressionProps(MathExpressionOptions):
    def __init__(
        self,
        *,
        color: typing.Optional[builtins.str] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        search_account: typing.Optional[builtins.str] = None,
        search_region: typing.Optional[builtins.str] = None,
        expression: builtins.str,
        using_metrics: typing.Optional[typing.Mapping[builtins.str, IMetric]] = None,
    ) -> None:
        '''Properties for a MathExpression.

        :param color: Color for this metric when added to a Graph in a Dashboard. Default: - Automatic color
        :param label: Label for this expression when added to a Graph in a Dashboard. If this expression evaluates to more than one time series (for example, through the use of ``METRICS()`` or ``SEARCH()`` expressions), each time series will appear in the graph using a combination of the expression label and the individual metric label. Specify the empty string (``''``) to suppress the expression label and only keep the metric label. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. If the math expression produces more than one time series, the maximum will be shown for each individual time series produce by this math expression. Default: - Expression value is used as label
        :param period: The period over which the expression's statistics are applied. This period overrides all periods in the metrics used in this math expression. Default: Duration.minutes(5)
        :param search_account: Account to evaluate search expressions within. Specifying a searchAccount has no effect to the account used for metrics within the expression (passed via usingMetrics). Default: - Deployment account.
        :param search_region: Region to evaluate search expressions within. Specifying a searchRegion has no effect to the region used for metrics within the expression (passed via usingMetrics). Default: - Deployment region.
        :param expression: The expression defining the metric. When an expression contains a SEARCH function, it cannot be used within an Alarm.
        :param using_metrics: The metrics used in the expression, in a map. The key is the identifier that represents the given metric in the expression, and the value is the actual Metric object. Default: - Empty map.

        :exampleMetadata: infused

        Example::

            # fn: lambda.Function
            
            
            all_problems = cloudwatch.MathExpression(
                expression="errors + throttles",
                using_metrics={
                    "errors": fn.metric_errors(),
                    "throttles": fn.metric_throttles()
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7cfb588e44acd0977aa0e09f00c3e2435bad84385ab7b6d163b332963d844e0a)
            check_type(argname="argument color", value=color, expected_type=type_hints["color"])
            check_type(argname="argument label", value=label, expected_type=type_hints["label"])
            check_type(argname="argument period", value=period, expected_type=type_hints["period"])
            check_type(argname="argument search_account", value=search_account, expected_type=type_hints["search_account"])
            check_type(argname="argument search_region", value=search_region, expected_type=type_hints["search_region"])
            check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
            check_type(argname="argument using_metrics", value=using_metrics, expected_type=type_hints["using_metrics"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "expression": expression,
        }
        if color is not None:
            self._values["color"] = color
        if label is not None:
            self._values["label"] = label
        if period is not None:
            self._values["period"] = period
        if search_account is not None:
            self._values["search_account"] = search_account
        if search_region is not None:
            self._values["search_region"] = search_region
        if using_metrics is not None:
            self._values["using_metrics"] = using_metrics

    @builtins.property
    def color(self) -> typing.Optional[builtins.str]:
        '''Color for this metric when added to a Graph in a Dashboard.

        :default: - Automatic color
        '''
        result = self._values.get("color")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def label(self) -> typing.Optional[builtins.str]:
        '''Label for this expression when added to a Graph in a Dashboard.

        If this expression evaluates to more than one time series (for
        example, through the use of ``METRICS()`` or ``SEARCH()`` expressions),
        each time series will appear in the graph using a combination of the
        expression label and the individual metric label. Specify the empty
        string (``''``) to suppress the expression label and only keep the
        metric label.

        You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_
        to show summary information about the displayed time series
        in the legend. For example, if you use::

           [max: ${MAX}] MyMetric

        As the metric label, the maximum value in the visible range will
        be shown next to the time series name in the graph's legend. If the
        math expression produces more than one time series, the maximum
        will be shown for each individual time series produce by this
        math expression.

        :default: - Expression value is used as label
        '''
        result = self._values.get("label")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def period(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The period over which the expression's statistics are applied.

        This period overrides all periods in the metrics used in this
        math expression.

        :default: Duration.minutes(5)
        '''
        result = self._values.get("period")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def search_account(self) -> typing.Optional[builtins.str]:
        '''Account to evaluate search expressions within.

        Specifying a searchAccount has no effect to the account used
        for metrics within the expression (passed via usingMetrics).

        :default: - Deployment account.
        '''
        result = self._values.get("search_account")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def search_region(self) -> typing.Optional[builtins.str]:
        '''Region to evaluate search expressions within.

        Specifying a searchRegion has no effect to the region used
        for metrics within the expression (passed via usingMetrics).

        :default: - Deployment region.
        '''
        result = self._values.get("search_region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def expression(self) -> builtins.str:
        '''The expression defining the metric.

        When an expression contains a SEARCH function, it cannot be used
        within an Alarm.
        '''
        result = self._values.get("expression")
        assert result is not None, "Required property 'expression' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def using_metrics(self) -> typing.Optional[typing.Mapping[builtins.str, IMetric]]:
        '''The metrics used in the expression, in a map.

        The key is the identifier that represents the given metric in the
        expression, and the value is the actual Metric object.

        :default: - Empty map.
        '''
        result = self._values.get("using_metrics")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, IMetric]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MathExpressionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IMetric)
class Metric(metaclass=jsii.JSIIMeta, jsii_type="aws-cdk-lib.aws_cloudwatch.Metric"):
    '''A metric emitted by a service.

    The metric is a combination of a metric identifier (namespace, name and dimensions)
    and an aggregation function (statistic, period and unit).

    It also contains metadata which is used only in graphs, such as color and label.
    It makes sense to embed this in here, so that compound constructs can attach
    that metadata to metrics they expose.

    This class does not represent a resource, so hence is not a construct. Instead,
    Metric is an abstraction that makes it easy to specify metrics for use in both
    alarms and graphs.

    :exampleMetadata: infused

    Example::

        # fn: lambda.Function
        
        
        minute_error_rate = fn.metric_errors(
            statistic=cloudwatch.Stats.AVERAGE,
            period=Duration.minutes(1),
            label="Lambda failure rate"
        )
    '''

    def __init__(
        self,
        *,
        metric_name: builtins.str,
        namespace: builtins.str,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional["Unit"] = None,
    ) -> None:
        '''
        :param metric_name: Name of the metric.
        :param namespace: Namespace of the metric.
        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        '''
        props = MetricProps(
            metric_name=metric_name,
            namespace=namespace,
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="grantPutMetricData")
    @builtins.classmethod
    def grant_put_metric_data(cls, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant permissions to the given identity to write metrics.

        :param grantee: The IAM identity to give permissions to.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80cc2795f9742554fa1b3991c8df3ae2020ca7ee2fdc5766276d72c863b4eb74)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
        return typing.cast(_Grant_a7ae64f8, jsii.sinvoke(cls, "grantPutMetricData", [grantee]))

    @jsii.member(jsii_name="attachTo")
    def attach_to(self, scope: _constructs_77d1e7e8.IConstruct) -> "Metric":
        '''Attach the metric object to the given construct scope.

        Returns a Metric object that uses the account and region from the Stack
        the given construct is defined in. If the metric is subsequently used
        in a Dashboard or Alarm in a different Stack defined in a different
        account or region, the appropriate 'region' and 'account' fields
        will be added to it.

        If the scope we attach to is in an environment-agnostic stack,
        nothing is done and the same Metric object is returned.

        :param scope: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25be678fc533e02941d84f54a76d8c3b96a0229380a8181f05cf39cb522d894f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        return typing.cast("Metric", jsii.invoke(self, "attachTo", [scope]))

    @jsii.member(jsii_name="createAlarm")
    def create_alarm(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        evaluation_periods: jsii.Number,
        threshold: jsii.Number,
        actions_enabled: typing.Optional[builtins.bool] = None,
        alarm_description: typing.Optional[builtins.str] = None,
        alarm_name: typing.Optional[builtins.str] = None,
        comparison_operator: typing.Optional[ComparisonOperator] = None,
        datapoints_to_alarm: typing.Optional[jsii.Number] = None,
        evaluate_low_sample_count_percentile: typing.Optional[builtins.str] = None,
        treat_missing_data: typing.Optional["TreatMissingData"] = None,
    ) -> "Alarm":
        '''Make a new Alarm for this metric.

        Combines both properties that may adjust the metric (aggregation) as well
        as alarm properties.

        :param scope: -
        :param id: -
        :param evaluation_periods: The number of periods over which data is compared to the specified threshold.
        :param threshold: The value against which the specified statistic is compared.
        :param actions_enabled: Whether the actions for this alarm are enabled. Default: true
        :param alarm_description: Description for the alarm. Default: No description
        :param alarm_name: Name of the alarm. Default: Automatically generated name
        :param comparison_operator: Comparison to use to check if metric is breaching. Default: GreaterThanOrEqualToThreshold
        :param datapoints_to_alarm: The number of datapoints that must be breaching to trigger the alarm. This is used only if you are setting an "M out of N" alarm. In that case, this value is the M. For more information, see Evaluating an Alarm in the Amazon CloudWatch User Guide. Default: ``evaluationPeriods``
        :param evaluate_low_sample_count_percentile: Specifies whether to evaluate the data and potentially change the alarm state if there are too few data points to be statistically significant. Used only for alarms that are based on percentiles. Default: - Not configured.
        :param treat_missing_data: Sets how this alarm is to handle missing data points. Default: TreatMissingData.Missing
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d06465478bbcf4229dd841339de63538dcc33dff4d9dbdf0e5b10087b556a00)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CreateAlarmOptions(
            evaluation_periods=evaluation_periods,
            threshold=threshold,
            actions_enabled=actions_enabled,
            alarm_description=alarm_description,
            alarm_name=alarm_name,
            comparison_operator=comparison_operator,
            datapoints_to_alarm=datapoints_to_alarm,
            evaluate_low_sample_count_percentile=evaluate_low_sample_count_percentile,
            treat_missing_data=treat_missing_data,
        )

        return typing.cast("Alarm", jsii.invoke(self, "createAlarm", [scope, id, props]))

    @jsii.member(jsii_name="toMetricConfig")
    def to_metric_config(self) -> "MetricConfig":
        '''Inspect the details of the metric object.'''
        return typing.cast("MetricConfig", jsii.invoke(self, "toMetricConfig", []))

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        '''Returns a string representation of an object.'''
        return typing.cast(builtins.str, jsii.invoke(self, "toString", []))

    @jsii.member(jsii_name="with")
    def with_(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional["Unit"] = None,
    ) -> "Metric":
        '''Return a copy of Metric ``with`` properties changed.

        All properties except namespace and metricName can be changed.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        '''
        props = MetricOptions(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast("Metric", jsii.invoke(self, "with", [props]))

    @builtins.property
    @jsii.member(jsii_name="metricName")
    def metric_name(self) -> builtins.str:
        '''Name of this metric.'''
        return typing.cast(builtins.str, jsii.get(self, "metricName"))

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        '''Namespace of this metric.'''
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @builtins.property
    @jsii.member(jsii_name="period")
    def period(self) -> _Duration_4839e8c3:
        '''Period of this metric.'''
        return typing.cast(_Duration_4839e8c3, jsii.get(self, "period"))

    @builtins.property
    @jsii.member(jsii_name="statistic")
    def statistic(self) -> builtins.str:
        '''Statistic of this metric.'''
        return typing.cast(builtins.str, jsii.get(self, "statistic"))

    @builtins.property
    @jsii.member(jsii_name="account")
    def account(self) -> typing.Optional[builtins.str]:
        '''Account which this metric comes from.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "account"))

    @builtins.property
    @jsii.member(jsii_name="color")
    def color(self) -> typing.Optional[builtins.str]:
        '''The hex color code used when this metric is rendered on a graph.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "color"))

    @builtins.property
    @jsii.member(jsii_name="dimensions")
    def dimensions(self) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Dimensions of this metric.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], jsii.get(self, "dimensions"))

    @builtins.property
    @jsii.member(jsii_name="label")
    def label(self) -> typing.Optional[builtins.str]:
        '''Label for this metric when added to a Graph in a Dashboard.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "label"))

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> typing.Optional[builtins.str]:
        '''Region which this metric comes from.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "region"))

    @builtins.property
    @jsii.member(jsii_name="unit")
    def unit(self) -> typing.Optional["Unit"]:
        '''Unit of the metric.'''
        return typing.cast(typing.Optional["Unit"], jsii.get(self, "unit"))

    @builtins.property
    @jsii.member(jsii_name="warnings")
    def warnings(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(deprecated) Warnings attached to this metric.

        :deprecated: - use warningsV2

        :stability: deprecated
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "warnings"))

    @builtins.property
    @jsii.member(jsii_name="warningsV2")
    def warnings_v2(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Warnings attached to this metric.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "warningsV2"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudwatch.MetricConfig",
    jsii_struct_bases=[],
    name_mapping={
        "math_expression": "mathExpression",
        "metric_stat": "metricStat",
        "rendering_properties": "renderingProperties",
    },
)
class MetricConfig:
    def __init__(
        self,
        *,
        math_expression: typing.Optional[typing.Union["MetricExpressionConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        metric_stat: typing.Optional[typing.Union["MetricStatConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        rendering_properties: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> None:
        '''Properties of a rendered metric.

        :param math_expression: In case the metric is a math expression, the details of the math expression. Default: - None
        :param metric_stat: In case the metric represents a query, the details of the query. Default: - None
        :param rendering_properties: Additional properties which will be rendered if the metric is used in a dashboard. Examples are 'label' and 'color', but any key in here will be added to dashboard graphs. Default: - None

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk as cdk
            from aws_cdk import aws_cloudwatch as cloudwatch
            
            # metric: cloudwatch.Metric
            # rendering_properties: Any
            # value: Any
            
            metric_config = cloudwatch.MetricConfig(
                math_expression=cloudwatch.MetricExpressionConfig(
                    expression="expression",
                    period=123,
                    using_metrics={
                        "using_metrics_key": metric
                    },
            
                    # the properties below are optional
                    search_account="searchAccount",
                    search_region="searchRegion"
                ),
                metric_stat=cloudwatch.MetricStatConfig(
                    metric_name="metricName",
                    namespace="namespace",
                    period=cdk.Duration.minutes(30),
                    statistic="statistic",
            
                    # the properties below are optional
                    account="account",
                    dimensions=[cloudwatch.Dimension(
                        name="name",
                        value=value
                    )],
                    region="region",
                    unit_filter=cloudwatch.Unit.SECONDS
                ),
                rendering_properties={
                    "rendering_properties_key": rendering_properties
                }
            )
        '''
        if isinstance(math_expression, dict):
            math_expression = MetricExpressionConfig(**math_expression)
        if isinstance(metric_stat, dict):
            metric_stat = MetricStatConfig(**metric_stat)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ddb584abe8421d7f77520aa621133794d500e179ff044f43970dac3fd018cca)
            check_type(argname="argument math_expression", value=math_expression, expected_type=type_hints["math_expression"])
            check_type(argname="argument metric_stat", value=metric_stat, expected_type=type_hints["metric_stat"])
            check_type(argname="argument rendering_properties", value=rendering_properties, expected_type=type_hints["rendering_properties"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if math_expression is not None:
            self._values["math_expression"] = math_expression
        if metric_stat is not None:
            self._values["metric_stat"] = metric_stat
        if rendering_properties is not None:
            self._values["rendering_properties"] = rendering_properties

    @builtins.property
    def math_expression(self) -> typing.Optional["MetricExpressionConfig"]:
        '''In case the metric is a math expression, the details of the math expression.

        :default: - None
        '''
        result = self._values.get("math_expression")
        return typing.cast(typing.Optional["MetricExpressionConfig"], result)

    @builtins.property
    def metric_stat(self) -> typing.Optional["MetricStatConfig"]:
        '''In case the metric represents a query, the details of the query.

        :default: - None
        '''
        result = self._values.get("metric_stat")
        return typing.cast(typing.Optional["MetricStatConfig"], result)

    @builtins.property
    def rendering_properties(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Additional properties which will be rendered if the metric is used in a dashboard.

        Examples are 'label' and 'color', but any key in here will be
        added to dashboard graphs.

        :default: - None
        '''
        result = self._values.get("rendering_properties")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MetricConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudwatch.MetricExpressionConfig",
    jsii_struct_bases=[],
    name_mapping={
        "expression": "expression",
        "period": "period",
        "using_metrics": "usingMetrics",
        "search_account": "searchAccount",
        "search_region": "searchRegion",
    },
)
class MetricExpressionConfig:
    def __init__(
        self,
        *,
        expression: builtins.str,
        period: jsii.Number,
        using_metrics: typing.Mapping[builtins.str, IMetric],
        search_account: typing.Optional[builtins.str] = None,
        search_region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for a concrete metric.

        :param expression: Math expression for the metric.
        :param period: How many seconds to aggregate over.
        :param using_metrics: Metrics used in the math expression.
        :param search_account: Account to evaluate search expressions within. Default: - Deployment account.
        :param search_region: Region to evaluate search expressions within. Default: - Deployment region.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cloudwatch as cloudwatch
            
            # metric: cloudwatch.Metric
            
            metric_expression_config = cloudwatch.MetricExpressionConfig(
                expression="expression",
                period=123,
                using_metrics={
                    "using_metrics_key": metric
                },
            
                # the properties below are optional
                search_account="searchAccount",
                search_region="searchRegion"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78c6be62e28f1743856b4fd66c3982e1e250f21015b1ed9d4e038be59f0d4fde)
            check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
            check_type(argname="argument period", value=period, expected_type=type_hints["period"])
            check_type(argname="argument using_metrics", value=using_metrics, expected_type=type_hints["using_metrics"])
            check_type(argname="argument search_account", value=search_account, expected_type=type_hints["search_account"])
            check_type(argname="argument search_region", value=search_region, expected_type=type_hints["search_region"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "expression": expression,
            "period": period,
            "using_metrics": using_metrics,
        }
        if search_account is not None:
            self._values["search_account"] = search_account
        if search_region is not None:
            self._values["search_region"] = search_region

    @builtins.property
    def expression(self) -> builtins.str:
        '''Math expression for the metric.'''
        result = self._values.get("expression")
        assert result is not None, "Required property 'expression' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def period(self) -> jsii.Number:
        '''How many seconds to aggregate over.'''
        result = self._values.get("period")
        assert result is not None, "Required property 'period' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def using_metrics(self) -> typing.Mapping[builtins.str, IMetric]:
        '''Metrics used in the math expression.'''
        result = self._values.get("using_metrics")
        assert result is not None, "Required property 'using_metrics' is missing"
        return typing.cast(typing.Mapping[builtins.str, IMetric], result)

    @builtins.property
    def search_account(self) -> typing.Optional[builtins.str]:
        '''Account to evaluate search expressions within.

        :default: - Deployment account.
        '''
        result = self._values.get("search_account")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def search_region(self) -> typing.Optional[builtins.str]:
        '''Region to evaluate search expressions within.

        :default: - Deployment region.
        '''
        result = self._values.get("search_region")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MetricExpressionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudwatch.MetricOptions",
    jsii_struct_bases=[CommonMetricOptions],
    name_mapping={
        "account": "account",
        "color": "color",
        "dimensions_map": "dimensionsMap",
        "label": "label",
        "period": "period",
        "region": "region",
        "statistic": "statistic",
        "unit": "unit",
    },
)
class MetricOptions(CommonMetricOptions):
    def __init__(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional["Unit"] = None,
    ) -> None:
        '''Properties of a metric that can be changed.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_cloudwatch as cloudwatch
            
            # delivery_stream: firehose.DeliveryStream
            
            
            # Alarm that triggers when the per-second average of incoming bytes exceeds 90% of the current service limit
            incoming_bytes_percent_of_limit = cloudwatch.MathExpression(
                expression="incomingBytes / 300 / bytePerSecLimit",
                using_metrics={
                    "incoming_bytes": delivery_stream.metric_incoming_bytes(statistic=cloudwatch.Statistic.SUM),
                    "byte_per_sec_limit": delivery_stream.metric("BytesPerSecondLimit")
                }
            )
            
            cloudwatch.Alarm(self, "Alarm",
                metric=incoming_bytes_percent_of_limit,
                threshold=0.9,
                evaluation_periods=3
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0dbe737a4d124c27184430b7c20048e16171cb8b5b94bdac632b26d8480d8116)
            check_type(argname="argument account", value=account, expected_type=type_hints["account"])
            check_type(argname="argument color", value=color, expected_type=type_hints["color"])
            check_type(argname="argument dimensions_map", value=dimensions_map, expected_type=type_hints["dimensions_map"])
            check_type(argname="argument label", value=label, expected_type=type_hints["label"])
            check_type(argname="argument period", value=period, expected_type=type_hints["period"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument statistic", value=statistic, expected_type=type_hints["statistic"])
            check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if account is not None:
            self._values["account"] = account
        if color is not None:
            self._values["color"] = color
        if dimensions_map is not None:
            self._values["dimensions_map"] = dimensions_map
        if label is not None:
            self._values["label"] = label
        if period is not None:
            self._values["period"] = period
        if region is not None:
            self._values["region"] = region
        if statistic is not None:
            self._values["statistic"] = statistic
        if unit is not None:
            self._values["unit"] = unit

    @builtins.property
    def account(self) -> typing.Optional[builtins.str]:
        '''Account which this metric comes from.

        :default: - Deployment account.
        '''
        result = self._values.get("account")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def color(self) -> typing.Optional[builtins.str]:
        '''The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here.

        :default: - Automatic color
        '''
        result = self._values.get("color")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dimensions_map(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Dimensions of the metric.

        :default: - No dimensions.
        '''
        result = self._values.get("dimensions_map")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def label(self) -> typing.Optional[builtins.str]:
        '''Label for this metric when added to a Graph in a Dashboard.

        You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_
        to show summary information about the entire displayed time series
        in the legend. For example, if you use::

           [max: ${MAX}] MyMetric

        As the metric label, the maximum value in the visible range will
        be shown next to the time series name in the graph's legend.

        :default: - No label
        '''
        result = self._values.get("label")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def period(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The period over which the specified statistic is applied.

        :default: Duration.minutes(5)
        '''
        result = self._values.get("period")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''Region which this metric comes from.

        :default: - Deployment region.
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def statistic(self) -> typing.Optional[builtins.str]:
        '''What function to use for aggregating.

        Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings.

        Can be one of the following:

        - "Minimum" | "min"
        - "Maximum" | "max"
        - "Average" | "avg"
        - "Sum" | "sum"
        - "SampleCount | "n"
        - "pNN.NN"
        - "tmNN.NN" | "tm(NN.NN%:NN.NN%)"
        - "iqm"
        - "wmNN.NN" | "wm(NN.NN%:NN.NN%)"
        - "tcNN.NN" | "tc(NN.NN%:NN.NN%)"
        - "tsNN.NN" | "ts(NN.NN%:NN.NN%)"

        :default: Average
        '''
        result = self._values.get("statistic")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def unit(self) -> typing.Optional["Unit"]:
        '''Unit used to filter the metric stream.

        Only refer to datums emitted to the metric stream with the given unit and
        ignore all others. Only useful when datums are being emitted to the same
        metric stream under different units.

        The default is to use all matric datums in the stream, regardless of unit,
        which is recommended in nearly all cases.

        CloudWatch does not honor this property for graphs.

        :default: - All metric datums in the given metric stream
        '''
        result = self._values.get("unit")
        return typing.cast(typing.Optional["Unit"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MetricOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudwatch.MetricProps",
    jsii_struct_bases=[CommonMetricOptions],
    name_mapping={
        "account": "account",
        "color": "color",
        "dimensions_map": "dimensionsMap",
        "label": "label",
        "period": "period",
        "region": "region",
        "statistic": "statistic",
        "unit": "unit",
        "metric_name": "metricName",
        "namespace": "namespace",
    },
)
class MetricProps(CommonMetricOptions):
    def __init__(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional["Unit"] = None,
        metric_name: builtins.str,
        namespace: builtins.str,
    ) -> None:
        '''Properties for a metric.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        :param metric_name: Name of the metric.
        :param namespace: Namespace of the metric.

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_cloudwatch as cloudwatch
            
            
            metric = cloudwatch.Metric(
                namespace="MyNamespace",
                metric_name="MyMetric",
                dimensions_map={"MyDimension": "MyDimensionValue"}
            )
            alarm = cloudwatch.Alarm(self, "MyAlarm",
                metric=metric,
                threshold=100,
                evaluation_periods=3,
                datapoints_to_alarm=2
            )
            
            topic_rule = iot.TopicRule(self, "TopicRule",
                sql=iot.IotSql.from_string_as_ver20160323("SELECT topic(2) as device_id FROM 'device/+/data'"),
                actions=[
                    actions.CloudWatchSetAlarmStateAction(alarm,
                        reason="AWS Iot Rule action is triggered",
                        alarm_state_to_set=cloudwatch.AlarmState.ALARM
                    )
                ]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e1e153a11ab88ed91297aedb5d7a78a81e7bf88f8aeda51bc11ff42ebe01d74)
            check_type(argname="argument account", value=account, expected_type=type_hints["account"])
            check_type(argname="argument color", value=color, expected_type=type_hints["color"])
            check_type(argname="argument dimensions_map", value=dimensions_map, expected_type=type_hints["dimensions_map"])
            check_type(argname="argument label", value=label, expected_type=type_hints["label"])
            check_type(argname="argument period", value=period, expected_type=type_hints["period"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument statistic", value=statistic, expected_type=type_hints["statistic"])
            check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
            check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "metric_name": metric_name,
            "namespace": namespace,
        }
        if account is not None:
            self._values["account"] = account
        if color is not None:
            self._values["color"] = color
        if dimensions_map is not None:
            self._values["dimensions_map"] = dimensions_map
        if label is not None:
            self._values["label"] = label
        if period is not None:
            self._values["period"] = period
        if region is not None:
            self._values["region"] = region
        if statistic is not None:
            self._values["statistic"] = statistic
        if unit is not None:
            self._values["unit"] = unit

    @builtins.property
    def account(self) -> typing.Optional[builtins.str]:
        '''Account which this metric comes from.

        :default: - Deployment account.
        '''
        result = self._values.get("account")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def color(self) -> typing.Optional[builtins.str]:
        '''The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here.

        :default: - Automatic color
        '''
        result = self._values.get("color")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dimensions_map(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Dimensions of the metric.

        :default: - No dimensions.
        '''
        result = self._values.get("dimensions_map")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def label(self) -> typing.Optional[builtins.str]:
        '''Label for this metric when added to a Graph in a Dashboard.

        You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_
        to show summary information about the entire displayed time series
        in the legend. For example, if you use::

           [max: ${MAX}] MyMetric

        As the metric label, the maximum value in the visible range will
        be shown next to the time series name in the graph's legend.

        :default: - No label
        '''
        result = self._values.get("label")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def period(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The period over which the specified statistic is applied.

        :default: Duration.minutes(5)
        '''
        result = self._values.get("period")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''Region which this metric comes from.

        :default: - Deployment region.
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def statistic(self) -> typing.Optional[builtins.str]:
        '''What function to use for aggregating.

        Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings.

        Can be one of the following:

        - "Minimum" | "min"
        - "Maximum" | "max"
        - "Average" | "avg"
        - "Sum" | "sum"
        - "SampleCount | "n"
        - "pNN.NN"
        - "tmNN.NN" | "tm(NN.NN%:NN.NN%)"
        - "iqm"
        - "wmNN.NN" | "wm(NN.NN%:NN.NN%)"
        - "tcNN.NN" | "tc(NN.NN%:NN.NN%)"
        - "tsNN.NN" | "ts(NN.NN%:NN.NN%)"

        :default: Average
        '''
        result = self._values.get("statistic")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def unit(self) -> typing.Optional["Unit"]:
        '''Unit used to filter the metric stream.

        Only refer to datums emitted to the metric stream with the given unit and
        ignore all others. Only useful when datums are being emitted to the same
        metric stream under different units.

        The default is to use all matric datums in the stream, regardless of unit,
        which is recommended in nearly all cases.

        CloudWatch does not honor this property for graphs.

        :default: - All metric datums in the given metric stream
        '''
        result = self._values.get("unit")
        return typing.cast(typing.Optional["Unit"], result)

    @builtins.property
    def metric_name(self) -> builtins.str:
        '''Name of the metric.'''
        result = self._values.get("metric_name")
        assert result is not None, "Required property 'metric_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> builtins.str:
        '''Namespace of the metric.'''
        result = self._values.get("namespace")
        assert result is not None, "Required property 'namespace' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MetricProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudwatch.MetricStatConfig",
    jsii_struct_bases=[],
    name_mapping={
        "metric_name": "metricName",
        "namespace": "namespace",
        "period": "period",
        "statistic": "statistic",
        "account": "account",
        "dimensions": "dimensions",
        "region": "region",
        "unit_filter": "unitFilter",
    },
)
class MetricStatConfig:
    def __init__(
        self,
        *,
        metric_name: builtins.str,
        namespace: builtins.str,
        period: _Duration_4839e8c3,
        statistic: builtins.str,
        account: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Sequence[typing.Union[Dimension, typing.Dict[builtins.str, typing.Any]]]] = None,
        region: typing.Optional[builtins.str] = None,
        unit_filter: typing.Optional["Unit"] = None,
    ) -> None:
        '''Properties for a concrete metric.

        NOTE: ``unit`` is no longer on this object since it is only used for ``Alarms``, and doesn't mean what one
        would expect it to mean there anyway. It is most likely to be misused.

        :param metric_name: Name of the metric.
        :param namespace: Namespace of the metric.
        :param period: How many seconds to aggregate over.
        :param statistic: Aggregation function to use (can be either simple or a percentile).
        :param account: Account which this metric comes from. Default: Deployment account.
        :param dimensions: The dimensions to apply to the alarm. Default: []
        :param region: Region which this metric comes from. Default: Deployment region.
        :param unit_filter: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. This field has been renamed from plain ``unit`` to clearly communicate its purpose. Default: - Refer to all metric datums

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk as cdk
            from aws_cdk import aws_cloudwatch as cloudwatch
            
            # value: Any
            
            metric_stat_config = cloudwatch.MetricStatConfig(
                metric_name="metricName",
                namespace="namespace",
                period=cdk.Duration.minutes(30),
                statistic="statistic",
            
                # the properties below are optional
                account="account",
                dimensions=[cloudwatch.Dimension(
                    name="name",
                    value=value
                )],
                region="region",
                unit_filter=cloudwatch.Unit.SECONDS
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4491ad5e5a4b9301258f50e45d0278fe9bbf165c840e3c65f8feab639322bae)
            check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument period", value=period, expected_type=type_hints["period"])
            check_type(argname="argument statistic", value=statistic, expected_type=type_hints["statistic"])
            check_type(argname="argument account", value=account, expected_type=type_hints["account"])
            check_type(argname="argument dimensions", value=dimensions, expected_type=type_hints["dimensions"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument unit_filter", value=unit_filter, expected_type=type_hints["unit_filter"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "metric_name": metric_name,
            "namespace": namespace,
            "period": period,
            "statistic": statistic,
        }
        if account is not None:
            self._values["account"] = account
        if dimensions is not None:
            self._values["dimensions"] = dimensions
        if region is not None:
            self._values["region"] = region
        if unit_filter is not None:
            self._values["unit_filter"] = unit_filter

    @builtins.property
    def metric_name(self) -> builtins.str:
        '''Name of the metric.'''
        result = self._values.get("metric_name")
        assert result is not None, "Required property 'metric_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> builtins.str:
        '''Namespace of the metric.'''
        result = self._values.get("namespace")
        assert result is not None, "Required property 'namespace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def period(self) -> _Duration_4839e8c3:
        '''How many seconds to aggregate over.'''
        result = self._values.get("period")
        assert result is not None, "Required property 'period' is missing"
        return typing.cast(_Duration_4839e8c3, result)

    @builtins.property
    def statistic(self) -> builtins.str:
        '''Aggregation function to use (can be either simple or a percentile).'''
        result = self._values.get("statistic")
        assert result is not None, "Required property 'statistic' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def account(self) -> typing.Optional[builtins.str]:
        '''Account which this metric comes from.

        :default: Deployment account.
        '''
        result = self._values.get("account")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dimensions(self) -> typing.Optional[typing.List[Dimension]]:
        '''The dimensions to apply to the alarm.

        :default: []
        '''
        result = self._values.get("dimensions")
        return typing.cast(typing.Optional[typing.List[Dimension]], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''Region which this metric comes from.

        :default: Deployment region.
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def unit_filter(self) -> typing.Optional["Unit"]:
        '''Unit used to filter the metric stream.

        Only refer to datums emitted to the metric stream with the given unit and
        ignore all others. Only useful when datums are being emitted to the same
        metric stream under different units.

        This field has been renamed from plain ``unit`` to clearly communicate
        its purpose.

        :default: - Refer to all metric datums
        '''
        result = self._values.get("unit_filter")
        return typing.cast(typing.Optional["Unit"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MetricStatConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudwatch.MetricWidgetProps",
    jsii_struct_bases=[],
    name_mapping={
        "height": "height",
        "region": "region",
        "title": "title",
        "width": "width",
    },
)
class MetricWidgetProps:
    def __init__(
        self,
        *,
        height: typing.Optional[jsii.Number] = None,
        region: typing.Optional[builtins.str] = None,
        title: typing.Optional[builtins.str] = None,
        width: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Basic properties for widgets that display metrics.

        :param height: Height of the widget. Default: - 6 for Alarm and Graph widgets. 3 for single value widgets where most recent value of a metric is displayed.
        :param region: The region the metrics of this graph should be taken from. Default: - Current region
        :param title: Title for the graph. Default: - None
        :param width: Width of the widget, in a grid of 24 units wide. Default: 6

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cloudwatch as cloudwatch
            
            metric_widget_props = cloudwatch.MetricWidgetProps(
                height=123,
                region="region",
                title="title",
                width=123
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__028d2c6eccbbf06b74566403b038cac0cdc1c8588c939f4352cc861885b12c38)
            check_type(argname="argument height", value=height, expected_type=type_hints["height"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument title", value=title, expected_type=type_hints["title"])
            check_type(argname="argument width", value=width, expected_type=type_hints["width"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if height is not None:
            self._values["height"] = height
        if region is not None:
            self._values["region"] = region
        if title is not None:
            self._values["title"] = title
        if width is not None:
            self._values["width"] = width

    @builtins.property
    def height(self) -> typing.Optional[jsii.Number]:
        '''Height of the widget.

        :default:

        - 6 for Alarm and Graph widgets.
        3 for single value widgets where most recent value of a metric is displayed.
        '''
        result = self._values.get("height")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''The region the metrics of this graph should be taken from.

        :default: - Current region
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def title(self) -> typing.Optional[builtins.str]:
        '''Title for the graph.

        :default: - None
        '''
        result = self._values.get("title")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def width(self) -> typing.Optional[jsii.Number]:
        '''Width of the widget, in a grid of 24 units wide.

        :default: 6
        '''
        result = self._values.get("width")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MetricWidgetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_cloudwatch.PeriodOverride")
class PeriodOverride(enum.Enum):
    '''Specify the period for graphs when the CloudWatch dashboard loads.'''

    AUTO = "AUTO"
    '''Period of all graphs on the dashboard automatically adapt to the time range of the dashboard.'''
    INHERIT = "INHERIT"
    '''Period set for each graph will be used.'''


@jsii.implements(IWidget)
class Row(metaclass=jsii.JSIIMeta, jsii_type="aws-cdk-lib.aws_cloudwatch.Row"):
    '''A widget that contains other widgets in a horizontal row.

    Widgets will be laid out next to each other

    :exampleMetadata: infused

    Example::

        # widget_a: cloudwatch.IWidget
        # widget_b: cloudwatch.IWidget
        
        
        cloudwatch.Row(widget_a, widget_b)
    '''

    def __init__(self, *widgets: IWidget) -> None:
        '''
        :param widgets: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40733d2619229fa61f0179677abbedccf016612d902783aeea0675549c61429e)
            check_type(argname="argument widgets", value=widgets, expected_type=typing.Tuple[type_hints["widgets"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        jsii.create(self.__class__, self, [*widgets])

    @jsii.member(jsii_name="addWidget")
    def add_widget(self, w: IWidget) -> None:
        '''Add the widget to this container.

        :param w: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be1559e21caabf749b14d57eaa513451f7692532be8e10362f6f35a8d79f522e)
            check_type(argname="argument w", value=w, expected_type=type_hints["w"])
        return typing.cast(None, jsii.invoke(self, "addWidget", [w]))

    @jsii.member(jsii_name="position")
    def position(self, x: jsii.Number, y: jsii.Number) -> None:
        '''Place the widget at a given position.

        :param x: -
        :param y: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__16ac800c3f04ad1be947a2de94d65265cf3e61d41b3ef93dc1a1a64706b3c07f)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
            check_type(argname="argument y", value=y, expected_type=type_hints["y"])
        return typing.cast(None, jsii.invoke(self, "position", [x, y]))

    @jsii.member(jsii_name="toJson")
    def to_json(self) -> typing.List[typing.Any]:
        '''Return the widget JSON for use in the dashboard.'''
        return typing.cast(typing.List[typing.Any], jsii.invoke(self, "toJson", []))

    @builtins.property
    @jsii.member(jsii_name="height")
    def height(self) -> jsii.Number:
        '''The amount of vertical grid units the widget will take up.'''
        return typing.cast(jsii.Number, jsii.get(self, "height"))

    @builtins.property
    @jsii.member(jsii_name="widgets")
    def widgets(self) -> typing.List[IWidget]:
        '''List of contained widgets.'''
        return typing.cast(typing.List[IWidget], jsii.get(self, "widgets"))

    @builtins.property
    @jsii.member(jsii_name="width")
    def width(self) -> jsii.Number:
        '''The amount of horizontal grid units the widget will take up.'''
        return typing.cast(jsii.Number, jsii.get(self, "width"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudwatch.SearchComponents",
    jsii_struct_bases=[],
    name_mapping={
        "dimensions": "dimensions",
        "metric_name": "metricName",
        "namespace": "namespace",
        "populate_from": "populateFrom",
    },
)
class SearchComponents:
    def __init__(
        self,
        *,
        dimensions: typing.Sequence[builtins.str],
        metric_name: builtins.str,
        namespace: builtins.str,
        populate_from: builtins.str,
    ) -> None:
        '''Search components for use with {@link Values.fromSearchComponents}.

        :param dimensions: The list of dimensions to be used in the search expression.
        :param metric_name: The metric name to be used in the search expression.
        :param namespace: The namespace to be used in the search expression.
        :param populate_from: The dimension name, that the search expression retrieves, whose values will be used to populate the values to choose from.

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_cloudwatch as cw
            
            
            dashboard = cw.Dashboard(self, "Dash",
                default_interval=Duration.days(7),
                variables=[cw.DashboardVariable(
                    id="functionName",
                    type=cw.VariableType.PATTERN,
                    label="Function",
                    input_type=cw.VariableInputType.RADIO,
                    value="originalFuncNameInDashboard",
                    # equivalent to cw.Values.fromSearch('{AWS/Lambda,FunctionName} MetricName=\"Duration\"', 'FunctionName')
                    values=cw.Values.from_search_components(
                        namespace="AWS/Lambda",
                        dimensions=["FunctionName"],
                        metric_name="Duration",
                        populate_from="FunctionName"
                    ),
                    default_value=cw.DefaultValue.FIRST,
                    visible=True
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__834c69a269555056b1b73146ff2784af68174eb591f39133c585607049d7afe7)
            check_type(argname="argument dimensions", value=dimensions, expected_type=type_hints["dimensions"])
            check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument populate_from", value=populate_from, expected_type=type_hints["populate_from"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "dimensions": dimensions,
            "metric_name": metric_name,
            "namespace": namespace,
            "populate_from": populate_from,
        }

    @builtins.property
    def dimensions(self) -> typing.List[builtins.str]:
        '''The list of dimensions to be used in the search expression.'''
        result = self._values.get("dimensions")
        assert result is not None, "Required property 'dimensions' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def metric_name(self) -> builtins.str:
        '''The metric name to be used in the search expression.'''
        result = self._values.get("metric_name")
        assert result is not None, "Required property 'metric_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> builtins.str:
        '''The namespace to be used in the search expression.'''
        result = self._values.get("namespace")
        assert result is not None, "Required property 'namespace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def populate_from(self) -> builtins.str:
        '''The dimension name, that the search expression retrieves, whose values will be used to populate the values to choose from.'''
        result = self._values.get("populate_from")
        assert result is not None, "Required property 'populate_from' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SearchComponents(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_cloudwatch.Shading")
class Shading(enum.Enum):
    '''Fill shading options that will be used with a horizontal annotation.'''

    NONE = "NONE"
    '''Don't add shading.'''
    ABOVE = "ABOVE"
    '''Add shading above the annotation.'''
    BELOW = "BELOW"
    '''Add shading below the annotation.'''


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudwatch.SingleValueWidgetProps",
    jsii_struct_bases=[MetricWidgetProps],
    name_mapping={
        "height": "height",
        "region": "region",
        "title": "title",
        "width": "width",
        "metrics": "metrics",
        "end": "end",
        "full_precision": "fullPrecision",
        "period": "period",
        "set_period_to_time_range": "setPeriodToTimeRange",
        "sparkline": "sparkline",
        "start": "start",
    },
)
class SingleValueWidgetProps(MetricWidgetProps):
    def __init__(
        self,
        *,
        height: typing.Optional[jsii.Number] = None,
        region: typing.Optional[builtins.str] = None,
        title: typing.Optional[builtins.str] = None,
        width: typing.Optional[jsii.Number] = None,
        metrics: typing.Sequence[IMetric],
        end: typing.Optional[builtins.str] = None,
        full_precision: typing.Optional[builtins.bool] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        set_period_to_time_range: typing.Optional[builtins.bool] = None,
        sparkline: typing.Optional[builtins.bool] = None,
        start: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for a SingleValueWidget.

        :param height: Height of the widget. Default: - 6 for Alarm and Graph widgets. 3 for single value widgets where most recent value of a metric is displayed.
        :param region: The region the metrics of this graph should be taken from. Default: - Current region
        :param title: Title for the graph. Default: - None
        :param width: Width of the widget, in a grid of 24 units wide. Default: 6
        :param metrics: Metrics to display.
        :param end: The end of the time range to use for each widget independently from those of the dashboard. If you specify a value for end, you must also specify a value for start. Specify an absolute time in the ISO 8601 format. For example, 2018-12-17T06:00:00.000Z. Default: When the dashboard loads, the end date will be the current time.
        :param full_precision: Whether to show as many digits as can fit, before rounding. Default: false
        :param period: The default period for all metrics in this widget. The period is the length of time represented by one data point on the graph. This default can be overridden within each metric definition. Default: cdk.Duration.seconds(300)
        :param set_period_to_time_range: Whether to show the value from the entire time range. Default: false
        :param sparkline: Whether to show a graph below the value illustrating the value for the whole time range. Cannot be used in combination with ``setPeriodToTimeRange`` Default: false
        :param start: The start of the time range to use for each widget independently from those of the dashboard. You can specify start without specifying end to specify a relative time range that ends with the current time. In this case, the value of start must begin with -P, and you can use M, H, D, W and M as abbreviations for minutes, hours, days, weeks and months. For example, -PT8H shows the last 8 hours and -P3M shows the last three months. You can also use start along with an end field, to specify an absolute time range. When specifying an absolute time range, use the ISO 8601 format. For example, 2018-12-17T06:00:00.000Z. Default: When the dashboard loads, the start time will be the default time range.

        :exampleMetadata: infused

        Example::

            # dashboard: cloudwatch.Dashboard
            
            
            dashboard.add_widgets(cloudwatch.SingleValueWidget(
                metrics=[],
            
                period=Duration.minutes(15)
            ))
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4596565f40195bdcc9fe939fa585a3bdf484f8a4a6817e427c6f9e1e49650041)
            check_type(argname="argument height", value=height, expected_type=type_hints["height"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument title", value=title, expected_type=type_hints["title"])
            check_type(argname="argument width", value=width, expected_type=type_hints["width"])
            check_type(argname="argument metrics", value=metrics, expected_type=type_hints["metrics"])
            check_type(argname="argument end", value=end, expected_type=type_hints["end"])
            check_type(argname="argument full_precision", value=full_precision, expected_type=type_hints["full_precision"])
            check_type(argname="argument period", value=period, expected_type=type_hints["period"])
            check_type(argname="argument set_period_to_time_range", value=set_period_to_time_range, expected_type=type_hints["set_period_to_time_range"])
            check_type(argname="argument sparkline", value=sparkline, expected_type=type_hints["sparkline"])
            check_type(argname="argument start", value=start, expected_type=type_hints["start"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "metrics": metrics,
        }
        if height is not None:
            self._values["height"] = height
        if region is not None:
            self._values["region"] = region
        if title is not None:
            self._values["title"] = title
        if width is not None:
            self._values["width"] = width
        if end is not None:
            self._values["end"] = end
        if full_precision is not None:
            self._values["full_precision"] = full_precision
        if period is not None:
            self._values["period"] = period
        if set_period_to_time_range is not None:
            self._values["set_period_to_time_range"] = set_period_to_time_range
        if sparkline is not None:
            self._values["sparkline"] = sparkline
        if start is not None:
            self._values["start"] = start

    @builtins.property
    def height(self) -> typing.Optional[jsii.Number]:
        '''Height of the widget.

        :default:

        - 6 for Alarm and Graph widgets.
        3 for single value widgets where most recent value of a metric is displayed.
        '''
        result = self._values.get("height")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''The region the metrics of this graph should be taken from.

        :default: - Current region
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def title(self) -> typing.Optional[builtins.str]:
        '''Title for the graph.

        :default: - None
        '''
        result = self._values.get("title")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def width(self) -> typing.Optional[jsii.Number]:
        '''Width of the widget, in a grid of 24 units wide.

        :default: 6
        '''
        result = self._values.get("width")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def metrics(self) -> typing.List[IMetric]:
        '''Metrics to display.'''
        result = self._values.get("metrics")
        assert result is not None, "Required property 'metrics' is missing"
        return typing.cast(typing.List[IMetric], result)

    @builtins.property
    def end(self) -> typing.Optional[builtins.str]:
        '''The end of the time range to use for each widget independently from those of the dashboard.

        If you specify a value for end, you must also specify a value for start.
        Specify an absolute time in the ISO 8601 format. For example, 2018-12-17T06:00:00.000Z.

        :default: When the dashboard loads, the end date will be the current time.
        '''
        result = self._values.get("end")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def full_precision(self) -> typing.Optional[builtins.bool]:
        '''Whether to show as many digits as can fit, before rounding.

        :default: false
        '''
        result = self._values.get("full_precision")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def period(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The default period for all metrics in this widget.

        The period is the length of time represented by one data point on the graph.
        This default can be overridden within each metric definition.

        :default: cdk.Duration.seconds(300)
        '''
        result = self._values.get("period")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def set_period_to_time_range(self) -> typing.Optional[builtins.bool]:
        '''Whether to show the value from the entire time range.

        :default: false
        '''
        result = self._values.get("set_period_to_time_range")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def sparkline(self) -> typing.Optional[builtins.bool]:
        '''Whether to show a graph below the value illustrating the value for the whole time range.

        Cannot be used in combination with ``setPeriodToTimeRange``

        :default: false
        '''
        result = self._values.get("sparkline")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def start(self) -> typing.Optional[builtins.str]:
        '''The start of the time range to use for each widget independently from those of the dashboard.

        You can specify start without specifying end to specify a relative time range that ends with the current time.
        In this case, the value of start must begin with -P, and you can use M, H, D, W and M as abbreviations for
        minutes, hours, days, weeks and months. For example, -PT8H shows the last 8 hours and -P3M shows the last three months.
        You can also use start along with an end field, to specify an absolute time range.
        When specifying an absolute time range, use the ISO 8601 format. For example, 2018-12-17T06:00:00.000Z.

        :default: When the dashboard loads, the start time will be the default time range.
        '''
        result = self._values.get("start")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SingleValueWidgetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IWidget)
class Spacer(metaclass=jsii.JSIIMeta, jsii_type="aws-cdk-lib.aws_cloudwatch.Spacer"):
    '''A widget that doesn't display anything but takes up space.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_cloudwatch as cloudwatch
        
        spacer = cloudwatch.Spacer(
            height=123,
            width=123
        )
    '''

    def __init__(
        self,
        *,
        height: typing.Optional[jsii.Number] = None,
        width: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param height: Height of the spacer. Default: : 1
        :param width: Width of the spacer. Default: 1
        '''
        props = SpacerProps(height=height, width=width)

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="position")
    def position(self, _x: jsii.Number, _y: jsii.Number) -> None:
        '''Place the widget at a given position.

        :param _x: -
        :param _y: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0236fe592a65d0a71aaf6677c75eec030eb736094a2786b8e76b8268bf9a92ed)
            check_type(argname="argument _x", value=_x, expected_type=type_hints["_x"])
            check_type(argname="argument _y", value=_y, expected_type=type_hints["_y"])
        return typing.cast(None, jsii.invoke(self, "position", [_x, _y]))

    @jsii.member(jsii_name="toJson")
    def to_json(self) -> typing.List[typing.Any]:
        '''Return the widget JSON for use in the dashboard.'''
        return typing.cast(typing.List[typing.Any], jsii.invoke(self, "toJson", []))

    @builtins.property
    @jsii.member(jsii_name="height")
    def height(self) -> jsii.Number:
        '''The amount of vertical grid units the widget will take up.'''
        return typing.cast(jsii.Number, jsii.get(self, "height"))

    @builtins.property
    @jsii.member(jsii_name="width")
    def width(self) -> jsii.Number:
        '''The amount of horizontal grid units the widget will take up.'''
        return typing.cast(jsii.Number, jsii.get(self, "width"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudwatch.SpacerProps",
    jsii_struct_bases=[],
    name_mapping={"height": "height", "width": "width"},
)
class SpacerProps:
    def __init__(
        self,
        *,
        height: typing.Optional[jsii.Number] = None,
        width: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Props of the spacer.

        :param height: Height of the spacer. Default: : 1
        :param width: Width of the spacer. Default: 1

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cloudwatch as cloudwatch
            
            spacer_props = cloudwatch.SpacerProps(
                height=123,
                width=123
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ce130b788b85b7cf4858285014ef18ed05d407efad51e70fc325d771e03cd07)
            check_type(argname="argument height", value=height, expected_type=type_hints["height"])
            check_type(argname="argument width", value=width, expected_type=type_hints["width"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if height is not None:
            self._values["height"] = height
        if width is not None:
            self._values["width"] = width

    @builtins.property
    def height(self) -> typing.Optional[jsii.Number]:
        '''Height of the spacer.

        :default: : 1
        '''
        result = self._values.get("height")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def width(self) -> typing.Optional[jsii.Number]:
        '''Width of the spacer.

        :default: 1
        '''
        result = self._values.get("width")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SpacerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_cloudwatch.Statistic")
class Statistic(enum.Enum):
    '''(deprecated) Statistic to use over the aggregation period.

    :deprecated: Use one of the factory methods on ``Stats`` to produce statistics strings

    :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Statistics-definitions.html
    :stability: deprecated
    :exampleMetadata: infused

    Example::

        # matchmaking_rule_set: gamelift.MatchmakingRuleSet
        
        # Alarm that triggers when the per-second average of not placed matches exceed 10%
        rule_evaluation_ratio = cloudwatch.MathExpression(
            expression="1 - (ruleEvaluationsPassed / ruleEvaluationsFailed)",
            using_metrics={
                "rule_evaluations_passed": matchmaking_rule_set.metric_rule_evaluations_passed(statistic=cloudwatch.Statistic.SUM),
                "rule_evaluations_failed": matchmaking_rule_set.metric("ruleEvaluationsFailed")
            }
        )
        cloudwatch.Alarm(self, "Alarm",
            metric=rule_evaluation_ratio,
            threshold=0.1,
            evaluation_periods=3
        )
    '''

    SAMPLE_COUNT = "SAMPLE_COUNT"
    '''(deprecated) The count (number) of data points used for the statistical calculation.

    :stability: deprecated
    '''
    AVERAGE = "AVERAGE"
    '''(deprecated) The value of Sum / SampleCount during the specified period.

    :stability: deprecated
    '''
    SUM = "SUM"
    '''(deprecated) All values submitted for the matching metric added together.

    This statistic can be useful for determining the total volume of a metric.

    :stability: deprecated
    '''
    MINIMUM = "MINIMUM"
    '''(deprecated) The lowest value observed during the specified period.

    You can use this value to determine low volumes of activity for your application.

    :stability: deprecated
    '''
    MAXIMUM = "MAXIMUM"
    '''(deprecated) The highest value observed during the specified period.

    You can use this value to determine high volumes of activity for your application.

    :stability: deprecated
    '''


class Stats(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="aws-cdk-lib.aws_cloudwatch.Stats",
):
    '''Factory functions for standard statistics strings.

    :exampleMetadata: infused

    Example::

        # dashboard: cloudwatch.Dashboard
        # execution_count_metric: cloudwatch.Metric
        # error_count_metric: cloudwatch.Metric
        
        
        dashboard.add_widgets(cloudwatch.GraphWidget(
            title="Executions vs error rate",
        
            left=[execution_count_metric],
        
            right=[error_count_metric.with(
                statistic=cloudwatch.Stats.AVERAGE,
                label="Error rate",
                color=cloudwatch.Color.GREEN
            )]
        ))
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="p")
    @builtins.classmethod
    def p(cls, percentile: jsii.Number) -> builtins.str:
        '''A shorter alias for ``percentile()``.

        :param percentile: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6fe6b13717c2f469cb6495af37c0676d3baf89c7971d1f4421f83fb8386423c5)
            check_type(argname="argument percentile", value=percentile, expected_type=type_hints["percentile"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "p", [percentile]))

    @jsii.member(jsii_name="percentile")
    @builtins.classmethod
    def percentile(cls, percentile: jsii.Number) -> builtins.str:
        '''Percentile indicates the relative standing of a value in a dataset.

        Percentiles help you get a better understanding of the distribution of your metric data.

        For example, ``p(90)`` is the 90th percentile and means that 90% of the data
        within the period is lower than this value and 10% of the data is higher
        than this value.

        :param percentile: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b20618ea2205ed15f0a41b04678afac5b1c065f0b533015b7b38bc29faf2d28f)
            check_type(argname="argument percentile", value=percentile, expected_type=type_hints["percentile"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "percentile", [percentile]))

    @jsii.member(jsii_name="percentileRank")
    @builtins.classmethod
    def percentile_rank(
        cls,
        v1: jsii.Number,
        v2: typing.Optional[jsii.Number] = None,
    ) -> builtins.str:
        '''Percentile rank (PR) is the percentage of values that meet a fixed threshold.

        - If two numbers are given, they define the lower and upper bounds in absolute values,
          respectively.
        - If one number is given, it defines the upper bound (the lower bound is assumed to
          be 0).

        For example, ``percentileRank(300)`` returns the percentage of data points that have a value of 300 or less.
        ``percentileRank(100, 2000)`` returns the percentage of data points that have a value between 100 and 2000.

        :param v1: -
        :param v2: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c9c42984ea88c4bfe005c7b416b3bc4f37f123fcb4179c31c52608b1d17d6ad)
            check_type(argname="argument v1", value=v1, expected_type=type_hints["v1"])
            check_type(argname="argument v2", value=v2, expected_type=type_hints["v2"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "percentileRank", [v1, v2]))

    @jsii.member(jsii_name="pr")
    @builtins.classmethod
    def pr(
        cls,
        v1: jsii.Number,
        v2: typing.Optional[jsii.Number] = None,
    ) -> builtins.str:
        '''Shorter alias for ``percentileRank()``.

        :param v1: -
        :param v2: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a8709abf45bdade8c71c455bb23d9992475641bb192922b080e052213ff7a2d)
            check_type(argname="argument v1", value=v1, expected_type=type_hints["v1"])
            check_type(argname="argument v2", value=v2, expected_type=type_hints["v2"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "pr", [v1, v2]))

    @jsii.member(jsii_name="tc")
    @builtins.classmethod
    def tc(
        cls,
        p1: jsii.Number,
        p2: typing.Optional[jsii.Number] = None,
    ) -> builtins.str:
        '''Shorter alias for ``trimmedCount()``.

        :param p1: -
        :param p2: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a59697bf582c1a9d2cf797a3831d238c515f86f8b25fa39d523b89bc479ee7b)
            check_type(argname="argument p1", value=p1, expected_type=type_hints["p1"])
            check_type(argname="argument p2", value=p2, expected_type=type_hints["p2"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "tc", [p1, p2]))

    @jsii.member(jsii_name="tm")
    @builtins.classmethod
    def tm(
        cls,
        p1: jsii.Number,
        p2: typing.Optional[jsii.Number] = None,
    ) -> builtins.str:
        '''A shorter alias for ``trimmedMean()``.

        :param p1: -
        :param p2: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f436c4f45d1d4c4b619c5d92a59806b069fccea9b744eb05a1a8a63d5fad1bc1)
            check_type(argname="argument p1", value=p1, expected_type=type_hints["p1"])
            check_type(argname="argument p2", value=p2, expected_type=type_hints["p2"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "tm", [p1, p2]))

    @jsii.member(jsii_name="trimmedCount")
    @builtins.classmethod
    def trimmed_count(
        cls,
        p1: jsii.Number,
        p2: typing.Optional[jsii.Number] = None,
    ) -> builtins.str:
        '''Trimmed count (TC) is the number of data points in the chosen range for a trimmed mean statistic.

        - If two numbers are given, they define the lower and upper bounds in percentages,
          respectively.
        - If one number is given, it defines the upper bound (the lower bound is assumed to
          be 0).

        For example, ``tc(90)`` returns the number of data points not including any
        data points that fall in the highest 10% of the values. ``tc(10, 90)``
        returns the number of data points not including any data points that fall
        in the lowest 10% of the values and the highest 90% of the values.

        :param p1: -
        :param p2: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4039f2f3dc599b3ff76634eaaa717bb526fa7c9790b7eb4d412a7860ef92c6c8)
            check_type(argname="argument p1", value=p1, expected_type=type_hints["p1"])
            check_type(argname="argument p2", value=p2, expected_type=type_hints["p2"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "trimmedCount", [p1, p2]))

    @jsii.member(jsii_name="trimmedMean")
    @builtins.classmethod
    def trimmed_mean(
        cls,
        p1: jsii.Number,
        p2: typing.Optional[jsii.Number] = None,
    ) -> builtins.str:
        '''Trimmed mean (TM) is the mean of all values that are between two specified boundaries.

        Values outside of the boundaries are ignored when the mean is calculated.
        You define the boundaries as one or two numbers between 0 and 100, up to 10
        decimal places. The numbers are percentages.

        - If two numbers are given, they define the lower and upper bounds in percentages,
          respectively.
        - If one number is given, it defines the upper bound (the lower bound is assumed to
          be 0).

        For example, ``tm(90)`` calculates the average after removing the 10% of data
        points with the highest values; ``tm(10, 90)`` calculates the average after removing the
        10% with the lowest and 10% with the highest values.

        :param p1: -
        :param p2: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a459a1d21547ef8c2ced058c40dc9c19552a9b7c47f0c98c4f674eea7415c1b4)
            check_type(argname="argument p1", value=p1, expected_type=type_hints["p1"])
            check_type(argname="argument p2", value=p2, expected_type=type_hints["p2"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "trimmedMean", [p1, p2]))

    @jsii.member(jsii_name="trimmedSum")
    @builtins.classmethod
    def trimmed_sum(
        cls,
        p1: jsii.Number,
        p2: typing.Optional[jsii.Number] = None,
    ) -> builtins.str:
        '''Trimmed sum (TS) is the sum of the values of data points in a chosen range for a trimmed mean statistic.

        It is equivalent to ``(Trimmed Mean) * (Trimmed count)``.

        - If two numbers are given, they define the lower and upper bounds in percentages,
          respectively.
        - If one number is given, it defines the upper bound (the lower bound is assumed to
          be 0).

        For example, ``ts(90)`` returns the sum of the data points not including any
        data points that fall in the highest 10% of the values.  ``ts(10, 90)``
        returns the sum of the data points not including any data points that fall
        in the lowest 10% of the values and the highest 90% of the values.

        :param p1: -
        :param p2: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b907dc76d7f5d30c86b61f5d0bc18c4c525bb2d23f21bb493c2c59eb8918a669)
            check_type(argname="argument p1", value=p1, expected_type=type_hints["p1"])
            check_type(argname="argument p2", value=p2, expected_type=type_hints["p2"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "trimmedSum", [p1, p2]))

    @jsii.member(jsii_name="ts")
    @builtins.classmethod
    def ts(
        cls,
        p1: jsii.Number,
        p2: typing.Optional[jsii.Number] = None,
    ) -> builtins.str:
        '''Shorter alias for ``trimmedSum()``.

        :param p1: -
        :param p2: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b47525d73a908d3fb5feeddc346925ac46e91b28aeb372a1d789770b4b54554b)
            check_type(argname="argument p1", value=p1, expected_type=type_hints["p1"])
            check_type(argname="argument p2", value=p2, expected_type=type_hints["p2"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "ts", [p1, p2]))

    @jsii.member(jsii_name="winsorizedMean")
    @builtins.classmethod
    def winsorized_mean(
        cls,
        p1: jsii.Number,
        p2: typing.Optional[jsii.Number] = None,
    ) -> builtins.str:
        '''Winsorized mean (WM) is similar to trimmed mean.

        However, with winsorized mean, the values that are outside the boundary are
        not ignored, but instead are considered to be equal to the value at the
        edge of the appropriate boundary.  After this normalization, the average is
        calculated. You define the boundaries as one or two numbers between 0 and
        100, up to 10 decimal places.

        - If two numbers are given, they define the lower and upper bounds in percentages,
          respectively.
        - If one number is given, it defines the upper bound (the lower bound is assumed to
          be 0).

        For example, ``tm(90)`` calculates the average after removing the 10% of data
        points with the highest values; ``tm(10, 90)`` calculates the average after removing the
        10% with the lowest and 10% with the highest values.

        For example, ``wm(90)`` calculates the average while treating the 10% of the
        highest values to be equal to the value at the 90th percentile.
        ``wm(10, 90)`` calculates the average while treaing the bottom 10% and the
        top 10% of values to be equal to the boundary values.

        :param p1: -
        :param p2: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56e0f0610a2a67b4632bbdfee23cd7509fcd0e93b34d23c36208dc99ac803774)
            check_type(argname="argument p1", value=p1, expected_type=type_hints["p1"])
            check_type(argname="argument p2", value=p2, expected_type=type_hints["p2"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "winsorizedMean", [p1, p2]))

    @jsii.member(jsii_name="wm")
    @builtins.classmethod
    def wm(
        cls,
        p1: jsii.Number,
        p2: typing.Optional[jsii.Number] = None,
    ) -> builtins.str:
        '''A shorter alias for ``winsorizedMean()``.

        :param p1: -
        :param p2: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1740e870895a9795d40caa429b748dd124ed575f6ae4335284294f42209ae324)
            check_type(argname="argument p1", value=p1, expected_type=type_hints["p1"])
            check_type(argname="argument p2", value=p2, expected_type=type_hints["p2"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "wm", [p1, p2]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AVERAGE")
    def AVERAGE(cls) -> builtins.str:
        '''The value of Sum / SampleCount during the specified period.'''
        return typing.cast(builtins.str, jsii.sget(cls, "AVERAGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IQM")
    def IQM(cls) -> builtins.str:
        '''Interquartile mean (IQM) is the trimmed mean of the interquartile range, or the middle 50% of values.

        It is equivalent to ``trimmedMean(25, 75)``.
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "IQM"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="MAXIMUM")
    def MAXIMUM(cls) -> builtins.str:
        '''The highest value observed during the specified period.

        You can use this value to determine high volumes of activity for your application.
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "MAXIMUM"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="MINIMUM")
    def MINIMUM(cls) -> builtins.str:
        '''The lowest value observed during the specified period.

        You can use this value to determine low volumes of activity for your application.
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "MINIMUM"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SAMPLE_COUNT")
    def SAMPLE_COUNT(cls) -> builtins.str:
        '''The count (number) of data points used for the statistical calculation.'''
        return typing.cast(builtins.str, jsii.sget(cls, "SAMPLE_COUNT"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SUM")
    def SUM(cls) -> builtins.str:
        '''All values submitted for the matching metric added together.

        This statistic can be useful for determining the total volume of a metric.
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "SUM"))


class _StatsProxy(Stats):
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, Stats).__jsii_proxy_class__ = lambda : _StatsProxy


@jsii.enum(jsii_type="aws-cdk-lib.aws_cloudwatch.TableLayout")
class TableLayout(enum.Enum):
    '''Layout for TableWidget.

    :exampleMetadata: infused

    Example::

        # dashboard: cloudwatch.Dashboard
        
        
        dashboard.add_widgets(cloudwatch.TableWidget(
            # ...
        
            layout=cloudwatch.TableLayout.VERTICAL
        ))
    '''

    HORIZONTAL = "HORIZONTAL"
    '''Data points are laid out in columns.'''
    VERTICAL = "VERTICAL"
    '''Data points are laid out in rows.'''


@jsii.enum(jsii_type="aws-cdk-lib.aws_cloudwatch.TableSummaryColumn")
class TableSummaryColumn(enum.Enum):
    '''Standard table summary columns.

    :exampleMetadata: infused

    Example::

        # dashboard: cloudwatch.Dashboard
        
        
        dashboard.add_widgets(cloudwatch.TableWidget(
            # ...
        
            summary=cloudwatch.TableSummaryProps(
                columns=[cloudwatch.TableSummaryColumn.AVERAGE],
                hide_non_summary_columns=True,
                sticky=True
            )
        ))
    '''

    MINIMUM = "MINIMUM"
    '''Minimum of all data points.'''
    MAXIMUM = "MAXIMUM"
    '''Maximum of all data points.'''
    SUM = "SUM"
    '''Sum of all data points.'''
    AVERAGE = "AVERAGE"
    '''Average of all data points.'''


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudwatch.TableSummaryProps",
    jsii_struct_bases=[],
    name_mapping={
        "columns": "columns",
        "hide_non_summary_columns": "hideNonSummaryColumns",
        "sticky": "sticky",
    },
)
class TableSummaryProps:
    def __init__(
        self,
        *,
        columns: typing.Optional[typing.Sequence[TableSummaryColumn]] = None,
        hide_non_summary_columns: typing.Optional[builtins.bool] = None,
        sticky: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Properties for TableWidget's summary columns.

        :param columns: Summary columns. Default: - No summary columns will be shown
        :param hide_non_summary_columns: Prevent the columns of datapoints from being displayed, so that only the label and summary columns are displayed. Default: - false
        :param sticky: Make the summary columns sticky, so that they remain in view while scrolling. Default: - false

        :exampleMetadata: infused

        Example::

            # dashboard: cloudwatch.Dashboard
            
            
            dashboard.add_widgets(cloudwatch.TableWidget(
                # ...
            
                summary=cloudwatch.TableSummaryProps(
                    columns=[cloudwatch.TableSummaryColumn.AVERAGE],
                    hide_non_summary_columns=True,
                    sticky=True
                )
            ))
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98c18eab758ffae376ffa1675e2524ad60cd0a50fd033fe135c6d98d0f5d2692)
            check_type(argname="argument columns", value=columns, expected_type=type_hints["columns"])
            check_type(argname="argument hide_non_summary_columns", value=hide_non_summary_columns, expected_type=type_hints["hide_non_summary_columns"])
            check_type(argname="argument sticky", value=sticky, expected_type=type_hints["sticky"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if columns is not None:
            self._values["columns"] = columns
        if hide_non_summary_columns is not None:
            self._values["hide_non_summary_columns"] = hide_non_summary_columns
        if sticky is not None:
            self._values["sticky"] = sticky

    @builtins.property
    def columns(self) -> typing.Optional[typing.List[TableSummaryColumn]]:
        '''Summary columns.

        :default: - No summary columns will be shown
        '''
        result = self._values.get("columns")
        return typing.cast(typing.Optional[typing.List[TableSummaryColumn]], result)

    @builtins.property
    def hide_non_summary_columns(self) -> typing.Optional[builtins.bool]:
        '''Prevent the columns of datapoints from being displayed, so that only the label and summary columns are displayed.

        :default: - false
        '''
        result = self._values.get("hide_non_summary_columns")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def sticky(self) -> typing.Optional[builtins.bool]:
        '''Make the summary columns sticky, so that they remain in view while scrolling.

        :default: - false
        '''
        result = self._values.get("sticky")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TableSummaryProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TableThreshold(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudwatch.TableThreshold",
):
    '''Thresholds for highlighting cells in TableWidget.

    :exampleMetadata: infused

    Example::

        # dashboard: cloudwatch.Dashboard
        
        
        dashboard.add_widgets(cloudwatch.TableWidget(
            # ...
        
            thresholds=[
                cloudwatch.TableThreshold.above(1000, cloudwatch.Color.RED),
                cloudwatch.TableThreshold.between(500, 1000, cloudwatch.Color.ORANGE),
                cloudwatch.TableThreshold.below(500, cloudwatch.Color.GREEN)
            ]
        ))
    '''

    @jsii.member(jsii_name="above")
    @builtins.classmethod
    def above(
        cls,
        value: jsii.Number,
        color: typing.Optional[builtins.str] = None,
    ) -> "TableThreshold":
        '''A threshold for highlighting and coloring cells above the specified value.

        :param value: lower bound of threshold range.
        :param color: cell color for values within threshold range.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70d2d8bf527174c0069d64738e83c5ebe4fd927ac2332ac0de67140546fb8616)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            check_type(argname="argument color", value=color, expected_type=type_hints["color"])
        return typing.cast("TableThreshold", jsii.sinvoke(cls, "above", [value, color]))

    @jsii.member(jsii_name="below")
    @builtins.classmethod
    def below(
        cls,
        value: jsii.Number,
        color: typing.Optional[builtins.str] = None,
    ) -> "TableThreshold":
        '''A threshold for highlighting and coloring cells below the specified value.

        :param value: upper bound of threshold range.
        :param color: cell color for values within threshold range.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6f92993218488cf545481e8167442910bb8b8c7c45aa7dfb6667808cb1077e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            check_type(argname="argument color", value=color, expected_type=type_hints["color"])
        return typing.cast("TableThreshold", jsii.sinvoke(cls, "below", [value, color]))

    @jsii.member(jsii_name="between")
    @builtins.classmethod
    def between(
        cls,
        lower_bound: jsii.Number,
        upper_bound: jsii.Number,
        color: typing.Optional[builtins.str] = None,
    ) -> "TableThreshold":
        '''A threshold for highlighting and coloring cells within the specified values.

        :param lower_bound: lower bound of threshold range.
        :param upper_bound: upper bound of threshold range.
        :param color: cell color for values within threshold range.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__837fdebf81b3f53de6d99624ebde152b4aba1d764a0cc2bd930440701533924a)
            check_type(argname="argument lower_bound", value=lower_bound, expected_type=type_hints["lower_bound"])
            check_type(argname="argument upper_bound", value=upper_bound, expected_type=type_hints["upper_bound"])
            check_type(argname="argument color", value=color, expected_type=type_hints["color"])
        return typing.cast("TableThreshold", jsii.sinvoke(cls, "between", [lower_bound, upper_bound, color]))

    @jsii.member(jsii_name="toJson")
    def to_json(self) -> typing.Any:
        return typing.cast(typing.Any, jsii.invoke(self, "toJson", []))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudwatch.TableWidgetProps",
    jsii_struct_bases=[MetricWidgetProps],
    name_mapping={
        "height": "height",
        "region": "region",
        "title": "title",
        "width": "width",
        "end": "end",
        "full_precision": "fullPrecision",
        "layout": "layout",
        "live_data": "liveData",
        "metrics": "metrics",
        "period": "period",
        "set_period_to_time_range": "setPeriodToTimeRange",
        "show_units_in_label": "showUnitsInLabel",
        "start": "start",
        "statistic": "statistic",
        "summary": "summary",
        "thresholds": "thresholds",
    },
)
class TableWidgetProps(MetricWidgetProps):
    def __init__(
        self,
        *,
        height: typing.Optional[jsii.Number] = None,
        region: typing.Optional[builtins.str] = None,
        title: typing.Optional[builtins.str] = None,
        width: typing.Optional[jsii.Number] = None,
        end: typing.Optional[builtins.str] = None,
        full_precision: typing.Optional[builtins.bool] = None,
        layout: typing.Optional[TableLayout] = None,
        live_data: typing.Optional[builtins.bool] = None,
        metrics: typing.Optional[typing.Sequence[IMetric]] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        set_period_to_time_range: typing.Optional[builtins.bool] = None,
        show_units_in_label: typing.Optional[builtins.bool] = None,
        start: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        summary: typing.Optional[typing.Union[TableSummaryProps, typing.Dict[builtins.str, typing.Any]]] = None,
        thresholds: typing.Optional[typing.Sequence[TableThreshold]] = None,
    ) -> None:
        '''Properties for a TableWidget.

        :param height: Height of the widget. Default: - 6 for Alarm and Graph widgets. 3 for single value widgets where most recent value of a metric is displayed.
        :param region: The region the metrics of this graph should be taken from. Default: - Current region
        :param title: Title for the graph. Default: - None
        :param width: Width of the widget, in a grid of 24 units wide. Default: 6
        :param end: The end of the time range to use for each widget independently from those of the dashboard. If you specify a value for end, you must also specify a value for start. Specify an absolute time in the ISO 8601 format. For example, 2018-12-17T06:00:00.000Z. Default: When the dashboard loads, the end date will be the current time.
        :param full_precision: Whether to show as many digits as can fit, before rounding. Default: false
        :param layout: Table layout. Default: - TableLayout.HORIZONTAL
        :param live_data: Whether the graph should show live data. Default: false
        :param metrics: Metrics to display in the table. Default: - No metrics
        :param period: The default period for all metrics in this widget. The period is the length of time represented by one data point on the graph. This default can be overridden within each metric definition. Default: cdk.Duration.seconds(300)
        :param set_period_to_time_range: Whether to show the value from the entire time range. Only applicable for Bar and Pie charts. If false, values will be from the most recent period of your chosen time range; if true, shows the value from the entire time range. Default: false
        :param show_units_in_label: Show the metrics units in the label column. Default: - false
        :param start: The start of the time range to use for each widget independently from those of the dashboard. You can specify start without specifying end to specify a relative time range that ends with the current time. In this case, the value of start must begin with -P, and you can use M, H, D, W and M as abbreviations for minutes, hours, days, weeks and months. For example, -PT8H shows the last 8 hours and -P3M shows the last three months. You can also use start along with an end field, to specify an absolute time range. When specifying an absolute time range, use the ISO 8601 format. For example, 2018-12-17T06:00:00.000Z. Default: When the dashboard loads, the start time will be the default time range.
        :param statistic: The default statistic to be displayed for each metric. This default can be overridden within the definition of each individual metric Default: - The statistic for each metric is used
        :param summary: Properties for displaying summary columns. Default: - no summary columns are shown
        :param thresholds: Thresholds for highlighting table cells. Default: - No thresholds

        :exampleMetadata: infused

        Example::

            # dashboard: cloudwatch.Dashboard
            
            
            dashboard.add_widgets(cloudwatch.TableWidget(
                # ...
            
                layout=cloudwatch.TableLayout.VERTICAL
            ))
        '''
        if isinstance(summary, dict):
            summary = TableSummaryProps(**summary)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03726ba90bb01c2a1340af4f73005fffe1b8288cff57d77f31d745d629defb8b)
            check_type(argname="argument height", value=height, expected_type=type_hints["height"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument title", value=title, expected_type=type_hints["title"])
            check_type(argname="argument width", value=width, expected_type=type_hints["width"])
            check_type(argname="argument end", value=end, expected_type=type_hints["end"])
            check_type(argname="argument full_precision", value=full_precision, expected_type=type_hints["full_precision"])
            check_type(argname="argument layout", value=layout, expected_type=type_hints["layout"])
            check_type(argname="argument live_data", value=live_data, expected_type=type_hints["live_data"])
            check_type(argname="argument metrics", value=metrics, expected_type=type_hints["metrics"])
            check_type(argname="argument period", value=period, expected_type=type_hints["period"])
            check_type(argname="argument set_period_to_time_range", value=set_period_to_time_range, expected_type=type_hints["set_period_to_time_range"])
            check_type(argname="argument show_units_in_label", value=show_units_in_label, expected_type=type_hints["show_units_in_label"])
            check_type(argname="argument start", value=start, expected_type=type_hints["start"])
            check_type(argname="argument statistic", value=statistic, expected_type=type_hints["statistic"])
            check_type(argname="argument summary", value=summary, expected_type=type_hints["summary"])
            check_type(argname="argument thresholds", value=thresholds, expected_type=type_hints["thresholds"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if height is not None:
            self._values["height"] = height
        if region is not None:
            self._values["region"] = region
        if title is not None:
            self._values["title"] = title
        if width is not None:
            self._values["width"] = width
        if end is not None:
            self._values["end"] = end
        if full_precision is not None:
            self._values["full_precision"] = full_precision
        if layout is not None:
            self._values["layout"] = layout
        if live_data is not None:
            self._values["live_data"] = live_data
        if metrics is not None:
            self._values["metrics"] = metrics
        if period is not None:
            self._values["period"] = period
        if set_period_to_time_range is not None:
            self._values["set_period_to_time_range"] = set_period_to_time_range
        if show_units_in_label is not None:
            self._values["show_units_in_label"] = show_units_in_label
        if start is not None:
            self._values["start"] = start
        if statistic is not None:
            self._values["statistic"] = statistic
        if summary is not None:
            self._values["summary"] = summary
        if thresholds is not None:
            self._values["thresholds"] = thresholds

    @builtins.property
    def height(self) -> typing.Optional[jsii.Number]:
        '''Height of the widget.

        :default:

        - 6 for Alarm and Graph widgets.
        3 for single value widgets where most recent value of a metric is displayed.
        '''
        result = self._values.get("height")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''The region the metrics of this graph should be taken from.

        :default: - Current region
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def title(self) -> typing.Optional[builtins.str]:
        '''Title for the graph.

        :default: - None
        '''
        result = self._values.get("title")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def width(self) -> typing.Optional[jsii.Number]:
        '''Width of the widget, in a grid of 24 units wide.

        :default: 6
        '''
        result = self._values.get("width")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def end(self) -> typing.Optional[builtins.str]:
        '''The end of the time range to use for each widget independently from those of the dashboard.

        If you specify a value for end, you must also specify a value for start.
        Specify an absolute time in the ISO 8601 format. For example, 2018-12-17T06:00:00.000Z.

        :default: When the dashboard loads, the end date will be the current time.
        '''
        result = self._values.get("end")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def full_precision(self) -> typing.Optional[builtins.bool]:
        '''Whether to show as many digits as can fit, before rounding.

        :default: false
        '''
        result = self._values.get("full_precision")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def layout(self) -> typing.Optional[TableLayout]:
        '''Table layout.

        :default: - TableLayout.HORIZONTAL
        '''
        result = self._values.get("layout")
        return typing.cast(typing.Optional[TableLayout], result)

    @builtins.property
    def live_data(self) -> typing.Optional[builtins.bool]:
        '''Whether the graph should show live data.

        :default: false
        '''
        result = self._values.get("live_data")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def metrics(self) -> typing.Optional[typing.List[IMetric]]:
        '''Metrics to display in the table.

        :default: - No metrics
        '''
        result = self._values.get("metrics")
        return typing.cast(typing.Optional[typing.List[IMetric]], result)

    @builtins.property
    def period(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The default period for all metrics in this widget.

        The period is the length of time represented by one data point on the graph.
        This default can be overridden within each metric definition.

        :default: cdk.Duration.seconds(300)
        '''
        result = self._values.get("period")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def set_period_to_time_range(self) -> typing.Optional[builtins.bool]:
        '''Whether to show the value from the entire time range. Only applicable for Bar and Pie charts.

        If false, values will be from the most recent period of your chosen time range;
        if true, shows the value from the entire time range.

        :default: false
        '''
        result = self._values.get("set_period_to_time_range")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def show_units_in_label(self) -> typing.Optional[builtins.bool]:
        '''Show the metrics units in the label column.

        :default: - false
        '''
        result = self._values.get("show_units_in_label")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def start(self) -> typing.Optional[builtins.str]:
        '''The start of the time range to use for each widget independently from those of the dashboard.

        You can specify start without specifying end to specify a relative time range that ends with the current time.
        In this case, the value of start must begin with -P, and you can use M, H, D, W and M as abbreviations for
        minutes, hours, days, weeks and months. For example, -PT8H shows the last 8 hours and -P3M shows the last three months.
        You can also use start along with an end field, to specify an absolute time range.
        When specifying an absolute time range, use the ISO 8601 format. For example, 2018-12-17T06:00:00.000Z.

        :default: When the dashboard loads, the start time will be the default time range.
        '''
        result = self._values.get("start")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def statistic(self) -> typing.Optional[builtins.str]:
        '''The default statistic to be displayed for each metric.

        This default can be overridden within the definition of each individual metric

        :default: - The statistic for each metric is used
        '''
        result = self._values.get("statistic")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def summary(self) -> typing.Optional[TableSummaryProps]:
        '''Properties for displaying summary columns.

        :default: - no summary columns are shown
        '''
        result = self._values.get("summary")
        return typing.cast(typing.Optional[TableSummaryProps], result)

    @builtins.property
    def thresholds(self) -> typing.Optional[typing.List[TableThreshold]]:
        '''Thresholds for highlighting table cells.

        :default: - No thresholds
        '''
        result = self._values.get("thresholds")
        return typing.cast(typing.Optional[typing.List[TableThreshold]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TableWidgetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_cloudwatch.TextWidgetBackground")
class TextWidgetBackground(enum.Enum):
    '''Background types available.

    :exampleMetadata: infused

    Example::

        # dashboard: cloudwatch.Dashboard
        
        
        dashboard.add_widgets(cloudwatch.TextWidget(
            markdown="# Key Performance Indicators",
            background=cloudwatch.TextWidgetBackground.TRANSPARENT
        ))
    '''

    SOLID = "SOLID"
    '''Solid background.'''
    TRANSPARENT = "TRANSPARENT"
    '''Transparent background.'''


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudwatch.TextWidgetProps",
    jsii_struct_bases=[],
    name_mapping={
        "markdown": "markdown",
        "background": "background",
        "height": "height",
        "width": "width",
    },
)
class TextWidgetProps:
    def __init__(
        self,
        *,
        markdown: builtins.str,
        background: typing.Optional[TextWidgetBackground] = None,
        height: typing.Optional[jsii.Number] = None,
        width: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Properties for a Text widget.

        :param markdown: The text to display, in MarkDown format.
        :param background: Background for the widget. Default: solid
        :param height: Height of the widget. Default: 2
        :param width: Width of the widget, in a grid of 24 units wide. Default: 6

        :exampleMetadata: infused

        Example::

            # dashboard: cloudwatch.Dashboard
            
            
            dashboard.add_widgets(cloudwatch.TextWidget(
                markdown="# Key Performance Indicators"
            ))
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c678c9d6bdc1a1e852f5260a40406f2e09cfc10b899093e99e66b9998d086d5e)
            check_type(argname="argument markdown", value=markdown, expected_type=type_hints["markdown"])
            check_type(argname="argument background", value=background, expected_type=type_hints["background"])
            check_type(argname="argument height", value=height, expected_type=type_hints["height"])
            check_type(argname="argument width", value=width, expected_type=type_hints["width"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "markdown": markdown,
        }
        if background is not None:
            self._values["background"] = background
        if height is not None:
            self._values["height"] = height
        if width is not None:
            self._values["width"] = width

    @builtins.property
    def markdown(self) -> builtins.str:
        '''The text to display, in MarkDown format.'''
        result = self._values.get("markdown")
        assert result is not None, "Required property 'markdown' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def background(self) -> typing.Optional[TextWidgetBackground]:
        '''Background for the widget.

        :default: solid
        '''
        result = self._values.get("background")
        return typing.cast(typing.Optional[TextWidgetBackground], result)

    @builtins.property
    def height(self) -> typing.Optional[jsii.Number]:
        '''Height of the widget.

        :default: 2
        '''
        result = self._values.get("height")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def width(self) -> typing.Optional[jsii.Number]:
        '''Width of the widget, in a grid of 24 units wide.

        :default: 6
        '''
        result = self._values.get("width")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TextWidgetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_cloudwatch.TreatMissingData")
class TreatMissingData(enum.Enum):
    '''Specify how missing data points are treated during alarm evaluation.

    :exampleMetadata: infused

    Example::

        import aws_cdk as cdk
        import aws_cdk.aws_cloudwatch as cloudwatch
        
        
        fn = lambda_.Function(self, "MyFunction",
            runtime=lambda_.Runtime.NODEJS_18_X,
            handler="index.handler",
            code=lambda_.Code.from_asset(path.join(__dirname, "lambda-handler")),
            timeout=Duration.minutes(5)
        )
        
        if fn.timeout:
            cloudwatch.Alarm(self, "MyAlarm",
                metric=fn.metric_duration().with(
                    statistic="Maximum"
                ),
                evaluation_periods=1,
                datapoints_to_alarm=1,
                threshold=fn.timeout.to_milliseconds(),
                treat_missing_data=cloudwatch.TreatMissingData.IGNORE,
                alarm_name="My Lambda Timeout"
            )
    '''

    BREACHING = "BREACHING"
    '''Missing data points are treated as breaching the threshold.'''
    NOT_BREACHING = "NOT_BREACHING"
    '''Missing data points are treated as being within the threshold.'''
    IGNORE = "IGNORE"
    '''The current alarm state is maintained.'''
    MISSING = "MISSING"
    '''The alarm does not consider missing data points when evaluating whether to change state.'''


@jsii.enum(jsii_type="aws-cdk-lib.aws_cloudwatch.Unit")
class Unit(enum.Enum):
    '''Unit for metric.

    :exampleMetadata: infused

    Example::

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
    '''

    SECONDS = "SECONDS"
    '''Seconds.'''
    MICROSECONDS = "MICROSECONDS"
    '''Microseconds.'''
    MILLISECONDS = "MILLISECONDS"
    '''Milliseconds.'''
    BYTES = "BYTES"
    '''Bytes.'''
    KILOBYTES = "KILOBYTES"
    '''Kilobytes.'''
    MEGABYTES = "MEGABYTES"
    '''Megabytes.'''
    GIGABYTES = "GIGABYTES"
    '''Gigabytes.'''
    TERABYTES = "TERABYTES"
    '''Terabytes.'''
    BITS = "BITS"
    '''Bits.'''
    KILOBITS = "KILOBITS"
    '''Kilobits.'''
    MEGABITS = "MEGABITS"
    '''Megabits.'''
    GIGABITS = "GIGABITS"
    '''Gigabits.'''
    TERABITS = "TERABITS"
    '''Terabits.'''
    PERCENT = "PERCENT"
    '''Percent.'''
    COUNT = "COUNT"
    '''Count.'''
    BYTES_PER_SECOND = "BYTES_PER_SECOND"
    '''Bytes/second (B/s).'''
    KILOBYTES_PER_SECOND = "KILOBYTES_PER_SECOND"
    '''Kilobytes/second (kB/s).'''
    MEGABYTES_PER_SECOND = "MEGABYTES_PER_SECOND"
    '''Megabytes/second (MB/s).'''
    GIGABYTES_PER_SECOND = "GIGABYTES_PER_SECOND"
    '''Gigabytes/second (GB/s).'''
    TERABYTES_PER_SECOND = "TERABYTES_PER_SECOND"
    '''Terabytes/second (TB/s).'''
    BITS_PER_SECOND = "BITS_PER_SECOND"
    '''Bits/second (b/s).'''
    KILOBITS_PER_SECOND = "KILOBITS_PER_SECOND"
    '''Kilobits/second (kb/s).'''
    MEGABITS_PER_SECOND = "MEGABITS_PER_SECOND"
    '''Megabits/second (Mb/s).'''
    GIGABITS_PER_SECOND = "GIGABITS_PER_SECOND"
    '''Gigabits/second (Gb/s).'''
    TERABITS_PER_SECOND = "TERABITS_PER_SECOND"
    '''Terabits/second (Tb/s).'''
    COUNT_PER_SECOND = "COUNT_PER_SECOND"
    '''Count/second.'''
    NONE = "NONE"
    '''None.'''


class Values(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="aws-cdk-lib.aws_cloudwatch.Values",
):
    '''A class for providing values for use with {@link VariableInputType.SELECT} and {@link VariableInputType.RADIO} dashboard variables.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_cloudwatch as cw
        
        
        dashboard = cw.Dashboard(self, "Dash",
            default_interval=Duration.days(7),
            variables=[cw.DashboardVariable(
                id="region",
                type=cw.VariableType.PROPERTY,
                label="Region",
                input_type=cw.VariableInputType.RADIO,
                value="region",
                values=cw.Values.from_values(cw.VariableValue(label="IAD", value="us-east-1"), label="DUB", value="us-west-2"),
                default_value=cw.DefaultValue.value("us-east-1"),
                visible=True
            )]
        )
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="fromSearch")
    @builtins.classmethod
    def from_search(
        cls,
        expression: builtins.str,
        populate_from: builtins.str,
    ) -> "Values":
        '''Create values from a search expression.

        :param expression: search expression that specifies a namespace, dimension name(s) and a metric name. For example ``{AWS/EC2,InstanceId} MetricName=\\"CPUUtilization\\"``
        :param populate_from: dimension the dimension name, that the search expression retrieves, whose values will be used to populate the values to choose from. For example ``InstanceId``
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__afe23853ba6c48e47b97d468ea15f87c9bfe3b880732f11d19570ed0895f18ca)
            check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
            check_type(argname="argument populate_from", value=populate_from, expected_type=type_hints["populate_from"])
        return typing.cast("Values", jsii.sinvoke(cls, "fromSearch", [expression, populate_from]))

    @jsii.member(jsii_name="fromSearchComponents")
    @builtins.classmethod
    def from_search_components(
        cls,
        *,
        dimensions: typing.Sequence[builtins.str],
        metric_name: builtins.str,
        namespace: builtins.str,
        populate_from: builtins.str,
    ) -> "Values":
        '''Create values from the components of search expression.

        :param dimensions: The list of dimensions to be used in the search expression.
        :param metric_name: The metric name to be used in the search expression.
        :param namespace: The namespace to be used in the search expression.
        :param populate_from: The dimension name, that the search expression retrieves, whose values will be used to populate the values to choose from.
        '''
        components = SearchComponents(
            dimensions=dimensions,
            metric_name=metric_name,
            namespace=namespace,
            populate_from=populate_from,
        )

        return typing.cast("Values", jsii.sinvoke(cls, "fromSearchComponents", [components]))

    @jsii.member(jsii_name="fromValues")
    @builtins.classmethod
    def from_values(cls, *values: "VariableValue") -> "Values":
        '''Create values from an array of possible variable values.

        :param values: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad2d8863dfb0f396c5d69f43fdc7137d8386cc972baa88ad212df48bbc5c3e6c)
            check_type(argname="argument values", value=values, expected_type=typing.Tuple[type_hints["values"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast("Values", jsii.sinvoke(cls, "fromValues", [*values]))

    @jsii.member(jsii_name="toJson")
    @abc.abstractmethod
    def to_json(self) -> typing.Any:
        ...


class _ValuesProxy(Values):
    @jsii.member(jsii_name="toJson")
    def to_json(self) -> typing.Any:
        return typing.cast(typing.Any, jsii.invoke(self, "toJson", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, Values).__jsii_proxy_class__ = lambda : _ValuesProxy


@jsii.enum(jsii_type="aws-cdk-lib.aws_cloudwatch.VariableInputType")
class VariableInputType(enum.Enum):
    '''
    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_cloudwatch as cw
        
        
        dashboard = cw.Dashboard(self, "Dash",
            default_interval=Duration.days(7),
            variables=[cw.DashboardVariable(
                id="functionName",
                type=cw.VariableType.PATTERN,
                label="Function",
                input_type=cw.VariableInputType.RADIO,
                value="originalFuncNameInDashboard",
                # equivalent to cw.Values.fromSearch('{AWS/Lambda,FunctionName} MetricName=\"Duration\"', 'FunctionName')
                values=cw.Values.from_search_components(
                    namespace="AWS/Lambda",
                    dimensions=["FunctionName"],
                    metric_name="Duration",
                    populate_from="FunctionName"
                ),
                default_value=cw.DefaultValue.FIRST,
                visible=True
            )]
        )
    '''

    INPUT = "INPUT"
    '''Freeform text input box.'''
    RADIO = "RADIO"
    '''A dropdown of pre-defined values, or values filled in from a metric search query.'''
    SELECT = "SELECT"
    '''A set of pre-defined radio buttons, which can also be defined from a metric search query.'''


@jsii.enum(jsii_type="aws-cdk-lib.aws_cloudwatch.VariableType")
class VariableType(enum.Enum):
    '''
    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_cloudwatch as cw
        
        
        dashboard = cw.Dashboard(self, "Dash",
            default_interval=Duration.days(7),
            variables=[cw.DashboardVariable(
                id="functionName",
                type=cw.VariableType.PATTERN,
                label="Function",
                input_type=cw.VariableInputType.RADIO,
                value="originalFuncNameInDashboard",
                # equivalent to cw.Values.fromSearch('{AWS/Lambda,FunctionName} MetricName=\"Duration\"', 'FunctionName')
                values=cw.Values.from_search_components(
                    namespace="AWS/Lambda",
                    dimensions=["FunctionName"],
                    metric_name="Duration",
                    populate_from="FunctionName"
                ),
                default_value=cw.DefaultValue.FIRST,
                visible=True
            )]
        )
    '''

    PROPERTY = "PROPERTY"
    '''A property variable changes the values of all instances of a property in the list of widgets in the dashboard.'''
    PATTERN = "PATTERN"
    '''A pattern variable is one that changes a regex pattern across the dashboard JSON.'''


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudwatch.VariableValue",
    jsii_struct_bases=[],
    name_mapping={"value": "value", "label": "label"},
)
class VariableValue:
    def __init__(
        self,
        *,
        value: builtins.str,
        label: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param value: Value of the selected item.
        :param label: Optional label for the selected item. Default: - the variable's value

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_cloudwatch as cw
            
            
            dashboard = cw.Dashboard(self, "Dash",
                default_interval=Duration.days(7),
                variables=[cw.DashboardVariable(
                    id="region",
                    type=cw.VariableType.PROPERTY,
                    label="Region",
                    input_type=cw.VariableInputType.RADIO,
                    value="region",
                    values=cw.Values.from_values(cw.VariableValue(label="IAD", value="us-east-1"), label="DUB", value="us-west-2"),
                    default_value=cw.DefaultValue.value("us-east-1"),
                    visible=True
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03c9a6d1a1a0197c51468b97744230720e131da2f17bd50bfcfa9f7a3b4092cb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            check_type(argname="argument label", value=label, expected_type=type_hints["label"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "value": value,
        }
        if label is not None:
            self._values["label"] = label

    @builtins.property
    def value(self) -> builtins.str:
        '''Value of the selected item.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def label(self) -> typing.Optional[builtins.str]:
        '''Optional label for the selected item.

        :default: - the variable's value
        '''
        result = self._values.get("label")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VariableValue(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudwatch.VerticalAnnotation",
    jsii_struct_bases=[],
    name_mapping={
        "date": "date",
        "color": "color",
        "fill": "fill",
        "label": "label",
        "visible": "visible",
    },
)
class VerticalAnnotation:
    def __init__(
        self,
        *,
        date: builtins.str,
        color: typing.Optional[builtins.str] = None,
        fill: typing.Optional["VerticalShading"] = None,
        label: typing.Optional[builtins.str] = None,
        visible: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Vertical annotation to be added to a graph.

        :param date: The date and time (in ISO 8601 format) in the graph where the vertical annotation line is to appear.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to be used for the annotation. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param fill: Add shading before or after the annotation. Default: No shading
        :param label: Label for the annotation. Default: - No label
        :param visible: Whether the annotation is visible. Default: true

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cloudwatch as cloudwatch
            
            vertical_annotation = cloudwatch.VerticalAnnotation(
                date="date",
            
                # the properties below are optional
                color="color",
                fill=cloudwatch.VerticalShading.NONE,
                label="label",
                visible=False
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c903f8a4aafff9c3e6b2539c8372df8551aba4035bb4187c0e0930b0ee60ff00)
            check_type(argname="argument date", value=date, expected_type=type_hints["date"])
            check_type(argname="argument color", value=color, expected_type=type_hints["color"])
            check_type(argname="argument fill", value=fill, expected_type=type_hints["fill"])
            check_type(argname="argument label", value=label, expected_type=type_hints["label"])
            check_type(argname="argument visible", value=visible, expected_type=type_hints["visible"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "date": date,
        }
        if color is not None:
            self._values["color"] = color
        if fill is not None:
            self._values["fill"] = fill
        if label is not None:
            self._values["label"] = label
        if visible is not None:
            self._values["visible"] = visible

    @builtins.property
    def date(self) -> builtins.str:
        '''The date and time (in ISO 8601 format) in the graph where the vertical annotation line is to appear.'''
        result = self._values.get("date")
        assert result is not None, "Required property 'date' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def color(self) -> typing.Optional[builtins.str]:
        '''The hex color code, prefixed with '#' (e.g. '#00ff00'), to be used for the annotation. The ``Color`` class has a set of standard colors that can be used here.

        :default: - Automatic color
        '''
        result = self._values.get("color")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def fill(self) -> typing.Optional["VerticalShading"]:
        '''Add shading before or after the annotation.

        :default: No shading
        '''
        result = self._values.get("fill")
        return typing.cast(typing.Optional["VerticalShading"], result)

    @builtins.property
    def label(self) -> typing.Optional[builtins.str]:
        '''Label for the annotation.

        :default: - No label
        '''
        result = self._values.get("label")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def visible(self) -> typing.Optional[builtins.bool]:
        '''Whether the annotation is visible.

        :default: true
        '''
        result = self._values.get("visible")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VerticalAnnotation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_cloudwatch.VerticalShading")
class VerticalShading(enum.Enum):
    '''Fill shading options that will be used with a vertical annotation.'''

    NONE = "NONE"
    '''Don't add shading.'''
    BEFORE = "BEFORE"
    '''Add shading before the annotation.'''
    AFTER = "AFTER"
    '''Add shading after the annotation.'''


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudwatch.YAxisProps",
    jsii_struct_bases=[],
    name_mapping={
        "label": "label",
        "max": "max",
        "min": "min",
        "show_units": "showUnits",
    },
)
class YAxisProps:
    def __init__(
        self,
        *,
        label: typing.Optional[builtins.str] = None,
        max: typing.Optional[jsii.Number] = None,
        min: typing.Optional[jsii.Number] = None,
        show_units: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Properties for a Y-Axis.

        :param label: The label. Default: - No label
        :param max: The max value. Default: - No maximum value
        :param min: The min value. Default: 0
        :param show_units: Whether to show units. Default: true

        :exampleMetadata: infused

        Example::

            # dashboard: cloudwatch.Dashboard
            # error_alarm: cloudwatch.Alarm
            # gauge_metric: cloudwatch.Metric
            
            
            dashboard.add_widgets(cloudwatch.GaugeWidget(
                metrics=[gauge_metric],
                left_yAxis=cloudwatch.YAxisProps(
                    min=0,
                    max=1000
                )
            ))
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec63852e8e70001b1e7a1554d96ad9ddb32bcfee6e3c022b5ba672bf9259a3be)
            check_type(argname="argument label", value=label, expected_type=type_hints["label"])
            check_type(argname="argument max", value=max, expected_type=type_hints["max"])
            check_type(argname="argument min", value=min, expected_type=type_hints["min"])
            check_type(argname="argument show_units", value=show_units, expected_type=type_hints["show_units"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if label is not None:
            self._values["label"] = label
        if max is not None:
            self._values["max"] = max
        if min is not None:
            self._values["min"] = min
        if show_units is not None:
            self._values["show_units"] = show_units

    @builtins.property
    def label(self) -> typing.Optional[builtins.str]:
        '''The label.

        :default: - No label
        '''
        result = self._values.get("label")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max(self) -> typing.Optional[jsii.Number]:
        '''The max value.

        :default: - No maximum value
        '''
        result = self._values.get("max")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min(self) -> typing.Optional[jsii.Number]:
        '''The min value.

        :default: 0
        '''
        result = self._values.get("min")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def show_units(self) -> typing.Optional[builtins.bool]:
        '''Whether to show units.

        :default: true
        '''
        result = self._values.get("show_units")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "YAxisProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudwatch.AlarmProps",
    jsii_struct_bases=[CreateAlarmOptions],
    name_mapping={
        "evaluation_periods": "evaluationPeriods",
        "threshold": "threshold",
        "actions_enabled": "actionsEnabled",
        "alarm_description": "alarmDescription",
        "alarm_name": "alarmName",
        "comparison_operator": "comparisonOperator",
        "datapoints_to_alarm": "datapointsToAlarm",
        "evaluate_low_sample_count_percentile": "evaluateLowSampleCountPercentile",
        "treat_missing_data": "treatMissingData",
        "metric": "metric",
    },
)
class AlarmProps(CreateAlarmOptions):
    def __init__(
        self,
        *,
        evaluation_periods: jsii.Number,
        threshold: jsii.Number,
        actions_enabled: typing.Optional[builtins.bool] = None,
        alarm_description: typing.Optional[builtins.str] = None,
        alarm_name: typing.Optional[builtins.str] = None,
        comparison_operator: typing.Optional[ComparisonOperator] = None,
        datapoints_to_alarm: typing.Optional[jsii.Number] = None,
        evaluate_low_sample_count_percentile: typing.Optional[builtins.str] = None,
        treat_missing_data: typing.Optional[TreatMissingData] = None,
        metric: IMetric,
    ) -> None:
        '''Properties for Alarms.

        :param evaluation_periods: The number of periods over which data is compared to the specified threshold.
        :param threshold: The value against which the specified statistic is compared.
        :param actions_enabled: Whether the actions for this alarm are enabled. Default: true
        :param alarm_description: Description for the alarm. Default: No description
        :param alarm_name: Name of the alarm. Default: Automatically generated name
        :param comparison_operator: Comparison to use to check if metric is breaching. Default: GreaterThanOrEqualToThreshold
        :param datapoints_to_alarm: The number of datapoints that must be breaching to trigger the alarm. This is used only if you are setting an "M out of N" alarm. In that case, this value is the M. For more information, see Evaluating an Alarm in the Amazon CloudWatch User Guide. Default: ``evaluationPeriods``
        :param evaluate_low_sample_count_percentile: Specifies whether to evaluate the data and potentially change the alarm state if there are too few data points to be statistically significant. Used only for alarms that are based on percentiles. Default: - Not configured.
        :param treat_missing_data: Sets how this alarm is to handle missing data points. Default: TreatMissingData.Missing
        :param metric: The metric to add the alarm on. Metric objects can be obtained from most resources, or you can construct custom Metric objects by instantiating one.

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_cloudwatch as cloudwatch
            
            # alias: lambda.Alias
            
            # or add alarms to an existing group
            # blue_green_alias: lambda.Alias
            
            alarm = cloudwatch.Alarm(self, "Errors",
                comparison_operator=cloudwatch.ComparisonOperator.GREATER_THAN_THRESHOLD,
                threshold=1,
                evaluation_periods=1,
                metric=alias.metric_errors()
            )
            deployment_group = codedeploy.LambdaDeploymentGroup(self, "BlueGreenDeployment",
                alias=alias,
                deployment_config=codedeploy.LambdaDeploymentConfig.LINEAR_10PERCENT_EVERY_1MINUTE,
                alarms=[alarm
                ]
            )
            deployment_group.add_alarm(cloudwatch.Alarm(self, "BlueGreenErrors",
                comparison_operator=cloudwatch.ComparisonOperator.GREATER_THAN_THRESHOLD,
                threshold=1,
                evaluation_periods=1,
                metric=blue_green_alias.metric_errors()
            ))
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2e7c873c118fbc1f6cf26e1bb5bd3d8549040c626a6450f2d686bb07b87266b)
            check_type(argname="argument evaluation_periods", value=evaluation_periods, expected_type=type_hints["evaluation_periods"])
            check_type(argname="argument threshold", value=threshold, expected_type=type_hints["threshold"])
            check_type(argname="argument actions_enabled", value=actions_enabled, expected_type=type_hints["actions_enabled"])
            check_type(argname="argument alarm_description", value=alarm_description, expected_type=type_hints["alarm_description"])
            check_type(argname="argument alarm_name", value=alarm_name, expected_type=type_hints["alarm_name"])
            check_type(argname="argument comparison_operator", value=comparison_operator, expected_type=type_hints["comparison_operator"])
            check_type(argname="argument datapoints_to_alarm", value=datapoints_to_alarm, expected_type=type_hints["datapoints_to_alarm"])
            check_type(argname="argument evaluate_low_sample_count_percentile", value=evaluate_low_sample_count_percentile, expected_type=type_hints["evaluate_low_sample_count_percentile"])
            check_type(argname="argument treat_missing_data", value=treat_missing_data, expected_type=type_hints["treat_missing_data"])
            check_type(argname="argument metric", value=metric, expected_type=type_hints["metric"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "evaluation_periods": evaluation_periods,
            "threshold": threshold,
            "metric": metric,
        }
        if actions_enabled is not None:
            self._values["actions_enabled"] = actions_enabled
        if alarm_description is not None:
            self._values["alarm_description"] = alarm_description
        if alarm_name is not None:
            self._values["alarm_name"] = alarm_name
        if comparison_operator is not None:
            self._values["comparison_operator"] = comparison_operator
        if datapoints_to_alarm is not None:
            self._values["datapoints_to_alarm"] = datapoints_to_alarm
        if evaluate_low_sample_count_percentile is not None:
            self._values["evaluate_low_sample_count_percentile"] = evaluate_low_sample_count_percentile
        if treat_missing_data is not None:
            self._values["treat_missing_data"] = treat_missing_data

    @builtins.property
    def evaluation_periods(self) -> jsii.Number:
        '''The number of periods over which data is compared to the specified threshold.'''
        result = self._values.get("evaluation_periods")
        assert result is not None, "Required property 'evaluation_periods' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def threshold(self) -> jsii.Number:
        '''The value against which the specified statistic is compared.'''
        result = self._values.get("threshold")
        assert result is not None, "Required property 'threshold' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def actions_enabled(self) -> typing.Optional[builtins.bool]:
        '''Whether the actions for this alarm are enabled.

        :default: true
        '''
        result = self._values.get("actions_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def alarm_description(self) -> typing.Optional[builtins.str]:
        '''Description for the alarm.

        :default: No description
        '''
        result = self._values.get("alarm_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def alarm_name(self) -> typing.Optional[builtins.str]:
        '''Name of the alarm.

        :default: Automatically generated name
        '''
        result = self._values.get("alarm_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def comparison_operator(self) -> typing.Optional[ComparisonOperator]:
        '''Comparison to use to check if metric is breaching.

        :default: GreaterThanOrEqualToThreshold
        '''
        result = self._values.get("comparison_operator")
        return typing.cast(typing.Optional[ComparisonOperator], result)

    @builtins.property
    def datapoints_to_alarm(self) -> typing.Optional[jsii.Number]:
        '''The number of datapoints that must be breaching to trigger the alarm.

        This is used only if you are setting an "M
        out of N" alarm. In that case, this value is the M. For more information, see Evaluating an Alarm in the Amazon
        CloudWatch User Guide.

        :default: ``evaluationPeriods``

        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#alarm-evaluation
        '''
        result = self._values.get("datapoints_to_alarm")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def evaluate_low_sample_count_percentile(self) -> typing.Optional[builtins.str]:
        '''Specifies whether to evaluate the data and potentially change the alarm state if there are too few data points to be statistically significant.

        Used only for alarms that are based on percentiles.

        :default: - Not configured.
        '''
        result = self._values.get("evaluate_low_sample_count_percentile")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def treat_missing_data(self) -> typing.Optional[TreatMissingData]:
        '''Sets how this alarm is to handle missing data points.

        :default: TreatMissingData.Missing
        '''
        result = self._values.get("treat_missing_data")
        return typing.cast(typing.Optional[TreatMissingData], result)

    @builtins.property
    def metric(self) -> IMetric:
        '''The metric to add the alarm on.

        Metric objects can be obtained from most resources, or you can construct
        custom Metric objects by instantiating one.
        '''
        result = self._values.get("metric")
        assert result is not None, "Required property 'metric' is missing"
        return typing.cast(IMetric, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AlarmProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudwatch.AlarmWidgetProps",
    jsii_struct_bases=[MetricWidgetProps],
    name_mapping={
        "height": "height",
        "region": "region",
        "title": "title",
        "width": "width",
        "alarm": "alarm",
        "left_y_axis": "leftYAxis",
    },
)
class AlarmWidgetProps(MetricWidgetProps):
    def __init__(
        self,
        *,
        height: typing.Optional[jsii.Number] = None,
        region: typing.Optional[builtins.str] = None,
        title: typing.Optional[builtins.str] = None,
        width: typing.Optional[jsii.Number] = None,
        alarm: "IAlarm",
        left_y_axis: typing.Optional[typing.Union[YAxisProps, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Properties for an AlarmWidget.

        :param height: Height of the widget. Default: - 6 for Alarm and Graph widgets. 3 for single value widgets where most recent value of a metric is displayed.
        :param region: The region the metrics of this graph should be taken from. Default: - Current region
        :param title: Title for the graph. Default: - None
        :param width: Width of the widget, in a grid of 24 units wide. Default: 6
        :param alarm: The alarm to show.
        :param left_y_axis: Left Y axis. Default: - No minimum or maximum values for the left Y-axis

        :exampleMetadata: infused

        Example::

            # dashboard: cloudwatch.Dashboard
            # error_alarm: cloudwatch.Alarm
            
            
            dashboard.add_widgets(cloudwatch.AlarmWidget(
                title="Errors",
                alarm=error_alarm
            ))
        '''
        if isinstance(left_y_axis, dict):
            left_y_axis = YAxisProps(**left_y_axis)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b6bef2cc64a78bffd68dc95a764829a6c125294deaebcd42b56c493541573d5)
            check_type(argname="argument height", value=height, expected_type=type_hints["height"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument title", value=title, expected_type=type_hints["title"])
            check_type(argname="argument width", value=width, expected_type=type_hints["width"])
            check_type(argname="argument alarm", value=alarm, expected_type=type_hints["alarm"])
            check_type(argname="argument left_y_axis", value=left_y_axis, expected_type=type_hints["left_y_axis"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "alarm": alarm,
        }
        if height is not None:
            self._values["height"] = height
        if region is not None:
            self._values["region"] = region
        if title is not None:
            self._values["title"] = title
        if width is not None:
            self._values["width"] = width
        if left_y_axis is not None:
            self._values["left_y_axis"] = left_y_axis

    @builtins.property
    def height(self) -> typing.Optional[jsii.Number]:
        '''Height of the widget.

        :default:

        - 6 for Alarm and Graph widgets.
        3 for single value widgets where most recent value of a metric is displayed.
        '''
        result = self._values.get("height")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''The region the metrics of this graph should be taken from.

        :default: - Current region
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def title(self) -> typing.Optional[builtins.str]:
        '''Title for the graph.

        :default: - None
        '''
        result = self._values.get("title")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def width(self) -> typing.Optional[jsii.Number]:
        '''Width of the widget, in a grid of 24 units wide.

        :default: 6
        '''
        result = self._values.get("width")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def alarm(self) -> "IAlarm":
        '''The alarm to show.'''
        result = self._values.get("alarm")
        assert result is not None, "Required property 'alarm' is missing"
        return typing.cast("IAlarm", result)

    @builtins.property
    def left_y_axis(self) -> typing.Optional[YAxisProps]:
        '''Left Y axis.

        :default: - No minimum or maximum values for the left Y-axis
        '''
        result = self._values.get("left_y_axis")
        return typing.cast(typing.Optional[YAxisProps], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AlarmWidgetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IWidget)
class Column(metaclass=jsii.JSIIMeta, jsii_type="aws-cdk-lib.aws_cloudwatch.Column"):
    '''A widget that contains other widgets in a vertical column.

    Widgets will be laid out next to each other

    :exampleMetadata: infused

    Example::

        # widget_a: cloudwatch.IWidget
        # widget_b: cloudwatch.IWidget
        
        
        cloudwatch.Column(widget_a, widget_b)
    '''

    def __init__(self, *widgets: IWidget) -> None:
        '''
        :param widgets: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76ce8e89badc991e6248d5096f1d0b7ed5c9b4e588f4383e932e8f87c07043c6)
            check_type(argname="argument widgets", value=widgets, expected_type=typing.Tuple[type_hints["widgets"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        jsii.create(self.__class__, self, [*widgets])

    @jsii.member(jsii_name="addWidget")
    def add_widget(self, w: IWidget) -> None:
        '''Add the widget to this container.

        :param w: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e7a63a93df283f275f6e4f6eea63f6665322c9a990c8c8aa9db71dd89fe730e)
            check_type(argname="argument w", value=w, expected_type=type_hints["w"])
        return typing.cast(None, jsii.invoke(self, "addWidget", [w]))

    @jsii.member(jsii_name="position")
    def position(self, x: jsii.Number, y: jsii.Number) -> None:
        '''Place the widget at a given position.

        :param x: -
        :param y: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be386baa88e2f34ab4e89e312e9a044e57596f584e0dc58e3e0de3089771cbf5)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
            check_type(argname="argument y", value=y, expected_type=type_hints["y"])
        return typing.cast(None, jsii.invoke(self, "position", [x, y]))

    @jsii.member(jsii_name="toJson")
    def to_json(self) -> typing.List[typing.Any]:
        '''Return the widget JSON for use in the dashboard.'''
        return typing.cast(typing.List[typing.Any], jsii.invoke(self, "toJson", []))

    @builtins.property
    @jsii.member(jsii_name="height")
    def height(self) -> jsii.Number:
        '''The amount of vertical grid units the widget will take up.'''
        return typing.cast(jsii.Number, jsii.get(self, "height"))

    @builtins.property
    @jsii.member(jsii_name="widgets")
    def widgets(self) -> typing.List[IWidget]:
        '''List of contained widgets.'''
        return typing.cast(typing.List[IWidget], jsii.get(self, "widgets"))

    @builtins.property
    @jsii.member(jsii_name="width")
    def width(self) -> jsii.Number:
        '''The amount of horizontal grid units the widget will take up.'''
        return typing.cast(jsii.Number, jsii.get(self, "width"))


@jsii.implements(IWidget)
class ConcreteWidget(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="aws-cdk-lib.aws_cloudwatch.ConcreteWidget",
):
    '''A real CloudWatch widget that has its own fixed size and remembers its position.

    This is in contrast to other widgets which exist for layout purposes.
    '''

    def __init__(self, width: jsii.Number, height: jsii.Number) -> None:
        '''
        :param width: The amount of horizontal grid units the widget will take up.
        :param height: The amount of vertical grid units the widget will take up.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5472697255361cd3423eece6fc66536dcf7e58a80d3801bec6331d231c9e36d)
            check_type(argname="argument width", value=width, expected_type=type_hints["width"])
            check_type(argname="argument height", value=height, expected_type=type_hints["height"])
        jsii.create(self.__class__, self, [width, height])

    @jsii.member(jsii_name="copyMetricWarnings")
    def _copy_metric_warnings(self, *ms: IMetric) -> None:
        '''Copy the warnings from the given metric.

        :param ms: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5ae2d5f50f7532d79ca7e346e91f137e37e297127e588b21f681019986b1c55)
            check_type(argname="argument ms", value=ms, expected_type=typing.Tuple[type_hints["ms"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "copyMetricWarnings", [*ms]))

    @jsii.member(jsii_name="position")
    def position(self, x: jsii.Number, y: jsii.Number) -> None:
        '''Place the widget at a given position.

        :param x: -
        :param y: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e0f6387845c9d7953cfc1de766c2a56f8bb9fb94f5c273ed272288b546b4392)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
            check_type(argname="argument y", value=y, expected_type=type_hints["y"])
        return typing.cast(None, jsii.invoke(self, "position", [x, y]))

    @jsii.member(jsii_name="toJson")
    @abc.abstractmethod
    def to_json(self) -> typing.List[typing.Any]:
        '''Return the widget JSON for use in the dashboard.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="height")
    def height(self) -> jsii.Number:
        '''The amount of vertical grid units the widget will take up.'''
        return typing.cast(jsii.Number, jsii.get(self, "height"))

    @builtins.property
    @jsii.member(jsii_name="width")
    def width(self) -> jsii.Number:
        '''The amount of horizontal grid units the widget will take up.'''
        return typing.cast(jsii.Number, jsii.get(self, "width"))

    @builtins.property
    @jsii.member(jsii_name="warnings")
    def warnings(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Any warnings that are produced as a result of putting together this widget.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "warnings"))

    @builtins.property
    @jsii.member(jsii_name="warningsV2")
    def warnings_v2(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Any warnings that are produced as a result of putting together this widget.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "warningsV2"))

    @builtins.property
    @jsii.member(jsii_name="x")
    def _x(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "x"))

    @_x.setter
    def _x(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6a944db25b0c1533973a41edef1a431615645e2f5fcbcc1e577c331d33bb0ff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "x", value)

    @builtins.property
    @jsii.member(jsii_name="y")
    def _y(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "y"))

    @_y.setter
    def _y(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81266f4e20969db506e61dedc6af36fce6fe0f75af699f49b5c6f11f9225bef2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "y", value)


class _ConcreteWidgetProxy(ConcreteWidget):
    @jsii.member(jsii_name="toJson")
    def to_json(self) -> typing.List[typing.Any]:
        '''Return the widget JSON for use in the dashboard.'''
        return typing.cast(typing.List[typing.Any], jsii.invoke(self, "toJson", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, ConcreteWidget).__jsii_proxy_class__ = lambda : _ConcreteWidgetProxy


class CustomWidget(
    ConcreteWidget,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudwatch.CustomWidget",
):
    '''A CustomWidget shows the result of a AWS lambda function.

    :exampleMetadata: infused

    Example::

        # dashboard: cloudwatch.Dashboard
        
        
        # Import or create a lambda function
        fn = lambda_.Function.from_function_arn(dashboard, "Function", "arn:aws:lambda:us-east-1:123456789012:function:MyFn")
        
        dashboard.add_widgets(cloudwatch.CustomWidget(
            function_arn=fn.function_arn,
            title="My lambda baked widget"
        ))
    '''

    def __init__(
        self,
        *,
        function_arn: builtins.str,
        title: builtins.str,
        height: typing.Optional[jsii.Number] = None,
        params: typing.Any = None,
        update_on_refresh: typing.Optional[builtins.bool] = None,
        update_on_resize: typing.Optional[builtins.bool] = None,
        update_on_time_range_change: typing.Optional[builtins.bool] = None,
        width: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param function_arn: The Arn of the AWS Lambda function that returns HTML or JSON that will be displayed in the widget.
        :param title: The title of the widget.
        :param height: Height of the widget. Default: - 6 for Alarm and Graph widgets. 3 for single value widgets where most recent value of a metric is displayed.
        :param params: Parameters passed to the lambda function. Default: - no parameters are passed to the lambda function
        :param update_on_refresh: Update the widget on refresh. Default: true
        :param update_on_resize: Update the widget on resize. Default: true
        :param update_on_time_range_change: Update the widget on time range change. Default: true
        :param width: Width of the widget, in a grid of 24 units wide. Default: 6
        '''
        props = CustomWidgetProps(
            function_arn=function_arn,
            title=title,
            height=height,
            params=params,
            update_on_refresh=update_on_refresh,
            update_on_resize=update_on_resize,
            update_on_time_range_change=update_on_time_range_change,
            width=width,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="toJson")
    def to_json(self) -> typing.List[typing.Any]:
        '''Return the widget JSON for use in the dashboard.'''
        return typing.cast(typing.List[typing.Any], jsii.invoke(self, "toJson", []))


@jsii.implements(IVariable)
class DashboardVariable(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudwatch.DashboardVariable",
):
    '''Dashboard Variable.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_cloudwatch as cw
        
        
        dashboard = cw.Dashboard(self, "Dash",
            default_interval=Duration.days(7),
            variables=[cw.DashboardVariable(
                id="functionName",
                type=cw.VariableType.PATTERN,
                label="Function",
                input_type=cw.VariableInputType.RADIO,
                value="originalFuncNameInDashboard",
                # equivalent to cw.Values.fromSearch('{AWS/Lambda,FunctionName} MetricName=\"Duration\"', 'FunctionName')
                values=cw.Values.from_search_components(
                    namespace="AWS/Lambda",
                    dimensions=["FunctionName"],
                    metric_name="Duration",
                    populate_from="FunctionName"
                ),
                default_value=cw.DefaultValue.FIRST,
                visible=True
            )]
        )
    '''

    def __init__(
        self,
        *,
        id: builtins.str,
        input_type: VariableInputType,
        type: VariableType,
        value: builtins.str,
        default_value: typing.Optional[DefaultValue] = None,
        label: typing.Optional[builtins.str] = None,
        values: typing.Optional[Values] = None,
        visible: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param id: Unique id.
        :param input_type: The way the variable value is selected.
        :param type: Type of the variable.
        :param value: Pattern or property value to replace.
        :param default_value: Optional default value. Default: - no default value is set
        :param label: Optional label in the toolbar. Default: - the variable's value
        :param values: Optional values (required for {@link VariableInputType.RADIO} and {@link VariableInputType.SELECT} dashboard variables). Default: - no values
        :param visible: Whether the variable is visible. Default: - true
        '''
        options = DashboardVariableOptions(
            id=id,
            input_type=input_type,
            type=type,
            value=value,
            default_value=default_value,
            label=label,
            values=values,
            visible=visible,
        )

        jsii.create(self.__class__, self, [options])

    @jsii.member(jsii_name="toJson")
    def to_json(self) -> typing.Any:
        '''Return the variable JSON for use in the dashboard.'''
        return typing.cast(typing.Any, jsii.invoke(self, "toJson", []))


class GaugeWidget(
    ConcreteWidget,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudwatch.GaugeWidget",
):
    '''A dashboard gauge widget that displays metrics.

    :exampleMetadata: infused

    Example::

        # dashboard: cloudwatch.Dashboard
        # error_alarm: cloudwatch.Alarm
        # gauge_metric: cloudwatch.Metric
        
        
        dashboard.add_widgets(cloudwatch.GaugeWidget(
            metrics=[gauge_metric],
            left_yAxis=cloudwatch.YAxisProps(
                min=0,
                max=1000
            )
        ))
    '''

    def __init__(
        self,
        *,
        annotations: typing.Optional[typing.Sequence[typing.Union[HorizontalAnnotation, typing.Dict[builtins.str, typing.Any]]]] = None,
        end: typing.Optional[builtins.str] = None,
        left_y_axis: typing.Optional[typing.Union[YAxisProps, typing.Dict[builtins.str, typing.Any]]] = None,
        legend_position: typing.Optional[LegendPosition] = None,
        live_data: typing.Optional[builtins.bool] = None,
        metrics: typing.Optional[typing.Sequence[IMetric]] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        set_period_to_time_range: typing.Optional[builtins.bool] = None,
        start: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        height: typing.Optional[jsii.Number] = None,
        region: typing.Optional[builtins.str] = None,
        title: typing.Optional[builtins.str] = None,
        width: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param annotations: Annotations for the left Y axis. Default: - No annotations
        :param end: The end of the time range to use for each widget independently from those of the dashboard. If you specify a value for end, you must also specify a value for start. Specify an absolute time in the ISO 8601 format. For example, 2018-12-17T06:00:00.000Z. Default: When the dashboard loads, the end date will be the current time.
        :param left_y_axis: Left Y axis. Default: - None
        :param legend_position: Position of the legend. Default: - bottom
        :param live_data: Whether the graph should show live data. Default: false
        :param metrics: Metrics to display on left Y axis. Default: - No metrics
        :param period: The default period for all metrics in this widget. The period is the length of time represented by one data point on the graph. This default can be overridden within each metric definition. Default: cdk.Duration.seconds(300)
        :param set_period_to_time_range: Whether to show the value from the entire time range. Only applicable for Bar and Pie charts. If false, values will be from the most recent period of your chosen time range; if true, shows the value from the entire time range. Default: false
        :param start: The start of the time range to use for each widget independently from those of the dashboard. You can specify start without specifying end to specify a relative time range that ends with the current time. In this case, the value of start must begin with -P, and you can use M, H, D, W and M as abbreviations for minutes, hours, days, weeks and months. For example, -PT8H shows the last 8 hours and -P3M shows the last three months. You can also use start along with an end field, to specify an absolute time range. When specifying an absolute time range, use the ISO 8601 format. For example, 2018-12-17T06:00:00.000Z. Default: When the dashboard loads, the start time will be the default time range.
        :param statistic: The default statistic to be displayed for each metric. This default can be overridden within the definition of each individual metric Default: - The statistic for each metric is used
        :param height: Height of the widget. Default: - 6 for Alarm and Graph widgets. 3 for single value widgets where most recent value of a metric is displayed.
        :param region: The region the metrics of this graph should be taken from. Default: - Current region
        :param title: Title for the graph. Default: - None
        :param width: Width of the widget, in a grid of 24 units wide. Default: 6
        '''
        props = GaugeWidgetProps(
            annotations=annotations,
            end=end,
            left_y_axis=left_y_axis,
            legend_position=legend_position,
            live_data=live_data,
            metrics=metrics,
            period=period,
            set_period_to_time_range=set_period_to_time_range,
            start=start,
            statistic=statistic,
            height=height,
            region=region,
            title=title,
            width=width,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="addMetric")
    def add_metric(self, metric: IMetric) -> None:
        '''Add another metric to the left Y axis of the GaugeWidget.

        :param metric: the metric to add.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11f194bd6989eaa4279174f388eb1c44a7faf424b684d189ffe90647dfd0eeb2)
            check_type(argname="argument metric", value=metric, expected_type=type_hints["metric"])
        return typing.cast(None, jsii.invoke(self, "addMetric", [metric]))

    @jsii.member(jsii_name="toJson")
    def to_json(self) -> typing.List[typing.Any]:
        '''Return the widget JSON for use in the dashboard.'''
        return typing.cast(typing.List[typing.Any], jsii.invoke(self, "toJson", []))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudwatch.GaugeWidgetProps",
    jsii_struct_bases=[MetricWidgetProps],
    name_mapping={
        "height": "height",
        "region": "region",
        "title": "title",
        "width": "width",
        "annotations": "annotations",
        "end": "end",
        "left_y_axis": "leftYAxis",
        "legend_position": "legendPosition",
        "live_data": "liveData",
        "metrics": "metrics",
        "period": "period",
        "set_period_to_time_range": "setPeriodToTimeRange",
        "start": "start",
        "statistic": "statistic",
    },
)
class GaugeWidgetProps(MetricWidgetProps):
    def __init__(
        self,
        *,
        height: typing.Optional[jsii.Number] = None,
        region: typing.Optional[builtins.str] = None,
        title: typing.Optional[builtins.str] = None,
        width: typing.Optional[jsii.Number] = None,
        annotations: typing.Optional[typing.Sequence[typing.Union[HorizontalAnnotation, typing.Dict[builtins.str, typing.Any]]]] = None,
        end: typing.Optional[builtins.str] = None,
        left_y_axis: typing.Optional[typing.Union[YAxisProps, typing.Dict[builtins.str, typing.Any]]] = None,
        legend_position: typing.Optional[LegendPosition] = None,
        live_data: typing.Optional[builtins.bool] = None,
        metrics: typing.Optional[typing.Sequence[IMetric]] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        set_period_to_time_range: typing.Optional[builtins.bool] = None,
        start: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for a GaugeWidget.

        :param height: Height of the widget. Default: - 6 for Alarm and Graph widgets. 3 for single value widgets where most recent value of a metric is displayed.
        :param region: The region the metrics of this graph should be taken from. Default: - Current region
        :param title: Title for the graph. Default: - None
        :param width: Width of the widget, in a grid of 24 units wide. Default: 6
        :param annotations: Annotations for the left Y axis. Default: - No annotations
        :param end: The end of the time range to use for each widget independently from those of the dashboard. If you specify a value for end, you must also specify a value for start. Specify an absolute time in the ISO 8601 format. For example, 2018-12-17T06:00:00.000Z. Default: When the dashboard loads, the end date will be the current time.
        :param left_y_axis: Left Y axis. Default: - None
        :param legend_position: Position of the legend. Default: - bottom
        :param live_data: Whether the graph should show live data. Default: false
        :param metrics: Metrics to display on left Y axis. Default: - No metrics
        :param period: The default period for all metrics in this widget. The period is the length of time represented by one data point on the graph. This default can be overridden within each metric definition. Default: cdk.Duration.seconds(300)
        :param set_period_to_time_range: Whether to show the value from the entire time range. Only applicable for Bar and Pie charts. If false, values will be from the most recent period of your chosen time range; if true, shows the value from the entire time range. Default: false
        :param start: The start of the time range to use for each widget independently from those of the dashboard. You can specify start without specifying end to specify a relative time range that ends with the current time. In this case, the value of start must begin with -P, and you can use M, H, D, W and M as abbreviations for minutes, hours, days, weeks and months. For example, -PT8H shows the last 8 hours and -P3M shows the last three months. You can also use start along with an end field, to specify an absolute time range. When specifying an absolute time range, use the ISO 8601 format. For example, 2018-12-17T06:00:00.000Z. Default: When the dashboard loads, the start time will be the default time range.
        :param statistic: The default statistic to be displayed for each metric. This default can be overridden within the definition of each individual metric Default: - The statistic for each metric is used

        :exampleMetadata: infused

        Example::

            # dashboard: cloudwatch.Dashboard
            # error_alarm: cloudwatch.Alarm
            # gauge_metric: cloudwatch.Metric
            
            
            dashboard.add_widgets(cloudwatch.GaugeWidget(
                metrics=[gauge_metric],
                left_yAxis=cloudwatch.YAxisProps(
                    min=0,
                    max=1000
                )
            ))
        '''
        if isinstance(left_y_axis, dict):
            left_y_axis = YAxisProps(**left_y_axis)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1f8fe2511861f7fc6d2225bf5821fc9134b7036355dffb1d0ddd86a99b53dc5)
            check_type(argname="argument height", value=height, expected_type=type_hints["height"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument title", value=title, expected_type=type_hints["title"])
            check_type(argname="argument width", value=width, expected_type=type_hints["width"])
            check_type(argname="argument annotations", value=annotations, expected_type=type_hints["annotations"])
            check_type(argname="argument end", value=end, expected_type=type_hints["end"])
            check_type(argname="argument left_y_axis", value=left_y_axis, expected_type=type_hints["left_y_axis"])
            check_type(argname="argument legend_position", value=legend_position, expected_type=type_hints["legend_position"])
            check_type(argname="argument live_data", value=live_data, expected_type=type_hints["live_data"])
            check_type(argname="argument metrics", value=metrics, expected_type=type_hints["metrics"])
            check_type(argname="argument period", value=period, expected_type=type_hints["period"])
            check_type(argname="argument set_period_to_time_range", value=set_period_to_time_range, expected_type=type_hints["set_period_to_time_range"])
            check_type(argname="argument start", value=start, expected_type=type_hints["start"])
            check_type(argname="argument statistic", value=statistic, expected_type=type_hints["statistic"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if height is not None:
            self._values["height"] = height
        if region is not None:
            self._values["region"] = region
        if title is not None:
            self._values["title"] = title
        if width is not None:
            self._values["width"] = width
        if annotations is not None:
            self._values["annotations"] = annotations
        if end is not None:
            self._values["end"] = end
        if left_y_axis is not None:
            self._values["left_y_axis"] = left_y_axis
        if legend_position is not None:
            self._values["legend_position"] = legend_position
        if live_data is not None:
            self._values["live_data"] = live_data
        if metrics is not None:
            self._values["metrics"] = metrics
        if period is not None:
            self._values["period"] = period
        if set_period_to_time_range is not None:
            self._values["set_period_to_time_range"] = set_period_to_time_range
        if start is not None:
            self._values["start"] = start
        if statistic is not None:
            self._values["statistic"] = statistic

    @builtins.property
    def height(self) -> typing.Optional[jsii.Number]:
        '''Height of the widget.

        :default:

        - 6 for Alarm and Graph widgets.
        3 for single value widgets where most recent value of a metric is displayed.
        '''
        result = self._values.get("height")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''The region the metrics of this graph should be taken from.

        :default: - Current region
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def title(self) -> typing.Optional[builtins.str]:
        '''Title for the graph.

        :default: - None
        '''
        result = self._values.get("title")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def width(self) -> typing.Optional[jsii.Number]:
        '''Width of the widget, in a grid of 24 units wide.

        :default: 6
        '''
        result = self._values.get("width")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def annotations(self) -> typing.Optional[typing.List[HorizontalAnnotation]]:
        '''Annotations for the left Y axis.

        :default: - No annotations
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Optional[typing.List[HorizontalAnnotation]], result)

    @builtins.property
    def end(self) -> typing.Optional[builtins.str]:
        '''The end of the time range to use for each widget independently from those of the dashboard.

        If you specify a value for end, you must also specify a value for start.
        Specify an absolute time in the ISO 8601 format. For example, 2018-12-17T06:00:00.000Z.

        :default: When the dashboard loads, the end date will be the current time.
        '''
        result = self._values.get("end")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def left_y_axis(self) -> typing.Optional[YAxisProps]:
        '''Left Y axis.

        :default: - None
        '''
        result = self._values.get("left_y_axis")
        return typing.cast(typing.Optional[YAxisProps], result)

    @builtins.property
    def legend_position(self) -> typing.Optional[LegendPosition]:
        '''Position of the legend.

        :default: - bottom
        '''
        result = self._values.get("legend_position")
        return typing.cast(typing.Optional[LegendPosition], result)

    @builtins.property
    def live_data(self) -> typing.Optional[builtins.bool]:
        '''Whether the graph should show live data.

        :default: false
        '''
        result = self._values.get("live_data")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def metrics(self) -> typing.Optional[typing.List[IMetric]]:
        '''Metrics to display on left Y axis.

        :default: - No metrics
        '''
        result = self._values.get("metrics")
        return typing.cast(typing.Optional[typing.List[IMetric]], result)

    @builtins.property
    def period(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The default period for all metrics in this widget.

        The period is the length of time represented by one data point on the graph.
        This default can be overridden within each metric definition.

        :default: cdk.Duration.seconds(300)
        '''
        result = self._values.get("period")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def set_period_to_time_range(self) -> typing.Optional[builtins.bool]:
        '''Whether to show the value from the entire time range. Only applicable for Bar and Pie charts.

        If false, values will be from the most recent period of your chosen time range;
        if true, shows the value from the entire time range.

        :default: false
        '''
        result = self._values.get("set_period_to_time_range")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def start(self) -> typing.Optional[builtins.str]:
        '''The start of the time range to use for each widget independently from those of the dashboard.

        You can specify start without specifying end to specify a relative time range that ends with the current time.
        In this case, the value of start must begin with -P, and you can use M, H, D, W and M as abbreviations for
        minutes, hours, days, weeks and months. For example, -PT8H shows the last 8 hours and -P3M shows the last three months.
        You can also use start along with an end field, to specify an absolute time range.
        When specifying an absolute time range, use the ISO 8601 format. For example, 2018-12-17T06:00:00.000Z.

        :default: When the dashboard loads, the start time will be the default time range.
        '''
        result = self._values.get("start")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def statistic(self) -> typing.Optional[builtins.str]:
        '''The default statistic to be displayed for each metric.

        This default can be overridden within the definition of each individual metric

        :default: - The statistic for each metric is used
        '''
        result = self._values.get("statistic")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GaugeWidgetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GraphWidget(
    ConcreteWidget,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudwatch.GraphWidget",
):
    '''A dashboard widget that displays metrics.

    :exampleMetadata: infused

    Example::

        # dashboard: cloudwatch.Dashboard
        
        
        dashboard.add_widgets(cloudwatch.GraphWidget(
            # ...
        
            legend_position=cloudwatch.LegendPosition.RIGHT
        ))
    '''

    def __init__(
        self,
        *,
        end: typing.Optional[builtins.str] = None,
        left: typing.Optional[typing.Sequence[IMetric]] = None,
        left_annotations: typing.Optional[typing.Sequence[typing.Union[HorizontalAnnotation, typing.Dict[builtins.str, typing.Any]]]] = None,
        left_y_axis: typing.Optional[typing.Union[YAxisProps, typing.Dict[builtins.str, typing.Any]]] = None,
        legend_position: typing.Optional[LegendPosition] = None,
        live_data: typing.Optional[builtins.bool] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        right: typing.Optional[typing.Sequence[IMetric]] = None,
        right_annotations: typing.Optional[typing.Sequence[typing.Union[HorizontalAnnotation, typing.Dict[builtins.str, typing.Any]]]] = None,
        right_y_axis: typing.Optional[typing.Union[YAxisProps, typing.Dict[builtins.str, typing.Any]]] = None,
        set_period_to_time_range: typing.Optional[builtins.bool] = None,
        stacked: typing.Optional[builtins.bool] = None,
        start: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        vertical_annotations: typing.Optional[typing.Sequence[typing.Union[VerticalAnnotation, typing.Dict[builtins.str, typing.Any]]]] = None,
        view: typing.Optional[GraphWidgetView] = None,
        height: typing.Optional[jsii.Number] = None,
        region: typing.Optional[builtins.str] = None,
        title: typing.Optional[builtins.str] = None,
        width: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param end: The end of the time range to use for each widget independently from those of the dashboard. If you specify a value for end, you must also specify a value for start. Specify an absolute time in the ISO 8601 format. For example, 2018-12-17T06:00:00.000Z. Default: When the dashboard loads, the end date will be the current time.
        :param left: Metrics to display on left Y axis. Default: - No metrics
        :param left_annotations: Annotations for the left Y axis. Default: - No annotations
        :param left_y_axis: Left Y axis. Default: - None
        :param legend_position: Position of the legend. Default: - bottom
        :param live_data: Whether the graph should show live data. Default: false
        :param period: The default period for all metrics in this widget. The period is the length of time represented by one data point on the graph. This default can be overridden within each metric definition. Default: cdk.Duration.seconds(300)
        :param right: Metrics to display on right Y axis. Default: - No metrics
        :param right_annotations: Annotations for the right Y axis. Default: - No annotations
        :param right_y_axis: Right Y axis. Default: - None
        :param set_period_to_time_range: Whether to show the value from the entire time range. Only applicable for Bar and Pie charts. If false, values will be from the most recent period of your chosen time range; if true, shows the value from the entire time range. Default: false
        :param stacked: Whether the graph should be shown as stacked lines. Default: false
        :param start: The start of the time range to use for each widget independently from those of the dashboard. You can specify start without specifying end to specify a relative time range that ends with the current time. In this case, the value of start must begin with -P, and you can use M, H, D, W and M as abbreviations for minutes, hours, days, weeks and months. For example, -PT8H shows the last 8 hours and -P3M shows the last three months. You can also use start along with an end field, to specify an absolute time range. When specifying an absolute time range, use the ISO 8601 format. For example, 2018-12-17T06:00:00.000Z. Default: When the dashboard loads, the start time will be the default time range.
        :param statistic: The default statistic to be displayed for each metric. This default can be overridden within the definition of each individual metric Default: - The statistic for each metric is used
        :param vertical_annotations: Annotations for the X axis. Default: - No annotations
        :param view: Display this metric. Default: TimeSeries
        :param height: Height of the widget. Default: - 6 for Alarm and Graph widgets. 3 for single value widgets where most recent value of a metric is displayed.
        :param region: The region the metrics of this graph should be taken from. Default: - Current region
        :param title: Title for the graph. Default: - None
        :param width: Width of the widget, in a grid of 24 units wide. Default: 6
        '''
        props = GraphWidgetProps(
            end=end,
            left=left,
            left_annotations=left_annotations,
            left_y_axis=left_y_axis,
            legend_position=legend_position,
            live_data=live_data,
            period=period,
            right=right,
            right_annotations=right_annotations,
            right_y_axis=right_y_axis,
            set_period_to_time_range=set_period_to_time_range,
            stacked=stacked,
            start=start,
            statistic=statistic,
            vertical_annotations=vertical_annotations,
            view=view,
            height=height,
            region=region,
            title=title,
            width=width,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="addLeftMetric")
    def add_left_metric(self, metric: IMetric) -> None:
        '''Add another metric to the left Y axis of the GraphWidget.

        :param metric: the metric to add.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78a36122d01bdf3dadbdef1806a83ff151cd1d77de21139074c37ca284275e0e)
            check_type(argname="argument metric", value=metric, expected_type=type_hints["metric"])
        return typing.cast(None, jsii.invoke(self, "addLeftMetric", [metric]))

    @jsii.member(jsii_name="addRightMetric")
    def add_right_metric(self, metric: IMetric) -> None:
        '''Add another metric to the right Y axis of the GraphWidget.

        :param metric: the metric to add.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d98276ba6bbea7a9a5b2efedfda4a862eeca9b42a2aaca743679984a15762407)
            check_type(argname="argument metric", value=metric, expected_type=type_hints["metric"])
        return typing.cast(None, jsii.invoke(self, "addRightMetric", [metric]))

    @jsii.member(jsii_name="toJson")
    def to_json(self) -> typing.List[typing.Any]:
        '''Return the widget JSON for use in the dashboard.'''
        return typing.cast(typing.List[typing.Any], jsii.invoke(self, "toJson", []))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudwatch.GraphWidgetProps",
    jsii_struct_bases=[MetricWidgetProps],
    name_mapping={
        "height": "height",
        "region": "region",
        "title": "title",
        "width": "width",
        "end": "end",
        "left": "left",
        "left_annotations": "leftAnnotations",
        "left_y_axis": "leftYAxis",
        "legend_position": "legendPosition",
        "live_data": "liveData",
        "period": "period",
        "right": "right",
        "right_annotations": "rightAnnotations",
        "right_y_axis": "rightYAxis",
        "set_period_to_time_range": "setPeriodToTimeRange",
        "stacked": "stacked",
        "start": "start",
        "statistic": "statistic",
        "vertical_annotations": "verticalAnnotations",
        "view": "view",
    },
)
class GraphWidgetProps(MetricWidgetProps):
    def __init__(
        self,
        *,
        height: typing.Optional[jsii.Number] = None,
        region: typing.Optional[builtins.str] = None,
        title: typing.Optional[builtins.str] = None,
        width: typing.Optional[jsii.Number] = None,
        end: typing.Optional[builtins.str] = None,
        left: typing.Optional[typing.Sequence[IMetric]] = None,
        left_annotations: typing.Optional[typing.Sequence[typing.Union[HorizontalAnnotation, typing.Dict[builtins.str, typing.Any]]]] = None,
        left_y_axis: typing.Optional[typing.Union[YAxisProps, typing.Dict[builtins.str, typing.Any]]] = None,
        legend_position: typing.Optional[LegendPosition] = None,
        live_data: typing.Optional[builtins.bool] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        right: typing.Optional[typing.Sequence[IMetric]] = None,
        right_annotations: typing.Optional[typing.Sequence[typing.Union[HorizontalAnnotation, typing.Dict[builtins.str, typing.Any]]]] = None,
        right_y_axis: typing.Optional[typing.Union[YAxisProps, typing.Dict[builtins.str, typing.Any]]] = None,
        set_period_to_time_range: typing.Optional[builtins.bool] = None,
        stacked: typing.Optional[builtins.bool] = None,
        start: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        vertical_annotations: typing.Optional[typing.Sequence[typing.Union[VerticalAnnotation, typing.Dict[builtins.str, typing.Any]]]] = None,
        view: typing.Optional[GraphWidgetView] = None,
    ) -> None:
        '''Properties for a GraphWidget.

        :param height: Height of the widget. Default: - 6 for Alarm and Graph widgets. 3 for single value widgets where most recent value of a metric is displayed.
        :param region: The region the metrics of this graph should be taken from. Default: - Current region
        :param title: Title for the graph. Default: - None
        :param width: Width of the widget, in a grid of 24 units wide. Default: 6
        :param end: The end of the time range to use for each widget independently from those of the dashboard. If you specify a value for end, you must also specify a value for start. Specify an absolute time in the ISO 8601 format. For example, 2018-12-17T06:00:00.000Z. Default: When the dashboard loads, the end date will be the current time.
        :param left: Metrics to display on left Y axis. Default: - No metrics
        :param left_annotations: Annotations for the left Y axis. Default: - No annotations
        :param left_y_axis: Left Y axis. Default: - None
        :param legend_position: Position of the legend. Default: - bottom
        :param live_data: Whether the graph should show live data. Default: false
        :param period: The default period for all metrics in this widget. The period is the length of time represented by one data point on the graph. This default can be overridden within each metric definition. Default: cdk.Duration.seconds(300)
        :param right: Metrics to display on right Y axis. Default: - No metrics
        :param right_annotations: Annotations for the right Y axis. Default: - No annotations
        :param right_y_axis: Right Y axis. Default: - None
        :param set_period_to_time_range: Whether to show the value from the entire time range. Only applicable for Bar and Pie charts. If false, values will be from the most recent period of your chosen time range; if true, shows the value from the entire time range. Default: false
        :param stacked: Whether the graph should be shown as stacked lines. Default: false
        :param start: The start of the time range to use for each widget independently from those of the dashboard. You can specify start without specifying end to specify a relative time range that ends with the current time. In this case, the value of start must begin with -P, and you can use M, H, D, W and M as abbreviations for minutes, hours, days, weeks and months. For example, -PT8H shows the last 8 hours and -P3M shows the last three months. You can also use start along with an end field, to specify an absolute time range. When specifying an absolute time range, use the ISO 8601 format. For example, 2018-12-17T06:00:00.000Z. Default: When the dashboard loads, the start time will be the default time range.
        :param statistic: The default statistic to be displayed for each metric. This default can be overridden within the definition of each individual metric Default: - The statistic for each metric is used
        :param vertical_annotations: Annotations for the X axis. Default: - No annotations
        :param view: Display this metric. Default: TimeSeries

        :exampleMetadata: infused

        Example::

            # dashboard: cloudwatch.Dashboard
            
            
            dashboard.add_widgets(cloudwatch.GraphWidget(
                # ...
            
                legend_position=cloudwatch.LegendPosition.RIGHT
            ))
        '''
        if isinstance(left_y_axis, dict):
            left_y_axis = YAxisProps(**left_y_axis)
        if isinstance(right_y_axis, dict):
            right_y_axis = YAxisProps(**right_y_axis)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3471ad100c9e34a517506d76368276ef9b137a3c7b33aecc91910b5dc9263b3b)
            check_type(argname="argument height", value=height, expected_type=type_hints["height"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument title", value=title, expected_type=type_hints["title"])
            check_type(argname="argument width", value=width, expected_type=type_hints["width"])
            check_type(argname="argument end", value=end, expected_type=type_hints["end"])
            check_type(argname="argument left", value=left, expected_type=type_hints["left"])
            check_type(argname="argument left_annotations", value=left_annotations, expected_type=type_hints["left_annotations"])
            check_type(argname="argument left_y_axis", value=left_y_axis, expected_type=type_hints["left_y_axis"])
            check_type(argname="argument legend_position", value=legend_position, expected_type=type_hints["legend_position"])
            check_type(argname="argument live_data", value=live_data, expected_type=type_hints["live_data"])
            check_type(argname="argument period", value=period, expected_type=type_hints["period"])
            check_type(argname="argument right", value=right, expected_type=type_hints["right"])
            check_type(argname="argument right_annotations", value=right_annotations, expected_type=type_hints["right_annotations"])
            check_type(argname="argument right_y_axis", value=right_y_axis, expected_type=type_hints["right_y_axis"])
            check_type(argname="argument set_period_to_time_range", value=set_period_to_time_range, expected_type=type_hints["set_period_to_time_range"])
            check_type(argname="argument stacked", value=stacked, expected_type=type_hints["stacked"])
            check_type(argname="argument start", value=start, expected_type=type_hints["start"])
            check_type(argname="argument statistic", value=statistic, expected_type=type_hints["statistic"])
            check_type(argname="argument vertical_annotations", value=vertical_annotations, expected_type=type_hints["vertical_annotations"])
            check_type(argname="argument view", value=view, expected_type=type_hints["view"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if height is not None:
            self._values["height"] = height
        if region is not None:
            self._values["region"] = region
        if title is not None:
            self._values["title"] = title
        if width is not None:
            self._values["width"] = width
        if end is not None:
            self._values["end"] = end
        if left is not None:
            self._values["left"] = left
        if left_annotations is not None:
            self._values["left_annotations"] = left_annotations
        if left_y_axis is not None:
            self._values["left_y_axis"] = left_y_axis
        if legend_position is not None:
            self._values["legend_position"] = legend_position
        if live_data is not None:
            self._values["live_data"] = live_data
        if period is not None:
            self._values["period"] = period
        if right is not None:
            self._values["right"] = right
        if right_annotations is not None:
            self._values["right_annotations"] = right_annotations
        if right_y_axis is not None:
            self._values["right_y_axis"] = right_y_axis
        if set_period_to_time_range is not None:
            self._values["set_period_to_time_range"] = set_period_to_time_range
        if stacked is not None:
            self._values["stacked"] = stacked
        if start is not None:
            self._values["start"] = start
        if statistic is not None:
            self._values["statistic"] = statistic
        if vertical_annotations is not None:
            self._values["vertical_annotations"] = vertical_annotations
        if view is not None:
            self._values["view"] = view

    @builtins.property
    def height(self) -> typing.Optional[jsii.Number]:
        '''Height of the widget.

        :default:

        - 6 for Alarm and Graph widgets.
        3 for single value widgets where most recent value of a metric is displayed.
        '''
        result = self._values.get("height")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''The region the metrics of this graph should be taken from.

        :default: - Current region
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def title(self) -> typing.Optional[builtins.str]:
        '''Title for the graph.

        :default: - None
        '''
        result = self._values.get("title")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def width(self) -> typing.Optional[jsii.Number]:
        '''Width of the widget, in a grid of 24 units wide.

        :default: 6
        '''
        result = self._values.get("width")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def end(self) -> typing.Optional[builtins.str]:
        '''The end of the time range to use for each widget independently from those of the dashboard.

        If you specify a value for end, you must also specify a value for start.
        Specify an absolute time in the ISO 8601 format. For example, 2018-12-17T06:00:00.000Z.

        :default: When the dashboard loads, the end date will be the current time.
        '''
        result = self._values.get("end")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def left(self) -> typing.Optional[typing.List[IMetric]]:
        '''Metrics to display on left Y axis.

        :default: - No metrics
        '''
        result = self._values.get("left")
        return typing.cast(typing.Optional[typing.List[IMetric]], result)

    @builtins.property
    def left_annotations(self) -> typing.Optional[typing.List[HorizontalAnnotation]]:
        '''Annotations for the left Y axis.

        :default: - No annotations
        '''
        result = self._values.get("left_annotations")
        return typing.cast(typing.Optional[typing.List[HorizontalAnnotation]], result)

    @builtins.property
    def left_y_axis(self) -> typing.Optional[YAxisProps]:
        '''Left Y axis.

        :default: - None
        '''
        result = self._values.get("left_y_axis")
        return typing.cast(typing.Optional[YAxisProps], result)

    @builtins.property
    def legend_position(self) -> typing.Optional[LegendPosition]:
        '''Position of the legend.

        :default: - bottom
        '''
        result = self._values.get("legend_position")
        return typing.cast(typing.Optional[LegendPosition], result)

    @builtins.property
    def live_data(self) -> typing.Optional[builtins.bool]:
        '''Whether the graph should show live data.

        :default: false
        '''
        result = self._values.get("live_data")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def period(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The default period for all metrics in this widget.

        The period is the length of time represented by one data point on the graph.
        This default can be overridden within each metric definition.

        :default: cdk.Duration.seconds(300)
        '''
        result = self._values.get("period")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def right(self) -> typing.Optional[typing.List[IMetric]]:
        '''Metrics to display on right Y axis.

        :default: - No metrics
        '''
        result = self._values.get("right")
        return typing.cast(typing.Optional[typing.List[IMetric]], result)

    @builtins.property
    def right_annotations(self) -> typing.Optional[typing.List[HorizontalAnnotation]]:
        '''Annotations for the right Y axis.

        :default: - No annotations
        '''
        result = self._values.get("right_annotations")
        return typing.cast(typing.Optional[typing.List[HorizontalAnnotation]], result)

    @builtins.property
    def right_y_axis(self) -> typing.Optional[YAxisProps]:
        '''Right Y axis.

        :default: - None
        '''
        result = self._values.get("right_y_axis")
        return typing.cast(typing.Optional[YAxisProps], result)

    @builtins.property
    def set_period_to_time_range(self) -> typing.Optional[builtins.bool]:
        '''Whether to show the value from the entire time range. Only applicable for Bar and Pie charts.

        If false, values will be from the most recent period of your chosen time range;
        if true, shows the value from the entire time range.

        :default: false
        '''
        result = self._values.get("set_period_to_time_range")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def stacked(self) -> typing.Optional[builtins.bool]:
        '''Whether the graph should be shown as stacked lines.

        :default: false
        '''
        result = self._values.get("stacked")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def start(self) -> typing.Optional[builtins.str]:
        '''The start of the time range to use for each widget independently from those of the dashboard.

        You can specify start without specifying end to specify a relative time range that ends with the current time.
        In this case, the value of start must begin with -P, and you can use M, H, D, W and M as abbreviations for
        minutes, hours, days, weeks and months. For example, -PT8H shows the last 8 hours and -P3M shows the last three months.
        You can also use start along with an end field, to specify an absolute time range.
        When specifying an absolute time range, use the ISO 8601 format. For example, 2018-12-17T06:00:00.000Z.

        :default: When the dashboard loads, the start time will be the default time range.
        '''
        result = self._values.get("start")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def statistic(self) -> typing.Optional[builtins.str]:
        '''The default statistic to be displayed for each metric.

        This default can be overridden within the definition of each individual metric

        :default: - The statistic for each metric is used
        '''
        result = self._values.get("statistic")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vertical_annotations(self) -> typing.Optional[typing.List[VerticalAnnotation]]:
        '''Annotations for the X axis.

        :default: - No annotations
        '''
        result = self._values.get("vertical_annotations")
        return typing.cast(typing.Optional[typing.List[VerticalAnnotation]], result)

    @builtins.property
    def view(self) -> typing.Optional[GraphWidgetView]:
        '''Display this metric.

        :default: TimeSeries
        '''
        result = self._values.get("view")
        return typing.cast(typing.Optional[GraphWidgetView], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GraphWidgetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.aws_cloudwatch.IAlarm")
class IAlarm(IAlarmRule, _IResource_c80c4260, typing_extensions.Protocol):
    '''Represents a CloudWatch Alarm.'''

    @builtins.property
    @jsii.member(jsii_name="alarmArn")
    def alarm_arn(self) -> builtins.str:
        '''Alarm ARN (i.e. arn:aws:cloudwatch:::alarm:Foo).

        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="alarmName")
    def alarm_name(self) -> builtins.str:
        '''Name of the alarm.

        :attribute: true
        '''
        ...


class _IAlarmProxy(
    jsii.proxy_for(IAlarmRule), # type: ignore[misc]
    jsii.proxy_for(_IResource_c80c4260), # type: ignore[misc]
):
    '''Represents a CloudWatch Alarm.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_cloudwatch.IAlarm"

    @builtins.property
    @jsii.member(jsii_name="alarmArn")
    def alarm_arn(self) -> builtins.str:
        '''Alarm ARN (i.e. arn:aws:cloudwatch:::alarm:Foo).

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "alarmArn"))

    @builtins.property
    @jsii.member(jsii_name="alarmName")
    def alarm_name(self) -> builtins.str:
        '''Name of the alarm.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "alarmName"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAlarm).__jsii_proxy_class__ = lambda : _IAlarmProxy


class LogQueryWidget(
    ConcreteWidget,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudwatch.LogQueryWidget",
):
    '''Display query results from Logs Insights.

    :exampleMetadata: infused

    Example::

        # dashboard: cloudwatch.Dashboard
        
        
        dashboard.add_widgets(cloudwatch.LogQueryWidget(
            log_group_names=["my-log-group"],
            view=cloudwatch.LogQueryVisualizationType.TABLE,
            # The lines will be automatically combined using '\n|'.
            query_lines=["fields @message", "filter @message like /Error/"
            ]
        ))
    '''

    def __init__(
        self,
        *,
        log_group_names: typing.Sequence[builtins.str],
        height: typing.Optional[jsii.Number] = None,
        query_lines: typing.Optional[typing.Sequence[builtins.str]] = None,
        query_string: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        title: typing.Optional[builtins.str] = None,
        view: typing.Optional[LogQueryVisualizationType] = None,
        width: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param log_group_names: Names of log groups to query.
        :param height: Height of the widget. Default: 6
        :param query_lines: A sequence of lines to use to build the query. The query will be built by joining the lines together using ``\\n|``. Default: - Exactly one of ``queryString``, ``queryLines`` is required.
        :param query_string: Full query string for log insights. Be sure to prepend every new line with a newline and pipe character (``\\n|``). Default: - Exactly one of ``queryString``, ``queryLines`` is required.
        :param region: The region the metrics of this widget should be taken from. Default: Current region
        :param title: Title for the widget. Default: No title
        :param view: The type of view to use. Default: LogQueryVisualizationType.TABLE
        :param width: Width of the widget, in a grid of 24 units wide. Default: 6
        '''
        props = LogQueryWidgetProps(
            log_group_names=log_group_names,
            height=height,
            query_lines=query_lines,
            query_string=query_string,
            region=region,
            title=title,
            view=view,
            width=width,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="toJson")
    def to_json(self) -> typing.List[typing.Any]:
        '''Return the widget JSON for use in the dashboard.'''
        return typing.cast(typing.List[typing.Any], jsii.invoke(self, "toJson", []))


class SingleValueWidget(
    ConcreteWidget,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudwatch.SingleValueWidget",
):
    '''A dashboard widget that displays the most recent value for every metric.

    :exampleMetadata: infused

    Example::

        # dashboard: cloudwatch.Dashboard
        
        
        dashboard.add_widgets(cloudwatch.SingleValueWidget(
            metrics=[],
        
            period=Duration.minutes(15)
        ))
    '''

    def __init__(
        self,
        *,
        metrics: typing.Sequence[IMetric],
        end: typing.Optional[builtins.str] = None,
        full_precision: typing.Optional[builtins.bool] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        set_period_to_time_range: typing.Optional[builtins.bool] = None,
        sparkline: typing.Optional[builtins.bool] = None,
        start: typing.Optional[builtins.str] = None,
        height: typing.Optional[jsii.Number] = None,
        region: typing.Optional[builtins.str] = None,
        title: typing.Optional[builtins.str] = None,
        width: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param metrics: Metrics to display.
        :param end: The end of the time range to use for each widget independently from those of the dashboard. If you specify a value for end, you must also specify a value for start. Specify an absolute time in the ISO 8601 format. For example, 2018-12-17T06:00:00.000Z. Default: When the dashboard loads, the end date will be the current time.
        :param full_precision: Whether to show as many digits as can fit, before rounding. Default: false
        :param period: The default period for all metrics in this widget. The period is the length of time represented by one data point on the graph. This default can be overridden within each metric definition. Default: cdk.Duration.seconds(300)
        :param set_period_to_time_range: Whether to show the value from the entire time range. Default: false
        :param sparkline: Whether to show a graph below the value illustrating the value for the whole time range. Cannot be used in combination with ``setPeriodToTimeRange`` Default: false
        :param start: The start of the time range to use for each widget independently from those of the dashboard. You can specify start without specifying end to specify a relative time range that ends with the current time. In this case, the value of start must begin with -P, and you can use M, H, D, W and M as abbreviations for minutes, hours, days, weeks and months. For example, -PT8H shows the last 8 hours and -P3M shows the last three months. You can also use start along with an end field, to specify an absolute time range. When specifying an absolute time range, use the ISO 8601 format. For example, 2018-12-17T06:00:00.000Z. Default: When the dashboard loads, the start time will be the default time range.
        :param height: Height of the widget. Default: - 6 for Alarm and Graph widgets. 3 for single value widgets where most recent value of a metric is displayed.
        :param region: The region the metrics of this graph should be taken from. Default: - Current region
        :param title: Title for the graph. Default: - None
        :param width: Width of the widget, in a grid of 24 units wide. Default: 6
        '''
        props = SingleValueWidgetProps(
            metrics=metrics,
            end=end,
            full_precision=full_precision,
            period=period,
            set_period_to_time_range=set_period_to_time_range,
            sparkline=sparkline,
            start=start,
            height=height,
            region=region,
            title=title,
            width=width,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="toJson")
    def to_json(self) -> typing.List[typing.Any]:
        '''Return the widget JSON for use in the dashboard.'''
        return typing.cast(typing.List[typing.Any], jsii.invoke(self, "toJson", []))


class TableWidget(
    ConcreteWidget,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudwatch.TableWidget",
):
    '''A dashboard widget that displays metrics.

    :exampleMetadata: infused

    Example::

        # dashboard: cloudwatch.Dashboard
        
        
        dashboard.add_widgets(cloudwatch.TableWidget(
            # ...
        
            layout=cloudwatch.TableLayout.VERTICAL
        ))
    '''

    def __init__(
        self,
        *,
        end: typing.Optional[builtins.str] = None,
        full_precision: typing.Optional[builtins.bool] = None,
        layout: typing.Optional[TableLayout] = None,
        live_data: typing.Optional[builtins.bool] = None,
        metrics: typing.Optional[typing.Sequence[IMetric]] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        set_period_to_time_range: typing.Optional[builtins.bool] = None,
        show_units_in_label: typing.Optional[builtins.bool] = None,
        start: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        summary: typing.Optional[typing.Union[TableSummaryProps, typing.Dict[builtins.str, typing.Any]]] = None,
        thresholds: typing.Optional[typing.Sequence[TableThreshold]] = None,
        height: typing.Optional[jsii.Number] = None,
        region: typing.Optional[builtins.str] = None,
        title: typing.Optional[builtins.str] = None,
        width: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param end: The end of the time range to use for each widget independently from those of the dashboard. If you specify a value for end, you must also specify a value for start. Specify an absolute time in the ISO 8601 format. For example, 2018-12-17T06:00:00.000Z. Default: When the dashboard loads, the end date will be the current time.
        :param full_precision: Whether to show as many digits as can fit, before rounding. Default: false
        :param layout: Table layout. Default: - TableLayout.HORIZONTAL
        :param live_data: Whether the graph should show live data. Default: false
        :param metrics: Metrics to display in the table. Default: - No metrics
        :param period: The default period for all metrics in this widget. The period is the length of time represented by one data point on the graph. This default can be overridden within each metric definition. Default: cdk.Duration.seconds(300)
        :param set_period_to_time_range: Whether to show the value from the entire time range. Only applicable for Bar and Pie charts. If false, values will be from the most recent period of your chosen time range; if true, shows the value from the entire time range. Default: false
        :param show_units_in_label: Show the metrics units in the label column. Default: - false
        :param start: The start of the time range to use for each widget independently from those of the dashboard. You can specify start without specifying end to specify a relative time range that ends with the current time. In this case, the value of start must begin with -P, and you can use M, H, D, W and M as abbreviations for minutes, hours, days, weeks and months. For example, -PT8H shows the last 8 hours and -P3M shows the last three months. You can also use start along with an end field, to specify an absolute time range. When specifying an absolute time range, use the ISO 8601 format. For example, 2018-12-17T06:00:00.000Z. Default: When the dashboard loads, the start time will be the default time range.
        :param statistic: The default statistic to be displayed for each metric. This default can be overridden within the definition of each individual metric Default: - The statistic for each metric is used
        :param summary: Properties for displaying summary columns. Default: - no summary columns are shown
        :param thresholds: Thresholds for highlighting table cells. Default: - No thresholds
        :param height: Height of the widget. Default: - 6 for Alarm and Graph widgets. 3 for single value widgets where most recent value of a metric is displayed.
        :param region: The region the metrics of this graph should be taken from. Default: - Current region
        :param title: Title for the graph. Default: - None
        :param width: Width of the widget, in a grid of 24 units wide. Default: 6
        '''
        props = TableWidgetProps(
            end=end,
            full_precision=full_precision,
            layout=layout,
            live_data=live_data,
            metrics=metrics,
            period=period,
            set_period_to_time_range=set_period_to_time_range,
            show_units_in_label=show_units_in_label,
            start=start,
            statistic=statistic,
            summary=summary,
            thresholds=thresholds,
            height=height,
            region=region,
            title=title,
            width=width,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="addMetric")
    def add_metric(self, metric: IMetric) -> None:
        '''Add another metric.

        :param metric: the metric to add.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14b284f52f62e4bb0b4243fb3b3bcaa2693e6ee107b2721f9467d31d81cf408b)
            check_type(argname="argument metric", value=metric, expected_type=type_hints["metric"])
        return typing.cast(None, jsii.invoke(self, "addMetric", [metric]))

    @jsii.member(jsii_name="toJson")
    def to_json(self) -> typing.List[typing.Any]:
        '''Return the widget JSON for use in the dashboard.'''
        return typing.cast(typing.List[typing.Any], jsii.invoke(self, "toJson", []))


class TextWidget(
    ConcreteWidget,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudwatch.TextWidget",
):
    '''A dashboard widget that displays MarkDown.

    :exampleMetadata: infused

    Example::

        # dashboard: cloudwatch.Dashboard
        
        
        dashboard.add_widgets(cloudwatch.TextWidget(
            markdown="# Key Performance Indicators"
        ))
    '''

    def __init__(
        self,
        *,
        markdown: builtins.str,
        background: typing.Optional[TextWidgetBackground] = None,
        height: typing.Optional[jsii.Number] = None,
        width: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param markdown: The text to display, in MarkDown format.
        :param background: Background for the widget. Default: solid
        :param height: Height of the widget. Default: 2
        :param width: Width of the widget, in a grid of 24 units wide. Default: 6
        '''
        props = TextWidgetProps(
            markdown=markdown, background=background, height=height, width=width
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="position")
    def position(self, x: jsii.Number, y: jsii.Number) -> None:
        '''Place the widget at a given position.

        :param x: -
        :param y: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8d51865c110b61caff6f389abfdbc4862eb4488d27c9b39083e0293fd0be343)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
            check_type(argname="argument y", value=y, expected_type=type_hints["y"])
        return typing.cast(None, jsii.invoke(self, "position", [x, y]))

    @jsii.member(jsii_name="toJson")
    def to_json(self) -> typing.List[typing.Any]:
        '''Return the widget JSON for use in the dashboard.'''
        return typing.cast(typing.List[typing.Any], jsii.invoke(self, "toJson", []))


@jsii.implements(IAlarm)
class AlarmBase(
    _Resource_45bc6135,
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="aws-cdk-lib.aws_cloudwatch.AlarmBase",
):
    '''The base class for Alarm and CompositeAlarm resources.'''

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
            type_hints = typing.get_type_hints(_typecheckingstub__6e7154d8d457acf3b0cf78ed544360096e7c3981ec43306ad2f509853c4efe1b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = _ResourceProps_15a65b4e(
            account=account,
            environment_from_arn=environment_from_arn,
            physical_name=physical_name,
            region=region,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="addAlarmAction")
    def add_alarm_action(self, *actions: IAlarmAction) -> None:
        '''Trigger this action if the alarm fires.

        Typically SnsAction or AutoScalingAction.

        :param actions: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bbc62cbd9f9d10401db80f46c6d4b0e4a15c97163470cbdd2dd91c82b5a76c38)
            check_type(argname="argument actions", value=actions, expected_type=typing.Tuple[type_hints["actions"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "addAlarmAction", [*actions]))

    @jsii.member(jsii_name="addInsufficientDataAction")
    def add_insufficient_data_action(self, *actions: IAlarmAction) -> None:
        '''Trigger this action if there is insufficient data to evaluate the alarm.

        Typically SnsAction or AutoScalingAction.

        :param actions: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e588099840d4554b8e9faf3cc33868d492f714f24d214d9f770291fb25fad20)
            check_type(argname="argument actions", value=actions, expected_type=typing.Tuple[type_hints["actions"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "addInsufficientDataAction", [*actions]))

    @jsii.member(jsii_name="addOkAction")
    def add_ok_action(self, *actions: IAlarmAction) -> None:
        '''Trigger this action if the alarm returns from breaching state into ok state.

        Typically SnsAction or AutoScalingAction.

        :param actions: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f195fe021c2d9115ee79498e038ce63454be2e0d319995ca3a3d767feb45dab)
            check_type(argname="argument actions", value=actions, expected_type=typing.Tuple[type_hints["actions"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "addOkAction", [*actions]))

    @jsii.member(jsii_name="renderAlarmRule")
    def render_alarm_rule(self) -> builtins.str:
        '''AlarmRule indicating ALARM state for Alarm.'''
        return typing.cast(builtins.str, jsii.invoke(self, "renderAlarmRule", []))

    @builtins.property
    @jsii.member(jsii_name="alarmArn")
    @abc.abstractmethod
    def alarm_arn(self) -> builtins.str:
        '''Alarm ARN (i.e. arn:aws:cloudwatch:::alarm:Foo).

        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="alarmName")
    @abc.abstractmethod
    def alarm_name(self) -> builtins.str:
        '''Name of the alarm.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="alarmActionArns")
    def _alarm_action_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "alarmActionArns"))

    @_alarm_action_arns.setter
    def _alarm_action_arns(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f77158cf05762b87148c9ece7c4fc0f4591bc620078d7052247bf9fa5146bbe8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alarmActionArns", value)

    @builtins.property
    @jsii.member(jsii_name="insufficientDataActionArns")
    def _insufficient_data_action_arns(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "insufficientDataActionArns"))

    @_insufficient_data_action_arns.setter
    def _insufficient_data_action_arns(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e28ecf3733272408c8625c4e9726b39ea586c58f4c89c08d7ba8579a99a5247)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "insufficientDataActionArns", value)

    @builtins.property
    @jsii.member(jsii_name="okActionArns")
    def _ok_action_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "okActionArns"))

    @_ok_action_arns.setter
    def _ok_action_arns(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32c054ee1bf96f6ce4073fc60bc6e30b8c1c7d0fe7f902e814f6554b6ee36a71)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "okActionArns", value)


class _AlarmBaseProxy(
    AlarmBase,
    jsii.proxy_for(_Resource_45bc6135), # type: ignore[misc]
):
    @builtins.property
    @jsii.member(jsii_name="alarmArn")
    def alarm_arn(self) -> builtins.str:
        '''Alarm ARN (i.e. arn:aws:cloudwatch:::alarm:Foo).

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "alarmArn"))

    @builtins.property
    @jsii.member(jsii_name="alarmName")
    def alarm_name(self) -> builtins.str:
        '''Name of the alarm.'''
        return typing.cast(builtins.str, jsii.get(self, "alarmName"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, AlarmBase).__jsii_proxy_class__ = lambda : _AlarmBaseProxy


class AlarmStatusWidget(
    ConcreteWidget,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudwatch.AlarmStatusWidget",
):
    '''A dashboard widget that displays alarms in a grid view.

    :exampleMetadata: infused

    Example::

        # dashboard: cloudwatch.Dashboard
        # error_alarm: cloudwatch.Alarm
        
        
        dashboard.add_widgets(
            cloudwatch.AlarmStatusWidget(
                alarms=[error_alarm]
            ))
    '''

    def __init__(
        self,
        *,
        alarms: typing.Sequence[IAlarm],
        height: typing.Optional[jsii.Number] = None,
        sort_by: typing.Optional[AlarmStatusWidgetSortBy] = None,
        states: typing.Optional[typing.Sequence[AlarmState]] = None,
        title: typing.Optional[builtins.str] = None,
        width: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param alarms: CloudWatch Alarms to show in widget.
        :param height: Height of the widget. Default: 3
        :param sort_by: Specifies how to sort the alarms in the widget. Default: - alphabetical order
        :param states: Use this field to filter the list of alarms displayed in the widget to only those alarms currently in the specified states. You can specify one or more alarm states in the value for this field. The alarm states that you can specify are ALARM, INSUFFICIENT_DATA, and OK. If you omit this field or specify an empty array, all the alarms specifed in alarms are displayed. Default: - all the alarms specified in alarms are displayed.
        :param title: The title of the widget. Default: 'Alarm Status'
        :param width: Width of the widget, in a grid of 24 units wide. Default: 6
        '''
        props = AlarmStatusWidgetProps(
            alarms=alarms,
            height=height,
            sort_by=sort_by,
            states=states,
            title=title,
            width=width,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="position")
    def position(self, x: jsii.Number, y: jsii.Number) -> None:
        '''Place the widget at a given position.

        :param x: -
        :param y: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1fc0a3126fa9c8844de1784e81a9f4f3230086511ca9713ee2ff0d042663da5f)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
            check_type(argname="argument y", value=y, expected_type=type_hints["y"])
        return typing.cast(None, jsii.invoke(self, "position", [x, y]))

    @jsii.member(jsii_name="toJson")
    def to_json(self) -> typing.List[typing.Any]:
        '''Return the widget JSON for use in the dashboard.'''
        return typing.cast(typing.List[typing.Any], jsii.invoke(self, "toJson", []))


class AlarmWidget(
    ConcreteWidget,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudwatch.AlarmWidget",
):
    '''Display the metric associated with an alarm, including the alarm line.

    :exampleMetadata: infused

    Example::

        # dashboard: cloudwatch.Dashboard
        # error_alarm: cloudwatch.Alarm
        
        
        dashboard.add_widgets(cloudwatch.AlarmWidget(
            title="Errors",
            alarm=error_alarm
        ))
    '''

    def __init__(
        self,
        *,
        alarm: IAlarm,
        left_y_axis: typing.Optional[typing.Union[YAxisProps, typing.Dict[builtins.str, typing.Any]]] = None,
        height: typing.Optional[jsii.Number] = None,
        region: typing.Optional[builtins.str] = None,
        title: typing.Optional[builtins.str] = None,
        width: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param alarm: The alarm to show.
        :param left_y_axis: Left Y axis. Default: - No minimum or maximum values for the left Y-axis
        :param height: Height of the widget. Default: - 6 for Alarm and Graph widgets. 3 for single value widgets where most recent value of a metric is displayed.
        :param region: The region the metrics of this graph should be taken from. Default: - Current region
        :param title: Title for the graph. Default: - None
        :param width: Width of the widget, in a grid of 24 units wide. Default: 6
        '''
        props = AlarmWidgetProps(
            alarm=alarm,
            left_y_axis=left_y_axis,
            height=height,
            region=region,
            title=title,
            width=width,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="toJson")
    def to_json(self) -> typing.List[typing.Any]:
        '''Return the widget JSON for use in the dashboard.'''
        return typing.cast(typing.List[typing.Any], jsii.invoke(self, "toJson", []))


class CompositeAlarm(
    AlarmBase,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudwatch.CompositeAlarm",
):
    '''A Composite Alarm based on Alarm Rule.

    :exampleMetadata: infused

    Example::

        # alarm1: cloudwatch.Alarm
        # alarm2: cloudwatch.Alarm
        # alarm3: cloudwatch.Alarm
        # alarm4: cloudwatch.Alarm
        
        
        alarm_rule = cloudwatch.AlarmRule.any_of(
            cloudwatch.AlarmRule.all_of(
                cloudwatch.AlarmRule.any_of(alarm1,
                    cloudwatch.AlarmRule.from_alarm(alarm2, cloudwatch.AlarmState.OK), alarm3),
                cloudwatch.AlarmRule.not(cloudwatch.AlarmRule.from_alarm(alarm4, cloudwatch.AlarmState.INSUFFICIENT_DATA))),
            cloudwatch.AlarmRule.from_boolean(False))
        
        cloudwatch.CompositeAlarm(self, "MyAwesomeCompositeAlarm",
            alarm_rule=alarm_rule
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        alarm_rule: IAlarmRule,
        actions_enabled: typing.Optional[builtins.bool] = None,
        actions_suppressor: typing.Optional[IAlarm] = None,
        actions_suppressor_extension_period: typing.Optional[_Duration_4839e8c3] = None,
        actions_suppressor_wait_period: typing.Optional[_Duration_4839e8c3] = None,
        alarm_description: typing.Optional[builtins.str] = None,
        composite_alarm_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param alarm_rule: Expression that specifies which other alarms are to be evaluated to determine this composite alarm's state.
        :param actions_enabled: Whether the actions for this alarm are enabled. Default: true
        :param actions_suppressor: Actions will be suppressed if the suppressor alarm is in the ALARM state. Default: - alarm will not be suppressed.
        :param actions_suppressor_extension_period: The maximum duration that the composite alarm waits after suppressor alarm goes out of the ALARM state. After this time, the composite alarm performs its actions. Default: - 1 minute extension period will be set.
        :param actions_suppressor_wait_period: The maximum duration that the composite alarm waits for the suppressor alarm to go into the ALARM state. After this time, the composite alarm performs its actions. Default: - 1 minute wait period will be set.
        :param alarm_description: Description for the alarm. Default: - No description.
        :param composite_alarm_name: Name of the alarm. Default: - Automatically generated name.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7a7ea1ddc8fb0690826832fbc77c405acacd10123a1aa81696d3863d8252abb)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CompositeAlarmProps(
            alarm_rule=alarm_rule,
            actions_enabled=actions_enabled,
            actions_suppressor=actions_suppressor,
            actions_suppressor_extension_period=actions_suppressor_extension_period,
            actions_suppressor_wait_period=actions_suppressor_wait_period,
            alarm_description=alarm_description,
            composite_alarm_name=composite_alarm_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromCompositeAlarmArn")
    @builtins.classmethod
    def from_composite_alarm_arn(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        composite_alarm_arn: builtins.str,
    ) -> IAlarm:
        '''Import an existing CloudWatch composite alarm provided an ARN.

        :param scope: The parent creating construct (usually ``this``).
        :param id: The construct's name.
        :param composite_alarm_arn: Composite Alarm ARN (i.e. arn:aws:cloudwatch:::alarm:CompositeAlarmName).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dfb039403469bae811c18af1008f632188c3f4e24312b57fe3c23c7e5e1405fc)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument composite_alarm_arn", value=composite_alarm_arn, expected_type=type_hints["composite_alarm_arn"])
        return typing.cast(IAlarm, jsii.sinvoke(cls, "fromCompositeAlarmArn", [scope, id, composite_alarm_arn]))

    @jsii.member(jsii_name="fromCompositeAlarmName")
    @builtins.classmethod
    def from_composite_alarm_name(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        composite_alarm_name: builtins.str,
    ) -> IAlarm:
        '''Import an existing CloudWatch composite alarm provided an Name.

        :param scope: The parent creating construct (usually ``this``).
        :param id: The construct's name.
        :param composite_alarm_name: Composite Alarm Name.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7b77df6004a58e1183aacd1214d4fe5762c7287cc2361f2ff0337e84ccbb6b3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument composite_alarm_name", value=composite_alarm_name, expected_type=type_hints["composite_alarm_name"])
        return typing.cast(IAlarm, jsii.sinvoke(cls, "fromCompositeAlarmName", [scope, id, composite_alarm_name]))

    @builtins.property
    @jsii.member(jsii_name="alarmArn")
    def alarm_arn(self) -> builtins.str:
        '''ARN of this alarm.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "alarmArn"))

    @builtins.property
    @jsii.member(jsii_name="alarmName")
    def alarm_name(self) -> builtins.str:
        '''Name of this alarm.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "alarmName"))


class Alarm(
    AlarmBase,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudwatch.Alarm",
):
    '''An alarm on a CloudWatch metric.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_cloudwatch as cloudwatch
        
        # alias: lambda.Alias
        
        # or add alarms to an existing group
        # blue_green_alias: lambda.Alias
        
        alarm = cloudwatch.Alarm(self, "Errors",
            comparison_operator=cloudwatch.ComparisonOperator.GREATER_THAN_THRESHOLD,
            threshold=1,
            evaluation_periods=1,
            metric=alias.metric_errors()
        )
        deployment_group = codedeploy.LambdaDeploymentGroup(self, "BlueGreenDeployment",
            alias=alias,
            deployment_config=codedeploy.LambdaDeploymentConfig.LINEAR_10PERCENT_EVERY_1MINUTE,
            alarms=[alarm
            ]
        )
        deployment_group.add_alarm(cloudwatch.Alarm(self, "BlueGreenErrors",
            comparison_operator=cloudwatch.ComparisonOperator.GREATER_THAN_THRESHOLD,
            threshold=1,
            evaluation_periods=1,
            metric=blue_green_alias.metric_errors()
        ))
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        metric: IMetric,
        evaluation_periods: jsii.Number,
        threshold: jsii.Number,
        actions_enabled: typing.Optional[builtins.bool] = None,
        alarm_description: typing.Optional[builtins.str] = None,
        alarm_name: typing.Optional[builtins.str] = None,
        comparison_operator: typing.Optional[ComparisonOperator] = None,
        datapoints_to_alarm: typing.Optional[jsii.Number] = None,
        evaluate_low_sample_count_percentile: typing.Optional[builtins.str] = None,
        treat_missing_data: typing.Optional[TreatMissingData] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param metric: The metric to add the alarm on. Metric objects can be obtained from most resources, or you can construct custom Metric objects by instantiating one.
        :param evaluation_periods: The number of periods over which data is compared to the specified threshold.
        :param threshold: The value against which the specified statistic is compared.
        :param actions_enabled: Whether the actions for this alarm are enabled. Default: true
        :param alarm_description: Description for the alarm. Default: No description
        :param alarm_name: Name of the alarm. Default: Automatically generated name
        :param comparison_operator: Comparison to use to check if metric is breaching. Default: GreaterThanOrEqualToThreshold
        :param datapoints_to_alarm: The number of datapoints that must be breaching to trigger the alarm. This is used only if you are setting an "M out of N" alarm. In that case, this value is the M. For more information, see Evaluating an Alarm in the Amazon CloudWatch User Guide. Default: ``evaluationPeriods``
        :param evaluate_low_sample_count_percentile: Specifies whether to evaluate the data and potentially change the alarm state if there are too few data points to be statistically significant. Used only for alarms that are based on percentiles. Default: - Not configured.
        :param treat_missing_data: Sets how this alarm is to handle missing data points. Default: TreatMissingData.Missing
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41e461c6171d2c06570e53eaf2dc07ca5b3d80e0feb2f773d23b3dd8e3826382)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = AlarmProps(
            metric=metric,
            evaluation_periods=evaluation_periods,
            threshold=threshold,
            actions_enabled=actions_enabled,
            alarm_description=alarm_description,
            alarm_name=alarm_name,
            comparison_operator=comparison_operator,
            datapoints_to_alarm=datapoints_to_alarm,
            evaluate_low_sample_count_percentile=evaluate_low_sample_count_percentile,
            treat_missing_data=treat_missing_data,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromAlarmArn")
    @builtins.classmethod
    def from_alarm_arn(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        alarm_arn: builtins.str,
    ) -> IAlarm:
        '''Import an existing CloudWatch alarm provided an ARN.

        :param scope: The parent creating construct (usually ``this``).
        :param id: The construct's name.
        :param alarm_arn: Alarm ARN (i.e. arn:aws:cloudwatch:::alarm:Foo).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8a5a6150e68ee9e26c8b7ebe6f92594c12f9b3cda4195d76462b991008c92b5)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument alarm_arn", value=alarm_arn, expected_type=type_hints["alarm_arn"])
        return typing.cast(IAlarm, jsii.sinvoke(cls, "fromAlarmArn", [scope, id, alarm_arn]))

    @jsii.member(jsii_name="fromAlarmName")
    @builtins.classmethod
    def from_alarm_name(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        alarm_name: builtins.str,
    ) -> IAlarm:
        '''Import an existing CloudWatch alarm provided an Name.

        :param scope: The parent creating construct (usually ``this``).
        :param id: The construct's name.
        :param alarm_name: Alarm Name.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f69e87f80e55b26f710e5c03872b4814d854ded266dd530cb19c3aeb9cae0b2)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument alarm_name", value=alarm_name, expected_type=type_hints["alarm_name"])
        return typing.cast(IAlarm, jsii.sinvoke(cls, "fromAlarmName", [scope, id, alarm_name]))

    @jsii.member(jsii_name="addAlarmAction")
    def add_alarm_action(self, *actions: IAlarmAction) -> None:
        '''Trigger this action if the alarm fires.

        Typically SnsAcion or AutoScalingAction.

        :param actions: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35e42b79cd71f370c96d9123c26abff1c323e3360845e3957f3fa6b0bb344dde)
            check_type(argname="argument actions", value=actions, expected_type=typing.Tuple[type_hints["actions"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "addAlarmAction", [*actions]))

    @jsii.member(jsii_name="toAnnotation")
    def to_annotation(self) -> HorizontalAnnotation:
        '''Turn this alarm into a horizontal annotation.

        This is useful if you want to represent an Alarm in a non-AlarmWidget.
        An ``AlarmWidget`` can directly show an alarm, but it can only show a
        single alarm and no other metrics. Instead, you can convert the alarm to
        a HorizontalAnnotation and add it as an annotation to another graph.

        This might be useful if:

        - You want to show multiple alarms inside a single graph, for example if
          you have both a "small margin/long period" alarm as well as a
          "large margin/short period" alarm.
        - You want to show an Alarm line in a graph with multiple metrics in it.
        '''
        return typing.cast(HorizontalAnnotation, jsii.invoke(self, "toAnnotation", []))

    @builtins.property
    @jsii.member(jsii_name="alarmArn")
    def alarm_arn(self) -> builtins.str:
        '''ARN of this alarm.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "alarmArn"))

    @builtins.property
    @jsii.member(jsii_name="alarmName")
    def alarm_name(self) -> builtins.str:
        '''Name of this alarm.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "alarmName"))

    @builtins.property
    @jsii.member(jsii_name="metric")
    def metric(self) -> IMetric:
        '''The metric object this alarm was based on.'''
        return typing.cast(IMetric, jsii.get(self, "metric"))


__all__ = [
    "Alarm",
    "AlarmActionConfig",
    "AlarmBase",
    "AlarmProps",
    "AlarmRule",
    "AlarmState",
    "AlarmStatusWidget",
    "AlarmStatusWidgetProps",
    "AlarmStatusWidgetSortBy",
    "AlarmWidget",
    "AlarmWidgetProps",
    "CfnAlarm",
    "CfnAlarmProps",
    "CfnAnomalyDetector",
    "CfnAnomalyDetectorProps",
    "CfnCompositeAlarm",
    "CfnCompositeAlarmProps",
    "CfnDashboard",
    "CfnDashboardProps",
    "CfnInsightRule",
    "CfnInsightRuleProps",
    "CfnMetricStream",
    "CfnMetricStreamProps",
    "Color",
    "Column",
    "CommonMetricOptions",
    "ComparisonOperator",
    "CompositeAlarm",
    "CompositeAlarmProps",
    "ConcreteWidget",
    "CreateAlarmOptions",
    "CustomWidget",
    "CustomWidgetProps",
    "Dashboard",
    "DashboardProps",
    "DashboardVariable",
    "DashboardVariableOptions",
    "DefaultValue",
    "Dimension",
    "GaugeWidget",
    "GaugeWidgetProps",
    "GraphWidget",
    "GraphWidgetProps",
    "GraphWidgetView",
    "HorizontalAnnotation",
    "IAlarm",
    "IAlarmAction",
    "IAlarmRule",
    "IMetric",
    "IVariable",
    "IWidget",
    "LegendPosition",
    "LogQueryVisualizationType",
    "LogQueryWidget",
    "LogQueryWidgetProps",
    "MathExpression",
    "MathExpressionOptions",
    "MathExpressionProps",
    "Metric",
    "MetricConfig",
    "MetricExpressionConfig",
    "MetricOptions",
    "MetricProps",
    "MetricStatConfig",
    "MetricWidgetProps",
    "PeriodOverride",
    "Row",
    "SearchComponents",
    "Shading",
    "SingleValueWidget",
    "SingleValueWidgetProps",
    "Spacer",
    "SpacerProps",
    "Statistic",
    "Stats",
    "TableLayout",
    "TableSummaryColumn",
    "TableSummaryProps",
    "TableThreshold",
    "TableWidget",
    "TableWidgetProps",
    "TextWidget",
    "TextWidgetBackground",
    "TextWidgetProps",
    "TreatMissingData",
    "Unit",
    "Values",
    "VariableInputType",
    "VariableType",
    "VariableValue",
    "VerticalAnnotation",
    "VerticalShading",
    "YAxisProps",
]

publication.publish()

def _typecheckingstub__1f1ff7030413de3d64c1ba15be58b5993bda266f09d078a54ade9ac8b5a2c478(
    *,
    alarm_action_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a73fcf7d7f6f71bc46cabb994493848ff6474356a6f35fb7c178bc77e7b4bf0b(
    *operands: IAlarmRule,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c83f7a2932bb0e6ad7daedb63c82a736735f725c8596adb65d2dd0358464ade(
    *operands: IAlarmRule,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7dd0ffc30f4ddc0cb0621fdae0fe1af07770e9fd504527c4df1f6e9ed2032cc(
    alarm: IAlarm,
    alarm_state: AlarmState,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4a2328411f3cd1f101e6ec1cb8b2e99fc902ce06552b8b213d9cab093ad51cc(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ab510b22518be75f8aa37082e6a3eb8a0352f4b78b509de75bac3e2651e7909(
    alarm_rule: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__130f148217f9842e34a2de59608585cc9ab66211fa42610aa323425b1f214b0a(
    operand: IAlarmRule,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b487d6400a85492ffe968131ec5a7294320f90cef90f0505f02beffc7d3055a1(
    *,
    alarms: typing.Sequence[IAlarm],
    height: typing.Optional[jsii.Number] = None,
    sort_by: typing.Optional[AlarmStatusWidgetSortBy] = None,
    states: typing.Optional[typing.Sequence[AlarmState]] = None,
    title: typing.Optional[builtins.str] = None,
    width: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5adc477b9cef758736625389f1a51dec08eb7b348be35f42b0e37d6d4d1f1b68(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    comparison_operator: builtins.str,
    evaluation_periods: jsii.Number,
    actions_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    alarm_actions: typing.Optional[typing.Sequence[builtins.str]] = None,
    alarm_description: typing.Optional[builtins.str] = None,
    alarm_name: typing.Optional[builtins.str] = None,
    datapoints_to_alarm: typing.Optional[jsii.Number] = None,
    dimensions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAlarm.DimensionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    evaluate_low_sample_count_percentile: typing.Optional[builtins.str] = None,
    extended_statistic: typing.Optional[builtins.str] = None,
    insufficient_data_actions: typing.Optional[typing.Sequence[builtins.str]] = None,
    metric_name: typing.Optional[builtins.str] = None,
    metrics: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAlarm.MetricDataQueryProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    namespace: typing.Optional[builtins.str] = None,
    ok_actions: typing.Optional[typing.Sequence[builtins.str]] = None,
    period: typing.Optional[jsii.Number] = None,
    statistic: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    threshold: typing.Optional[jsii.Number] = None,
    threshold_metric_id: typing.Optional[builtins.str] = None,
    treat_missing_data: typing.Optional[builtins.str] = None,
    unit: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83bef261115d965bc301e33589e4c9b4a854da5d951fb8e2186758fba16c7f57(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8443d72766166ac6ee22ecc2f730f3a6b9fd8414ecf17bbd95ef7e5baf82310(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b70639e8f0bfbbc34ad2338567df4a5d70d17215776eb7aa3581fbe2e40cd29(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c080be98f630293bbc63f05942376d4ca0d4a15c82eb9cee4cb1c32b2740abc4(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__605b7067b394998a8071adbf9755ea958792836f86023d0ef23df99b8ee52bcb(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ecc41a9526c2e2c0867e81a362f65327319d216e7659dca4b3860ae75753c28a(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae70f62af2cc75616247d133c6c848bc3a0216db1566dcd494bdbf08a99c4638(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23c8c04504dd76a6623e461e9b6448e0dbf5a2092e2c1aed4d8ecbff1f899de1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8ecc192776c2ee14846f714a390af6c702ed6e634dd57dd26288202304a0796(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6076cadb3051943abe05b65350e48c7b75b471794dd9cdc8472d1758a7b8cd4e(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnAlarm.DimensionProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aec0314071d83d4872fc9ec8f90d1938e3aa18c267eaf43f637379b01d86c684(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__888f8bf20de080b19a46eb68471ca6b6923449631ab8135ff7aa454a9f07b7e9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5eda8d8bf828721d6f8004c5a122ff02b8cf461eca3fe5dc711411c966cf3f14(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71f82ca7521ace9dd7ff6c8ef3a9d77edf1d69fcd526f9d5535ff804be3e3d3f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13ee627a7bc97218488ea85296e024a4aa67101fe00623848363348c246cc493(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnAlarm.MetricDataQueryProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c788f613b67dd11d2bae1b2a09b80da6e70c30f1037ed4dad770b721c5a5fc9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e122d784f2d44eb64ddfad9117d6763bb7f170c7d3e0dc4a96dc353d55ac374d(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__628a5231423fe29bcf97062014bb2e10fb13ab9ea4e1008de39270a9520ab6a4(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__233ab7996f3717f1bae1d0b9c6063cfa83de67875ac91777906dbd68693e81a3(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__895712e62b896ed30b8848bddfdb970fd334934c19393e2eb8ad06392ecf8af9(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5fbcb41a59e8a1cba566cf0b26b3129b32d1bb58de6d5fcb5045e9d2ddf908de(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0dea69dd6b9252440a0712cbe34f23c9bf1cc751d0b8326af6517cd05d511fc3(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__daed33fabd0003672d13ed63fe7c6c290e186f469fb0feb75842f06ec413f25a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2311746224e8eb79c889c7ea604776c607667cdabb1ca67c2b7b269c33749d5(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__caa951097684de7785a360ff0dd7dd52b38193dd6abedc429031dbeef388a48b(
    *,
    name: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44202067ada87cd47b3af31a51714a781d59c3a94ffe7a34b1e426ddaa87372f(
    *,
    id: builtins.str,
    account_id: typing.Optional[builtins.str] = None,
    expression: typing.Optional[builtins.str] = None,
    label: typing.Optional[builtins.str] = None,
    metric_stat: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAlarm.MetricStatProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    period: typing.Optional[jsii.Number] = None,
    return_data: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f25dbc8a0f576b492c27e93b80f26a025e8007e3b69752a846bae6af97ce55cf(
    *,
    dimensions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAlarm.DimensionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    metric_name: typing.Optional[builtins.str] = None,
    namespace: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1dccb5e7c21aab3526dfa08bb25fc1fac8540f50228147e0db89d426f59d20fe(
    *,
    metric: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAlarm.MetricProperty, typing.Dict[builtins.str, typing.Any]]],
    period: jsii.Number,
    stat: builtins.str,
    unit: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc643fb1b5f1f1f0e0d9896a5988171163c1f79adc28d1e921bdf85f14782517(
    *,
    comparison_operator: builtins.str,
    evaluation_periods: jsii.Number,
    actions_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    alarm_actions: typing.Optional[typing.Sequence[builtins.str]] = None,
    alarm_description: typing.Optional[builtins.str] = None,
    alarm_name: typing.Optional[builtins.str] = None,
    datapoints_to_alarm: typing.Optional[jsii.Number] = None,
    dimensions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAlarm.DimensionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    evaluate_low_sample_count_percentile: typing.Optional[builtins.str] = None,
    extended_statistic: typing.Optional[builtins.str] = None,
    insufficient_data_actions: typing.Optional[typing.Sequence[builtins.str]] = None,
    metric_name: typing.Optional[builtins.str] = None,
    metrics: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAlarm.MetricDataQueryProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    namespace: typing.Optional[builtins.str] = None,
    ok_actions: typing.Optional[typing.Sequence[builtins.str]] = None,
    period: typing.Optional[jsii.Number] = None,
    statistic: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    threshold: typing.Optional[jsii.Number] = None,
    threshold_metric_id: typing.Optional[builtins.str] = None,
    treat_missing_data: typing.Optional[builtins.str] = None,
    unit: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09a2ebaa31c6ab1b46831db515c9eec0f049e129318fe5ad32dd73c9e596659a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnomalyDetector.ConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    dimensions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnomalyDetector.DimensionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    metric_characteristics: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnomalyDetector.MetricCharacteristicsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    metric_math_anomaly_detector: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnomalyDetector.MetricMathAnomalyDetectorProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    metric_name: typing.Optional[builtins.str] = None,
    namespace: typing.Optional[builtins.str] = None,
    single_metric_anomaly_detector: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnomalyDetector.SingleMetricAnomalyDetectorProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    stat: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3e4e45621b2bf2b69c3fe98b2cba7744a560f297c63ceb4f36a9522a03416fb(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d95740790e1f93b73e8f89f80ba917c53d59b96d60ce701fb57c17eaeafdc94(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4577cb9dfe92537d1cc8e64146892876070d141d09590038417ae6ad98c7b32a(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAnomalyDetector.ConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa81b524032f55c8d3aa5c261568d608ed375b489e67451c339cda6dff9fdd55(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnAnomalyDetector.DimensionProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__730fad039b3befd0235c3dce81008e3d9f65ab635fe956e8ed48f3ba7060aaba(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAnomalyDetector.MetricCharacteristicsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8f418300bad7bba64cba09c0d26246445ca23587310af02c4b72408240a1db4(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAnomalyDetector.MetricMathAnomalyDetectorProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62529ca050619ba994a39e1006e0e31850759c9d38fecaa7680c69fed8dfa964(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__773837afe915f1d5b355e30c8993ab753a19fdd128100f68379277738d9ce6f3(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f79f6e93c8bc8ee29709af3c665820fb1e16318cf78b4220c7fd5bcb8a1148b8(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAnomalyDetector.SingleMetricAnomalyDetectorProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7812721bb3336919f3fffca23d863b6f1d266a939ca4c3862657da872edd822(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67352ac72587eb41e06664f1e6dbbc18d0b51da2732f4318f403896a70102121(
    *,
    excluded_time_ranges: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnomalyDetector.RangeProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    metric_time_zone: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__621384455c6fe008d1544e799a687e205dfd7c831d4d16758c94209b7b77dac9(
    *,
    name: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__782bb184e35a5f89f30dd279aa12cf0d77b7069596cc47017cd113eb386bfa0b(
    *,
    periodic_spikes: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d07af40dc753cdda4381651fa3711189e996a0d1ada4554c36c730242ecee721(
    *,
    id: builtins.str,
    account_id: typing.Optional[builtins.str] = None,
    expression: typing.Optional[builtins.str] = None,
    label: typing.Optional[builtins.str] = None,
    metric_stat: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnomalyDetector.MetricStatProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    period: typing.Optional[jsii.Number] = None,
    return_data: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe2d23d029852cd64aa565c80080a904e189f6017f7ab50f0c89da36d7c772bb(
    *,
    metric_data_queries: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnomalyDetector.MetricDataQueryProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b189668a1a93615dfd113ac1c4798293f70acd463c9a2519156d29af0bf0392(
    *,
    metric_name: builtins.str,
    namespace: builtins.str,
    dimensions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnomalyDetector.DimensionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b3d65b4810e6974d2b03459fe0fd3d8db280dcecbf37190a36d9be3e039913c(
    *,
    metric: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnomalyDetector.MetricProperty, typing.Dict[builtins.str, typing.Any]]],
    period: jsii.Number,
    stat: builtins.str,
    unit: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9bc80976f2b683f55d7e2d50a80f5b0ac541edd875fa1a1062846959cb4afa0b(
    *,
    end_time: builtins.str,
    start_time: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a262a607da9d06ac67c27003b22dd869da37f8dcb73d7c6f1f5c7524458adf0(
    *,
    account_id: typing.Optional[builtins.str] = None,
    dimensions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnomalyDetector.DimensionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    metric_name: typing.Optional[builtins.str] = None,
    namespace: typing.Optional[builtins.str] = None,
    stat: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__929a09b64f3cc2009ffca4b74d148c42dfbbc7531a49bc66cb58443f8870fba2(
    *,
    configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnomalyDetector.ConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    dimensions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnomalyDetector.DimensionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    metric_characteristics: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnomalyDetector.MetricCharacteristicsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    metric_math_anomaly_detector: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnomalyDetector.MetricMathAnomalyDetectorProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    metric_name: typing.Optional[builtins.str] = None,
    namespace: typing.Optional[builtins.str] = None,
    single_metric_anomaly_detector: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnomalyDetector.SingleMetricAnomalyDetectorProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    stat: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c24d10326e3cd470724ecbde5d50ff23fdf44dc88f809d9a181a5cd867e5cf3(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    alarm_rule: builtins.str,
    actions_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    actions_suppressor: typing.Optional[builtins.str] = None,
    actions_suppressor_extension_period: typing.Optional[jsii.Number] = None,
    actions_suppressor_wait_period: typing.Optional[jsii.Number] = None,
    alarm_actions: typing.Optional[typing.Sequence[builtins.str]] = None,
    alarm_description: typing.Optional[builtins.str] = None,
    alarm_name: typing.Optional[builtins.str] = None,
    insufficient_data_actions: typing.Optional[typing.Sequence[builtins.str]] = None,
    ok_actions: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__399fd96f9e0939b1087102f4b90094a74c88e8fdf84dcd24f4f9a6faf0d9ee93(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c792f92e772e604ae78dfb7743ace896d51e15317ab3c7188cb3c3f01b50a12a(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e343637dcbb025d59f785b38d36b2f01ca3c7a48777520e981849e0b80fefcb7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43ce9ab8aaafd96e9ff146e41c5e3921be5380953cea24e5da817be9a65afdcb(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec17e197e4085501e80806e6a6281d3058abe5cef41136d5b9adb00c43ad208a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f59b02bf7b3f38f8619d99d396adb8a199f811d2b0b285ea883b46dbc6c8093a(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc105b69ef4e4fb77cafb9a01fd07d05e35906a88000902617ddd4ff60098ce4(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68f13f2cdd6512362166f971941eb93e413522e0a7f50732f11be4849a0314b5(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba7d39bfc4a33f1e068842cf86eda6b8b89a710218c633e611c70f1c8daa97ab(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bae9a025d5364aad3383cb09745b81ba3d0a684c7d80304295a0b7f668d191b1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3202031aa3ce5a8e5bb11c41944febb49ef69bfd275589ad920d63e8166038bb(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f061adaf1332cbeeb6cedda66357d6a65aea2023583d23de2ed9b9c193d8e7e9(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__457680b612885bf2c4b88aebcb2510b437690fdf7d6235bf00d83846c1ee3452(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f61e2b790710dde8e1d3a57752c99da295b632afeb42e0870113583f0277be2c(
    *,
    alarm_rule: builtins.str,
    actions_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    actions_suppressor: typing.Optional[builtins.str] = None,
    actions_suppressor_extension_period: typing.Optional[jsii.Number] = None,
    actions_suppressor_wait_period: typing.Optional[jsii.Number] = None,
    alarm_actions: typing.Optional[typing.Sequence[builtins.str]] = None,
    alarm_description: typing.Optional[builtins.str] = None,
    alarm_name: typing.Optional[builtins.str] = None,
    insufficient_data_actions: typing.Optional[typing.Sequence[builtins.str]] = None,
    ok_actions: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5add67d5fc6c551e627bade2623b719ee8c8de03ff6216bc3471bbe529821b66(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    dashboard_body: builtins.str,
    dashboard_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea2b521a69d5f78d24dc5aba9c387baa4fc450da2dc68bb876531861ee0929b2(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ce11f5733e6656fe8931f571c3719842e64f032f829682b3282f6a1b8f67e06(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a865365ce6c92cb381923f9ec71606f45f52c25334fd65ce166ec545a411b9d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07330e06be9439e4eb97f9c714be0b2c8c09a55b7ef93d990e58a14e431f65eb(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42d47a219edd6b2c040597f718bfa93d023a9554d8079e5c8295ecd47caee4ca(
    *,
    dashboard_body: builtins.str,
    dashboard_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d177572b447b5b9761effd52cd14b4510ca4c8fc8607968bdc5e0bd8deae855(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    rule_body: builtins.str,
    rule_name: builtins.str,
    rule_state: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cba00200e260114593f7b73e5266f02b1427404baba75fd95d8aed05d7f2b685(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85b06cd7db59c69ce5f4eeed03813e201c4d3359daf90d04d6607b73d60e27cb(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e43a5d364bdee89deaa1521057666bc0592788c8b09eb4a4a1368a9983955ab9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb020ce7ae390a51012545e5480226be8351f5fa9dd387e75ff1ee669883417a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45517418d6e99e8c2af45e33f2d1375212c73bac3d2c9599691ac383edef3c3b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d330e494e47f68df8f1753b4e301d3df252f832725f14292abf5fa4ee104054(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea720192b6c423ff900f4b69425db7a31e90fed21a852500910edce4589cfb7c(
    *,
    rule_body: builtins.str,
    rule_name: builtins.str,
    rule_state: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__324083d9d1c11bed8d2cf8d1d0cab6adbcb8194552cea34115b984457ef131eb(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    firehose_arn: builtins.str,
    output_format: builtins.str,
    role_arn: builtins.str,
    exclude_filters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMetricStream.MetricStreamFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    include_filters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMetricStream.MetricStreamFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    include_linked_accounts_metrics: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    name: typing.Optional[builtins.str] = None,
    statistics_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMetricStream.MetricStreamStatisticsConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d75d145801429f4f9f0daaae66adb695e6690f2bd7b00a62aedff30952bef4c(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc4e04abbe7c420d426a886e2590972a98723e1abf197bd044bef66ef0f366ca(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__303acca869f0b2f0dd33e2a704edc1c9841d282e2c5d6fefab0857984b4a7a14(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7e65744c47b6274b336b0cab06cc0e6fd616351335054e76423aa5e24f60fdb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84ed2e0742cbeea084c4b032aceb0bc50b5b099cfab1446baec0d7580228eda5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8a010b725b9721d5a0070180f728cef097b885a9247729c230c1e48162efb49(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnMetricStream.MetricStreamFilterProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9fd63e599d47997efeead98c50e00925a352821609b2a35cc5d8286cc277d16d(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnMetricStream.MetricStreamFilterProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db935a48c332f03a24316c2a8a9a44ae9aee2c31a0f66ccbca7f9645b7f6f148(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ecec6f0d2b2483e898160ef393fb18ddcf4dd3fc4d302c943abaa1e538f6e3f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5fccdc8e5b648171c23d1254144728db070b30ea4ff96cea910d95125b8aab0(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnMetricStream.MetricStreamStatisticsConfigurationProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ff12b171ab408aef715723528314a6f2877123297d21c2d3c0cf73a13965ffe(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4de34777618ee8ff0a4cfe901b94bf76a91e50ee6a29cf6a17d55887c3348025(
    *,
    namespace: builtins.str,
    metric_names: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__014629a07843af45b16fe266381194e9a273db3a2b42bae461f897e5c6c957a9(
    *,
    additional_statistics: typing.Sequence[builtins.str],
    include_metrics: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMetricStream.MetricStreamStatisticsMetricProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd6943836e019c7fb3dffa95c2ffb1b7cb9db587bd9c145bf9373c8ff342926b(
    *,
    metric_name: builtins.str,
    namespace: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3841eb4f0098d496658caf6739d964d8b08f872e67d2ad28362ac3882ccd7d74(
    *,
    firehose_arn: builtins.str,
    output_format: builtins.str,
    role_arn: builtins.str,
    exclude_filters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMetricStream.MetricStreamFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    include_filters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMetricStream.MetricStreamFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    include_linked_accounts_metrics: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    name: typing.Optional[builtins.str] = None,
    statistics_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMetricStream.MetricStreamStatisticsConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd18f372aac3bb8d4a678dd4ee7a3b5bd34447637695b896086139ee2b7b4a19(
    *,
    account: typing.Optional[builtins.str] = None,
    color: typing.Optional[builtins.str] = None,
    dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    label: typing.Optional[builtins.str] = None,
    period: typing.Optional[_Duration_4839e8c3] = None,
    region: typing.Optional[builtins.str] = None,
    statistic: typing.Optional[builtins.str] = None,
    unit: typing.Optional[Unit] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac3983e61925a8b50987e3b6213e939907d0c4bb41a5682e1321634d8b68675b(
    *,
    alarm_rule: IAlarmRule,
    actions_enabled: typing.Optional[builtins.bool] = None,
    actions_suppressor: typing.Optional[IAlarm] = None,
    actions_suppressor_extension_period: typing.Optional[_Duration_4839e8c3] = None,
    actions_suppressor_wait_period: typing.Optional[_Duration_4839e8c3] = None,
    alarm_description: typing.Optional[builtins.str] = None,
    composite_alarm_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91617a8a8e9f459ae82e35cee9e72d7bc0040c89e7759483900a64aadd24ca0b(
    *,
    evaluation_periods: jsii.Number,
    threshold: jsii.Number,
    actions_enabled: typing.Optional[builtins.bool] = None,
    alarm_description: typing.Optional[builtins.str] = None,
    alarm_name: typing.Optional[builtins.str] = None,
    comparison_operator: typing.Optional[ComparisonOperator] = None,
    datapoints_to_alarm: typing.Optional[jsii.Number] = None,
    evaluate_low_sample_count_percentile: typing.Optional[builtins.str] = None,
    treat_missing_data: typing.Optional[TreatMissingData] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d71374eb7e9e4cb8250337037e840a61230633064256eddde7401c0a174961c(
    *,
    function_arn: builtins.str,
    title: builtins.str,
    height: typing.Optional[jsii.Number] = None,
    params: typing.Any = None,
    update_on_refresh: typing.Optional[builtins.bool] = None,
    update_on_resize: typing.Optional[builtins.bool] = None,
    update_on_time_range_change: typing.Optional[builtins.bool] = None,
    width: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6fda01df790539d40ed9b476d4407925232861deff439705940e219dc8e29020(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    dashboard_name: typing.Optional[builtins.str] = None,
    default_interval: typing.Optional[_Duration_4839e8c3] = None,
    end: typing.Optional[builtins.str] = None,
    period_override: typing.Optional[PeriodOverride] = None,
    start: typing.Optional[builtins.str] = None,
    variables: typing.Optional[typing.Sequence[IVariable]] = None,
    widgets: typing.Optional[typing.Sequence[typing.Sequence[IWidget]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1da9fa9df70a5b921eac287c4fe08d6816d2514a66f72147b77e9feea1a8a606(
    variable: IVariable,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e914386fa8a66a4e8e6cbeaa4a3f975f705962fc3be601de7228f8576e15c42d(
    *widgets: IWidget,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c41d6a8494d12ab7a95fc9ee6638b207cc78fd0aa3e36ceec570a394588d6890(
    *,
    dashboard_name: typing.Optional[builtins.str] = None,
    default_interval: typing.Optional[_Duration_4839e8c3] = None,
    end: typing.Optional[builtins.str] = None,
    period_override: typing.Optional[PeriodOverride] = None,
    start: typing.Optional[builtins.str] = None,
    variables: typing.Optional[typing.Sequence[IVariable]] = None,
    widgets: typing.Optional[typing.Sequence[typing.Sequence[IWidget]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4da4c2a317eff8c9083c9e23732734166969be3616c35a7f51e21115e260cba6(
    *,
    id: builtins.str,
    input_type: VariableInputType,
    type: VariableType,
    value: builtins.str,
    default_value: typing.Optional[DefaultValue] = None,
    label: typing.Optional[builtins.str] = None,
    values: typing.Optional[Values] = None,
    visible: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4f7631acc3b9fb4aea3e273751a2a20c7480f62e33d5789fd4938c009af2ec8(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9f1a4bef1bc9e7080c21c9fd7656533f0a327837e2ebfcb35a0338efb47ad17(
    *,
    name: builtins.str,
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__590b09336dca786909b6d40a91a4108f1ce6787811718cd6151f7cd2d8e37be9(
    *,
    value: jsii.Number,
    color: typing.Optional[builtins.str] = None,
    fill: typing.Optional[Shading] = None,
    label: typing.Optional[builtins.str] = None,
    visible: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19a88cc904e70d7841abfa1406b71edcf34c316b173c37c2881e75702bc0c75a(
    scope: _constructs_77d1e7e8.Construct,
    alarm: IAlarm,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f09026a4cce4261b0c1f425d42f625c9bd8f0ba4495e11743f621a2cd44b00f8(
    x: jsii.Number,
    y: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7d4a308b1274696259a35b14b5ae833f34881f95eaba521bb47a74b3a80e8c0(
    *,
    log_group_names: typing.Sequence[builtins.str],
    height: typing.Optional[jsii.Number] = None,
    query_lines: typing.Optional[typing.Sequence[builtins.str]] = None,
    query_string: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    title: typing.Optional[builtins.str] = None,
    view: typing.Optional[LogQueryVisualizationType] = None,
    width: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2288caf1bef913802628b6170f42c00c75c6fb8a67ec2e269d8e950bb21fbe4b(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    evaluation_periods: jsii.Number,
    threshold: jsii.Number,
    actions_enabled: typing.Optional[builtins.bool] = None,
    alarm_description: typing.Optional[builtins.str] = None,
    alarm_name: typing.Optional[builtins.str] = None,
    comparison_operator: typing.Optional[ComparisonOperator] = None,
    datapoints_to_alarm: typing.Optional[jsii.Number] = None,
    evaluate_low_sample_count_percentile: typing.Optional[builtins.str] = None,
    treat_missing_data: typing.Optional[TreatMissingData] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f28a14de04cee7a41ccdb702d4444beec1719a2620a487cbc8e934b85c29a574(
    *,
    color: typing.Optional[builtins.str] = None,
    label: typing.Optional[builtins.str] = None,
    period: typing.Optional[_Duration_4839e8c3] = None,
    search_account: typing.Optional[builtins.str] = None,
    search_region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7cfb588e44acd0977aa0e09f00c3e2435bad84385ab7b6d163b332963d844e0a(
    *,
    color: typing.Optional[builtins.str] = None,
    label: typing.Optional[builtins.str] = None,
    period: typing.Optional[_Duration_4839e8c3] = None,
    search_account: typing.Optional[builtins.str] = None,
    search_region: typing.Optional[builtins.str] = None,
    expression: builtins.str,
    using_metrics: typing.Optional[typing.Mapping[builtins.str, IMetric]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80cc2795f9742554fa1b3991c8df3ae2020ca7ee2fdc5766276d72c863b4eb74(
    grantee: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25be678fc533e02941d84f54a76d8c3b96a0229380a8181f05cf39cb522d894f(
    scope: _constructs_77d1e7e8.IConstruct,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d06465478bbcf4229dd841339de63538dcc33dff4d9dbdf0e5b10087b556a00(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    evaluation_periods: jsii.Number,
    threshold: jsii.Number,
    actions_enabled: typing.Optional[builtins.bool] = None,
    alarm_description: typing.Optional[builtins.str] = None,
    alarm_name: typing.Optional[builtins.str] = None,
    comparison_operator: typing.Optional[ComparisonOperator] = None,
    datapoints_to_alarm: typing.Optional[jsii.Number] = None,
    evaluate_low_sample_count_percentile: typing.Optional[builtins.str] = None,
    treat_missing_data: typing.Optional[TreatMissingData] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ddb584abe8421d7f77520aa621133794d500e179ff044f43970dac3fd018cca(
    *,
    math_expression: typing.Optional[typing.Union[MetricExpressionConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    metric_stat: typing.Optional[typing.Union[MetricStatConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    rendering_properties: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78c6be62e28f1743856b4fd66c3982e1e250f21015b1ed9d4e038be59f0d4fde(
    *,
    expression: builtins.str,
    period: jsii.Number,
    using_metrics: typing.Mapping[builtins.str, IMetric],
    search_account: typing.Optional[builtins.str] = None,
    search_region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0dbe737a4d124c27184430b7c20048e16171cb8b5b94bdac632b26d8480d8116(
    *,
    account: typing.Optional[builtins.str] = None,
    color: typing.Optional[builtins.str] = None,
    dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    label: typing.Optional[builtins.str] = None,
    period: typing.Optional[_Duration_4839e8c3] = None,
    region: typing.Optional[builtins.str] = None,
    statistic: typing.Optional[builtins.str] = None,
    unit: typing.Optional[Unit] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e1e153a11ab88ed91297aedb5d7a78a81e7bf88f8aeda51bc11ff42ebe01d74(
    *,
    account: typing.Optional[builtins.str] = None,
    color: typing.Optional[builtins.str] = None,
    dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    label: typing.Optional[builtins.str] = None,
    period: typing.Optional[_Duration_4839e8c3] = None,
    region: typing.Optional[builtins.str] = None,
    statistic: typing.Optional[builtins.str] = None,
    unit: typing.Optional[Unit] = None,
    metric_name: builtins.str,
    namespace: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4491ad5e5a4b9301258f50e45d0278fe9bbf165c840e3c65f8feab639322bae(
    *,
    metric_name: builtins.str,
    namespace: builtins.str,
    period: _Duration_4839e8c3,
    statistic: builtins.str,
    account: typing.Optional[builtins.str] = None,
    dimensions: typing.Optional[typing.Sequence[typing.Union[Dimension, typing.Dict[builtins.str, typing.Any]]]] = None,
    region: typing.Optional[builtins.str] = None,
    unit_filter: typing.Optional[Unit] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__028d2c6eccbbf06b74566403b038cac0cdc1c8588c939f4352cc861885b12c38(
    *,
    height: typing.Optional[jsii.Number] = None,
    region: typing.Optional[builtins.str] = None,
    title: typing.Optional[builtins.str] = None,
    width: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40733d2619229fa61f0179677abbedccf016612d902783aeea0675549c61429e(
    *widgets: IWidget,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be1559e21caabf749b14d57eaa513451f7692532be8e10362f6f35a8d79f522e(
    w: IWidget,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16ac800c3f04ad1be947a2de94d65265cf3e61d41b3ef93dc1a1a64706b3c07f(
    x: jsii.Number,
    y: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__834c69a269555056b1b73146ff2784af68174eb591f39133c585607049d7afe7(
    *,
    dimensions: typing.Sequence[builtins.str],
    metric_name: builtins.str,
    namespace: builtins.str,
    populate_from: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4596565f40195bdcc9fe939fa585a3bdf484f8a4a6817e427c6f9e1e49650041(
    *,
    height: typing.Optional[jsii.Number] = None,
    region: typing.Optional[builtins.str] = None,
    title: typing.Optional[builtins.str] = None,
    width: typing.Optional[jsii.Number] = None,
    metrics: typing.Sequence[IMetric],
    end: typing.Optional[builtins.str] = None,
    full_precision: typing.Optional[builtins.bool] = None,
    period: typing.Optional[_Duration_4839e8c3] = None,
    set_period_to_time_range: typing.Optional[builtins.bool] = None,
    sparkline: typing.Optional[builtins.bool] = None,
    start: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0236fe592a65d0a71aaf6677c75eec030eb736094a2786b8e76b8268bf9a92ed(
    _x: jsii.Number,
    _y: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ce130b788b85b7cf4858285014ef18ed05d407efad51e70fc325d771e03cd07(
    *,
    height: typing.Optional[jsii.Number] = None,
    width: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6fe6b13717c2f469cb6495af37c0676d3baf89c7971d1f4421f83fb8386423c5(
    percentile: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b20618ea2205ed15f0a41b04678afac5b1c065f0b533015b7b38bc29faf2d28f(
    percentile: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c9c42984ea88c4bfe005c7b416b3bc4f37f123fcb4179c31c52608b1d17d6ad(
    v1: jsii.Number,
    v2: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a8709abf45bdade8c71c455bb23d9992475641bb192922b080e052213ff7a2d(
    v1: jsii.Number,
    v2: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a59697bf582c1a9d2cf797a3831d238c515f86f8b25fa39d523b89bc479ee7b(
    p1: jsii.Number,
    p2: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f436c4f45d1d4c4b619c5d92a59806b069fccea9b744eb05a1a8a63d5fad1bc1(
    p1: jsii.Number,
    p2: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4039f2f3dc599b3ff76634eaaa717bb526fa7c9790b7eb4d412a7860ef92c6c8(
    p1: jsii.Number,
    p2: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a459a1d21547ef8c2ced058c40dc9c19552a9b7c47f0c98c4f674eea7415c1b4(
    p1: jsii.Number,
    p2: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b907dc76d7f5d30c86b61f5d0bc18c4c525bb2d23f21bb493c2c59eb8918a669(
    p1: jsii.Number,
    p2: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b47525d73a908d3fb5feeddc346925ac46e91b28aeb372a1d789770b4b54554b(
    p1: jsii.Number,
    p2: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56e0f0610a2a67b4632bbdfee23cd7509fcd0e93b34d23c36208dc99ac803774(
    p1: jsii.Number,
    p2: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1740e870895a9795d40caa429b748dd124ed575f6ae4335284294f42209ae324(
    p1: jsii.Number,
    p2: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98c18eab758ffae376ffa1675e2524ad60cd0a50fd033fe135c6d98d0f5d2692(
    *,
    columns: typing.Optional[typing.Sequence[TableSummaryColumn]] = None,
    hide_non_summary_columns: typing.Optional[builtins.bool] = None,
    sticky: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70d2d8bf527174c0069d64738e83c5ebe4fd927ac2332ac0de67140546fb8616(
    value: jsii.Number,
    color: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6f92993218488cf545481e8167442910bb8b8c7c45aa7dfb6667808cb1077e6(
    value: jsii.Number,
    color: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__837fdebf81b3f53de6d99624ebde152b4aba1d764a0cc2bd930440701533924a(
    lower_bound: jsii.Number,
    upper_bound: jsii.Number,
    color: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03726ba90bb01c2a1340af4f73005fffe1b8288cff57d77f31d745d629defb8b(
    *,
    height: typing.Optional[jsii.Number] = None,
    region: typing.Optional[builtins.str] = None,
    title: typing.Optional[builtins.str] = None,
    width: typing.Optional[jsii.Number] = None,
    end: typing.Optional[builtins.str] = None,
    full_precision: typing.Optional[builtins.bool] = None,
    layout: typing.Optional[TableLayout] = None,
    live_data: typing.Optional[builtins.bool] = None,
    metrics: typing.Optional[typing.Sequence[IMetric]] = None,
    period: typing.Optional[_Duration_4839e8c3] = None,
    set_period_to_time_range: typing.Optional[builtins.bool] = None,
    show_units_in_label: typing.Optional[builtins.bool] = None,
    start: typing.Optional[builtins.str] = None,
    statistic: typing.Optional[builtins.str] = None,
    summary: typing.Optional[typing.Union[TableSummaryProps, typing.Dict[builtins.str, typing.Any]]] = None,
    thresholds: typing.Optional[typing.Sequence[TableThreshold]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c678c9d6bdc1a1e852f5260a40406f2e09cfc10b899093e99e66b9998d086d5e(
    *,
    markdown: builtins.str,
    background: typing.Optional[TextWidgetBackground] = None,
    height: typing.Optional[jsii.Number] = None,
    width: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afe23853ba6c48e47b97d468ea15f87c9bfe3b880732f11d19570ed0895f18ca(
    expression: builtins.str,
    populate_from: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad2d8863dfb0f396c5d69f43fdc7137d8386cc972baa88ad212df48bbc5c3e6c(
    *values: VariableValue,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03c9a6d1a1a0197c51468b97744230720e131da2f17bd50bfcfa9f7a3b4092cb(
    *,
    value: builtins.str,
    label: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c903f8a4aafff9c3e6b2539c8372df8551aba4035bb4187c0e0930b0ee60ff00(
    *,
    date: builtins.str,
    color: typing.Optional[builtins.str] = None,
    fill: typing.Optional[VerticalShading] = None,
    label: typing.Optional[builtins.str] = None,
    visible: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec63852e8e70001b1e7a1554d96ad9ddb32bcfee6e3c022b5ba672bf9259a3be(
    *,
    label: typing.Optional[builtins.str] = None,
    max: typing.Optional[jsii.Number] = None,
    min: typing.Optional[jsii.Number] = None,
    show_units: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2e7c873c118fbc1f6cf26e1bb5bd3d8549040c626a6450f2d686bb07b87266b(
    *,
    evaluation_periods: jsii.Number,
    threshold: jsii.Number,
    actions_enabled: typing.Optional[builtins.bool] = None,
    alarm_description: typing.Optional[builtins.str] = None,
    alarm_name: typing.Optional[builtins.str] = None,
    comparison_operator: typing.Optional[ComparisonOperator] = None,
    datapoints_to_alarm: typing.Optional[jsii.Number] = None,
    evaluate_low_sample_count_percentile: typing.Optional[builtins.str] = None,
    treat_missing_data: typing.Optional[TreatMissingData] = None,
    metric: IMetric,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b6bef2cc64a78bffd68dc95a764829a6c125294deaebcd42b56c493541573d5(
    *,
    height: typing.Optional[jsii.Number] = None,
    region: typing.Optional[builtins.str] = None,
    title: typing.Optional[builtins.str] = None,
    width: typing.Optional[jsii.Number] = None,
    alarm: IAlarm,
    left_y_axis: typing.Optional[typing.Union[YAxisProps, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76ce8e89badc991e6248d5096f1d0b7ed5c9b4e588f4383e932e8f87c07043c6(
    *widgets: IWidget,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e7a63a93df283f275f6e4f6eea63f6665322c9a990c8c8aa9db71dd89fe730e(
    w: IWidget,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be386baa88e2f34ab4e89e312e9a044e57596f584e0dc58e3e0de3089771cbf5(
    x: jsii.Number,
    y: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5472697255361cd3423eece6fc66536dcf7e58a80d3801bec6331d231c9e36d(
    width: jsii.Number,
    height: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5ae2d5f50f7532d79ca7e346e91f137e37e297127e588b21f681019986b1c55(
    *ms: IMetric,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e0f6387845c9d7953cfc1de766c2a56f8bb9fb94f5c273ed272288b546b4392(
    x: jsii.Number,
    y: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6a944db25b0c1533973a41edef1a431615645e2f5fcbcc1e577c331d33bb0ff(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81266f4e20969db506e61dedc6af36fce6fe0f75af699f49b5c6f11f9225bef2(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11f194bd6989eaa4279174f388eb1c44a7faf424b684d189ffe90647dfd0eeb2(
    metric: IMetric,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1f8fe2511861f7fc6d2225bf5821fc9134b7036355dffb1d0ddd86a99b53dc5(
    *,
    height: typing.Optional[jsii.Number] = None,
    region: typing.Optional[builtins.str] = None,
    title: typing.Optional[builtins.str] = None,
    width: typing.Optional[jsii.Number] = None,
    annotations: typing.Optional[typing.Sequence[typing.Union[HorizontalAnnotation, typing.Dict[builtins.str, typing.Any]]]] = None,
    end: typing.Optional[builtins.str] = None,
    left_y_axis: typing.Optional[typing.Union[YAxisProps, typing.Dict[builtins.str, typing.Any]]] = None,
    legend_position: typing.Optional[LegendPosition] = None,
    live_data: typing.Optional[builtins.bool] = None,
    metrics: typing.Optional[typing.Sequence[IMetric]] = None,
    period: typing.Optional[_Duration_4839e8c3] = None,
    set_period_to_time_range: typing.Optional[builtins.bool] = None,
    start: typing.Optional[builtins.str] = None,
    statistic: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78a36122d01bdf3dadbdef1806a83ff151cd1d77de21139074c37ca284275e0e(
    metric: IMetric,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d98276ba6bbea7a9a5b2efedfda4a862eeca9b42a2aaca743679984a15762407(
    metric: IMetric,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3471ad100c9e34a517506d76368276ef9b137a3c7b33aecc91910b5dc9263b3b(
    *,
    height: typing.Optional[jsii.Number] = None,
    region: typing.Optional[builtins.str] = None,
    title: typing.Optional[builtins.str] = None,
    width: typing.Optional[jsii.Number] = None,
    end: typing.Optional[builtins.str] = None,
    left: typing.Optional[typing.Sequence[IMetric]] = None,
    left_annotations: typing.Optional[typing.Sequence[typing.Union[HorizontalAnnotation, typing.Dict[builtins.str, typing.Any]]]] = None,
    left_y_axis: typing.Optional[typing.Union[YAxisProps, typing.Dict[builtins.str, typing.Any]]] = None,
    legend_position: typing.Optional[LegendPosition] = None,
    live_data: typing.Optional[builtins.bool] = None,
    period: typing.Optional[_Duration_4839e8c3] = None,
    right: typing.Optional[typing.Sequence[IMetric]] = None,
    right_annotations: typing.Optional[typing.Sequence[typing.Union[HorizontalAnnotation, typing.Dict[builtins.str, typing.Any]]]] = None,
    right_y_axis: typing.Optional[typing.Union[YAxisProps, typing.Dict[builtins.str, typing.Any]]] = None,
    set_period_to_time_range: typing.Optional[builtins.bool] = None,
    stacked: typing.Optional[builtins.bool] = None,
    start: typing.Optional[builtins.str] = None,
    statistic: typing.Optional[builtins.str] = None,
    vertical_annotations: typing.Optional[typing.Sequence[typing.Union[VerticalAnnotation, typing.Dict[builtins.str, typing.Any]]]] = None,
    view: typing.Optional[GraphWidgetView] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14b284f52f62e4bb0b4243fb3b3bcaa2693e6ee107b2721f9467d31d81cf408b(
    metric: IMetric,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8d51865c110b61caff6f389abfdbc4862eb4488d27c9b39083e0293fd0be343(
    x: jsii.Number,
    y: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e7154d8d457acf3b0cf78ed544360096e7c3981ec43306ad2f509853c4efe1b(
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

def _typecheckingstub__bbc62cbd9f9d10401db80f46c6d4b0e4a15c97163470cbdd2dd91c82b5a76c38(
    *actions: IAlarmAction,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e588099840d4554b8e9faf3cc33868d492f714f24d214d9f770291fb25fad20(
    *actions: IAlarmAction,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f195fe021c2d9115ee79498e038ce63454be2e0d319995ca3a3d767feb45dab(
    *actions: IAlarmAction,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f77158cf05762b87148c9ece7c4fc0f4591bc620078d7052247bf9fa5146bbe8(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e28ecf3733272408c8625c4e9726b39ea586c58f4c89c08d7ba8579a99a5247(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32c054ee1bf96f6ce4073fc60bc6e30b8c1c7d0fe7f902e814f6554b6ee36a71(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1fc0a3126fa9c8844de1784e81a9f4f3230086511ca9713ee2ff0d042663da5f(
    x: jsii.Number,
    y: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7a7ea1ddc8fb0690826832fbc77c405acacd10123a1aa81696d3863d8252abb(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    alarm_rule: IAlarmRule,
    actions_enabled: typing.Optional[builtins.bool] = None,
    actions_suppressor: typing.Optional[IAlarm] = None,
    actions_suppressor_extension_period: typing.Optional[_Duration_4839e8c3] = None,
    actions_suppressor_wait_period: typing.Optional[_Duration_4839e8c3] = None,
    alarm_description: typing.Optional[builtins.str] = None,
    composite_alarm_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dfb039403469bae811c18af1008f632188c3f4e24312b57fe3c23c7e5e1405fc(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    composite_alarm_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7b77df6004a58e1183aacd1214d4fe5762c7287cc2361f2ff0337e84ccbb6b3(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    composite_alarm_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41e461c6171d2c06570e53eaf2dc07ca5b3d80e0feb2f773d23b3dd8e3826382(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    metric: IMetric,
    evaluation_periods: jsii.Number,
    threshold: jsii.Number,
    actions_enabled: typing.Optional[builtins.bool] = None,
    alarm_description: typing.Optional[builtins.str] = None,
    alarm_name: typing.Optional[builtins.str] = None,
    comparison_operator: typing.Optional[ComparisonOperator] = None,
    datapoints_to_alarm: typing.Optional[jsii.Number] = None,
    evaluate_low_sample_count_percentile: typing.Optional[builtins.str] = None,
    treat_missing_data: typing.Optional[TreatMissingData] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8a5a6150e68ee9e26c8b7ebe6f92594c12f9b3cda4195d76462b991008c92b5(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    alarm_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f69e87f80e55b26f710e5c03872b4814d854ded266dd530cb19c3aeb9cae0b2(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    alarm_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35e42b79cd71f370c96d9123c26abff1c323e3360845e3957f3fa6b0bb344dde(
    *actions: IAlarmAction,
) -> None:
    """Type checking stubs"""
    pass
