'''
# Amazon CloudWatch Synthetics Construct Library

Amazon CloudWatch Synthetics allow you to monitor your application by generating **synthetic** traffic. The traffic is produced by a **canary**: a configurable script that runs on a schedule. You configure the canary script to follow the same routes and perform the same actions as a user, which allows you to continually verify your user experience even when you don't have any traffic on your applications.

## Canary

To illustrate how to use a canary, assume your application defines the following endpoint:

```console
% curl "https://api.example.com/user/books/topbook/"
The Hitchhikers Guide to the Galaxy
```

The below code defines a canary that will hit the `books/topbook` endpoint every 5 minutes:

```python
canary = synthetics.Canary(self, "MyCanary",
    schedule=synthetics.Schedule.rate(Duration.minutes(5)),
    test=synthetics.Test.custom(
        code=synthetics.Code.from_asset(path.join(__dirname, "canary")),
        handler="index.handler"
    ),
    runtime=synthetics.Runtime.SYNTHETICS_NODEJS_PUPPETEER_6_2,
    environment_variables={
        "stage": "prod"
    }
)
```

The following is an example of an `index.js` file which exports the `handler` function:

```js
const synthetics = require('Synthetics');
const log = require('SyntheticsLogger');

const pageLoadBlueprint = async function () {
  // Configure the stage of the API using environment variables
  const url = `https://api.example.com/${process.env.stage}/user/books/topbook/`;

  const page = await synthetics.getPage();
  const response = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 30000 });
  // Wait for page to render. Increase or decrease wait time based on endpoint being monitored.
  await page.waitFor(15000);
  // This will take a screenshot that will be included in test output artifacts.
  await synthetics.takeScreenshot('loaded', 'loaded');
  const pageTitle = await page.title();
  log.info('Page title: ' + pageTitle);
  if (response.status() !== 200) {
    throw 'Failed to load page!';
  }
};

exports.handler = async () => {
  return await pageLoadBlueprint();
};
```

> **Note:** The function **must** be called `handler`.

The canary will automatically produce a CloudWatch Dashboard:

![UI Screenshot](images/ui-screenshot.png)

The Canary code will be executed in a lambda function created by Synthetics on your behalf. The Lambda function includes a custom [runtime](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Library.html) provided by Synthetics. The provided runtime includes a variety of handy tools such as [Puppeteer](https://www.npmjs.com/package/puppeteer-core) (for nodejs based one) and Chromium.

To learn more about Synthetics capabilities, check out the [docs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html).

### Canary Schedule

You can specify the schedule on which a canary runs by providing a
[`Schedule`](https://docs.aws.amazon.com/cdk/api/latest/docs/@aws-cdk_aws-synthetics.Schedule.html)
object to the `schedule` property.

Configure a run rate of up to 60 minutes with `Schedule.rate`:

```python
schedule = synthetics.Schedule.rate(Duration.minutes(5))
```

You can also specify a [cron expression](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_cron.html) with `Schedule.cron`:

```python
schedule = synthetics.Schedule.cron(
    hour="0,8,16"
)
```

If you want the canary to run just once upon deployment, you can use `Schedule.once()`.

### Deleting underlying resources on canary deletion

When you delete a lambda, the following underlying resources are isolated in your AWS account:

* Lambda Function that runs your canary script
* S3 Bucket for artifact storage
* IAM roles and policies
* Log Groups in CloudWatch Logs.

To learn more about these underlying resources, see
[Synthetics Canaries Deletion](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/synthetics_canaries_deletion.html).

In the CDK, you can configure your canary to delete the underlying lambda function when the canary is deleted.
This can be provisioned by setting `cleanup: Cleanup.LAMBDA`. Note that this
will create a custom resource under the hood that takes care of the lambda deletion for you.

```python
canary = synthetics.Canary(self, "Canary",
    test=synthetics.Test.custom(
        handler="index.handler",
        code=synthetics.Code.from_inline("/* Synthetics handler code")
    ),
    cleanup=synthetics.Cleanup.LAMBDA,
    runtime=synthetics.Runtime.SYNTHETICS_NODEJS_PUPPETEER_6_2
)
```

> Note: To properly clean up your canary on deletion, you still have to manually delete other resources
> like S3 buckets and CloudWatch logs.

### Configuring the Canary Script

To configure the script the canary executes, use the `test` property. The `test` property accepts a `Test` instance that can be initialized by the `Test` class static methods. Currently, the only implemented method is `Test.custom()`, which allows you to bring your own code. In the future, other methods will be added. `Test.custom()` accepts `code` and `handler` properties -- both are required by Synthetics to create a lambda function on your behalf.

The `synthetics.Code` class exposes static methods to bundle your code artifacts:

* `code.fromInline(code)` - specify an inline script.
* `code.fromAsset(path)` - specify a .zip file or a directory in the local filesystem which will be zipped and uploaded to S3 on deployment. See the above Note for directory structure.
* `code.fromBucket(bucket, key[, objectVersion])` - specify an S3 object that contains the .zip file of your runtime code. See the above Note for directory structure.

Using the `Code` class static initializers:

```python
# To supply the code from a S3 bucket:
import aws_cdk.aws_s3 as s3
# To supply the code inline:
synthetics.Canary(self, "Inline Canary",
    test=synthetics.Test.custom(
        code=synthetics.Code.from_inline("/* Synthetics handler code */"),
        handler="index.handler"
    ),
    runtime=synthetics.Runtime.SYNTHETICS_NODEJS_PUPPETEER_6_2
)

# To supply the code from your local filesystem:
synthetics.Canary(self, "Asset Canary",
    test=synthetics.Test.custom(
        code=synthetics.Code.from_asset(path.join(__dirname, "canary")),
        handler="index.handler"
    ),
    runtime=synthetics.Runtime.SYNTHETICS_NODEJS_PUPPETEER_6_2
)
bucket = s3.Bucket(self, "Code Bucket")
synthetics.Canary(self, "Bucket Canary",
    test=synthetics.Test.custom(
        code=synthetics.Code.from_bucket(bucket, "canary.zip"),
        handler="index.handler"
    ),
    runtime=synthetics.Runtime.SYNTHETICS_NODEJS_PUPPETEER_6_2
)
```

> **Note:** Synthetics have a specified folder structure for canaries. For Node scripts supplied via `code.fromAsset()` or `code.fromBucket()`, the canary resource requires the following folder structure:
>
> ```plaintext
> canary/
> ├── nodejs/
>    ├── node_modules/
>         ├── <filename>.js
> ```
>
> For Python scripts supplied via `code.fromAsset()` or `code.fromBucket()`, the canary resource requires the following folder structure:
>
> ```plaintext
> canary/
> ├── python/
>     ├── <filename>.py
> ```
>
> See Synthetics [docs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_WritingCanary.html).

### Running a canary on a VPC

You can specify what [VPC a canary executes in](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_VPC.html).
This can allow for monitoring services that may be internal to a specific VPC. To place a canary within a VPC, you can specify the `vpc` property with the desired `VPC` to place then canary in.
This will automatically attach the appropriate IAM permissions to attach to the VPC. This will also create a Security Group and attach to the default subnets for the VPC unless specified via `vpcSubnets` and `securityGroups`.

```python
import aws_cdk.aws_ec2 as ec2

# vpc: ec2.IVpc

synthetics.Canary(self, "Vpc Canary",
    test=synthetics.Test.custom(
        code=synthetics.Code.from_asset(path.join(__dirname, "canary")),
        handler="index.handler"
    ),
    runtime=synthetics.Runtime.SYNTHETICS_NODEJS_PUPPETEER_6_2,
    vpc=vpc
)
```

> **Note:** By default, the Synthetics runtime needs access to the S3 and CloudWatch APIs, which will fail in a private subnet without internet access enabled (e.g. an isolated subnnet).
>
> Ensure that the Canary is placed in a VPC either with internet connectivity or with VPC Endpoints for S3 and CloudWatch enabled and configured.
>
> See [Synthetics VPC docs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_VPC.html).

### Alarms

You can configure a CloudWatch Alarm on a canary metric. Metrics are emitted by CloudWatch automatically and can be accessed by the following APIs:

* `canary.metricSuccessPercent()` - percentage of successful canary runs over a given time
* `canary.metricDuration()` - how much time each canary run takes, in seconds.
* `canary.metricFailed()` - number of failed canary runs over a given time

Create an alarm that tracks the canary metric:

```python
import aws_cdk.aws_cloudwatch as cloudwatch

# canary: synthetics.Canary

cloudwatch.Alarm(self, "CanaryAlarm",
    metric=canary.metric_success_percent(),
    evaluation_periods=2,
    threshold=90,
    comparison_operator=cloudwatch.ComparisonOperator.LESS_THAN_THRESHOLD
)
```

### Artifacts

You can pass an S3 bucket to store artifacts from canary runs. If you do not,
one will be auto-generated when the canary is created. You may add
[lifecycle rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html)
to the auto-generated bucket.

```python
canary = synthetics.Canary(self, "MyCanary",
    schedule=synthetics.Schedule.rate(Duration.minutes(5)),
    test=synthetics.Test.custom(
        code=synthetics.Code.from_asset(path.join(__dirname, "canary")),
        handler="index.handler"
    ),
    runtime=synthetics.Runtime.SYNTHETICS_NODEJS_PUPPETEER_6_2,
    artifacts_bucket_lifecycle_rules=[LifecycleRule(
        expiration=Duration.days(30)
    )]
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
    AssetHashType as _AssetHashType_05b67f2d,
    BundlingOptions as _BundlingOptions_588cc936,
    CfnResource as _CfnResource_9df397a6,
    CfnTag as _CfnTag_f6864754,
    Duration as _Duration_4839e8c3,
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    ITaggable as _ITaggable_36806126,
    IgnoreMode as _IgnoreMode_655a98e8,
    Resource as _Resource_45bc6135,
    SymlinkFollowMode as _SymlinkFollowMode_047ec1f6,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)
from ..aws_cloudwatch import (
    Metric as _Metric_e396a4dc,
    MetricOptions as _MetricOptions_1788b62f,
    Unit as _Unit_61bc6f70,
)
from ..aws_ec2 import (
    Connections as _Connections_0f31fce8,
    IConnectable as _IConnectable_10015a05,
    ISecurityGroup as _ISecurityGroup_acf8a799,
    IVpc as _IVpc_f30d5663,
    SubnetSelection as _SubnetSelection_e57d76df,
)
from ..aws_iam import IGrantable as _IGrantable_71c4f5de, IRole as _IRole_235f5d8e
from ..aws_s3 import (
    IBucket as _IBucket_42e086fd,
    LifecycleRule as _LifecycleRule_bb74e6ff,
    Location as _Location_0948fa7f,
)
from ..aws_s3_assets import AssetOptions as _AssetOptions_2aa69621


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_synthetics.ArtifactsBucketLocation",
    jsii_struct_bases=[],
    name_mapping={"bucket": "bucket", "prefix": "prefix"},
)
class ArtifactsBucketLocation:
    def __init__(
        self,
        *,
        bucket: _IBucket_42e086fd,
        prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Options for specifying the s3 location that stores the data of each canary run.

        The artifacts bucket location **cannot**
        be updated once the canary is created.

        :param bucket: The s3 location that stores the data of each run.
        :param prefix: The S3 bucket prefix. Specify this if you want a more specific path within the artifacts bucket. Default: - no prefix

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_s3 as s3
            from aws_cdk import aws_synthetics as synthetics
            
            # bucket: s3.Bucket
            
            artifacts_bucket_location = synthetics.ArtifactsBucketLocation(
                bucket=bucket,
            
                # the properties below are optional
                prefix="prefix"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3f4adf0ebd4ec63bde8a045a448259a907ff7a524c6a3b4503e1797b05a9d5f)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bucket": bucket,
        }
        if prefix is not None:
            self._values["prefix"] = prefix

    @builtins.property
    def bucket(self) -> _IBucket_42e086fd:
        '''The s3 location that stores the data of each run.'''
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return typing.cast(_IBucket_42e086fd, result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''The S3 bucket prefix.

        Specify this if you want a more specific path within the artifacts bucket.

        :default: - no prefix
        '''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ArtifactsBucketLocation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IConnectable_10015a05)
class Canary(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_synthetics.Canary",
):
    '''Define a new Canary.

    :exampleMetadata: infused

    Example::

        canary = synthetics.Canary(self, "MyCanary",
            schedule=synthetics.Schedule.rate(Duration.minutes(5)),
            test=synthetics.Test.custom(
                code=synthetics.Code.from_asset(path.join(__dirname, "canary")),
                handler="index.handler"
            ),
            runtime=synthetics.Runtime.SYNTHETICS_NODEJS_PUPPETEER_6_2,
            environment_variables={
                "stage": "prod"
            }
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        runtime: "Runtime",
        test: "Test",
        artifacts_bucket_lifecycle_rules: typing.Optional[typing.Sequence[typing.Union[_LifecycleRule_bb74e6ff, typing.Dict[builtins.str, typing.Any]]]] = None,
        artifacts_bucket_location: typing.Optional[typing.Union[ArtifactsBucketLocation, typing.Dict[builtins.str, typing.Any]]] = None,
        canary_name: typing.Optional[builtins.str] = None,
        cleanup: typing.Optional["Cleanup"] = None,
        environment_variables: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        failure_retention_period: typing.Optional[_Duration_4839e8c3] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
        schedule: typing.Optional["Schedule"] = None,
        security_groups: typing.Optional[typing.Sequence[_ISecurityGroup_acf8a799]] = None,
        start_after_creation: typing.Optional[builtins.bool] = None,
        success_retention_period: typing.Optional[_Duration_4839e8c3] = None,
        time_to_live: typing.Optional[_Duration_4839e8c3] = None,
        vpc: typing.Optional[_IVpc_f30d5663] = None,
        vpc_subnets: typing.Optional[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param runtime: Specify the runtime version to use for the canary.
        :param test: The type of test that you want your canary to run. Use ``Test.custom()`` to specify the test to run.
        :param artifacts_bucket_lifecycle_rules: Lifecycle rules for the generated canary artifact bucket. Has no effect if a bucket is passed to ``artifactsBucketLocation``. If you pass a bucket to ``artifactsBucketLocation``, you can add lifecycle rules to the bucket itself. Default: - no rules applied to the generated bucket.
        :param artifacts_bucket_location: The s3 location that stores the data of the canary runs. Default: - A new s3 bucket will be created without a prefix.
        :param canary_name: The name of the canary. Be sure to give it a descriptive name that distinguishes it from other canaries in your account. Do not include secrets or proprietary information in your canary name. The canary name makes up part of the canary ARN, which is included in outbound calls over the internet. Default: - A unique name will be generated from the construct ID
        :param cleanup: Specify the underlying resources to be cleaned up when the canary is deleted. Using ``Cleanup.LAMBDA`` will create a Custom Resource to achieve this. Default: Cleanup.NOTHING
        :param environment_variables: Key-value pairs that the Synthetics caches and makes available for your canary scripts. Use environment variables to apply configuration changes, such as test and production environment configurations, without changing your Canary script source code. Default: - No environment variables.
        :param failure_retention_period: How many days should failed runs be retained. Default: Duration.days(31)
        :param role: Canary execution role. This is the role that will be assumed by the canary upon execution. It controls the permissions that the canary will have. The role must be assumable by the AWS Lambda service principal. If not supplied, a role will be created with all the required permissions. If you provide a Role, you must add the required permissions. Default: - A unique role will be generated for this canary. You can add permissions to roles by calling 'addToRolePolicy'.
        :param schedule: Specify the schedule for how often the canary runs. For example, if you set ``schedule`` to ``rate(10 minutes)``, then the canary will run every 10 minutes. You can set the schedule with ``Schedule.rate(Duration)`` (recommended) or you can specify an expression using ``Schedule.expression()``. Default: 'rate(5 minutes)'
        :param security_groups: The list of security groups to associate with the canary's network interfaces. You must provide ``vpc`` when using this prop. Default: - If the canary is placed within a VPC and a security group is not specified a dedicated security group will be created for this canary.
        :param start_after_creation: Whether or not the canary should start after creation. Default: true
        :param success_retention_period: How many days should successful runs be retained. Default: Duration.days(31)
        :param time_to_live: How long the canary will be in a 'RUNNING' state. For example, if you set ``timeToLive`` to be 1 hour and ``schedule`` to be ``rate(10 minutes)``, your canary will run at 10 minute intervals for an hour, for a total of 6 times. Default: - no limit
        :param vpc: The VPC where this canary is run. Specify this if the canary needs to access resources in a VPC. Default: - Not in VPC
        :param vpc_subnets: Where to place the network interfaces within the VPC. You must provide ``vpc`` when using this prop. Default: - the Vpc default strategy if not specified
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3b6d76e5f93e31884e16cc00a9b4fc93e6782ff7db09c74aa1ef9346f53ccb0)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CanaryProps(
            runtime=runtime,
            test=test,
            artifacts_bucket_lifecycle_rules=artifacts_bucket_lifecycle_rules,
            artifacts_bucket_location=artifacts_bucket_location,
            canary_name=canary_name,
            cleanup=cleanup,
            environment_variables=environment_variables,
            failure_retention_period=failure_retention_period,
            role=role,
            schedule=schedule,
            security_groups=security_groups,
            start_after_creation=start_after_creation,
            success_retention_period=success_retention_period,
            time_to_live=time_to_live,
            vpc=vpc,
            vpc_subnets=vpc_subnets,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="metricDuration")
    def metric_duration(
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
        '''Measure the Duration of a single canary run, in seconds.

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
        options = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricDuration", [options]))

    @jsii.member(jsii_name="metricFailed")
    def metric_failed(
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
        '''Measure the number of failed canary runs over a given time period.

        Default: sum over 5 minutes

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        '''
        options = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricFailed", [options]))

    @jsii.member(jsii_name="metricSuccessPercent")
    def metric_success_percent(
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
        '''Measure the percentage of successful canary runs.

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
        options = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricSuccessPercent", [options]))

    @builtins.property
    @jsii.member(jsii_name="artifactsBucket")
    def artifacts_bucket(self) -> _IBucket_42e086fd:
        '''Bucket where data from each canary run is stored.'''
        return typing.cast(_IBucket_42e086fd, jsii.get(self, "artifactsBucket"))

    @builtins.property
    @jsii.member(jsii_name="canaryId")
    def canary_id(self) -> builtins.str:
        '''The canary ID.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "canaryId"))

    @builtins.property
    @jsii.member(jsii_name="canaryName")
    def canary_name(self) -> builtins.str:
        '''The canary Name.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "canaryName"))

    @builtins.property
    @jsii.member(jsii_name="canaryState")
    def canary_state(self) -> builtins.str:
        '''The state of the canary.

        For example, 'RUNNING', 'STOPPED', 'NOT STARTED', or 'ERROR'.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "canaryState"))

    @builtins.property
    @jsii.member(jsii_name="connections")
    def connections(self) -> _Connections_0f31fce8:
        '''Access the Connections object.

        Will fail if not a VPC-enabled Canary
        '''
        return typing.cast(_Connections_0f31fce8, jsii.get(self, "connections"))

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> _IRole_235f5d8e:
        '''Execution role associated with this Canary.'''
        return typing.cast(_IRole_235f5d8e, jsii.get(self, "role"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_synthetics.CanaryProps",
    jsii_struct_bases=[],
    name_mapping={
        "runtime": "runtime",
        "test": "test",
        "artifacts_bucket_lifecycle_rules": "artifactsBucketLifecycleRules",
        "artifacts_bucket_location": "artifactsBucketLocation",
        "canary_name": "canaryName",
        "cleanup": "cleanup",
        "environment_variables": "environmentVariables",
        "failure_retention_period": "failureRetentionPeriod",
        "role": "role",
        "schedule": "schedule",
        "security_groups": "securityGroups",
        "start_after_creation": "startAfterCreation",
        "success_retention_period": "successRetentionPeriod",
        "time_to_live": "timeToLive",
        "vpc": "vpc",
        "vpc_subnets": "vpcSubnets",
    },
)
class CanaryProps:
    def __init__(
        self,
        *,
        runtime: "Runtime",
        test: "Test",
        artifacts_bucket_lifecycle_rules: typing.Optional[typing.Sequence[typing.Union[_LifecycleRule_bb74e6ff, typing.Dict[builtins.str, typing.Any]]]] = None,
        artifacts_bucket_location: typing.Optional[typing.Union[ArtifactsBucketLocation, typing.Dict[builtins.str, typing.Any]]] = None,
        canary_name: typing.Optional[builtins.str] = None,
        cleanup: typing.Optional["Cleanup"] = None,
        environment_variables: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        failure_retention_period: typing.Optional[_Duration_4839e8c3] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
        schedule: typing.Optional["Schedule"] = None,
        security_groups: typing.Optional[typing.Sequence[_ISecurityGroup_acf8a799]] = None,
        start_after_creation: typing.Optional[builtins.bool] = None,
        success_retention_period: typing.Optional[_Duration_4839e8c3] = None,
        time_to_live: typing.Optional[_Duration_4839e8c3] = None,
        vpc: typing.Optional[_IVpc_f30d5663] = None,
        vpc_subnets: typing.Optional[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Properties for a canary.

        :param runtime: Specify the runtime version to use for the canary.
        :param test: The type of test that you want your canary to run. Use ``Test.custom()`` to specify the test to run.
        :param artifacts_bucket_lifecycle_rules: Lifecycle rules for the generated canary artifact bucket. Has no effect if a bucket is passed to ``artifactsBucketLocation``. If you pass a bucket to ``artifactsBucketLocation``, you can add lifecycle rules to the bucket itself. Default: - no rules applied to the generated bucket.
        :param artifacts_bucket_location: The s3 location that stores the data of the canary runs. Default: - A new s3 bucket will be created without a prefix.
        :param canary_name: The name of the canary. Be sure to give it a descriptive name that distinguishes it from other canaries in your account. Do not include secrets or proprietary information in your canary name. The canary name makes up part of the canary ARN, which is included in outbound calls over the internet. Default: - A unique name will be generated from the construct ID
        :param cleanup: Specify the underlying resources to be cleaned up when the canary is deleted. Using ``Cleanup.LAMBDA`` will create a Custom Resource to achieve this. Default: Cleanup.NOTHING
        :param environment_variables: Key-value pairs that the Synthetics caches and makes available for your canary scripts. Use environment variables to apply configuration changes, such as test and production environment configurations, without changing your Canary script source code. Default: - No environment variables.
        :param failure_retention_period: How many days should failed runs be retained. Default: Duration.days(31)
        :param role: Canary execution role. This is the role that will be assumed by the canary upon execution. It controls the permissions that the canary will have. The role must be assumable by the AWS Lambda service principal. If not supplied, a role will be created with all the required permissions. If you provide a Role, you must add the required permissions. Default: - A unique role will be generated for this canary. You can add permissions to roles by calling 'addToRolePolicy'.
        :param schedule: Specify the schedule for how often the canary runs. For example, if you set ``schedule`` to ``rate(10 minutes)``, then the canary will run every 10 minutes. You can set the schedule with ``Schedule.rate(Duration)`` (recommended) or you can specify an expression using ``Schedule.expression()``. Default: 'rate(5 minutes)'
        :param security_groups: The list of security groups to associate with the canary's network interfaces. You must provide ``vpc`` when using this prop. Default: - If the canary is placed within a VPC and a security group is not specified a dedicated security group will be created for this canary.
        :param start_after_creation: Whether or not the canary should start after creation. Default: true
        :param success_retention_period: How many days should successful runs be retained. Default: Duration.days(31)
        :param time_to_live: How long the canary will be in a 'RUNNING' state. For example, if you set ``timeToLive`` to be 1 hour and ``schedule`` to be ``rate(10 minutes)``, your canary will run at 10 minute intervals for an hour, for a total of 6 times. Default: - no limit
        :param vpc: The VPC where this canary is run. Specify this if the canary needs to access resources in a VPC. Default: - Not in VPC
        :param vpc_subnets: Where to place the network interfaces within the VPC. You must provide ``vpc`` when using this prop. Default: - the Vpc default strategy if not specified

        :exampleMetadata: infused

        Example::

            canary = synthetics.Canary(self, "MyCanary",
                schedule=synthetics.Schedule.rate(Duration.minutes(5)),
                test=synthetics.Test.custom(
                    code=synthetics.Code.from_asset(path.join(__dirname, "canary")),
                    handler="index.handler"
                ),
                runtime=synthetics.Runtime.SYNTHETICS_NODEJS_PUPPETEER_6_2,
                environment_variables={
                    "stage": "prod"
                }
            )
        '''
        if isinstance(artifacts_bucket_location, dict):
            artifacts_bucket_location = ArtifactsBucketLocation(**artifacts_bucket_location)
        if isinstance(vpc_subnets, dict):
            vpc_subnets = _SubnetSelection_e57d76df(**vpc_subnets)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44ec0b14d52b66927d4daebe6f97bb070f3629bb0eb86e21668ca7862bb5f5bd)
            check_type(argname="argument runtime", value=runtime, expected_type=type_hints["runtime"])
            check_type(argname="argument test", value=test, expected_type=type_hints["test"])
            check_type(argname="argument artifacts_bucket_lifecycle_rules", value=artifacts_bucket_lifecycle_rules, expected_type=type_hints["artifacts_bucket_lifecycle_rules"])
            check_type(argname="argument artifacts_bucket_location", value=artifacts_bucket_location, expected_type=type_hints["artifacts_bucket_location"])
            check_type(argname="argument canary_name", value=canary_name, expected_type=type_hints["canary_name"])
            check_type(argname="argument cleanup", value=cleanup, expected_type=type_hints["cleanup"])
            check_type(argname="argument environment_variables", value=environment_variables, expected_type=type_hints["environment_variables"])
            check_type(argname="argument failure_retention_period", value=failure_retention_period, expected_type=type_hints["failure_retention_period"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument schedule", value=schedule, expected_type=type_hints["schedule"])
            check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
            check_type(argname="argument start_after_creation", value=start_after_creation, expected_type=type_hints["start_after_creation"])
            check_type(argname="argument success_retention_period", value=success_retention_period, expected_type=type_hints["success_retention_period"])
            check_type(argname="argument time_to_live", value=time_to_live, expected_type=type_hints["time_to_live"])
            check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
            check_type(argname="argument vpc_subnets", value=vpc_subnets, expected_type=type_hints["vpc_subnets"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "runtime": runtime,
            "test": test,
        }
        if artifacts_bucket_lifecycle_rules is not None:
            self._values["artifacts_bucket_lifecycle_rules"] = artifacts_bucket_lifecycle_rules
        if artifacts_bucket_location is not None:
            self._values["artifacts_bucket_location"] = artifacts_bucket_location
        if canary_name is not None:
            self._values["canary_name"] = canary_name
        if cleanup is not None:
            self._values["cleanup"] = cleanup
        if environment_variables is not None:
            self._values["environment_variables"] = environment_variables
        if failure_retention_period is not None:
            self._values["failure_retention_period"] = failure_retention_period
        if role is not None:
            self._values["role"] = role
        if schedule is not None:
            self._values["schedule"] = schedule
        if security_groups is not None:
            self._values["security_groups"] = security_groups
        if start_after_creation is not None:
            self._values["start_after_creation"] = start_after_creation
        if success_retention_period is not None:
            self._values["success_retention_period"] = success_retention_period
        if time_to_live is not None:
            self._values["time_to_live"] = time_to_live
        if vpc is not None:
            self._values["vpc"] = vpc
        if vpc_subnets is not None:
            self._values["vpc_subnets"] = vpc_subnets

    @builtins.property
    def runtime(self) -> "Runtime":
        '''Specify the runtime version to use for the canary.

        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Library.html
        '''
        result = self._values.get("runtime")
        assert result is not None, "Required property 'runtime' is missing"
        return typing.cast("Runtime", result)

    @builtins.property
    def test(self) -> "Test":
        '''The type of test that you want your canary to run.

        Use ``Test.custom()`` to specify the test to run.
        '''
        result = self._values.get("test")
        assert result is not None, "Required property 'test' is missing"
        return typing.cast("Test", result)

    @builtins.property
    def artifacts_bucket_lifecycle_rules(
        self,
    ) -> typing.Optional[typing.List[_LifecycleRule_bb74e6ff]]:
        '''Lifecycle rules for the generated canary artifact bucket.

        Has no effect
        if a bucket is passed to ``artifactsBucketLocation``. If you pass a bucket
        to ``artifactsBucketLocation``, you can add lifecycle rules to the bucket
        itself.

        :default: - no rules applied to the generated bucket.
        '''
        result = self._values.get("artifacts_bucket_lifecycle_rules")
        return typing.cast(typing.Optional[typing.List[_LifecycleRule_bb74e6ff]], result)

    @builtins.property
    def artifacts_bucket_location(self) -> typing.Optional[ArtifactsBucketLocation]:
        '''The s3 location that stores the data of the canary runs.

        :default: - A new s3 bucket will be created without a prefix.
        '''
        result = self._values.get("artifacts_bucket_location")
        return typing.cast(typing.Optional[ArtifactsBucketLocation], result)

    @builtins.property
    def canary_name(self) -> typing.Optional[builtins.str]:
        '''The name of the canary.

        Be sure to give it a descriptive name that distinguishes it from
        other canaries in your account.

        Do not include secrets or proprietary information in your canary name. The canary name
        makes up part of the canary ARN, which is included in outbound calls over the internet.

        :default: - A unique name will be generated from the construct ID

        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/servicelens_canaries_security.html
        '''
        result = self._values.get("canary_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cleanup(self) -> typing.Optional["Cleanup"]:
        '''Specify the underlying resources to be cleaned up when the canary is deleted.

        Using ``Cleanup.LAMBDA`` will create a Custom Resource to achieve this.

        :default: Cleanup.NOTHING
        '''
        result = self._values.get("cleanup")
        return typing.cast(typing.Optional["Cleanup"], result)

    @builtins.property
    def environment_variables(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Key-value pairs that the Synthetics caches and makes available for your canary scripts.

        Use environment variables
        to apply configuration changes, such as test and production environment configurations, without changing your
        Canary script source code.

        :default: - No environment variables.
        '''
        result = self._values.get("environment_variables")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def failure_retention_period(self) -> typing.Optional[_Duration_4839e8c3]:
        '''How many days should failed runs be retained.

        :default: Duration.days(31)
        '''
        result = self._values.get("failure_retention_period")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''Canary execution role.

        This is the role that will be assumed by the canary upon execution.
        It controls the permissions that the canary will have. The role must
        be assumable by the AWS Lambda service principal.

        If not supplied, a role will be created with all the required permissions.
        If you provide a Role, you must add the required permissions.

        :default:

        - A unique role will be generated for this canary.
        You can add permissions to roles by calling 'addToRolePolicy'.

        :see: required permissions: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-executionrolearn
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    @builtins.property
    def schedule(self) -> typing.Optional["Schedule"]:
        '''Specify the schedule for how often the canary runs.

        For example, if you set ``schedule`` to ``rate(10 minutes)``, then the canary will run every 10 minutes.
        You can set the schedule with ``Schedule.rate(Duration)`` (recommended) or you can specify an expression using ``Schedule.expression()``.

        :default: 'rate(5 minutes)'
        '''
        result = self._values.get("schedule")
        return typing.cast(typing.Optional["Schedule"], result)

    @builtins.property
    def security_groups(self) -> typing.Optional[typing.List[_ISecurityGroup_acf8a799]]:
        '''The list of security groups to associate with the canary's network interfaces.

        You must provide ``vpc`` when using this prop.

        :default:

        - If the canary is placed within a VPC and a security group is
        not specified a dedicated security group will be created for this canary.
        '''
        result = self._values.get("security_groups")
        return typing.cast(typing.Optional[typing.List[_ISecurityGroup_acf8a799]], result)

    @builtins.property
    def start_after_creation(self) -> typing.Optional[builtins.bool]:
        '''Whether or not the canary should start after creation.

        :default: true
        '''
        result = self._values.get("start_after_creation")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def success_retention_period(self) -> typing.Optional[_Duration_4839e8c3]:
        '''How many days should successful runs be retained.

        :default: Duration.days(31)
        '''
        result = self._values.get("success_retention_period")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def time_to_live(self) -> typing.Optional[_Duration_4839e8c3]:
        '''How long the canary will be in a 'RUNNING' state.

        For example, if you set ``timeToLive`` to be 1 hour and ``schedule`` to be ``rate(10 minutes)``,
        your canary will run at 10 minute intervals for an hour, for a total of 6 times.

        :default: - no limit
        '''
        result = self._values.get("time_to_live")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def vpc(self) -> typing.Optional[_IVpc_f30d5663]:
        '''The VPC where this canary is run.

        Specify this if the canary needs to access resources in a VPC.

        :default: - Not in VPC
        '''
        result = self._values.get("vpc")
        return typing.cast(typing.Optional[_IVpc_f30d5663], result)

    @builtins.property
    def vpc_subnets(self) -> typing.Optional[_SubnetSelection_e57d76df]:
        '''Where to place the network interfaces within the VPC.

        You must provide ``vpc`` when using this prop.

        :default: - the Vpc default strategy if not specified
        '''
        result = self._values.get("vpc_subnets")
        return typing.cast(typing.Optional[_SubnetSelection_e57d76df], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CanaryProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnCanary(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_synthetics.CfnCanary",
):
    '''Creates or updates a canary.

    Canaries are scripts that monitor your endpoints and APIs from the outside-in. Canaries help you check the availability and latency of your web services and troubleshoot anomalies by investigating load time data, screenshots of the UI, logs, and metrics. You can set up a canary to run continuously or just once.

    To create canaries, you must have the ``CloudWatchSyntheticsFullAccess`` policy. If you are creating a new IAM role for the canary, you also need the the ``iam:CreateRole`` , ``iam:CreatePolicy`` and ``iam:AttachRolePolicy`` permissions. For more information, see `Necessary Roles and Permissions <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Roles>`_ .

    Do not include secrets or proprietary information in your canary names. The canary name makes up part of the Amazon Resource Name (ARN) for the canary, and the ARN is included in outbound calls over the internet. For more information, see `Security Considerations for Synthetics Canaries <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/servicelens_canaries_security.html>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html
    :cloudformationResource: AWS::Synthetics::Canary
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_synthetics as synthetics
        
        cfn_canary = synthetics.CfnCanary(self, "MyCfnCanary",
            artifact_s3_location="artifactS3Location",
            code=synthetics.CfnCanary.CodeProperty(
                handler="handler",
        
                # the properties below are optional
                s3_bucket="s3Bucket",
                s3_key="s3Key",
                s3_object_version="s3ObjectVersion",
                script="script",
                source_location_arn="sourceLocationArn"
            ),
            execution_role_arn="executionRoleArn",
            name="name",
            runtime_version="runtimeVersion",
            schedule=synthetics.CfnCanary.ScheduleProperty(
                expression="expression",
        
                # the properties below are optional
                duration_in_seconds="durationInSeconds"
            ),
        
            # the properties below are optional
            artifact_config=synthetics.CfnCanary.ArtifactConfigProperty(
                s3_encryption=synthetics.CfnCanary.S3EncryptionProperty(
                    encryption_mode="encryptionMode",
                    kms_key_arn="kmsKeyArn"
                )
            ),
            delete_lambda_resources_on_canary_deletion=False,
            failure_retention_period=123,
            run_config=synthetics.CfnCanary.RunConfigProperty(
                active_tracing=False,
                environment_variables={
                    "environment_variables_key": "environmentVariables"
                },
                memory_in_mb=123,
                timeout_in_seconds=123
            ),
            start_canary_after_creation=False,
            success_retention_period=123,
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            visual_reference=synthetics.CfnCanary.VisualReferenceProperty(
                base_canary_run_id="baseCanaryRunId",
        
                # the properties below are optional
                base_screenshots=[synthetics.CfnCanary.BaseScreenshotProperty(
                    screenshot_name="screenshotName",
        
                    # the properties below are optional
                    ignore_coordinates=["ignoreCoordinates"]
                )]
            ),
            vpc_config=synthetics.CfnCanary.VPCConfigProperty(
                security_group_ids=["securityGroupIds"],
                subnet_ids=["subnetIds"],
        
                # the properties below are optional
                vpc_id="vpcId"
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        artifact_s3_location: builtins.str,
        code: typing.Union[_IResolvable_da3f097b, typing.Union["CfnCanary.CodeProperty", typing.Dict[builtins.str, typing.Any]]],
        execution_role_arn: builtins.str,
        name: builtins.str,
        runtime_version: builtins.str,
        schedule: typing.Union[_IResolvable_da3f097b, typing.Union["CfnCanary.ScheduleProperty", typing.Dict[builtins.str, typing.Any]]],
        artifact_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCanary.ArtifactConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        delete_lambda_resources_on_canary_deletion: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        failure_retention_period: typing.Optional[jsii.Number] = None,
        run_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCanary.RunConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        start_canary_after_creation: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        success_retention_period: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        visual_reference: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCanary.VisualReferenceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        vpc_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCanary.VPCConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param artifact_s3_location: The location in Amazon S3 where Synthetics stores artifacts from the runs of this canary. Artifacts include the log file, screenshots, and HAR files. Specify the full location path, including ``s3://`` at the beginning of the path.
        :param code: Use this structure to input your script code for the canary. This structure contains the Lambda handler with the location where the canary should start running the script. If the script is stored in an S3 bucket, the bucket name, key, and version are also included. If the script is passed into the canary directly, the script code is contained in the value of ``Script`` .
        :param execution_role_arn: The ARN of the IAM role to be used to run the canary. This role must already exist, and must include ``lambda.amazonaws.com`` as a principal in the trust policy. The role must also have the following permissions: - ``s3:PutObject`` - ``s3:GetBucketLocation`` - ``s3:ListAllMyBuckets`` - ``cloudwatch:PutMetricData`` - ``logs:CreateLogGroup`` - ``logs:CreateLogStream`` - ``logs:PutLogEvents``
        :param name: The name for this canary. Be sure to give it a descriptive name that distinguishes it from other canaries in your account. Do not include secrets or proprietary information in your canary names. The canary name makes up part of the canary ARN, and the ARN is included in outbound calls over the internet. For more information, see `Security Considerations for Synthetics Canaries <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/servicelens_canaries_security.html>`_ .
        :param runtime_version: Specifies the runtime version to use for the canary. For more information about runtime versions, see `Canary Runtime Versions <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Library.html>`_ .
        :param schedule: A structure that contains information about how often the canary is to run, and when these runs are to stop.
        :param artifact_config: A structure that contains the configuration for canary artifacts, including the encryption-at-rest settings for artifacts that the canary uploads to Amazon S3.
        :param delete_lambda_resources_on_canary_deletion: (deprecated) Deletes associated lambda resources created by Synthetics if set to True. Default is False
        :param failure_retention_period: The number of days to retain data about failed runs of this canary. If you omit this field, the default of 31 days is used. The valid range is 1 to 455 days.
        :param run_config: A structure that contains input information for a canary run. If you omit this structure, the frequency of the canary is used as canary's timeout value, up to a maximum of 900 seconds.
        :param start_canary_after_creation: Specify TRUE to have the canary start making runs immediately after it is created. A canary that you create using CloudFormation can't be used to monitor the CloudFormation stack that creates the canary or to roll back that stack if there is a failure.
        :param success_retention_period: The number of days to retain data about successful runs of this canary. If you omit this field, the default of 31 days is used. The valid range is 1 to 455 days.
        :param tags: The list of key-value pairs that are associated with the canary.
        :param visual_reference: If this canary performs visual monitoring by comparing screenshots, this structure contains the ID of the canary run to use as the baseline for screenshots, and the coordinates of any parts of the screen to ignore during the visual monitoring comparison.
        :param vpc_config: If this canary is to test an endpoint in a VPC, this structure contains information about the subnet and security groups of the VPC endpoint. For more information, see `Running a Canary in a VPC <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_VPC.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8fcb3f48eca9399b4d1d31a5ef709e22f9fa52ad1e174b75d8313ef2b971663)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCanaryProps(
            artifact_s3_location=artifact_s3_location,
            code=code,
            execution_role_arn=execution_role_arn,
            name=name,
            runtime_version=runtime_version,
            schedule=schedule,
            artifact_config=artifact_config,
            delete_lambda_resources_on_canary_deletion=delete_lambda_resources_on_canary_deletion,
            failure_retention_period=failure_retention_period,
            run_config=run_config,
            start_canary_after_creation=start_canary_after_creation,
            success_retention_period=success_retention_period,
            tags=tags,
            visual_reference=visual_reference,
            vpc_config=vpc_config,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc166bab0fcf177897c1dbb233203e39458428064bc6ff7215b01b2b3ec6f3a2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__65410bca39459dd8b2ef582ab37870de468cb765034b9600759877910b340355)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCodeSourceLocationArn")
    def attr_code_source_location_arn(self) -> builtins.str:
        '''``Ref`` returns the ARN of the Lambda layer where Synthetics stores the canary script code.

        :cloudformationAttribute: Code.SourceLocationArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCodeSourceLocationArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The ID of the canary.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrState")
    def attr_state(self) -> builtins.str:
        '''The state of the canary.

        For example, ``RUNNING`` .

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
    @jsii.member(jsii_name="artifactS3Location")
    def artifact_s3_location(self) -> builtins.str:
        '''The location in Amazon S3 where Synthetics stores artifacts from the runs of this canary.'''
        return typing.cast(builtins.str, jsii.get(self, "artifactS3Location"))

    @artifact_s3_location.setter
    def artifact_s3_location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cdaba4ac1ed08cbb682b002e6d07aabeaccadbe7c5a6d4bbbc1aaaa15bb4831c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "artifactS3Location", value)

    @builtins.property
    @jsii.member(jsii_name="code")
    def code(self) -> typing.Union[_IResolvable_da3f097b, "CfnCanary.CodeProperty"]:
        '''Use this structure to input your script code for the canary.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnCanary.CodeProperty"], jsii.get(self, "code"))

    @code.setter
    def code(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnCanary.CodeProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__940d05df3a63f7ad05e985fa05317d4b896a6a845409a8d700cbf186fd8e49d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "code", value)

    @builtins.property
    @jsii.member(jsii_name="executionRoleArn")
    def execution_role_arn(self) -> builtins.str:
        '''The ARN of the IAM role to be used to run the canary.'''
        return typing.cast(builtins.str, jsii.get(self, "executionRoleArn"))

    @execution_role_arn.setter
    def execution_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21989f82228cbbd4b8df02c1285ab8cf3635cf4eb894f4a4c999e6b763e92ded)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "executionRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name for this canary.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02a5568fdb7b5da09cb493a9883d04e695a0b6375532601c26ea6ba719fd869a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="runtimeVersion")
    def runtime_version(self) -> builtins.str:
        '''Specifies the runtime version to use for the canary.'''
        return typing.cast(builtins.str, jsii.get(self, "runtimeVersion"))

    @runtime_version.setter
    def runtime_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64f9d8326de93a51cdd4ab89bc4c5431c218c9b46372d81f4fe7a8961b26fa2c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "runtimeVersion", value)

    @builtins.property
    @jsii.member(jsii_name="schedule")
    def schedule(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnCanary.ScheduleProperty"]:
        '''A structure that contains information about how often the canary is to run, and when these runs are to stop.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnCanary.ScheduleProperty"], jsii.get(self, "schedule"))

    @schedule.setter
    def schedule(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnCanary.ScheduleProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e387628a17b84461f77d8fdc851f2b16bcda58e50d8e9279d02062270a5516f0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schedule", value)

    @builtins.property
    @jsii.member(jsii_name="artifactConfig")
    def artifact_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCanary.ArtifactConfigProperty"]]:
        '''A structure that contains the configuration for canary artifacts, including the encryption-at-rest settings for artifacts that the canary uploads to Amazon S3.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCanary.ArtifactConfigProperty"]], jsii.get(self, "artifactConfig"))

    @artifact_config.setter
    def artifact_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCanary.ArtifactConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5946ee35eff32e4581a6d2e3e0c69d62cdc3c17f079123211f7251bc1a10d878)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "artifactConfig", value)

    @builtins.property
    @jsii.member(jsii_name="deleteLambdaResourcesOnCanaryDeletion")
    def delete_lambda_resources_on_canary_deletion(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''(deprecated) Deletes associated lambda resources created by Synthetics if set to True.

        :deprecated: this property has been deprecated

        :stability: deprecated
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "deleteLambdaResourcesOnCanaryDeletion"))

    @delete_lambda_resources_on_canary_deletion.setter
    def delete_lambda_resources_on_canary_deletion(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__442577c2c36e4274dca25b3d866e1aeec3f4ffc18732e01050131a31f768f2b3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deleteLambdaResourcesOnCanaryDeletion", value)

    @builtins.property
    @jsii.member(jsii_name="failureRetentionPeriod")
    def failure_retention_period(self) -> typing.Optional[jsii.Number]:
        '''The number of days to retain data about failed runs of this canary.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "failureRetentionPeriod"))

    @failure_retention_period.setter
    def failure_retention_period(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02a7e43f45419c4cb8e909f309f8848d4ced91d17b01d14e5ea0b8cec28aab1b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "failureRetentionPeriod", value)

    @builtins.property
    @jsii.member(jsii_name="runConfig")
    def run_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCanary.RunConfigProperty"]]:
        '''A structure that contains input information for a canary run.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCanary.RunConfigProperty"]], jsii.get(self, "runConfig"))

    @run_config.setter
    def run_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCanary.RunConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e65fb80249e43aebfe46950832be73ed0795003be5d74ca1ef7cd12bb2408557)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "runConfig", value)

    @builtins.property
    @jsii.member(jsii_name="startCanaryAfterCreation")
    def start_canary_after_creation(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specify TRUE to have the canary start making runs immediately after it is created.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "startCanaryAfterCreation"))

    @start_canary_after_creation.setter
    def start_canary_after_creation(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a98feaf45022b36ef5c9888f87b978029d5e1fde70599e1972543b1778adfad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startCanaryAfterCreation", value)

    @builtins.property
    @jsii.member(jsii_name="successRetentionPeriod")
    def success_retention_period(self) -> typing.Optional[jsii.Number]:
        '''The number of days to retain data about successful runs of this canary.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "successRetentionPeriod"))

    @success_retention_period.setter
    def success_retention_period(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8bbba327f646025c54903ccf2c19cedc26cf07f79658c389f65ef40b263130f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "successRetentionPeriod", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The list of key-value pairs that are associated with the canary.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__212d1e59a4bd96a18f447b1c742abcfeb7c668063c8e1670fa0770e339ac4077)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="visualReference")
    def visual_reference(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCanary.VisualReferenceProperty"]]:
        '''If this canary performs visual monitoring by comparing screenshots, this structure contains the ID of the canary run to use as the baseline for screenshots, and the coordinates of any parts of the screen to ignore during the visual monitoring comparison.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCanary.VisualReferenceProperty"]], jsii.get(self, "visualReference"))

    @visual_reference.setter
    def visual_reference(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCanary.VisualReferenceProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21e93a70969fa03a3f0aa85f6b1615a26d9a0afef8a0cf27f0888fc59aef420b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "visualReference", value)

    @builtins.property
    @jsii.member(jsii_name="vpcConfig")
    def vpc_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCanary.VPCConfigProperty"]]:
        '''If this canary is to test an endpoint in a VPC, this structure contains information about the subnet and security groups of the VPC endpoint.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCanary.VPCConfigProperty"]], jsii.get(self, "vpcConfig"))

    @vpc_config.setter
    def vpc_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCanary.VPCConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be63ed6816e3043aef63f6e7c0d0dfcc35f1249735acd4eff8530f8c2253b747)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcConfig", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_synthetics.CfnCanary.ArtifactConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_encryption": "s3Encryption"},
    )
    class ArtifactConfigProperty:
        def __init__(
            self,
            *,
            s3_encryption: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCanary.S3EncryptionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''A structure that contains the configuration for canary artifacts, including the encryption-at-rest settings for artifacts that the canary uploads to Amazon S3 .

            :param s3_encryption: A structure that contains the configuration of the encryption-at-rest settings for artifacts that the canary uploads to Amazon S3 . Artifact encryption functionality is available only for canaries that use Synthetics runtime version syn-nodejs-puppeteer-3.3 or later. For more information, see `Encrypting canary artifacts <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_artifact_encryption.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-artifactconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_synthetics as synthetics
                
                artifact_config_property = synthetics.CfnCanary.ArtifactConfigProperty(
                    s3_encryption=synthetics.CfnCanary.S3EncryptionProperty(
                        encryption_mode="encryptionMode",
                        kms_key_arn="kmsKeyArn"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9c456e72742651aec26b46a7fbd663821284d03931fd10859243079b815dad28)
                check_type(argname="argument s3_encryption", value=s3_encryption, expected_type=type_hints["s3_encryption"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if s3_encryption is not None:
                self._values["s3_encryption"] = s3_encryption

        @builtins.property
        def s3_encryption(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCanary.S3EncryptionProperty"]]:
            '''A structure that contains the configuration of the encryption-at-rest settings for artifacts that the canary uploads to Amazon S3 .

            Artifact encryption functionality is available only for canaries that use Synthetics runtime version syn-nodejs-puppeteer-3.3 or later. For more information, see `Encrypting canary artifacts <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_artifact_encryption.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-artifactconfig.html#cfn-synthetics-canary-artifactconfig-s3encryption
            '''
            result = self._values.get("s3_encryption")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCanary.S3EncryptionProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ArtifactConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_synthetics.CfnCanary.BaseScreenshotProperty",
        jsii_struct_bases=[],
        name_mapping={
            "screenshot_name": "screenshotName",
            "ignore_coordinates": "ignoreCoordinates",
        },
    )
    class BaseScreenshotProperty:
        def __init__(
            self,
            *,
            screenshot_name: builtins.str,
            ignore_coordinates: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''A structure representing a screenshot that is used as a baseline during visual monitoring comparisons made by the canary.

            :param screenshot_name: The name of the screenshot. This is generated the first time the canary is run after the ``UpdateCanary`` operation that specified for this canary to perform visual monitoring.
            :param ignore_coordinates: Coordinates that define the part of a screen to ignore during screenshot comparisons. To obtain the coordinates to use here, use the CloudWatch console to draw the boundaries on the screen. For more information, see `Edit or delete a canary <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/synthetics_canaries_deletion.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-basescreenshot.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_synthetics as synthetics
                
                base_screenshot_property = synthetics.CfnCanary.BaseScreenshotProperty(
                    screenshot_name="screenshotName",
                
                    # the properties below are optional
                    ignore_coordinates=["ignoreCoordinates"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8d401a2416919aef18322e23fb875fc37ad8f90f34f8f5708a245f22f9d3208f)
                check_type(argname="argument screenshot_name", value=screenshot_name, expected_type=type_hints["screenshot_name"])
                check_type(argname="argument ignore_coordinates", value=ignore_coordinates, expected_type=type_hints["ignore_coordinates"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "screenshot_name": screenshot_name,
            }
            if ignore_coordinates is not None:
                self._values["ignore_coordinates"] = ignore_coordinates

        @builtins.property
        def screenshot_name(self) -> builtins.str:
            '''The name of the screenshot.

            This is generated the first time the canary is run after the ``UpdateCanary`` operation that specified for this canary to perform visual monitoring.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-basescreenshot.html#cfn-synthetics-canary-basescreenshot-screenshotname
            '''
            result = self._values.get("screenshot_name")
            assert result is not None, "Required property 'screenshot_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def ignore_coordinates(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Coordinates that define the part of a screen to ignore during screenshot comparisons.

            To obtain the coordinates to use here, use the CloudWatch console to draw the boundaries on the screen. For more information, see `Edit or delete a canary <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/synthetics_canaries_deletion.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-basescreenshot.html#cfn-synthetics-canary-basescreenshot-ignorecoordinates
            '''
            result = self._values.get("ignore_coordinates")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BaseScreenshotProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_synthetics.CfnCanary.CodeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "handler": "handler",
            "s3_bucket": "s3Bucket",
            "s3_key": "s3Key",
            "s3_object_version": "s3ObjectVersion",
            "script": "script",
            "source_location_arn": "sourceLocationArn",
        },
    )
    class CodeProperty:
        def __init__(
            self,
            *,
            handler: builtins.str,
            s3_bucket: typing.Optional[builtins.str] = None,
            s3_key: typing.Optional[builtins.str] = None,
            s3_object_version: typing.Optional[builtins.str] = None,
            script: typing.Optional[builtins.str] = None,
            source_location_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Use this structure to input your script code for the canary.

            This structure contains the Lambda handler with the location where the canary should start running the script. If the script is stored in an S3 bucket, the bucket name, key, and version are also included. If the script is passed into the canary directly, the script code is contained in the value of ``Script`` .

            :param handler: The entry point to use for the source code when running the canary. For canaries that use the ``syn-python-selenium-1.0`` runtime or a ``syn-nodejs.puppeteer`` runtime earlier than ``syn-nodejs.puppeteer-3.4`` , the handler must be specified as ``*fileName* .handler`` . For ``syn-python-selenium-1.1`` , ``syn-nodejs.puppeteer-3.4`` , and later runtimes, the handler can be specified as ``*fileName* . *functionName*`` , or you can specify a folder where canary scripts reside as ``*folder* / *fileName* . *functionName*`` .
            :param s3_bucket: If your canary script is located in S3, specify the bucket name here. The bucket must already exist.
            :param s3_key: The S3 key of your script. For more information, see `Working with Amazon S3 Objects <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingObjects.html>`_ .
            :param s3_object_version: The S3 version ID of your script.
            :param script: If you input your canary script directly into the canary instead of referring to an S3 location, the value of this parameter is the script in plain text. It can be up to 5 MB.
            :param source_location_arn: The ARN of the Lambda layer where Synthetics stores the canary script code.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-code.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_synthetics as synthetics
                
                code_property = synthetics.CfnCanary.CodeProperty(
                    handler="handler",
                
                    # the properties below are optional
                    s3_bucket="s3Bucket",
                    s3_key="s3Key",
                    s3_object_version="s3ObjectVersion",
                    script="script",
                    source_location_arn="sourceLocationArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3d403372a613babc1ab10717d050ec9a7f4055961f3545f2d0600d89c7b3dcc3)
                check_type(argname="argument handler", value=handler, expected_type=type_hints["handler"])
                check_type(argname="argument s3_bucket", value=s3_bucket, expected_type=type_hints["s3_bucket"])
                check_type(argname="argument s3_key", value=s3_key, expected_type=type_hints["s3_key"])
                check_type(argname="argument s3_object_version", value=s3_object_version, expected_type=type_hints["s3_object_version"])
                check_type(argname="argument script", value=script, expected_type=type_hints["script"])
                check_type(argname="argument source_location_arn", value=source_location_arn, expected_type=type_hints["source_location_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "handler": handler,
            }
            if s3_bucket is not None:
                self._values["s3_bucket"] = s3_bucket
            if s3_key is not None:
                self._values["s3_key"] = s3_key
            if s3_object_version is not None:
                self._values["s3_object_version"] = s3_object_version
            if script is not None:
                self._values["script"] = script
            if source_location_arn is not None:
                self._values["source_location_arn"] = source_location_arn

        @builtins.property
        def handler(self) -> builtins.str:
            '''The entry point to use for the source code when running the canary.

            For canaries that use the ``syn-python-selenium-1.0`` runtime or a ``syn-nodejs.puppeteer`` runtime earlier than ``syn-nodejs.puppeteer-3.4`` , the handler must be specified as ``*fileName* .handler`` . For ``syn-python-selenium-1.1`` , ``syn-nodejs.puppeteer-3.4`` , and later runtimes, the handler can be specified as ``*fileName* . *functionName*`` , or you can specify a folder where canary scripts reside as ``*folder* / *fileName* . *functionName*`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-code.html#cfn-synthetics-canary-code-handler
            '''
            result = self._values.get("handler")
            assert result is not None, "Required property 'handler' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_bucket(self) -> typing.Optional[builtins.str]:
            '''If your canary script is located in S3, specify the bucket name here.

            The bucket must already exist.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-code.html#cfn-synthetics-canary-code-s3bucket
            '''
            result = self._values.get("s3_bucket")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3_key(self) -> typing.Optional[builtins.str]:
            '''The S3 key of your script.

            For more information, see `Working with Amazon S3 Objects <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingObjects.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-code.html#cfn-synthetics-canary-code-s3key
            '''
            result = self._values.get("s3_key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3_object_version(self) -> typing.Optional[builtins.str]:
            '''The S3 version ID of your script.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-code.html#cfn-synthetics-canary-code-s3objectversion
            '''
            result = self._values.get("s3_object_version")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def script(self) -> typing.Optional[builtins.str]:
            '''If you input your canary script directly into the canary instead of referring to an S3 location, the value of this parameter is the script in plain text.

            It can be up to 5 MB.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-code.html#cfn-synthetics-canary-code-script
            '''
            result = self._values.get("script")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def source_location_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the Lambda layer where Synthetics stores the canary script code.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-code.html#cfn-synthetics-canary-code-sourcelocationarn
            '''
            result = self._values.get("source_location_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CodeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_synthetics.CfnCanary.RunConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "active_tracing": "activeTracing",
            "environment_variables": "environmentVariables",
            "memory_in_mb": "memoryInMb",
            "timeout_in_seconds": "timeoutInSeconds",
        },
    )
    class RunConfigProperty:
        def __init__(
            self,
            *,
            active_tracing: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            environment_variables: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
            memory_in_mb: typing.Optional[jsii.Number] = None,
            timeout_in_seconds: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''A structure that contains input information for a canary run.

            This structure is required.

            :param active_tracing: Specifies whether this canary is to use active AWS X-Ray tracing when it runs. Active tracing enables this canary run to be displayed in the ServiceLens and X-Ray service maps even if the canary does not hit an endpoint that has X-Ray tracing enabled. Using X-Ray tracing incurs charges. For more information, see `Canaries and X-Ray tracing <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_tracing.html>`_ . You can enable active tracing only for canaries that use version ``syn-nodejs-2.0`` or later for their canary runtime.
            :param environment_variables: Specifies the keys and values to use for any environment variables used in the canary script. Use the following format: { "key1" : "value1", "key2" : "value2", ...} Keys must start with a letter and be at least two characters. The total size of your environment variables cannot exceed 4 KB. You can't specify any Lambda reserved environment variables as the keys for your environment variables. For more information about reserved keys, see `Runtime environment variables <https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html#configuration-envvars-runtime>`_ .
            :param memory_in_mb: The maximum amount of memory that the canary can use while running. This value must be a multiple of 64. The range is 960 to 3008.
            :param timeout_in_seconds: How long the canary is allowed to run before it must stop. You can't set this time to be longer than the frequency of the runs of this canary. If you omit this field, the frequency of the canary is used as this value, up to a maximum of 900 seconds.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-runconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_synthetics as synthetics
                
                run_config_property = synthetics.CfnCanary.RunConfigProperty(
                    active_tracing=False,
                    environment_variables={
                        "environment_variables_key": "environmentVariables"
                    },
                    memory_in_mb=123,
                    timeout_in_seconds=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fa148862e82948accbbe951e7afcee721aa7014754c81106d2648fe1c5cf28e2)
                check_type(argname="argument active_tracing", value=active_tracing, expected_type=type_hints["active_tracing"])
                check_type(argname="argument environment_variables", value=environment_variables, expected_type=type_hints["environment_variables"])
                check_type(argname="argument memory_in_mb", value=memory_in_mb, expected_type=type_hints["memory_in_mb"])
                check_type(argname="argument timeout_in_seconds", value=timeout_in_seconds, expected_type=type_hints["timeout_in_seconds"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if active_tracing is not None:
                self._values["active_tracing"] = active_tracing
            if environment_variables is not None:
                self._values["environment_variables"] = environment_variables
            if memory_in_mb is not None:
                self._values["memory_in_mb"] = memory_in_mb
            if timeout_in_seconds is not None:
                self._values["timeout_in_seconds"] = timeout_in_seconds

        @builtins.property
        def active_tracing(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies whether this canary is to use active AWS X-Ray tracing when it runs.

            Active tracing enables this canary run to be displayed in the ServiceLens and X-Ray service maps even if the canary does not hit an endpoint that has X-Ray tracing enabled. Using X-Ray tracing incurs charges. For more information, see `Canaries and X-Ray tracing <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_tracing.html>`_ .

            You can enable active tracing only for canaries that use version ``syn-nodejs-2.0`` or later for their canary runtime.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-runconfig.html#cfn-synthetics-canary-runconfig-activetracing
            '''
            result = self._values.get("active_tracing")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def environment_variables(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
            '''Specifies the keys and values to use for any environment variables used in the canary script.

            Use the following format:

            { "key1" : "value1", "key2" : "value2", ...}

            Keys must start with a letter and be at least two characters. The total size of your environment variables cannot exceed 4 KB. You can't specify any Lambda reserved environment variables as the keys for your environment variables. For more information about reserved keys, see `Runtime environment variables <https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html#configuration-envvars-runtime>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-runconfig.html#cfn-synthetics-canary-runconfig-environmentvariables
            '''
            result = self._values.get("environment_variables")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], result)

        @builtins.property
        def memory_in_mb(self) -> typing.Optional[jsii.Number]:
            '''The maximum amount of memory that the canary can use while running.

            This value must be a multiple of 64. The range is 960 to 3008.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-runconfig.html#cfn-synthetics-canary-runconfig-memoryinmb
            '''
            result = self._values.get("memory_in_mb")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def timeout_in_seconds(self) -> typing.Optional[jsii.Number]:
            '''How long the canary is allowed to run before it must stop.

            You can't set this time to be longer than the frequency of the runs of this canary.

            If you omit this field, the frequency of the canary is used as this value, up to a maximum of 900 seconds.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-runconfig.html#cfn-synthetics-canary-runconfig-timeoutinseconds
            '''
            result = self._values.get("timeout_in_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RunConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_synthetics.CfnCanary.S3EncryptionProperty",
        jsii_struct_bases=[],
        name_mapping={"encryption_mode": "encryptionMode", "kms_key_arn": "kmsKeyArn"},
    )
    class S3EncryptionProperty:
        def __init__(
            self,
            *,
            encryption_mode: typing.Optional[builtins.str] = None,
            kms_key_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A structure that contains the configuration of the encryption-at-rest settings for artifacts that the canary uploads to Amazon S3 .

            Artifact encryption functionality is available only for canaries that use Synthetics runtime version syn-nodejs-puppeteer-3.3 or later. For more information, see `Encrypting canary artifacts <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_artifact_encryption.html>`_ .

            :param encryption_mode: The encryption method to use for artifacts created by this canary. Specify ``SSE_S3`` to use server-side encryption (SSE) with an Amazon S3-managed key. Specify ``SSE-KMS`` to use server-side encryption with a customer-managed AWS KMS key. If you omit this parameter, an AWS -managed AWS KMS key is used.
            :param kms_key_arn: The ARN of the customer-managed AWS KMS key to use, if you specify ``SSE-KMS`` for ``EncryptionMode``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-s3encryption.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_synthetics as synthetics
                
                s3_encryption_property = synthetics.CfnCanary.S3EncryptionProperty(
                    encryption_mode="encryptionMode",
                    kms_key_arn="kmsKeyArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__551aad28104a61040e1d9e12e77c77ae47c6e19a45d15bfa94e441c5d297d3ab)
                check_type(argname="argument encryption_mode", value=encryption_mode, expected_type=type_hints["encryption_mode"])
                check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if encryption_mode is not None:
                self._values["encryption_mode"] = encryption_mode
            if kms_key_arn is not None:
                self._values["kms_key_arn"] = kms_key_arn

        @builtins.property
        def encryption_mode(self) -> typing.Optional[builtins.str]:
            '''The encryption method to use for artifacts created by this canary.

            Specify ``SSE_S3`` to use server-side encryption (SSE) with an Amazon S3-managed key. Specify ``SSE-KMS`` to use server-side encryption with a customer-managed AWS KMS key.

            If you omit this parameter, an AWS -managed AWS KMS key is used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-s3encryption.html#cfn-synthetics-canary-s3encryption-encryptionmode
            '''
            result = self._values.get("encryption_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def kms_key_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the customer-managed AWS KMS key to use, if you specify ``SSE-KMS`` for ``EncryptionMode``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-s3encryption.html#cfn-synthetics-canary-s3encryption-kmskeyarn
            '''
            result = self._values.get("kms_key_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3EncryptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_synthetics.CfnCanary.ScheduleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "expression": "expression",
            "duration_in_seconds": "durationInSeconds",
        },
    )
    class ScheduleProperty:
        def __init__(
            self,
            *,
            expression: builtins.str,
            duration_in_seconds: typing.Optional[builtins.str] = None,
        ) -> None:
            '''This structure specifies how often a canary is to make runs and the date and time when it should stop making runs.

            :param expression: A ``rate`` expression or a ``cron`` expression that defines how often the canary is to run. For a rate expression, The syntax is ``rate( *number unit* )`` . *unit* can be ``minute`` , ``minutes`` , or ``hour`` . For example, ``rate(1 minute)`` runs the canary once a minute, ``rate(10 minutes)`` runs it once every 10 minutes, and ``rate(1 hour)`` runs it once every hour. You can specify a frequency between ``rate(1 minute)`` and ``rate(1 hour)`` . Specifying ``rate(0 minute)`` or ``rate(0 hour)`` is a special value that causes the canary to run only once when it is started. Use ``cron( *expression* )`` to specify a cron expression. You can't schedule a canary to wait for more than a year before running. For information about the syntax for cron expressions, see `Scheduling canary runs using cron <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_cron.html>`_ .
            :param duration_in_seconds: How long, in seconds, for the canary to continue making regular runs according to the schedule in the ``Expression`` value. If you specify 0, the canary continues making runs until you stop it. If you omit this field, the default of 0 is used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-schedule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_synthetics as synthetics
                
                schedule_property = synthetics.CfnCanary.ScheduleProperty(
                    expression="expression",
                
                    # the properties below are optional
                    duration_in_seconds="durationInSeconds"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e4999288d0e0c5de04c56a3436208778026602dfdca27710aee93f9f4e034c29)
                check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
                check_type(argname="argument duration_in_seconds", value=duration_in_seconds, expected_type=type_hints["duration_in_seconds"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "expression": expression,
            }
            if duration_in_seconds is not None:
                self._values["duration_in_seconds"] = duration_in_seconds

        @builtins.property
        def expression(self) -> builtins.str:
            '''A ``rate`` expression or a ``cron`` expression that defines how often the canary is to run.

            For a rate expression, The syntax is ``rate( *number unit* )`` . *unit* can be ``minute`` , ``minutes`` , or ``hour`` .

            For example, ``rate(1 minute)`` runs the canary once a minute, ``rate(10 minutes)`` runs it once every 10 minutes, and ``rate(1 hour)`` runs it once every hour. You can specify a frequency between ``rate(1 minute)`` and ``rate(1 hour)`` .

            Specifying ``rate(0 minute)`` or ``rate(0 hour)`` is a special value that causes the canary to run only once when it is started.

            Use ``cron( *expression* )`` to specify a cron expression. You can't schedule a canary to wait for more than a year before running. For information about the syntax for cron expressions, see `Scheduling canary runs using cron <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_cron.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-schedule.html#cfn-synthetics-canary-schedule-expression
            '''
            result = self._values.get("expression")
            assert result is not None, "Required property 'expression' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def duration_in_seconds(self) -> typing.Optional[builtins.str]:
            '''How long, in seconds, for the canary to continue making regular runs according to the schedule in the ``Expression`` value.

            If you specify 0, the canary continues making runs until you stop it. If you omit this field, the default of 0 is used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-schedule.html#cfn-synthetics-canary-schedule-durationinseconds
            '''
            result = self._values.get("duration_in_seconds")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScheduleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_synthetics.CfnCanary.VPCConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "security_group_ids": "securityGroupIds",
            "subnet_ids": "subnetIds",
            "vpc_id": "vpcId",
        },
    )
    class VPCConfigProperty:
        def __init__(
            self,
            *,
            security_group_ids: typing.Sequence[builtins.str],
            subnet_ids: typing.Sequence[builtins.str],
            vpc_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''If this canary is to test an endpoint in a VPC, this structure contains information about the subnet and security groups of the VPC endpoint.

            For more information, see `Running a Canary in a VPC <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_VPC.html>`_ .

            :param security_group_ids: The IDs of the security groups for this canary.
            :param subnet_ids: The IDs of the subnets where this canary is to run.
            :param vpc_id: The ID of the VPC where this canary is to run.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-vpcconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_synthetics as synthetics
                
                v_pCConfig_property = synthetics.CfnCanary.VPCConfigProperty(
                    security_group_ids=["securityGroupIds"],
                    subnet_ids=["subnetIds"],
                
                    # the properties below are optional
                    vpc_id="vpcId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__eccfde82eb2354e9c416fba506f2ff8e4fb1a86792529f65e2d8eafbc8415074)
                check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
                check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
                check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "security_group_ids": security_group_ids,
                "subnet_ids": subnet_ids,
            }
            if vpc_id is not None:
                self._values["vpc_id"] = vpc_id

        @builtins.property
        def security_group_ids(self) -> typing.List[builtins.str]:
            '''The IDs of the security groups for this canary.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-vpcconfig.html#cfn-synthetics-canary-vpcconfig-securitygroupids
            '''
            result = self._values.get("security_group_ids")
            assert result is not None, "Required property 'security_group_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def subnet_ids(self) -> typing.List[builtins.str]:
            '''The IDs of the subnets where this canary is to run.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-vpcconfig.html#cfn-synthetics-canary-vpcconfig-subnetids
            '''
            result = self._values.get("subnet_ids")
            assert result is not None, "Required property 'subnet_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def vpc_id(self) -> typing.Optional[builtins.str]:
            '''The ID of the VPC where this canary is to run.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-vpcconfig.html#cfn-synthetics-canary-vpcconfig-vpcid
            '''
            result = self._values.get("vpc_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VPCConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_synthetics.CfnCanary.VisualReferenceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "base_canary_run_id": "baseCanaryRunId",
            "base_screenshots": "baseScreenshots",
        },
    )
    class VisualReferenceProperty:
        def __init__(
            self,
            *,
            base_canary_run_id: builtins.str,
            base_screenshots: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCanary.BaseScreenshotProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Defines the screenshots to use as the baseline for comparisons during visual monitoring comparisons during future runs of this canary.

            If you omit this parameter, no changes are made to any baseline screenshots that the canary might be using already.

            Visual monitoring is supported only on canaries running the *syn-puppeteer-node-3.2* runtime or later. For more information, see `Visual monitoring <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Library_SyntheticsLogger_VisualTesting.html>`_ and `Visual monitoring blueprint <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Blueprints_VisualTesting.html>`_

            :param base_canary_run_id: Specifies which canary run to use the screenshots from as the baseline for future visual monitoring with this canary. Valid values are ``nextrun`` to use the screenshots from the next run after this update is made, ``lastrun`` to use the screenshots from the most recent run before this update was made, or the value of ``Id`` in the `CanaryRun <https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_CanaryRun.html>`_ from any past run of this canary.
            :param base_screenshots: An array of screenshots that are used as the baseline for comparisons during visual monitoring.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-visualreference.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_synthetics as synthetics
                
                visual_reference_property = synthetics.CfnCanary.VisualReferenceProperty(
                    base_canary_run_id="baseCanaryRunId",
                
                    # the properties below are optional
                    base_screenshots=[synthetics.CfnCanary.BaseScreenshotProperty(
                        screenshot_name="screenshotName",
                
                        # the properties below are optional
                        ignore_coordinates=["ignoreCoordinates"]
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f52b6b7318141dc99f6bd36c21b91cda286b67d7dea805791a6132a2cd794526)
                check_type(argname="argument base_canary_run_id", value=base_canary_run_id, expected_type=type_hints["base_canary_run_id"])
                check_type(argname="argument base_screenshots", value=base_screenshots, expected_type=type_hints["base_screenshots"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "base_canary_run_id": base_canary_run_id,
            }
            if base_screenshots is not None:
                self._values["base_screenshots"] = base_screenshots

        @builtins.property
        def base_canary_run_id(self) -> builtins.str:
            '''Specifies which canary run to use the screenshots from as the baseline for future visual monitoring with this canary.

            Valid values are ``nextrun`` to use the screenshots from the next run after this update is made, ``lastrun`` to use the screenshots from the most recent run before this update was made, or the value of ``Id`` in the `CanaryRun <https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_CanaryRun.html>`_ from any past run of this canary.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-visualreference.html#cfn-synthetics-canary-visualreference-basecanaryrunid
            '''
            result = self._values.get("base_canary_run_id")
            assert result is not None, "Required property 'base_canary_run_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def base_screenshots(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCanary.BaseScreenshotProperty"]]]]:
            '''An array of screenshots that are used as the baseline for comparisons during visual monitoring.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-visualreference.html#cfn-synthetics-canary-visualreference-basescreenshots
            '''
            result = self._values.get("base_screenshots")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCanary.BaseScreenshotProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VisualReferenceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_synthetics.CfnCanaryProps",
    jsii_struct_bases=[],
    name_mapping={
        "artifact_s3_location": "artifactS3Location",
        "code": "code",
        "execution_role_arn": "executionRoleArn",
        "name": "name",
        "runtime_version": "runtimeVersion",
        "schedule": "schedule",
        "artifact_config": "artifactConfig",
        "delete_lambda_resources_on_canary_deletion": "deleteLambdaResourcesOnCanaryDeletion",
        "failure_retention_period": "failureRetentionPeriod",
        "run_config": "runConfig",
        "start_canary_after_creation": "startCanaryAfterCreation",
        "success_retention_period": "successRetentionPeriod",
        "tags": "tags",
        "visual_reference": "visualReference",
        "vpc_config": "vpcConfig",
    },
)
class CfnCanaryProps:
    def __init__(
        self,
        *,
        artifact_s3_location: builtins.str,
        code: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCanary.CodeProperty, typing.Dict[builtins.str, typing.Any]]],
        execution_role_arn: builtins.str,
        name: builtins.str,
        runtime_version: builtins.str,
        schedule: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCanary.ScheduleProperty, typing.Dict[builtins.str, typing.Any]]],
        artifact_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCanary.ArtifactConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        delete_lambda_resources_on_canary_deletion: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        failure_retention_period: typing.Optional[jsii.Number] = None,
        run_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCanary.RunConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        start_canary_after_creation: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        success_retention_period: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        visual_reference: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCanary.VisualReferenceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        vpc_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCanary.VPCConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnCanary``.

        :param artifact_s3_location: The location in Amazon S3 where Synthetics stores artifacts from the runs of this canary. Artifacts include the log file, screenshots, and HAR files. Specify the full location path, including ``s3://`` at the beginning of the path.
        :param code: Use this structure to input your script code for the canary. This structure contains the Lambda handler with the location where the canary should start running the script. If the script is stored in an S3 bucket, the bucket name, key, and version are also included. If the script is passed into the canary directly, the script code is contained in the value of ``Script`` .
        :param execution_role_arn: The ARN of the IAM role to be used to run the canary. This role must already exist, and must include ``lambda.amazonaws.com`` as a principal in the trust policy. The role must also have the following permissions: - ``s3:PutObject`` - ``s3:GetBucketLocation`` - ``s3:ListAllMyBuckets`` - ``cloudwatch:PutMetricData`` - ``logs:CreateLogGroup`` - ``logs:CreateLogStream`` - ``logs:PutLogEvents``
        :param name: The name for this canary. Be sure to give it a descriptive name that distinguishes it from other canaries in your account. Do not include secrets or proprietary information in your canary names. The canary name makes up part of the canary ARN, and the ARN is included in outbound calls over the internet. For more information, see `Security Considerations for Synthetics Canaries <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/servicelens_canaries_security.html>`_ .
        :param runtime_version: Specifies the runtime version to use for the canary. For more information about runtime versions, see `Canary Runtime Versions <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Library.html>`_ .
        :param schedule: A structure that contains information about how often the canary is to run, and when these runs are to stop.
        :param artifact_config: A structure that contains the configuration for canary artifacts, including the encryption-at-rest settings for artifacts that the canary uploads to Amazon S3.
        :param delete_lambda_resources_on_canary_deletion: (deprecated) Deletes associated lambda resources created by Synthetics if set to True. Default is False
        :param failure_retention_period: The number of days to retain data about failed runs of this canary. If you omit this field, the default of 31 days is used. The valid range is 1 to 455 days.
        :param run_config: A structure that contains input information for a canary run. If you omit this structure, the frequency of the canary is used as canary's timeout value, up to a maximum of 900 seconds.
        :param start_canary_after_creation: Specify TRUE to have the canary start making runs immediately after it is created. A canary that you create using CloudFormation can't be used to monitor the CloudFormation stack that creates the canary or to roll back that stack if there is a failure.
        :param success_retention_period: The number of days to retain data about successful runs of this canary. If you omit this field, the default of 31 days is used. The valid range is 1 to 455 days.
        :param tags: The list of key-value pairs that are associated with the canary.
        :param visual_reference: If this canary performs visual monitoring by comparing screenshots, this structure contains the ID of the canary run to use as the baseline for screenshots, and the coordinates of any parts of the screen to ignore during the visual monitoring comparison.
        :param vpc_config: If this canary is to test an endpoint in a VPC, this structure contains information about the subnet and security groups of the VPC endpoint. For more information, see `Running a Canary in a VPC <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_VPC.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_synthetics as synthetics
            
            cfn_canary_props = synthetics.CfnCanaryProps(
                artifact_s3_location="artifactS3Location",
                code=synthetics.CfnCanary.CodeProperty(
                    handler="handler",
            
                    # the properties below are optional
                    s3_bucket="s3Bucket",
                    s3_key="s3Key",
                    s3_object_version="s3ObjectVersion",
                    script="script",
                    source_location_arn="sourceLocationArn"
                ),
                execution_role_arn="executionRoleArn",
                name="name",
                runtime_version="runtimeVersion",
                schedule=synthetics.CfnCanary.ScheduleProperty(
                    expression="expression",
            
                    # the properties below are optional
                    duration_in_seconds="durationInSeconds"
                ),
            
                # the properties below are optional
                artifact_config=synthetics.CfnCanary.ArtifactConfigProperty(
                    s3_encryption=synthetics.CfnCanary.S3EncryptionProperty(
                        encryption_mode="encryptionMode",
                        kms_key_arn="kmsKeyArn"
                    )
                ),
                delete_lambda_resources_on_canary_deletion=False,
                failure_retention_period=123,
                run_config=synthetics.CfnCanary.RunConfigProperty(
                    active_tracing=False,
                    environment_variables={
                        "environment_variables_key": "environmentVariables"
                    },
                    memory_in_mb=123,
                    timeout_in_seconds=123
                ),
                start_canary_after_creation=False,
                success_retention_period=123,
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                visual_reference=synthetics.CfnCanary.VisualReferenceProperty(
                    base_canary_run_id="baseCanaryRunId",
            
                    # the properties below are optional
                    base_screenshots=[synthetics.CfnCanary.BaseScreenshotProperty(
                        screenshot_name="screenshotName",
            
                        # the properties below are optional
                        ignore_coordinates=["ignoreCoordinates"]
                    )]
                ),
                vpc_config=synthetics.CfnCanary.VPCConfigProperty(
                    security_group_ids=["securityGroupIds"],
                    subnet_ids=["subnetIds"],
            
                    # the properties below are optional
                    vpc_id="vpcId"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d869d56ce0d1d2e2add2f80bf39b28abbec2752c719e03194ee540bf1949e423)
            check_type(argname="argument artifact_s3_location", value=artifact_s3_location, expected_type=type_hints["artifact_s3_location"])
            check_type(argname="argument code", value=code, expected_type=type_hints["code"])
            check_type(argname="argument execution_role_arn", value=execution_role_arn, expected_type=type_hints["execution_role_arn"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument runtime_version", value=runtime_version, expected_type=type_hints["runtime_version"])
            check_type(argname="argument schedule", value=schedule, expected_type=type_hints["schedule"])
            check_type(argname="argument artifact_config", value=artifact_config, expected_type=type_hints["artifact_config"])
            check_type(argname="argument delete_lambda_resources_on_canary_deletion", value=delete_lambda_resources_on_canary_deletion, expected_type=type_hints["delete_lambda_resources_on_canary_deletion"])
            check_type(argname="argument failure_retention_period", value=failure_retention_period, expected_type=type_hints["failure_retention_period"])
            check_type(argname="argument run_config", value=run_config, expected_type=type_hints["run_config"])
            check_type(argname="argument start_canary_after_creation", value=start_canary_after_creation, expected_type=type_hints["start_canary_after_creation"])
            check_type(argname="argument success_retention_period", value=success_retention_period, expected_type=type_hints["success_retention_period"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument visual_reference", value=visual_reference, expected_type=type_hints["visual_reference"])
            check_type(argname="argument vpc_config", value=vpc_config, expected_type=type_hints["vpc_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "artifact_s3_location": artifact_s3_location,
            "code": code,
            "execution_role_arn": execution_role_arn,
            "name": name,
            "runtime_version": runtime_version,
            "schedule": schedule,
        }
        if artifact_config is not None:
            self._values["artifact_config"] = artifact_config
        if delete_lambda_resources_on_canary_deletion is not None:
            self._values["delete_lambda_resources_on_canary_deletion"] = delete_lambda_resources_on_canary_deletion
        if failure_retention_period is not None:
            self._values["failure_retention_period"] = failure_retention_period
        if run_config is not None:
            self._values["run_config"] = run_config
        if start_canary_after_creation is not None:
            self._values["start_canary_after_creation"] = start_canary_after_creation
        if success_retention_period is not None:
            self._values["success_retention_period"] = success_retention_period
        if tags is not None:
            self._values["tags"] = tags
        if visual_reference is not None:
            self._values["visual_reference"] = visual_reference
        if vpc_config is not None:
            self._values["vpc_config"] = vpc_config

    @builtins.property
    def artifact_s3_location(self) -> builtins.str:
        '''The location in Amazon S3 where Synthetics stores artifacts from the runs of this canary.

        Artifacts include the log file, screenshots, and HAR files. Specify the full location path, including ``s3://`` at the beginning of the path.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-artifacts3location
        '''
        result = self._values.get("artifact_s3_location")
        assert result is not None, "Required property 'artifact_s3_location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def code(self) -> typing.Union[_IResolvable_da3f097b, CfnCanary.CodeProperty]:
        '''Use this structure to input your script code for the canary.

        This structure contains the Lambda handler with the location where the canary should start running the script. If the script is stored in an S3 bucket, the bucket name, key, and version are also included. If the script is passed into the canary directly, the script code is contained in the value of ``Script`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-code
        '''
        result = self._values.get("code")
        assert result is not None, "Required property 'code' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnCanary.CodeProperty], result)

    @builtins.property
    def execution_role_arn(self) -> builtins.str:
        '''The ARN of the IAM role to be used to run the canary.

        This role must already exist, and must include ``lambda.amazonaws.com`` as a principal in the trust policy. The role must also have the following permissions:

        - ``s3:PutObject``
        - ``s3:GetBucketLocation``
        - ``s3:ListAllMyBuckets``
        - ``cloudwatch:PutMetricData``
        - ``logs:CreateLogGroup``
        - ``logs:CreateLogStream``
        - ``logs:PutLogEvents``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-executionrolearn
        '''
        result = self._values.get("execution_role_arn")
        assert result is not None, "Required property 'execution_role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name for this canary.

        Be sure to give it a descriptive name that distinguishes it from other canaries in your account.

        Do not include secrets or proprietary information in your canary names. The canary name makes up part of the canary ARN, and the ARN is included in outbound calls over the internet. For more information, see `Security Considerations for Synthetics Canaries <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/servicelens_canaries_security.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def runtime_version(self) -> builtins.str:
        '''Specifies the runtime version to use for the canary.

        For more information about runtime versions, see `Canary Runtime Versions <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Library.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-runtimeversion
        '''
        result = self._values.get("runtime_version")
        assert result is not None, "Required property 'runtime_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def schedule(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnCanary.ScheduleProperty]:
        '''A structure that contains information about how often the canary is to run, and when these runs are to stop.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-schedule
        '''
        result = self._values.get("schedule")
        assert result is not None, "Required property 'schedule' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnCanary.ScheduleProperty], result)

    @builtins.property
    def artifact_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCanary.ArtifactConfigProperty]]:
        '''A structure that contains the configuration for canary artifacts, including the encryption-at-rest settings for artifacts that the canary uploads to Amazon S3.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-artifactconfig
        '''
        result = self._values.get("artifact_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCanary.ArtifactConfigProperty]], result)

    @builtins.property
    def delete_lambda_resources_on_canary_deletion(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''(deprecated) Deletes associated lambda resources created by Synthetics if set to True.

        Default is False

        :deprecated: this property has been deprecated

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-deletelambdaresourcesoncanarydeletion
        :stability: deprecated
        '''
        result = self._values.get("delete_lambda_resources_on_canary_deletion")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def failure_retention_period(self) -> typing.Optional[jsii.Number]:
        '''The number of days to retain data about failed runs of this canary.

        If you omit this field, the default of 31 days is used. The valid range is 1 to 455 days.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-failureretentionperiod
        '''
        result = self._values.get("failure_retention_period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def run_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCanary.RunConfigProperty]]:
        '''A structure that contains input information for a canary run.

        If you omit this structure, the frequency of the canary is used as canary's timeout value, up to a maximum of 900 seconds.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-runconfig
        '''
        result = self._values.get("run_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCanary.RunConfigProperty]], result)

    @builtins.property
    def start_canary_after_creation(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specify TRUE to have the canary start making runs immediately after it is created.

        A canary that you create using CloudFormation can't be used to monitor the CloudFormation stack that creates the canary or to roll back that stack if there is a failure.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-startcanaryaftercreation
        '''
        result = self._values.get("start_canary_after_creation")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def success_retention_period(self) -> typing.Optional[jsii.Number]:
        '''The number of days to retain data about successful runs of this canary.

        If you omit this field, the default of 31 days is used. The valid range is 1 to 455 days.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-successretentionperiod
        '''
        result = self._values.get("success_retention_period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The list of key-value pairs that are associated with the canary.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def visual_reference(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCanary.VisualReferenceProperty]]:
        '''If this canary performs visual monitoring by comparing screenshots, this structure contains the ID of the canary run to use as the baseline for screenshots, and the coordinates of any parts of the screen to ignore during the visual monitoring comparison.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-visualreference
        '''
        result = self._values.get("visual_reference")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCanary.VisualReferenceProperty]], result)

    @builtins.property
    def vpc_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCanary.VPCConfigProperty]]:
        '''If this canary is to test an endpoint in a VPC, this structure contains information about the subnet and security groups of the VPC endpoint.

        For more information, see `Running a Canary in a VPC <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_VPC.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-vpcconfig
        '''
        result = self._values.get("vpc_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCanary.VPCConfigProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCanaryProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnGroup(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_synthetics.CfnGroup",
):
    '''Creates or updates a group which you can use to associate canaries with each other, including cross-Region canaries.

    Using groups can help you with managing and automating your canaries, and you can also view aggregated run results and statistics for all canaries in a group.

    Groups are global resources. When you create a group, it is replicated across all AWS Regions, and you can add canaries from any Region to it, and view it in any Region. Although the group ARN format reflects the Region name where it was created, a group is not constrained to any Region. This means that you can put canaries from multiple Regions into the same group, and then use that group to view and manage all of those canaries in a single view.

    Each group can contain as many as 10 canaries. You can have as many as 20 groups in your account. Any single canary can be a member of up to 10 groups.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-group.html
    :cloudformationResource: AWS::Synthetics::Group
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_synthetics as synthetics
        
        cfn_group = synthetics.CfnGroup(self, "MyCfnGroup",
            name="name",
        
            # the properties below are optional
            resource_arns=["resourceArns"],
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
        name: builtins.str,
        resource_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: A name for the group. It can include any Unicode characters. The names for all groups in your account, across all Regions, must be unique.
        :param resource_arns: The ARNs of the canaries that you want to associate with this group.
        :param tags: The list of key-value pairs that are associated with the group.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__973b5b11ee0c26a7aa94d55785d1a025e0c569700b7877564d84ae1447c2af09)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnGroupProps(name=name, resource_arns=resource_arns, tags=tags)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c02721081747307dfd2212f0ae4958cfbad3dc1ec5b0667712fb08ebd5d7e65)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c4dd500824b1b77e386dc3d0eca110f83c00176cc9ac0861387258adf2b7914e)
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
        '''The Id of the group.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

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
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''A name for the group.

        It can include any Unicode characters.
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6401b033d62b6cede0e2328e1f7c75c5607ed33e285fb529afce4814a3551bee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="resourceArns")
    def resource_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The ARNs of the canaries that you want to associate with this group.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "resourceArns"))

    @resource_arns.setter
    def resource_arns(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__078802d6cab1e35c6ba04d10e648f52314cd74f1c2d198563fb8a7d6435999ba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceArns", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The list of key-value pairs that are associated with the group.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d85cd0ddf465884c3990e0492b92e22606ecfb33b8127bf42d0c344b78427aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_synthetics.CfnGroupProps",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "resource_arns": "resourceArns", "tags": "tags"},
)
class CfnGroupProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        resource_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnGroup``.

        :param name: A name for the group. It can include any Unicode characters. The names for all groups in your account, across all Regions, must be unique.
        :param resource_arns: The ARNs of the canaries that you want to associate with this group.
        :param tags: The list of key-value pairs that are associated with the group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-group.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_synthetics as synthetics
            
            cfn_group_props = synthetics.CfnGroupProps(
                name="name",
            
                # the properties below are optional
                resource_arns=["resourceArns"],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ab100d4133b5b7bd6483c4c3bcf827df685974681f592679f7de8f8ea64b33f)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_arns", value=resource_arns, expected_type=type_hints["resource_arns"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if resource_arns is not None:
            self._values["resource_arns"] = resource_arns
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''A name for the group. It can include any Unicode characters.

        The names for all groups in your account, across all Regions, must be unique.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-group.html#cfn-synthetics-group-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The ARNs of the canaries that you want to associate with this group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-group.html#cfn-synthetics-group-resourcearns
        '''
        result = self._values.get("resource_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The list of key-value pairs that are associated with the group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-group.html#cfn-synthetics-group-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_synthetics.Cleanup")
class Cleanup(enum.Enum):
    '''Different ways to clean up underlying Canary resources when the Canary is deleted.

    :exampleMetadata: infused

    Example::

        canary = synthetics.Canary(self, "Canary",
            test=synthetics.Test.custom(
                handler="index.handler",
                code=synthetics.Code.from_inline("/* Synthetics handler code")
            ),
            cleanup=synthetics.Cleanup.LAMBDA,
            runtime=synthetics.Runtime.SYNTHETICS_NODEJS_PUPPETEER_6_2
        )
    '''

    NOTHING = "NOTHING"
    '''Clean up nothing.

    The user is responsible for cleaning up
    all resources left behind by the Canary.
    '''
    LAMBDA = "LAMBDA"
    '''Clean up the underlying Lambda function only.

    The user is
    responsible for cleaning up all other resources left behind
    by the Canary.
    '''


class Code(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="aws-cdk-lib.aws_synthetics.Code",
):
    '''The code the canary should execute.

    :exampleMetadata: infused

    Example::

        canary = synthetics.Canary(self, "MyCanary",
            schedule=synthetics.Schedule.rate(Duration.minutes(5)),
            test=synthetics.Test.custom(
                code=synthetics.Code.from_asset(path.join(__dirname, "canary")),
                handler="index.handler"
            ),
            runtime=synthetics.Runtime.SYNTHETICS_NODEJS_PUPPETEER_6_2,
            environment_variables={
                "stage": "prod"
            }
        )
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="fromAsset")
    @builtins.classmethod
    def from_asset(
        cls,
        asset_path: builtins.str,
        *,
        deploy_time: typing.Optional[builtins.bool] = None,
        readers: typing.Optional[typing.Sequence[_IGrantable_71c4f5de]] = None,
        asset_hash: typing.Optional[builtins.str] = None,
        asset_hash_type: typing.Optional[_AssetHashType_05b67f2d] = None,
        bundling: typing.Optional[typing.Union[_BundlingOptions_588cc936, typing.Dict[builtins.str, typing.Any]]] = None,
        exclude: typing.Optional[typing.Sequence[builtins.str]] = None,
        follow_symlinks: typing.Optional[_SymlinkFollowMode_047ec1f6] = None,
        ignore_mode: typing.Optional[_IgnoreMode_655a98e8] = None,
    ) -> "AssetCode":
        '''Specify code from a local path.

        Path must include the folder structure ``nodejs/node_modules/myCanaryFilename.js``.

        :param asset_path: Either a directory or a .zip file.
        :param deploy_time: Whether or not the asset needs to exist beyond deployment time; i.e. are copied over to a different location and not needed afterwards. Setting this property to true has an impact on the lifecycle of the asset, because we will assume that it is safe to delete after the CloudFormation deployment succeeds. For example, Lambda Function assets are copied over to Lambda during deployment. Therefore, it is not necessary to store the asset in S3, so we consider those deployTime assets. Default: false
        :param readers: A list of principals that should be able to read this asset from S3. You can use ``asset.grantRead(principal)`` to grant read permissions later. Default: - No principals that can read file asset.
        :param asset_hash: Specify a custom hash for this asset. If ``assetHashType`` is set it must be set to ``AssetHashType.CUSTOM``. For consistency, this custom hash will be SHA256 hashed and encoded as hex. The resulting hash will be the asset hash. NOTE: the hash is used in order to identify a specific revision of the asset, and used for optimizing and caching deployment activities related to this asset such as packaging, uploading to Amazon S3, etc. If you chose to customize the hash, you will need to make sure it is updated every time the asset changes, or otherwise it is possible that some deployments will not be invalidated. Default: - based on ``assetHashType``
        :param asset_hash_type: Specifies the type of hash to calculate for this asset. If ``assetHash`` is configured, this option must be ``undefined`` or ``AssetHashType.CUSTOM``. Default: - the default is ``AssetHashType.SOURCE``, but if ``assetHash`` is explicitly specified this value defaults to ``AssetHashType.CUSTOM``.
        :param bundling: Bundle the asset by executing a command in a Docker container or a custom bundling provider. The asset path will be mounted at ``/asset-input``. The Docker container is responsible for putting content at ``/asset-output``. The content at ``/asset-output`` will be zipped and used as the final asset. Default: - uploaded as-is to S3 if the asset is a regular file or a .zip file, archived into a .zip file and uploaded to S3 otherwise
        :param exclude: File paths matching the patterns will be excluded. See ``ignoreMode`` to set the matching behavior. Has no effect on Assets bundled using the ``bundling`` property. Default: - nothing is excluded
        :param follow_symlinks: A strategy for how to handle symlinks. Default: SymlinkFollowMode.NEVER
        :param ignore_mode: The ignore behavior to use for ``exclude`` patterns. Default: IgnoreMode.GLOB

        :return: ``AssetCode`` associated with the specified path.

        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_WritingCanary.html#CloudWatch_Synthetics_Canaries_write_from_scratch
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02201c2190b076bbceced8708b435fab8189f7f505650002941cc7a50e23adff)
            check_type(argname="argument asset_path", value=asset_path, expected_type=type_hints["asset_path"])
        options = _AssetOptions_2aa69621(
            deploy_time=deploy_time,
            readers=readers,
            asset_hash=asset_hash,
            asset_hash_type=asset_hash_type,
            bundling=bundling,
            exclude=exclude,
            follow_symlinks=follow_symlinks,
            ignore_mode=ignore_mode,
        )

        return typing.cast("AssetCode", jsii.sinvoke(cls, "fromAsset", [asset_path, options]))

    @jsii.member(jsii_name="fromBucket")
    @builtins.classmethod
    def from_bucket(
        cls,
        bucket: _IBucket_42e086fd,
        key: builtins.str,
        object_version: typing.Optional[builtins.str] = None,
    ) -> "S3Code":
        '''Specify code from an s3 bucket.

        The object in the s3 bucket must be a .zip file that contains
        the structure ``nodejs/node_modules/myCanaryFilename.js``.

        :param bucket: The S3 bucket.
        :param key: The object key.
        :param object_version: Optional S3 object version.

        :return: ``S3Code`` associated with the specified S3 object.

        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_WritingCanary.html#CloudWatch_Synthetics_Canaries_write_from_scratch
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__449747bf42ca4f0c5864a72ad8bd3bcd8b8dedef173ae2e8a54e213a343068a6)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument object_version", value=object_version, expected_type=type_hints["object_version"])
        return typing.cast("S3Code", jsii.sinvoke(cls, "fromBucket", [bucket, key, object_version]))

    @jsii.member(jsii_name="fromInline")
    @builtins.classmethod
    def from_inline(cls, code: builtins.str) -> "InlineCode":
        '''Specify code inline.

        :param code: The actual handler code (limited to 5MB).

        :return: ``InlineCode`` with inline code.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72d5e409f31e6e624d17b0671dedc0be55eeb0d3f459389a05661b94b0f5d0ab)
            check_type(argname="argument code", value=code, expected_type=type_hints["code"])
        return typing.cast("InlineCode", jsii.sinvoke(cls, "fromInline", [code]))

    @jsii.member(jsii_name="bind")
    @abc.abstractmethod
    def bind(
        self,
        scope: _constructs_77d1e7e8.Construct,
        handler: builtins.str,
        family: "RuntimeFamily",
    ) -> "CodeConfig":
        '''Called when the canary is initialized to allow this object to bind to the stack, add resources and have fun.

        :param scope: The binding scope. Don't be smart about trying to down-cast or assume it's initialized. You may just use it as a construct scope.
        :param handler: -
        :param family: -

        :return: a bound ``CodeConfig``.
        '''
        ...


class _CodeProxy(Code):
    @jsii.member(jsii_name="bind")
    def bind(
        self,
        scope: _constructs_77d1e7e8.Construct,
        handler: builtins.str,
        family: "RuntimeFamily",
    ) -> "CodeConfig":
        '''Called when the canary is initialized to allow this object to bind to the stack, add resources and have fun.

        :param scope: The binding scope. Don't be smart about trying to down-cast or assume it's initialized. You may just use it as a construct scope.
        :param handler: -
        :param family: -

        :return: a bound ``CodeConfig``.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__16072f2291ff792418a957a399b7ca3a9d2e16cb1e67d33d5682dbb0eebaf541)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument handler", value=handler, expected_type=type_hints["handler"])
            check_type(argname="argument family", value=family, expected_type=type_hints["family"])
        return typing.cast("CodeConfig", jsii.invoke(self, "bind", [scope, handler, family]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, Code).__jsii_proxy_class__ = lambda : _CodeProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_synthetics.CodeConfig",
    jsii_struct_bases=[],
    name_mapping={"inline_code": "inlineCode", "s3_location": "s3Location"},
)
class CodeConfig:
    def __init__(
        self,
        *,
        inline_code: typing.Optional[builtins.str] = None,
        s3_location: typing.Optional[typing.Union[_Location_0948fa7f, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Configuration of the code class.

        :param inline_code: Inline code (mutually exclusive with ``s3Location``). Default: - none
        :param s3_location: The location of the code in S3 (mutually exclusive with ``inlineCode``). Default: - none

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_synthetics as synthetics
            
            code_config = synthetics.CodeConfig(
                inline_code="inlineCode",
                s3_location=Location(
                    bucket_name="bucketName",
                    object_key="objectKey",
            
                    # the properties below are optional
                    object_version="objectVersion"
                )
            )
        '''
        if isinstance(s3_location, dict):
            s3_location = _Location_0948fa7f(**s3_location)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a34e85aaf9472ee1bd9ebc1e0c43060979cf58692956f81c385d453a371973e)
            check_type(argname="argument inline_code", value=inline_code, expected_type=type_hints["inline_code"])
            check_type(argname="argument s3_location", value=s3_location, expected_type=type_hints["s3_location"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if inline_code is not None:
            self._values["inline_code"] = inline_code
        if s3_location is not None:
            self._values["s3_location"] = s3_location

    @builtins.property
    def inline_code(self) -> typing.Optional[builtins.str]:
        '''Inline code (mutually exclusive with ``s3Location``).

        :default: - none
        '''
        result = self._values.get("inline_code")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def s3_location(self) -> typing.Optional[_Location_0948fa7f]:
        '''The location of the code in S3 (mutually exclusive with ``inlineCode``).

        :default: - none
        '''
        result = self._values.get("s3_location")
        return typing.cast(typing.Optional[_Location_0948fa7f], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodeConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_synthetics.CronOptions",
    jsii_struct_bases=[],
    name_mapping={
        "day": "day",
        "hour": "hour",
        "minute": "minute",
        "month": "month",
        "week_day": "weekDay",
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
    ) -> None:
        '''Options to configure a cron expression.

        All fields are strings so you can use complex expressions. Absence of
        a field implies '*' or '?', whichever one is appropriate.

        :param day: The day of the month to run this rule at. Default: - Every day of the month
        :param hour: The hour to run this rule at. Default: - Every hour
        :param minute: The minute to run this rule at. Default: - Every minute
        :param month: The month to run this rule at. Default: - Every month
        :param week_day: The day of the week to run this rule at. Default: - Any day of the week

        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_cron.html
        :exampleMetadata: infused

        Example::

            schedule = synthetics.Schedule.cron(
                hour="0,8,16"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f80f44d8794a637e9994828c4264f001f407cac43a28d1b0c7e51bb7487337d)
            check_type(argname="argument day", value=day, expected_type=type_hints["day"])
            check_type(argname="argument hour", value=hour, expected_type=type_hints["hour"])
            check_type(argname="argument minute", value=minute, expected_type=type_hints["minute"])
            check_type(argname="argument month", value=month, expected_type=type_hints["month"])
            check_type(argname="argument week_day", value=week_day, expected_type=type_hints["week_day"])
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

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CronOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_synthetics.CustomTestOptions",
    jsii_struct_bases=[],
    name_mapping={"code": "code", "handler": "handler"},
)
class CustomTestOptions:
    def __init__(self, *, code: Code, handler: builtins.str) -> None:
        '''Properties for specifying a test.

        :param code: The code of the canary script.
        :param handler: The handler for the code. Must end with ``.handler``.

        :exampleMetadata: infused

        Example::

            canary = synthetics.Canary(self, "MyCanary",
                schedule=synthetics.Schedule.rate(Duration.minutes(5)),
                test=synthetics.Test.custom(
                    code=synthetics.Code.from_asset(path.join(__dirname, "canary")),
                    handler="index.handler"
                ),
                runtime=synthetics.Runtime.SYNTHETICS_NODEJS_PUPPETEER_6_2,
                environment_variables={
                    "stage": "prod"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__998aa034b450d34cd7535661c029c2c24a7a34b950b79e5a2b055d31ab5ea31d)
            check_type(argname="argument code", value=code, expected_type=type_hints["code"])
            check_type(argname="argument handler", value=handler, expected_type=type_hints["handler"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "code": code,
            "handler": handler,
        }

    @builtins.property
    def code(self) -> Code:
        '''The code of the canary script.'''
        result = self._values.get("code")
        assert result is not None, "Required property 'code' is missing"
        return typing.cast(Code, result)

    @builtins.property
    def handler(self) -> builtins.str:
        '''The handler for the code.

        Must end with ``.handler``.
        '''
        result = self._values.get("handler")
        assert result is not None, "Required property 'handler' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CustomTestOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class InlineCode(
    Code,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_synthetics.InlineCode",
):
    '''Canary code from an inline string.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_synthetics as synthetics
        
        inline_code = synthetics.InlineCode("code")
    '''

    def __init__(self, code: builtins.str) -> None:
        '''
        :param code: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e4d6f25be5e212e7eccf81a0bb26d92760fb4f335d2fd7395acbdc376c975d2)
            check_type(argname="argument code", value=code, expected_type=type_hints["code"])
        jsii.create(self.__class__, self, [code])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _scope: _constructs_77d1e7e8.Construct,
        handler: builtins.str,
        _family: "RuntimeFamily",
    ) -> CodeConfig:
        '''Called when the canary is initialized to allow this object to bind to the stack, add resources and have fun.

        :param _scope: -
        :param handler: -
        :param _family: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c1dddac73b46d6693b6032065ae6db988e1e76cb520ebf3d4aa58e532f543a9)
            check_type(argname="argument _scope", value=_scope, expected_type=type_hints["_scope"])
            check_type(argname="argument handler", value=handler, expected_type=type_hints["handler"])
            check_type(argname="argument _family", value=_family, expected_type=type_hints["_family"])
        return typing.cast(CodeConfig, jsii.invoke(self, "bind", [_scope, handler, _family]))


class Runtime(metaclass=jsii.JSIIMeta, jsii_type="aws-cdk-lib.aws_synthetics.Runtime"):
    '''Runtime options for a canary.

    :exampleMetadata: infused

    Example::

        canary = synthetics.Canary(self, "MyCanary",
            schedule=synthetics.Schedule.rate(Duration.minutes(5)),
            test=synthetics.Test.custom(
                code=synthetics.Code.from_asset(path.join(__dirname, "canary")),
                handler="index.handler"
            ),
            runtime=synthetics.Runtime.SYNTHETICS_NODEJS_PUPPETEER_6_2,
            environment_variables={
                "stage": "prod"
            }
        )
    '''

    def __init__(self, name: builtins.str, family: "RuntimeFamily") -> None:
        '''
        :param name: The name of the runtime version.
        :param family: The Lambda runtime family.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba23a2bd20fc9334e4b0fac6e1c104de0f53b4ec265cf53ef1a80ad25868f780)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument family", value=family, expected_type=type_hints["family"])
        jsii.create(self.__class__, self, [name, family])

    @jsii.python.classproperty
    @jsii.member(jsii_name="SYNTHETICS_NODEJS_PUPPETEER_3_5")
    def SYNTHETICS_NODEJS_PUPPETEER_3_5(cls) -> "Runtime":
        '''(deprecated) ``syn-nodejs-puppeteer-3.5`` includes the following: - Lambda runtime Node.js 14.x - Puppeteer-core version 5.5.0 - Chromium version 92.0.4512.

        New features:

        - **Updated dependencies**: The only new features in this runtime are the updated dependencies.

        :deprecated: Legacy runtime no longer supported by AWS Lambda. Migrate to the latest NodeJS Puppeteer runtime.

        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Library_nodejs_puppeteer.html#CloudWatch_Synthetics_runtimeversion-nodejs-puppeteer-3.5
        :stability: deprecated
        '''
        return typing.cast("Runtime", jsii.sget(cls, "SYNTHETICS_NODEJS_PUPPETEER_3_5"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SYNTHETICS_NODEJS_PUPPETEER_3_6")
    def SYNTHETICS_NODEJS_PUPPETEER_3_6(cls) -> "Runtime":
        '''(deprecated) ``syn-nodejs-puppeteer-3.6`` includes the following: - Lambda runtime Node.js 14.x - Puppeteer-core version 5.5.0 - Chromium version 92.0.4512.

        :deprecated: Legacy runtime no longer supported by AWS Lambda. Migrate to the latest NodeJS Puppeteer runtime.

        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Library_nodejs_puppeteer.html#CloudWatch_Synthetics_runtimeversion-nodejs-puppeteer-3.6
        :stability: deprecated
        '''
        return typing.cast("Runtime", jsii.sget(cls, "SYNTHETICS_NODEJS_PUPPETEER_3_6"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SYNTHETICS_NODEJS_PUPPETEER_3_7")
    def SYNTHETICS_NODEJS_PUPPETEER_3_7(cls) -> "Runtime":
        '''(deprecated) ``syn-nodejs-puppeteer-3.7`` includes the following: - Lambda runtime Node.js 14.x - Puppeteer-core version 5.5.0 - Chromium version 92.0.4512.

        New Features:

        - **Logging enhancement**: The canary will upload logs to Amazon S3 even if it times out or crashes.
        - **Lambda layer size reduced**: The size of the Lambda layer used for canaries is reduced by 34%.

        :deprecated: Legacy runtime no longer supported by AWS Lambda. Migrate to the latest NodeJS Puppeteer runtime.

        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Library_nodejs_puppeteer.html#CloudWatch_Synthetics_runtimeversion-nodejs-puppeteer-3.7
        :stability: deprecated
        '''
        return typing.cast("Runtime", jsii.sget(cls, "SYNTHETICS_NODEJS_PUPPETEER_3_7"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SYNTHETICS_NODEJS_PUPPETEER_3_8")
    def SYNTHETICS_NODEJS_PUPPETEER_3_8(cls) -> "Runtime":
        '''(deprecated) ``syn-nodejs-puppeteer-3.8`` includes the following: - Lambda runtime Node.js 14.x - Puppeteer-core version 10.1.0 - Chromium version 92.0.4512.

        New Features:

        - **Profile cleanup**: Chromium profiles are now cleaned up after each canary run.

        :deprecated: Legacy runtime no longer supported by AWS Lambda. Migrate to the latest NodeJS Puppeteer runtime.

        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Library_nodejs_puppeteer.html#CloudWatch_Synthetics_runtimeversion-nodejs-puppeteer-3.8
        :stability: deprecated
        '''
        return typing.cast("Runtime", jsii.sget(cls, "SYNTHETICS_NODEJS_PUPPETEER_3_8"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SYNTHETICS_NODEJS_PUPPETEER_3_9")
    def SYNTHETICS_NODEJS_PUPPETEER_3_9(cls) -> "Runtime":
        '''(deprecated) ``syn-nodejs-puppeteer-3.9`` includes the following:.

        - Lambda runtime Node.js 14.x
        - Puppeteer-core version 5.5.0
        - Chromium version 92.0.4512

        New Features:

        - **Dependency upgrades**: Upgrades some third-party dependency packages.

        :deprecated: Legacy runtime no longer supported by AWS Lambda. Migrate to the latest NodeJS Puppeteer runtime.

        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Library_nodejs_puppeteer.html#CloudWatch_Synthetics_runtimeversion-nodejs-puppeteer-3.9
        :stability: deprecated
        '''
        return typing.cast("Runtime", jsii.sget(cls, "SYNTHETICS_NODEJS_PUPPETEER_3_9"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SYNTHETICS_NODEJS_PUPPETEER_4_0")
    def SYNTHETICS_NODEJS_PUPPETEER_4_0(cls) -> "Runtime":
        '''(deprecated) ``syn-nodejs-puppeteer-4.0`` includes the following: - Lambda runtime Node.js 16.x - Puppeteer-core version 5.5.0 - Chromium version 92.0.4512.

        New Features:

        - **Dependency upgrades**: The Node.js dependency is updated to 16.x.

        :deprecated: Legacy runtime no longer supported by AWS Lambda. Migrate to the latest NodeJS Puppeteer runtime.

        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Library_nodejs_puppeteer.html#CloudWatch_Synthetics_runtimeversion-nodejs-puppeteer-4.0
        :stability: deprecated
        '''
        return typing.cast("Runtime", jsii.sget(cls, "SYNTHETICS_NODEJS_PUPPETEER_4_0"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SYNTHETICS_NODEJS_PUPPETEER_5_0")
    def SYNTHETICS_NODEJS_PUPPETEER_5_0(cls) -> "Runtime":
        '''(deprecated) ``syn-nodejs-puppeteer-5.0`` includes the following: - Lambda runtime Node.js 16.x - Puppeteer-core version 19.7.0 - Chromium version 111.0.5563.146.

        New Features:

        - **Dependency upgrade**: The Puppeteer-core version is updated to 19.7.0. The Chromium version is upgraded to 111.0.5563.146.

        :deprecated: Legacy runtime no longer supported by AWS Lambda. Migrate to the latest NodeJS Puppeteer runtime.

        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Library_nodejs_puppeteer.html#CloudWatch_Synthetics_runtimeversion-nodejs-puppeteer-5.0
        :stability: deprecated
        '''
        return typing.cast("Runtime", jsii.sget(cls, "SYNTHETICS_NODEJS_PUPPETEER_5_0"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SYNTHETICS_NODEJS_PUPPETEER_5_1")
    def SYNTHETICS_NODEJS_PUPPETEER_5_1(cls) -> "Runtime":
        '''(deprecated) ``syn-nodejs-puppeteer-5.1`` includes the following: - Lambda runtime Node.js 16.x - Puppeteer-core version 19.7.0 - Chromium version 111.0.5563.146.

        Bug fixes:

        - **Bug fix**: This runtime fixes a bug in ``syn-nodejs-puppeteer-5.0`` where the HAR files created by the canaries were missing request headers.

        :deprecated: Legacy runtime no longer supported by AWS Lambda. Migrate to the latest NodeJS Puppeteer runtime.

        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Library_nodejs_puppeteer.html#CloudWatch_Synthetics_runtimeversion-nodejs-puppeteer-5.1
        :stability: deprecated
        '''
        return typing.cast("Runtime", jsii.sget(cls, "SYNTHETICS_NODEJS_PUPPETEER_5_1"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SYNTHETICS_NODEJS_PUPPETEER_5_2")
    def SYNTHETICS_NODEJS_PUPPETEER_5_2(cls) -> "Runtime":
        '''``syn-nodejs-puppeteer-5.2`` includes the following: - Lambda runtime Node.js 16.x - Puppeteer-core version 19.7.0 - Chromium version 111.0.5563.146.

        New Features:

        - **Updated versions of the bundled libraries in Chromium**
        - **Bug fixes**

        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Library_nodejs_puppeteer.html#CloudWatch_Synthetics_runtimeversion-nodejs-puppeteer-5.2
        '''
        return typing.cast("Runtime", jsii.sget(cls, "SYNTHETICS_NODEJS_PUPPETEER_5_2"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SYNTHETICS_NODEJS_PUPPETEER_6_0")
    def SYNTHETICS_NODEJS_PUPPETEER_6_0(cls) -> "Runtime":
        '''(deprecated) ``syn-nodejs-puppeteer-6.0`` includes the following: - Lambda runtime Node.js 18.x - Puppeteer-core version 19.7.0 - Chromium version 111.0.5563.146.

        New Features:

        - **Dependency upgrade**: The Node.js dependency is upgraded to 18.x.
          Bug fixes:
        - **Bug fix**: Clean up core dump generated when Chromium crashes during a canary run.

        :deprecated: Legacy runtime no longer supported by AWS Lambda. Migrate to the latest NodeJS Puppeteer runtime.

        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Library_nodejs_puppeteer.html#CloudWatch_Synthetics_runtimeversion-nodejs-puppeteer-6.0
        :stability: deprecated
        '''
        return typing.cast("Runtime", jsii.sget(cls, "SYNTHETICS_NODEJS_PUPPETEER_6_0"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SYNTHETICS_NODEJS_PUPPETEER_6_1")
    def SYNTHETICS_NODEJS_PUPPETEER_6_1(cls) -> "Runtime":
        '''(deprecated) ``syn-nodejs-puppeteer-6.1`` includes the following: - Lambda runtime Node.js 18.x - Puppeteer-core version 19.7.0 - Chromium version 111.0.5563.146.

        New Features:

        - **Stability improvements**: Added auto-retry logic for handling intermittent Puppeteer launch errors.
        - **Dependency upgrades**: Upgrades for some third-party dependency packages.
        - **Canaries without Amazon S3 permissions**: Bug fixes, such that canaries that don't have any Amazon S3 permissions can still run. These canaries with no Amazon S3 permissions won't be able to upload screenshots or other artifacts to Amazon S3. For more information about permissions for canaries, see {@link https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_CanaryPermissions.html Required roles and permissions for canaries}.

        :deprecated: Legacy runtime no longer supported by AWS Lambda. Migrate to the latest NodeJS Puppeteer runtime.

        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Library_nodejs_puppeteer.html#CloudWatch_Synthetics_runtimeversion-nodejs-puppeteer-6.1
        :stability: deprecated
        '''
        return typing.cast("Runtime", jsii.sget(cls, "SYNTHETICS_NODEJS_PUPPETEER_6_1"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SYNTHETICS_NODEJS_PUPPETEER_6_2")
    def SYNTHETICS_NODEJS_PUPPETEER_6_2(cls) -> "Runtime":
        '''``syn-nodejs-puppeteer-6.2`` includes the following: - Lambda runtime Node.js 18.x - Puppeteer-core version 19.7.0 - Chromium version 111.0.5563.146.

        New Features:

        - **Updated versions of the bundled libraries in Chromium**
        - **Ephemeral storage monitoring**: This runtime adds ephemeral storage monitoring in customer accounts.
        - **Bug fixes**

        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Library_nodejs_puppeteer.html#CloudWatch_Synthetics_runtimeversion-nodejs-puppeteer-6.1
        '''
        return typing.cast("Runtime", jsii.sget(cls, "SYNTHETICS_NODEJS_PUPPETEER_6_2"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SYNTHETICS_NODEJS_PUPPETEER_7_0")
    def SYNTHETICS_NODEJS_PUPPETEER_7_0(cls) -> "Runtime":
        '''``syn-nodejs-puppeteer-7.0`` includes the following: - Lambda runtime Node.js 18.x - Puppeteer-core version 21.9.0 - Chromium version 121.0.6167.139.

        New Features:

        - **Updated versions of the bundled libraries in Puppeteer and Chromium**: The Puppeteer and Chromium dependencies are updated to new versions.

        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Library_nodejs_puppeteer.html#CloudWatch_Synthetics_runtimeversion-nodejs-puppeteer-7.0
        '''
        return typing.cast("Runtime", jsii.sget(cls, "SYNTHETICS_NODEJS_PUPPETEER_7_0"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SYNTHETICS_PYTHON_SELENIUM_1_0")
    def SYNTHETICS_PYTHON_SELENIUM_1_0(cls) -> "Runtime":
        '''(deprecated) ``syn-python-selenium-1.0`` includes the following: - Lambda runtime Python 3.8 - Selenium version 3.141.0 - Chromium version 83.0.4103.0.

        :deprecated: Legacy runtime no longer supported by AWS Lambda. Migrate to the latest Python Selenium runtime.

        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Library_python_selenium.html#CloudWatch_Synthetics_runtimeversion-syn-python-selenium-1.0
        :stability: deprecated
        '''
        return typing.cast("Runtime", jsii.sget(cls, "SYNTHETICS_PYTHON_SELENIUM_1_0"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SYNTHETICS_PYTHON_SELENIUM_1_1")
    def SYNTHETICS_PYTHON_SELENIUM_1_1(cls) -> "Runtime":
        '''(deprecated) ``syn-python-selenium-1.1`` includes the following: - Lambda runtime Python 3.8 - Selenium version 3.141.0 - Chromium version 83.0.4103.0.

        New Features:

        - **Custom handler function**: You can now use a custom handler function for your canary scripts.
        - **Configuration options for adding metrics and step failure configurations**: These options were already available in runtimes for Node.js canaries.
        - **Custom arguments in Chrome**: You can now open a browser in incognito mode or pass in proxy server configuration.
        - **Cross-Region artifact buckets**: A canary can store its artifacts in an Amazon S3 bucket in a different Region.

        :deprecated: Legacy runtime no longer supported by AWS Lambda. Migrate to the latest Python Selenium runtime.

        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Library_python_selenium.html#CloudWatch_Synthetics_runtimeversion-syn-python-selenium-1.1
        :stability: deprecated
        '''
        return typing.cast("Runtime", jsii.sget(cls, "SYNTHETICS_PYTHON_SELENIUM_1_1"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SYNTHETICS_PYTHON_SELENIUM_1_2")
    def SYNTHETICS_PYTHON_SELENIUM_1_2(cls) -> "Runtime":
        '''(deprecated) ``syn-python-selenium-1.2`` includes the following: - Lambda runtime Python 3.8 - Selenium version 3.141.0 - Chromium version 92.0.4512.0.

        New Features:

        - **Updated dependencies**: The only new features in this runtime are the updated dependencies.

        :deprecated: Legacy runtime no longer supported by AWS Lambda. Migrate to the latest Python Selenium runtime.

        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Library_python_selenium.html#CloudWatch_Synthetics_runtimeversion-syn-python-selenium-1.2
        :stability: deprecated
        '''
        return typing.cast("Runtime", jsii.sget(cls, "SYNTHETICS_PYTHON_SELENIUM_1_2"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SYNTHETICS_PYTHON_SELENIUM_1_3")
    def SYNTHETICS_PYTHON_SELENIUM_1_3(cls) -> "Runtime":
        '''(deprecated) ``syn-python-selenium-1.3`` includes the following: - Lambda runtime Python 3.8 - Selenium version 3.141.0 - Chromium version 92.0.4512.0.

        New Features:

        - **More precise timestamps**: The start time and stop time of canary runs are now precise to the millisecond.

        :deprecated: Legacy runtime no longer supported by AWS Lambda. Migrate to the latest Python Selenium runtime.

        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Library_python_selenium.html#CloudWatch_Synthetics_runtimeversion-syn-python-selenium-1.3
        :stability: deprecated
        '''
        return typing.cast("Runtime", jsii.sget(cls, "SYNTHETICS_PYTHON_SELENIUM_1_3"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SYNTHETICS_PYTHON_SELENIUM_2_0")
    def SYNTHETICS_PYTHON_SELENIUM_2_0(cls) -> "Runtime":
        '''(deprecated) ``syn-python-selenium-2.0`` includes the following: - Lambda runtime Python 3.8 - Selenium version 4.10.0 - Chromium version 111.0.5563.146.

        New Features:

        - **Updated dependencies**: The Chromium and Selenium dependencies are updated to new versions.
        - **More precise timestamps**: The start time and stop time of canary runs are now precise to the millisecond.

        Bug fixes:

        - **Timestamp added**: A timestamp has been added to canary logs.
        - **Session re-use**: A bug was fixed so that canaries are now prevented from reusing the session from their previous canary run.

        :deprecated: Legacy runtime no longer supported by AWS Lambda. Migrate to the latest Python Selenium runtime.

        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Library_python_selenium.html#CloudWatch_Synthetics_runtimeversion-syn-python-selenium-2.0
        :stability: deprecated
        '''
        return typing.cast("Runtime", jsii.sget(cls, "SYNTHETICS_PYTHON_SELENIUM_2_0"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SYNTHETICS_PYTHON_SELENIUM_2_1")
    def SYNTHETICS_PYTHON_SELENIUM_2_1(cls) -> "Runtime":
        '''``syn-python-selenium-2.1`` includes the following: - Lambda runtime Python 3.8 - Selenium version 4.15.1 - Chromium version 111.0.5563.146.

        New Features:

        - **Updated versions of the bundled libraries in Chromium**: The Chromium and Selenium dependencies are updated to new versions.

        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Library_python_selenium.html#CloudWatch_Synthetics_runtimeversion-syn-python-selenium-2.0
        '''
        return typing.cast("Runtime", jsii.sget(cls, "SYNTHETICS_PYTHON_SELENIUM_2_1"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SYNTHETICS_PYTHON_SELENIUM_3_0")
    def SYNTHETICS_PYTHON_SELENIUM_3_0(cls) -> "Runtime":
        '''``syn-python-selenium-3.0`` includes the following: - Lambda runtime Python 3.8 - Selenium version 4.15.1 - Chromium version 121.0.6167.139.

        New Features:

        - **Updated versions of the bundled libraries in Chromium**: The Chromium dependency is updated to a new version.

        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Library_python_selenium.html#CloudWatch_Synthetics_runtimeversion-syn-python-selenium-3.0
        '''
        return typing.cast("Runtime", jsii.sget(cls, "SYNTHETICS_PYTHON_SELENIUM_3_0"))

    @builtins.property
    @jsii.member(jsii_name="family")
    def family(self) -> "RuntimeFamily":
        '''The Lambda runtime family.'''
        return typing.cast("RuntimeFamily", jsii.get(self, "family"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the runtime version.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))


@jsii.enum(jsii_type="aws-cdk-lib.aws_synthetics.RuntimeFamily")
class RuntimeFamily(enum.Enum):
    '''All known Lambda runtime families.'''

    NODEJS = "NODEJS"
    '''All Lambda runtimes that depend on Node.js.'''
    PYTHON = "PYTHON"
    '''All lambda runtimes that depend on Python.'''
    OTHER = "OTHER"
    '''Any future runtime family.'''


class S3Code(
    Code,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_synthetics.S3Code",
):
    '''S3 bucket path to the code zip file.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_s3 as s3
        from aws_cdk import aws_synthetics as synthetics
        
        # bucket: s3.Bucket
        
        s3_code = synthetics.S3Code(bucket, "key", "objectVersion")
    '''

    def __init__(
        self,
        bucket: _IBucket_42e086fd,
        key: builtins.str,
        object_version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket: -
        :param key: -
        :param object_version: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94d1b4f54d462b3f798f1b900a1b75b486a8dc3f4f14650931bf7631ce93a5bd)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument object_version", value=object_version, expected_type=type_hints["object_version"])
        jsii.create(self.__class__, self, [bucket, key, object_version])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _scope: _constructs_77d1e7e8.Construct,
        _handler: builtins.str,
        _family: RuntimeFamily,
    ) -> CodeConfig:
        '''Called when the canary is initialized to allow this object to bind to the stack, add resources and have fun.

        :param _scope: -
        :param _handler: -
        :param _family: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e764381c92bbdf3e70a0cf34a6f1afa9abfa207f9eb030a4ac6823b6e04ab07)
            check_type(argname="argument _scope", value=_scope, expected_type=type_hints["_scope"])
            check_type(argname="argument _handler", value=_handler, expected_type=type_hints["_handler"])
            check_type(argname="argument _family", value=_family, expected_type=type_hints["_family"])
        return typing.cast(CodeConfig, jsii.invoke(self, "bind", [_scope, _handler, _family]))


class Schedule(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_synthetics.Schedule",
):
    '''Schedule for canary runs.

    :exampleMetadata: infused

    Example::

        canary = synthetics.Canary(self, "MyCanary",
            schedule=synthetics.Schedule.rate(Duration.minutes(5)),
            test=synthetics.Test.custom(
                code=synthetics.Code.from_asset(path.join(__dirname, "canary")),
                handler="index.handler"
            ),
            runtime=synthetics.Runtime.SYNTHETICS_NODEJS_PUPPETEER_6_2,
            environment_variables={
                "stage": "prod"
            }
        )
    '''

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
    ) -> "Schedule":
        '''Create a schedule from a set of cron fields.

        :param day: The day of the month to run this rule at. Default: - Every day of the month
        :param hour: The hour to run this rule at. Default: - Every hour
        :param minute: The minute to run this rule at. Default: - Every minute
        :param month: The month to run this rule at. Default: - Every month
        :param week_day: The day of the week to run this rule at. Default: - Any day of the week
        '''
        options = CronOptions(
            day=day, hour=hour, minute=minute, month=month, week_day=week_day
        )

        return typing.cast("Schedule", jsii.sinvoke(cls, "cron", [options]))

    @jsii.member(jsii_name="expression")
    @builtins.classmethod
    def expression(cls, expression: builtins.str) -> "Schedule":
        '''Construct a schedule from a literal schedule expression.

        The expression must be in a ``rate(number units)`` format.
        For example, ``Schedule.expression('rate(10 minutes)')``

        :param expression: The expression to use.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a8334828acbf2ad1c4c442e45a5fc06cb2afe4d6c84839d6e453ee067100a34)
            check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
        return typing.cast("Schedule", jsii.sinvoke(cls, "expression", [expression]))

    @jsii.member(jsii_name="once")
    @builtins.classmethod
    def once(cls) -> "Schedule":
        '''The canary will be executed once.'''
        return typing.cast("Schedule", jsii.sinvoke(cls, "once", []))

    @jsii.member(jsii_name="rate")
    @builtins.classmethod
    def rate(cls, interval: _Duration_4839e8c3) -> "Schedule":
        '''Construct a schedule from an interval.

        Allowed values: 0 (for a single run) or between 1 and 60 minutes.
        To specify a single run, you can use ``Schedule.once()``.

        :param interval: The interval at which to run the canary.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__551eb869b238a461522af26f46eb23c0d3b0fef05c536646aaa672b55e35210a)
            check_type(argname="argument interval", value=interval, expected_type=type_hints["interval"])
        return typing.cast("Schedule", jsii.sinvoke(cls, "rate", [interval]))

    @builtins.property
    @jsii.member(jsii_name="expressionString")
    def expression_string(self) -> builtins.str:
        '''The Schedule expression.'''
        return typing.cast(builtins.str, jsii.get(self, "expressionString"))


class Test(metaclass=jsii.JSIIMeta, jsii_type="aws-cdk-lib.aws_synthetics.Test"):
    '''Specify a test that the canary should run.

    :exampleMetadata: infused

    Example::

        canary = synthetics.Canary(self, "MyCanary",
            schedule=synthetics.Schedule.rate(Duration.minutes(5)),
            test=synthetics.Test.custom(
                code=synthetics.Code.from_asset(path.join(__dirname, "canary")),
                handler="index.handler"
            ),
            runtime=synthetics.Runtime.SYNTHETICS_NODEJS_PUPPETEER_6_2,
            environment_variables={
                "stage": "prod"
            }
        )
    '''

    @jsii.member(jsii_name="custom")
    @builtins.classmethod
    def custom(cls, *, code: Code, handler: builtins.str) -> "Test":
        '''Specify a custom test with your own code.

        :param code: The code of the canary script.
        :param handler: The handler for the code. Must end with ``.handler``.

        :return: ``Test`` associated with the specified Code object
        '''
        options = CustomTestOptions(code=code, handler=handler)

        return typing.cast("Test", jsii.sinvoke(cls, "custom", [options]))

    @builtins.property
    @jsii.member(jsii_name="code")
    def code(self) -> Code:
        '''The code that the canary should run.'''
        return typing.cast(Code, jsii.get(self, "code"))

    @builtins.property
    @jsii.member(jsii_name="handler")
    def handler(self) -> builtins.str:
        '''The handler of the canary.'''
        return typing.cast(builtins.str, jsii.get(self, "handler"))


class AssetCode(
    Code,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_synthetics.AssetCode",
):
    '''Canary code from an Asset.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk as cdk
        from aws_cdk import aws_iam as iam
        from aws_cdk import aws_synthetics as synthetics
        
        # docker_image: cdk.DockerImage
        # grantable: iam.IGrantable
        # local_bundling: cdk.ILocalBundling
        
        asset_code = synthetics.AssetCode("assetPath",
            asset_hash="assetHash",
            asset_hash_type=cdk.AssetHashType.SOURCE,
            bundling=cdk.BundlingOptions(
                image=docker_image,
        
                # the properties below are optional
                bundling_file_access=cdk.BundlingFileAccess.VOLUME_COPY,
                command=["command"],
                entrypoint=["entrypoint"],
                environment={
                    "environment_key": "environment"
                },
                local=local_bundling,
                network="network",
                output_type=cdk.BundlingOutput.ARCHIVED,
                platform="platform",
                security_opt="securityOpt",
                user="user",
                volumes=[cdk.DockerVolume(
                    container_path="containerPath",
                    host_path="hostPath",
        
                    # the properties below are optional
                    consistency=cdk.DockerVolumeConsistency.CONSISTENT
                )],
                volumes_from=["volumesFrom"],
                working_directory="workingDirectory"
            ),
            deploy_time=False,
            exclude=["exclude"],
            follow_symlinks=cdk.SymlinkFollowMode.NEVER,
            ignore_mode=cdk.IgnoreMode.GLOB,
            readers=[grantable]
        )
    '''

    def __init__(
        self,
        asset_path: builtins.str,
        *,
        deploy_time: typing.Optional[builtins.bool] = None,
        readers: typing.Optional[typing.Sequence[_IGrantable_71c4f5de]] = None,
        asset_hash: typing.Optional[builtins.str] = None,
        asset_hash_type: typing.Optional[_AssetHashType_05b67f2d] = None,
        bundling: typing.Optional[typing.Union[_BundlingOptions_588cc936, typing.Dict[builtins.str, typing.Any]]] = None,
        exclude: typing.Optional[typing.Sequence[builtins.str]] = None,
        follow_symlinks: typing.Optional[_SymlinkFollowMode_047ec1f6] = None,
        ignore_mode: typing.Optional[_IgnoreMode_655a98e8] = None,
    ) -> None:
        '''
        :param asset_path: The path to the asset file or directory.
        :param deploy_time: Whether or not the asset needs to exist beyond deployment time; i.e. are copied over to a different location and not needed afterwards. Setting this property to true has an impact on the lifecycle of the asset, because we will assume that it is safe to delete after the CloudFormation deployment succeeds. For example, Lambda Function assets are copied over to Lambda during deployment. Therefore, it is not necessary to store the asset in S3, so we consider those deployTime assets. Default: false
        :param readers: A list of principals that should be able to read this asset from S3. You can use ``asset.grantRead(principal)`` to grant read permissions later. Default: - No principals that can read file asset.
        :param asset_hash: Specify a custom hash for this asset. If ``assetHashType`` is set it must be set to ``AssetHashType.CUSTOM``. For consistency, this custom hash will be SHA256 hashed and encoded as hex. The resulting hash will be the asset hash. NOTE: the hash is used in order to identify a specific revision of the asset, and used for optimizing and caching deployment activities related to this asset such as packaging, uploading to Amazon S3, etc. If you chose to customize the hash, you will need to make sure it is updated every time the asset changes, or otherwise it is possible that some deployments will not be invalidated. Default: - based on ``assetHashType``
        :param asset_hash_type: Specifies the type of hash to calculate for this asset. If ``assetHash`` is configured, this option must be ``undefined`` or ``AssetHashType.CUSTOM``. Default: - the default is ``AssetHashType.SOURCE``, but if ``assetHash`` is explicitly specified this value defaults to ``AssetHashType.CUSTOM``.
        :param bundling: Bundle the asset by executing a command in a Docker container or a custom bundling provider. The asset path will be mounted at ``/asset-input``. The Docker container is responsible for putting content at ``/asset-output``. The content at ``/asset-output`` will be zipped and used as the final asset. Default: - uploaded as-is to S3 if the asset is a regular file or a .zip file, archived into a .zip file and uploaded to S3 otherwise
        :param exclude: File paths matching the patterns will be excluded. See ``ignoreMode`` to set the matching behavior. Has no effect on Assets bundled using the ``bundling`` property. Default: - nothing is excluded
        :param follow_symlinks: A strategy for how to handle symlinks. Default: SymlinkFollowMode.NEVER
        :param ignore_mode: The ignore behavior to use for ``exclude`` patterns. Default: IgnoreMode.GLOB
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60a29a536d66536254f2ca409a65dc32f30e483b29091222d42f32106bd3754f)
            check_type(argname="argument asset_path", value=asset_path, expected_type=type_hints["asset_path"])
        options = _AssetOptions_2aa69621(
            deploy_time=deploy_time,
            readers=readers,
            asset_hash=asset_hash,
            asset_hash_type=asset_hash_type,
            bundling=bundling,
            exclude=exclude,
            follow_symlinks=follow_symlinks,
            ignore_mode=ignore_mode,
        )

        jsii.create(self.__class__, self, [asset_path, options])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        scope: _constructs_77d1e7e8.Construct,
        handler: builtins.str,
        family: RuntimeFamily,
    ) -> CodeConfig:
        '''Called when the canary is initialized to allow this object to bind to the stack, add resources and have fun.

        :param scope: -
        :param handler: -
        :param family: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dcf81e22fccedf5b193b8ec9218200abb14bc77d3601c5cd7edbedda5914c393)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument handler", value=handler, expected_type=type_hints["handler"])
            check_type(argname="argument family", value=family, expected_type=type_hints["family"])
        return typing.cast(CodeConfig, jsii.invoke(self, "bind", [scope, handler, family]))


__all__ = [
    "ArtifactsBucketLocation",
    "AssetCode",
    "Canary",
    "CanaryProps",
    "CfnCanary",
    "CfnCanaryProps",
    "CfnGroup",
    "CfnGroupProps",
    "Cleanup",
    "Code",
    "CodeConfig",
    "CronOptions",
    "CustomTestOptions",
    "InlineCode",
    "Runtime",
    "RuntimeFamily",
    "S3Code",
    "Schedule",
    "Test",
]

publication.publish()

def _typecheckingstub__a3f4adf0ebd4ec63bde8a045a448259a907ff7a524c6a3b4503e1797b05a9d5f(
    *,
    bucket: _IBucket_42e086fd,
    prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3b6d76e5f93e31884e16cc00a9b4fc93e6782ff7db09c74aa1ef9346f53ccb0(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    runtime: Runtime,
    test: Test,
    artifacts_bucket_lifecycle_rules: typing.Optional[typing.Sequence[typing.Union[_LifecycleRule_bb74e6ff, typing.Dict[builtins.str, typing.Any]]]] = None,
    artifacts_bucket_location: typing.Optional[typing.Union[ArtifactsBucketLocation, typing.Dict[builtins.str, typing.Any]]] = None,
    canary_name: typing.Optional[builtins.str] = None,
    cleanup: typing.Optional[Cleanup] = None,
    environment_variables: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    failure_retention_period: typing.Optional[_Duration_4839e8c3] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
    schedule: typing.Optional[Schedule] = None,
    security_groups: typing.Optional[typing.Sequence[_ISecurityGroup_acf8a799]] = None,
    start_after_creation: typing.Optional[builtins.bool] = None,
    success_retention_period: typing.Optional[_Duration_4839e8c3] = None,
    time_to_live: typing.Optional[_Duration_4839e8c3] = None,
    vpc: typing.Optional[_IVpc_f30d5663] = None,
    vpc_subnets: typing.Optional[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44ec0b14d52b66927d4daebe6f97bb070f3629bb0eb86e21668ca7862bb5f5bd(
    *,
    runtime: Runtime,
    test: Test,
    artifacts_bucket_lifecycle_rules: typing.Optional[typing.Sequence[typing.Union[_LifecycleRule_bb74e6ff, typing.Dict[builtins.str, typing.Any]]]] = None,
    artifacts_bucket_location: typing.Optional[typing.Union[ArtifactsBucketLocation, typing.Dict[builtins.str, typing.Any]]] = None,
    canary_name: typing.Optional[builtins.str] = None,
    cleanup: typing.Optional[Cleanup] = None,
    environment_variables: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    failure_retention_period: typing.Optional[_Duration_4839e8c3] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
    schedule: typing.Optional[Schedule] = None,
    security_groups: typing.Optional[typing.Sequence[_ISecurityGroup_acf8a799]] = None,
    start_after_creation: typing.Optional[builtins.bool] = None,
    success_retention_period: typing.Optional[_Duration_4839e8c3] = None,
    time_to_live: typing.Optional[_Duration_4839e8c3] = None,
    vpc: typing.Optional[_IVpc_f30d5663] = None,
    vpc_subnets: typing.Optional[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8fcb3f48eca9399b4d1d31a5ef709e22f9fa52ad1e174b75d8313ef2b971663(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    artifact_s3_location: builtins.str,
    code: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCanary.CodeProperty, typing.Dict[builtins.str, typing.Any]]],
    execution_role_arn: builtins.str,
    name: builtins.str,
    runtime_version: builtins.str,
    schedule: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCanary.ScheduleProperty, typing.Dict[builtins.str, typing.Any]]],
    artifact_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCanary.ArtifactConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    delete_lambda_resources_on_canary_deletion: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    failure_retention_period: typing.Optional[jsii.Number] = None,
    run_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCanary.RunConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    start_canary_after_creation: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    success_retention_period: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    visual_reference: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCanary.VisualReferenceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    vpc_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCanary.VPCConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc166bab0fcf177897c1dbb233203e39458428064bc6ff7215b01b2b3ec6f3a2(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65410bca39459dd8b2ef582ab37870de468cb765034b9600759877910b340355(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cdaba4ac1ed08cbb682b002e6d07aabeaccadbe7c5a6d4bbbc1aaaa15bb4831c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__940d05df3a63f7ad05e985fa05317d4b896a6a845409a8d700cbf186fd8e49d5(
    value: typing.Union[_IResolvable_da3f097b, CfnCanary.CodeProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21989f82228cbbd4b8df02c1285ab8cf3635cf4eb894f4a4c999e6b763e92ded(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02a5568fdb7b5da09cb493a9883d04e695a0b6375532601c26ea6ba719fd869a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64f9d8326de93a51cdd4ab89bc4c5431c218c9b46372d81f4fe7a8961b26fa2c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e387628a17b84461f77d8fdc851f2b16bcda58e50d8e9279d02062270a5516f0(
    value: typing.Union[_IResolvable_da3f097b, CfnCanary.ScheduleProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5946ee35eff32e4581a6d2e3e0c69d62cdc3c17f079123211f7251bc1a10d878(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCanary.ArtifactConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__442577c2c36e4274dca25b3d866e1aeec3f4ffc18732e01050131a31f768f2b3(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02a7e43f45419c4cb8e909f309f8848d4ced91d17b01d14e5ea0b8cec28aab1b(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e65fb80249e43aebfe46950832be73ed0795003be5d74ca1ef7cd12bb2408557(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCanary.RunConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a98feaf45022b36ef5c9888f87b978029d5e1fde70599e1972543b1778adfad(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8bbba327f646025c54903ccf2c19cedc26cf07f79658c389f65ef40b263130f(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__212d1e59a4bd96a18f447b1c742abcfeb7c668063c8e1670fa0770e339ac4077(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21e93a70969fa03a3f0aa85f6b1615a26d9a0afef8a0cf27f0888fc59aef420b(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCanary.VisualReferenceProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be63ed6816e3043aef63f6e7c0d0dfcc35f1249735acd4eff8530f8c2253b747(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCanary.VPCConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c456e72742651aec26b46a7fbd663821284d03931fd10859243079b815dad28(
    *,
    s3_encryption: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCanary.S3EncryptionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d401a2416919aef18322e23fb875fc37ad8f90f34f8f5708a245f22f9d3208f(
    *,
    screenshot_name: builtins.str,
    ignore_coordinates: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d403372a613babc1ab10717d050ec9a7f4055961f3545f2d0600d89c7b3dcc3(
    *,
    handler: builtins.str,
    s3_bucket: typing.Optional[builtins.str] = None,
    s3_key: typing.Optional[builtins.str] = None,
    s3_object_version: typing.Optional[builtins.str] = None,
    script: typing.Optional[builtins.str] = None,
    source_location_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa148862e82948accbbe951e7afcee721aa7014754c81106d2648fe1c5cf28e2(
    *,
    active_tracing: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    environment_variables: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
    memory_in_mb: typing.Optional[jsii.Number] = None,
    timeout_in_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__551aad28104a61040e1d9e12e77c77ae47c6e19a45d15bfa94e441c5d297d3ab(
    *,
    encryption_mode: typing.Optional[builtins.str] = None,
    kms_key_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4999288d0e0c5de04c56a3436208778026602dfdca27710aee93f9f4e034c29(
    *,
    expression: builtins.str,
    duration_in_seconds: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eccfde82eb2354e9c416fba506f2ff8e4fb1a86792529f65e2d8eafbc8415074(
    *,
    security_group_ids: typing.Sequence[builtins.str],
    subnet_ids: typing.Sequence[builtins.str],
    vpc_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f52b6b7318141dc99f6bd36c21b91cda286b67d7dea805791a6132a2cd794526(
    *,
    base_canary_run_id: builtins.str,
    base_screenshots: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCanary.BaseScreenshotProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d869d56ce0d1d2e2add2f80bf39b28abbec2752c719e03194ee540bf1949e423(
    *,
    artifact_s3_location: builtins.str,
    code: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCanary.CodeProperty, typing.Dict[builtins.str, typing.Any]]],
    execution_role_arn: builtins.str,
    name: builtins.str,
    runtime_version: builtins.str,
    schedule: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCanary.ScheduleProperty, typing.Dict[builtins.str, typing.Any]]],
    artifact_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCanary.ArtifactConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    delete_lambda_resources_on_canary_deletion: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    failure_retention_period: typing.Optional[jsii.Number] = None,
    run_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCanary.RunConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    start_canary_after_creation: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    success_retention_period: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    visual_reference: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCanary.VisualReferenceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    vpc_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCanary.VPCConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__973b5b11ee0c26a7aa94d55785d1a025e0c569700b7877564d84ae1447c2af09(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    resource_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c02721081747307dfd2212f0ae4958cfbad3dc1ec5b0667712fb08ebd5d7e65(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4dd500824b1b77e386dc3d0eca110f83c00176cc9ac0861387258adf2b7914e(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6401b033d62b6cede0e2328e1f7c75c5607ed33e285fb529afce4814a3551bee(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__078802d6cab1e35c6ba04d10e648f52314cd74f1c2d198563fb8a7d6435999ba(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d85cd0ddf465884c3990e0492b92e22606ecfb33b8127bf42d0c344b78427aa(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ab100d4133b5b7bd6483c4c3bcf827df685974681f592679f7de8f8ea64b33f(
    *,
    name: builtins.str,
    resource_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02201c2190b076bbceced8708b435fab8189f7f505650002941cc7a50e23adff(
    asset_path: builtins.str,
    *,
    deploy_time: typing.Optional[builtins.bool] = None,
    readers: typing.Optional[typing.Sequence[_IGrantable_71c4f5de]] = None,
    asset_hash: typing.Optional[builtins.str] = None,
    asset_hash_type: typing.Optional[_AssetHashType_05b67f2d] = None,
    bundling: typing.Optional[typing.Union[_BundlingOptions_588cc936, typing.Dict[builtins.str, typing.Any]]] = None,
    exclude: typing.Optional[typing.Sequence[builtins.str]] = None,
    follow_symlinks: typing.Optional[_SymlinkFollowMode_047ec1f6] = None,
    ignore_mode: typing.Optional[_IgnoreMode_655a98e8] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__449747bf42ca4f0c5864a72ad8bd3bcd8b8dedef173ae2e8a54e213a343068a6(
    bucket: _IBucket_42e086fd,
    key: builtins.str,
    object_version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72d5e409f31e6e624d17b0671dedc0be55eeb0d3f459389a05661b94b0f5d0ab(
    code: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16072f2291ff792418a957a399b7ca3a9d2e16cb1e67d33d5682dbb0eebaf541(
    scope: _constructs_77d1e7e8.Construct,
    handler: builtins.str,
    family: RuntimeFamily,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a34e85aaf9472ee1bd9ebc1e0c43060979cf58692956f81c385d453a371973e(
    *,
    inline_code: typing.Optional[builtins.str] = None,
    s3_location: typing.Optional[typing.Union[_Location_0948fa7f, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f80f44d8794a637e9994828c4264f001f407cac43a28d1b0c7e51bb7487337d(
    *,
    day: typing.Optional[builtins.str] = None,
    hour: typing.Optional[builtins.str] = None,
    minute: typing.Optional[builtins.str] = None,
    month: typing.Optional[builtins.str] = None,
    week_day: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__998aa034b450d34cd7535661c029c2c24a7a34b950b79e5a2b055d31ab5ea31d(
    *,
    code: Code,
    handler: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e4d6f25be5e212e7eccf81a0bb26d92760fb4f335d2fd7395acbdc376c975d2(
    code: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c1dddac73b46d6693b6032065ae6db988e1e76cb520ebf3d4aa58e532f543a9(
    _scope: _constructs_77d1e7e8.Construct,
    handler: builtins.str,
    _family: RuntimeFamily,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba23a2bd20fc9334e4b0fac6e1c104de0f53b4ec265cf53ef1a80ad25868f780(
    name: builtins.str,
    family: RuntimeFamily,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94d1b4f54d462b3f798f1b900a1b75b486a8dc3f4f14650931bf7631ce93a5bd(
    bucket: _IBucket_42e086fd,
    key: builtins.str,
    object_version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e764381c92bbdf3e70a0cf34a6f1afa9abfa207f9eb030a4ac6823b6e04ab07(
    _scope: _constructs_77d1e7e8.Construct,
    _handler: builtins.str,
    _family: RuntimeFamily,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a8334828acbf2ad1c4c442e45a5fc06cb2afe4d6c84839d6e453ee067100a34(
    expression: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__551eb869b238a461522af26f46eb23c0d3b0fef05c536646aaa672b55e35210a(
    interval: _Duration_4839e8c3,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60a29a536d66536254f2ca409a65dc32f30e483b29091222d42f32106bd3754f(
    asset_path: builtins.str,
    *,
    deploy_time: typing.Optional[builtins.bool] = None,
    readers: typing.Optional[typing.Sequence[_IGrantable_71c4f5de]] = None,
    asset_hash: typing.Optional[builtins.str] = None,
    asset_hash_type: typing.Optional[_AssetHashType_05b67f2d] = None,
    bundling: typing.Optional[typing.Union[_BundlingOptions_588cc936, typing.Dict[builtins.str, typing.Any]]] = None,
    exclude: typing.Optional[typing.Sequence[builtins.str]] = None,
    follow_symlinks: typing.Optional[_SymlinkFollowMode_047ec1f6] = None,
    ignore_mode: typing.Optional[_IgnoreMode_655a98e8] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dcf81e22fccedf5b193b8ec9218200abb14bc77d3601c5cd7edbedda5914c393(
    scope: _constructs_77d1e7e8.Construct,
    handler: builtins.str,
    family: RuntimeFamily,
) -> None:
    """Type checking stubs"""
    pass
