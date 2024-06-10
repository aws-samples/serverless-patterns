'''
# AWS AppConfig Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

For a high level overview of what AWS AppConfig is and how it works, please take a look here:
[What is AWS AppConfig?](https://docs.aws.amazon.com/appconfig/latest/userguide/what-is-appconfig.html)

## Basic Hosted Configuration Use Case

> The main way most AWS AppConfig users utilize the service is through hosted configuration, which involves storing
> configuration data directly within AWS AppConfig.

An example use case:

```python
app = appconfig.Application(self, "MyApp")
env = appconfig.Environment(self, "MyEnv",
    application=app
)

appconfig.HostedConfiguration(self, "MyHostedConfig",
    application=app,
    deploy_to=[env],
    content=appconfig.ConfigurationContent.from_inline_text("This is my configuration content.")
)
```

This will create the application and environment for your configuration and then deploy your configuration to the
specified environment.

For more information about what these resources are: [Creating feature flags and free form configuration data in AWS AppConfig](https://docs.aws.amazon.com/appconfig/latest/userguide/creating-feature-flags-and-configuration-data.html).

For more information about deploying configuration: [Deploying feature flags and configuration data in AWS AppConfig](https://docs.aws.amazon.com/appconfig/latest/userguide/deploying-feature-flags.html)

---


For an in-depth walkthrough of specific resources and how to use them, please take a look at the following sections.

## Application

[AWS AppConfig Application Documentation](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-namespace.html)

In AWS AppConfig, an application is simply an organizational
construct like a folder. Configurations and environments are
associated with the application.

When creating an application through CDK, the name and
description of an application are optional.

Create a simple application:

```python
appconfig.Application(self, "MyApplication")
```

## Environment

[AWS AppConfig Environment Documentation](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-environment.html)

Basic environment with monitors:

```python
# application: appconfig.Application
# alarm: cloudwatch.Alarm
# composite_alarm: cloudwatch.CompositeAlarm


appconfig.Environment(self, "MyEnvironment",
    application=application,
    monitors=[
        appconfig.Monitor.from_cloud_watch_alarm(alarm),
        appconfig.Monitor.from_cloud_watch_alarm(composite_alarm)
    ]
)
```

Environment monitors also support L1 `CfnEnvironment.MonitorsProperty` constructs through the `fromCfnMonitorsProperty` method.
However, this is not the recommended approach for CloudWatch alarms because a role will not be auto-generated if not provided.

See [About the AWS AppConfig data plane service](https://docs.aws.amazon.com/appconfig/latest/userguide/about-data-plane.html) for more information.

### Permissions

You can grant read permission on the environment's configurations with the grantReadConfig method as follows:

```python
import aws_cdk.aws_iam as iam


app = appconfig.Application(self, "MyAppConfig")
env = appconfig.Environment(self, "MyEnvironment",
    application=app
)

user = iam.User(self, "MyUser")
env.grant_read_config(user)
```

## Deployment Strategy

[AWS AppConfig Deployment Strategy Documentation](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-deployment-strategy.html)

A deployment strategy defines how a configuration will roll out. The roll out is defined by four parameters: deployment type,
growth factor, deployment duration, and final bake time.

Deployment strategy with predefined values:

```python
appconfig.DeploymentStrategy(self, "MyDeploymentStrategy",
    rollout_strategy=appconfig.RolloutStrategy.CANARY_10_PERCENT_20_MINUTES
)
```

Deployment strategy with custom values:

```python
appconfig.DeploymentStrategy(self, "MyDeploymentStrategy",
    rollout_strategy=appconfig.RolloutStrategy.linear(
        growth_factor=20,
        deployment_duration=Duration.minutes(30),
        final_bake_time=Duration.minutes(30)
    )
)
```

Referencing a deployment strategy by ID:

```python
appconfig.DeploymentStrategy.from_deployment_strategy_id(self, "MyImportedDeploymentStrategy", appconfig.DeploymentStrategyId.from_string("abc123"))
```

Referencing an AWS AppConfig predefined deployment strategy by ID:

```python
appconfig.DeploymentStrategy.from_deployment_strategy_id(self, "MyImportedPredefinedDeploymentStrategy", appconfig.DeploymentStrategyId.CANARY_10_PERCENT_20_MINUTES)
```

## Configuration

A configuration is a higher-level construct that can either be a `HostedConfiguration` (stored internally through AWS
AppConfig) or a `SourcedConfiguration` (stored in an Amazon S3 bucket, AWS Secrets Manager secrets, Systems Manager (SSM)
Parameter Store parameters, SSM documents, or AWS CodePipeline). This construct manages deployments on creation.

### HostedConfiguration

A hosted configuration represents configuration stored in the AWS AppConfig hosted configuration store. A hosted configuration
takes in the configuration content and associated AWS AppConfig application. On construction of a hosted configuration, the
configuration is deployed.

You can define hosted configuration content using any of the following ConfigurationContent methods:

* `fromFile` - Defines the hosted configuration content from a file (you can specify a relative path). The content type will
  be determined by the file extension unless specified.

```python
# application: appconfig.Application


appconfig.HostedConfiguration(self, "MyHostedConfiguration",
    application=application,
    content=appconfig.ConfigurationContent.from_file("config.json")
)
```

* `fromInlineText` - Defines the hosted configuration from inline text. The content type will be set as `text/plain`.

```python
# application: appconfig.Application


appconfig.HostedConfiguration(self, "MyHostedConfiguration",
    application=application,
    content=appconfig.ConfigurationContent.from_inline_text("This is my configuration content.")
)
```

* `fromInlineJson` - Defines the hosted configuration from inline JSON. The content type will be set as `application/json` unless specified.

```python
# application: appconfig.Application


appconfig.HostedConfiguration(self, "MyHostedConfiguration",
    application=application,
    content=appconfig.ConfigurationContent.from_inline_json("{}")
)
```

* `fromInlineYaml` - Defines the hosted configuration from inline YAML. The content type will be set as `application/x-yaml`.

```python
# application: appconfig.Application


appconfig.HostedConfiguration(self, "MyHostedConfiguration",
    application=application,
    content=appconfig.ConfigurationContent.from_inline_yaml("MyConfig: This is my content.")
)
```

* `fromInline` - Defines the hosted configuration from user-specified content types. The content type will be set as `application/octet-stream` unless specified.

```python
# application: appconfig.Application


appconfig.HostedConfiguration(self, "MyHostedConfiguration",
    application=application,
    content=appconfig.ConfigurationContent.from_inline("This is my configuration content.")
)
```

AWS AppConfig supports the following types of configuration profiles.

* **[Feature flag](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-configuration-and-profile-feature-flags.html)**: Use a feature flag configuration to turn on new features that require a timely deployment, such as a product launch or announcement.
* **[Freeform](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-free-form-configurations-creating.html)**: Use a freeform configuration to carefully introduce changes to your application.

A hosted configuration with type:

```python
# application: appconfig.Application


appconfig.HostedConfiguration(self, "MyHostedConfiguration",
    application=application,
    content=appconfig.ConfigurationContent.from_inline_text("This is my configuration content."),
    type=appconfig.ConfigurationType.FEATURE_FLAGS
)
```

When you create a configuration and configuration profile, you can specify up to two validators. A validator ensures that your
configuration data is syntactically and semantically correct. You can create validators in either JSON Schema or as an AWS
Lambda function.
See [About validators](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-configuration-and-profile.html#appconfig-creating-configuration-and-profile-validators) for more information.

When you import a JSON Schema validator from a file, you can pass in a relative path.

A hosted configuration with validators:

```python
# application: appconfig.Application
# fn: lambda.Function


appconfig.HostedConfiguration(self, "MyHostedConfiguration",
    application=application,
    content=appconfig.ConfigurationContent.from_inline_text("This is my configuration content."),
    validators=[
        appconfig.JsonSchemaValidator.from_file("schema.json"),
        appconfig.LambdaValidator.from_function(fn)
    ]
)
```

You can attach a deployment strategy (as described in the previous section) to your configuration to specify how you want your
configuration to roll out.

A hosted configuration with a deployment strategy:

```python
# application: appconfig.Application


appconfig.HostedConfiguration(self, "MyHostedConfiguration",
    application=application,
    content=appconfig.ConfigurationContent.from_inline_text("This is my configuration content."),
    deployment_strategy=appconfig.DeploymentStrategy(self, "MyDeploymentStrategy",
        rollout_strategy=appconfig.RolloutStrategy.linear(
            growth_factor=15,
            deployment_duration=Duration.minutes(30),
            final_bake_time=Duration.minutes(15)
        )
    )
)
```

The `deployTo` parameter is used to specify which environments to deploy the configuration to.

A hosted configuration with `deployTo`:

```python
# application: appconfig.Application
# env: appconfig.Environment


appconfig.HostedConfiguration(self, "MyHostedConfiguration",
    application=application,
    content=appconfig.ConfigurationContent.from_inline_text("This is my configuration content."),
    deploy_to=[env]
)
```

When more than one configuration is set to deploy to the same environment, the
deployments will occur one at a time. This is done to satisfy
[AppConfig's constraint](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-deploying.html):

> [!NOTE]
> You can only deploy one configuration at a time to an environment.
> However, you can deploy one configuration each to different environments at the same time.

The deployment order matches the order in which the configurations are declared.

```python
app = appconfig.Application(self, "MyApp")
env = appconfig.Environment(self, "MyEnv",
    application=app
)

appconfig.HostedConfiguration(self, "MyFirstHostedConfig",
    application=app,
    deploy_to=[env],
    content=appconfig.ConfigurationContent.from_inline_text("This is my first configuration content.")
)

appconfig.HostedConfiguration(self, "MySecondHostedConfig",
    application=app,
    deploy_to=[env],
    content=appconfig.ConfigurationContent.from_inline_text("This is my second configuration content.")
)
```

If an application would benefit from a deployment order that differs from the
declared order, you can defer the decision by using `IEnvironment.addDeployment`
rather than the `deployTo` property.
In this example, `firstConfig` will be deployed before `secondConfig`.

```python
app = appconfig.Application(self, "MyApp")
env = appconfig.Environment(self, "MyEnv",
    application=app
)

second_config = appconfig.HostedConfiguration(self, "MySecondHostedConfig",
    application=app,
    content=appconfig.ConfigurationContent.from_inline_text("This is my second configuration content.")
)

first_config = appconfig.HostedConfiguration(self, "MyFirstHostedConfig",
    application=app,
    deploy_to=[env],
    content=appconfig.ConfigurationContent.from_inline_text("This is my first configuration content.")
)

env.add_deployment(second_config)
```

Alternatively, you can defer multiple deployments in favor of
`IEnvironment.addDeployments`, which allows you to declare multiple
configurations in the order they will be deployed.
In this example the deployment order will be
`firstConfig`, then `secondConfig`, and finally `thirdConfig`.

```python
app = appconfig.Application(self, "MyApp")
env = appconfig.Environment(self, "MyEnv",
    application=app
)

second_config = appconfig.HostedConfiguration(self, "MySecondHostedConfig",
    application=app,
    content=appconfig.ConfigurationContent.from_inline_text("This is my second configuration content.")
)

third_config = appconfig.HostedConfiguration(self, "MyThirdHostedConfig",
    application=app,
    content=appconfig.ConfigurationContent.from_inline_text("This is my third configuration content.")
)

first_config = appconfig.HostedConfiguration(self, "MyFirstHostedConfig",
    application=app,
    content=appconfig.ConfigurationContent.from_inline_text("This is my first configuration content.")
)

env.add_deployments(first_config, second_config, third_config)
```

Any mix of `deployTo`, `addDeployment`, and `addDeployments` is permitted.
The declaration order will be respected regardless of the approach used.

> [!IMPORTANT]
> If none of these options are utilized, there will not be any deployments.

### SourcedConfiguration

A sourced configuration represents configuration stored in any of the following:

* Amazon S3 bucket
* AWS Secrets Manager secret
* Systems Manager
* (SSM) Parameter Store parameter
* SSM document
* AWS CodePipeline.

A sourced configuration takes in the location source
construct and optionally a version number to deploy. On construction of a sourced configuration, the configuration is deployed
only if a version number is specified.

### S3

Use an Amazon S3 bucket to store a configuration.

```python
# application: appconfig.Application


bucket = s3.Bucket(self, "MyBucket",
    versioned=True
)

appconfig.SourcedConfiguration(self, "MySourcedConfiguration",
    application=application,
    location=appconfig.ConfigurationSource.from_bucket(bucket, "path/to/file.json")
)
```

Use an encrypted bucket:

```python
# application: appconfig.Application


bucket = s3.Bucket(self, "MyBucket",
    versioned=True,
    encryption=s3.BucketEncryption.KMS
)

appconfig.SourcedConfiguration(self, "MySourcedConfiguration",
    application=application,
    location=appconfig.ConfigurationSource.from_bucket(bucket, "path/to/file.json")
)
```

### AWS Secrets Manager secret

Use a Secrets Manager secret to store a configuration.

```python
# application: appconfig.Application
# secret: secrets.Secret


appconfig.SourcedConfiguration(self, "MySourcedConfiguration",
    application=application,
    location=appconfig.ConfigurationSource.from_secret(secret)
)
```

### SSM Parameter Store parameter

Use an SSM parameter to store a configuration.

```python
# application: appconfig.Application
# parameter: ssm.StringParameter


appconfig.SourcedConfiguration(self, "MySourcedConfiguration",
    application=application,
    location=appconfig.ConfigurationSource.from_parameter(parameter),
    version_number="1"
)
```

### SSM document

Use an SSM document to store a configuration.

```python
# application: appconfig.Application
# document: ssm.CfnDocument


appconfig.SourcedConfiguration(self, "MySourcedConfiguration",
    application=application,
    location=appconfig.ConfigurationSource.from_cfn_document(document)
)
```

### AWS CodePipeline

Use an AWS CodePipeline pipeline to store a configuration.

```python
# application: appconfig.Application
# pipeline: codepipeline.Pipeline


appconfig.SourcedConfiguration(self, "MySourcedConfiguration",
    application=application,
    location=appconfig.ConfigurationSource.from_pipeline(pipeline)
)
```

Similar to a hosted configuration, a sourced configuration can optionally take in a type, validators, a `deployTo` parameter, and a deployment strategy.

A sourced configuration with type:

```python
# application: appconfig.Application
# bucket: s3.Bucket


appconfig.SourcedConfiguration(self, "MySourcedConfiguration",
    application=application,
    location=appconfig.ConfigurationSource.from_bucket(bucket, "path/to/file.json"),
    type=appconfig.ConfigurationType.FEATURE_FLAGS,
    name="MyConfig",
    description="This is my sourced configuration from CDK."
)
```

A sourced configuration with validators:

```python
# application: appconfig.Application
# bucket: s3.Bucket
# fn: lambda.Function


appconfig.SourcedConfiguration(self, "MySourcedConfiguration",
    application=application,
    location=appconfig.ConfigurationSource.from_bucket(bucket, "path/to/file.json"),
    validators=[
        appconfig.JsonSchemaValidator.from_file("schema.json"),
        appconfig.LambdaValidator.from_function(fn)
    ]
)
```

A sourced configuration with a deployment strategy:

```python
# application: appconfig.Application
# bucket: s3.Bucket


appconfig.SourcedConfiguration(self, "MySourcedConfiguration",
    application=application,
    location=appconfig.ConfigurationSource.from_bucket(bucket, "path/to/file.json"),
    deployment_strategy=appconfig.DeploymentStrategy(self, "MyDeploymentStrategy",
        rollout_strategy=appconfig.RolloutStrategy.linear(
            growth_factor=15,
            deployment_duration=Duration.minutes(30),
            final_bake_time=Duration.minutes(15)
        )
    )
)
```

## Extension

An extension augments your ability to inject logic or behavior at different points during the AWS AppConfig workflow of
creating or deploying a configuration.
See: https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions.html

### AWS Lambda destination

Use an AWS Lambda as the event destination for an extension.

```python
# fn: lambda.Function


appconfig.Extension(self, "MyExtension",
    actions=[
        appconfig.Action(
            action_points=[appconfig.ActionPoint.ON_DEPLOYMENT_START],
            event_destination=appconfig.LambdaDestination(fn)
        )
    ]
)
```

Lambda extension with parameters:

```python
# fn: lambda.Function


appconfig.Extension(self, "MyExtension",
    actions=[
        appconfig.Action(
            action_points=[appconfig.ActionPoint.ON_DEPLOYMENT_START],
            event_destination=appconfig.LambdaDestination(fn)
        )
    ],
    parameters=[
        appconfig.Parameter.required("testParam", "true"),
        appconfig.Parameter.not_required("testNotRequiredParam")
    ]
)
```

### Amazon Simple Queue Service (SQS) destination

Use a queue as the event destination for an extension.

```python
# queue: sqs.Queue


appconfig.Extension(self, "MyExtension",
    actions=[
        appconfig.Action(
            action_points=[appconfig.ActionPoint.ON_DEPLOYMENT_START],
            event_destination=appconfig.SqsDestination(queue)
        )
    ]
)
```

### Amazon Simple Notification Service (SNS) destination

Use an SNS topic as the event destination for an extension.

```python
# topic: sns.Topic


appconfig.Extension(self, "MyExtension",
    actions=[
        appconfig.Action(
            action_points=[appconfig.ActionPoint.ON_DEPLOYMENT_START],
            event_destination=appconfig.SnsDestination(topic)
        )
    ]
)
```

### Amazon EventBridge destination

Use the default event bus as the event destination for an extension.

```python
bus = events.EventBus.from_event_bus_name(self, "MyEventBus", "default")

appconfig.Extension(self, "MyExtension",
    actions=[
        appconfig.Action(
            action_points=[appconfig.ActionPoint.ON_DEPLOYMENT_START],
            event_destination=appconfig.EventBridgeDestination(bus)
        )
    ]
)
```

You can also add extensions and their associations directly by calling `onDeploymentComplete()` or any other action point
method on the AWS AppConfig application, configuration, or environment resource. To add an association to an existing
extension, you can call `addExtension()` on the resource.

Adding an association to an AWS AppConfig application:

```python
# application: appconfig.Application
# extension: appconfig.Extension
# lambda_destination: appconfig.LambdaDestination


application.add_extension(extension)
application.on_deployment_complete(lambda_destination)
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
    ITaggableV2 as _ITaggableV2_4e6798f8,
    Resource as _Resource_45bc6135,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)
from ..aws_cloudwatch import IAlarm as _IAlarm_ff3eabc0
from ..aws_codepipeline import IPipeline as _IPipeline_0931f838
from ..aws_ecs import TaskDefinition as _TaskDefinition_a541a103
from ..aws_events import IEventBus as _IEventBus_88d13111
from ..aws_iam import (
    Grant as _Grant_a7ae64f8,
    IGrantable as _IGrantable_71c4f5de,
    IRole as _IRole_235f5d8e,
    PolicyDocument as _PolicyDocument_3ac34393,
)
from ..aws_kms import IKey as _IKey_5f11635f
from ..aws_lambda import (
    Function as _Function_244f85d8, IFunction as _IFunction_6adb0ab8
)
from ..aws_s3 import IBucket as _IBucket_42e086fd
from ..aws_secretsmanager import ISecret as _ISecret_6e020e6a
from ..aws_sns import ITopic as _ITopic_9eca4852
from ..aws_sqs import IQueue as _IQueue_7ed6f679
from ..aws_ssm import (
    CfnDocument as _CfnDocument_8b177f00, IParameter as _IParameter_509a0f80
)


class Action(metaclass=jsii.JSIIMeta, jsii_type="aws-cdk-lib.aws_appconfig.Action"):
    '''Defines an action for an extension.

    :exampleMetadata: infused

    Example::

        # fn: lambda.Function
        
        
        appconfig.Extension(self, "MyExtension",
            actions=[
                appconfig.Action(
                    action_points=[appconfig.ActionPoint.ON_DEPLOYMENT_START],
                    event_destination=appconfig.LambdaDestination(fn)
                )
            ]
        )
    '''

    def __init__(
        self,
        *,
        action_points: typing.Sequence["ActionPoint"],
        event_destination: "IEventDestination",
        description: typing.Optional[builtins.str] = None,
        execution_role: typing.Optional[_IRole_235f5d8e] = None,
        invoke_without_execution_role: typing.Optional[builtins.bool] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param action_points: The action points that will trigger the extension action.
        :param event_destination: The event destination for the action.
        :param description: The description for the action. Default: - No description.
        :param execution_role: The execution role for the action. Default: - A role is generated.
        :param invoke_without_execution_role: The flag that specifies whether or not to create the execution role. If set to true, then the role will not be auto-generated under the assumption there is already the corresponding resource-based policy attached to the event destination. If false, the execution role will be generated if not provided. Default: false
        :param name: The name for the action. Default: - A name is generated.
        '''
        props = ActionProps(
            action_points=action_points,
            event_destination=event_destination,
            description=description,
            execution_role=execution_role,
            invoke_without_execution_role=invoke_without_execution_role,
            name=name,
        )

        jsii.create(self.__class__, self, [props])

    @builtins.property
    @jsii.member(jsii_name="actionPoints")
    def action_points(self) -> typing.List["ActionPoint"]:
        '''The action points that will trigger the extension action.'''
        return typing.cast(typing.List["ActionPoint"], jsii.get(self, "actionPoints"))

    @builtins.property
    @jsii.member(jsii_name="eventDestination")
    def event_destination(self) -> "IEventDestination":
        '''The event destination for the action.'''
        return typing.cast("IEventDestination", jsii.get(self, "eventDestination"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description for the action.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @builtins.property
    @jsii.member(jsii_name="executionRole")
    def execution_role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''The execution role for the action.'''
        return typing.cast(typing.Optional[_IRole_235f5d8e], jsii.get(self, "executionRole"))

    @builtins.property
    @jsii.member(jsii_name="invokeWithoutExecutionRole")
    def invoke_without_execution_role(self) -> typing.Optional[builtins.bool]:
        '''The flag that specifies whether to create the execution role.'''
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "invokeWithoutExecutionRole"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name for the action.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))


@jsii.enum(jsii_type="aws-cdk-lib.aws_appconfig.ActionPoint")
class ActionPoint(enum.Enum):
    '''Defines Extension action points.

    :see: https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions-about.html#working-with-appconfig-extensions-how-it-works-step-2
    :exampleMetadata: infused

    Example::

        # fn: lambda.Function
        
        
        appconfig.Extension(self, "MyExtension",
            actions=[
                appconfig.Action(
                    action_points=[appconfig.ActionPoint.ON_DEPLOYMENT_START],
                    event_destination=appconfig.LambdaDestination(fn)
                )
            ]
        )
    '''

    PRE_CREATE_HOSTED_CONFIGURATION_VERSION = "PRE_CREATE_HOSTED_CONFIGURATION_VERSION"
    PRE_START_DEPLOYMENT = "PRE_START_DEPLOYMENT"
    ON_DEPLOYMENT_START = "ON_DEPLOYMENT_START"
    ON_DEPLOYMENT_STEP = "ON_DEPLOYMENT_STEP"
    ON_DEPLOYMENT_BAKING = "ON_DEPLOYMENT_BAKING"
    ON_DEPLOYMENT_COMPLETE = "ON_DEPLOYMENT_COMPLETE"
    ON_DEPLOYMENT_ROLLED_BACK = "ON_DEPLOYMENT_ROLLED_BACK"


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appconfig.ActionProps",
    jsii_struct_bases=[],
    name_mapping={
        "action_points": "actionPoints",
        "event_destination": "eventDestination",
        "description": "description",
        "execution_role": "executionRole",
        "invoke_without_execution_role": "invokeWithoutExecutionRole",
        "name": "name",
    },
)
class ActionProps:
    def __init__(
        self,
        *,
        action_points: typing.Sequence[ActionPoint],
        event_destination: "IEventDestination",
        description: typing.Optional[builtins.str] = None,
        execution_role: typing.Optional[_IRole_235f5d8e] = None,
        invoke_without_execution_role: typing.Optional[builtins.bool] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for the Action construct.

        :param action_points: The action points that will trigger the extension action.
        :param event_destination: The event destination for the action.
        :param description: The description for the action. Default: - No description.
        :param execution_role: The execution role for the action. Default: - A role is generated.
        :param invoke_without_execution_role: The flag that specifies whether or not to create the execution role. If set to true, then the role will not be auto-generated under the assumption there is already the corresponding resource-based policy attached to the event destination. If false, the execution role will be generated if not provided. Default: false
        :param name: The name for the action. Default: - A name is generated.

        :exampleMetadata: infused

        Example::

            # fn: lambda.Function
            
            
            appconfig.Extension(self, "MyExtension",
                actions=[
                    appconfig.Action(
                        action_points=[appconfig.ActionPoint.ON_DEPLOYMENT_START],
                        event_destination=appconfig.LambdaDestination(fn)
                    )
                ]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d69874f3a61f1cf288efe1495c078fb07b686754d78d66ba26a1bf2e49af8cfb)
            check_type(argname="argument action_points", value=action_points, expected_type=type_hints["action_points"])
            check_type(argname="argument event_destination", value=event_destination, expected_type=type_hints["event_destination"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument execution_role", value=execution_role, expected_type=type_hints["execution_role"])
            check_type(argname="argument invoke_without_execution_role", value=invoke_without_execution_role, expected_type=type_hints["invoke_without_execution_role"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "action_points": action_points,
            "event_destination": event_destination,
        }
        if description is not None:
            self._values["description"] = description
        if execution_role is not None:
            self._values["execution_role"] = execution_role
        if invoke_without_execution_role is not None:
            self._values["invoke_without_execution_role"] = invoke_without_execution_role
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def action_points(self) -> typing.List[ActionPoint]:
        '''The action points that will trigger the extension action.'''
        result = self._values.get("action_points")
        assert result is not None, "Required property 'action_points' is missing"
        return typing.cast(typing.List[ActionPoint], result)

    @builtins.property
    def event_destination(self) -> "IEventDestination":
        '''The event destination for the action.'''
        result = self._values.get("event_destination")
        assert result is not None, "Required property 'event_destination' is missing"
        return typing.cast("IEventDestination", result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description for the action.

        :default: - No description.
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def execution_role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''The execution role for the action.

        :default: - A role is generated.
        '''
        result = self._values.get("execution_role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    @builtins.property
    def invoke_without_execution_role(self) -> typing.Optional[builtins.bool]:
        '''The flag that specifies whether or not to create the execution role.

        If set to true, then the role will not be auto-generated under the assumption
        there is already the corresponding resource-based policy attached to the event
        destination. If false, the execution role will be generated if not provided.

        :default: false
        '''
        result = self._values.get("invoke_without_execution_role")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name for the action.

        :default: - A name is generated.
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ActionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appconfig.ApplicationProps",
    jsii_struct_bases=[],
    name_mapping={"application_name": "applicationName", "description": "description"},
)
class ApplicationProps:
    def __init__(
        self,
        *,
        application_name: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for the Application construct.

        :param application_name: The name of the application. Default: - A name is generated.
        :param description: The description for the application. Default: - No description.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appconfig as appconfig
            
            application_props = appconfig.ApplicationProps(
                application_name="applicationName",
                description="description"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c495cbb9f880c8e82aa0fdbd8db994460c32e416c849e56db45c634dcf325d8)
            check_type(argname="argument application_name", value=application_name, expected_type=type_hints["application_name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if application_name is not None:
            self._values["application_name"] = application_name
        if description is not None:
            self._values["description"] = description

    @builtins.property
    def application_name(self) -> typing.Optional[builtins.str]:
        '''The name of the application.

        :default: - A name is generated.
        '''
        result = self._values.get("application_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description for the application.

        :default: - No description.
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnApplication(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appconfig.CfnApplication",
):
    '''The ``AWS::AppConfig::Application`` resource creates an application.

    In AWS AppConfig , an application is simply an organizational construct like a folder. This organizational construct has a relationship with some unit of executable code. For example, you could create an application called MyMobileApp to organize and manage configuration data for a mobile application installed by your users.

    AWS AppConfig requires that you create resources and deploy a configuration in the following order:

    - Create an application
    - Create an environment
    - Create a configuration profile
    - Choose a pre-defined deployment strategy or create your own
    - Deploy the configuration

    For more information, see `AWS AppConfig <https://docs.aws.amazon.com/appconfig/latest/userguide/what-is-appconfig.html>`_ in the *AWS AppConfig User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-application.html
    :cloudformationResource: AWS::AppConfig::Application
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_appconfig as appconfig
        
        cfn_application = appconfig.CfnApplication(self, "MyCfnApplication",
            name="name",
        
            # the properties below are optional
            description="description",
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
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: A name for the application.
        :param description: A description of the application.
        :param tags: Metadata to assign to the application. Tags help organize and categorize your AWS AppConfig resources. Each tag consists of a key and an optional value, both of which you define.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5cb8c402a0d1a836162f596142de6ed2a1f2a0635a355ae334b92eb1175e956)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnApplicationProps(name=name, description=description, tags=tags)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ea7b1a84049868bc175511a7cff8896cbe830377b519f6e81ca6912165c12a6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f6ba5479a5d56f629f8d2769fdc6bc86ac3ecfb94f4a9b20a0a26e228f899e8a)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrApplicationId")
    def attr_application_id(self) -> builtins.str:
        '''The application ID.

        :cloudformationAttribute: ApplicationId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrApplicationId"))

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
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''A name for the application.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd439efd20029913dc2dc3442824daa5698101df926aeab59ca95e5e5b8bbd51)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the application.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a824db2a54c11ce0a54133772196bc9c7049c60fe6169de15459866f72df2438)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Metadata to assign to the application.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1c6b2136fb3c6e3eba293e5878e147b18261e888036e9d04f50ade7f12363e3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appconfig.CfnApplicationProps",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "description": "description", "tags": "tags"},
)
class CfnApplicationProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnApplication``.

        :param name: A name for the application.
        :param description: A description of the application.
        :param tags: Metadata to assign to the application. Tags help organize and categorize your AWS AppConfig resources. Each tag consists of a key and an optional value, both of which you define.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-application.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appconfig as appconfig
            
            cfn_application_props = appconfig.CfnApplicationProps(
                name="name",
            
                # the properties below are optional
                description="description",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32e1eda1678f32e80ec88e7c377d932bfe40dcff82d39b0dd0edf98a68d3e9d9)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''A name for the application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-application.html#cfn-appconfig-application-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-application.html#cfn-appconfig-application-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Metadata to assign to the application.

        Tags help organize and categorize your AWS AppConfig resources. Each tag consists of a key and an optional value, both of which you define.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-application.html#cfn-appconfig-application-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApplicationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnConfigurationProfile(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appconfig.CfnConfigurationProfile",
):
    '''The ``AWS::AppConfig::ConfigurationProfile`` resource creates a configuration profile that enables AWS AppConfig to access the configuration source.

    Valid configuration sources include AWS Systems Manager (SSM) documents, SSM Parameter Store parameters, and Amazon S3 . A configuration profile includes the following information.

    - The Uri location of the configuration data.
    - The AWS Identity and Access Management ( IAM ) role that provides access to the configuration data.
    - A validator for the configuration data. Available validators include either a JSON Schema or the Amazon Resource Name (ARN) of an AWS Lambda function.

    AWS AppConfig requires that you create resources and deploy a configuration in the following order:

    - Create an application
    - Create an environment
    - Create a configuration profile
    - Choose a pre-defined deployment strategy or create your own
    - Deploy the configuration

    For more information, see `AWS AppConfig <https://docs.aws.amazon.com/appconfig/latest/userguide/what-is-appconfig.html>`_ in the *AWS AppConfig User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-configurationprofile.html
    :cloudformationResource: AWS::AppConfig::ConfigurationProfile
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_appconfig as appconfig
        
        cfn_configuration_profile = appconfig.CfnConfigurationProfile(self, "MyCfnConfigurationProfile",
            application_id="applicationId",
            location_uri="locationUri",
            name="name",
        
            # the properties below are optional
            description="description",
            kms_key_identifier="kmsKeyIdentifier",
            retrieval_role_arn="retrievalRoleArn",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            type="type",
            validators=[appconfig.CfnConfigurationProfile.ValidatorsProperty(
                content="content",
                type="type"
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        application_id: builtins.str,
        location_uri: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        kms_key_identifier: typing.Optional[builtins.str] = None,
        retrieval_role_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        type: typing.Optional[builtins.str] = None,
        validators: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfigurationProfile.ValidatorsProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param application_id: The application ID.
        :param location_uri: A URI to locate the configuration. You can specify the following:. - For the AWS AppConfig hosted configuration store and for feature flags, specify ``hosted`` . - For an AWS Systems Manager Parameter Store parameter, specify either the parameter name in the format ``ssm-parameter://<parameter name>`` or the ARN. - For an AWS CodePipeline pipeline, specify the URI in the following format: ``codepipeline`` ://. - For an AWS Secrets Manager secret, specify the URI in the following format: ``secretsmanager`` ://. - For an Amazon S3 object, specify the URI in the following format: ``s3://<bucket>/<objectKey>`` . Here is an example: ``s3://my-bucket/my-app/us-east-1/my-config.json`` - For an SSM document, specify either the document name in the format ``ssm-document://<document name>`` or the Amazon Resource Name (ARN).
        :param name: A name for the configuration profile.
        :param description: A description of the configuration profile.
        :param kms_key_identifier: The AWS Key Management Service key identifier (key ID, key alias, or key ARN) provided when the resource was created or updated.
        :param retrieval_role_arn: The ARN of an IAM role with permission to access the configuration at the specified ``LocationUri`` . .. epigraph:: A retrieval role ARN is not required for configurations stored in the AWS AppConfig hosted configuration store. It is required for all other sources that store your configuration.
        :param tags: Metadata to assign to the configuration profile. Tags help organize and categorize your AWS AppConfig resources. Each tag consists of a key and an optional value, both of which you define.
        :param type: The type of configurations contained in the profile. AWS AppConfig supports ``feature flags`` and ``freeform`` configurations. We recommend you create feature flag configurations to enable or disable new features and freeform configurations to distribute configurations to an application. When calling this API, enter one of the following values for ``Type`` : ``AWS.AppConfig.FeatureFlags`` ``AWS.Freeform``
        :param validators: A list of methods for validating the configuration.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__332c05b5fb120e53a9fcdde311f2bc23aaec927aa0e70b013e72cc2cebe88708)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnConfigurationProfileProps(
            application_id=application_id,
            location_uri=location_uri,
            name=name,
            description=description,
            kms_key_identifier=kms_key_identifier,
            retrieval_role_arn=retrieval_role_arn,
            tags=tags,
            type=type,
            validators=validators,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e772e24251baa448c01bcc3e6670ade5ceed90c38ae4803dc614bd5e09316acd)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e32e704ce25e06be45d32d6a2f4cb3655c378ec2a6662baf1f650e54d58d3148)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrConfigurationProfileId")
    def attr_configuration_profile_id(self) -> builtins.str:
        '''The configuration profile ID.

        :cloudformationAttribute: ConfigurationProfileId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrConfigurationProfileId"))

    @builtins.property
    @jsii.member(jsii_name="attrKmsKeyArn")
    def attr_kms_key_arn(self) -> builtins.str:
        '''The Amazon Resource Name of the AWS Key Management Service key to encrypt new configuration data versions in the AWS AppConfig hosted configuration store.

        This attribute is only used for ``hosted`` configuration types. To encrypt data managed in other configuration stores, see the documentation for how to specify an AWS KMS key for that particular service.

        :cloudformationAttribute: KmsKeyArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrKmsKeyArn"))

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
    @jsii.member(jsii_name="applicationId")
    def application_id(self) -> builtins.str:
        '''The application ID.'''
        return typing.cast(builtins.str, jsii.get(self, "applicationId"))

    @application_id.setter
    def application_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a90d416aa5727f39ec3c71cf2276506643a5cf358d97a872994efb5efc0c6a23)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationId", value)

    @builtins.property
    @jsii.member(jsii_name="locationUri")
    def location_uri(self) -> builtins.str:
        '''A URI to locate the configuration.

        You can specify the following:.
        '''
        return typing.cast(builtins.str, jsii.get(self, "locationUri"))

    @location_uri.setter
    def location_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b354f0f45617e66d27b62ebf9a76fdbe168c6f5b6731023e6a366547233a4cb5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "locationUri", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''A name for the configuration profile.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92d26c2b0d5b0b13ed55ca82e2b92075cdb99d8bd6d4a9122e33104a12cf9d5d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the configuration profile.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5884bd7f8fdc28919378604807977665ba3e82a47697c023e5982eb7257f557c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyIdentifier")
    def kms_key_identifier(self) -> typing.Optional[builtins.str]:
        '''The AWS Key Management Service key identifier (key ID, key alias, or key ARN) provided when the resource was created or updated.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyIdentifier"))

    @kms_key_identifier.setter
    def kms_key_identifier(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3eeb407208b90160e95c0fa6df04c352da355146a3ccf76bdbd6393ad76427e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="retrievalRoleArn")
    def retrieval_role_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of an IAM role with permission to access the configuration at the specified ``LocationUri`` .'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "retrievalRoleArn"))

    @retrieval_role_arn.setter
    def retrieval_role_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d3f2e474a52e1c1e45abe4e24cd6c758600c20023f3697e0c69533c0e771bc2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retrievalRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Metadata to assign to the configuration profile.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ebd94616157773a4ab3988775ff92592f3cda9938c8625e395d1dbbf8406354b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> typing.Optional[builtins.str]:
        '''The type of configurations contained in the profile.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "type"))

    @type.setter
    def type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c45113a4405009713d71c8289b038f5cff241d53b81b243f0372147d29440ad9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="validators")
    def validators(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnConfigurationProfile.ValidatorsProperty"]]]]:
        '''A list of methods for validating the configuration.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnConfigurationProfile.ValidatorsProperty"]]]], jsii.get(self, "validators"))

    @validators.setter
    def validators(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnConfigurationProfile.ValidatorsProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11ba2acd464e5613cd96989e3516592dcd5684d8452b3028698e0549f5d5fafb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "validators", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appconfig.CfnConfigurationProfile.ValidatorsProperty",
        jsii_struct_bases=[],
        name_mapping={"content": "content", "type": "type"},
    )
    class ValidatorsProperty:
        def __init__(
            self,
            *,
            content: typing.Optional[builtins.str] = None,
            type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A validator provides a syntactic or semantic check to ensure the configuration that you want to deploy functions as intended.

            To validate your application configuration data, you provide a schema or an AWS Lambda function that runs against the configuration. The configuration deployment or update can only proceed when the configuration data is valid. For more information, see `About validators <https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-configuration-profile.html#appconfig-creating-configuration-and-profile-validators>`_ in the *AWS AppConfig User Guide* .

            :param content: Either the JSON Schema content or the Amazon Resource Name (ARN) of an Lambda function.
            :param type: AWS AppConfig supports validators of type ``JSON_SCHEMA`` and ``LAMBDA``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-configurationprofile-validators.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appconfig as appconfig
                
                validators_property = appconfig.CfnConfigurationProfile.ValidatorsProperty(
                    content="content",
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e3e2223bb16cf91626b0a44db9aa8ec9190717961f143668d3ff6961eec9abdd)
                check_type(argname="argument content", value=content, expected_type=type_hints["content"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if content is not None:
                self._values["content"] = content
            if type is not None:
                self._values["type"] = type

        @builtins.property
        def content(self) -> typing.Optional[builtins.str]:
            '''Either the JSON Schema content or the Amazon Resource Name (ARN) of an Lambda function.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-configurationprofile-validators.html#cfn-appconfig-configurationprofile-validators-content
            '''
            result = self._values.get("content")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''AWS AppConfig supports validators of type ``JSON_SCHEMA`` and ``LAMBDA``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-configurationprofile-validators.html#cfn-appconfig-configurationprofile-validators-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ValidatorsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appconfig.CfnConfigurationProfileProps",
    jsii_struct_bases=[],
    name_mapping={
        "application_id": "applicationId",
        "location_uri": "locationUri",
        "name": "name",
        "description": "description",
        "kms_key_identifier": "kmsKeyIdentifier",
        "retrieval_role_arn": "retrievalRoleArn",
        "tags": "tags",
        "type": "type",
        "validators": "validators",
    },
)
class CfnConfigurationProfileProps:
    def __init__(
        self,
        *,
        application_id: builtins.str,
        location_uri: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        kms_key_identifier: typing.Optional[builtins.str] = None,
        retrieval_role_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        type: typing.Optional[builtins.str] = None,
        validators: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationProfile.ValidatorsProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnConfigurationProfile``.

        :param application_id: The application ID.
        :param location_uri: A URI to locate the configuration. You can specify the following:. - For the AWS AppConfig hosted configuration store and for feature flags, specify ``hosted`` . - For an AWS Systems Manager Parameter Store parameter, specify either the parameter name in the format ``ssm-parameter://<parameter name>`` or the ARN. - For an AWS CodePipeline pipeline, specify the URI in the following format: ``codepipeline`` ://. - For an AWS Secrets Manager secret, specify the URI in the following format: ``secretsmanager`` ://. - For an Amazon S3 object, specify the URI in the following format: ``s3://<bucket>/<objectKey>`` . Here is an example: ``s3://my-bucket/my-app/us-east-1/my-config.json`` - For an SSM document, specify either the document name in the format ``ssm-document://<document name>`` or the Amazon Resource Name (ARN).
        :param name: A name for the configuration profile.
        :param description: A description of the configuration profile.
        :param kms_key_identifier: The AWS Key Management Service key identifier (key ID, key alias, or key ARN) provided when the resource was created or updated.
        :param retrieval_role_arn: The ARN of an IAM role with permission to access the configuration at the specified ``LocationUri`` . .. epigraph:: A retrieval role ARN is not required for configurations stored in the AWS AppConfig hosted configuration store. It is required for all other sources that store your configuration.
        :param tags: Metadata to assign to the configuration profile. Tags help organize and categorize your AWS AppConfig resources. Each tag consists of a key and an optional value, both of which you define.
        :param type: The type of configurations contained in the profile. AWS AppConfig supports ``feature flags`` and ``freeform`` configurations. We recommend you create feature flag configurations to enable or disable new features and freeform configurations to distribute configurations to an application. When calling this API, enter one of the following values for ``Type`` : ``AWS.AppConfig.FeatureFlags`` ``AWS.Freeform``
        :param validators: A list of methods for validating the configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-configurationprofile.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appconfig as appconfig
            
            cfn_configuration_profile_props = appconfig.CfnConfigurationProfileProps(
                application_id="applicationId",
                location_uri="locationUri",
                name="name",
            
                # the properties below are optional
                description="description",
                kms_key_identifier="kmsKeyIdentifier",
                retrieval_role_arn="retrievalRoleArn",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                type="type",
                validators=[appconfig.CfnConfigurationProfile.ValidatorsProperty(
                    content="content",
                    type="type"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37522e89a156f185f3387aea77d01f8010adde3d2bcfeb76862a70fd9b7e08bc)
            check_type(argname="argument application_id", value=application_id, expected_type=type_hints["application_id"])
            check_type(argname="argument location_uri", value=location_uri, expected_type=type_hints["location_uri"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument kms_key_identifier", value=kms_key_identifier, expected_type=type_hints["kms_key_identifier"])
            check_type(argname="argument retrieval_role_arn", value=retrieval_role_arn, expected_type=type_hints["retrieval_role_arn"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument validators", value=validators, expected_type=type_hints["validators"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_id": application_id,
            "location_uri": location_uri,
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if kms_key_identifier is not None:
            self._values["kms_key_identifier"] = kms_key_identifier
        if retrieval_role_arn is not None:
            self._values["retrieval_role_arn"] = retrieval_role_arn
        if tags is not None:
            self._values["tags"] = tags
        if type is not None:
            self._values["type"] = type
        if validators is not None:
            self._values["validators"] = validators

    @builtins.property
    def application_id(self) -> builtins.str:
        '''The application ID.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-configurationprofile.html#cfn-appconfig-configurationprofile-applicationid
        '''
        result = self._values.get("application_id")
        assert result is not None, "Required property 'application_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def location_uri(self) -> builtins.str:
        '''A URI to locate the configuration. You can specify the following:.

        - For the AWS AppConfig hosted configuration store and for feature flags, specify ``hosted`` .
        - For an AWS Systems Manager Parameter Store parameter, specify either the parameter name in the format ``ssm-parameter://<parameter name>`` or the ARN.
        - For an AWS CodePipeline pipeline, specify the URI in the following format: ``codepipeline`` ://.
        - For an AWS Secrets Manager secret, specify the URI in the following format: ``secretsmanager`` ://.
        - For an Amazon S3 object, specify the URI in the following format: ``s3://<bucket>/<objectKey>`` . Here is an example: ``s3://my-bucket/my-app/us-east-1/my-config.json``
        - For an SSM document, specify either the document name in the format ``ssm-document://<document name>`` or the Amazon Resource Name (ARN).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-configurationprofile.html#cfn-appconfig-configurationprofile-locationuri
        '''
        result = self._values.get("location_uri")
        assert result is not None, "Required property 'location_uri' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''A name for the configuration profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-configurationprofile.html#cfn-appconfig-configurationprofile-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the configuration profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-configurationprofile.html#cfn-appconfig-configurationprofile-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_identifier(self) -> typing.Optional[builtins.str]:
        '''The AWS Key Management Service key identifier (key ID, key alias, or key ARN) provided when the resource was created or updated.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-configurationprofile.html#cfn-appconfig-configurationprofile-kmskeyidentifier
        '''
        result = self._values.get("kms_key_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def retrieval_role_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of an IAM role with permission to access the configuration at the specified ``LocationUri`` .

        .. epigraph::

           A retrieval role ARN is not required for configurations stored in the AWS AppConfig hosted configuration store. It is required for all other sources that store your configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-configurationprofile.html#cfn-appconfig-configurationprofile-retrievalrolearn
        '''
        result = self._values.get("retrieval_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Metadata to assign to the configuration profile.

        Tags help organize and categorize your AWS AppConfig resources. Each tag consists of a key and an optional value, both of which you define.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-configurationprofile.html#cfn-appconfig-configurationprofile-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''The type of configurations contained in the profile.

        AWS AppConfig supports ``feature flags`` and ``freeform`` configurations. We recommend you create feature flag configurations to enable or disable new features and freeform configurations to distribute configurations to an application. When calling this API, enter one of the following values for ``Type`` :

        ``AWS.AppConfig.FeatureFlags``

        ``AWS.Freeform``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-configurationprofile.html#cfn-appconfig-configurationprofile-type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def validators(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnConfigurationProfile.ValidatorsProperty]]]]:
        '''A list of methods for validating the configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-configurationprofile.html#cfn-appconfig-configurationprofile-validators
        '''
        result = self._values.get("validators")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnConfigurationProfile.ValidatorsProperty]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnConfigurationProfileProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnDeployment(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appconfig.CfnDeployment",
):
    '''The ``AWS::AppConfig::Deployment`` resource starts a deployment.

    Starting a deployment in AWS AppConfig calls the ``StartDeployment`` API action. This call includes the IDs of the AWS AppConfig application, the environment, the configuration profile, and (optionally) the configuration data version to deploy. The call also includes the ID of the deployment strategy to use, which determines how the configuration data is deployed.

    AWS AppConfig monitors the distribution to all hosts and reports status. If a distribution fails, then AWS AppConfig rolls back the configuration.

    AWS AppConfig requires that you create resources and deploy a configuration in the following order:

    - Create an application
    - Create an environment
    - Create a configuration profile
    - Choose a pre-defined deployment strategy or create your own
    - Deploy the configuration

    For more information, see `AWS AppConfig <https://docs.aws.amazon.com/appconfig/latest/userguide/what-is-appconfig.html>`_ in the *AWS AppConfig User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deployment.html
    :cloudformationResource: AWS::AppConfig::Deployment
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_appconfig as appconfig
        
        cfn_deployment = appconfig.CfnDeployment(self, "MyCfnDeployment",
            application_id="applicationId",
            configuration_profile_id="configurationProfileId",
            configuration_version="configurationVersion",
            deployment_strategy_id="deploymentStrategyId",
            environment_id="environmentId",
        
            # the properties below are optional
            description="description",
            dynamic_extension_parameters=[appconfig.CfnDeployment.DynamicExtensionParametersProperty(
                extension_reference="extensionReference",
                parameter_name="parameterName",
                parameter_value="parameterValue"
            )],
            kms_key_identifier="kmsKeyIdentifier",
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
        application_id: builtins.str,
        configuration_profile_id: builtins.str,
        configuration_version: builtins.str,
        deployment_strategy_id: builtins.str,
        environment_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        dynamic_extension_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeployment.DynamicExtensionParametersProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        kms_key_identifier: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param application_id: The application ID.
        :param configuration_profile_id: The configuration profile ID.
        :param configuration_version: The configuration version to deploy. If deploying an AWS AppConfig hosted configuration version, you can specify either the version number or version label. For all other configurations, you must specify the version number.
        :param deployment_strategy_id: The deployment strategy ID.
        :param environment_id: The environment ID.
        :param description: A description of the deployment.
        :param dynamic_extension_parameters: A map of dynamic extension parameter names to values to pass to associated extensions with ``PRE_START_DEPLOYMENT`` actions.
        :param kms_key_identifier: The AWS Key Management Service key identifier (key ID, key alias, or key ARN) provided when the resource was created or updated.
        :param tags: Metadata to assign to the deployment. Tags help organize and categorize your AWS AppConfig resources. Each tag consists of a key and an optional value, both of which you define.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1b3c15ba63fb6169371007d7bae981d061f49c21042389030326b9ae1271344)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDeploymentProps(
            application_id=application_id,
            configuration_profile_id=configuration_profile_id,
            configuration_version=configuration_version,
            deployment_strategy_id=deployment_strategy_id,
            environment_id=environment_id,
            description=description,
            dynamic_extension_parameters=dynamic_extension_parameters,
            kms_key_identifier=kms_key_identifier,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aaa2637a497fc43f28ee8b6e77e0f1878471c7f5bc0a736d0303ca69cb2d082c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6d3096cada1facd4de77c79fe8d588aa3d9567d81b3f913d2c2e6cf8fac54d0e)
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
    @jsii.member(jsii_name="cdkTagManager")
    def cdk_tag_manager(self) -> _TagManager_0a598cb3:
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "cdkTagManager"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="applicationId")
    def application_id(self) -> builtins.str:
        '''The application ID.'''
        return typing.cast(builtins.str, jsii.get(self, "applicationId"))

    @application_id.setter
    def application_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95aaa1f67bb9531251e5f9c62292c84df7727307a58c223aaa637f0a36a3d65d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationId", value)

    @builtins.property
    @jsii.member(jsii_name="configurationProfileId")
    def configuration_profile_id(self) -> builtins.str:
        '''The configuration profile ID.'''
        return typing.cast(builtins.str, jsii.get(self, "configurationProfileId"))

    @configuration_profile_id.setter
    def configuration_profile_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca3182ab453e0412fad7ba8649da4e0cfebf187bd90f38a026444982eb8bf50e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configurationProfileId", value)

    @builtins.property
    @jsii.member(jsii_name="configurationVersion")
    def configuration_version(self) -> builtins.str:
        '''The configuration version to deploy.'''
        return typing.cast(builtins.str, jsii.get(self, "configurationVersion"))

    @configuration_version.setter
    def configuration_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5abde1954bdb5d84cfce775808f90c961127e86db5ff5164bb90a98e3b0f9f20)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configurationVersion", value)

    @builtins.property
    @jsii.member(jsii_name="deploymentStrategyId")
    def deployment_strategy_id(self) -> builtins.str:
        '''The deployment strategy ID.'''
        return typing.cast(builtins.str, jsii.get(self, "deploymentStrategyId"))

    @deployment_strategy_id.setter
    def deployment_strategy_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0527964ec5c65ed1bca366f0674e5cda5d23fe019ae479f3ee3fb550fbdb0c23)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deploymentStrategyId", value)

    @builtins.property
    @jsii.member(jsii_name="environmentId")
    def environment_id(self) -> builtins.str:
        '''The environment ID.'''
        return typing.cast(builtins.str, jsii.get(self, "environmentId"))

    @environment_id.setter
    def environment_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f949624a9b6e222d754ab636966342dbb9eb207d34230837c882091a20f9abac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environmentId", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the deployment.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96f77dd19f2c1b41d04318bc8aa9cc8f75808190471ba4922eb58652c55c5e38)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="dynamicExtensionParameters")
    def dynamic_extension_parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDeployment.DynamicExtensionParametersProperty"]]]]:
        '''A map of dynamic extension parameter names to values to pass to associated extensions with ``PRE_START_DEPLOYMENT`` actions.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDeployment.DynamicExtensionParametersProperty"]]]], jsii.get(self, "dynamicExtensionParameters"))

    @dynamic_extension_parameters.setter
    def dynamic_extension_parameters(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDeployment.DynamicExtensionParametersProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5a4416b6ac2f6fbc5dd497fd6aafe41844d2e927bc75ce571b37c2f1b805bfb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dynamicExtensionParameters", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyIdentifier")
    def kms_key_identifier(self) -> typing.Optional[builtins.str]:
        '''The AWS Key Management Service key identifier (key ID, key alias, or key ARN) provided when the resource was created or updated.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyIdentifier"))

    @kms_key_identifier.setter
    def kms_key_identifier(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98b30f15af8144546829026dccf1aaf4fedd94b59dabeb6c8e8d7bc2b71e2efb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Metadata to assign to the deployment.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12211b05040a4e1a62df97a0128f266db1c0380eba8db0726824e99ad7241551)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appconfig.CfnDeployment.DynamicExtensionParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "extension_reference": "extensionReference",
            "parameter_name": "parameterName",
            "parameter_value": "parameterValue",
        },
    )
    class DynamicExtensionParametersProperty:
        def __init__(
            self,
            *,
            extension_reference: typing.Optional[builtins.str] = None,
            parameter_name: typing.Optional[builtins.str] = None,
            parameter_value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A map of dynamic extension parameter names to values to pass to associated extensions with ``PRE_START_DEPLOYMENT`` actions.

            :param extension_reference: The ARN or ID of the extension for which you are inserting a dynamic parameter.
            :param parameter_name: The parameter name.
            :param parameter_value: The parameter value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-deployment-dynamicextensionparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appconfig as appconfig
                
                dynamic_extension_parameters_property = appconfig.CfnDeployment.DynamicExtensionParametersProperty(
                    extension_reference="extensionReference",
                    parameter_name="parameterName",
                    parameter_value="parameterValue"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__db7299354c46559a877995ee8ab04c4fd72aaaf53cc390877fbf50f65ac43390)
                check_type(argname="argument extension_reference", value=extension_reference, expected_type=type_hints["extension_reference"])
                check_type(argname="argument parameter_name", value=parameter_name, expected_type=type_hints["parameter_name"])
                check_type(argname="argument parameter_value", value=parameter_value, expected_type=type_hints["parameter_value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if extension_reference is not None:
                self._values["extension_reference"] = extension_reference
            if parameter_name is not None:
                self._values["parameter_name"] = parameter_name
            if parameter_value is not None:
                self._values["parameter_value"] = parameter_value

        @builtins.property
        def extension_reference(self) -> typing.Optional[builtins.str]:
            '''The ARN or ID of the extension for which you are inserting a dynamic parameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-deployment-dynamicextensionparameters.html#cfn-appconfig-deployment-dynamicextensionparameters-extensionreference
            '''
            result = self._values.get("extension_reference")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def parameter_name(self) -> typing.Optional[builtins.str]:
            '''The parameter name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-deployment-dynamicextensionparameters.html#cfn-appconfig-deployment-dynamicextensionparameters-parametername
            '''
            result = self._values.get("parameter_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def parameter_value(self) -> typing.Optional[builtins.str]:
            '''The parameter value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-deployment-dynamicextensionparameters.html#cfn-appconfig-deployment-dynamicextensionparameters-parametervalue
            '''
            result = self._values.get("parameter_value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DynamicExtensionParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appconfig.CfnDeploymentProps",
    jsii_struct_bases=[],
    name_mapping={
        "application_id": "applicationId",
        "configuration_profile_id": "configurationProfileId",
        "configuration_version": "configurationVersion",
        "deployment_strategy_id": "deploymentStrategyId",
        "environment_id": "environmentId",
        "description": "description",
        "dynamic_extension_parameters": "dynamicExtensionParameters",
        "kms_key_identifier": "kmsKeyIdentifier",
        "tags": "tags",
    },
)
class CfnDeploymentProps:
    def __init__(
        self,
        *,
        application_id: builtins.str,
        configuration_profile_id: builtins.str,
        configuration_version: builtins.str,
        deployment_strategy_id: builtins.str,
        environment_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        dynamic_extension_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeployment.DynamicExtensionParametersProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        kms_key_identifier: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDeployment``.

        :param application_id: The application ID.
        :param configuration_profile_id: The configuration profile ID.
        :param configuration_version: The configuration version to deploy. If deploying an AWS AppConfig hosted configuration version, you can specify either the version number or version label. For all other configurations, you must specify the version number.
        :param deployment_strategy_id: The deployment strategy ID.
        :param environment_id: The environment ID.
        :param description: A description of the deployment.
        :param dynamic_extension_parameters: A map of dynamic extension parameter names to values to pass to associated extensions with ``PRE_START_DEPLOYMENT`` actions.
        :param kms_key_identifier: The AWS Key Management Service key identifier (key ID, key alias, or key ARN) provided when the resource was created or updated.
        :param tags: Metadata to assign to the deployment. Tags help organize and categorize your AWS AppConfig resources. Each tag consists of a key and an optional value, both of which you define.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deployment.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appconfig as appconfig
            
            cfn_deployment_props = appconfig.CfnDeploymentProps(
                application_id="applicationId",
                configuration_profile_id="configurationProfileId",
                configuration_version="configurationVersion",
                deployment_strategy_id="deploymentStrategyId",
                environment_id="environmentId",
            
                # the properties below are optional
                description="description",
                dynamic_extension_parameters=[appconfig.CfnDeployment.DynamicExtensionParametersProperty(
                    extension_reference="extensionReference",
                    parameter_name="parameterName",
                    parameter_value="parameterValue"
                )],
                kms_key_identifier="kmsKeyIdentifier",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8289d78d65be12b91a60529d6c53d8a4385f73c87b2a23cfef86efebc1e00914)
            check_type(argname="argument application_id", value=application_id, expected_type=type_hints["application_id"])
            check_type(argname="argument configuration_profile_id", value=configuration_profile_id, expected_type=type_hints["configuration_profile_id"])
            check_type(argname="argument configuration_version", value=configuration_version, expected_type=type_hints["configuration_version"])
            check_type(argname="argument deployment_strategy_id", value=deployment_strategy_id, expected_type=type_hints["deployment_strategy_id"])
            check_type(argname="argument environment_id", value=environment_id, expected_type=type_hints["environment_id"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument dynamic_extension_parameters", value=dynamic_extension_parameters, expected_type=type_hints["dynamic_extension_parameters"])
            check_type(argname="argument kms_key_identifier", value=kms_key_identifier, expected_type=type_hints["kms_key_identifier"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_id": application_id,
            "configuration_profile_id": configuration_profile_id,
            "configuration_version": configuration_version,
            "deployment_strategy_id": deployment_strategy_id,
            "environment_id": environment_id,
        }
        if description is not None:
            self._values["description"] = description
        if dynamic_extension_parameters is not None:
            self._values["dynamic_extension_parameters"] = dynamic_extension_parameters
        if kms_key_identifier is not None:
            self._values["kms_key_identifier"] = kms_key_identifier
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def application_id(self) -> builtins.str:
        '''The application ID.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deployment.html#cfn-appconfig-deployment-applicationid
        '''
        result = self._values.get("application_id")
        assert result is not None, "Required property 'application_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def configuration_profile_id(self) -> builtins.str:
        '''The configuration profile ID.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deployment.html#cfn-appconfig-deployment-configurationprofileid
        '''
        result = self._values.get("configuration_profile_id")
        assert result is not None, "Required property 'configuration_profile_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def configuration_version(self) -> builtins.str:
        '''The configuration version to deploy.

        If deploying an AWS AppConfig hosted configuration version, you can specify either the version number or version label. For all other configurations, you must specify the version number.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deployment.html#cfn-appconfig-deployment-configurationversion
        '''
        result = self._values.get("configuration_version")
        assert result is not None, "Required property 'configuration_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def deployment_strategy_id(self) -> builtins.str:
        '''The deployment strategy ID.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deployment.html#cfn-appconfig-deployment-deploymentstrategyid
        '''
        result = self._values.get("deployment_strategy_id")
        assert result is not None, "Required property 'deployment_strategy_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def environment_id(self) -> builtins.str:
        '''The environment ID.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deployment.html#cfn-appconfig-deployment-environmentid
        '''
        result = self._values.get("environment_id")
        assert result is not None, "Required property 'environment_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the deployment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deployment.html#cfn-appconfig-deployment-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dynamic_extension_parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDeployment.DynamicExtensionParametersProperty]]]]:
        '''A map of dynamic extension parameter names to values to pass to associated extensions with ``PRE_START_DEPLOYMENT`` actions.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deployment.html#cfn-appconfig-deployment-dynamicextensionparameters
        '''
        result = self._values.get("dynamic_extension_parameters")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDeployment.DynamicExtensionParametersProperty]]]], result)

    @builtins.property
    def kms_key_identifier(self) -> typing.Optional[builtins.str]:
        '''The AWS Key Management Service key identifier (key ID, key alias, or key ARN) provided when the resource was created or updated.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deployment.html#cfn-appconfig-deployment-kmskeyidentifier
        '''
        result = self._values.get("kms_key_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Metadata to assign to the deployment.

        Tags help organize and categorize your AWS AppConfig resources. Each tag consists of a key and an optional value, both of which you define.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deployment.html#cfn-appconfig-deployment-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDeploymentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnDeploymentStrategy(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appconfig.CfnDeploymentStrategy",
):
    '''The ``AWS::AppConfig::DeploymentStrategy`` resource creates an AWS AppConfig deployment strategy.

    A deployment strategy defines important criteria for rolling out your configuration to the designated targets. A deployment strategy includes: the overall duration required, a percentage of targets to receive the deployment during each interval, an algorithm that defines how percentage grows, and bake time.

    AWS AppConfig requires that you create resources and deploy a configuration in the following order:

    - Create an application
    - Create an environment
    - Create a configuration profile
    - Choose a pre-defined deployment strategy or create your own
    - Deploy the configuration

    For more information, see `AWS AppConfig <https://docs.aws.amazon.com/appconfig/latest/userguide/what-is-appconfig.html>`_ in the *AWS AppConfig User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deploymentstrategy.html
    :cloudformationResource: AWS::AppConfig::DeploymentStrategy
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_appconfig as appconfig
        
        cfn_deployment_strategy = appconfig.CfnDeploymentStrategy(self, "MyCfnDeploymentStrategy",
            deployment_duration_in_minutes=123,
            growth_factor=123,
            name="name",
            replicate_to="replicateTo",
        
            # the properties below are optional
            description="description",
            final_bake_time_in_minutes=123,
            growth_type="growthType",
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
        deployment_duration_in_minutes: jsii.Number,
        growth_factor: jsii.Number,
        name: builtins.str,
        replicate_to: builtins.str,
        description: typing.Optional[builtins.str] = None,
        final_bake_time_in_minutes: typing.Optional[jsii.Number] = None,
        growth_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param deployment_duration_in_minutes: Total amount of time for a deployment to last.
        :param growth_factor: The percentage of targets to receive a deployed configuration during each interval.
        :param name: A name for the deployment strategy.
        :param replicate_to: Save the deployment strategy to a Systems Manager (SSM) document.
        :param description: A description of the deployment strategy.
        :param final_bake_time_in_minutes: Specifies the amount of time AWS AppConfig monitors for Amazon CloudWatch alarms after the configuration has been deployed to 100% of its targets, before considering the deployment to be complete. If an alarm is triggered during this time, AWS AppConfig rolls back the deployment. You must configure permissions for AWS AppConfig to roll back based on CloudWatch alarms. For more information, see `Configuring permissions for rollback based on Amazon CloudWatch alarms <https://docs.aws.amazon.com/appconfig/latest/userguide/getting-started-with-appconfig-cloudwatch-alarms-permissions.html>`_ in the *AWS AppConfig User Guide* .
        :param growth_type: The algorithm used to define how percentage grows over time. AWS AppConfig supports the following growth types:. *Linear* : For this type, AWS AppConfig processes the deployment by dividing the total number of targets by the value specified for ``Step percentage`` . For example, a linear deployment that uses a ``Step percentage`` of 10 deploys the configuration to 10 percent of the hosts. After those deployments are complete, the system deploys the configuration to the next 10 percent. This continues until 100% of the targets have successfully received the configuration. *Exponential* : For this type, AWS AppConfig processes the deployment exponentially using the following formula: ``G*(2^N)`` . In this formula, ``G`` is the growth factor specified by the user and ``N`` is the number of steps until the configuration is deployed to all targets. For example, if you specify a growth factor of 2, then the system rolls out the configuration as follows: ``2*(2^0)`` ``2*(2^1)`` ``2*(2^2)`` Expressed numerically, the deployment rolls out as follows: 2% of the targets, 4% of the targets, 8% of the targets, and continues until the configuration has been deployed to all targets.
        :param tags: Assigns metadata to an AWS AppConfig resource. Tags help organize and categorize your AWS AppConfig resources. Each tag consists of a key and an optional value, both of which you define. You can specify a maximum of 50 tags for a resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb88c221f102c1b57ba4f19db7656eb36ff011a70e3643e39d048c313eda22fd)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDeploymentStrategyProps(
            deployment_duration_in_minutes=deployment_duration_in_minutes,
            growth_factor=growth_factor,
            name=name,
            replicate_to=replicate_to,
            description=description,
            final_bake_time_in_minutes=final_bake_time_in_minutes,
            growth_type=growth_type,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c07282bd387e2aab09e9241f96ded37ff336d3f231f996e048ef207d3a38bc3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__750f81fb9177952991767d28a4a55a4de59c55177b25056fdd45e8aff0c293c2)
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
        '''The deployment strategy ID.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

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
    @jsii.member(jsii_name="deploymentDurationInMinutes")
    def deployment_duration_in_minutes(self) -> jsii.Number:
        '''Total amount of time for a deployment to last.'''
        return typing.cast(jsii.Number, jsii.get(self, "deploymentDurationInMinutes"))

    @deployment_duration_in_minutes.setter
    def deployment_duration_in_minutes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2b9cfcca9dae7bf599adef5f2b44e7662994e8143e1b3ccfa6f12c4d8ad5a19)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deploymentDurationInMinutes", value)

    @builtins.property
    @jsii.member(jsii_name="growthFactor")
    def growth_factor(self) -> jsii.Number:
        '''The percentage of targets to receive a deployed configuration during each interval.'''
        return typing.cast(jsii.Number, jsii.get(self, "growthFactor"))

    @growth_factor.setter
    def growth_factor(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ac4cbcedcf27ec80d55a98d836dbb9ac52523d6ff7838145b4d527fadaf652d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "growthFactor", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''A name for the deployment strategy.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43a46b42e0607ca1c01aa58dff3034f44511b63f99f559fe0fd370080f52f2c7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="replicateTo")
    def replicate_to(self) -> builtins.str:
        '''Save the deployment strategy to a Systems Manager (SSM) document.'''
        return typing.cast(builtins.str, jsii.get(self, "replicateTo"))

    @replicate_to.setter
    def replicate_to(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb6ef1a3102939b024e6e99b451674a1ad1f6879f5355a20a6d365cfeab4ad4e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replicateTo", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the deployment strategy.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f47275a573fd911ba6db69f152dd00eab69b450d732941105375d198524fd2b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="finalBakeTimeInMinutes")
    def final_bake_time_in_minutes(self) -> typing.Optional[jsii.Number]:
        '''Specifies the amount of time AWS AppConfig monitors for Amazon CloudWatch alarms after the configuration has been deployed to 100% of its targets, before considering the deployment to be complete.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "finalBakeTimeInMinutes"))

    @final_bake_time_in_minutes.setter
    def final_bake_time_in_minutes(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad18c900d6d84d1f1dba268d6d666b830e5e5276badda4b775deb06725f3c4ea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "finalBakeTimeInMinutes", value)

    @builtins.property
    @jsii.member(jsii_name="growthType")
    def growth_type(self) -> typing.Optional[builtins.str]:
        '''The algorithm used to define how percentage grows over time.

        AWS AppConfig supports the following growth types:.
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "growthType"))

    @growth_type.setter
    def growth_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38dbe338fc520a7ce3134f048d86265b2db4966fa73c38281b48ff6124acbc16)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "growthType", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Assigns metadata to an AWS AppConfig resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b0c7e44af284b89d6923411489d05fa28350784f8d88a837a0d019a1d575e65)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appconfig.CfnDeploymentStrategyProps",
    jsii_struct_bases=[],
    name_mapping={
        "deployment_duration_in_minutes": "deploymentDurationInMinutes",
        "growth_factor": "growthFactor",
        "name": "name",
        "replicate_to": "replicateTo",
        "description": "description",
        "final_bake_time_in_minutes": "finalBakeTimeInMinutes",
        "growth_type": "growthType",
        "tags": "tags",
    },
)
class CfnDeploymentStrategyProps:
    def __init__(
        self,
        *,
        deployment_duration_in_minutes: jsii.Number,
        growth_factor: jsii.Number,
        name: builtins.str,
        replicate_to: builtins.str,
        description: typing.Optional[builtins.str] = None,
        final_bake_time_in_minutes: typing.Optional[jsii.Number] = None,
        growth_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDeploymentStrategy``.

        :param deployment_duration_in_minutes: Total amount of time for a deployment to last.
        :param growth_factor: The percentage of targets to receive a deployed configuration during each interval.
        :param name: A name for the deployment strategy.
        :param replicate_to: Save the deployment strategy to a Systems Manager (SSM) document.
        :param description: A description of the deployment strategy.
        :param final_bake_time_in_minutes: Specifies the amount of time AWS AppConfig monitors for Amazon CloudWatch alarms after the configuration has been deployed to 100% of its targets, before considering the deployment to be complete. If an alarm is triggered during this time, AWS AppConfig rolls back the deployment. You must configure permissions for AWS AppConfig to roll back based on CloudWatch alarms. For more information, see `Configuring permissions for rollback based on Amazon CloudWatch alarms <https://docs.aws.amazon.com/appconfig/latest/userguide/getting-started-with-appconfig-cloudwatch-alarms-permissions.html>`_ in the *AWS AppConfig User Guide* .
        :param growth_type: The algorithm used to define how percentage grows over time. AWS AppConfig supports the following growth types:. *Linear* : For this type, AWS AppConfig processes the deployment by dividing the total number of targets by the value specified for ``Step percentage`` . For example, a linear deployment that uses a ``Step percentage`` of 10 deploys the configuration to 10 percent of the hosts. After those deployments are complete, the system deploys the configuration to the next 10 percent. This continues until 100% of the targets have successfully received the configuration. *Exponential* : For this type, AWS AppConfig processes the deployment exponentially using the following formula: ``G*(2^N)`` . In this formula, ``G`` is the growth factor specified by the user and ``N`` is the number of steps until the configuration is deployed to all targets. For example, if you specify a growth factor of 2, then the system rolls out the configuration as follows: ``2*(2^0)`` ``2*(2^1)`` ``2*(2^2)`` Expressed numerically, the deployment rolls out as follows: 2% of the targets, 4% of the targets, 8% of the targets, and continues until the configuration has been deployed to all targets.
        :param tags: Assigns metadata to an AWS AppConfig resource. Tags help organize and categorize your AWS AppConfig resources. Each tag consists of a key and an optional value, both of which you define. You can specify a maximum of 50 tags for a resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deploymentstrategy.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appconfig as appconfig
            
            cfn_deployment_strategy_props = appconfig.CfnDeploymentStrategyProps(
                deployment_duration_in_minutes=123,
                growth_factor=123,
                name="name",
                replicate_to="replicateTo",
            
                # the properties below are optional
                description="description",
                final_bake_time_in_minutes=123,
                growth_type="growthType",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__199999cc14040404b938fa601301d483ec681a01c3bd23495d2d90dde59820b5)
            check_type(argname="argument deployment_duration_in_minutes", value=deployment_duration_in_minutes, expected_type=type_hints["deployment_duration_in_minutes"])
            check_type(argname="argument growth_factor", value=growth_factor, expected_type=type_hints["growth_factor"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument replicate_to", value=replicate_to, expected_type=type_hints["replicate_to"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument final_bake_time_in_minutes", value=final_bake_time_in_minutes, expected_type=type_hints["final_bake_time_in_minutes"])
            check_type(argname="argument growth_type", value=growth_type, expected_type=type_hints["growth_type"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "deployment_duration_in_minutes": deployment_duration_in_minutes,
            "growth_factor": growth_factor,
            "name": name,
            "replicate_to": replicate_to,
        }
        if description is not None:
            self._values["description"] = description
        if final_bake_time_in_minutes is not None:
            self._values["final_bake_time_in_minutes"] = final_bake_time_in_minutes
        if growth_type is not None:
            self._values["growth_type"] = growth_type
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def deployment_duration_in_minutes(self) -> jsii.Number:
        '''Total amount of time for a deployment to last.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deploymentstrategy.html#cfn-appconfig-deploymentstrategy-deploymentdurationinminutes
        '''
        result = self._values.get("deployment_duration_in_minutes")
        assert result is not None, "Required property 'deployment_duration_in_minutes' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def growth_factor(self) -> jsii.Number:
        '''The percentage of targets to receive a deployed configuration during each interval.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deploymentstrategy.html#cfn-appconfig-deploymentstrategy-growthfactor
        '''
        result = self._values.get("growth_factor")
        assert result is not None, "Required property 'growth_factor' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''A name for the deployment strategy.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deploymentstrategy.html#cfn-appconfig-deploymentstrategy-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def replicate_to(self) -> builtins.str:
        '''Save the deployment strategy to a Systems Manager (SSM) document.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deploymentstrategy.html#cfn-appconfig-deploymentstrategy-replicateto
        '''
        result = self._values.get("replicate_to")
        assert result is not None, "Required property 'replicate_to' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the deployment strategy.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deploymentstrategy.html#cfn-appconfig-deploymentstrategy-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def final_bake_time_in_minutes(self) -> typing.Optional[jsii.Number]:
        '''Specifies the amount of time AWS AppConfig monitors for Amazon CloudWatch alarms after the configuration has been deployed to 100% of its targets, before considering the deployment to be complete.

        If an alarm is triggered during this time, AWS AppConfig rolls back the deployment. You must configure permissions for AWS AppConfig to roll back based on CloudWatch alarms. For more information, see `Configuring permissions for rollback based on Amazon CloudWatch alarms <https://docs.aws.amazon.com/appconfig/latest/userguide/getting-started-with-appconfig-cloudwatch-alarms-permissions.html>`_ in the *AWS AppConfig User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deploymentstrategy.html#cfn-appconfig-deploymentstrategy-finalbaketimeinminutes
        '''
        result = self._values.get("final_bake_time_in_minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def growth_type(self) -> typing.Optional[builtins.str]:
        '''The algorithm used to define how percentage grows over time. AWS AppConfig supports the following growth types:.

        *Linear* : For this type, AWS AppConfig processes the deployment by dividing the total number of targets by the value specified for ``Step percentage`` . For example, a linear deployment that uses a ``Step percentage`` of 10 deploys the configuration to 10 percent of the hosts. After those deployments are complete, the system deploys the configuration to the next 10 percent. This continues until 100% of the targets have successfully received the configuration.

        *Exponential* : For this type, AWS AppConfig processes the deployment exponentially using the following formula: ``G*(2^N)`` . In this formula, ``G`` is the growth factor specified by the user and ``N`` is the number of steps until the configuration is deployed to all targets. For example, if you specify a growth factor of 2, then the system rolls out the configuration as follows:

        ``2*(2^0)``

        ``2*(2^1)``

        ``2*(2^2)``

        Expressed numerically, the deployment rolls out as follows: 2% of the targets, 4% of the targets, 8% of the targets, and continues until the configuration has been deployed to all targets.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deploymentstrategy.html#cfn-appconfig-deploymentstrategy-growthtype
        '''
        result = self._values.get("growth_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Assigns metadata to an AWS AppConfig resource.

        Tags help organize and categorize your AWS AppConfig resources. Each tag consists of a key and an optional value, both of which you define. You can specify a maximum of 50 tags for a resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deploymentstrategy.html#cfn-appconfig-deploymentstrategy-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDeploymentStrategyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnEnvironment(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appconfig.CfnEnvironment",
):
    '''The ``AWS::AppConfig::Environment`` resource creates an environment, which is a logical deployment group of AWS AppConfig targets, such as applications in a ``Beta`` or ``Production`` environment.

    You define one or more environments for each AWS AppConfig application. You can also define environments for application subcomponents such as the ``Web`` , ``Mobile`` and ``Back-end`` components for your application. You can configure Amazon CloudWatch alarms for each environment. The system monitors alarms during a configuration deployment. If an alarm is triggered, the system rolls back the configuration.

    AWS AppConfig requires that you create resources and deploy a configuration in the following order:

    - Create an application
    - Create an environment
    - Create a configuration profile
    - Choose a pre-defined deployment strategy or create your own
    - Deploy the configuration

    For more information, see `AWS AppConfig <https://docs.aws.amazon.com/appconfig/latest/userguide/what-is-appconfig.html>`_ in the *AWS AppConfig User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-environment.html
    :cloudformationResource: AWS::AppConfig::Environment
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_appconfig as appconfig
        
        cfn_environment = appconfig.CfnEnvironment(self, "MyCfnEnvironment",
            application_id="applicationId",
            name="name",
        
            # the properties below are optional
            description="description",
            monitors=[appconfig.CfnEnvironment.MonitorsProperty(
                alarm_arn="alarmArn",
                alarm_role_arn="alarmRoleArn"
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
        application_id: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        monitors: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEnvironment.MonitorsProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param application_id: The application ID.
        :param name: A name for the environment.
        :param description: A description of the environment.
        :param monitors: Amazon CloudWatch alarms to monitor during the deployment process.
        :param tags: Metadata to assign to the environment. Tags help organize and categorize your AWS AppConfig resources. Each tag consists of a key and an optional value, both of which you define.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f357d5cab83004926812cf34c99a144f4f5d23ca26e4a818590a950622a06fc3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnEnvironmentProps(
            application_id=application_id,
            name=name,
            description=description,
            monitors=monitors,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3842dacad1a08e5d9103a4c646c8fa2385f77b6f5495fbd4dab597c037c8f09b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2dbe73a2ef533ed22edd7fd274c6cca5a979759478da06114e8699f7b2409820)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrEnvironmentId")
    def attr_environment_id(self) -> builtins.str:
        '''The environment ID.

        :cloudformationAttribute: EnvironmentId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEnvironmentId"))

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
    @jsii.member(jsii_name="applicationId")
    def application_id(self) -> builtins.str:
        '''The application ID.'''
        return typing.cast(builtins.str, jsii.get(self, "applicationId"))

    @application_id.setter
    def application_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d35c6a50b39401e18b97d5d78f1d4d92aaf846c18aa4ec32bce024a53e54c4be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationId", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''A name for the environment.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__569391bda37ae2bcb096c8b3ab953d25c7ff488899b2557c773cc8f72ee8a4cb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the environment.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__154bd59aabeed21e27800d9d45bcdbb412639a65e9aaaf72ef6dae673fa26a43)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="monitors")
    def monitors(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEnvironment.MonitorsProperty"]]]]:
        '''Amazon CloudWatch alarms to monitor during the deployment process.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEnvironment.MonitorsProperty"]]]], jsii.get(self, "monitors"))

    @monitors.setter
    def monitors(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEnvironment.MonitorsProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8d099ead34dfe7be9eb945722b31207889d993d21d927e1eeba6592c7f8fd44)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "monitors", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Metadata to assign to the environment.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60701727c0b2b8f0404d231ccc24899f35678bacc781ed4c6443de1b14432f68)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appconfig.CfnEnvironment.MonitorProperty",
        jsii_struct_bases=[],
        name_mapping={"alarm_arn": "alarmArn", "alarm_role_arn": "alarmRoleArn"},
    )
    class MonitorProperty:
        def __init__(
            self,
            *,
            alarm_arn: builtins.str,
            alarm_role_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Amazon CloudWatch alarms to monitor during the deployment process.

            :param alarm_arn: Amazon Resource Name (ARN) of the Amazon CloudWatch alarm.
            :param alarm_role_arn: ARN of an AWS Identity and Access Management (IAM) role for AWS AppConfig to monitor ``AlarmArn`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-environment-monitor.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appconfig as appconfig
                
                monitor_property = appconfig.CfnEnvironment.MonitorProperty(
                    alarm_arn="alarmArn",
                
                    # the properties below are optional
                    alarm_role_arn="alarmRoleArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__252b3a605905895f1b8ffc133b32547c64db1b58b121d4f635ec61960b027938)
                check_type(argname="argument alarm_arn", value=alarm_arn, expected_type=type_hints["alarm_arn"])
                check_type(argname="argument alarm_role_arn", value=alarm_role_arn, expected_type=type_hints["alarm_role_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "alarm_arn": alarm_arn,
            }
            if alarm_role_arn is not None:
                self._values["alarm_role_arn"] = alarm_role_arn

        @builtins.property
        def alarm_arn(self) -> builtins.str:
            '''Amazon Resource Name (ARN) of the Amazon CloudWatch alarm.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-environment-monitor.html#cfn-appconfig-environment-monitor-alarmarn
            '''
            result = self._values.get("alarm_arn")
            assert result is not None, "Required property 'alarm_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def alarm_role_arn(self) -> typing.Optional[builtins.str]:
            '''ARN of an AWS Identity and Access Management (IAM) role for AWS AppConfig to monitor ``AlarmArn`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-environment-monitor.html#cfn-appconfig-environment-monitor-alarmrolearn
            '''
            result = self._values.get("alarm_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appconfig.CfnEnvironment.MonitorsProperty",
        jsii_struct_bases=[],
        name_mapping={"alarm_arn": "alarmArn", "alarm_role_arn": "alarmRoleArn"},
    )
    class MonitorsProperty:
        def __init__(
            self,
            *,
            alarm_arn: typing.Optional[builtins.str] = None,
            alarm_role_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param alarm_arn: 
            :param alarm_role_arn: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-environment-monitors.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appconfig as appconfig
                
                monitors_property = appconfig.CfnEnvironment.MonitorsProperty(
                    alarm_arn="alarmArn",
                    alarm_role_arn="alarmRoleArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__43d91f41d1c9d1acd545d0999d47687e0e5b7be03ec08728e3c5aa73ff76549f)
                check_type(argname="argument alarm_arn", value=alarm_arn, expected_type=type_hints["alarm_arn"])
                check_type(argname="argument alarm_role_arn", value=alarm_role_arn, expected_type=type_hints["alarm_role_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if alarm_arn is not None:
                self._values["alarm_arn"] = alarm_arn
            if alarm_role_arn is not None:
                self._values["alarm_role_arn"] = alarm_role_arn

        @builtins.property
        def alarm_arn(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-environment-monitors.html#cfn-appconfig-environment-monitors-alarmarn
            '''
            result = self._values.get("alarm_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def alarm_role_arn(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-environment-monitors.html#cfn-appconfig-environment-monitors-alarmrolearn
            '''
            result = self._values.get("alarm_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitorsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appconfig.CfnEnvironmentProps",
    jsii_struct_bases=[],
    name_mapping={
        "application_id": "applicationId",
        "name": "name",
        "description": "description",
        "monitors": "monitors",
        "tags": "tags",
    },
)
class CfnEnvironmentProps:
    def __init__(
        self,
        *,
        application_id: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        monitors: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.MonitorsProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnEnvironment``.

        :param application_id: The application ID.
        :param name: A name for the environment.
        :param description: A description of the environment.
        :param monitors: Amazon CloudWatch alarms to monitor during the deployment process.
        :param tags: Metadata to assign to the environment. Tags help organize and categorize your AWS AppConfig resources. Each tag consists of a key and an optional value, both of which you define.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-environment.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appconfig as appconfig
            
            cfn_environment_props = appconfig.CfnEnvironmentProps(
                application_id="applicationId",
                name="name",
            
                # the properties below are optional
                description="description",
                monitors=[appconfig.CfnEnvironment.MonitorsProperty(
                    alarm_arn="alarmArn",
                    alarm_role_arn="alarmRoleArn"
                )],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6c9856f1a5a9dfaed9be42ec835bb6eac4d4882999b993cbd02b3b11bbfe1ca)
            check_type(argname="argument application_id", value=application_id, expected_type=type_hints["application_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument monitors", value=monitors, expected_type=type_hints["monitors"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_id": application_id,
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if monitors is not None:
            self._values["monitors"] = monitors
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def application_id(self) -> builtins.str:
        '''The application ID.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-environment.html#cfn-appconfig-environment-applicationid
        '''
        result = self._values.get("application_id")
        assert result is not None, "Required property 'application_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''A name for the environment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-environment.html#cfn-appconfig-environment-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the environment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-environment.html#cfn-appconfig-environment-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def monitors(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnEnvironment.MonitorsProperty]]]]:
        '''Amazon CloudWatch alarms to monitor during the deployment process.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-environment.html#cfn-appconfig-environment-monitors
        '''
        result = self._values.get("monitors")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnEnvironment.MonitorsProperty]]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Metadata to assign to the environment.

        Tags help organize and categorize your AWS AppConfig resources. Each tag consists of a key and an optional value, both of which you define.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-environment.html#cfn-appconfig-environment-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEnvironmentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnExtension(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appconfig.CfnExtension",
):
    '''Creates an AWS AppConfig extension.

    An extension augments your ability to inject logic or behavior at different points during the AWS AppConfig workflow of creating or deploying a configuration.

    You can create your own extensions or use the AWS authored extensions provided by AWS AppConfig . For an AWS AppConfig extension that uses AWS Lambda , you must create a Lambda function to perform any computation and processing defined in the extension. If you plan to create custom versions of the AWS authored notification extensions, you only need to specify an Amazon Resource Name (ARN) in the ``Uri`` field for the new extension version.

    - For a custom EventBridge notification extension, enter the ARN of the EventBridge default events in the ``Uri`` field.
    - For a custom Amazon SNS notification extension, enter the ARN of an Amazon SNS topic in the ``Uri`` field.
    - For a custom Amazon SQS notification extension, enter the ARN of an Amazon SQS message queue in the ``Uri`` field.

    For more information about extensions, see `Extending workflows <https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions.html>`_ in the *AWS AppConfig User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-extension.html
    :cloudformationResource: AWS::AppConfig::Extension
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_appconfig as appconfig
        
        # actions: Any
        
        cfn_extension = appconfig.CfnExtension(self, "MyCfnExtension",
            actions=actions,
            name="name",
        
            # the properties below are optional
            description="description",
            latest_version_number=123,
            parameters={
                "parameters_key": appconfig.CfnExtension.ParameterProperty(
                    required=False,
        
                    # the properties below are optional
                    description="description",
                    dynamic=False
                )
            },
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
        actions: typing.Any,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union["CfnExtension.ParameterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param actions: The actions defined in the extension.
        :param name: A name for the extension. Each extension name in your account must be unique. Extension versions use the same name.
        :param description: Information about the extension.
        :param latest_version_number: You can omit this field when you create an extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field.
        :param parameters: The parameters accepted by the extension. You specify parameter values when you associate the extension to an AWS AppConfig resource by using the ``CreateExtensionAssociation`` API action. For AWS Lambda extension actions, these parameters are included in the Lambda request object.
        :param tags: Adds one or more tags for the specified extension. Tags are metadata that help you categorize resources in different ways, for example, by purpose, owner, or environment. Each tag consists of a key and an optional value, both of which you define.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3442a7f4d7a9c3256544c6b0526d285ef0cf3970ec1f140b344aed1abc4eef5)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnExtensionProps(
            actions=actions,
            name=name,
            description=description,
            latest_version_number=latest_version_number,
            parameters=parameters,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6930a24c04bd5aebe54f7a225f7ec08743e520b61a781973e88a4b6678524a5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__57070195544dc008ade09c677ffa495cf4120e6b1dc834d6ffa101c3cf189599)
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
        '''The system-generated Amazon Resource Name (ARN) for the extension.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The system-generated ID of the extension.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrVersionNumber")
    def attr_version_number(self) -> jsii.Number:
        '''The extension version number.

        :cloudformationAttribute: VersionNumber
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrVersionNumber"))

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
    @jsii.member(jsii_name="actions")
    def actions(self) -> typing.Any:
        '''The actions defined in the extension.'''
        return typing.cast(typing.Any, jsii.get(self, "actions"))

    @actions.setter
    def actions(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f734d5e14d1ac32f7ec277282f23b1f2f7c0b8ce8e48d8df2b080f67d200577f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "actions", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''A name for the extension.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__081c55af29bf24c3599cf24134be4ce60656f052c575f59ff68c2084fa523481)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''Information about the extension.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__334508667f33fe5d26ff2e39e3bcbaaea618391e439f25094004fab0d75eb718)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="latestVersionNumber")
    def latest_version_number(self) -> typing.Optional[jsii.Number]:
        '''You can omit this field when you create an extension.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "latestVersionNumber"))

    @latest_version_number.setter
    def latest_version_number(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b38bdb75b51870401d0b83754078af02e3e6886d97a64481c3733b63a5a4c814)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "latestVersionNumber", value)

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, "CfnExtension.ParameterProperty"]]]]:
        '''The parameters accepted by the extension.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, "CfnExtension.ParameterProperty"]]]], jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, "CfnExtension.ParameterProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ad5fbf78cb34accb172520e561c08795fbca80280af2dcc78243ceb84841d07)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Adds one or more tags for the specified extension.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e6cc683bfd791a6ddfdc2295e58057279b3a19bc4adc7a11fbff993fe64fe37)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appconfig.CfnExtension.ActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "name": "name",
            "uri": "uri",
            "description": "description",
            "role_arn": "roleArn",
        },
    )
    class ActionProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            uri: builtins.str,
            description: typing.Optional[builtins.str] = None,
            role_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The actions defined in the extension.

            :param name: The action name.
            :param uri: The extension URI associated to the action point in the extension definition. The URI can be an Amazon Resource Name (ARN) for one of the following: an AWS Lambda function, an Amazon Simple Queue Service queue, an Amazon Simple Notification Service topic, or the Amazon EventBridge default event bus.
            :param description: Information about actions defined in the extension.
            :param role_arn: An Amazon Resource Name (ARN) for an AWS Identity and Access Management assume role.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-extension-action.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appconfig as appconfig
                
                action_property = appconfig.CfnExtension.ActionProperty(
                    name="name",
                    uri="uri",
                
                    # the properties below are optional
                    description="description",
                    role_arn="roleArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__58317247cdf8a690d14849381527f22c6a038c04470bb6ed420b3ade323b7e43)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument uri", value=uri, expected_type=type_hints["uri"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
                "uri": uri,
            }
            if description is not None:
                self._values["description"] = description
            if role_arn is not None:
                self._values["role_arn"] = role_arn

        @builtins.property
        def name(self) -> builtins.str:
            '''The action name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-extension-action.html#cfn-appconfig-extension-action-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def uri(self) -> builtins.str:
            '''The extension URI associated to the action point in the extension definition.

            The URI can be an Amazon Resource Name (ARN) for one of the following: an AWS Lambda function, an Amazon Simple Queue Service queue, an Amazon Simple Notification Service topic, or the Amazon EventBridge default event bus.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-extension-action.html#cfn-appconfig-extension-action-uri
            '''
            result = self._values.get("uri")
            assert result is not None, "Required property 'uri' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''Information about actions defined in the extension.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-extension-action.html#cfn-appconfig-extension-action-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def role_arn(self) -> typing.Optional[builtins.str]:
            '''An Amazon Resource Name (ARN) for an AWS Identity and Access Management assume role.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-extension-action.html#cfn-appconfig-extension-action-rolearn
            '''
            result = self._values.get("role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appconfig.CfnExtension.ParameterProperty",
        jsii_struct_bases=[],
        name_mapping={
            "required": "required",
            "description": "description",
            "dynamic": "dynamic",
        },
    )
    class ParameterProperty:
        def __init__(
            self,
            *,
            required: typing.Union[builtins.bool, _IResolvable_da3f097b],
            description: typing.Optional[builtins.str] = None,
            dynamic: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''A value such as an Amazon Resource Name (ARN) or an Amazon Simple Notification Service topic entered in an extension when invoked.

            Parameter values are specified in an extension association. For more information about extensions, see `Extending workflows <https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions.html>`_ in the *AWS AppConfig User Guide* .

            :param required: A parameter value must be specified in the extension association.
            :param description: Information about the parameter.
            :param dynamic: Indicates whether this parameter's value can be supplied at the extension's action point instead of during extension association. Dynamic parameters can't be marked ``Required`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-extension-parameter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appconfig as appconfig
                
                parameter_property = appconfig.CfnExtension.ParameterProperty(
                    required=False,
                
                    # the properties below are optional
                    description="description",
                    dynamic=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__683bc731900456f8d594ddc90d3c7fc1fcdc884942410401537639fad3d02ed1)
                check_type(argname="argument required", value=required, expected_type=type_hints["required"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument dynamic", value=dynamic, expected_type=type_hints["dynamic"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "required": required,
            }
            if description is not None:
                self._values["description"] = description
            if dynamic is not None:
                self._values["dynamic"] = dynamic

        @builtins.property
        def required(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''A parameter value must be specified in the extension association.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-extension-parameter.html#cfn-appconfig-extension-parameter-required
            '''
            result = self._values.get("required")
            assert result is not None, "Required property 'required' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''Information about the parameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-extension-parameter.html#cfn-appconfig-extension-parameter-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def dynamic(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates whether this parameter's value can be supplied at the extension's action point instead of during extension association.

            Dynamic parameters can't be marked ``Required`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-extension-parameter.html#cfn-appconfig-extension-parameter-dynamic
            '''
            result = self._values.get("dynamic")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnExtensionAssociation(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appconfig.CfnExtensionAssociation",
):
    '''When you create an extension or configure an AWS authored extension, you associate the extension with an AWS AppConfig application, environment, or configuration profile.

    For example, you can choose to run the ``AWS AppConfig deployment events to Amazon SNS`` AWS authored extension and receive notifications on an Amazon SNS topic anytime a configuration deployment is started for a specific application. Defining which extension to associate with an AWS AppConfig resource is called an *extension association* . An extension association is a specified relationship between an extension and an AWS AppConfig resource, such as an application or a configuration profile. For more information about extensions and associations, see `Extending workflows <https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions.html>`_ in the *AWS AppConfig User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-extensionassociation.html
    :cloudformationResource: AWS::AppConfig::ExtensionAssociation
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_appconfig as appconfig
        
        cfn_extension_association = appconfig.CfnExtensionAssociation(self, "MyCfnExtensionAssociation",
            extension_identifier="extensionIdentifier",
            extension_version_number=123,
            parameters={
                "parameters_key": "parameters"
            },
            resource_identifier="resourceIdentifier",
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
        extension_identifier: typing.Optional[builtins.str] = None,
        extension_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
        resource_identifier: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param extension_identifier: The name, the ID, or the Amazon Resource Name (ARN) of the extension.
        :param extension_version_number: The version number of the extension. If not specified, AWS AppConfig uses the maximum version of the extension.
        :param parameters: The parameter names and values defined in the extensions. Extension parameters marked ``Required`` must be entered for this field.
        :param resource_identifier: The ARN of an application, configuration profile, or environment.
        :param tags: Adds one or more tags for the specified extension association. Tags are metadata that help you categorize resources in different ways, for example, by purpose, owner, or environment. Each tag consists of a key and an optional value, both of which you define.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2e5a069dff64a93330fdfc39cee819956ed46cafa89dc1aee558b0c288de8af)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnExtensionAssociationProps(
            extension_identifier=extension_identifier,
            extension_version_number=extension_version_number,
            parameters=parameters,
            resource_identifier=resource_identifier,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__209622600665bfa16663cc19d0b91c8caf5c5d29f4cc7cb09fd6fba67bcb1739)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d0a9f34459bdf3e807e0362d7767352a597304250be35f36b98afb6b8d6ca733)
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
        '''The ARN of the extension defined in the association.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrExtensionArn")
    def attr_extension_arn(self) -> builtins.str:
        '''The ARN of the extension defined in the association.

        :cloudformationAttribute: ExtensionArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrExtensionArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The system-generated ID for the association.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrResourceArn")
    def attr_resource_arn(self) -> builtins.str:
        '''The ARNs of applications, configuration profiles, or environments defined in the association.

        :cloudformationAttribute: ResourceArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrResourceArn"))

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
    @jsii.member(jsii_name="extensionIdentifier")
    def extension_identifier(self) -> typing.Optional[builtins.str]:
        '''The name, the ID, or the Amazon Resource Name (ARN) of the extension.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "extensionIdentifier"))

    @extension_identifier.setter
    def extension_identifier(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd635cb248fd501f641536d553e5645fb6dd03b8db84e4059ddc6af591a307e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "extensionIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="extensionVersionNumber")
    def extension_version_number(self) -> typing.Optional[jsii.Number]:
        '''The version number of the extension.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "extensionVersionNumber"))

    @extension_version_number.setter
    def extension_version_number(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4aa600ead50aeb1f2d5f5f5fe334e3e11a16eccfa413e5de0742f763f7938a43)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "extensionVersionNumber", value)

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
        '''The parameter names and values defined in the extensions.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc72677d37ba0fe5b56dcbee5b8705c9e4e30a75b5d3b051bc792305dfd3deda)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value)

    @builtins.property
    @jsii.member(jsii_name="resourceIdentifier")
    def resource_identifier(self) -> typing.Optional[builtins.str]:
        '''The ARN of an application, configuration profile, or environment.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceIdentifier"))

    @resource_identifier.setter
    def resource_identifier(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ff48a7c10c5007769564f0b18da5363288efbb9ca805f7bb5a7fd93e791ec3d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Adds one or more tags for the specified extension association.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d31c336e3843162aab44371392cbb25a2b62fcd270c6fc472b3f2819a21b9ea1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appconfig.CfnExtensionAssociationProps",
    jsii_struct_bases=[],
    name_mapping={
        "extension_identifier": "extensionIdentifier",
        "extension_version_number": "extensionVersionNumber",
        "parameters": "parameters",
        "resource_identifier": "resourceIdentifier",
        "tags": "tags",
    },
)
class CfnExtensionAssociationProps:
    def __init__(
        self,
        *,
        extension_identifier: typing.Optional[builtins.str] = None,
        extension_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
        resource_identifier: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnExtensionAssociation``.

        :param extension_identifier: The name, the ID, or the Amazon Resource Name (ARN) of the extension.
        :param extension_version_number: The version number of the extension. If not specified, AWS AppConfig uses the maximum version of the extension.
        :param parameters: The parameter names and values defined in the extensions. Extension parameters marked ``Required`` must be entered for this field.
        :param resource_identifier: The ARN of an application, configuration profile, or environment.
        :param tags: Adds one or more tags for the specified extension association. Tags are metadata that help you categorize resources in different ways, for example, by purpose, owner, or environment. Each tag consists of a key and an optional value, both of which you define.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-extensionassociation.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appconfig as appconfig
            
            cfn_extension_association_props = appconfig.CfnExtensionAssociationProps(
                extension_identifier="extensionIdentifier",
                extension_version_number=123,
                parameters={
                    "parameters_key": "parameters"
                },
                resource_identifier="resourceIdentifier",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__658f796ad2928720e80bab1455b7c28527f38d13b4efe7780e0a592469829ce9)
            check_type(argname="argument extension_identifier", value=extension_identifier, expected_type=type_hints["extension_identifier"])
            check_type(argname="argument extension_version_number", value=extension_version_number, expected_type=type_hints["extension_version_number"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument resource_identifier", value=resource_identifier, expected_type=type_hints["resource_identifier"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if extension_identifier is not None:
            self._values["extension_identifier"] = extension_identifier
        if extension_version_number is not None:
            self._values["extension_version_number"] = extension_version_number
        if parameters is not None:
            self._values["parameters"] = parameters
        if resource_identifier is not None:
            self._values["resource_identifier"] = resource_identifier
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def extension_identifier(self) -> typing.Optional[builtins.str]:
        '''The name, the ID, or the Amazon Resource Name (ARN) of the extension.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-extensionassociation.html#cfn-appconfig-extensionassociation-extensionidentifier
        '''
        result = self._values.get("extension_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def extension_version_number(self) -> typing.Optional[jsii.Number]:
        '''The version number of the extension.

        If not specified, AWS AppConfig uses the maximum version of the extension.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-extensionassociation.html#cfn-appconfig-extensionassociation-extensionversionnumber
        '''
        result = self._values.get("extension_version_number")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
        '''The parameter names and values defined in the extensions.

        Extension parameters marked ``Required`` must be entered for this field.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-extensionassociation.html#cfn-appconfig-extensionassociation-parameters
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], result)

    @builtins.property
    def resource_identifier(self) -> typing.Optional[builtins.str]:
        '''The ARN of an application, configuration profile, or environment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-extensionassociation.html#cfn-appconfig-extensionassociation-resourceidentifier
        '''
        result = self._values.get("resource_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Adds one or more tags for the specified extension association.

        Tags are metadata that help you categorize resources in different ways, for example, by purpose, owner, or environment. Each tag consists of a key and an optional value, both of which you define.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-extensionassociation.html#cfn-appconfig-extensionassociation-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExtensionAssociationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appconfig.CfnExtensionProps",
    jsii_struct_bases=[],
    name_mapping={
        "actions": "actions",
        "name": "name",
        "description": "description",
        "latest_version_number": "latestVersionNumber",
        "parameters": "parameters",
        "tags": "tags",
    },
)
class CfnExtensionProps:
    def __init__(
        self,
        *,
        actions: typing.Any,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union[CfnExtension.ParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnExtension``.

        :param actions: The actions defined in the extension.
        :param name: A name for the extension. Each extension name in your account must be unique. Extension versions use the same name.
        :param description: Information about the extension.
        :param latest_version_number: You can omit this field when you create an extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field.
        :param parameters: The parameters accepted by the extension. You specify parameter values when you associate the extension to an AWS AppConfig resource by using the ``CreateExtensionAssociation`` API action. For AWS Lambda extension actions, these parameters are included in the Lambda request object.
        :param tags: Adds one or more tags for the specified extension. Tags are metadata that help you categorize resources in different ways, for example, by purpose, owner, or environment. Each tag consists of a key and an optional value, both of which you define.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-extension.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appconfig as appconfig
            
            # actions: Any
            
            cfn_extension_props = appconfig.CfnExtensionProps(
                actions=actions,
                name="name",
            
                # the properties below are optional
                description="description",
                latest_version_number=123,
                parameters={
                    "parameters_key": appconfig.CfnExtension.ParameterProperty(
                        required=False,
            
                        # the properties below are optional
                        description="description",
                        dynamic=False
                    )
                },
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a81148d01bee60e4140891afd5b9da3eab7a3dd5f81524eaa37f895ff781df1f)
            check_type(argname="argument actions", value=actions, expected_type=type_hints["actions"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument latest_version_number", value=latest_version_number, expected_type=type_hints["latest_version_number"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "actions": actions,
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if latest_version_number is not None:
            self._values["latest_version_number"] = latest_version_number
        if parameters is not None:
            self._values["parameters"] = parameters
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def actions(self) -> typing.Any:
        '''The actions defined in the extension.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-extension.html#cfn-appconfig-extension-actions
        '''
        result = self._values.get("actions")
        assert result is not None, "Required property 'actions' is missing"
        return typing.cast(typing.Any, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''A name for the extension.

        Each extension name in your account must be unique. Extension versions use the same name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-extension.html#cfn-appconfig-extension-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Information about the extension.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-extension.html#cfn-appconfig-extension-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def latest_version_number(self) -> typing.Optional[jsii.Number]:
        '''You can omit this field when you create an extension.

        When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-extension.html#cfn-appconfig-extension-latestversionnumber
        '''
        result = self._values.get("latest_version_number")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, CfnExtension.ParameterProperty]]]]:
        '''The parameters accepted by the extension.

        You specify parameter values when you associate the extension to an AWS AppConfig resource by using the ``CreateExtensionAssociation`` API action. For AWS Lambda extension actions, these parameters are included in the Lambda request object.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-extension.html#cfn-appconfig-extension-parameters
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, CfnExtension.ParameterProperty]]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Adds one or more tags for the specified extension.

        Tags are metadata that help you categorize resources in different ways, for example, by purpose, owner, or environment. Each tag consists of a key and an optional value, both of which you define.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-extension.html#cfn-appconfig-extension-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExtensionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnHostedConfigurationVersion(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appconfig.CfnHostedConfigurationVersion",
):
    '''Create a new configuration in the AWS AppConfig hosted configuration store.

    Configurations must be 1 MB or smaller. The AWS AppConfig hosted configuration store provides the following benefits over other configuration store options.

    - You don't need to set up and configure other services such as Amazon Simple Storage Service ( Amazon S3 ) or Parameter Store.
    - You don't need to configure AWS Identity and Access Management ( IAM ) permissions to use the configuration store.
    - You can store configurations in any content type.
    - There is no cost to use the store.
    - You can create a configuration and add it to the store when you create a configuration profile.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-hostedconfigurationversion.html
    :cloudformationResource: AWS::AppConfig::HostedConfigurationVersion
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_appconfig as appconfig
        
        cfn_hosted_configuration_version = appconfig.CfnHostedConfigurationVersion(self, "MyCfnHostedConfigurationVersion",
            application_id="applicationId",
            configuration_profile_id="configurationProfileId",
            content="content",
            content_type="contentType",
        
            # the properties below are optional
            description="description",
            latest_version_number=123,
            version_label="versionLabel"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        application_id: builtins.str,
        configuration_profile_id: builtins.str,
        content: builtins.str,
        content_type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        version_label: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param application_id: The application ID.
        :param configuration_profile_id: The configuration profile ID.
        :param content: The content of the configuration or the configuration data.
        :param content_type: A standard MIME type describing the format of the configuration content. For more information, see `Content-Type <https://docs.aws.amazon.com/https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.17>`_ .
        :param description: A description of the configuration.
        :param latest_version_number: An optional locking token used to prevent race conditions from overwriting configuration updates when creating a new version. To ensure your data is not overwritten when creating multiple hosted configuration versions in rapid succession, specify the version number of the latest hosted configuration version.
        :param version_label: A user-defined label for an AWS AppConfig hosted configuration version.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f2dc9ae7157f5223a79cf8ea4a7355ec285dbe0fda348428c6e0e6cdabbb60b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnHostedConfigurationVersionProps(
            application_id=application_id,
            configuration_profile_id=configuration_profile_id,
            content=content,
            content_type=content_type,
            description=description,
            latest_version_number=latest_version_number,
            version_label=version_label,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__287f244644cef79eb3704756fc9fd6f98e693a42df76727f726091d3190ab82c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__694959938824dc357bd7ac9b60be653c213df7cdcc44905d59d6e7d7e1182171)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrVersionNumber")
    def attr_version_number(self) -> builtins.str:
        '''The configuration version.

        :cloudformationAttribute: VersionNumber
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrVersionNumber"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="applicationId")
    def application_id(self) -> builtins.str:
        '''The application ID.'''
        return typing.cast(builtins.str, jsii.get(self, "applicationId"))

    @application_id.setter
    def application_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97e3d21e204bcf08a8dceb763729bfb70936f6d97ed550af3dfe101fac0f4331)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationId", value)

    @builtins.property
    @jsii.member(jsii_name="configurationProfileId")
    def configuration_profile_id(self) -> builtins.str:
        '''The configuration profile ID.'''
        return typing.cast(builtins.str, jsii.get(self, "configurationProfileId"))

    @configuration_profile_id.setter
    def configuration_profile_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4193469efc98930e2e72ffffb47c40bb1631526d907d8eaab051ac721dce3631)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configurationProfileId", value)

    @builtins.property
    @jsii.member(jsii_name="content")
    def content(self) -> builtins.str:
        '''The content of the configuration or the configuration data.'''
        return typing.cast(builtins.str, jsii.get(self, "content"))

    @content.setter
    def content(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac0de9d6bf3585fb47f9ad3fbb1d23a9a11447de5c02a24b6971d67ab3a7fa70)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "content", value)

    @builtins.property
    @jsii.member(jsii_name="contentType")
    def content_type(self) -> builtins.str:
        '''A standard MIME type describing the format of the configuration content.'''
        return typing.cast(builtins.str, jsii.get(self, "contentType"))

    @content_type.setter
    def content_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb880ec8c47eca7663501403482ddb505ffe759b4792fa0a7236d31e1313d7fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentType", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the configuration.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d43da3f82c30824ce1a2d29683403d6e68cb792341046055e7df42a980951259)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="latestVersionNumber")
    def latest_version_number(self) -> typing.Optional[jsii.Number]:
        '''An optional locking token used to prevent race conditions from overwriting configuration updates when creating a new version.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "latestVersionNumber"))

    @latest_version_number.setter
    def latest_version_number(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14797876de335768bb8254a37ba88bf3300df4a568a8174a333380741acaa4b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "latestVersionNumber", value)

    @builtins.property
    @jsii.member(jsii_name="versionLabel")
    def version_label(self) -> typing.Optional[builtins.str]:
        '''A user-defined label for an AWS AppConfig hosted configuration version.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionLabel"))

    @version_label.setter
    def version_label(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__384487882c55b43a28f4a742590e489e653df19c023a94fbfacb65cdf0cf00e2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "versionLabel", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appconfig.CfnHostedConfigurationVersionProps",
    jsii_struct_bases=[],
    name_mapping={
        "application_id": "applicationId",
        "configuration_profile_id": "configurationProfileId",
        "content": "content",
        "content_type": "contentType",
        "description": "description",
        "latest_version_number": "latestVersionNumber",
        "version_label": "versionLabel",
    },
)
class CfnHostedConfigurationVersionProps:
    def __init__(
        self,
        *,
        application_id: builtins.str,
        configuration_profile_id: builtins.str,
        content: builtins.str,
        content_type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        version_label: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnHostedConfigurationVersion``.

        :param application_id: The application ID.
        :param configuration_profile_id: The configuration profile ID.
        :param content: The content of the configuration or the configuration data.
        :param content_type: A standard MIME type describing the format of the configuration content. For more information, see `Content-Type <https://docs.aws.amazon.com/https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.17>`_ .
        :param description: A description of the configuration.
        :param latest_version_number: An optional locking token used to prevent race conditions from overwriting configuration updates when creating a new version. To ensure your data is not overwritten when creating multiple hosted configuration versions in rapid succession, specify the version number of the latest hosted configuration version.
        :param version_label: A user-defined label for an AWS AppConfig hosted configuration version.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-hostedconfigurationversion.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appconfig as appconfig
            
            cfn_hosted_configuration_version_props = appconfig.CfnHostedConfigurationVersionProps(
                application_id="applicationId",
                configuration_profile_id="configurationProfileId",
                content="content",
                content_type="contentType",
            
                # the properties below are optional
                description="description",
                latest_version_number=123,
                version_label="versionLabel"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2e12025d283b0b516fc7a346d00f20eff94d8259ba3fc82c8cb240aeb05264e)
            check_type(argname="argument application_id", value=application_id, expected_type=type_hints["application_id"])
            check_type(argname="argument configuration_profile_id", value=configuration_profile_id, expected_type=type_hints["configuration_profile_id"])
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument content_type", value=content_type, expected_type=type_hints["content_type"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument latest_version_number", value=latest_version_number, expected_type=type_hints["latest_version_number"])
            check_type(argname="argument version_label", value=version_label, expected_type=type_hints["version_label"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_id": application_id,
            "configuration_profile_id": configuration_profile_id,
            "content": content,
            "content_type": content_type,
        }
        if description is not None:
            self._values["description"] = description
        if latest_version_number is not None:
            self._values["latest_version_number"] = latest_version_number
        if version_label is not None:
            self._values["version_label"] = version_label

    @builtins.property
    def application_id(self) -> builtins.str:
        '''The application ID.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-hostedconfigurationversion.html#cfn-appconfig-hostedconfigurationversion-applicationid
        '''
        result = self._values.get("application_id")
        assert result is not None, "Required property 'application_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def configuration_profile_id(self) -> builtins.str:
        '''The configuration profile ID.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-hostedconfigurationversion.html#cfn-appconfig-hostedconfigurationversion-configurationprofileid
        '''
        result = self._values.get("configuration_profile_id")
        assert result is not None, "Required property 'configuration_profile_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def content(self) -> builtins.str:
        '''The content of the configuration or the configuration data.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-hostedconfigurationversion.html#cfn-appconfig-hostedconfigurationversion-content
        '''
        result = self._values.get("content")
        assert result is not None, "Required property 'content' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def content_type(self) -> builtins.str:
        '''A standard MIME type describing the format of the configuration content.

        For more information, see `Content-Type <https://docs.aws.amazon.com/https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.17>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-hostedconfigurationversion.html#cfn-appconfig-hostedconfigurationversion-contenttype
        '''
        result = self._values.get("content_type")
        assert result is not None, "Required property 'content_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-hostedconfigurationversion.html#cfn-appconfig-hostedconfigurationversion-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def latest_version_number(self) -> typing.Optional[jsii.Number]:
        '''An optional locking token used to prevent race conditions from overwriting configuration updates when creating a new version.

        To ensure your data is not overwritten when creating multiple hosted configuration versions in rapid succession, specify the version number of the latest hosted configuration version.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-hostedconfigurationversion.html#cfn-appconfig-hostedconfigurationversion-latestversionnumber
        '''
        result = self._values.get("latest_version_number")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def version_label(self) -> typing.Optional[builtins.str]:
        '''A user-defined label for an AWS AppConfig hosted configuration version.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-hostedconfigurationversion.html#cfn-appconfig-hostedconfigurationversion-versionlabel
        '''
        result = self._values.get("version_label")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnHostedConfigurationVersionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ConfigurationContent(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="aws-cdk-lib.aws_appconfig.ConfigurationContent",
):
    '''Defines the hosted configuration content.

    :exampleMetadata: infused

    Example::

        app = appconfig.Application(self, "MyApp")
        env = appconfig.Environment(self, "MyEnv",
            application=app
        )
        
        appconfig.HostedConfiguration(self, "MyHostedConfig",
            application=app,
            deploy_to=[env],
            content=appconfig.ConfigurationContent.from_inline_text("This is my configuration content.")
        )
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="fromFile")
    @builtins.classmethod
    def from_file(
        cls,
        input_path: builtins.str,
        content_type: typing.Optional[builtins.str] = None,
    ) -> "ConfigurationContent":
        '''Defines the hosted configuration content from a file.

        :param input_path: The path to the file that defines configuration content.
        :param content_type: The content type of the configuration.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90a444a396ae95bf4dbe20a3cba4428b472f8dc18cddec786f4ed521d3ef8224)
            check_type(argname="argument input_path", value=input_path, expected_type=type_hints["input_path"])
            check_type(argname="argument content_type", value=content_type, expected_type=type_hints["content_type"])
        return typing.cast("ConfigurationContent", jsii.sinvoke(cls, "fromFile", [input_path, content_type]))

    @jsii.member(jsii_name="fromInline")
    @builtins.classmethod
    def from_inline(
        cls,
        content: builtins.str,
        content_type: typing.Optional[builtins.str] = None,
    ) -> "ConfigurationContent":
        '''Defines the hosted configuration content from inline code.

        :param content: The inline code that defines the configuration content.
        :param content_type: The content type of the configuration.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3dc78a8c320c476850c109277461b0640bc3492938af15c32744671285117e99)
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument content_type", value=content_type, expected_type=type_hints["content_type"])
        return typing.cast("ConfigurationContent", jsii.sinvoke(cls, "fromInline", [content, content_type]))

    @jsii.member(jsii_name="fromInlineJson")
    @builtins.classmethod
    def from_inline_json(
        cls,
        content: builtins.str,
        content_type: typing.Optional[builtins.str] = None,
    ) -> "ConfigurationContent":
        '''Defines the hosted configuration content as JSON from inline code.

        :param content: The inline code that defines the configuration content.
        :param content_type: The content type of the configuration.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0be240b695740e98f6925d6eb7c6948c1cdff98558955885c2275a539fa4e5f0)
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument content_type", value=content_type, expected_type=type_hints["content_type"])
        return typing.cast("ConfigurationContent", jsii.sinvoke(cls, "fromInlineJson", [content, content_type]))

    @jsii.member(jsii_name="fromInlineText")
    @builtins.classmethod
    def from_inline_text(cls, content: builtins.str) -> "ConfigurationContent":
        '''Defines the hosted configuration content as text from inline code.

        :param content: The inline code that defines the configuration content.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5d1c66ba91caf344acedcb9844b33debef555ae94702faf53abe298e612f662)
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
        return typing.cast("ConfigurationContent", jsii.sinvoke(cls, "fromInlineText", [content]))

    @jsii.member(jsii_name="fromInlineYaml")
    @builtins.classmethod
    def from_inline_yaml(cls, content: builtins.str) -> "ConfigurationContent":
        '''Defines the hosted configuration content as YAML from inline code.

        :param content: The inline code that defines the configuration content.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af127c28dd1d72bacc88a31e7606c4f0729ead8629d2aa39eca948c88e6a19f9)
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
        return typing.cast("ConfigurationContent", jsii.sinvoke(cls, "fromInlineYaml", [content]))

    @builtins.property
    @jsii.member(jsii_name="content")
    @abc.abstractmethod
    def content(self) -> builtins.str:
        '''The configuration content.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="contentType")
    @abc.abstractmethod
    def content_type(self) -> builtins.str:
        '''The configuration content type.'''
        ...


class _ConfigurationContentProxy(ConfigurationContent):
    @builtins.property
    @jsii.member(jsii_name="content")
    def content(self) -> builtins.str:
        '''The configuration content.'''
        return typing.cast(builtins.str, jsii.get(self, "content"))

    @builtins.property
    @jsii.member(jsii_name="contentType")
    def content_type(self) -> builtins.str:
        '''The configuration content type.'''
        return typing.cast(builtins.str, jsii.get(self, "contentType"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, ConfigurationContent).__jsii_proxy_class__ = lambda : _ConfigurationContentProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appconfig.ConfigurationOptions",
    jsii_struct_bases=[],
    name_mapping={
        "deployment_key": "deploymentKey",
        "deployment_strategy": "deploymentStrategy",
        "deploy_to": "deployTo",
        "description": "description",
        "name": "name",
        "type": "type",
        "validators": "validators",
    },
)
class ConfigurationOptions:
    def __init__(
        self,
        *,
        deployment_key: typing.Optional[_IKey_5f11635f] = None,
        deployment_strategy: typing.Optional["IDeploymentStrategy"] = None,
        deploy_to: typing.Optional[typing.Sequence["IEnvironment"]] = None,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        type: typing.Optional["ConfigurationType"] = None,
        validators: typing.Optional[typing.Sequence["IValidator"]] = None,
    ) -> None:
        '''Options for the Configuration construct.

        :param deployment_key: The deployment key of the configuration. Default: - None.
        :param deployment_strategy: The deployment strategy for the configuration. Default: - A deployment strategy with the rollout strategy set to RolloutStrategy.CANARY_10_PERCENT_20_MINUTES
        :param deploy_to: The list of environments to deploy the configuration to. If this parameter is not specified, then there will be no deployment created alongside this configuration. Deployments can be added later using the ``IEnvironment.addDeployment`` or ``IEnvironment.addDeployments`` methods. Default: - None.
        :param description: The description of the configuration. Default: - No description.
        :param name: The name of the configuration. Default: - A name is generated.
        :param type: The type of configuration. Default: ConfigurationType.FREEFORM
        :param validators: The validators for the configuration. Default: - No validators.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appconfig as appconfig
            from aws_cdk import aws_kms as kms
            
            # deployment_strategy: appconfig.DeploymentStrategy
            # environment: appconfig.Environment
            # key: kms.Key
            # validator: appconfig.IValidator
            
            configuration_options = appconfig.ConfigurationOptions(
                deployment_key=key,
                deployment_strategy=deployment_strategy,
                deploy_to=[environment],
                description="description",
                name="name",
                type=appconfig.ConfigurationType.FREEFORM,
                validators=[validator]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d8aafff2e2f314c1c4bef6e213f0aaef56ff294051b33fee835ad5716a7e093)
            check_type(argname="argument deployment_key", value=deployment_key, expected_type=type_hints["deployment_key"])
            check_type(argname="argument deployment_strategy", value=deployment_strategy, expected_type=type_hints["deployment_strategy"])
            check_type(argname="argument deploy_to", value=deploy_to, expected_type=type_hints["deploy_to"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument validators", value=validators, expected_type=type_hints["validators"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if deployment_key is not None:
            self._values["deployment_key"] = deployment_key
        if deployment_strategy is not None:
            self._values["deployment_strategy"] = deployment_strategy
        if deploy_to is not None:
            self._values["deploy_to"] = deploy_to
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name
        if type is not None:
            self._values["type"] = type
        if validators is not None:
            self._values["validators"] = validators

    @builtins.property
    def deployment_key(self) -> typing.Optional[_IKey_5f11635f]:
        '''The deployment key of the configuration.

        :default: - None.
        '''
        result = self._values.get("deployment_key")
        return typing.cast(typing.Optional[_IKey_5f11635f], result)

    @builtins.property
    def deployment_strategy(self) -> typing.Optional["IDeploymentStrategy"]:
        '''The deployment strategy for the configuration.

        :default:

        - A deployment strategy with the rollout strategy set to
        RolloutStrategy.CANARY_10_PERCENT_20_MINUTES
        '''
        result = self._values.get("deployment_strategy")
        return typing.cast(typing.Optional["IDeploymentStrategy"], result)

    @builtins.property
    def deploy_to(self) -> typing.Optional[typing.List["IEnvironment"]]:
        '''The list of environments to deploy the configuration to.

        If this parameter is not specified, then there will be no
        deployment created alongside this configuration.

        Deployments can be added later using the ``IEnvironment.addDeployment`` or
        ``IEnvironment.addDeployments`` methods.

        :default: - None.
        '''
        result = self._values.get("deploy_to")
        return typing.cast(typing.Optional[typing.List["IEnvironment"]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the configuration.

        :default: - No description.
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the configuration.

        :default: - A name is generated.
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional["ConfigurationType"]:
        '''The type of configuration.

        :default: ConfigurationType.FREEFORM
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional["ConfigurationType"], result)

    @builtins.property
    def validators(self) -> typing.Optional[typing.List["IValidator"]]:
        '''The validators for the configuration.

        :default: - No validators.
        '''
        result = self._values.get("validators")
        return typing.cast(typing.Optional[typing.List["IValidator"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConfigurationOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appconfig.ConfigurationProps",
    jsii_struct_bases=[ConfigurationOptions],
    name_mapping={
        "deployment_key": "deploymentKey",
        "deployment_strategy": "deploymentStrategy",
        "deploy_to": "deployTo",
        "description": "description",
        "name": "name",
        "type": "type",
        "validators": "validators",
        "application": "application",
    },
)
class ConfigurationProps(ConfigurationOptions):
    def __init__(
        self,
        *,
        deployment_key: typing.Optional[_IKey_5f11635f] = None,
        deployment_strategy: typing.Optional["IDeploymentStrategy"] = None,
        deploy_to: typing.Optional[typing.Sequence["IEnvironment"]] = None,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        type: typing.Optional["ConfigurationType"] = None,
        validators: typing.Optional[typing.Sequence["IValidator"]] = None,
        application: "IApplication",
    ) -> None:
        '''Properties for the Configuration construct.

        :param deployment_key: The deployment key of the configuration. Default: - None.
        :param deployment_strategy: The deployment strategy for the configuration. Default: - A deployment strategy with the rollout strategy set to RolloutStrategy.CANARY_10_PERCENT_20_MINUTES
        :param deploy_to: The list of environments to deploy the configuration to. If this parameter is not specified, then there will be no deployment created alongside this configuration. Deployments can be added later using the ``IEnvironment.addDeployment`` or ``IEnvironment.addDeployments`` methods. Default: - None.
        :param description: The description of the configuration. Default: - No description.
        :param name: The name of the configuration. Default: - A name is generated.
        :param type: The type of configuration. Default: ConfigurationType.FREEFORM
        :param validators: The validators for the configuration. Default: - No validators.
        :param application: The application associated with the configuration.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appconfig as appconfig
            from aws_cdk import aws_kms as kms
            
            # application: appconfig.Application
            # deployment_strategy: appconfig.DeploymentStrategy
            # environment: appconfig.Environment
            # key: kms.Key
            # validator: appconfig.IValidator
            
            configuration_props = appconfig.ConfigurationProps(
                application=application,
            
                # the properties below are optional
                deployment_key=key,
                deployment_strategy=deployment_strategy,
                deploy_to=[environment],
                description="description",
                name="name",
                type=appconfig.ConfigurationType.FREEFORM,
                validators=[validator]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fde28a86ff967e860849eabd5d00b00f1f841ba2ded09e00655f2b7d433ef121)
            check_type(argname="argument deployment_key", value=deployment_key, expected_type=type_hints["deployment_key"])
            check_type(argname="argument deployment_strategy", value=deployment_strategy, expected_type=type_hints["deployment_strategy"])
            check_type(argname="argument deploy_to", value=deploy_to, expected_type=type_hints["deploy_to"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument validators", value=validators, expected_type=type_hints["validators"])
            check_type(argname="argument application", value=application, expected_type=type_hints["application"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application": application,
        }
        if deployment_key is not None:
            self._values["deployment_key"] = deployment_key
        if deployment_strategy is not None:
            self._values["deployment_strategy"] = deployment_strategy
        if deploy_to is not None:
            self._values["deploy_to"] = deploy_to
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name
        if type is not None:
            self._values["type"] = type
        if validators is not None:
            self._values["validators"] = validators

    @builtins.property
    def deployment_key(self) -> typing.Optional[_IKey_5f11635f]:
        '''The deployment key of the configuration.

        :default: - None.
        '''
        result = self._values.get("deployment_key")
        return typing.cast(typing.Optional[_IKey_5f11635f], result)

    @builtins.property
    def deployment_strategy(self) -> typing.Optional["IDeploymentStrategy"]:
        '''The deployment strategy for the configuration.

        :default:

        - A deployment strategy with the rollout strategy set to
        RolloutStrategy.CANARY_10_PERCENT_20_MINUTES
        '''
        result = self._values.get("deployment_strategy")
        return typing.cast(typing.Optional["IDeploymentStrategy"], result)

    @builtins.property
    def deploy_to(self) -> typing.Optional[typing.List["IEnvironment"]]:
        '''The list of environments to deploy the configuration to.

        If this parameter is not specified, then there will be no
        deployment created alongside this configuration.

        Deployments can be added later using the ``IEnvironment.addDeployment`` or
        ``IEnvironment.addDeployments`` methods.

        :default: - None.
        '''
        result = self._values.get("deploy_to")
        return typing.cast(typing.Optional[typing.List["IEnvironment"]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the configuration.

        :default: - No description.
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the configuration.

        :default: - A name is generated.
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional["ConfigurationType"]:
        '''The type of configuration.

        :default: ConfigurationType.FREEFORM
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional["ConfigurationType"], result)

    @builtins.property
    def validators(self) -> typing.Optional[typing.List["IValidator"]]:
        '''The validators for the configuration.

        :default: - No validators.
        '''
        result = self._values.get("validators")
        return typing.cast(typing.Optional[typing.List["IValidator"]], result)

    @builtins.property
    def application(self) -> "IApplication":
        '''The application associated with the configuration.'''
        result = self._values.get("application")
        assert result is not None, "Required property 'application' is missing"
        return typing.cast("IApplication", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ConfigurationSource(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="aws-cdk-lib.aws_appconfig.ConfigurationSource",
):
    '''Defines the integrated configuration sources.

    :exampleMetadata: infused

    Example::

        # application: appconfig.Application
        # bucket: s3.Bucket
        
        
        appconfig.SourcedConfiguration(self, "MySourcedConfiguration",
            application=application,
            location=appconfig.ConfigurationSource.from_bucket(bucket, "path/to/file.json"),
            type=appconfig.ConfigurationType.FEATURE_FLAGS,
            name="MyConfig",
            description="This is my sourced configuration from CDK."
        )
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="fromBucket")
    @builtins.classmethod
    def from_bucket(
        cls,
        bucket: _IBucket_42e086fd,
        object_key: builtins.str,
        key: typing.Optional[_IKey_5f11635f] = None,
    ) -> "ConfigurationSource":
        '''Defines configuration content from an Amazon S3 bucket.

        :param bucket: The S3 bucket where the configuration is stored.
        :param object_key: The path to the configuration.
        :param key: The KMS Key that the bucket is encrypted with.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e27dc717a0100d15b46f08976cbd9816d9234c98e20254c8d4090fd04187aa48)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument object_key", value=object_key, expected_type=type_hints["object_key"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
        return typing.cast("ConfigurationSource", jsii.sinvoke(cls, "fromBucket", [bucket, object_key, key]))

    @jsii.member(jsii_name="fromCfnDocument")
    @builtins.classmethod
    def from_cfn_document(
        cls,
        document: _CfnDocument_8b177f00,
    ) -> "ConfigurationSource":
        '''Defines configuration content from a Systems Manager (SSM) document.

        :param document: The SSM document where the configuration is stored.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f9f2ec1a2ab20cc29bcfe3f1d8216c56caff367e7c5fac53bb7e81cb5a4a385)
            check_type(argname="argument document", value=document, expected_type=type_hints["document"])
        return typing.cast("ConfigurationSource", jsii.sinvoke(cls, "fromCfnDocument", [document]))

    @jsii.member(jsii_name="fromParameter")
    @builtins.classmethod
    def from_parameter(
        cls,
        parameter: _IParameter_509a0f80,
        key: typing.Optional[_IKey_5f11635f] = None,
    ) -> "ConfigurationSource":
        '''Defines configuration content from a Systems Manager (SSM) Parameter Store parameter.

        :param parameter: The parameter where the configuration is stored.
        :param key: The KMS Key that the secure string is encrypted with.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd6b66aaa0f14b1ceb91da8242ecc9bb0684df0b51abed7aa97919255659d04d)
            check_type(argname="argument parameter", value=parameter, expected_type=type_hints["parameter"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
        return typing.cast("ConfigurationSource", jsii.sinvoke(cls, "fromParameter", [parameter, key]))

    @jsii.member(jsii_name="fromPipeline")
    @builtins.classmethod
    def from_pipeline(cls, pipeline: _IPipeline_0931f838) -> "ConfigurationSource":
        '''Defines configuration content from AWS CodePipeline.

        :param pipeline: The pipeline where the configuration is stored.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7947957f92568ae27b5114957b81b662d25a30e2da5f3c76e8d1158c12566aca)
            check_type(argname="argument pipeline", value=pipeline, expected_type=type_hints["pipeline"])
        return typing.cast("ConfigurationSource", jsii.sinvoke(cls, "fromPipeline", [pipeline]))

    @jsii.member(jsii_name="fromSecret")
    @builtins.classmethod
    def from_secret(cls, secret: _ISecret_6e020e6a) -> "ConfigurationSource":
        '''Defines configuration content from an AWS Secrets Manager secret.

        :param secret: The secret where the configuration is stored.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a73d209b4025c3cdaf34909720e3249a1d3d4989e16aec9d748a6e59bb835675)
            check_type(argname="argument secret", value=secret, expected_type=type_hints["secret"])
        return typing.cast("ConfigurationSource", jsii.sinvoke(cls, "fromSecret", [secret]))

    @builtins.property
    @jsii.member(jsii_name="locationUri")
    @abc.abstractmethod
    def location_uri(self) -> builtins.str:
        '''The URI of the configuration source.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="type")
    @abc.abstractmethod
    def type(self) -> "ConfigurationSourceType":
        '''The type of the configuration source.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="key")
    @abc.abstractmethod
    def key(self) -> typing.Optional[_IKey_5f11635f]:
        '''The KMS Key that encrypts the configuration.'''
        ...


class _ConfigurationSourceProxy(ConfigurationSource):
    @builtins.property
    @jsii.member(jsii_name="locationUri")
    def location_uri(self) -> builtins.str:
        '''The URI of the configuration source.'''
        return typing.cast(builtins.str, jsii.get(self, "locationUri"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> "ConfigurationSourceType":
        '''The type of the configuration source.'''
        return typing.cast("ConfigurationSourceType", jsii.get(self, "type"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> typing.Optional[_IKey_5f11635f]:
        '''The KMS Key that encrypts the configuration.'''
        return typing.cast(typing.Optional[_IKey_5f11635f], jsii.get(self, "key"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, ConfigurationSource).__jsii_proxy_class__ = lambda : _ConfigurationSourceProxy


@jsii.enum(jsii_type="aws-cdk-lib.aws_appconfig.ConfigurationSourceType")
class ConfigurationSourceType(enum.Enum):
    '''The configuration source type.'''

    S3 = "S3"
    SECRETS_MANAGER = "SECRETS_MANAGER"
    SSM_PARAMETER = "SSM_PARAMETER"
    SSM_DOCUMENT = "SSM_DOCUMENT"
    CODE_PIPELINE = "CODE_PIPELINE"


@jsii.enum(jsii_type="aws-cdk-lib.aws_appconfig.ConfigurationType")
class ConfigurationType(enum.Enum):
    '''The configuration type.

    :exampleMetadata: infused

    Example::

        # application: appconfig.Application
        
        
        appconfig.HostedConfiguration(self, "MyHostedConfiguration",
            application=application,
            content=appconfig.ConfigurationContent.from_inline_text("This is my configuration content."),
            type=appconfig.ConfigurationType.FEATURE_FLAGS
        )
    '''

    FREEFORM = "FREEFORM"
    '''Freeform configuration profile.

    Allows you to store your data in the AWS AppConfig
    hosted configuration store or another Systems Manager capability or AWS service that integrates
    with AWS AppConfig.

    :see: https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-free-form-configurations-creating.html
    '''
    FEATURE_FLAGS = "FEATURE_FLAGS"
    '''Feature flag configuration profile.

    This configuration stores its data
    in the AWS AppConfig hosted configuration store and the URI is simply hosted.
    '''


class DeploymentStrategyId(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="aws-cdk-lib.aws_appconfig.DeploymentStrategyId",
):
    '''Defines the deployment strategy ID's of AWS AppConfig deployment strategies.

    :see: https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-deployment-strategy.html
    :exampleMetadata: infused

    Example::

        appconfig.DeploymentStrategy.from_deployment_strategy_id(self, "MyImportedDeploymentStrategy", appconfig.DeploymentStrategyId.from_string("abc123"))
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="fromString")
    @builtins.classmethod
    def from_string(
        cls,
        deployment_strategy_id: builtins.str,
    ) -> "DeploymentStrategyId":
        '''Builds a deployment strategy ID from a string.

        :param deployment_strategy_id: The deployment strategy ID.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8463842034a8619eb54964cc08c28aa3cea9fcdbf4e58de63f128b5b5322da8)
            check_type(argname="argument deployment_strategy_id", value=deployment_strategy_id, expected_type=type_hints["deployment_strategy_id"])
        return typing.cast("DeploymentStrategyId", jsii.sinvoke(cls, "fromString", [deployment_strategy_id]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ALL_AT_ONCE")
    def ALL_AT_ONCE(cls) -> "DeploymentStrategyId":
        '''**Quick**.

        This strategy deploys the configuration to all targets immediately.
        '''
        return typing.cast("DeploymentStrategyId", jsii.sget(cls, "ALL_AT_ONCE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CANARY_10_PERCENT_20_MINUTES")
    def CANARY_10_PERCENT_20_MINUTES(cls) -> "DeploymentStrategyId":
        '''**AWS Recommended**.

        This strategy processes the deployment exponentially using a 10% growth factor over 20 minutes.
        AWS AppConfig recommends using this strategy for production deployments because it aligns with AWS best practices
        for configuration deployments.
        '''
        return typing.cast("DeploymentStrategyId", jsii.sget(cls, "CANARY_10_PERCENT_20_MINUTES"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="LINEAR_20_PERCENT_EVERY_6_MINUTES")
    def LINEAR_20_PERCENT_EVERY_6_MINUTES(cls) -> "DeploymentStrategyId":
        '''**AWS Recommended**.

        This strategy deploys the configuration to 20% of all targets every six minutes for a 30 minute deployment.
        AWS AppConfig recommends using this strategy for production deployments because it aligns with AWS best practices
        for configuration deployments.
        '''
        return typing.cast("DeploymentStrategyId", jsii.sget(cls, "LINEAR_20_PERCENT_EVERY_6_MINUTES"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="LINEAR_50_PERCENT_EVERY_30_SECONDS")
    def LINEAR_50_PERCENT_EVERY_30_SECONDS(cls) -> "DeploymentStrategyId":
        '''**Testing/Demonstration**.

        This strategy deploys the configuration to half of all targets every 30 seconds for a
        one-minute deployment. AWS AppConfig recommends using this strategy only for testing or demonstration purposes because
        it has a short duration and bake time.
        '''
        return typing.cast("DeploymentStrategyId", jsii.sget(cls, "LINEAR_50_PERCENT_EVERY_30_SECONDS"))

    @builtins.property
    @jsii.member(jsii_name="id")
    @abc.abstractmethod
    def id(self) -> builtins.str:
        '''The deployment strategy ID.'''
        ...


class _DeploymentStrategyIdProxy(DeploymentStrategyId):
    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        '''The deployment strategy ID.'''
        return typing.cast(builtins.str, jsii.get(self, "id"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, DeploymentStrategyId).__jsii_proxy_class__ = lambda : _DeploymentStrategyIdProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appconfig.DeploymentStrategyProps",
    jsii_struct_bases=[],
    name_mapping={
        "rollout_strategy": "rolloutStrategy",
        "deployment_strategy_name": "deploymentStrategyName",
        "description": "description",
    },
)
class DeploymentStrategyProps:
    def __init__(
        self,
        *,
        rollout_strategy: "RolloutStrategy",
        deployment_strategy_name: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for DeploymentStrategy.

        :param rollout_strategy: The rollout strategy for the deployment strategy. You can use predefined deployment strategies, such as RolloutStrategy.ALL_AT_ONCE, RolloutStrategy.LINEAR_50_PERCENT_EVERY_30_SECONDS, or RolloutStrategy.CANARY_10_PERCENT_20_MINUTES.
        :param deployment_strategy_name: A name for the deployment strategy. Default: - A name is generated.
        :param description: A description of the deployment strategy. Default: - No description.

        :exampleMetadata: infused

        Example::

            appconfig.DeploymentStrategy(self, "MyDeploymentStrategy",
                rollout_strategy=appconfig.RolloutStrategy.linear(
                    growth_factor=20,
                    deployment_duration=Duration.minutes(30),
                    final_bake_time=Duration.minutes(30)
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b2751d6de1bb1e5195de3102d4fca0a566bedf6102d7bf2ce66a0d8291280f5)
            check_type(argname="argument rollout_strategy", value=rollout_strategy, expected_type=type_hints["rollout_strategy"])
            check_type(argname="argument deployment_strategy_name", value=deployment_strategy_name, expected_type=type_hints["deployment_strategy_name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "rollout_strategy": rollout_strategy,
        }
        if deployment_strategy_name is not None:
            self._values["deployment_strategy_name"] = deployment_strategy_name
        if description is not None:
            self._values["description"] = description

    @builtins.property
    def rollout_strategy(self) -> "RolloutStrategy":
        '''The rollout strategy for the deployment strategy.

        You can use predefined deployment
        strategies, such as RolloutStrategy.ALL_AT_ONCE, RolloutStrategy.LINEAR_50_PERCENT_EVERY_30_SECONDS,
        or RolloutStrategy.CANARY_10_PERCENT_20_MINUTES.
        '''
        result = self._values.get("rollout_strategy")
        assert result is not None, "Required property 'rollout_strategy' is missing"
        return typing.cast("RolloutStrategy", result)

    @builtins.property
    def deployment_strategy_name(self) -> typing.Optional[builtins.str]:
        '''A name for the deployment strategy.

        :default: - A name is generated.
        '''
        result = self._values.get("deployment_strategy_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the deployment strategy.

        :default: - No description.
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DeploymentStrategyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appconfig.EnvironmentAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "application": "application",
        "environment_id": "environmentId",
        "description": "description",
        "monitors": "monitors",
        "name": "name",
    },
)
class EnvironmentAttributes:
    def __init__(
        self,
        *,
        application: "IApplication",
        environment_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        monitors: typing.Optional[typing.Sequence["Monitor"]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Attributes of an existing AWS AppConfig environment to import it.

        :param application: The application associated with the environment.
        :param environment_id: The ID of the environment.
        :param description: The description of the environment. Default: - None.
        :param monitors: The monitors for the environment. Default: - None.
        :param name: The name of the environment. Default: - None.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appconfig as appconfig
            
            # application: appconfig.Application
            # monitor: appconfig.Monitor
            
            environment_attributes = appconfig.EnvironmentAttributes(
                application=application,
                environment_id="environmentId",
            
                # the properties below are optional
                description="description",
                monitors=[monitor],
                name="name"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37c9050d36cf121416083b853e136100e069c334aadd707074579edb0620bf52)
            check_type(argname="argument application", value=application, expected_type=type_hints["application"])
            check_type(argname="argument environment_id", value=environment_id, expected_type=type_hints["environment_id"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument monitors", value=monitors, expected_type=type_hints["monitors"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application": application,
            "environment_id": environment_id,
        }
        if description is not None:
            self._values["description"] = description
        if monitors is not None:
            self._values["monitors"] = monitors
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def application(self) -> "IApplication":
        '''The application associated with the environment.'''
        result = self._values.get("application")
        assert result is not None, "Required property 'application' is missing"
        return typing.cast("IApplication", result)

    @builtins.property
    def environment_id(self) -> builtins.str:
        '''The ID of the environment.'''
        result = self._values.get("environment_id")
        assert result is not None, "Required property 'environment_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the environment.

        :default: - None.
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def monitors(self) -> typing.Optional[typing.List["Monitor"]]:
        '''The monitors for the environment.

        :default: - None.
        '''
        result = self._values.get("monitors")
        return typing.cast(typing.Optional[typing.List["Monitor"]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the environment.

        :default: - None.
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EnvironmentAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appconfig.EnvironmentOptions",
    jsii_struct_bases=[],
    name_mapping={
        "description": "description",
        "environment_name": "environmentName",
        "monitors": "monitors",
    },
)
class EnvironmentOptions:
    def __init__(
        self,
        *,
        description: typing.Optional[builtins.str] = None,
        environment_name: typing.Optional[builtins.str] = None,
        monitors: typing.Optional[typing.Sequence["Monitor"]] = None,
    ) -> None:
        '''Options for the Environment construct.

        :param description: The description of the environment. Default: - No description.
        :param environment_name: The name of the environment. Default: - A name is generated.
        :param monitors: The monitors for the environment. Default: - No monitors.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appconfig as appconfig
            
            # monitor: appconfig.Monitor
            
            environment_options = appconfig.EnvironmentOptions(
                description="description",
                environment_name="environmentName",
                monitors=[monitor]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fbb7b0217b9bc7608bc896aa9827a29bb06de82b32c07cf8d98954734cdae547)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument environment_name", value=environment_name, expected_type=type_hints["environment_name"])
            check_type(argname="argument monitors", value=monitors, expected_type=type_hints["monitors"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if description is not None:
            self._values["description"] = description
        if environment_name is not None:
            self._values["environment_name"] = environment_name
        if monitors is not None:
            self._values["monitors"] = monitors

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the environment.

        :default: - No description.
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def environment_name(self) -> typing.Optional[builtins.str]:
        '''The name of the environment.

        :default: - A name is generated.
        '''
        result = self._values.get("environment_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def monitors(self) -> typing.Optional[typing.List["Monitor"]]:
        '''The monitors for the environment.

        :default: - No monitors.
        '''
        result = self._values.get("monitors")
        return typing.cast(typing.Optional[typing.List["Monitor"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EnvironmentOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appconfig.EnvironmentProps",
    jsii_struct_bases=[EnvironmentOptions],
    name_mapping={
        "description": "description",
        "environment_name": "environmentName",
        "monitors": "monitors",
        "application": "application",
    },
)
class EnvironmentProps(EnvironmentOptions):
    def __init__(
        self,
        *,
        description: typing.Optional[builtins.str] = None,
        environment_name: typing.Optional[builtins.str] = None,
        monitors: typing.Optional[typing.Sequence["Monitor"]] = None,
        application: "IApplication",
    ) -> None:
        '''Properties for the Environment construct.

        :param description: The description of the environment. Default: - No description.
        :param environment_name: The name of the environment. Default: - A name is generated.
        :param monitors: The monitors for the environment. Default: - No monitors.
        :param application: The application to be associated with the environment.

        :exampleMetadata: infused

        Example::

            app = appconfig.Application(self, "MyApp")
            env = appconfig.Environment(self, "MyEnv",
                application=app
            )
            
            appconfig.HostedConfiguration(self, "MyFirstHostedConfig",
                application=app,
                deploy_to=[env],
                content=appconfig.ConfigurationContent.from_inline_text("This is my first configuration content.")
            )
            
            appconfig.HostedConfiguration(self, "MySecondHostedConfig",
                application=app,
                deploy_to=[env],
                content=appconfig.ConfigurationContent.from_inline_text("This is my second configuration content.")
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70814b8db38d5e11a0b33e43663913fb290e190ace3191585fc4d0bd4c97bfff)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument environment_name", value=environment_name, expected_type=type_hints["environment_name"])
            check_type(argname="argument monitors", value=monitors, expected_type=type_hints["monitors"])
            check_type(argname="argument application", value=application, expected_type=type_hints["application"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application": application,
        }
        if description is not None:
            self._values["description"] = description
        if environment_name is not None:
            self._values["environment_name"] = environment_name
        if monitors is not None:
            self._values["monitors"] = monitors

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the environment.

        :default: - No description.
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def environment_name(self) -> typing.Optional[builtins.str]:
        '''The name of the environment.

        :default: - A name is generated.
        '''
        result = self._values.get("environment_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def monitors(self) -> typing.Optional[typing.List["Monitor"]]:
        '''The monitors for the environment.

        :default: - No monitors.
        '''
        result = self._values.get("monitors")
        return typing.cast(typing.Optional[typing.List["Monitor"]], result)

    @builtins.property
    def application(self) -> "IApplication":
        '''The application to be associated with the environment.'''
        result = self._values.get("application")
        assert result is not None, "Required property 'application' is missing"
        return typing.cast("IApplication", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EnvironmentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appconfig.ExtensionAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "extension_id": "extensionId",
        "extension_version_number": "extensionVersionNumber",
        "actions": "actions",
        "description": "description",
        "extension_arn": "extensionArn",
        "name": "name",
    },
)
class ExtensionAttributes:
    def __init__(
        self,
        *,
        extension_id: builtins.str,
        extension_version_number: jsii.Number,
        actions: typing.Optional[typing.Sequence[Action]] = None,
        description: typing.Optional[builtins.str] = None,
        extension_arn: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Attributes of an existing AWS AppConfig extension to import.

        :param extension_id: The ID of the extension.
        :param extension_version_number: The version number of the extension.
        :param actions: The actions of the extension. Default: - None.
        :param description: The description of the extension. Default: - None.
        :param extension_arn: The Amazon Resource Name (ARN) of the extension. Default: - The extension ARN is generated.
        :param name: The name of the extension. Default: - None.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appconfig as appconfig
            
            # action: appconfig.Action
            
            extension_attributes = appconfig.ExtensionAttributes(
                extension_id="extensionId",
                extension_version_number=123,
            
                # the properties below are optional
                actions=[action],
                description="description",
                extension_arn="extensionArn",
                name="name"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11f1d1fbf4b9190d06fa9b9ba49d1f42b2396559148c034133b90f93955b93cc)
            check_type(argname="argument extension_id", value=extension_id, expected_type=type_hints["extension_id"])
            check_type(argname="argument extension_version_number", value=extension_version_number, expected_type=type_hints["extension_version_number"])
            check_type(argname="argument actions", value=actions, expected_type=type_hints["actions"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument extension_arn", value=extension_arn, expected_type=type_hints["extension_arn"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "extension_id": extension_id,
            "extension_version_number": extension_version_number,
        }
        if actions is not None:
            self._values["actions"] = actions
        if description is not None:
            self._values["description"] = description
        if extension_arn is not None:
            self._values["extension_arn"] = extension_arn
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def extension_id(self) -> builtins.str:
        '''The ID of the extension.'''
        result = self._values.get("extension_id")
        assert result is not None, "Required property 'extension_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def extension_version_number(self) -> jsii.Number:
        '''The version number of the extension.'''
        result = self._values.get("extension_version_number")
        assert result is not None, "Required property 'extension_version_number' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def actions(self) -> typing.Optional[typing.List[Action]]:
        '''The actions of the extension.

        :default: - None.
        '''
        result = self._values.get("actions")
        return typing.cast(typing.Optional[typing.List[Action]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the extension.

        :default: - None.
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def extension_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the extension.

        :default: - The extension ARN is generated.
        '''
        result = self._values.get("extension_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the extension.

        :default: - None.
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExtensionAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appconfig.ExtensionOptions",
    jsii_struct_bases=[],
    name_mapping={
        "description": "description",
        "extension_name": "extensionName",
        "latest_version_number": "latestVersionNumber",
        "parameters": "parameters",
    },
)
class ExtensionOptions:
    def __init__(
        self,
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence["Parameter"]] = None,
    ) -> None:
        '''Options for the Extension construct.

        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appconfig as appconfig
            
            # parameter: appconfig.Parameter
            
            extension_options = appconfig.ExtensionOptions(
                description="description",
                extension_name="extensionName",
                latest_version_number=123,
                parameters=[parameter]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e71eebf3abb67e3bfb63792c1df83d0e0e153e5e160fd92004f78031c885a39)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument extension_name", value=extension_name, expected_type=type_hints["extension_name"])
            check_type(argname="argument latest_version_number", value=latest_version_number, expected_type=type_hints["latest_version_number"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if description is not None:
            self._values["description"] = description
        if extension_name is not None:
            self._values["extension_name"] = extension_name
        if latest_version_number is not None:
            self._values["latest_version_number"] = latest_version_number
        if parameters is not None:
            self._values["parameters"] = parameters

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the extension.

        :default: - No description.
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def extension_name(self) -> typing.Optional[builtins.str]:
        '''The name of the extension.

        :default: - A name is generated.
        '''
        result = self._values.get("extension_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def latest_version_number(self) -> typing.Optional[jsii.Number]:
        '''The latest version number of the extension.

        When you create a new version,
        specify the most recent current version number. For example, you create version 3,
        enter 2 for this field.

        :default: - None.
        '''
        result = self._values.get("latest_version_number")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def parameters(self) -> typing.Optional[typing.List["Parameter"]]:
        '''The parameters accepted for the extension.

        :default: - None.
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.List["Parameter"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExtensionOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appconfig.ExtensionProps",
    jsii_struct_bases=[ExtensionOptions],
    name_mapping={
        "description": "description",
        "extension_name": "extensionName",
        "latest_version_number": "latestVersionNumber",
        "parameters": "parameters",
        "actions": "actions",
    },
)
class ExtensionProps(ExtensionOptions):
    def __init__(
        self,
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence["Parameter"]] = None,
        actions: typing.Sequence[Action],
    ) -> None:
        '''Properties for the Extension construct.

        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        :param actions: The actions for the extension.

        :exampleMetadata: infused

        Example::

            # fn: lambda.Function
            
            
            appconfig.Extension(self, "MyExtension",
                actions=[
                    appconfig.Action(
                        action_points=[appconfig.ActionPoint.ON_DEPLOYMENT_START],
                        event_destination=appconfig.LambdaDestination(fn)
                    )
                ]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__003bfe5f4d042a69eceddde85ccfcfdb2e64aaea78e2842680880437998cd38f)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument extension_name", value=extension_name, expected_type=type_hints["extension_name"])
            check_type(argname="argument latest_version_number", value=latest_version_number, expected_type=type_hints["latest_version_number"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument actions", value=actions, expected_type=type_hints["actions"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "actions": actions,
        }
        if description is not None:
            self._values["description"] = description
        if extension_name is not None:
            self._values["extension_name"] = extension_name
        if latest_version_number is not None:
            self._values["latest_version_number"] = latest_version_number
        if parameters is not None:
            self._values["parameters"] = parameters

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the extension.

        :default: - No description.
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def extension_name(self) -> typing.Optional[builtins.str]:
        '''The name of the extension.

        :default: - A name is generated.
        '''
        result = self._values.get("extension_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def latest_version_number(self) -> typing.Optional[jsii.Number]:
        '''The latest version number of the extension.

        When you create a new version,
        specify the most recent current version number. For example, you create version 3,
        enter 2 for this field.

        :default: - None.
        '''
        result = self._values.get("latest_version_number")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def parameters(self) -> typing.Optional[typing.List["Parameter"]]:
        '''The parameters accepted for the extension.

        :default: - None.
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.List["Parameter"]], result)

    @builtins.property
    def actions(self) -> typing.List[Action]:
        '''The actions for the extension.'''
        result = self._values.get("actions")
        assert result is not None, "Required property 'actions' is missing"
        return typing.cast(typing.List[Action], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExtensionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_appconfig.GrowthType")
class GrowthType(enum.Enum):
    '''Defines the growth type of the deployment strategy.'''

    LINEAR = "LINEAR"
    '''AWS AppConfig will process the deployment by increments of the growth factor evenly distributed over the deployment.'''
    EXPONENTIAL = "EXPONENTIAL"
    '''AWS AppConfig will process the deployment exponentially using the following formula: ``G*(2^N)``.

    In this formula, ``G`` is the step percentage specified by the user and ``N``
    is the number of steps until the configuration is deployed to all targets.
    '''


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appconfig.HostedConfigurationOptions",
    jsii_struct_bases=[ConfigurationOptions],
    name_mapping={
        "deployment_key": "deploymentKey",
        "deployment_strategy": "deploymentStrategy",
        "deploy_to": "deployTo",
        "description": "description",
        "name": "name",
        "type": "type",
        "validators": "validators",
        "content": "content",
        "latest_version_number": "latestVersionNumber",
        "version_label": "versionLabel",
    },
)
class HostedConfigurationOptions(ConfigurationOptions):
    def __init__(
        self,
        *,
        deployment_key: typing.Optional[_IKey_5f11635f] = None,
        deployment_strategy: typing.Optional["IDeploymentStrategy"] = None,
        deploy_to: typing.Optional[typing.Sequence["IEnvironment"]] = None,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        type: typing.Optional[ConfigurationType] = None,
        validators: typing.Optional[typing.Sequence["IValidator"]] = None,
        content: ConfigurationContent,
        latest_version_number: typing.Optional[jsii.Number] = None,
        version_label: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Options for HostedConfiguration.

        :param deployment_key: The deployment key of the configuration. Default: - None.
        :param deployment_strategy: The deployment strategy for the configuration. Default: - A deployment strategy with the rollout strategy set to RolloutStrategy.CANARY_10_PERCENT_20_MINUTES
        :param deploy_to: The list of environments to deploy the configuration to. If this parameter is not specified, then there will be no deployment created alongside this configuration. Deployments can be added later using the ``IEnvironment.addDeployment`` or ``IEnvironment.addDeployments`` methods. Default: - None.
        :param description: The description of the configuration. Default: - No description.
        :param name: The name of the configuration. Default: - A name is generated.
        :param type: The type of configuration. Default: ConfigurationType.FREEFORM
        :param validators: The validators for the configuration. Default: - No validators.
        :param content: The content of the hosted configuration.
        :param latest_version_number: The latest version number of the hosted configuration. Default: - None.
        :param version_label: The version label of the hosted configuration. Default: - None.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appconfig as appconfig
            from aws_cdk import aws_kms as kms
            
            # configuration_content: appconfig.ConfigurationContent
            # deployment_strategy: appconfig.DeploymentStrategy
            # environment: appconfig.Environment
            # key: kms.Key
            # validator: appconfig.IValidator
            
            hosted_configuration_options = appconfig.HostedConfigurationOptions(
                content=configuration_content,
            
                # the properties below are optional
                deployment_key=key,
                deployment_strategy=deployment_strategy,
                deploy_to=[environment],
                description="description",
                latest_version_number=123,
                name="name",
                type=appconfig.ConfigurationType.FREEFORM,
                validators=[validator],
                version_label="versionLabel"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c4d8fda2e4860630073eda40d5a32347248e82c24127624ef93e735b071da8f)
            check_type(argname="argument deployment_key", value=deployment_key, expected_type=type_hints["deployment_key"])
            check_type(argname="argument deployment_strategy", value=deployment_strategy, expected_type=type_hints["deployment_strategy"])
            check_type(argname="argument deploy_to", value=deploy_to, expected_type=type_hints["deploy_to"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument validators", value=validators, expected_type=type_hints["validators"])
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument latest_version_number", value=latest_version_number, expected_type=type_hints["latest_version_number"])
            check_type(argname="argument version_label", value=version_label, expected_type=type_hints["version_label"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "content": content,
        }
        if deployment_key is not None:
            self._values["deployment_key"] = deployment_key
        if deployment_strategy is not None:
            self._values["deployment_strategy"] = deployment_strategy
        if deploy_to is not None:
            self._values["deploy_to"] = deploy_to
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name
        if type is not None:
            self._values["type"] = type
        if validators is not None:
            self._values["validators"] = validators
        if latest_version_number is not None:
            self._values["latest_version_number"] = latest_version_number
        if version_label is not None:
            self._values["version_label"] = version_label

    @builtins.property
    def deployment_key(self) -> typing.Optional[_IKey_5f11635f]:
        '''The deployment key of the configuration.

        :default: - None.
        '''
        result = self._values.get("deployment_key")
        return typing.cast(typing.Optional[_IKey_5f11635f], result)

    @builtins.property
    def deployment_strategy(self) -> typing.Optional["IDeploymentStrategy"]:
        '''The deployment strategy for the configuration.

        :default:

        - A deployment strategy with the rollout strategy set to
        RolloutStrategy.CANARY_10_PERCENT_20_MINUTES
        '''
        result = self._values.get("deployment_strategy")
        return typing.cast(typing.Optional["IDeploymentStrategy"], result)

    @builtins.property
    def deploy_to(self) -> typing.Optional[typing.List["IEnvironment"]]:
        '''The list of environments to deploy the configuration to.

        If this parameter is not specified, then there will be no
        deployment created alongside this configuration.

        Deployments can be added later using the ``IEnvironment.addDeployment`` or
        ``IEnvironment.addDeployments`` methods.

        :default: - None.
        '''
        result = self._values.get("deploy_to")
        return typing.cast(typing.Optional[typing.List["IEnvironment"]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the configuration.

        :default: - No description.
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the configuration.

        :default: - A name is generated.
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[ConfigurationType]:
        '''The type of configuration.

        :default: ConfigurationType.FREEFORM
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[ConfigurationType], result)

    @builtins.property
    def validators(self) -> typing.Optional[typing.List["IValidator"]]:
        '''The validators for the configuration.

        :default: - No validators.
        '''
        result = self._values.get("validators")
        return typing.cast(typing.Optional[typing.List["IValidator"]], result)

    @builtins.property
    def content(self) -> ConfigurationContent:
        '''The content of the hosted configuration.'''
        result = self._values.get("content")
        assert result is not None, "Required property 'content' is missing"
        return typing.cast(ConfigurationContent, result)

    @builtins.property
    def latest_version_number(self) -> typing.Optional[jsii.Number]:
        '''The latest version number of the hosted configuration.

        :default: - None.
        '''
        result = self._values.get("latest_version_number")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def version_label(self) -> typing.Optional[builtins.str]:
        '''The version label of the hosted configuration.

        :default: - None.
        '''
        result = self._values.get("version_label")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HostedConfigurationOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appconfig.HostedConfigurationProps",
    jsii_struct_bases=[ConfigurationProps],
    name_mapping={
        "deployment_key": "deploymentKey",
        "deployment_strategy": "deploymentStrategy",
        "deploy_to": "deployTo",
        "description": "description",
        "name": "name",
        "type": "type",
        "validators": "validators",
        "application": "application",
        "content": "content",
        "latest_version_number": "latestVersionNumber",
        "version_label": "versionLabel",
    },
)
class HostedConfigurationProps(ConfigurationProps):
    def __init__(
        self,
        *,
        deployment_key: typing.Optional[_IKey_5f11635f] = None,
        deployment_strategy: typing.Optional["IDeploymentStrategy"] = None,
        deploy_to: typing.Optional[typing.Sequence["IEnvironment"]] = None,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        type: typing.Optional[ConfigurationType] = None,
        validators: typing.Optional[typing.Sequence["IValidator"]] = None,
        application: "IApplication",
        content: ConfigurationContent,
        latest_version_number: typing.Optional[jsii.Number] = None,
        version_label: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for HostedConfiguration.

        :param deployment_key: The deployment key of the configuration. Default: - None.
        :param deployment_strategy: The deployment strategy for the configuration. Default: - A deployment strategy with the rollout strategy set to RolloutStrategy.CANARY_10_PERCENT_20_MINUTES
        :param deploy_to: The list of environments to deploy the configuration to. If this parameter is not specified, then there will be no deployment created alongside this configuration. Deployments can be added later using the ``IEnvironment.addDeployment`` or ``IEnvironment.addDeployments`` methods. Default: - None.
        :param description: The description of the configuration. Default: - No description.
        :param name: The name of the configuration. Default: - A name is generated.
        :param type: The type of configuration. Default: ConfigurationType.FREEFORM
        :param validators: The validators for the configuration. Default: - No validators.
        :param application: The application associated with the configuration.
        :param content: The content of the hosted configuration.
        :param latest_version_number: The latest version number of the hosted configuration. Default: - None.
        :param version_label: The version label of the hosted configuration. Default: - None.

        :exampleMetadata: infused

        Example::

            app = appconfig.Application(self, "MyApp")
            env = appconfig.Environment(self, "MyEnv",
                application=app
            )
            
            appconfig.HostedConfiguration(self, "MyHostedConfig",
                application=app,
                deploy_to=[env],
                content=appconfig.ConfigurationContent.from_inline_text("This is my configuration content.")
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7cba9d5464f3f4cbc208d892995245e5078fc2cc794651c71942035a9b151b2e)
            check_type(argname="argument deployment_key", value=deployment_key, expected_type=type_hints["deployment_key"])
            check_type(argname="argument deployment_strategy", value=deployment_strategy, expected_type=type_hints["deployment_strategy"])
            check_type(argname="argument deploy_to", value=deploy_to, expected_type=type_hints["deploy_to"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument validators", value=validators, expected_type=type_hints["validators"])
            check_type(argname="argument application", value=application, expected_type=type_hints["application"])
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument latest_version_number", value=latest_version_number, expected_type=type_hints["latest_version_number"])
            check_type(argname="argument version_label", value=version_label, expected_type=type_hints["version_label"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application": application,
            "content": content,
        }
        if deployment_key is not None:
            self._values["deployment_key"] = deployment_key
        if deployment_strategy is not None:
            self._values["deployment_strategy"] = deployment_strategy
        if deploy_to is not None:
            self._values["deploy_to"] = deploy_to
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name
        if type is not None:
            self._values["type"] = type
        if validators is not None:
            self._values["validators"] = validators
        if latest_version_number is not None:
            self._values["latest_version_number"] = latest_version_number
        if version_label is not None:
            self._values["version_label"] = version_label

    @builtins.property
    def deployment_key(self) -> typing.Optional[_IKey_5f11635f]:
        '''The deployment key of the configuration.

        :default: - None.
        '''
        result = self._values.get("deployment_key")
        return typing.cast(typing.Optional[_IKey_5f11635f], result)

    @builtins.property
    def deployment_strategy(self) -> typing.Optional["IDeploymentStrategy"]:
        '''The deployment strategy for the configuration.

        :default:

        - A deployment strategy with the rollout strategy set to
        RolloutStrategy.CANARY_10_PERCENT_20_MINUTES
        '''
        result = self._values.get("deployment_strategy")
        return typing.cast(typing.Optional["IDeploymentStrategy"], result)

    @builtins.property
    def deploy_to(self) -> typing.Optional[typing.List["IEnvironment"]]:
        '''The list of environments to deploy the configuration to.

        If this parameter is not specified, then there will be no
        deployment created alongside this configuration.

        Deployments can be added later using the ``IEnvironment.addDeployment`` or
        ``IEnvironment.addDeployments`` methods.

        :default: - None.
        '''
        result = self._values.get("deploy_to")
        return typing.cast(typing.Optional[typing.List["IEnvironment"]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the configuration.

        :default: - No description.
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the configuration.

        :default: - A name is generated.
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[ConfigurationType]:
        '''The type of configuration.

        :default: ConfigurationType.FREEFORM
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[ConfigurationType], result)

    @builtins.property
    def validators(self) -> typing.Optional[typing.List["IValidator"]]:
        '''The validators for the configuration.

        :default: - No validators.
        '''
        result = self._values.get("validators")
        return typing.cast(typing.Optional[typing.List["IValidator"]], result)

    @builtins.property
    def application(self) -> "IApplication":
        '''The application associated with the configuration.'''
        result = self._values.get("application")
        assert result is not None, "Required property 'application' is missing"
        return typing.cast("IApplication", result)

    @builtins.property
    def content(self) -> ConfigurationContent:
        '''The content of the hosted configuration.'''
        result = self._values.get("content")
        assert result is not None, "Required property 'content' is missing"
        return typing.cast(ConfigurationContent, result)

    @builtins.property
    def latest_version_number(self) -> typing.Optional[jsii.Number]:
        '''The latest version number of the hosted configuration.

        :default: - None.
        '''
        result = self._values.get("latest_version_number")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def version_label(self) -> typing.Optional[builtins.str]:
        '''The version label of the hosted configuration.

        :default: - None.
        '''
        result = self._values.get("version_label")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HostedConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.aws_appconfig.IApplication")
class IApplication(_IResource_c80c4260, typing_extensions.Protocol):
    @builtins.property
    @jsii.member(jsii_name="applicationArn")
    def application_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the application.

        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="applicationId")
    def application_id(self) -> builtins.str:
        '''The ID of the application.

        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the application.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the application.'''
        ...

    @jsii.member(jsii_name="addEnvironment")
    def add_environment(
        self,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        environment_name: typing.Optional[builtins.str] = None,
        monitors: typing.Optional[typing.Sequence["Monitor"]] = None,
    ) -> "IEnvironment":
        '''Adds an environment.

        :param id: The name of the environment construct.
        :param description: The description of the environment. Default: - No description.
        :param environment_name: The name of the environment. Default: - A name is generated.
        :param monitors: The monitors for the environment. Default: - No monitors.
        '''
        ...

    @jsii.member(jsii_name="addExistingEnvironment")
    def add_existing_environment(self, environment: "IEnvironment") -> None:
        '''Adds an existing environment.

        :param environment: The environment.
        '''
        ...

    @jsii.member(jsii_name="addExtension")
    def add_extension(self, extension: "IExtension") -> None:
        '''Adds an extension association to the application.

        :param extension: The extension to create an association for.
        '''
        ...

    @jsii.member(jsii_name="addHostedConfiguration")
    def add_hosted_configuration(
        self,
        id: builtins.str,
        *,
        content: ConfigurationContent,
        latest_version_number: typing.Optional[jsii.Number] = None,
        version_label: typing.Optional[builtins.str] = None,
        deployment_key: typing.Optional[_IKey_5f11635f] = None,
        deployment_strategy: typing.Optional["IDeploymentStrategy"] = None,
        deploy_to: typing.Optional[typing.Sequence["IEnvironment"]] = None,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        type: typing.Optional[ConfigurationType] = None,
        validators: typing.Optional[typing.Sequence["IValidator"]] = None,
    ) -> "HostedConfiguration":
        '''Adds a hosted configuration.

        :param id: The name of the hosted configuration construct.
        :param content: The content of the hosted configuration.
        :param latest_version_number: The latest version number of the hosted configuration. Default: - None.
        :param version_label: The version label of the hosted configuration. Default: - None.
        :param deployment_key: The deployment key of the configuration. Default: - None.
        :param deployment_strategy: The deployment strategy for the configuration. Default: - A deployment strategy with the rollout strategy set to RolloutStrategy.CANARY_10_PERCENT_20_MINUTES
        :param deploy_to: The list of environments to deploy the configuration to. If this parameter is not specified, then there will be no deployment created alongside this configuration. Deployments can be added later using the ``IEnvironment.addDeployment`` or ``IEnvironment.addDeployments`` methods. Default: - None.
        :param description: The description of the configuration. Default: - No description.
        :param name: The name of the configuration. Default: - A name is generated.
        :param type: The type of configuration. Default: ConfigurationType.FREEFORM
        :param validators: The validators for the configuration. Default: - No validators.
        '''
        ...

    @jsii.member(jsii_name="addSourcedConfiguration")
    def add_sourced_configuration(
        self,
        id: builtins.str,
        *,
        location: ConfigurationSource,
        retrieval_role: typing.Optional[_IRole_235f5d8e] = None,
        version_number: typing.Optional[builtins.str] = None,
        deployment_key: typing.Optional[_IKey_5f11635f] = None,
        deployment_strategy: typing.Optional["IDeploymentStrategy"] = None,
        deploy_to: typing.Optional[typing.Sequence["IEnvironment"]] = None,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        type: typing.Optional[ConfigurationType] = None,
        validators: typing.Optional[typing.Sequence["IValidator"]] = None,
    ) -> "SourcedConfiguration":
        '''Adds a sourced configuration.

        :param id: The name of the sourced configuration construct.
        :param location: The location where the configuration is stored.
        :param retrieval_role: The IAM role to retrieve the configuration. Default: - A role is generated.
        :param version_number: The version number of the sourced configuration to deploy. If this is not specified, then there will be no deployment. Default: - None.
        :param deployment_key: The deployment key of the configuration. Default: - None.
        :param deployment_strategy: The deployment strategy for the configuration. Default: - A deployment strategy with the rollout strategy set to RolloutStrategy.CANARY_10_PERCENT_20_MINUTES
        :param deploy_to: The list of environments to deploy the configuration to. If this parameter is not specified, then there will be no deployment created alongside this configuration. Deployments can be added later using the ``IEnvironment.addDeployment`` or ``IEnvironment.addDeployments`` methods. Default: - None.
        :param description: The description of the configuration. Default: - No description.
        :param name: The name of the configuration. Default: - A name is generated.
        :param type: The type of configuration. Default: ConfigurationType.FREEFORM
        :param validators: The validators for the configuration. Default: - No validators.
        '''
        ...

    @jsii.member(jsii_name="environments")
    def environments(self) -> typing.List["IEnvironment"]:
        '''Returns the list of associated environments.'''
        ...

    @jsii.member(jsii_name="on")
    def on(
        self,
        action_point: ActionPoint,
        event_destination: "IEventDestination",
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence["Parameter"]] = None,
    ) -> None:
        '''Adds an extension defined by the action point and event destination and also creates an extension association to an application.

        :param action_point: The action point which triggers the event.
        :param event_destination: The event that occurs during the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        ...

    @jsii.member(jsii_name="onDeploymentBaking")
    def on_deployment_baking(
        self,
        event_destination: "IEventDestination",
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence["Parameter"]] = None,
    ) -> None:
        '''Adds an ON_DEPLOYMENT_BAKING extension with the provided event destination and also creates an extension association to an application.

        :param event_destination: The event that occurs during the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        ...

    @jsii.member(jsii_name="onDeploymentComplete")
    def on_deployment_complete(
        self,
        event_destination: "IEventDestination",
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence["Parameter"]] = None,
    ) -> None:
        '''Adds an ON_DEPLOYMENT_COMPLETE extension with the provided event destination and also creates an extension association to an application.

        :param event_destination: The event that occurs during the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        ...

    @jsii.member(jsii_name="onDeploymentRolledBack")
    def on_deployment_rolled_back(
        self,
        event_destination: "IEventDestination",
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence["Parameter"]] = None,
    ) -> None:
        '''Adds an ON_DEPLOYMENT_ROLLED_BACK extension with the provided event destination and also creates an extension association to an application.

        :param event_destination: The event that occurs during the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        ...

    @jsii.member(jsii_name="onDeploymentStart")
    def on_deployment_start(
        self,
        event_destination: "IEventDestination",
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence["Parameter"]] = None,
    ) -> None:
        '''Adds an ON_DEPLOYMENT_START extension with the provided event destination and also creates an extension association to an application.

        :param event_destination: The event that occurs during the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        ...

    @jsii.member(jsii_name="onDeploymentStep")
    def on_deployment_step(
        self,
        event_destination: "IEventDestination",
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence["Parameter"]] = None,
    ) -> None:
        '''Adds an ON_DEPLOYMENT_STEP extension with the provided event destination and also creates an extension association to an application.

        :param event_destination: The event that occurs during the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        ...

    @jsii.member(jsii_name="preCreateHostedConfigurationVersion")
    def pre_create_hosted_configuration_version(
        self,
        event_destination: "IEventDestination",
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence["Parameter"]] = None,
    ) -> None:
        '''Adds a PRE_CREATE_HOSTED_CONFIGURATION_VERSION extension with the provided event destination and also creates an extension association to an application.

        :param event_destination: The event that occurs during the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        ...

    @jsii.member(jsii_name="preStartDeployment")
    def pre_start_deployment(
        self,
        event_destination: "IEventDestination",
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence["Parameter"]] = None,
    ) -> None:
        '''Adds a PRE_START_DEPLOYMENT extension with the provided event destination and also creates an extension association to an application.

        :param event_destination: The event that occurs during the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        ...


class _IApplicationProxy(
    jsii.proxy_for(_IResource_c80c4260), # type: ignore[misc]
):
    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_appconfig.IApplication"

    @builtins.property
    @jsii.member(jsii_name="applicationArn")
    def application_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the application.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "applicationArn"))

    @builtins.property
    @jsii.member(jsii_name="applicationId")
    def application_id(self) -> builtins.str:
        '''The ID of the application.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "applicationId"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the application.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the application.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @jsii.member(jsii_name="addEnvironment")
    def add_environment(
        self,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        environment_name: typing.Optional[builtins.str] = None,
        monitors: typing.Optional[typing.Sequence["Monitor"]] = None,
    ) -> "IEnvironment":
        '''Adds an environment.

        :param id: The name of the environment construct.
        :param description: The description of the environment. Default: - No description.
        :param environment_name: The name of the environment. Default: - A name is generated.
        :param monitors: The monitors for the environment. Default: - No monitors.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb165be70f31f79374053f908981a5e02c37cbdefd4d2123a7e32165fb887042)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = EnvironmentOptions(
            description=description,
            environment_name=environment_name,
            monitors=monitors,
        )

        return typing.cast("IEnvironment", jsii.invoke(self, "addEnvironment", [id, options]))

    @jsii.member(jsii_name="addExistingEnvironment")
    def add_existing_environment(self, environment: "IEnvironment") -> None:
        '''Adds an existing environment.

        :param environment: The environment.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51863d25dd80b6b2aec3914f4049011443f202b08c7c800cd559c58ed15cc0d7)
            check_type(argname="argument environment", value=environment, expected_type=type_hints["environment"])
        return typing.cast(None, jsii.invoke(self, "addExistingEnvironment", [environment]))

    @jsii.member(jsii_name="addExtension")
    def add_extension(self, extension: "IExtension") -> None:
        '''Adds an extension association to the application.

        :param extension: The extension to create an association for.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3dfb6e70c8a97e61af9439d803dd44620f78eac39e160dc612cb32b98725d2a9)
            check_type(argname="argument extension", value=extension, expected_type=type_hints["extension"])
        return typing.cast(None, jsii.invoke(self, "addExtension", [extension]))

    @jsii.member(jsii_name="addHostedConfiguration")
    def add_hosted_configuration(
        self,
        id: builtins.str,
        *,
        content: ConfigurationContent,
        latest_version_number: typing.Optional[jsii.Number] = None,
        version_label: typing.Optional[builtins.str] = None,
        deployment_key: typing.Optional[_IKey_5f11635f] = None,
        deployment_strategy: typing.Optional["IDeploymentStrategy"] = None,
        deploy_to: typing.Optional[typing.Sequence["IEnvironment"]] = None,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        type: typing.Optional[ConfigurationType] = None,
        validators: typing.Optional[typing.Sequence["IValidator"]] = None,
    ) -> "HostedConfiguration":
        '''Adds a hosted configuration.

        :param id: The name of the hosted configuration construct.
        :param content: The content of the hosted configuration.
        :param latest_version_number: The latest version number of the hosted configuration. Default: - None.
        :param version_label: The version label of the hosted configuration. Default: - None.
        :param deployment_key: The deployment key of the configuration. Default: - None.
        :param deployment_strategy: The deployment strategy for the configuration. Default: - A deployment strategy with the rollout strategy set to RolloutStrategy.CANARY_10_PERCENT_20_MINUTES
        :param deploy_to: The list of environments to deploy the configuration to. If this parameter is not specified, then there will be no deployment created alongside this configuration. Deployments can be added later using the ``IEnvironment.addDeployment`` or ``IEnvironment.addDeployments`` methods. Default: - None.
        :param description: The description of the configuration. Default: - No description.
        :param name: The name of the configuration. Default: - A name is generated.
        :param type: The type of configuration. Default: ConfigurationType.FREEFORM
        :param validators: The validators for the configuration. Default: - No validators.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3bd9df804b6975de3426c197a45965f129649a986f5cd9a03f0a4ee6f3cad84d)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = HostedConfigurationOptions(
            content=content,
            latest_version_number=latest_version_number,
            version_label=version_label,
            deployment_key=deployment_key,
            deployment_strategy=deployment_strategy,
            deploy_to=deploy_to,
            description=description,
            name=name,
            type=type,
            validators=validators,
        )

        return typing.cast("HostedConfiguration", jsii.invoke(self, "addHostedConfiguration", [id, options]))

    @jsii.member(jsii_name="addSourcedConfiguration")
    def add_sourced_configuration(
        self,
        id: builtins.str,
        *,
        location: ConfigurationSource,
        retrieval_role: typing.Optional[_IRole_235f5d8e] = None,
        version_number: typing.Optional[builtins.str] = None,
        deployment_key: typing.Optional[_IKey_5f11635f] = None,
        deployment_strategy: typing.Optional["IDeploymentStrategy"] = None,
        deploy_to: typing.Optional[typing.Sequence["IEnvironment"]] = None,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        type: typing.Optional[ConfigurationType] = None,
        validators: typing.Optional[typing.Sequence["IValidator"]] = None,
    ) -> "SourcedConfiguration":
        '''Adds a sourced configuration.

        :param id: The name of the sourced configuration construct.
        :param location: The location where the configuration is stored.
        :param retrieval_role: The IAM role to retrieve the configuration. Default: - A role is generated.
        :param version_number: The version number of the sourced configuration to deploy. If this is not specified, then there will be no deployment. Default: - None.
        :param deployment_key: The deployment key of the configuration. Default: - None.
        :param deployment_strategy: The deployment strategy for the configuration. Default: - A deployment strategy with the rollout strategy set to RolloutStrategy.CANARY_10_PERCENT_20_MINUTES
        :param deploy_to: The list of environments to deploy the configuration to. If this parameter is not specified, then there will be no deployment created alongside this configuration. Deployments can be added later using the ``IEnvironment.addDeployment`` or ``IEnvironment.addDeployments`` methods. Default: - None.
        :param description: The description of the configuration. Default: - No description.
        :param name: The name of the configuration. Default: - A name is generated.
        :param type: The type of configuration. Default: ConfigurationType.FREEFORM
        :param validators: The validators for the configuration. Default: - No validators.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__652068ebd01467de1bc3159a4c8fef165c1053fe6662fcbb6e0b8cb9fec285ff)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = SourcedConfigurationOptions(
            location=location,
            retrieval_role=retrieval_role,
            version_number=version_number,
            deployment_key=deployment_key,
            deployment_strategy=deployment_strategy,
            deploy_to=deploy_to,
            description=description,
            name=name,
            type=type,
            validators=validators,
        )

        return typing.cast("SourcedConfiguration", jsii.invoke(self, "addSourcedConfiguration", [id, options]))

    @jsii.member(jsii_name="environments")
    def environments(self) -> typing.List["IEnvironment"]:
        '''Returns the list of associated environments.'''
        return typing.cast(typing.List["IEnvironment"], jsii.invoke(self, "environments", []))

    @jsii.member(jsii_name="on")
    def on(
        self,
        action_point: ActionPoint,
        event_destination: "IEventDestination",
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence["Parameter"]] = None,
    ) -> None:
        '''Adds an extension defined by the action point and event destination and also creates an extension association to an application.

        :param action_point: The action point which triggers the event.
        :param event_destination: The event that occurs during the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d755f676cf64362ca69375955a2d00058210806c720c3245a961824cd5407ab)
            check_type(argname="argument action_point", value=action_point, expected_type=type_hints["action_point"])
            check_type(argname="argument event_destination", value=event_destination, expected_type=type_hints["event_destination"])
        options = ExtensionOptions(
            description=description,
            extension_name=extension_name,
            latest_version_number=latest_version_number,
            parameters=parameters,
        )

        return typing.cast(None, jsii.invoke(self, "on", [action_point, event_destination, options]))

    @jsii.member(jsii_name="onDeploymentBaking")
    def on_deployment_baking(
        self,
        event_destination: "IEventDestination",
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence["Parameter"]] = None,
    ) -> None:
        '''Adds an ON_DEPLOYMENT_BAKING extension with the provided event destination and also creates an extension association to an application.

        :param event_destination: The event that occurs during the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be554a7ff5cf6482e867ec00580dd9f3ee89ad10ddb4c5ec39a08250191f625c)
            check_type(argname="argument event_destination", value=event_destination, expected_type=type_hints["event_destination"])
        options = ExtensionOptions(
            description=description,
            extension_name=extension_name,
            latest_version_number=latest_version_number,
            parameters=parameters,
        )

        return typing.cast(None, jsii.invoke(self, "onDeploymentBaking", [event_destination, options]))

    @jsii.member(jsii_name="onDeploymentComplete")
    def on_deployment_complete(
        self,
        event_destination: "IEventDestination",
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence["Parameter"]] = None,
    ) -> None:
        '''Adds an ON_DEPLOYMENT_COMPLETE extension with the provided event destination and also creates an extension association to an application.

        :param event_destination: The event that occurs during the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78526e82674bf1c4a84dd0a0c976f78629d8538ec16b9c7e91aba8ef23a2ebf7)
            check_type(argname="argument event_destination", value=event_destination, expected_type=type_hints["event_destination"])
        options = ExtensionOptions(
            description=description,
            extension_name=extension_name,
            latest_version_number=latest_version_number,
            parameters=parameters,
        )

        return typing.cast(None, jsii.invoke(self, "onDeploymentComplete", [event_destination, options]))

    @jsii.member(jsii_name="onDeploymentRolledBack")
    def on_deployment_rolled_back(
        self,
        event_destination: "IEventDestination",
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence["Parameter"]] = None,
    ) -> None:
        '''Adds an ON_DEPLOYMENT_ROLLED_BACK extension with the provided event destination and also creates an extension association to an application.

        :param event_destination: The event that occurs during the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__034f622b91f25952ad7c4bab6456b57864c9e3bc626ae6eea947fe4d08915afd)
            check_type(argname="argument event_destination", value=event_destination, expected_type=type_hints["event_destination"])
        options = ExtensionOptions(
            description=description,
            extension_name=extension_name,
            latest_version_number=latest_version_number,
            parameters=parameters,
        )

        return typing.cast(None, jsii.invoke(self, "onDeploymentRolledBack", [event_destination, options]))

    @jsii.member(jsii_name="onDeploymentStart")
    def on_deployment_start(
        self,
        event_destination: "IEventDestination",
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence["Parameter"]] = None,
    ) -> None:
        '''Adds an ON_DEPLOYMENT_START extension with the provided event destination and also creates an extension association to an application.

        :param event_destination: The event that occurs during the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__016aa77ef2c908d64b76cf21200f5958ff7634df1b3d77a188a8e09c7a70bd56)
            check_type(argname="argument event_destination", value=event_destination, expected_type=type_hints["event_destination"])
        options = ExtensionOptions(
            description=description,
            extension_name=extension_name,
            latest_version_number=latest_version_number,
            parameters=parameters,
        )

        return typing.cast(None, jsii.invoke(self, "onDeploymentStart", [event_destination, options]))

    @jsii.member(jsii_name="onDeploymentStep")
    def on_deployment_step(
        self,
        event_destination: "IEventDestination",
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence["Parameter"]] = None,
    ) -> None:
        '''Adds an ON_DEPLOYMENT_STEP extension with the provided event destination and also creates an extension association to an application.

        :param event_destination: The event that occurs during the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71b1982dcc7245c64b03552696f23c45795d967bafdd9dc9ab92802003c78d22)
            check_type(argname="argument event_destination", value=event_destination, expected_type=type_hints["event_destination"])
        options = ExtensionOptions(
            description=description,
            extension_name=extension_name,
            latest_version_number=latest_version_number,
            parameters=parameters,
        )

        return typing.cast(None, jsii.invoke(self, "onDeploymentStep", [event_destination, options]))

    @jsii.member(jsii_name="preCreateHostedConfigurationVersion")
    def pre_create_hosted_configuration_version(
        self,
        event_destination: "IEventDestination",
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence["Parameter"]] = None,
    ) -> None:
        '''Adds a PRE_CREATE_HOSTED_CONFIGURATION_VERSION extension with the provided event destination and also creates an extension association to an application.

        :param event_destination: The event that occurs during the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58ebf4627ce889183b1c4f07bd2d0c79f4c30add9ad5c1e7916ab5d0565c0e71)
            check_type(argname="argument event_destination", value=event_destination, expected_type=type_hints["event_destination"])
        options = ExtensionOptions(
            description=description,
            extension_name=extension_name,
            latest_version_number=latest_version_number,
            parameters=parameters,
        )

        return typing.cast(None, jsii.invoke(self, "preCreateHostedConfigurationVersion", [event_destination, options]))

    @jsii.member(jsii_name="preStartDeployment")
    def pre_start_deployment(
        self,
        event_destination: "IEventDestination",
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence["Parameter"]] = None,
    ) -> None:
        '''Adds a PRE_START_DEPLOYMENT extension with the provided event destination and also creates an extension association to an application.

        :param event_destination: The event that occurs during the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e94c708c7603af848bf6e13c31c0fc2a81ad1aa833b38ab455b5a4db91d0835)
            check_type(argname="argument event_destination", value=event_destination, expected_type=type_hints["event_destination"])
        options = ExtensionOptions(
            description=description,
            extension_name=extension_name,
            latest_version_number=latest_version_number,
            parameters=parameters,
        )

        return typing.cast(None, jsii.invoke(self, "preStartDeployment", [event_destination, options]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IApplication).__jsii_proxy_class__ = lambda : _IApplicationProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_appconfig.IConfiguration")
class IConfiguration(_constructs_77d1e7e8.IConstruct, typing_extensions.Protocol):
    @builtins.property
    @jsii.member(jsii_name="application")
    def application(self) -> IApplication:
        '''The application associated with the configuration.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="configurationProfileId")
    def configuration_profile_id(self) -> builtins.str:
        '''The ID of the configuration profile.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="deploymentKey")
    def deployment_key(self) -> typing.Optional[_IKey_5f11635f]:
        '''The deployment key for the configuration.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="deploymentStrategy")
    def deployment_strategy(self) -> typing.Optional["IDeploymentStrategy"]:
        '''The deployment strategy for the configuration.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="deployTo")
    def deploy_to(self) -> typing.Optional[typing.List["IEnvironment"]]:
        '''The environments to deploy to.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the configuration.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the configuration.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> typing.Optional[ConfigurationType]:
        '''The configuration type.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="validators")
    def validators(self) -> typing.Optional[typing.List["IValidator"]]:
        '''The validators for the configuration.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="versionNumber")
    def version_number(self) -> typing.Optional[builtins.str]:
        '''The configuration version number.'''
        ...


class _IConfigurationProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
):
    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_appconfig.IConfiguration"

    @builtins.property
    @jsii.member(jsii_name="application")
    def application(self) -> IApplication:
        '''The application associated with the configuration.'''
        return typing.cast(IApplication, jsii.get(self, "application"))

    @builtins.property
    @jsii.member(jsii_name="configurationProfileId")
    def configuration_profile_id(self) -> builtins.str:
        '''The ID of the configuration profile.'''
        return typing.cast(builtins.str, jsii.get(self, "configurationProfileId"))

    @builtins.property
    @jsii.member(jsii_name="deploymentKey")
    def deployment_key(self) -> typing.Optional[_IKey_5f11635f]:
        '''The deployment key for the configuration.'''
        return typing.cast(typing.Optional[_IKey_5f11635f], jsii.get(self, "deploymentKey"))

    @builtins.property
    @jsii.member(jsii_name="deploymentStrategy")
    def deployment_strategy(self) -> typing.Optional["IDeploymentStrategy"]:
        '''The deployment strategy for the configuration.'''
        return typing.cast(typing.Optional["IDeploymentStrategy"], jsii.get(self, "deploymentStrategy"))

    @builtins.property
    @jsii.member(jsii_name="deployTo")
    def deploy_to(self) -> typing.Optional[typing.List["IEnvironment"]]:
        '''The environments to deploy to.'''
        return typing.cast(typing.Optional[typing.List["IEnvironment"]], jsii.get(self, "deployTo"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the configuration.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the configuration.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> typing.Optional[ConfigurationType]:
        '''The configuration type.'''
        return typing.cast(typing.Optional[ConfigurationType], jsii.get(self, "type"))

    @builtins.property
    @jsii.member(jsii_name="validators")
    def validators(self) -> typing.Optional[typing.List["IValidator"]]:
        '''The validators for the configuration.'''
        return typing.cast(typing.Optional[typing.List["IValidator"]], jsii.get(self, "validators"))

    @builtins.property
    @jsii.member(jsii_name="versionNumber")
    def version_number(self) -> typing.Optional[builtins.str]:
        '''The configuration version number.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionNumber"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IConfiguration).__jsii_proxy_class__ = lambda : _IConfigurationProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_appconfig.IDeploymentStrategy")
class IDeploymentStrategy(_IResource_c80c4260, typing_extensions.Protocol):
    @builtins.property
    @jsii.member(jsii_name="deploymentStrategyArn")
    def deployment_strategy_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the deployment strategy.

        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="deploymentStrategyId")
    def deployment_strategy_id(self) -> builtins.str:
        '''The ID of the deployment strategy.

        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="deploymentDurationInMinutes")
    def deployment_duration_in_minutes(self) -> typing.Optional[jsii.Number]:
        '''The deployment duration in minutes.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the deployment strategy.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="finalBakeTimeInMinutes")
    def final_bake_time_in_minutes(self) -> typing.Optional[jsii.Number]:
        '''The final bake time in minutes.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="growthFactor")
    def growth_factor(self) -> typing.Optional[jsii.Number]:
        '''The growth factor of the deployment strategy.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="growthType")
    def growth_type(self) -> typing.Optional[GrowthType]:
        '''The growth type of the deployment strategy.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the deployment strategy.'''
        ...


class _IDeploymentStrategyProxy(
    jsii.proxy_for(_IResource_c80c4260), # type: ignore[misc]
):
    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_appconfig.IDeploymentStrategy"

    @builtins.property
    @jsii.member(jsii_name="deploymentStrategyArn")
    def deployment_strategy_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the deployment strategy.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "deploymentStrategyArn"))

    @builtins.property
    @jsii.member(jsii_name="deploymentStrategyId")
    def deployment_strategy_id(self) -> builtins.str:
        '''The ID of the deployment strategy.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "deploymentStrategyId"))

    @builtins.property
    @jsii.member(jsii_name="deploymentDurationInMinutes")
    def deployment_duration_in_minutes(self) -> typing.Optional[jsii.Number]:
        '''The deployment duration in minutes.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "deploymentDurationInMinutes"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the deployment strategy.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @builtins.property
    @jsii.member(jsii_name="finalBakeTimeInMinutes")
    def final_bake_time_in_minutes(self) -> typing.Optional[jsii.Number]:
        '''The final bake time in minutes.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "finalBakeTimeInMinutes"))

    @builtins.property
    @jsii.member(jsii_name="growthFactor")
    def growth_factor(self) -> typing.Optional[jsii.Number]:
        '''The growth factor of the deployment strategy.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "growthFactor"))

    @builtins.property
    @jsii.member(jsii_name="growthType")
    def growth_type(self) -> typing.Optional[GrowthType]:
        '''The growth type of the deployment strategy.'''
        return typing.cast(typing.Optional[GrowthType], jsii.get(self, "growthType"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the deployment strategy.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDeploymentStrategy).__jsii_proxy_class__ = lambda : _IDeploymentStrategyProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_appconfig.IEnvironment")
class IEnvironment(_IResource_c80c4260, typing_extensions.Protocol):
    @builtins.property
    @jsii.member(jsii_name="applicationId")
    def application_id(self) -> builtins.str:
        '''The ID of the application associated to the environment.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="environmentArn")
    def environment_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the environment.

        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="environmentId")
    def environment_id(self) -> builtins.str:
        '''The ID of the environment.

        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="application")
    def application(self) -> typing.Optional[IApplication]:
        '''The application associated with the environment.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the environment.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="monitors")
    def monitors(self) -> typing.Optional[typing.List["Monitor"]]:
        '''The monitors for the environment.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the environment.'''
        ...

    @jsii.member(jsii_name="addDeployment")
    def add_deployment(self, configuration: IConfiguration) -> None:
        '''Creates a deployment of the supplied configuration to this environment.

        Note that you can only deploy one configuration at a time to an environment.
        However, you can deploy one configuration each to different environments at the same time.
        If more than one deployment is requested for this environment, they will occur in the same order they were provided.

        :param configuration: The configuration that will be deployed to this environment.
        '''
        ...

    @jsii.member(jsii_name="addDeployments")
    def add_deployments(self, *configurations: IConfiguration) -> None:
        '''Creates a deployment for each of the supplied configurations to this environment.

        These configurations will be deployed in the same order as the input array.

        :param configurations: The configurations that will be deployed to this environment.
        '''
        ...

    @jsii.member(jsii_name="addExtension")
    def add_extension(self, extension: "IExtension") -> None:
        '''Adds an extension association to the environment.

        :param extension: The extension to create an association for.
        '''
        ...

    @jsii.member(jsii_name="grant")
    def grant(
        self,
        grantee: _IGrantable_71c4f5de,
        *actions: builtins.str,
    ) -> _Grant_a7ae64f8:
        '''Adds an IAM policy statement associated with this environment to an IAM principal's policy.

        :param grantee: the principal (no-op if undefined).
        :param actions: the set of actions to allow (i.e., 'appconfig:GetLatestConfiguration', 'appconfig:StartConfigurationSession', etc.).
        '''
        ...

    @jsii.member(jsii_name="grantReadConfig")
    def grant_read_config(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Permits an IAM principal to perform read operations on this environment's configurations.

        Actions: GetLatestConfiguration, StartConfigurationSession.

        :param grantee: Principal to grant read rights to.
        '''
        ...

    @jsii.member(jsii_name="on")
    def on(
        self,
        action_point: ActionPoint,
        event_destination: "IEventDestination",
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence["Parameter"]] = None,
    ) -> None:
        '''Adds an extension defined by the action point and event destination and also creates an extension association to the environment.

        :param action_point: The action point which triggers the event.
        :param event_destination: The event that occurs during the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        ...

    @jsii.member(jsii_name="onDeploymentBaking")
    def on_deployment_baking(
        self,
        event_destination: "IEventDestination",
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence["Parameter"]] = None,
    ) -> None:
        '''Adds an ON_DEPLOYMENT_BAKING extension with the provided event destination and also creates an extension association to the environment.

        :param event_destination: The event that occurs during the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        ...

    @jsii.member(jsii_name="onDeploymentComplete")
    def on_deployment_complete(
        self,
        event_destination: "IEventDestination",
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence["Parameter"]] = None,
    ) -> None:
        '''Adds an ON_DEPLOYMENT_COMPLETE extension with the provided event destination and also creates an extension association to the environment.

        :param event_destination: The event that occurs during the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        ...

    @jsii.member(jsii_name="onDeploymentRolledBack")
    def on_deployment_rolled_back(
        self,
        event_destination: "IEventDestination",
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence["Parameter"]] = None,
    ) -> None:
        '''Adds an ON_DEPLOYMENT_ROLLED_BACK extension with the provided event destination and also creates an extension association to the environment.

        :param event_destination: The event that occurs during the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        ...

    @jsii.member(jsii_name="onDeploymentStart")
    def on_deployment_start(
        self,
        event_destination: "IEventDestination",
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence["Parameter"]] = None,
    ) -> None:
        '''Adds an ON_DEPLOYMENT_START extension with the provided event destination and also creates an extension association to the environment.

        :param event_destination: The event that occurs during the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        ...

    @jsii.member(jsii_name="onDeploymentStep")
    def on_deployment_step(
        self,
        event_destination: "IEventDestination",
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence["Parameter"]] = None,
    ) -> None:
        '''Adds an ON_DEPLOYMENT_STEP extension with the provided event destination and also creates an extension association to the environment.

        :param event_destination: The event that occurs during the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        ...

    @jsii.member(jsii_name="preCreateHostedConfigurationVersion")
    def pre_create_hosted_configuration_version(
        self,
        event_destination: "IEventDestination",
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence["Parameter"]] = None,
    ) -> None:
        '''Adds a PRE_CREATE_HOSTED_CONFIGURATION_VERSION extension with the provided event destination and also creates an extension association to the environment.

        :param event_destination: The event that occurs during the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        ...

    @jsii.member(jsii_name="preStartDeployment")
    def pre_start_deployment(
        self,
        event_destination: "IEventDestination",
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence["Parameter"]] = None,
    ) -> None:
        '''Adds a PRE_START_DEPLOYMENT extension with the provided event destination and also creates an extension association to the environment.

        :param event_destination: The event that occurs during the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        ...


class _IEnvironmentProxy(
    jsii.proxy_for(_IResource_c80c4260), # type: ignore[misc]
):
    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_appconfig.IEnvironment"

    @builtins.property
    @jsii.member(jsii_name="applicationId")
    def application_id(self) -> builtins.str:
        '''The ID of the application associated to the environment.'''
        return typing.cast(builtins.str, jsii.get(self, "applicationId"))

    @builtins.property
    @jsii.member(jsii_name="environmentArn")
    def environment_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the environment.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "environmentArn"))

    @builtins.property
    @jsii.member(jsii_name="environmentId")
    def environment_id(self) -> builtins.str:
        '''The ID of the environment.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "environmentId"))

    @builtins.property
    @jsii.member(jsii_name="application")
    def application(self) -> typing.Optional[IApplication]:
        '''The application associated with the environment.'''
        return typing.cast(typing.Optional[IApplication], jsii.get(self, "application"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the environment.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @builtins.property
    @jsii.member(jsii_name="monitors")
    def monitors(self) -> typing.Optional[typing.List["Monitor"]]:
        '''The monitors for the environment.'''
        return typing.cast(typing.Optional[typing.List["Monitor"]], jsii.get(self, "monitors"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the environment.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @jsii.member(jsii_name="addDeployment")
    def add_deployment(self, configuration: IConfiguration) -> None:
        '''Creates a deployment of the supplied configuration to this environment.

        Note that you can only deploy one configuration at a time to an environment.
        However, you can deploy one configuration each to different environments at the same time.
        If more than one deployment is requested for this environment, they will occur in the same order they were provided.

        :param configuration: The configuration that will be deployed to this environment.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f39f9fc38c2348c1cbb526adb681012a66d9e97575dc37ba0af87ab3bc3eddc)
            check_type(argname="argument configuration", value=configuration, expected_type=type_hints["configuration"])
        return typing.cast(None, jsii.invoke(self, "addDeployment", [configuration]))

    @jsii.member(jsii_name="addDeployments")
    def add_deployments(self, *configurations: IConfiguration) -> None:
        '''Creates a deployment for each of the supplied configurations to this environment.

        These configurations will be deployed in the same order as the input array.

        :param configurations: The configurations that will be deployed to this environment.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44b48a1bae27d9166bf28c62529963c2221d313260dbc1e9f5239536a54010d5)
            check_type(argname="argument configurations", value=configurations, expected_type=typing.Tuple[type_hints["configurations"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "addDeployments", [*configurations]))

    @jsii.member(jsii_name="addExtension")
    def add_extension(self, extension: "IExtension") -> None:
        '''Adds an extension association to the environment.

        :param extension: The extension to create an association for.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21f3fd9d8706d2da33872e0f177690ef7904e1a5bffb8f09838105674dab79cf)
            check_type(argname="argument extension", value=extension, expected_type=type_hints["extension"])
        return typing.cast(None, jsii.invoke(self, "addExtension", [extension]))

    @jsii.member(jsii_name="grant")
    def grant(
        self,
        grantee: _IGrantable_71c4f5de,
        *actions: builtins.str,
    ) -> _Grant_a7ae64f8:
        '''Adds an IAM policy statement associated with this environment to an IAM principal's policy.

        :param grantee: the principal (no-op if undefined).
        :param actions: the set of actions to allow (i.e., 'appconfig:GetLatestConfiguration', 'appconfig:StartConfigurationSession', etc.).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f223f0108afb5683d5788fc1fb9f93cbd4c76cb5698d6aae016951683e8148ee)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
            check_type(argname="argument actions", value=actions, expected_type=typing.Tuple[type_hints["actions"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grant", [grantee, *actions]))

    @jsii.member(jsii_name="grantReadConfig")
    def grant_read_config(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Permits an IAM principal to perform read operations on this environment's configurations.

        Actions: GetLatestConfiguration, StartConfigurationSession.

        :param grantee: Principal to grant read rights to.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9980f2056195344785f7b36a405e0d1227ad963e409c454217caf9b0e4ab2c9d)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantReadConfig", [grantee]))

    @jsii.member(jsii_name="on")
    def on(
        self,
        action_point: ActionPoint,
        event_destination: "IEventDestination",
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence["Parameter"]] = None,
    ) -> None:
        '''Adds an extension defined by the action point and event destination and also creates an extension association to the environment.

        :param action_point: The action point which triggers the event.
        :param event_destination: The event that occurs during the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a99dab2b60d71d853252dc1cd4c58e0db20f0d3344869d8b3c0078d823053f47)
            check_type(argname="argument action_point", value=action_point, expected_type=type_hints["action_point"])
            check_type(argname="argument event_destination", value=event_destination, expected_type=type_hints["event_destination"])
        options = ExtensionOptions(
            description=description,
            extension_name=extension_name,
            latest_version_number=latest_version_number,
            parameters=parameters,
        )

        return typing.cast(None, jsii.invoke(self, "on", [action_point, event_destination, options]))

    @jsii.member(jsii_name="onDeploymentBaking")
    def on_deployment_baking(
        self,
        event_destination: "IEventDestination",
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence["Parameter"]] = None,
    ) -> None:
        '''Adds an ON_DEPLOYMENT_BAKING extension with the provided event destination and also creates an extension association to the environment.

        :param event_destination: The event that occurs during the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bef62040c375bd2337f0d3e61b60a7c152f6460a98daef5742016059a14271a8)
            check_type(argname="argument event_destination", value=event_destination, expected_type=type_hints["event_destination"])
        options = ExtensionOptions(
            description=description,
            extension_name=extension_name,
            latest_version_number=latest_version_number,
            parameters=parameters,
        )

        return typing.cast(None, jsii.invoke(self, "onDeploymentBaking", [event_destination, options]))

    @jsii.member(jsii_name="onDeploymentComplete")
    def on_deployment_complete(
        self,
        event_destination: "IEventDestination",
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence["Parameter"]] = None,
    ) -> None:
        '''Adds an ON_DEPLOYMENT_COMPLETE extension with the provided event destination and also creates an extension association to the environment.

        :param event_destination: The event that occurs during the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d011fee22ec2026b2d30ec4752fd2b51dd4643c49774a9c6e595752709d9ce26)
            check_type(argname="argument event_destination", value=event_destination, expected_type=type_hints["event_destination"])
        options = ExtensionOptions(
            description=description,
            extension_name=extension_name,
            latest_version_number=latest_version_number,
            parameters=parameters,
        )

        return typing.cast(None, jsii.invoke(self, "onDeploymentComplete", [event_destination, options]))

    @jsii.member(jsii_name="onDeploymentRolledBack")
    def on_deployment_rolled_back(
        self,
        event_destination: "IEventDestination",
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence["Parameter"]] = None,
    ) -> None:
        '''Adds an ON_DEPLOYMENT_ROLLED_BACK extension with the provided event destination and also creates an extension association to the environment.

        :param event_destination: The event that occurs during the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80820f672394fd7f1353941a67dfc3c0f6661b448abcd5dbefa5d17e6beee7cf)
            check_type(argname="argument event_destination", value=event_destination, expected_type=type_hints["event_destination"])
        options = ExtensionOptions(
            description=description,
            extension_name=extension_name,
            latest_version_number=latest_version_number,
            parameters=parameters,
        )

        return typing.cast(None, jsii.invoke(self, "onDeploymentRolledBack", [event_destination, options]))

    @jsii.member(jsii_name="onDeploymentStart")
    def on_deployment_start(
        self,
        event_destination: "IEventDestination",
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence["Parameter"]] = None,
    ) -> None:
        '''Adds an ON_DEPLOYMENT_START extension with the provided event destination and also creates an extension association to the environment.

        :param event_destination: The event that occurs during the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e495273d9b8cd07ab5fafbb39bb5f77a539112c335e202da5fc32fdf8a9e350a)
            check_type(argname="argument event_destination", value=event_destination, expected_type=type_hints["event_destination"])
        options = ExtensionOptions(
            description=description,
            extension_name=extension_name,
            latest_version_number=latest_version_number,
            parameters=parameters,
        )

        return typing.cast(None, jsii.invoke(self, "onDeploymentStart", [event_destination, options]))

    @jsii.member(jsii_name="onDeploymentStep")
    def on_deployment_step(
        self,
        event_destination: "IEventDestination",
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence["Parameter"]] = None,
    ) -> None:
        '''Adds an ON_DEPLOYMENT_STEP extension with the provided event destination and also creates an extension association to the environment.

        :param event_destination: The event that occurs during the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__934644fa645d264ebfb46e1fbc7a539792a455110f9ccc0c772308cb0cd2b3b2)
            check_type(argname="argument event_destination", value=event_destination, expected_type=type_hints["event_destination"])
        options = ExtensionOptions(
            description=description,
            extension_name=extension_name,
            latest_version_number=latest_version_number,
            parameters=parameters,
        )

        return typing.cast(None, jsii.invoke(self, "onDeploymentStep", [event_destination, options]))

    @jsii.member(jsii_name="preCreateHostedConfigurationVersion")
    def pre_create_hosted_configuration_version(
        self,
        event_destination: "IEventDestination",
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence["Parameter"]] = None,
    ) -> None:
        '''Adds a PRE_CREATE_HOSTED_CONFIGURATION_VERSION extension with the provided event destination and also creates an extension association to the environment.

        :param event_destination: The event that occurs during the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8730b489063898186752e5bbb505fc429ca40b3257aadac613dd158db05049ae)
            check_type(argname="argument event_destination", value=event_destination, expected_type=type_hints["event_destination"])
        options = ExtensionOptions(
            description=description,
            extension_name=extension_name,
            latest_version_number=latest_version_number,
            parameters=parameters,
        )

        return typing.cast(None, jsii.invoke(self, "preCreateHostedConfigurationVersion", [event_destination, options]))

    @jsii.member(jsii_name="preStartDeployment")
    def pre_start_deployment(
        self,
        event_destination: "IEventDestination",
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence["Parameter"]] = None,
    ) -> None:
        '''Adds a PRE_START_DEPLOYMENT extension with the provided event destination and also creates an extension association to the environment.

        :param event_destination: The event that occurs during the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11a5b9a15937937180da1889814f9b51e695b3dda7f18fad38f06693f0bf3bcd)
            check_type(argname="argument event_destination", value=event_destination, expected_type=type_hints["event_destination"])
        options = ExtensionOptions(
            description=description,
            extension_name=extension_name,
            latest_version_number=latest_version_number,
            parameters=parameters,
        )

        return typing.cast(None, jsii.invoke(self, "preStartDeployment", [event_destination, options]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEnvironment).__jsii_proxy_class__ = lambda : _IEnvironmentProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_appconfig.IEventDestination")
class IEventDestination(typing_extensions.Protocol):
    '''Implemented by allowed extension event destinations.'''

    @builtins.property
    @jsii.member(jsii_name="extensionUri")
    def extension_uri(self) -> builtins.str:
        '''The URI of the extension event destination.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> "SourceType":
        '''The type of the extension event destination.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="policyDocument")
    def policy_document(self) -> typing.Optional[_PolicyDocument_3ac34393]:
        '''The IAM policy document to invoke the event destination.'''
        ...


class _IEventDestinationProxy:
    '''Implemented by allowed extension event destinations.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_appconfig.IEventDestination"

    @builtins.property
    @jsii.member(jsii_name="extensionUri")
    def extension_uri(self) -> builtins.str:
        '''The URI of the extension event destination.'''
        return typing.cast(builtins.str, jsii.get(self, "extensionUri"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> "SourceType":
        '''The type of the extension event destination.'''
        return typing.cast("SourceType", jsii.get(self, "type"))

    @builtins.property
    @jsii.member(jsii_name="policyDocument")
    def policy_document(self) -> typing.Optional[_PolicyDocument_3ac34393]:
        '''The IAM policy document to invoke the event destination.'''
        return typing.cast(typing.Optional[_PolicyDocument_3ac34393], jsii.get(self, "policyDocument"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEventDestination).__jsii_proxy_class__ = lambda : _IEventDestinationProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_appconfig.IExtensible")
class IExtensible(typing_extensions.Protocol):
    '''Defines the extensible base implementation for extension association resources.'''

    @jsii.member(jsii_name="addExtension")
    def add_extension(self, extension: "IExtension") -> None:
        '''Adds an extension association to the derived resource.

        :param extension: The extension to create an association for.
        '''
        ...

    @jsii.member(jsii_name="on")
    def on(
        self,
        action_point: ActionPoint,
        event_destination: IEventDestination,
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence["Parameter"]] = None,
    ) -> None:
        '''Adds an extension defined by the action point and event destination and also creates an extension association to the derived resource.

        :param action_point: The action point which triggers the event.
        :param event_destination: The event that occurs during the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        ...

    @jsii.member(jsii_name="onDeploymentBaking")
    def on_deployment_baking(
        self,
        event_destination: IEventDestination,
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence["Parameter"]] = None,
    ) -> None:
        '''Adds an ON_DEPLOYMENT_BAKING extension with the provided event destination and also creates an extension association to the derived resource.

        :param event_destination: The event that occurs during the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        ...

    @jsii.member(jsii_name="onDeploymentComplete")
    def on_deployment_complete(
        self,
        event_destination: IEventDestination,
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence["Parameter"]] = None,
    ) -> None:
        '''Adds an ON_DEPLOYMENT_COMPLETE extension with the provided event destination and also creates an extension association to the derived resource.

        :param event_destination: The event that occurs during the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        ...

    @jsii.member(jsii_name="onDeploymentRolledBack")
    def on_deployment_rolled_back(
        self,
        event_destination: IEventDestination,
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence["Parameter"]] = None,
    ) -> None:
        '''Adds an ON_DEPLOYMENT_ROLLED_BACK extension with the provided event destination and also creates an extension association to the derived resource.

        :param event_destination: The event that occurs during the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        ...

    @jsii.member(jsii_name="onDeploymentStart")
    def on_deployment_start(
        self,
        event_destination: IEventDestination,
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence["Parameter"]] = None,
    ) -> None:
        '''Adds an ON_DEPLOYMENT_START extension with the provided event destination and also creates an extension association to the derived resource.

        :param event_destination: The event that occurs during the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        ...

    @jsii.member(jsii_name="onDeploymentStep")
    def on_deployment_step(
        self,
        event_destination: IEventDestination,
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence["Parameter"]] = None,
    ) -> None:
        '''Adds an ON_DEPLOYMENT_STEP extension with the provided event destination and also creates an extension association to the derived resource.

        :param event_destination: The event that occurs during the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        ...

    @jsii.member(jsii_name="preCreateHostedConfigurationVersion")
    def pre_create_hosted_configuration_version(
        self,
        event_destination: IEventDestination,
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence["Parameter"]] = None,
    ) -> None:
        '''Adds a PRE_CREATE_HOSTED_CONFIGURATION_VERSION extension with the provided event destination and also creates an extension association to the derived resource.

        :param event_destination: The event that occurs during the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        ...

    @jsii.member(jsii_name="preStartDeployment")
    def pre_start_deployment(
        self,
        event_destination: IEventDestination,
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence["Parameter"]] = None,
    ) -> None:
        '''Adds a PRE_START_DEPLOYMENT extension with the provided event destination and also creates an extension association to the derived resource.

        :param event_destination: The event that occurs during the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        ...


class _IExtensibleProxy:
    '''Defines the extensible base implementation for extension association resources.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_appconfig.IExtensible"

    @jsii.member(jsii_name="addExtension")
    def add_extension(self, extension: "IExtension") -> None:
        '''Adds an extension association to the derived resource.

        :param extension: The extension to create an association for.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__636f478c5d08860b2bd38ade9249d6b6fb935a98206f256a2ce4651910bc75d2)
            check_type(argname="argument extension", value=extension, expected_type=type_hints["extension"])
        return typing.cast(None, jsii.invoke(self, "addExtension", [extension]))

    @jsii.member(jsii_name="on")
    def on(
        self,
        action_point: ActionPoint,
        event_destination: IEventDestination,
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence["Parameter"]] = None,
    ) -> None:
        '''Adds an extension defined by the action point and event destination and also creates an extension association to the derived resource.

        :param action_point: The action point which triggers the event.
        :param event_destination: The event that occurs during the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e51cabd347b530685c4f785d2c1fa5904d0191b12572fa1c83b4ee1b4e018cb4)
            check_type(argname="argument action_point", value=action_point, expected_type=type_hints["action_point"])
            check_type(argname="argument event_destination", value=event_destination, expected_type=type_hints["event_destination"])
        options = ExtensionOptions(
            description=description,
            extension_name=extension_name,
            latest_version_number=latest_version_number,
            parameters=parameters,
        )

        return typing.cast(None, jsii.invoke(self, "on", [action_point, event_destination, options]))

    @jsii.member(jsii_name="onDeploymentBaking")
    def on_deployment_baking(
        self,
        event_destination: IEventDestination,
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence["Parameter"]] = None,
    ) -> None:
        '''Adds an ON_DEPLOYMENT_BAKING extension with the provided event destination and also creates an extension association to the derived resource.

        :param event_destination: The event that occurs during the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6fa7ec332edec343e312eed71e77af42754053e46d5f53a5d9e9553a39b901bd)
            check_type(argname="argument event_destination", value=event_destination, expected_type=type_hints["event_destination"])
        options = ExtensionOptions(
            description=description,
            extension_name=extension_name,
            latest_version_number=latest_version_number,
            parameters=parameters,
        )

        return typing.cast(None, jsii.invoke(self, "onDeploymentBaking", [event_destination, options]))

    @jsii.member(jsii_name="onDeploymentComplete")
    def on_deployment_complete(
        self,
        event_destination: IEventDestination,
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence["Parameter"]] = None,
    ) -> None:
        '''Adds an ON_DEPLOYMENT_COMPLETE extension with the provided event destination and also creates an extension association to the derived resource.

        :param event_destination: The event that occurs during the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81b022234ee1ebf91a3c01114a87d92835d32179a6a8002d81fd0d6bca9a56b5)
            check_type(argname="argument event_destination", value=event_destination, expected_type=type_hints["event_destination"])
        options = ExtensionOptions(
            description=description,
            extension_name=extension_name,
            latest_version_number=latest_version_number,
            parameters=parameters,
        )

        return typing.cast(None, jsii.invoke(self, "onDeploymentComplete", [event_destination, options]))

    @jsii.member(jsii_name="onDeploymentRolledBack")
    def on_deployment_rolled_back(
        self,
        event_destination: IEventDestination,
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence["Parameter"]] = None,
    ) -> None:
        '''Adds an ON_DEPLOYMENT_ROLLED_BACK extension with the provided event destination and also creates an extension association to the derived resource.

        :param event_destination: The event that occurs during the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf6b6442be5cf3ca27f13266e178b6af166e7da8b09b6a4488c37c5d4f316321)
            check_type(argname="argument event_destination", value=event_destination, expected_type=type_hints["event_destination"])
        options = ExtensionOptions(
            description=description,
            extension_name=extension_name,
            latest_version_number=latest_version_number,
            parameters=parameters,
        )

        return typing.cast(None, jsii.invoke(self, "onDeploymentRolledBack", [event_destination, options]))

    @jsii.member(jsii_name="onDeploymentStart")
    def on_deployment_start(
        self,
        event_destination: IEventDestination,
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence["Parameter"]] = None,
    ) -> None:
        '''Adds an ON_DEPLOYMENT_START extension with the provided event destination and also creates an extension association to the derived resource.

        :param event_destination: The event that occurs during the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b18a5bb1eeef9a5b8cc629ae95374f939f48bc090b42485b360fb085c2325636)
            check_type(argname="argument event_destination", value=event_destination, expected_type=type_hints["event_destination"])
        options = ExtensionOptions(
            description=description,
            extension_name=extension_name,
            latest_version_number=latest_version_number,
            parameters=parameters,
        )

        return typing.cast(None, jsii.invoke(self, "onDeploymentStart", [event_destination, options]))

    @jsii.member(jsii_name="onDeploymentStep")
    def on_deployment_step(
        self,
        event_destination: IEventDestination,
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence["Parameter"]] = None,
    ) -> None:
        '''Adds an ON_DEPLOYMENT_STEP extension with the provided event destination and also creates an extension association to the derived resource.

        :param event_destination: The event that occurs during the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b9f21b4a7c2b4d829a87f00606d3b497186ac272a0e388ed8b46a67d80e3b42)
            check_type(argname="argument event_destination", value=event_destination, expected_type=type_hints["event_destination"])
        options = ExtensionOptions(
            description=description,
            extension_name=extension_name,
            latest_version_number=latest_version_number,
            parameters=parameters,
        )

        return typing.cast(None, jsii.invoke(self, "onDeploymentStep", [event_destination, options]))

    @jsii.member(jsii_name="preCreateHostedConfigurationVersion")
    def pre_create_hosted_configuration_version(
        self,
        event_destination: IEventDestination,
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence["Parameter"]] = None,
    ) -> None:
        '''Adds a PRE_CREATE_HOSTED_CONFIGURATION_VERSION extension with the provided event destination and also creates an extension association to the derived resource.

        :param event_destination: The event that occurs during the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d9383750894ef15ea5397fbe279df0dfa736eb00f19f0da10a9876cbafe3d26)
            check_type(argname="argument event_destination", value=event_destination, expected_type=type_hints["event_destination"])
        options = ExtensionOptions(
            description=description,
            extension_name=extension_name,
            latest_version_number=latest_version_number,
            parameters=parameters,
        )

        return typing.cast(None, jsii.invoke(self, "preCreateHostedConfigurationVersion", [event_destination, options]))

    @jsii.member(jsii_name="preStartDeployment")
    def pre_start_deployment(
        self,
        event_destination: IEventDestination,
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence["Parameter"]] = None,
    ) -> None:
        '''Adds a PRE_START_DEPLOYMENT extension with the provided event destination and also creates an extension association to the derived resource.

        :param event_destination: The event that occurs during the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d882c483f3b7fe82114c8c7963525171dd0a2605c29b70221b2a01606bda297a)
            check_type(argname="argument event_destination", value=event_destination, expected_type=type_hints["event_destination"])
        options = ExtensionOptions(
            description=description,
            extension_name=extension_name,
            latest_version_number=latest_version_number,
            parameters=parameters,
        )

        return typing.cast(None, jsii.invoke(self, "preStartDeployment", [event_destination, options]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IExtensible).__jsii_proxy_class__ = lambda : _IExtensibleProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_appconfig.IExtension")
class IExtension(_IResource_c80c4260, typing_extensions.Protocol):
    @builtins.property
    @jsii.member(jsii_name="extensionArn")
    def extension_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the extension.

        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="extensionId")
    def extension_id(self) -> builtins.str:
        '''The ID of the extension.

        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="extensionVersionNumber")
    def extension_version_number(self) -> jsii.Number:
        '''The version number of the extension.

        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="actions")
    def actions(self) -> typing.Optional[typing.List[Action]]:
        '''The actions for the extension.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the extension.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="latestVersionNumber")
    def latest_version_number(self) -> typing.Optional[jsii.Number]:
        '''The latest version number of the extension.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the extension.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> typing.Optional[typing.List["Parameter"]]:
        '''The parameters of the extension.'''
        ...


class _IExtensionProxy(
    jsii.proxy_for(_IResource_c80c4260), # type: ignore[misc]
):
    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_appconfig.IExtension"

    @builtins.property
    @jsii.member(jsii_name="extensionArn")
    def extension_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the extension.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "extensionArn"))

    @builtins.property
    @jsii.member(jsii_name="extensionId")
    def extension_id(self) -> builtins.str:
        '''The ID of the extension.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "extensionId"))

    @builtins.property
    @jsii.member(jsii_name="extensionVersionNumber")
    def extension_version_number(self) -> jsii.Number:
        '''The version number of the extension.

        :attribute: true
        '''
        return typing.cast(jsii.Number, jsii.get(self, "extensionVersionNumber"))

    @builtins.property
    @jsii.member(jsii_name="actions")
    def actions(self) -> typing.Optional[typing.List[Action]]:
        '''The actions for the extension.'''
        return typing.cast(typing.Optional[typing.List[Action]], jsii.get(self, "actions"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the extension.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @builtins.property
    @jsii.member(jsii_name="latestVersionNumber")
    def latest_version_number(self) -> typing.Optional[jsii.Number]:
        '''The latest version number of the extension.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "latestVersionNumber"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the extension.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> typing.Optional[typing.List["Parameter"]]:
        '''The parameters of the extension.'''
        return typing.cast(typing.Optional[typing.List["Parameter"]], jsii.get(self, "parameters"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IExtension).__jsii_proxy_class__ = lambda : _IExtensionProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_appconfig.IValidator")
class IValidator(typing_extensions.Protocol):
    @builtins.property
    @jsii.member(jsii_name="content")
    def content(self) -> builtins.str:
        '''The content of the validator.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> "ValidatorType":
        '''The type of validator.'''
        ...


class _IValidatorProxy:
    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_appconfig.IValidator"

    @builtins.property
    @jsii.member(jsii_name="content")
    def content(self) -> builtins.str:
        '''The content of the validator.'''
        return typing.cast(builtins.str, jsii.get(self, "content"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> "ValidatorType":
        '''The type of validator.'''
        return typing.cast("ValidatorType", jsii.get(self, "type"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IValidator).__jsii_proxy_class__ = lambda : _IValidatorProxy


@jsii.implements(IValidator)
class JsonSchemaValidator(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="aws-cdk-lib.aws_appconfig.JsonSchemaValidator",
):
    '''Defines a JSON Schema validator.

    :exampleMetadata: infused

    Example::

        # application: appconfig.Application
        # fn: lambda.Function
        
        
        appconfig.HostedConfiguration(self, "MyHostedConfiguration",
            application=application,
            content=appconfig.ConfigurationContent.from_inline_text("This is my configuration content."),
            validators=[
                appconfig.JsonSchemaValidator.from_file("schema.json"),
                appconfig.LambdaValidator.from_function(fn)
            ]
        )
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="fromFile")
    @builtins.classmethod
    def from_file(cls, input_path: builtins.str) -> "JsonSchemaValidator":
        '''Defines a JSON Schema validator from a file.

        :param input_path: The path to the file that defines the validator.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78883cc72a23f294c8f7fa290505676f4a7bab645b06f048344b15590a97acae)
            check_type(argname="argument input_path", value=input_path, expected_type=type_hints["input_path"])
        return typing.cast("JsonSchemaValidator", jsii.sinvoke(cls, "fromFile", [input_path]))

    @jsii.member(jsii_name="fromInline")
    @builtins.classmethod
    def from_inline(cls, code: builtins.str) -> "JsonSchemaValidator":
        '''Defines a JSON Schema validator from inline code.

        :param code: The inline code that defines the validator.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ac39b4aca41716a9c0c911538ffd870eaabc02b68632f8b0cee4708ca0935da)
            check_type(argname="argument code", value=code, expected_type=type_hints["code"])
        return typing.cast("JsonSchemaValidator", jsii.sinvoke(cls, "fromInline", [code]))

    @builtins.property
    @jsii.member(jsii_name="content")
    @abc.abstractmethod
    def content(self) -> builtins.str:
        '''The content of the validator.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="type")
    @abc.abstractmethod
    def type(self) -> "ValidatorType":
        '''The type of validator.'''
        ...


class _JsonSchemaValidatorProxy(JsonSchemaValidator):
    @builtins.property
    @jsii.member(jsii_name="content")
    def content(self) -> builtins.str:
        '''The content of the validator.'''
        return typing.cast(builtins.str, jsii.get(self, "content"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> "ValidatorType":
        '''The type of validator.'''
        return typing.cast("ValidatorType", jsii.get(self, "type"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, JsonSchemaValidator).__jsii_proxy_class__ = lambda : _JsonSchemaValidatorProxy


@jsii.implements(IEventDestination)
class LambdaDestination(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appconfig.LambdaDestination",
):
    '''Use an AWS Lambda function as an event destination.

    :exampleMetadata: infused

    Example::

        # fn: lambda.Function
        
        
        appconfig.Extension(self, "MyExtension",
            actions=[
                appconfig.Action(
                    action_points=[appconfig.ActionPoint.ON_DEPLOYMENT_START],
                    event_destination=appconfig.LambdaDestination(fn)
                )
            ]
        )
    '''

    def __init__(self, func: _IFunction_6adb0ab8) -> None:
        '''
        :param func: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c652c76ed075aa64f62bcabc7e6b60f2d86c05f769c17fb271ed8405259f68bb)
            check_type(argname="argument func", value=func, expected_type=type_hints["func"])
        jsii.create(self.__class__, self, [func])

    @builtins.property
    @jsii.member(jsii_name="extensionUri")
    def extension_uri(self) -> builtins.str:
        '''The URI of the extension event destination.'''
        return typing.cast(builtins.str, jsii.get(self, "extensionUri"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> "SourceType":
        '''The type of the extension event destination.'''
        return typing.cast("SourceType", jsii.get(self, "type"))

    @builtins.property
    @jsii.member(jsii_name="policyDocument")
    def policy_document(self) -> typing.Optional[_PolicyDocument_3ac34393]:
        '''The IAM policy document to invoke the event destination.'''
        return typing.cast(typing.Optional[_PolicyDocument_3ac34393], jsii.get(self, "policyDocument"))


@jsii.implements(IValidator)
class LambdaValidator(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="aws-cdk-lib.aws_appconfig.LambdaValidator",
):
    '''Defines an AWS Lambda validator.

    :exampleMetadata: infused

    Example::

        # application: appconfig.Application
        # fn: lambda.Function
        
        
        appconfig.HostedConfiguration(self, "MyHostedConfiguration",
            application=application,
            content=appconfig.ConfigurationContent.from_inline_text("This is my configuration content."),
            validators=[
                appconfig.JsonSchemaValidator.from_file("schema.json"),
                appconfig.LambdaValidator.from_function(fn)
            ]
        )
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="fromFunction")
    @builtins.classmethod
    def from_function(cls, func: _Function_244f85d8) -> "LambdaValidator":
        '''Defines an AWS Lambda validator from a Lambda function.

        This will call
        ``addPermission`` to your function to grant AWS AppConfig permissions.

        :param func: The function that defines the validator.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a245d9ad2d5a72963867d7f392bf31c9977c87f33b0ba8389f1024ee4eecad9e)
            check_type(argname="argument func", value=func, expected_type=type_hints["func"])
        return typing.cast("LambdaValidator", jsii.sinvoke(cls, "fromFunction", [func]))

    @builtins.property
    @jsii.member(jsii_name="content")
    @abc.abstractmethod
    def content(self) -> builtins.str:
        '''The content of the validator.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="type")
    @abc.abstractmethod
    def type(self) -> "ValidatorType":
        '''The type of validator.'''
        ...


class _LambdaValidatorProxy(LambdaValidator):
    @builtins.property
    @jsii.member(jsii_name="content")
    def content(self) -> builtins.str:
        '''The content of the validator.'''
        return typing.cast(builtins.str, jsii.get(self, "content"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> "ValidatorType":
        '''The type of validator.'''
        return typing.cast("ValidatorType", jsii.get(self, "type"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, LambdaValidator).__jsii_proxy_class__ = lambda : _LambdaValidatorProxy


class Monitor(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="aws-cdk-lib.aws_appconfig.Monitor",
):
    '''Defines monitors that will be associated with an AWS AppConfig environment.

    :exampleMetadata: infused

    Example::

        # application: appconfig.Application
        # alarm: cloudwatch.Alarm
        # composite_alarm: cloudwatch.CompositeAlarm
        
        
        appconfig.Environment(self, "MyEnvironment",
            application=application,
            monitors=[
                appconfig.Monitor.from_cloud_watch_alarm(alarm),
                appconfig.Monitor.from_cloud_watch_alarm(composite_alarm)
            ]
        )
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="fromCfnMonitorsProperty")
    @builtins.classmethod
    def from_cfn_monitors_property(
        cls,
        *,
        alarm_arn: typing.Optional[builtins.str] = None,
        alarm_role_arn: typing.Optional[builtins.str] = None,
    ) -> "Monitor":
        '''Creates a Monitor from a CfnEnvironment.MonitorsProperty construct.

        :param alarm_arn: 
        :param alarm_role_arn: 
        '''
        monitors_property = CfnEnvironment.MonitorsProperty(
            alarm_arn=alarm_arn, alarm_role_arn=alarm_role_arn
        )

        return typing.cast("Monitor", jsii.sinvoke(cls, "fromCfnMonitorsProperty", [monitors_property]))

    @jsii.member(jsii_name="fromCloudWatchAlarm")
    @builtins.classmethod
    def from_cloud_watch_alarm(
        cls,
        alarm: _IAlarm_ff3eabc0,
        alarm_role: typing.Optional[_IRole_235f5d8e] = None,
    ) -> "Monitor":
        '''Creates a Monitor from a CloudWatch alarm.

        If the alarm role is not specified, a role will
        be generated.

        :param alarm: The Amazon CloudWatch alarm.
        :param alarm_role: The IAM role for AWS AppConfig to view the alarm state.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ccc59f1c5523364b8528526a5b6087774df2b905407caca37b7c685a5bfb76cb)
            check_type(argname="argument alarm", value=alarm, expected_type=type_hints["alarm"])
            check_type(argname="argument alarm_role", value=alarm_role, expected_type=type_hints["alarm_role"])
        return typing.cast("Monitor", jsii.sinvoke(cls, "fromCloudWatchAlarm", [alarm, alarm_role]))

    @builtins.property
    @jsii.member(jsii_name="alarmArn")
    @abc.abstractmethod
    def alarm_arn(self) -> builtins.str:
        '''The alarm ARN for AWS AppConfig to monitor.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="monitorType")
    @abc.abstractmethod
    def monitor_type(self) -> "MonitorType":
        '''The type of monitor.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="alarmRoleArn")
    @abc.abstractmethod
    def alarm_role_arn(self) -> typing.Optional[builtins.str]:
        '''The IAM role ARN for AWS AppConfig to view the alarm state.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="isCompositeAlarm")
    @abc.abstractmethod
    def is_composite_alarm(self) -> typing.Optional[builtins.bool]:
        '''Indicates whether a CloudWatch alarm is a composite alarm.'''
        ...


class _MonitorProxy(Monitor):
    @builtins.property
    @jsii.member(jsii_name="alarmArn")
    def alarm_arn(self) -> builtins.str:
        '''The alarm ARN for AWS AppConfig to monitor.'''
        return typing.cast(builtins.str, jsii.get(self, "alarmArn"))

    @builtins.property
    @jsii.member(jsii_name="monitorType")
    def monitor_type(self) -> "MonitorType":
        '''The type of monitor.'''
        return typing.cast("MonitorType", jsii.get(self, "monitorType"))

    @builtins.property
    @jsii.member(jsii_name="alarmRoleArn")
    def alarm_role_arn(self) -> typing.Optional[builtins.str]:
        '''The IAM role ARN for AWS AppConfig to view the alarm state.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alarmRoleArn"))

    @builtins.property
    @jsii.member(jsii_name="isCompositeAlarm")
    def is_composite_alarm(self) -> typing.Optional[builtins.bool]:
        '''Indicates whether a CloudWatch alarm is a composite alarm.'''
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "isCompositeAlarm"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, Monitor).__jsii_proxy_class__ = lambda : _MonitorProxy


@jsii.enum(jsii_type="aws-cdk-lib.aws_appconfig.MonitorType")
class MonitorType(enum.Enum):
    '''The type of Monitor.'''

    CLOUDWATCH = "CLOUDWATCH"
    '''A Monitor from a CloudWatch alarm.'''
    CFN_MONITORS_PROPERTY = "CFN_MONITORS_PROPERTY"
    '''A Monitor from a CfnEnvironment.MonitorsProperty construct.'''


class Parameter(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appconfig.Parameter",
):
    '''Defines a parameter for an extension.

    :exampleMetadata: infused

    Example::

        # fn: lambda.Function
        
        
        appconfig.Extension(self, "MyExtension",
            actions=[
                appconfig.Action(
                    action_points=[appconfig.ActionPoint.ON_DEPLOYMENT_START],
                    event_destination=appconfig.LambdaDestination(fn)
                )
            ],
            parameters=[
                appconfig.Parameter.required("testParam", "true"),
                appconfig.Parameter.not_required("testNotRequiredParam")
            ]
        )
    '''

    @jsii.member(jsii_name="notRequired")
    @builtins.classmethod
    def not_required(
        cls,
        name: builtins.str,
        value: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
    ) -> "Parameter":
        '''An optional parameter for an extension.

        :param name: The name of the parameter.
        :param value: The value of the parameter.
        :param description: A description for the parameter.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e86480f6d31f87043e7defee36f9e4716c05611a4f0372a521151cc2c7968eac)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
        return typing.cast("Parameter", jsii.sinvoke(cls, "notRequired", [name, value, description]))

    @jsii.member(jsii_name="required")
    @builtins.classmethod
    def required(
        cls,
        name: builtins.str,
        value: builtins.str,
        description: typing.Optional[builtins.str] = None,
    ) -> "Parameter":
        '''A required parameter for an extension.

        :param name: The name of the parameter.
        :param value: The value of the parameter.
        :param description: A description for the parameter.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c36eea0e8c419bcd42c01216c20d5a8f57657c660596cf07a801d4c269c0306)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
        return typing.cast("Parameter", jsii.sinvoke(cls, "required", [name, value, description]))

    @builtins.property
    @jsii.member(jsii_name="isRequired")
    def is_required(self) -> builtins.bool:
        '''A boolean that indicates if the parameter is required or optional.'''
        return typing.cast(builtins.bool, jsii.get(self, "isRequired"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the parameter.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the parameter.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> typing.Optional[builtins.str]:
        '''The value of the parameter.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "value"))


@jsii.enum(jsii_type="aws-cdk-lib.aws_appconfig.Platform")
class Platform(enum.Enum):
    '''Defines the platform for the AWS AppConfig Lambda extension.'''

    X86_64 = "X86_64"
    ARM_64 = "ARM_64"


class RolloutStrategy(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="aws-cdk-lib.aws_appconfig.RolloutStrategy",
):
    '''Defines the rollout strategy for a deployment strategy and includes the growth factor, deployment duration, growth type, and optionally final bake time.

    :see: https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-deployment-strategy.html
    :exampleMetadata: infused

    Example::

        appconfig.DeploymentStrategy(self, "MyDeploymentStrategy",
            rollout_strategy=appconfig.RolloutStrategy.linear(
                growth_factor=20,
                deployment_duration=Duration.minutes(30),
                final_bake_time=Duration.minutes(30)
            )
        )
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="exponential")
    @builtins.classmethod
    def exponential(
        cls,
        *,
        deployment_duration: _Duration_4839e8c3,
        growth_factor: jsii.Number,
        final_bake_time: typing.Optional[_Duration_4839e8c3] = None,
    ) -> "RolloutStrategy":
        '''Build your own exponential rollout strategy.

        :param deployment_duration: The deployment duration of the deployment strategy. This defines the total amount of time for a deployment to last.
        :param growth_factor: The growth factor of the deployment strategy. This defines the percentage of targets to receive a deployed configuration during each interval.
        :param final_bake_time: The final bake time of the deployment strategy. This setting specifies the amount of time AWS AppConfig monitors for Amazon CloudWatch alarms after the configuration has been deployed to 100% of its targets, before considering the deployment to be complete. If an alarm is triggered during this time, AWS AppConfig rolls back the deployment. Default: Duration.minutes(0)
        '''
        props = RolloutStrategyProps(
            deployment_duration=deployment_duration,
            growth_factor=growth_factor,
            final_bake_time=final_bake_time,
        )

        return typing.cast("RolloutStrategy", jsii.sinvoke(cls, "exponential", [props]))

    @jsii.member(jsii_name="linear")
    @builtins.classmethod
    def linear(
        cls,
        *,
        deployment_duration: _Duration_4839e8c3,
        growth_factor: jsii.Number,
        final_bake_time: typing.Optional[_Duration_4839e8c3] = None,
    ) -> "RolloutStrategy":
        '''Build your own linear rollout strategy.

        :param deployment_duration: The deployment duration of the deployment strategy. This defines the total amount of time for a deployment to last.
        :param growth_factor: The growth factor of the deployment strategy. This defines the percentage of targets to receive a deployed configuration during each interval.
        :param final_bake_time: The final bake time of the deployment strategy. This setting specifies the amount of time AWS AppConfig monitors for Amazon CloudWatch alarms after the configuration has been deployed to 100% of its targets, before considering the deployment to be complete. If an alarm is triggered during this time, AWS AppConfig rolls back the deployment. Default: Duration.minutes(0)
        '''
        props = RolloutStrategyProps(
            deployment_duration=deployment_duration,
            growth_factor=growth_factor,
            final_bake_time=final_bake_time,
        )

        return typing.cast("RolloutStrategy", jsii.sinvoke(cls, "linear", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ALL_AT_ONCE")
    def ALL_AT_ONCE(cls) -> "RolloutStrategy":
        '''**Quick**.

        This strategy deploys the configuration to all targets immediately.
        '''
        return typing.cast("RolloutStrategy", jsii.sget(cls, "ALL_AT_ONCE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CANARY_10_PERCENT_20_MINUTES")
    def CANARY_10_PERCENT_20_MINUTES(cls) -> "RolloutStrategy":
        '''**AWS Recommended**.

        This strategy processes the deployment exponentially using a 10% growth factor over 20 minutes.
        AWS AppConfig recommends using this strategy for production deployments because it aligns with AWS best practices
        for configuration deployments.
        '''
        return typing.cast("RolloutStrategy", jsii.sget(cls, "CANARY_10_PERCENT_20_MINUTES"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="LINEAR_20_PERCENT_EVERY_6_MINUTES")
    def LINEAR_20_PERCENT_EVERY_6_MINUTES(cls) -> "RolloutStrategy":
        '''**AWS Recommended**.

        This strategy deploys the configuration to 20% of all targets every six minutes for a 30 minute deployment.
        AWS AppConfig recommends using this strategy for production deployments because it aligns with AWS best practices
        for configuration deployments.
        '''
        return typing.cast("RolloutStrategy", jsii.sget(cls, "LINEAR_20_PERCENT_EVERY_6_MINUTES"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="LINEAR_50_PERCENT_EVERY_30_SECONDS")
    def LINEAR_50_PERCENT_EVERY_30_SECONDS(cls) -> "RolloutStrategy":
        '''**Testing/Demonstration**.

        This strategy deploys the configuration to half of all targets every 30 seconds for a
        one-minute deployment. AWS AppConfig recommends using this strategy only for testing or demonstration purposes because
        it has a short duration and bake time.
        '''
        return typing.cast("RolloutStrategy", jsii.sget(cls, "LINEAR_50_PERCENT_EVERY_30_SECONDS"))

    @builtins.property
    @jsii.member(jsii_name="deploymentDuration")
    @abc.abstractmethod
    def deployment_duration(self) -> _Duration_4839e8c3:
        '''The deployment duration of the rollout strategy.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="growthFactor")
    @abc.abstractmethod
    def growth_factor(self) -> jsii.Number:
        '''The growth factor of the rollout strategy.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="finalBakeTime")
    @abc.abstractmethod
    def final_bake_time(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The final bake time of the deployment strategy.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="growthType")
    @abc.abstractmethod
    def growth_type(self) -> typing.Optional[GrowthType]:
        '''The growth type of the rollout strategy.'''
        ...


class _RolloutStrategyProxy(RolloutStrategy):
    @builtins.property
    @jsii.member(jsii_name="deploymentDuration")
    def deployment_duration(self) -> _Duration_4839e8c3:
        '''The deployment duration of the rollout strategy.'''
        return typing.cast(_Duration_4839e8c3, jsii.get(self, "deploymentDuration"))

    @builtins.property
    @jsii.member(jsii_name="growthFactor")
    def growth_factor(self) -> jsii.Number:
        '''The growth factor of the rollout strategy.'''
        return typing.cast(jsii.Number, jsii.get(self, "growthFactor"))

    @builtins.property
    @jsii.member(jsii_name="finalBakeTime")
    def final_bake_time(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The final bake time of the deployment strategy.'''
        return typing.cast(typing.Optional[_Duration_4839e8c3], jsii.get(self, "finalBakeTime"))

    @builtins.property
    @jsii.member(jsii_name="growthType")
    def growth_type(self) -> typing.Optional[GrowthType]:
        '''The growth type of the rollout strategy.'''
        return typing.cast(typing.Optional[GrowthType], jsii.get(self, "growthType"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, RolloutStrategy).__jsii_proxy_class__ = lambda : _RolloutStrategyProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appconfig.RolloutStrategyProps",
    jsii_struct_bases=[],
    name_mapping={
        "deployment_duration": "deploymentDuration",
        "growth_factor": "growthFactor",
        "final_bake_time": "finalBakeTime",
    },
)
class RolloutStrategyProps:
    def __init__(
        self,
        *,
        deployment_duration: _Duration_4839e8c3,
        growth_factor: jsii.Number,
        final_bake_time: typing.Optional[_Duration_4839e8c3] = None,
    ) -> None:
        '''Properties for the Rollout Strategy.

        :param deployment_duration: The deployment duration of the deployment strategy. This defines the total amount of time for a deployment to last.
        :param growth_factor: The growth factor of the deployment strategy. This defines the percentage of targets to receive a deployed configuration during each interval.
        :param final_bake_time: The final bake time of the deployment strategy. This setting specifies the amount of time AWS AppConfig monitors for Amazon CloudWatch alarms after the configuration has been deployed to 100% of its targets, before considering the deployment to be complete. If an alarm is triggered during this time, AWS AppConfig rolls back the deployment. Default: Duration.minutes(0)

        :exampleMetadata: infused

        Example::

            # application: appconfig.Application
            
            
            appconfig.HostedConfiguration(self, "MyHostedConfiguration",
                application=application,
                content=appconfig.ConfigurationContent.from_inline_text("This is my configuration content."),
                deployment_strategy=appconfig.DeploymentStrategy(self, "MyDeploymentStrategy",
                    rollout_strategy=appconfig.RolloutStrategy.linear(
                        growth_factor=15,
                        deployment_duration=Duration.minutes(30),
                        final_bake_time=Duration.minutes(15)
                    )
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd34e38231115cf062a079b568bd536f7138f65ab8fb9db0b917b7c17c03e75b)
            check_type(argname="argument deployment_duration", value=deployment_duration, expected_type=type_hints["deployment_duration"])
            check_type(argname="argument growth_factor", value=growth_factor, expected_type=type_hints["growth_factor"])
            check_type(argname="argument final_bake_time", value=final_bake_time, expected_type=type_hints["final_bake_time"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "deployment_duration": deployment_duration,
            "growth_factor": growth_factor,
        }
        if final_bake_time is not None:
            self._values["final_bake_time"] = final_bake_time

    @builtins.property
    def deployment_duration(self) -> _Duration_4839e8c3:
        '''The deployment duration of the deployment strategy.

        This defines
        the total amount of time for a deployment to last.
        '''
        result = self._values.get("deployment_duration")
        assert result is not None, "Required property 'deployment_duration' is missing"
        return typing.cast(_Duration_4839e8c3, result)

    @builtins.property
    def growth_factor(self) -> jsii.Number:
        '''The growth factor of the deployment strategy.

        This defines
        the percentage of targets to receive a deployed configuration
        during each interval.
        '''
        result = self._values.get("growth_factor")
        assert result is not None, "Required property 'growth_factor' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def final_bake_time(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The final bake time of the deployment strategy.

        This setting specifies the amount of time AWS AppConfig monitors for Amazon
        CloudWatch alarms after the configuration has been deployed to
        100% of its targets, before considering the deployment to be complete.
        If an alarm is triggered during this time, AWS AppConfig rolls back
        the deployment.

        :default: Duration.minutes(0)
        '''
        result = self._values.get("final_bake_time")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RolloutStrategyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IEventDestination)
class SnsDestination(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appconfig.SnsDestination",
):
    '''Use an Amazon SNS topic as an event destination.

    :exampleMetadata: infused

    Example::

        # topic: sns.Topic
        
        
        appconfig.Extension(self, "MyExtension",
            actions=[
                appconfig.Action(
                    action_points=[appconfig.ActionPoint.ON_DEPLOYMENT_START],
                    event_destination=appconfig.SnsDestination(topic)
                )
            ]
        )
    '''

    def __init__(self, topic: _ITopic_9eca4852) -> None:
        '''
        :param topic: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7717c5cbe1c0c49e9bad0179c39c84fc906b10056fbae28b785806ae0d939597)
            check_type(argname="argument topic", value=topic, expected_type=type_hints["topic"])
        jsii.create(self.__class__, self, [topic])

    @builtins.property
    @jsii.member(jsii_name="extensionUri")
    def extension_uri(self) -> builtins.str:
        '''The URI of the extension event destination.'''
        return typing.cast(builtins.str, jsii.get(self, "extensionUri"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> "SourceType":
        '''The type of the extension event destination.'''
        return typing.cast("SourceType", jsii.get(self, "type"))

    @builtins.property
    @jsii.member(jsii_name="policyDocument")
    def policy_document(self) -> typing.Optional[_PolicyDocument_3ac34393]:
        '''The IAM policy document to invoke the event destination.'''
        return typing.cast(typing.Optional[_PolicyDocument_3ac34393], jsii.get(self, "policyDocument"))


@jsii.enum(jsii_type="aws-cdk-lib.aws_appconfig.SourceType")
class SourceType(enum.Enum):
    '''Defines the source type for event destinations.'''

    LAMBDA = "LAMBDA"
    SQS = "SQS"
    SNS = "SNS"
    EVENTS = "EVENTS"


@jsii.implements(IConfiguration, IExtensible)
class SourcedConfiguration(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appconfig.SourcedConfiguration",
):
    '''A sourced configuration represents configuration stored in an Amazon S3 bucket, AWS Secrets Manager secret, Systems Manager (SSM) Parameter Store parameter, SSM document, or AWS CodePipeline.

    :exampleMetadata: infused

    Example::

        # application: appconfig.Application
        # bucket: s3.Bucket
        
        
        appconfig.SourcedConfiguration(self, "MySourcedConfiguration",
            application=application,
            location=appconfig.ConfigurationSource.from_bucket(bucket, "path/to/file.json"),
            type=appconfig.ConfigurationType.FEATURE_FLAGS,
            name="MyConfig",
            description="This is my sourced configuration from CDK."
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        location: ConfigurationSource,
        retrieval_role: typing.Optional[_IRole_235f5d8e] = None,
        version_number: typing.Optional[builtins.str] = None,
        application: IApplication,
        deployment_key: typing.Optional[_IKey_5f11635f] = None,
        deployment_strategy: typing.Optional[IDeploymentStrategy] = None,
        deploy_to: typing.Optional[typing.Sequence[IEnvironment]] = None,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        type: typing.Optional[ConfigurationType] = None,
        validators: typing.Optional[typing.Sequence[IValidator]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param location: The location where the configuration is stored.
        :param retrieval_role: The IAM role to retrieve the configuration. Default: - A role is generated.
        :param version_number: The version number of the sourced configuration to deploy. If this is not specified, then there will be no deployment. Default: - None.
        :param application: The application associated with the configuration.
        :param deployment_key: The deployment key of the configuration. Default: - None.
        :param deployment_strategy: The deployment strategy for the configuration. Default: - A deployment strategy with the rollout strategy set to RolloutStrategy.CANARY_10_PERCENT_20_MINUTES
        :param deploy_to: The list of environments to deploy the configuration to. If this parameter is not specified, then there will be no deployment created alongside this configuration. Deployments can be added later using the ``IEnvironment.addDeployment`` or ``IEnvironment.addDeployments`` methods. Default: - None.
        :param description: The description of the configuration. Default: - No description.
        :param name: The name of the configuration. Default: - A name is generated.
        :param type: The type of configuration. Default: ConfigurationType.FREEFORM
        :param validators: The validators for the configuration. Default: - No validators.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61200a738f2584e5d86190492c99ded9cebb5cc41d230eec1c74f7130b50cb6e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = SourcedConfigurationProps(
            location=location,
            retrieval_role=retrieval_role,
            version_number=version_number,
            application=application,
            deployment_key=deployment_key,
            deployment_strategy=deployment_strategy,
            deploy_to=deploy_to,
            description=description,
            name=name,
            type=type,
            validators=validators,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="addExistingEnvironmentsToApplication")
    def _add_existing_environments_to_application(self) -> None:
        return typing.cast(None, jsii.invoke(self, "addExistingEnvironmentsToApplication", []))

    @jsii.member(jsii_name="addExtension")
    def add_extension(self, extension: IExtension) -> None:
        '''Adds an extension association to the configuration profile.

        :param extension: The extension to create an association for.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__567a975af03924cb099dbb4e55da080a85101964698787ded85c7d42f63cd3b5)
            check_type(argname="argument extension", value=extension, expected_type=type_hints["extension"])
        return typing.cast(None, jsii.invoke(self, "addExtension", [extension]))

    @jsii.member(jsii_name="deployConfigToEnvironments")
    def _deploy_config_to_environments(self) -> None:
        return typing.cast(None, jsii.invoke(self, "deployConfigToEnvironments", []))

    @jsii.member(jsii_name="on")
    def on(
        self,
        action_point: ActionPoint,
        event_destination: IEventDestination,
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence[Parameter]] = None,
    ) -> None:
        '''Adds an extension defined by the action point and event destination and also creates an extension association to the configuration profile.

        :param action_point: The action point which triggers the event.
        :param event_destination: The event that occurs during the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63ed4552787e88def66e9a8b0abdb2cf11f84235e5089c5e232a1053e6059ecc)
            check_type(argname="argument action_point", value=action_point, expected_type=type_hints["action_point"])
            check_type(argname="argument event_destination", value=event_destination, expected_type=type_hints["event_destination"])
        options = ExtensionOptions(
            description=description,
            extension_name=extension_name,
            latest_version_number=latest_version_number,
            parameters=parameters,
        )

        return typing.cast(None, jsii.invoke(self, "on", [action_point, event_destination, options]))

    @jsii.member(jsii_name="onDeploymentBaking")
    def on_deployment_baking(
        self,
        event_destination: IEventDestination,
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence[Parameter]] = None,
    ) -> None:
        '''Adds an ON_DEPLOYMENT_BAKING extension with the provided event destination and also creates an extension association to the configuration profile.

        :param event_destination: The event that occurs during the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a145ea507639ac2b7073bd0f352974744e3821459664f412348146516ee16082)
            check_type(argname="argument event_destination", value=event_destination, expected_type=type_hints["event_destination"])
        options = ExtensionOptions(
            description=description,
            extension_name=extension_name,
            latest_version_number=latest_version_number,
            parameters=parameters,
        )

        return typing.cast(None, jsii.invoke(self, "onDeploymentBaking", [event_destination, options]))

    @jsii.member(jsii_name="onDeploymentComplete")
    def on_deployment_complete(
        self,
        event_destination: IEventDestination,
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence[Parameter]] = None,
    ) -> None:
        '''Adds an ON_DEPLOYMENT_COMPLETE extension with the provided event destination and also creates an extension association to the configuration profile.

        :param event_destination: The event that occurs during the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0fe8f4ebcc7ac2ce0b33ab896176c13c0f82e5bd7bf4396cdfbb5e837e3ec16d)
            check_type(argname="argument event_destination", value=event_destination, expected_type=type_hints["event_destination"])
        options = ExtensionOptions(
            description=description,
            extension_name=extension_name,
            latest_version_number=latest_version_number,
            parameters=parameters,
        )

        return typing.cast(None, jsii.invoke(self, "onDeploymentComplete", [event_destination, options]))

    @jsii.member(jsii_name="onDeploymentRolledBack")
    def on_deployment_rolled_back(
        self,
        event_destination: IEventDestination,
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence[Parameter]] = None,
    ) -> None:
        '''Adds an ON_DEPLOYMENT_ROLLED_BACK extension with the provided event destination and also creates an extension association to the configuration profile.

        :param event_destination: The event that occurs during the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64649b15b58a938933f677b7b099e3ead2b877aef924bed10aa8fd894977cb18)
            check_type(argname="argument event_destination", value=event_destination, expected_type=type_hints["event_destination"])
        options = ExtensionOptions(
            description=description,
            extension_name=extension_name,
            latest_version_number=latest_version_number,
            parameters=parameters,
        )

        return typing.cast(None, jsii.invoke(self, "onDeploymentRolledBack", [event_destination, options]))

    @jsii.member(jsii_name="onDeploymentStart")
    def on_deployment_start(
        self,
        event_destination: IEventDestination,
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence[Parameter]] = None,
    ) -> None:
        '''Adds an ON_DEPLOYMENT_START extension with the provided event destination and also creates an extension association to the configuration profile.

        :param event_destination: The event that occurs during the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a72a20510f9367a1ef380b113df52cc7b9a3191df20f658f8fafce65cf900ef)
            check_type(argname="argument event_destination", value=event_destination, expected_type=type_hints["event_destination"])
        options = ExtensionOptions(
            description=description,
            extension_name=extension_name,
            latest_version_number=latest_version_number,
            parameters=parameters,
        )

        return typing.cast(None, jsii.invoke(self, "onDeploymentStart", [event_destination, options]))

    @jsii.member(jsii_name="onDeploymentStep")
    def on_deployment_step(
        self,
        event_destination: IEventDestination,
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence[Parameter]] = None,
    ) -> None:
        '''Adds an ON_DEPLOYMENT_STEP extension with the provided event destination and also creates an extension association to the configuration profile.

        :param event_destination: The event that occurs during the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__918c62fffe22d9133a92395bb9d8eb25cb55764c05a34180ae8212464e093e09)
            check_type(argname="argument event_destination", value=event_destination, expected_type=type_hints["event_destination"])
        options = ExtensionOptions(
            description=description,
            extension_name=extension_name,
            latest_version_number=latest_version_number,
            parameters=parameters,
        )

        return typing.cast(None, jsii.invoke(self, "onDeploymentStep", [event_destination, options]))

    @jsii.member(jsii_name="preCreateHostedConfigurationVersion")
    def pre_create_hosted_configuration_version(
        self,
        event_destination: IEventDestination,
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence[Parameter]] = None,
    ) -> None:
        '''Adds a PRE_CREATE_HOSTED_CONFIGURATION_VERSION extension with the provided event destination and also creates an extension association to the configuration profile.

        :param event_destination: The event that occurs during the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71565cf401ee87c96ccfb60887b1f50eea8c2e04bc591d9804604fc7923acb19)
            check_type(argname="argument event_destination", value=event_destination, expected_type=type_hints["event_destination"])
        options = ExtensionOptions(
            description=description,
            extension_name=extension_name,
            latest_version_number=latest_version_number,
            parameters=parameters,
        )

        return typing.cast(None, jsii.invoke(self, "preCreateHostedConfigurationVersion", [event_destination, options]))

    @jsii.member(jsii_name="preStartDeployment")
    def pre_start_deployment(
        self,
        event_destination: IEventDestination,
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence[Parameter]] = None,
    ) -> None:
        '''Adds a PRE_START_DEPLOYMENT extension with the provided event destination and also creates an extension association to the configuration profile.

        :param event_destination: The event that occurs during the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f65a8de4cec461bba4019fd73ca34ff5fcaf12f9911f7d1bea01ee3e18caf136)
            check_type(argname="argument event_destination", value=event_destination, expected_type=type_hints["event_destination"])
        options = ExtensionOptions(
            description=description,
            extension_name=extension_name,
            latest_version_number=latest_version_number,
            parameters=parameters,
        )

        return typing.cast(None, jsii.invoke(self, "preStartDeployment", [event_destination, options]))

    @builtins.property
    @jsii.member(jsii_name="application")
    def application(self) -> IApplication:
        '''The application associated with the configuration.'''
        return typing.cast(IApplication, jsii.get(self, "application"))

    @builtins.property
    @jsii.member(jsii_name="configurationProfileArn")
    def configuration_profile_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the configuration profile.'''
        return typing.cast(builtins.str, jsii.get(self, "configurationProfileArn"))

    @builtins.property
    @jsii.member(jsii_name="configurationProfileId")
    def configuration_profile_id(self) -> builtins.str:
        '''The ID of the configuration profile.'''
        return typing.cast(builtins.str, jsii.get(self, "configurationProfileId"))

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> ConfigurationSource:
        '''The location where the configuration is stored.'''
        return typing.cast(ConfigurationSource, jsii.get(self, "location"))

    @builtins.property
    @jsii.member(jsii_name="deploymentKey")
    def deployment_key(self) -> typing.Optional[_IKey_5f11635f]:
        '''The deployment key for the configuration.'''
        return typing.cast(typing.Optional[_IKey_5f11635f], jsii.get(self, "deploymentKey"))

    @builtins.property
    @jsii.member(jsii_name="deploymentStrategy")
    def deployment_strategy(self) -> typing.Optional[IDeploymentStrategy]:
        '''The deployment strategy for the configuration.'''
        return typing.cast(typing.Optional[IDeploymentStrategy], jsii.get(self, "deploymentStrategy"))

    @builtins.property
    @jsii.member(jsii_name="deployTo")
    def deploy_to(self) -> typing.Optional[typing.List[IEnvironment]]:
        '''The environments to deploy to.'''
        return typing.cast(typing.Optional[typing.List[IEnvironment]], jsii.get(self, "deployTo"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the configuration.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the configuration.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="retrievalRole")
    def retrieval_role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''The IAM role to retrieve the configuration.'''
        return typing.cast(typing.Optional[_IRole_235f5d8e], jsii.get(self, "retrievalRole"))

    @builtins.property
    @jsii.member(jsii_name="sourceKey")
    def source_key(self) -> typing.Optional[_IKey_5f11635f]:
        '''The key to decrypt the configuration if applicable.

        This key
        can be used when storing configuration in AWS Secrets Manager, Systems Manager Parameter Store,
        or Amazon S3.
        '''
        return typing.cast(typing.Optional[_IKey_5f11635f], jsii.get(self, "sourceKey"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> typing.Optional[ConfigurationType]:
        '''The configuration type.'''
        return typing.cast(typing.Optional[ConfigurationType], jsii.get(self, "type"))

    @builtins.property
    @jsii.member(jsii_name="validators")
    def validators(self) -> typing.Optional[typing.List[IValidator]]:
        '''The validators for the configuration.'''
        return typing.cast(typing.Optional[typing.List[IValidator]], jsii.get(self, "validators"))

    @builtins.property
    @jsii.member(jsii_name="versionNumber")
    def version_number(self) -> typing.Optional[builtins.str]:
        '''The version number of the configuration to deploy.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionNumber"))

    @builtins.property
    @jsii.member(jsii_name="applicationId")
    def _application_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "applicationId"))

    @_application_id.setter
    def _application_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0e9989f54c29397e556923d6dc5808d84cb6c3a5de0ea3c83ce4461584c451e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationId", value)

    @builtins.property
    @jsii.member(jsii_name="extensible")
    def _extensible(self) -> "ExtensibleBase":
        return typing.cast("ExtensibleBase", jsii.get(self, "extensible"))

    @_extensible.setter
    def _extensible(self, value: "ExtensibleBase") -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af782e66a589643c3273915140536d8c7931cca7f2adf6a0fc45e67b9228eebf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "extensible", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appconfig.SourcedConfigurationOptions",
    jsii_struct_bases=[ConfigurationOptions],
    name_mapping={
        "deployment_key": "deploymentKey",
        "deployment_strategy": "deploymentStrategy",
        "deploy_to": "deployTo",
        "description": "description",
        "name": "name",
        "type": "type",
        "validators": "validators",
        "location": "location",
        "retrieval_role": "retrievalRole",
        "version_number": "versionNumber",
    },
)
class SourcedConfigurationOptions(ConfigurationOptions):
    def __init__(
        self,
        *,
        deployment_key: typing.Optional[_IKey_5f11635f] = None,
        deployment_strategy: typing.Optional[IDeploymentStrategy] = None,
        deploy_to: typing.Optional[typing.Sequence[IEnvironment]] = None,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        type: typing.Optional[ConfigurationType] = None,
        validators: typing.Optional[typing.Sequence[IValidator]] = None,
        location: ConfigurationSource,
        retrieval_role: typing.Optional[_IRole_235f5d8e] = None,
        version_number: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Options for SourcedConfiguration.

        :param deployment_key: The deployment key of the configuration. Default: - None.
        :param deployment_strategy: The deployment strategy for the configuration. Default: - A deployment strategy with the rollout strategy set to RolloutStrategy.CANARY_10_PERCENT_20_MINUTES
        :param deploy_to: The list of environments to deploy the configuration to. If this parameter is not specified, then there will be no deployment created alongside this configuration. Deployments can be added later using the ``IEnvironment.addDeployment`` or ``IEnvironment.addDeployments`` methods. Default: - None.
        :param description: The description of the configuration. Default: - No description.
        :param name: The name of the configuration. Default: - A name is generated.
        :param type: The type of configuration. Default: ConfigurationType.FREEFORM
        :param validators: The validators for the configuration. Default: - No validators.
        :param location: The location where the configuration is stored.
        :param retrieval_role: The IAM role to retrieve the configuration. Default: - A role is generated.
        :param version_number: The version number of the sourced configuration to deploy. If this is not specified, then there will be no deployment. Default: - None.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appconfig as appconfig
            from aws_cdk import aws_iam as iam
            from aws_cdk import aws_kms as kms
            
            # configuration_source: appconfig.ConfigurationSource
            # deployment_strategy: appconfig.DeploymentStrategy
            # environment: appconfig.Environment
            # key: kms.Key
            # role: iam.Role
            # validator: appconfig.IValidator
            
            sourced_configuration_options = appconfig.SourcedConfigurationOptions(
                location=configuration_source,
            
                # the properties below are optional
                deployment_key=key,
                deployment_strategy=deployment_strategy,
                deploy_to=[environment],
                description="description",
                name="name",
                retrieval_role=role,
                type=appconfig.ConfigurationType.FREEFORM,
                validators=[validator],
                version_number="versionNumber"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__115deabe7a02ce295c431e7d9a99bcbe112bc017436380d80181c5db491187a1)
            check_type(argname="argument deployment_key", value=deployment_key, expected_type=type_hints["deployment_key"])
            check_type(argname="argument deployment_strategy", value=deployment_strategy, expected_type=type_hints["deployment_strategy"])
            check_type(argname="argument deploy_to", value=deploy_to, expected_type=type_hints["deploy_to"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument validators", value=validators, expected_type=type_hints["validators"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument retrieval_role", value=retrieval_role, expected_type=type_hints["retrieval_role"])
            check_type(argname="argument version_number", value=version_number, expected_type=type_hints["version_number"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "location": location,
        }
        if deployment_key is not None:
            self._values["deployment_key"] = deployment_key
        if deployment_strategy is not None:
            self._values["deployment_strategy"] = deployment_strategy
        if deploy_to is not None:
            self._values["deploy_to"] = deploy_to
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name
        if type is not None:
            self._values["type"] = type
        if validators is not None:
            self._values["validators"] = validators
        if retrieval_role is not None:
            self._values["retrieval_role"] = retrieval_role
        if version_number is not None:
            self._values["version_number"] = version_number

    @builtins.property
    def deployment_key(self) -> typing.Optional[_IKey_5f11635f]:
        '''The deployment key of the configuration.

        :default: - None.
        '''
        result = self._values.get("deployment_key")
        return typing.cast(typing.Optional[_IKey_5f11635f], result)

    @builtins.property
    def deployment_strategy(self) -> typing.Optional[IDeploymentStrategy]:
        '''The deployment strategy for the configuration.

        :default:

        - A deployment strategy with the rollout strategy set to
        RolloutStrategy.CANARY_10_PERCENT_20_MINUTES
        '''
        result = self._values.get("deployment_strategy")
        return typing.cast(typing.Optional[IDeploymentStrategy], result)

    @builtins.property
    def deploy_to(self) -> typing.Optional[typing.List[IEnvironment]]:
        '''The list of environments to deploy the configuration to.

        If this parameter is not specified, then there will be no
        deployment created alongside this configuration.

        Deployments can be added later using the ``IEnvironment.addDeployment`` or
        ``IEnvironment.addDeployments`` methods.

        :default: - None.
        '''
        result = self._values.get("deploy_to")
        return typing.cast(typing.Optional[typing.List[IEnvironment]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the configuration.

        :default: - No description.
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the configuration.

        :default: - A name is generated.
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[ConfigurationType]:
        '''The type of configuration.

        :default: ConfigurationType.FREEFORM
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[ConfigurationType], result)

    @builtins.property
    def validators(self) -> typing.Optional[typing.List[IValidator]]:
        '''The validators for the configuration.

        :default: - No validators.
        '''
        result = self._values.get("validators")
        return typing.cast(typing.Optional[typing.List[IValidator]], result)

    @builtins.property
    def location(self) -> ConfigurationSource:
        '''The location where the configuration is stored.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(ConfigurationSource, result)

    @builtins.property
    def retrieval_role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''The IAM role to retrieve the configuration.

        :default: - A role is generated.
        '''
        result = self._values.get("retrieval_role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    @builtins.property
    def version_number(self) -> typing.Optional[builtins.str]:
        '''The version number of the sourced configuration to deploy.

        If this is not specified,
        then there will be no deployment.

        :default: - None.
        '''
        result = self._values.get("version_number")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SourcedConfigurationOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appconfig.SourcedConfigurationProps",
    jsii_struct_bases=[ConfigurationProps],
    name_mapping={
        "deployment_key": "deploymentKey",
        "deployment_strategy": "deploymentStrategy",
        "deploy_to": "deployTo",
        "description": "description",
        "name": "name",
        "type": "type",
        "validators": "validators",
        "application": "application",
        "location": "location",
        "retrieval_role": "retrievalRole",
        "version_number": "versionNumber",
    },
)
class SourcedConfigurationProps(ConfigurationProps):
    def __init__(
        self,
        *,
        deployment_key: typing.Optional[_IKey_5f11635f] = None,
        deployment_strategy: typing.Optional[IDeploymentStrategy] = None,
        deploy_to: typing.Optional[typing.Sequence[IEnvironment]] = None,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        type: typing.Optional[ConfigurationType] = None,
        validators: typing.Optional[typing.Sequence[IValidator]] = None,
        application: IApplication,
        location: ConfigurationSource,
        retrieval_role: typing.Optional[_IRole_235f5d8e] = None,
        version_number: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for SourcedConfiguration.

        :param deployment_key: The deployment key of the configuration. Default: - None.
        :param deployment_strategy: The deployment strategy for the configuration. Default: - A deployment strategy with the rollout strategy set to RolloutStrategy.CANARY_10_PERCENT_20_MINUTES
        :param deploy_to: The list of environments to deploy the configuration to. If this parameter is not specified, then there will be no deployment created alongside this configuration. Deployments can be added later using the ``IEnvironment.addDeployment`` or ``IEnvironment.addDeployments`` methods. Default: - None.
        :param description: The description of the configuration. Default: - No description.
        :param name: The name of the configuration. Default: - A name is generated.
        :param type: The type of configuration. Default: ConfigurationType.FREEFORM
        :param validators: The validators for the configuration. Default: - No validators.
        :param application: The application associated with the configuration.
        :param location: The location where the configuration is stored.
        :param retrieval_role: The IAM role to retrieve the configuration. Default: - A role is generated.
        :param version_number: The version number of the sourced configuration to deploy. If this is not specified, then there will be no deployment. Default: - None.

        :exampleMetadata: infused

        Example::

            # application: appconfig.Application
            # bucket: s3.Bucket
            
            
            appconfig.SourcedConfiguration(self, "MySourcedConfiguration",
                application=application,
                location=appconfig.ConfigurationSource.from_bucket(bucket, "path/to/file.json"),
                type=appconfig.ConfigurationType.FEATURE_FLAGS,
                name="MyConfig",
                description="This is my sourced configuration from CDK."
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d41101d1b0f699a52d44a2b86fe3e9dcd0e6f1487f088908464eb49cb3e5e12c)
            check_type(argname="argument deployment_key", value=deployment_key, expected_type=type_hints["deployment_key"])
            check_type(argname="argument deployment_strategy", value=deployment_strategy, expected_type=type_hints["deployment_strategy"])
            check_type(argname="argument deploy_to", value=deploy_to, expected_type=type_hints["deploy_to"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument validators", value=validators, expected_type=type_hints["validators"])
            check_type(argname="argument application", value=application, expected_type=type_hints["application"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument retrieval_role", value=retrieval_role, expected_type=type_hints["retrieval_role"])
            check_type(argname="argument version_number", value=version_number, expected_type=type_hints["version_number"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application": application,
            "location": location,
        }
        if deployment_key is not None:
            self._values["deployment_key"] = deployment_key
        if deployment_strategy is not None:
            self._values["deployment_strategy"] = deployment_strategy
        if deploy_to is not None:
            self._values["deploy_to"] = deploy_to
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name
        if type is not None:
            self._values["type"] = type
        if validators is not None:
            self._values["validators"] = validators
        if retrieval_role is not None:
            self._values["retrieval_role"] = retrieval_role
        if version_number is not None:
            self._values["version_number"] = version_number

    @builtins.property
    def deployment_key(self) -> typing.Optional[_IKey_5f11635f]:
        '''The deployment key of the configuration.

        :default: - None.
        '''
        result = self._values.get("deployment_key")
        return typing.cast(typing.Optional[_IKey_5f11635f], result)

    @builtins.property
    def deployment_strategy(self) -> typing.Optional[IDeploymentStrategy]:
        '''The deployment strategy for the configuration.

        :default:

        - A deployment strategy with the rollout strategy set to
        RolloutStrategy.CANARY_10_PERCENT_20_MINUTES
        '''
        result = self._values.get("deployment_strategy")
        return typing.cast(typing.Optional[IDeploymentStrategy], result)

    @builtins.property
    def deploy_to(self) -> typing.Optional[typing.List[IEnvironment]]:
        '''The list of environments to deploy the configuration to.

        If this parameter is not specified, then there will be no
        deployment created alongside this configuration.

        Deployments can be added later using the ``IEnvironment.addDeployment`` or
        ``IEnvironment.addDeployments`` methods.

        :default: - None.
        '''
        result = self._values.get("deploy_to")
        return typing.cast(typing.Optional[typing.List[IEnvironment]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the configuration.

        :default: - No description.
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the configuration.

        :default: - A name is generated.
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[ConfigurationType]:
        '''The type of configuration.

        :default: ConfigurationType.FREEFORM
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[ConfigurationType], result)

    @builtins.property
    def validators(self) -> typing.Optional[typing.List[IValidator]]:
        '''The validators for the configuration.

        :default: - No validators.
        '''
        result = self._values.get("validators")
        return typing.cast(typing.Optional[typing.List[IValidator]], result)

    @builtins.property
    def application(self) -> IApplication:
        '''The application associated with the configuration.'''
        result = self._values.get("application")
        assert result is not None, "Required property 'application' is missing"
        return typing.cast(IApplication, result)

    @builtins.property
    def location(self) -> ConfigurationSource:
        '''The location where the configuration is stored.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(ConfigurationSource, result)

    @builtins.property
    def retrieval_role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''The IAM role to retrieve the configuration.

        :default: - A role is generated.
        '''
        result = self._values.get("retrieval_role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    @builtins.property
    def version_number(self) -> typing.Optional[builtins.str]:
        '''The version number of the sourced configuration to deploy.

        If this is not specified,
        then there will be no deployment.

        :default: - None.
        '''
        result = self._values.get("version_number")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SourcedConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IEventDestination)
class SqsDestination(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appconfig.SqsDestination",
):
    '''Use an Amazon SQS queue as an event destination.

    :exampleMetadata: infused

    Example::

        # queue: sqs.Queue
        
        
        appconfig.Extension(self, "MyExtension",
            actions=[
                appconfig.Action(
                    action_points=[appconfig.ActionPoint.ON_DEPLOYMENT_START],
                    event_destination=appconfig.SqsDestination(queue)
                )
            ]
        )
    '''

    def __init__(self, queue: _IQueue_7ed6f679) -> None:
        '''
        :param queue: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c28280d4c69ff29c8717c5fad93f2870bc55344bfbee733f6c2105ed3497ab5b)
            check_type(argname="argument queue", value=queue, expected_type=type_hints["queue"])
        jsii.create(self.__class__, self, [queue])

    @builtins.property
    @jsii.member(jsii_name="extensionUri")
    def extension_uri(self) -> builtins.str:
        '''The URI of the extension event destination.'''
        return typing.cast(builtins.str, jsii.get(self, "extensionUri"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> SourceType:
        '''The type of the extension event destination.'''
        return typing.cast(SourceType, jsii.get(self, "type"))

    @builtins.property
    @jsii.member(jsii_name="policyDocument")
    def policy_document(self) -> typing.Optional[_PolicyDocument_3ac34393]:
        '''The IAM policy document to invoke the event destination.'''
        return typing.cast(typing.Optional[_PolicyDocument_3ac34393], jsii.get(self, "policyDocument"))


@jsii.enum(jsii_type="aws-cdk-lib.aws_appconfig.ValidatorType")
class ValidatorType(enum.Enum):
    '''The validator type.'''

    JSON_SCHEMA = "JSON_SCHEMA"
    '''JSON Scema validator.'''
    LAMBDA = "LAMBDA"
    '''Validate using a Lambda function.'''


@jsii.implements(IApplication, IExtensible)
class Application(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appconfig.Application",
):
    '''An AWS AppConfig application.

    :see: https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-application.html
    :resource: AWS::AppConfig::Application
    :exampleMetadata: infused

    Example::

        app = appconfig.Application(self, "MyApp")
        env = appconfig.Environment(self, "MyEnv",
            application=app
        )
        
        appconfig.HostedConfiguration(self, "MyHostedConfig",
            application=app,
            deploy_to=[env],
            content=appconfig.ConfigurationContent.from_inline_text("This is my configuration content.")
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        application_name: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param application_name: The name of the application. Default: - A name is generated.
        :param description: The description for the application. Default: - No description.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1e564dd652de62b6550596a7830dbc1244bd584b24647a457f2e0424816f76e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ApplicationProps(
            application_name=application_name, description=description
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="addAgentToEcs")
    @builtins.classmethod
    def add_agent_to_ecs(cls, task_def: _TaskDefinition_a541a103) -> None:
        '''Adds the AWS AppConfig Agent as a container to the provided ECS task definition.

        :param task_def: The ECS task definition [disable-awslint:ref-via-interface].
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18d0bc0084bf434e4353d076c6c6a72311baedc58526dd0fcd93d827e77fc2d9)
            check_type(argname="argument task_def", value=task_def, expected_type=type_hints["task_def"])
        return typing.cast(None, jsii.sinvoke(cls, "addAgentToEcs", [task_def]))

    @jsii.member(jsii_name="fromApplicationArn")
    @builtins.classmethod
    def from_application_arn(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        application_arn: builtins.str,
    ) -> IApplication:
        '''Imports an AWS AppConfig application into the CDK using its Amazon Resource Name (ARN).

        :param scope: The parent construct.
        :param id: The name of the application construct.
        :param application_arn: The Amazon Resource Name (ARN) of the application.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76e4fec3d46016fd59c8bd0733b8dac8db60ebadadc4e94e6bfb10742e1d7435)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument application_arn", value=application_arn, expected_type=type_hints["application_arn"])
        return typing.cast(IApplication, jsii.sinvoke(cls, "fromApplicationArn", [scope, id, application_arn]))

    @jsii.member(jsii_name="fromApplicationId")
    @builtins.classmethod
    def from_application_id(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        application_id: builtins.str,
    ) -> IApplication:
        '''Imports an AWS AppConfig application into the CDK using its ID.

        :param scope: The parent construct.
        :param id: The name of the application construct.
        :param application_id: The ID of the application.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3cdd944facfa98bfbfbebc6eb2e937c4f847d03f65d52d4a9068926fe2c93f61)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument application_id", value=application_id, expected_type=type_hints["application_id"])
        return typing.cast(IApplication, jsii.sinvoke(cls, "fromApplicationId", [scope, id, application_id]))

    @jsii.member(jsii_name="getLambdaLayerVersionArn")
    @builtins.classmethod
    def get_lambda_layer_version_arn(
        cls,
        region: builtins.str,
        platform: typing.Optional[Platform] = None,
    ) -> builtins.str:
        '''Retrieves the Lambda layer version Amazon Resource Name (ARN) for the AWS AppConfig Lambda extension.

        :param region: The region for the Lambda layer (for example, 'us-east-1').
        :param platform: The platform for the Lambda layer (default is Platform.X86_64).

        :return: Lambda layer version ARN
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f23af9ea4630280fc41549b208a41050e1d321a3300899bad1754e76fac80c00)
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument platform", value=platform, expected_type=type_hints["platform"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "getLambdaLayerVersionArn", [region, platform]))

    @jsii.member(jsii_name="addEnvironment")
    def add_environment(
        self,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        environment_name: typing.Optional[builtins.str] = None,
        monitors: typing.Optional[typing.Sequence[Monitor]] = None,
    ) -> IEnvironment:
        '''Adds an environment.

        :param id: -
        :param description: The description of the environment. Default: - No description.
        :param environment_name: The name of the environment. Default: - A name is generated.
        :param monitors: The monitors for the environment. Default: - No monitors.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fbd38f9aba7df4d45f96d0029239a2f96f2fcad218a295b86c260e75cde6f20a)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = EnvironmentOptions(
            description=description,
            environment_name=environment_name,
            monitors=monitors,
        )

        return typing.cast(IEnvironment, jsii.invoke(self, "addEnvironment", [id, options]))

    @jsii.member(jsii_name="addExistingEnvironment")
    def add_existing_environment(self, environment: IEnvironment) -> None:
        '''Adds an existing environment.

        :param environment: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__16233ddf7a1e42dc23f4bda96b70ec9417da6d3fedfafeec39f99b911d35656e)
            check_type(argname="argument environment", value=environment, expected_type=type_hints["environment"])
        return typing.cast(None, jsii.invoke(self, "addExistingEnvironment", [environment]))

    @jsii.member(jsii_name="addExtension")
    def add_extension(self, extension: IExtension) -> None:
        '''Adds an extension association to the application.

        :param extension: The extension to create an association for.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97553b8fa0201fc58b21e96c914a619a1f6afeeb493a7ec1e67046be7d15a722)
            check_type(argname="argument extension", value=extension, expected_type=type_hints["extension"])
        return typing.cast(None, jsii.invoke(self, "addExtension", [extension]))

    @jsii.member(jsii_name="addHostedConfiguration")
    def add_hosted_configuration(
        self,
        id: builtins.str,
        *,
        content: ConfigurationContent,
        latest_version_number: typing.Optional[jsii.Number] = None,
        version_label: typing.Optional[builtins.str] = None,
        deployment_key: typing.Optional[_IKey_5f11635f] = None,
        deployment_strategy: typing.Optional[IDeploymentStrategy] = None,
        deploy_to: typing.Optional[typing.Sequence[IEnvironment]] = None,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        type: typing.Optional[ConfigurationType] = None,
        validators: typing.Optional[typing.Sequence[IValidator]] = None,
    ) -> "HostedConfiguration":
        '''Adds a hosted configuration.

        :param id: -
        :param content: The content of the hosted configuration.
        :param latest_version_number: The latest version number of the hosted configuration. Default: - None.
        :param version_label: The version label of the hosted configuration. Default: - None.
        :param deployment_key: The deployment key of the configuration. Default: - None.
        :param deployment_strategy: The deployment strategy for the configuration. Default: - A deployment strategy with the rollout strategy set to RolloutStrategy.CANARY_10_PERCENT_20_MINUTES
        :param deploy_to: The list of environments to deploy the configuration to. If this parameter is not specified, then there will be no deployment created alongside this configuration. Deployments can be added later using the ``IEnvironment.addDeployment`` or ``IEnvironment.addDeployments`` methods. Default: - None.
        :param description: The description of the configuration. Default: - No description.
        :param name: The name of the configuration. Default: - A name is generated.
        :param type: The type of configuration. Default: ConfigurationType.FREEFORM
        :param validators: The validators for the configuration. Default: - No validators.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b18310538532e3e3e53af99bb5da0c248186673a38a5175633a0149cf8ae0af)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = HostedConfigurationOptions(
            content=content,
            latest_version_number=latest_version_number,
            version_label=version_label,
            deployment_key=deployment_key,
            deployment_strategy=deployment_strategy,
            deploy_to=deploy_to,
            description=description,
            name=name,
            type=type,
            validators=validators,
        )

        return typing.cast("HostedConfiguration", jsii.invoke(self, "addHostedConfiguration", [id, options]))

    @jsii.member(jsii_name="addSourcedConfiguration")
    def add_sourced_configuration(
        self,
        id: builtins.str,
        *,
        location: ConfigurationSource,
        retrieval_role: typing.Optional[_IRole_235f5d8e] = None,
        version_number: typing.Optional[builtins.str] = None,
        deployment_key: typing.Optional[_IKey_5f11635f] = None,
        deployment_strategy: typing.Optional[IDeploymentStrategy] = None,
        deploy_to: typing.Optional[typing.Sequence[IEnvironment]] = None,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        type: typing.Optional[ConfigurationType] = None,
        validators: typing.Optional[typing.Sequence[IValidator]] = None,
    ) -> SourcedConfiguration:
        '''Adds a sourced configuration.

        :param id: -
        :param location: The location where the configuration is stored.
        :param retrieval_role: The IAM role to retrieve the configuration. Default: - A role is generated.
        :param version_number: The version number of the sourced configuration to deploy. If this is not specified, then there will be no deployment. Default: - None.
        :param deployment_key: The deployment key of the configuration. Default: - None.
        :param deployment_strategy: The deployment strategy for the configuration. Default: - A deployment strategy with the rollout strategy set to RolloutStrategy.CANARY_10_PERCENT_20_MINUTES
        :param deploy_to: The list of environments to deploy the configuration to. If this parameter is not specified, then there will be no deployment created alongside this configuration. Deployments can be added later using the ``IEnvironment.addDeployment`` or ``IEnvironment.addDeployments`` methods. Default: - None.
        :param description: The description of the configuration. Default: - No description.
        :param name: The name of the configuration. Default: - A name is generated.
        :param type: The type of configuration. Default: ConfigurationType.FREEFORM
        :param validators: The validators for the configuration. Default: - No validators.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c0399b30aac3a09a4a5e9f3f33f358c90afa60099a7dd6cfc1f1b40ff373215)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = SourcedConfigurationOptions(
            location=location,
            retrieval_role=retrieval_role,
            version_number=version_number,
            deployment_key=deployment_key,
            deployment_strategy=deployment_strategy,
            deploy_to=deploy_to,
            description=description,
            name=name,
            type=type,
            validators=validators,
        )

        return typing.cast(SourcedConfiguration, jsii.invoke(self, "addSourcedConfiguration", [id, options]))

    @jsii.member(jsii_name="environments")
    def environments(self) -> typing.List[IEnvironment]:
        '''Returns the list of associated environments.'''
        return typing.cast(typing.List[IEnvironment], jsii.invoke(self, "environments", []))

    @jsii.member(jsii_name="on")
    def on(
        self,
        action_point: ActionPoint,
        event_destination: IEventDestination,
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence[Parameter]] = None,
    ) -> None:
        '''Adds an extension defined by the action point and event destination and also creates an extension association to an application.

        :param action_point: The action point which triggers the event.
        :param event_destination: The event that occurs during the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__727774ca5ea7bba2fa87dc8ad6f91306047bf14b07d86949cc12510628c56ec2)
            check_type(argname="argument action_point", value=action_point, expected_type=type_hints["action_point"])
            check_type(argname="argument event_destination", value=event_destination, expected_type=type_hints["event_destination"])
        options = ExtensionOptions(
            description=description,
            extension_name=extension_name,
            latest_version_number=latest_version_number,
            parameters=parameters,
        )

        return typing.cast(None, jsii.invoke(self, "on", [action_point, event_destination, options]))

    @jsii.member(jsii_name="onDeploymentBaking")
    def on_deployment_baking(
        self,
        event_destination: IEventDestination,
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence[Parameter]] = None,
    ) -> None:
        '''Adds an ON_DEPLOYMENT_BAKING extension with the provided event destination and also creates an extension association to an application.

        :param event_destination: The event that occurs during the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__134b1acb6af5ac0c469c09cb9c572fc82e8a942398a4c09aa8f2c8b97953aa12)
            check_type(argname="argument event_destination", value=event_destination, expected_type=type_hints["event_destination"])
        options = ExtensionOptions(
            description=description,
            extension_name=extension_name,
            latest_version_number=latest_version_number,
            parameters=parameters,
        )

        return typing.cast(None, jsii.invoke(self, "onDeploymentBaking", [event_destination, options]))

    @jsii.member(jsii_name="onDeploymentComplete")
    def on_deployment_complete(
        self,
        event_destination: IEventDestination,
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence[Parameter]] = None,
    ) -> None:
        '''Adds an ON_DEPLOYMENT_COMPLETE extension with the provided event destination and also creates an extension association to an application.

        :param event_destination: The event that occurs during the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43cf11a606f3bce0aaad5e1befddf0a9458ad3ff320049d375379fbbd55e106e)
            check_type(argname="argument event_destination", value=event_destination, expected_type=type_hints["event_destination"])
        options = ExtensionOptions(
            description=description,
            extension_name=extension_name,
            latest_version_number=latest_version_number,
            parameters=parameters,
        )

        return typing.cast(None, jsii.invoke(self, "onDeploymentComplete", [event_destination, options]))

    @jsii.member(jsii_name="onDeploymentRolledBack")
    def on_deployment_rolled_back(
        self,
        event_destination: IEventDestination,
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence[Parameter]] = None,
    ) -> None:
        '''Adds an ON_DEPLOYMENT_ROLLED_BACK extension with the provided event destination and also creates an extension association to an application.

        :param event_destination: The event that occurs during the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e75df1a62410c2ab540f65a3a2294952a49aac8ea5def188ee109a52eb3d3ff)
            check_type(argname="argument event_destination", value=event_destination, expected_type=type_hints["event_destination"])
        options = ExtensionOptions(
            description=description,
            extension_name=extension_name,
            latest_version_number=latest_version_number,
            parameters=parameters,
        )

        return typing.cast(None, jsii.invoke(self, "onDeploymentRolledBack", [event_destination, options]))

    @jsii.member(jsii_name="onDeploymentStart")
    def on_deployment_start(
        self,
        event_destination: IEventDestination,
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence[Parameter]] = None,
    ) -> None:
        '''Adds an ON_DEPLOYMENT_START extension with the provided event destination and also creates an extension association to an application.

        :param event_destination: The event that occurs during the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af4fa8c37c6e1a14ec8b5a2243b1f62d1182e4551cd8d7247c737964514b946f)
            check_type(argname="argument event_destination", value=event_destination, expected_type=type_hints["event_destination"])
        options = ExtensionOptions(
            description=description,
            extension_name=extension_name,
            latest_version_number=latest_version_number,
            parameters=parameters,
        )

        return typing.cast(None, jsii.invoke(self, "onDeploymentStart", [event_destination, options]))

    @jsii.member(jsii_name="onDeploymentStep")
    def on_deployment_step(
        self,
        event_destination: IEventDestination,
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence[Parameter]] = None,
    ) -> None:
        '''Adds an ON_DEPLOYMENT_STEP extension with the provided event destination and also creates an extension association to an application.

        :param event_destination: The event that occurs during the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20656d70f751052e70a657c2ab0b4d42341ae80f5507359b32d99b7e89e6b5a4)
            check_type(argname="argument event_destination", value=event_destination, expected_type=type_hints["event_destination"])
        options = ExtensionOptions(
            description=description,
            extension_name=extension_name,
            latest_version_number=latest_version_number,
            parameters=parameters,
        )

        return typing.cast(None, jsii.invoke(self, "onDeploymentStep", [event_destination, options]))

    @jsii.member(jsii_name="preCreateHostedConfigurationVersion")
    def pre_create_hosted_configuration_version(
        self,
        event_destination: IEventDestination,
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence[Parameter]] = None,
    ) -> None:
        '''Adds a PRE_CREATE_HOSTED_CONFIGURATION_VERSION extension with the provided event destination and also creates an extension association to an application.

        :param event_destination: The event that occurs during the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__299d964c2aac2516ce8b1125bb695b718f5f425a8b70c26c082dff2413b12032)
            check_type(argname="argument event_destination", value=event_destination, expected_type=type_hints["event_destination"])
        options = ExtensionOptions(
            description=description,
            extension_name=extension_name,
            latest_version_number=latest_version_number,
            parameters=parameters,
        )

        return typing.cast(None, jsii.invoke(self, "preCreateHostedConfigurationVersion", [event_destination, options]))

    @jsii.member(jsii_name="preStartDeployment")
    def pre_start_deployment(
        self,
        event_destination: IEventDestination,
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence[Parameter]] = None,
    ) -> None:
        '''Adds a PRE_START_DEPLOYMENT extension with the provided event destination and also creates an extension association to an application.

        :param event_destination: The event that occurs during the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af63cf64ce7c3fe83523222dceaef56e9447ce8f6a2afb5d2567c6c9792f3543)
            check_type(argname="argument event_destination", value=event_destination, expected_type=type_hints["event_destination"])
        options = ExtensionOptions(
            description=description,
            extension_name=extension_name,
            latest_version_number=latest_version_number,
            parameters=parameters,
        )

        return typing.cast(None, jsii.invoke(self, "preStartDeployment", [event_destination, options]))

    @builtins.property
    @jsii.member(jsii_name="applicationArn")
    def application_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the application.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "applicationArn"))

    @builtins.property
    @jsii.member(jsii_name="applicationId")
    def application_id(self) -> builtins.str:
        '''The ID of the application.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "applicationId"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the application.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the application.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="extensible")
    def _extensible(self) -> "ExtensibleBase":
        return typing.cast("ExtensibleBase", jsii.get(self, "extensible"))

    @_extensible.setter
    def _extensible(self, value: "ExtensibleBase") -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82766fd65d19c222e55a3bd3d37a0ce2dbc32473446dfef2bbba053456f75dd9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "extensible", value)


@jsii.implements(IDeploymentStrategy)
class DeploymentStrategy(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appconfig.DeploymentStrategy",
):
    '''An AWS AppConfig deployment strategy.

    :see: https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-deployment-strategy.html
    :resource: AWS::AppConfig::DeploymentStrategy
    :exampleMetadata: infused

    Example::

        appconfig.DeploymentStrategy(self, "MyDeploymentStrategy",
            rollout_strategy=appconfig.RolloutStrategy.linear(
                growth_factor=20,
                deployment_duration=Duration.minutes(30),
                final_bake_time=Duration.minutes(30)
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        rollout_strategy: RolloutStrategy,
        deployment_strategy_name: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param rollout_strategy: The rollout strategy for the deployment strategy. You can use predefined deployment strategies, such as RolloutStrategy.ALL_AT_ONCE, RolloutStrategy.LINEAR_50_PERCENT_EVERY_30_SECONDS, or RolloutStrategy.CANARY_10_PERCENT_20_MINUTES.
        :param deployment_strategy_name: A name for the deployment strategy. Default: - A name is generated.
        :param description: A description of the deployment strategy. Default: - No description.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__355f732c5b86477a8c74b5d90e398dea8eb36c47e6f7eb1df2958e42495a6598)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = DeploymentStrategyProps(
            rollout_strategy=rollout_strategy,
            deployment_strategy_name=deployment_strategy_name,
            description=description,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromDeploymentStrategyArn")
    @builtins.classmethod
    def from_deployment_strategy_arn(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        deployment_strategy_arn: builtins.str,
    ) -> IDeploymentStrategy:
        '''Imports a deployment strategy into the CDK using its Amazon Resource Name (ARN).

        :param scope: The parent construct.
        :param id: The name of the deployment strategy construct.
        :param deployment_strategy_arn: The Amazon Resource Name (ARN) of the deployment strategy.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b37d45983b2147369edbbbb7365fa518ba24fcce4bb42681de698092ccc6be4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument deployment_strategy_arn", value=deployment_strategy_arn, expected_type=type_hints["deployment_strategy_arn"])
        return typing.cast(IDeploymentStrategy, jsii.sinvoke(cls, "fromDeploymentStrategyArn", [scope, id, deployment_strategy_arn]))

    @jsii.member(jsii_name="fromDeploymentStrategyId")
    @builtins.classmethod
    def from_deployment_strategy_id(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        deployment_strategy_id: DeploymentStrategyId,
    ) -> IDeploymentStrategy:
        '''Imports a deployment strategy into the CDK using its ID.

        :param scope: The parent construct.
        :param id: The name of the deployment strategy construct.
        :param deployment_strategy_id: The ID of the deployment strategy.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75327d45b26489bd7407fafc6ad0df26d223ce07225e44f5e5383facc04fcf58)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument deployment_strategy_id", value=deployment_strategy_id, expected_type=type_hints["deployment_strategy_id"])
        return typing.cast(IDeploymentStrategy, jsii.sinvoke(cls, "fromDeploymentStrategyId", [scope, id, deployment_strategy_id]))

    @builtins.property
    @jsii.member(jsii_name="deploymentStrategyArn")
    def deployment_strategy_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the deployment strategy.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "deploymentStrategyArn"))

    @builtins.property
    @jsii.member(jsii_name="deploymentStrategyId")
    def deployment_strategy_id(self) -> builtins.str:
        '''The ID of the deployment strategy.'''
        return typing.cast(builtins.str, jsii.get(self, "deploymentStrategyId"))

    @builtins.property
    @jsii.member(jsii_name="deploymentDurationInMinutes")
    def deployment_duration_in_minutes(self) -> typing.Optional[jsii.Number]:
        '''The deployment duration in minutes of the deployment strategy.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "deploymentDurationInMinutes"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the deployment strategy.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @builtins.property
    @jsii.member(jsii_name="finalBakeTimeInMinutes")
    def final_bake_time_in_minutes(self) -> typing.Optional[jsii.Number]:
        '''The final bake time in minutes of the deployment strategy.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "finalBakeTimeInMinutes"))

    @builtins.property
    @jsii.member(jsii_name="growthFactor")
    def growth_factor(self) -> typing.Optional[jsii.Number]:
        '''The growth factor of the deployment strategy.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "growthFactor"))

    @builtins.property
    @jsii.member(jsii_name="growthType")
    def growth_type(self) -> typing.Optional[GrowthType]:
        '''The growth type of the deployment strategy.'''
        return typing.cast(typing.Optional[GrowthType], jsii.get(self, "growthType"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the deployment strategy.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))


@jsii.implements(IEnvironment, IExtensible)
class Environment(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appconfig.Environment",
):
    '''An AWS AppConfig environment.

    :see: https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-environment.html
    :resource: AWS::AppConfig::Environment
    :exampleMetadata: infused

    Example::

        app = appconfig.Application(self, "MyApp")
        env = appconfig.Environment(self, "MyEnv",
            application=app
        )
        
        appconfig.HostedConfiguration(self, "MyFirstHostedConfig",
            application=app,
            deploy_to=[env],
            content=appconfig.ConfigurationContent.from_inline_text("This is my first configuration content.")
        )
        
        appconfig.HostedConfiguration(self, "MySecondHostedConfig",
            application=app,
            deploy_to=[env],
            content=appconfig.ConfigurationContent.from_inline_text("This is my second configuration content.")
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        application: IApplication,
        description: typing.Optional[builtins.str] = None,
        environment_name: typing.Optional[builtins.str] = None,
        monitors: typing.Optional[typing.Sequence[Monitor]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param application: The application to be associated with the environment.
        :param description: The description of the environment. Default: - No description.
        :param environment_name: The name of the environment. Default: - A name is generated.
        :param monitors: The monitors for the environment. Default: - No monitors.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09c6baa2088c107dc1834ea8f2a8c0f35612bf3782c77c3ef6879f99339a8ca7)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = EnvironmentProps(
            application=application,
            description=description,
            environment_name=environment_name,
            monitors=monitors,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromEnvironmentArn")
    @builtins.classmethod
    def from_environment_arn(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        environment_arn: builtins.str,
    ) -> IEnvironment:
        '''Imports an environment into the CDK using its Amazon Resource Name (ARN).

        :param scope: The parent construct.
        :param id: The name of the environment construct.
        :param environment_arn: The Amazon Resource Name (ARN) of the environment.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85f387eeef7a94f96ab485e8173f4b432330c3d2f02329d4f772d886d0070f5a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument environment_arn", value=environment_arn, expected_type=type_hints["environment_arn"])
        return typing.cast(IEnvironment, jsii.sinvoke(cls, "fromEnvironmentArn", [scope, id, environment_arn]))

    @jsii.member(jsii_name="fromEnvironmentAttributes")
    @builtins.classmethod
    def from_environment_attributes(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        application: IApplication,
        environment_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        monitors: typing.Optional[typing.Sequence[Monitor]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> IEnvironment:
        '''Imports an environment into the CDK from its attributes.

        :param scope: The parent construct.
        :param id: The name of the environment construct.
        :param application: The application associated with the environment.
        :param environment_id: The ID of the environment.
        :param description: The description of the environment. Default: - None.
        :param monitors: The monitors for the environment. Default: - None.
        :param name: The name of the environment. Default: - None.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d0acdd2bc2062b1e3a3bcead8b9d2670bef03c315b3aa44522a2099520a2b48)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        attrs = EnvironmentAttributes(
            application=application,
            environment_id=environment_id,
            description=description,
            monitors=monitors,
            name=name,
        )

        return typing.cast(IEnvironment, jsii.sinvoke(cls, "fromEnvironmentAttributes", [scope, id, attrs]))

    @jsii.member(jsii_name="addDeployment")
    def add_deployment(self, configuration: IConfiguration) -> None:
        '''Creates a deployment of the supplied configuration to this environment.

        Note that you can only deploy one configuration at a time to an environment.
        However, you can deploy one configuration each to different environments at the same time.
        If more than one deployment is requested for this environment, they will occur in the same order they were provided.

        :param configuration: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60a6cee655356c4a43230057c8909db67a6239e7701192ff39fda6b5549a6672)
            check_type(argname="argument configuration", value=configuration, expected_type=type_hints["configuration"])
        return typing.cast(None, jsii.invoke(self, "addDeployment", [configuration]))

    @jsii.member(jsii_name="addDeployments")
    def add_deployments(self, *configurations: IConfiguration) -> None:
        '''Creates a deployment for each of the supplied configurations to this environment.

        These configurations will be deployed in the same order as the input array.

        :param configurations: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a87ca2c61c81bb433441138d696247c8865c67883b0937278f3b0aa320b5db0)
            check_type(argname="argument configurations", value=configurations, expected_type=typing.Tuple[type_hints["configurations"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "addDeployments", [*configurations]))

    @jsii.member(jsii_name="addExtension")
    def add_extension(self, extension: IExtension) -> None:
        '''Adds an extension association to the environment.

        :param extension: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__46eeb9c815b4c9f3f9ff6e64ae0bba20fa3057be7b74747b611ea672668a95cf)
            check_type(argname="argument extension", value=extension, expected_type=type_hints["extension"])
        return typing.cast(None, jsii.invoke(self, "addExtension", [extension]))

    @jsii.member(jsii_name="grant")
    def grant(
        self,
        grantee: _IGrantable_71c4f5de,
        *actions: builtins.str,
    ) -> _Grant_a7ae64f8:
        '''Adds an IAM policy statement associated with this environment to an IAM principal's policy.

        :param grantee: -
        :param actions: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c65f9ec077d5abb2638f74671e3f2d65ef4fed80c0e32561b7b807b917e7d53)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
            check_type(argname="argument actions", value=actions, expected_type=typing.Tuple[type_hints["actions"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grant", [grantee, *actions]))

    @jsii.member(jsii_name="grantReadConfig")
    def grant_read_config(self, identity: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Permits an IAM principal to perform read operations on this environment's configurations.

        Actions: GetLatestConfiguration, StartConfigurationSession.

        :param identity: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__790a777ba7325eb4b088cf4fe3be2b4fdcc0c100050d537316abc7125c7f326f)
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantReadConfig", [identity]))

    @jsii.member(jsii_name="on")
    def on(
        self,
        action_point: ActionPoint,
        event_destination: IEventDestination,
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence[Parameter]] = None,
    ) -> None:
        '''Adds an extension defined by the action point and event destination and also creates an extension association to the environment.

        :param action_point: -
        :param event_destination: -
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c5b20c6ba105fc862af761c49db56fe32fde770ccf217e82ae6d4ae54bada0f)
            check_type(argname="argument action_point", value=action_point, expected_type=type_hints["action_point"])
            check_type(argname="argument event_destination", value=event_destination, expected_type=type_hints["event_destination"])
        options = ExtensionOptions(
            description=description,
            extension_name=extension_name,
            latest_version_number=latest_version_number,
            parameters=parameters,
        )

        return typing.cast(None, jsii.invoke(self, "on", [action_point, event_destination, options]))

    @jsii.member(jsii_name="onDeploymentBaking")
    def on_deployment_baking(
        self,
        event_destination: IEventDestination,
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence[Parameter]] = None,
    ) -> None:
        '''Adds an ON_DEPLOYMENT_BAKING extension with the provided event destination and also creates an extension association to the environment.

        :param event_destination: -
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f4454f449feb8e261a065afd7db0ca3cc40df93581582d67a92531c61da1458)
            check_type(argname="argument event_destination", value=event_destination, expected_type=type_hints["event_destination"])
        options = ExtensionOptions(
            description=description,
            extension_name=extension_name,
            latest_version_number=latest_version_number,
            parameters=parameters,
        )

        return typing.cast(None, jsii.invoke(self, "onDeploymentBaking", [event_destination, options]))

    @jsii.member(jsii_name="onDeploymentComplete")
    def on_deployment_complete(
        self,
        event_destination: IEventDestination,
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence[Parameter]] = None,
    ) -> None:
        '''Adds an ON_DEPLOYMENT_COMPLETE extension with the provided event destination and also creates an extension association to the environment.

        :param event_destination: -
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78f9cb6929bf857fb78f3e50ae777f7ad0b72a8340597d58727ccec6d8285614)
            check_type(argname="argument event_destination", value=event_destination, expected_type=type_hints["event_destination"])
        options = ExtensionOptions(
            description=description,
            extension_name=extension_name,
            latest_version_number=latest_version_number,
            parameters=parameters,
        )

        return typing.cast(None, jsii.invoke(self, "onDeploymentComplete", [event_destination, options]))

    @jsii.member(jsii_name="onDeploymentRolledBack")
    def on_deployment_rolled_back(
        self,
        event_destination: IEventDestination,
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence[Parameter]] = None,
    ) -> None:
        '''Adds an ON_DEPLOYMENT_ROLLED_BACK extension with the provided event destination and also creates an extension association to the environment.

        :param event_destination: -
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8127118f73782a3390b7d2b32acfd493beb5de7191565a608f9420135471066)
            check_type(argname="argument event_destination", value=event_destination, expected_type=type_hints["event_destination"])
        options = ExtensionOptions(
            description=description,
            extension_name=extension_name,
            latest_version_number=latest_version_number,
            parameters=parameters,
        )

        return typing.cast(None, jsii.invoke(self, "onDeploymentRolledBack", [event_destination, options]))

    @jsii.member(jsii_name="onDeploymentStart")
    def on_deployment_start(
        self,
        event_destination: IEventDestination,
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence[Parameter]] = None,
    ) -> None:
        '''Adds an ON_DEPLOYMENT_START extension with the provided event destination and also creates an extension association to the environment.

        :param event_destination: -
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62b75fa8040428cb2e8eaedd119654e80a90641410e1e58a25ccf041128aeaf4)
            check_type(argname="argument event_destination", value=event_destination, expected_type=type_hints["event_destination"])
        options = ExtensionOptions(
            description=description,
            extension_name=extension_name,
            latest_version_number=latest_version_number,
            parameters=parameters,
        )

        return typing.cast(None, jsii.invoke(self, "onDeploymentStart", [event_destination, options]))

    @jsii.member(jsii_name="onDeploymentStep")
    def on_deployment_step(
        self,
        event_destination: IEventDestination,
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence[Parameter]] = None,
    ) -> None:
        '''Adds an ON_DEPLOYMENT_STEP extension with the provided event destination and also creates an extension association to the environment.

        :param event_destination: -
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3903e077af062c1b31f63d11710d11cc5807cb4fdd9694d38a86e3050f67a068)
            check_type(argname="argument event_destination", value=event_destination, expected_type=type_hints["event_destination"])
        options = ExtensionOptions(
            description=description,
            extension_name=extension_name,
            latest_version_number=latest_version_number,
            parameters=parameters,
        )

        return typing.cast(None, jsii.invoke(self, "onDeploymentStep", [event_destination, options]))

    @jsii.member(jsii_name="preCreateHostedConfigurationVersion")
    def pre_create_hosted_configuration_version(
        self,
        event_destination: IEventDestination,
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence[Parameter]] = None,
    ) -> None:
        '''Adds a PRE_CREATE_HOSTED_CONFIGURATION_VERSION extension with the provided event destination and also creates an extension association to the environment.

        :param event_destination: -
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f574c3024d31be00420b36fcfec7902de0226ae4a571a80f5e6502c34900f5fa)
            check_type(argname="argument event_destination", value=event_destination, expected_type=type_hints["event_destination"])
        options = ExtensionOptions(
            description=description,
            extension_name=extension_name,
            latest_version_number=latest_version_number,
            parameters=parameters,
        )

        return typing.cast(None, jsii.invoke(self, "preCreateHostedConfigurationVersion", [event_destination, options]))

    @jsii.member(jsii_name="preStartDeployment")
    def pre_start_deployment(
        self,
        event_destination: IEventDestination,
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence[Parameter]] = None,
    ) -> None:
        '''Adds a PRE_START_DEPLOYMENT extension with the provided event destination and also creates an extension association to the environment.

        :param event_destination: -
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22ccb2ca13f7df2815220f1d2cdda0fb9d20c17ac1fafb9dcc50064559b9a066)
            check_type(argname="argument event_destination", value=event_destination, expected_type=type_hints["event_destination"])
        options = ExtensionOptions(
            description=description,
            extension_name=extension_name,
            latest_version_number=latest_version_number,
            parameters=parameters,
        )

        return typing.cast(None, jsii.invoke(self, "preStartDeployment", [event_destination, options]))

    @builtins.property
    @jsii.member(jsii_name="applicationId")
    def application_id(self) -> builtins.str:
        '''The ID of the environment.'''
        return typing.cast(builtins.str, jsii.get(self, "applicationId"))

    @builtins.property
    @jsii.member(jsii_name="environmentArn")
    def environment_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the environment.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "environmentArn"))

    @builtins.property
    @jsii.member(jsii_name="environmentId")
    def environment_id(self) -> builtins.str:
        '''The ID of the environment.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "environmentId"))

    @builtins.property
    @jsii.member(jsii_name="application")
    def application(self) -> typing.Optional[IApplication]:
        '''The application associated with the environment.'''
        return typing.cast(typing.Optional[IApplication], jsii.get(self, "application"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the environment.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @builtins.property
    @jsii.member(jsii_name="monitors")
    def monitors(self) -> typing.Optional[typing.List[Monitor]]:
        '''The monitors for the environment.'''
        return typing.cast(typing.Optional[typing.List[Monitor]], jsii.get(self, "monitors"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the environment.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="deploymentQueue")
    def _deployment_queue(self) -> typing.List[CfnDeployment]:
        return typing.cast(typing.List[CfnDeployment], jsii.get(self, "deploymentQueue"))

    @_deployment_queue.setter
    def _deployment_queue(self, value: typing.List[CfnDeployment]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd39d7b7b77c944582e5f7fabeb3e37717eaa470540d764633f9ce909058030a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deploymentQueue", value)

    @builtins.property
    @jsii.member(jsii_name="extensible")
    def _extensible(self) -> "ExtensibleBase":
        return typing.cast("ExtensibleBase", jsii.get(self, "extensible"))

    @_extensible.setter
    def _extensible(self, value: "ExtensibleBase") -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f249899e37c9153afa9dc39542328ce1c247c1f209ac134fb2bc8a4ad1120946)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "extensible", value)


@jsii.implements(IEventDestination)
class EventBridgeDestination(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appconfig.EventBridgeDestination",
):
    '''Use an Amazon EventBridge event bus as an event destination.

    :exampleMetadata: infused

    Example::

        bus = events.EventBus.from_event_bus_name(self, "MyEventBus", "default")
        
        appconfig.Extension(self, "MyExtension",
            actions=[
                appconfig.Action(
                    action_points=[appconfig.ActionPoint.ON_DEPLOYMENT_START],
                    event_destination=appconfig.EventBridgeDestination(bus)
                )
            ]
        )
    '''

    def __init__(self, bus: _IEventBus_88d13111) -> None:
        '''
        :param bus: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80f21051c7734c306113ac626a6c5c630b229e3c1cb7444771ec9a9a993a7a3f)
            check_type(argname="argument bus", value=bus, expected_type=type_hints["bus"])
        jsii.create(self.__class__, self, [bus])

    @builtins.property
    @jsii.member(jsii_name="extensionUri")
    def extension_uri(self) -> builtins.str:
        '''The URI of the extension event destination.'''
        return typing.cast(builtins.str, jsii.get(self, "extensionUri"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> SourceType:
        '''The type of the extension event destination.'''
        return typing.cast(SourceType, jsii.get(self, "type"))


@jsii.implements(IExtensible)
class ExtensibleBase(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appconfig.ExtensibleBase",
):
    '''This class is meant to be used by AWS AppConfig resources (application, configuration profile, environment) directly.

    There is currently no use
    for this class outside of the AWS AppConfig construct implementation. It is
    intended to be used with the resources since there is currently no way to
    inherit from two classes (at least within JSII constraints).

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_appconfig as appconfig
        
        extensible_base = appconfig.ExtensibleBase(self, "resourceArn", "resourceName")
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        resource_arn: builtins.str,
        resource_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param resource_arn: -
        :param resource_name: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__859c379a4d03dea0c0fd17b7fd6acf3b7d65d43c3c4b856443463daca4ef489c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
            check_type(argname="argument resource_name", value=resource_name, expected_type=type_hints["resource_name"])
        jsii.create(self.__class__, self, [scope, resource_arn, resource_name])

    @jsii.member(jsii_name="addExtension")
    def add_extension(self, extension: IExtension) -> None:
        '''Adds an extension association to the derived resource.

        :param extension: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6a9c7f9aa42fa6ded0470d92dbcd83940a578472e76af9396bdbd356d3926fc)
            check_type(argname="argument extension", value=extension, expected_type=type_hints["extension"])
        return typing.cast(None, jsii.invoke(self, "addExtension", [extension]))

    @jsii.member(jsii_name="on")
    def on(
        self,
        action_point: ActionPoint,
        event_destination: IEventDestination,
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence[Parameter]] = None,
    ) -> None:
        '''Adds an extension defined by the action point and event destination and also creates an extension association to the derived resource.

        :param action_point: -
        :param event_destination: -
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a6722e71c8fd1cc15e9b19f2e0909d6bbb97c17169577f39de30b2d1260a131)
            check_type(argname="argument action_point", value=action_point, expected_type=type_hints["action_point"])
            check_type(argname="argument event_destination", value=event_destination, expected_type=type_hints["event_destination"])
        options = ExtensionOptions(
            description=description,
            extension_name=extension_name,
            latest_version_number=latest_version_number,
            parameters=parameters,
        )

        return typing.cast(None, jsii.invoke(self, "on", [action_point, event_destination, options]))

    @jsii.member(jsii_name="onDeploymentBaking")
    def on_deployment_baking(
        self,
        event_destination: IEventDestination,
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence[Parameter]] = None,
    ) -> None:
        '''Adds an ON_DEPLOYMENT_BAKING extension with the provided event destination and also creates an extension association to the derived resource.

        :param event_destination: -
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec27ee4753650addf32b95b09fec2cb92d81a9c9171b0c84cf371c07727fbcb6)
            check_type(argname="argument event_destination", value=event_destination, expected_type=type_hints["event_destination"])
        options = ExtensionOptions(
            description=description,
            extension_name=extension_name,
            latest_version_number=latest_version_number,
            parameters=parameters,
        )

        return typing.cast(None, jsii.invoke(self, "onDeploymentBaking", [event_destination, options]))

    @jsii.member(jsii_name="onDeploymentComplete")
    def on_deployment_complete(
        self,
        event_destination: IEventDestination,
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence[Parameter]] = None,
    ) -> None:
        '''Adds an ON_DEPLOYMENT_COMPLETE extension with the provided event destination and also creates an extension association to the derived resource.

        :param event_destination: -
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b10722268778e5ad348b053b6dfa3088b7136433373392d19ffe8fa94f3e69cf)
            check_type(argname="argument event_destination", value=event_destination, expected_type=type_hints["event_destination"])
        options = ExtensionOptions(
            description=description,
            extension_name=extension_name,
            latest_version_number=latest_version_number,
            parameters=parameters,
        )

        return typing.cast(None, jsii.invoke(self, "onDeploymentComplete", [event_destination, options]))

    @jsii.member(jsii_name="onDeploymentRolledBack")
    def on_deployment_rolled_back(
        self,
        event_destination: IEventDestination,
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence[Parameter]] = None,
    ) -> None:
        '''Adds an ON_DEPLOYMENT_ROLLED_BACK extension with the provided event destination and also creates an extension association to the derived resource.

        :param event_destination: -
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4463425263eafb5ee62382d54de44afc2b669415871a836ff016494929fd805)
            check_type(argname="argument event_destination", value=event_destination, expected_type=type_hints["event_destination"])
        options = ExtensionOptions(
            description=description,
            extension_name=extension_name,
            latest_version_number=latest_version_number,
            parameters=parameters,
        )

        return typing.cast(None, jsii.invoke(self, "onDeploymentRolledBack", [event_destination, options]))

    @jsii.member(jsii_name="onDeploymentStart")
    def on_deployment_start(
        self,
        event_destination: IEventDestination,
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence[Parameter]] = None,
    ) -> None:
        '''Adds an ON_DEPLOYMENT_START extension with the provided event destination and also creates an extension association to the derived resource.

        :param event_destination: -
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35795185ba628914eac8facd076158729a01914ea36274cabb0a1b1a7199fe79)
            check_type(argname="argument event_destination", value=event_destination, expected_type=type_hints["event_destination"])
        options = ExtensionOptions(
            description=description,
            extension_name=extension_name,
            latest_version_number=latest_version_number,
            parameters=parameters,
        )

        return typing.cast(None, jsii.invoke(self, "onDeploymentStart", [event_destination, options]))

    @jsii.member(jsii_name="onDeploymentStep")
    def on_deployment_step(
        self,
        event_destination: IEventDestination,
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence[Parameter]] = None,
    ) -> None:
        '''Adds an ON_DEPLOYMENT_STEP extension with the provided event destination and also creates an extension association to the derived resource.

        :param event_destination: -
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__040c76c87c97ded56b6f961a3f12386f7e3a3eae5691a332b2449e12945de1a3)
            check_type(argname="argument event_destination", value=event_destination, expected_type=type_hints["event_destination"])
        options = ExtensionOptions(
            description=description,
            extension_name=extension_name,
            latest_version_number=latest_version_number,
            parameters=parameters,
        )

        return typing.cast(None, jsii.invoke(self, "onDeploymentStep", [event_destination, options]))

    @jsii.member(jsii_name="preCreateHostedConfigurationVersion")
    def pre_create_hosted_configuration_version(
        self,
        event_destination: IEventDestination,
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence[Parameter]] = None,
    ) -> None:
        '''Adds a PRE_CREATE_HOSTED_CONFIGURATION_VERSION extension with the provided event destination and also creates an extension association to the derived resource.

        :param event_destination: -
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0876520af8e864feae7bfca8859c4660ea6a7c7ae48c3755fa69e58161cd6866)
            check_type(argname="argument event_destination", value=event_destination, expected_type=type_hints["event_destination"])
        options = ExtensionOptions(
            description=description,
            extension_name=extension_name,
            latest_version_number=latest_version_number,
            parameters=parameters,
        )

        return typing.cast(None, jsii.invoke(self, "preCreateHostedConfigurationVersion", [event_destination, options]))

    @jsii.member(jsii_name="preStartDeployment")
    def pre_start_deployment(
        self,
        event_destination: IEventDestination,
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence[Parameter]] = None,
    ) -> None:
        '''Adds a PRE_START_DEPLOYMENT extension with the provided event destination and also creates an extension association to the derived resource.

        :param event_destination: -
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a2539aa3c7790e56e2d710cf16d21806637a211078c85589485c38d18db2d34)
            check_type(argname="argument event_destination", value=event_destination, expected_type=type_hints["event_destination"])
        options = ExtensionOptions(
            description=description,
            extension_name=extension_name,
            latest_version_number=latest_version_number,
            parameters=parameters,
        )

        return typing.cast(None, jsii.invoke(self, "preStartDeployment", [event_destination, options]))


@jsii.implements(IExtension)
class Extension(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appconfig.Extension",
):
    '''An AWS AppConfig extension.

    :see: https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions.html
    :resource: AWS::AppConfig::Extension
    :exampleMetadata: infused

    Example::

        # fn: lambda.Function
        
        
        appconfig.Extension(self, "MyExtension",
            actions=[
                appconfig.Action(
                    action_points=[appconfig.ActionPoint.ON_DEPLOYMENT_START],
                    event_destination=appconfig.LambdaDestination(fn)
                )
            ]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        actions: typing.Sequence[Action],
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence[Parameter]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param actions: The actions for the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2651da7526c7d2966c70f3f4d4a570b1b30f5f6ee97508d27ddc0afdeffa5b68)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ExtensionProps(
            actions=actions,
            description=description,
            extension_name=extension_name,
            latest_version_number=latest_version_number,
            parameters=parameters,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromExtensionArn")
    @builtins.classmethod
    def from_extension_arn(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        extension_arn: builtins.str,
    ) -> IExtension:
        '''Imports an extension into the CDK using its Amazon Resource Name (ARN).

        :param scope: The parent construct.
        :param id: The name of the extension construct.
        :param extension_arn: The Amazon Resource Name (ARN) of the extension.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__675381e6515f056b4ecc6dca61eda68802c57de4687430e36e54e9b24d670c34)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument extension_arn", value=extension_arn, expected_type=type_hints["extension_arn"])
        return typing.cast(IExtension, jsii.sinvoke(cls, "fromExtensionArn", [scope, id, extension_arn]))

    @jsii.member(jsii_name="fromExtensionAttributes")
    @builtins.classmethod
    def from_extension_attributes(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        extension_id: builtins.str,
        extension_version_number: jsii.Number,
        actions: typing.Optional[typing.Sequence[Action]] = None,
        description: typing.Optional[builtins.str] = None,
        extension_arn: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> IExtension:
        '''Imports an extension into the CDK using its attributes.

        :param scope: The parent construct.
        :param id: The name of the extension construct.
        :param extension_id: The ID of the extension.
        :param extension_version_number: The version number of the extension.
        :param actions: The actions of the extension. Default: - None.
        :param description: The description of the extension. Default: - None.
        :param extension_arn: The Amazon Resource Name (ARN) of the extension. Default: - The extension ARN is generated.
        :param name: The name of the extension. Default: - None.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72f1e669cca59ef8756f1a767c7447e601a93a5765f9603a3f36fcc4077bf272)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        attrs = ExtensionAttributes(
            extension_id=extension_id,
            extension_version_number=extension_version_number,
            actions=actions,
            description=description,
            extension_arn=extension_arn,
            name=name,
        )

        return typing.cast(IExtension, jsii.sinvoke(cls, "fromExtensionAttributes", [scope, id, attrs]))

    @builtins.property
    @jsii.member(jsii_name="extensionArn")
    def extension_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the extension.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "extensionArn"))

    @builtins.property
    @jsii.member(jsii_name="extensionId")
    def extension_id(self) -> builtins.str:
        '''The ID of the extension.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "extensionId"))

    @builtins.property
    @jsii.member(jsii_name="extensionVersionNumber")
    def extension_version_number(self) -> jsii.Number:
        '''The version number of the extension.

        :attribute: true
        '''
        return typing.cast(jsii.Number, jsii.get(self, "extensionVersionNumber"))

    @builtins.property
    @jsii.member(jsii_name="actions")
    def actions(self) -> typing.Optional[typing.List[Action]]:
        '''The actions for the extension.'''
        return typing.cast(typing.Optional[typing.List[Action]], jsii.get(self, "actions"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the extension.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @builtins.property
    @jsii.member(jsii_name="latestVersionNumber")
    def latest_version_number(self) -> typing.Optional[jsii.Number]:
        '''The latest version number of the extension.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "latestVersionNumber"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the extension.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> typing.Optional[typing.List[Parameter]]:
        '''The parameters of the extension.'''
        return typing.cast(typing.Optional[typing.List[Parameter]], jsii.get(self, "parameters"))


@jsii.implements(IConfiguration, IExtensible)
class HostedConfiguration(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appconfig.HostedConfiguration",
):
    '''A hosted configuration represents configuration stored in the AWS AppConfig hosted configuration store.

    :exampleMetadata: infused

    Example::

        app = appconfig.Application(self, "MyApp")
        env = appconfig.Environment(self, "MyEnv",
            application=app
        )
        
        appconfig.HostedConfiguration(self, "MyHostedConfig",
            application=app,
            deploy_to=[env],
            content=appconfig.ConfigurationContent.from_inline_text("This is my configuration content.")
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        content: ConfigurationContent,
        latest_version_number: typing.Optional[jsii.Number] = None,
        version_label: typing.Optional[builtins.str] = None,
        application: IApplication,
        deployment_key: typing.Optional[_IKey_5f11635f] = None,
        deployment_strategy: typing.Optional[IDeploymentStrategy] = None,
        deploy_to: typing.Optional[typing.Sequence[IEnvironment]] = None,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        type: typing.Optional[ConfigurationType] = None,
        validators: typing.Optional[typing.Sequence[IValidator]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param content: The content of the hosted configuration.
        :param latest_version_number: The latest version number of the hosted configuration. Default: - None.
        :param version_label: The version label of the hosted configuration. Default: - None.
        :param application: The application associated with the configuration.
        :param deployment_key: The deployment key of the configuration. Default: - None.
        :param deployment_strategy: The deployment strategy for the configuration. Default: - A deployment strategy with the rollout strategy set to RolloutStrategy.CANARY_10_PERCENT_20_MINUTES
        :param deploy_to: The list of environments to deploy the configuration to. If this parameter is not specified, then there will be no deployment created alongside this configuration. Deployments can be added later using the ``IEnvironment.addDeployment`` or ``IEnvironment.addDeployments`` methods. Default: - None.
        :param description: The description of the configuration. Default: - No description.
        :param name: The name of the configuration. Default: - A name is generated.
        :param type: The type of configuration. Default: ConfigurationType.FREEFORM
        :param validators: The validators for the configuration. Default: - No validators.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e7eecc550d3d689f07534db869c7be67f00e08dcbf880bbb2656d01940aa8e8)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = HostedConfigurationProps(
            content=content,
            latest_version_number=latest_version_number,
            version_label=version_label,
            application=application,
            deployment_key=deployment_key,
            deployment_strategy=deployment_strategy,
            deploy_to=deploy_to,
            description=description,
            name=name,
            type=type,
            validators=validators,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="addExistingEnvironmentsToApplication")
    def _add_existing_environments_to_application(self) -> None:
        return typing.cast(None, jsii.invoke(self, "addExistingEnvironmentsToApplication", []))

    @jsii.member(jsii_name="addExtension")
    def add_extension(self, extension: IExtension) -> None:
        '''Adds an extension association to the configuration profile.

        :param extension: The extension to create an association for.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dcffd5e999d1df96cb081e766c8016c4aa0123304ff23d455b57cbab7e0b7685)
            check_type(argname="argument extension", value=extension, expected_type=type_hints["extension"])
        return typing.cast(None, jsii.invoke(self, "addExtension", [extension]))

    @jsii.member(jsii_name="deployConfigToEnvironments")
    def _deploy_config_to_environments(self) -> None:
        return typing.cast(None, jsii.invoke(self, "deployConfigToEnvironments", []))

    @jsii.member(jsii_name="on")
    def on(
        self,
        action_point: ActionPoint,
        event_destination: IEventDestination,
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence[Parameter]] = None,
    ) -> None:
        '''Adds an extension defined by the action point and event destination and also creates an extension association to the configuration profile.

        :param action_point: The action point which triggers the event.
        :param event_destination: The event that occurs during the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2cdc0ffbe5a8630ebd90111a737ca2b967dee69b1b2b68149dd3251cce675208)
            check_type(argname="argument action_point", value=action_point, expected_type=type_hints["action_point"])
            check_type(argname="argument event_destination", value=event_destination, expected_type=type_hints["event_destination"])
        options = ExtensionOptions(
            description=description,
            extension_name=extension_name,
            latest_version_number=latest_version_number,
            parameters=parameters,
        )

        return typing.cast(None, jsii.invoke(self, "on", [action_point, event_destination, options]))

    @jsii.member(jsii_name="onDeploymentBaking")
    def on_deployment_baking(
        self,
        event_destination: IEventDestination,
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence[Parameter]] = None,
    ) -> None:
        '''Adds an ON_DEPLOYMENT_BAKING extension with the provided event destination and also creates an extension association to the configuration profile.

        :param event_destination: The event that occurs during the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ceda34dc0d119d50cc7ecc5a567ff2fc5c604fc1bb576ec935fb8335caf48c74)
            check_type(argname="argument event_destination", value=event_destination, expected_type=type_hints["event_destination"])
        options = ExtensionOptions(
            description=description,
            extension_name=extension_name,
            latest_version_number=latest_version_number,
            parameters=parameters,
        )

        return typing.cast(None, jsii.invoke(self, "onDeploymentBaking", [event_destination, options]))

    @jsii.member(jsii_name="onDeploymentComplete")
    def on_deployment_complete(
        self,
        event_destination: IEventDestination,
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence[Parameter]] = None,
    ) -> None:
        '''Adds an ON_DEPLOYMENT_COMPLETE extension with the provided event destination and also creates an extension association to the configuration profile.

        :param event_destination: The event that occurs during the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95fca11df6f0876cf9825441d8ff70e095a2215e4eb6550fd49e603838afe3ca)
            check_type(argname="argument event_destination", value=event_destination, expected_type=type_hints["event_destination"])
        options = ExtensionOptions(
            description=description,
            extension_name=extension_name,
            latest_version_number=latest_version_number,
            parameters=parameters,
        )

        return typing.cast(None, jsii.invoke(self, "onDeploymentComplete", [event_destination, options]))

    @jsii.member(jsii_name="onDeploymentRolledBack")
    def on_deployment_rolled_back(
        self,
        event_destination: IEventDestination,
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence[Parameter]] = None,
    ) -> None:
        '''Adds an ON_DEPLOYMENT_ROLLED_BACK extension with the provided event destination and also creates an extension association to the configuration profile.

        :param event_destination: The event that occurs during the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bac203b4ea30df38ac6f158d19b1afc4955e500a8830d6e3e75b448a1b98937b)
            check_type(argname="argument event_destination", value=event_destination, expected_type=type_hints["event_destination"])
        options = ExtensionOptions(
            description=description,
            extension_name=extension_name,
            latest_version_number=latest_version_number,
            parameters=parameters,
        )

        return typing.cast(None, jsii.invoke(self, "onDeploymentRolledBack", [event_destination, options]))

    @jsii.member(jsii_name="onDeploymentStart")
    def on_deployment_start(
        self,
        event_destination: IEventDestination,
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence[Parameter]] = None,
    ) -> None:
        '''Adds an ON_DEPLOYMENT_START extension with the provided event destination and also creates an extension association to the configuration profile.

        :param event_destination: The event that occurs during the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2fd8a68a1ddc7aca359954daa777db0d209ac14b7b24a6ba5b435bafd3b718bd)
            check_type(argname="argument event_destination", value=event_destination, expected_type=type_hints["event_destination"])
        options = ExtensionOptions(
            description=description,
            extension_name=extension_name,
            latest_version_number=latest_version_number,
            parameters=parameters,
        )

        return typing.cast(None, jsii.invoke(self, "onDeploymentStart", [event_destination, options]))

    @jsii.member(jsii_name="onDeploymentStep")
    def on_deployment_step(
        self,
        event_destination: IEventDestination,
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence[Parameter]] = None,
    ) -> None:
        '''Adds an ON_DEPLOYMENT_STEP extension with the provided event destination and also creates an extension association to the configuration profile.

        :param event_destination: The event that occurs during the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7673b3ddc8b5478788c8347bb28dece31c205a8030ce432584227064e3e7dbd1)
            check_type(argname="argument event_destination", value=event_destination, expected_type=type_hints["event_destination"])
        options = ExtensionOptions(
            description=description,
            extension_name=extension_name,
            latest_version_number=latest_version_number,
            parameters=parameters,
        )

        return typing.cast(None, jsii.invoke(self, "onDeploymentStep", [event_destination, options]))

    @jsii.member(jsii_name="preCreateHostedConfigurationVersion")
    def pre_create_hosted_configuration_version(
        self,
        event_destination: IEventDestination,
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence[Parameter]] = None,
    ) -> None:
        '''Adds a PRE_CREATE_HOSTED_CONFIGURATION_VERSION extension with the provided event destination and also creates an extension association to the configuration profile.

        :param event_destination: The event that occurs during the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3b0e26d65395b369b7b5023f0ce3b98d1c183d44f8cad8b1ec1a7ea1edc936b)
            check_type(argname="argument event_destination", value=event_destination, expected_type=type_hints["event_destination"])
        options = ExtensionOptions(
            description=description,
            extension_name=extension_name,
            latest_version_number=latest_version_number,
            parameters=parameters,
        )

        return typing.cast(None, jsii.invoke(self, "preCreateHostedConfigurationVersion", [event_destination, options]))

    @jsii.member(jsii_name="preStartDeployment")
    def pre_start_deployment(
        self,
        event_destination: IEventDestination,
        *,
        description: typing.Optional[builtins.str] = None,
        extension_name: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
        parameters: typing.Optional[typing.Sequence[Parameter]] = None,
    ) -> None:
        '''Adds a PRE_START_DEPLOYMENT extension with the provided event destination and also creates an extension association to the configuration profile.

        :param event_destination: The event that occurs during the extension.
        :param description: A description of the extension. Default: - No description.
        :param extension_name: The name of the extension. Default: - A name is generated.
        :param latest_version_number: The latest version number of the extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field. Default: - None.
        :param parameters: The parameters accepted for the extension. Default: - None.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40083372633c70683c32dc01cf6546ae2759ee8aa8001f03ec550ad5578f1e4f)
            check_type(argname="argument event_destination", value=event_destination, expected_type=type_hints["event_destination"])
        options = ExtensionOptions(
            description=description,
            extension_name=extension_name,
            latest_version_number=latest_version_number,
            parameters=parameters,
        )

        return typing.cast(None, jsii.invoke(self, "preStartDeployment", [event_destination, options]))

    @builtins.property
    @jsii.member(jsii_name="application")
    def application(self) -> IApplication:
        '''The application associated with the configuration.'''
        return typing.cast(IApplication, jsii.get(self, "application"))

    @builtins.property
    @jsii.member(jsii_name="configurationProfileArn")
    def configuration_profile_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the configuration profile.'''
        return typing.cast(builtins.str, jsii.get(self, "configurationProfileArn"))

    @builtins.property
    @jsii.member(jsii_name="configurationProfileId")
    def configuration_profile_id(self) -> builtins.str:
        '''The ID of the configuration profile.'''
        return typing.cast(builtins.str, jsii.get(self, "configurationProfileId"))

    @builtins.property
    @jsii.member(jsii_name="content")
    def content(self) -> builtins.str:
        '''The content of the hosted configuration.'''
        return typing.cast(builtins.str, jsii.get(self, "content"))

    @builtins.property
    @jsii.member(jsii_name="hostedConfigurationVersionArn")
    def hosted_configuration_version_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the hosted configuration version.'''
        return typing.cast(builtins.str, jsii.get(self, "hostedConfigurationVersionArn"))

    @builtins.property
    @jsii.member(jsii_name="contentType")
    def content_type(self) -> typing.Optional[builtins.str]:
        '''The content type of the hosted configuration.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentType"))

    @builtins.property
    @jsii.member(jsii_name="deploymentKey")
    def deployment_key(self) -> typing.Optional[_IKey_5f11635f]:
        '''The deployment key for the configuration.'''
        return typing.cast(typing.Optional[_IKey_5f11635f], jsii.get(self, "deploymentKey"))

    @builtins.property
    @jsii.member(jsii_name="deploymentStrategy")
    def deployment_strategy(self) -> typing.Optional[IDeploymentStrategy]:
        '''The deployment strategy for the configuration.'''
        return typing.cast(typing.Optional[IDeploymentStrategy], jsii.get(self, "deploymentStrategy"))

    @builtins.property
    @jsii.member(jsii_name="deployTo")
    def deploy_to(self) -> typing.Optional[typing.List[IEnvironment]]:
        '''The environments to deploy to.'''
        return typing.cast(typing.Optional[typing.List[IEnvironment]], jsii.get(self, "deployTo"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the configuration.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @builtins.property
    @jsii.member(jsii_name="latestVersionNumber")
    def latest_version_number(self) -> typing.Optional[jsii.Number]:
        '''The latest version number of the hosted configuration.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "latestVersionNumber"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the configuration.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> typing.Optional[ConfigurationType]:
        '''The configuration type.'''
        return typing.cast(typing.Optional[ConfigurationType], jsii.get(self, "type"))

    @builtins.property
    @jsii.member(jsii_name="validators")
    def validators(self) -> typing.Optional[typing.List[IValidator]]:
        '''The validators for the configuration.'''
        return typing.cast(typing.Optional[typing.List[IValidator]], jsii.get(self, "validators"))

    @builtins.property
    @jsii.member(jsii_name="versionLabel")
    def version_label(self) -> typing.Optional[builtins.str]:
        '''The version label of the hosted configuration.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionLabel"))

    @builtins.property
    @jsii.member(jsii_name="versionNumber")
    def version_number(self) -> typing.Optional[builtins.str]:
        '''The version number of the hosted configuration.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionNumber"))

    @builtins.property
    @jsii.member(jsii_name="applicationId")
    def _application_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "applicationId"))

    @_application_id.setter
    def _application_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4058b9695ce055c514ee6b279cac6589d3ab9aa62414133fc4992ec610aa1d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationId", value)

    @builtins.property
    @jsii.member(jsii_name="extensible")
    def _extensible(self) -> ExtensibleBase:
        return typing.cast(ExtensibleBase, jsii.get(self, "extensible"))

    @_extensible.setter
    def _extensible(self, value: ExtensibleBase) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27c25acd80a9bdc9870365bad92556272569854dc957ad7cdf2b6e5a2c29c2ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "extensible", value)


__all__ = [
    "Action",
    "ActionPoint",
    "ActionProps",
    "Application",
    "ApplicationProps",
    "CfnApplication",
    "CfnApplicationProps",
    "CfnConfigurationProfile",
    "CfnConfigurationProfileProps",
    "CfnDeployment",
    "CfnDeploymentProps",
    "CfnDeploymentStrategy",
    "CfnDeploymentStrategyProps",
    "CfnEnvironment",
    "CfnEnvironmentProps",
    "CfnExtension",
    "CfnExtensionAssociation",
    "CfnExtensionAssociationProps",
    "CfnExtensionProps",
    "CfnHostedConfigurationVersion",
    "CfnHostedConfigurationVersionProps",
    "ConfigurationContent",
    "ConfigurationOptions",
    "ConfigurationProps",
    "ConfigurationSource",
    "ConfigurationSourceType",
    "ConfigurationType",
    "DeploymentStrategy",
    "DeploymentStrategyId",
    "DeploymentStrategyProps",
    "Environment",
    "EnvironmentAttributes",
    "EnvironmentOptions",
    "EnvironmentProps",
    "EventBridgeDestination",
    "ExtensibleBase",
    "Extension",
    "ExtensionAttributes",
    "ExtensionOptions",
    "ExtensionProps",
    "GrowthType",
    "HostedConfiguration",
    "HostedConfigurationOptions",
    "HostedConfigurationProps",
    "IApplication",
    "IConfiguration",
    "IDeploymentStrategy",
    "IEnvironment",
    "IEventDestination",
    "IExtensible",
    "IExtension",
    "IValidator",
    "JsonSchemaValidator",
    "LambdaDestination",
    "LambdaValidator",
    "Monitor",
    "MonitorType",
    "Parameter",
    "Platform",
    "RolloutStrategy",
    "RolloutStrategyProps",
    "SnsDestination",
    "SourceType",
    "SourcedConfiguration",
    "SourcedConfigurationOptions",
    "SourcedConfigurationProps",
    "SqsDestination",
    "ValidatorType",
]

publication.publish()

def _typecheckingstub__d69874f3a61f1cf288efe1495c078fb07b686754d78d66ba26a1bf2e49af8cfb(
    *,
    action_points: typing.Sequence[ActionPoint],
    event_destination: IEventDestination,
    description: typing.Optional[builtins.str] = None,
    execution_role: typing.Optional[_IRole_235f5d8e] = None,
    invoke_without_execution_role: typing.Optional[builtins.bool] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c495cbb9f880c8e82aa0fdbd8db994460c32e416c849e56db45c634dcf325d8(
    *,
    application_name: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5cb8c402a0d1a836162f596142de6ed2a1f2a0635a355ae334b92eb1175e956(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ea7b1a84049868bc175511a7cff8896cbe830377b519f6e81ca6912165c12a6(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6ba5479a5d56f629f8d2769fdc6bc86ac3ecfb94f4a9b20a0a26e228f899e8a(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd439efd20029913dc2dc3442824daa5698101df926aeab59ca95e5e5b8bbd51(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a824db2a54c11ce0a54133772196bc9c7049c60fe6169de15459866f72df2438(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1c6b2136fb3c6e3eba293e5878e147b18261e888036e9d04f50ade7f12363e3(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32e1eda1678f32e80ec88e7c377d932bfe40dcff82d39b0dd0edf98a68d3e9d9(
    *,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__332c05b5fb120e53a9fcdde311f2bc23aaec927aa0e70b013e72cc2cebe88708(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    application_id: builtins.str,
    location_uri: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    kms_key_identifier: typing.Optional[builtins.str] = None,
    retrieval_role_arn: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    type: typing.Optional[builtins.str] = None,
    validators: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationProfile.ValidatorsProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e772e24251baa448c01bcc3e6670ade5ceed90c38ae4803dc614bd5e09316acd(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e32e704ce25e06be45d32d6a2f4cb3655c378ec2a6662baf1f650e54d58d3148(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a90d416aa5727f39ec3c71cf2276506643a5cf358d97a872994efb5efc0c6a23(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b354f0f45617e66d27b62ebf9a76fdbe168c6f5b6731023e6a366547233a4cb5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92d26c2b0d5b0b13ed55ca82e2b92075cdb99d8bd6d4a9122e33104a12cf9d5d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5884bd7f8fdc28919378604807977665ba3e82a47697c023e5982eb7257f557c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3eeb407208b90160e95c0fa6df04c352da355146a3ccf76bdbd6393ad76427e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d3f2e474a52e1c1e45abe4e24cd6c758600c20023f3697e0c69533c0e771bc2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ebd94616157773a4ab3988775ff92592f3cda9938c8625e395d1dbbf8406354b(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c45113a4405009713d71c8289b038f5cff241d53b81b243f0372147d29440ad9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11ba2acd464e5613cd96989e3516592dcd5684d8452b3028698e0549f5d5fafb(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnConfigurationProfile.ValidatorsProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3e2223bb16cf91626b0a44db9aa8ec9190717961f143668d3ff6961eec9abdd(
    *,
    content: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37522e89a156f185f3387aea77d01f8010adde3d2bcfeb76862a70fd9b7e08bc(
    *,
    application_id: builtins.str,
    location_uri: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    kms_key_identifier: typing.Optional[builtins.str] = None,
    retrieval_role_arn: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    type: typing.Optional[builtins.str] = None,
    validators: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationProfile.ValidatorsProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1b3c15ba63fb6169371007d7bae981d061f49c21042389030326b9ae1271344(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    application_id: builtins.str,
    configuration_profile_id: builtins.str,
    configuration_version: builtins.str,
    deployment_strategy_id: builtins.str,
    environment_id: builtins.str,
    description: typing.Optional[builtins.str] = None,
    dynamic_extension_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeployment.DynamicExtensionParametersProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    kms_key_identifier: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aaa2637a497fc43f28ee8b6e77e0f1878471c7f5bc0a736d0303ca69cb2d082c(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d3096cada1facd4de77c79fe8d588aa3d9567d81b3f913d2c2e6cf8fac54d0e(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95aaa1f67bb9531251e5f9c62292c84df7727307a58c223aaa637f0a36a3d65d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca3182ab453e0412fad7ba8649da4e0cfebf187bd90f38a026444982eb8bf50e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5abde1954bdb5d84cfce775808f90c961127e86db5ff5164bb90a98e3b0f9f20(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0527964ec5c65ed1bca366f0674e5cda5d23fe019ae479f3ee3fb550fbdb0c23(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f949624a9b6e222d754ab636966342dbb9eb207d34230837c882091a20f9abac(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96f77dd19f2c1b41d04318bc8aa9cc8f75808190471ba4922eb58652c55c5e38(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5a4416b6ac2f6fbc5dd497fd6aafe41844d2e927bc75ce571b37c2f1b805bfb(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDeployment.DynamicExtensionParametersProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98b30f15af8144546829026dccf1aaf4fedd94b59dabeb6c8e8d7bc2b71e2efb(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12211b05040a4e1a62df97a0128f266db1c0380eba8db0726824e99ad7241551(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db7299354c46559a877995ee8ab04c4fd72aaaf53cc390877fbf50f65ac43390(
    *,
    extension_reference: typing.Optional[builtins.str] = None,
    parameter_name: typing.Optional[builtins.str] = None,
    parameter_value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8289d78d65be12b91a60529d6c53d8a4385f73c87b2a23cfef86efebc1e00914(
    *,
    application_id: builtins.str,
    configuration_profile_id: builtins.str,
    configuration_version: builtins.str,
    deployment_strategy_id: builtins.str,
    environment_id: builtins.str,
    description: typing.Optional[builtins.str] = None,
    dynamic_extension_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeployment.DynamicExtensionParametersProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    kms_key_identifier: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb88c221f102c1b57ba4f19db7656eb36ff011a70e3643e39d048c313eda22fd(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    deployment_duration_in_minutes: jsii.Number,
    growth_factor: jsii.Number,
    name: builtins.str,
    replicate_to: builtins.str,
    description: typing.Optional[builtins.str] = None,
    final_bake_time_in_minutes: typing.Optional[jsii.Number] = None,
    growth_type: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c07282bd387e2aab09e9241f96ded37ff336d3f231f996e048ef207d3a38bc3(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__750f81fb9177952991767d28a4a55a4de59c55177b25056fdd45e8aff0c293c2(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2b9cfcca9dae7bf599adef5f2b44e7662994e8143e1b3ccfa6f12c4d8ad5a19(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ac4cbcedcf27ec80d55a98d836dbb9ac52523d6ff7838145b4d527fadaf652d(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43a46b42e0607ca1c01aa58dff3034f44511b63f99f559fe0fd370080f52f2c7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb6ef1a3102939b024e6e99b451674a1ad1f6879f5355a20a6d365cfeab4ad4e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f47275a573fd911ba6db69f152dd00eab69b450d732941105375d198524fd2b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad18c900d6d84d1f1dba268d6d666b830e5e5276badda4b775deb06725f3c4ea(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38dbe338fc520a7ce3134f048d86265b2db4966fa73c38281b48ff6124acbc16(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b0c7e44af284b89d6923411489d05fa28350784f8d88a837a0d019a1d575e65(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__199999cc14040404b938fa601301d483ec681a01c3bd23495d2d90dde59820b5(
    *,
    deployment_duration_in_minutes: jsii.Number,
    growth_factor: jsii.Number,
    name: builtins.str,
    replicate_to: builtins.str,
    description: typing.Optional[builtins.str] = None,
    final_bake_time_in_minutes: typing.Optional[jsii.Number] = None,
    growth_type: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f357d5cab83004926812cf34c99a144f4f5d23ca26e4a818590a950622a06fc3(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    application_id: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    monitors: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.MonitorsProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3842dacad1a08e5d9103a4c646c8fa2385f77b6f5495fbd4dab597c037c8f09b(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2dbe73a2ef533ed22edd7fd274c6cca5a979759478da06114e8699f7b2409820(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d35c6a50b39401e18b97d5d78f1d4d92aaf846c18aa4ec32bce024a53e54c4be(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__569391bda37ae2bcb096c8b3ab953d25c7ff488899b2557c773cc8f72ee8a4cb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__154bd59aabeed21e27800d9d45bcdbb412639a65e9aaaf72ef6dae673fa26a43(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8d099ead34dfe7be9eb945722b31207889d993d21d927e1eeba6592c7f8fd44(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnEnvironment.MonitorsProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60701727c0b2b8f0404d231ccc24899f35678bacc781ed4c6443de1b14432f68(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__252b3a605905895f1b8ffc133b32547c64db1b58b121d4f635ec61960b027938(
    *,
    alarm_arn: builtins.str,
    alarm_role_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43d91f41d1c9d1acd545d0999d47687e0e5b7be03ec08728e3c5aa73ff76549f(
    *,
    alarm_arn: typing.Optional[builtins.str] = None,
    alarm_role_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6c9856f1a5a9dfaed9be42ec835bb6eac4d4882999b993cbd02b3b11bbfe1ca(
    *,
    application_id: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    monitors: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.MonitorsProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3442a7f4d7a9c3256544c6b0526d285ef0cf3970ec1f140b344aed1abc4eef5(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    actions: typing.Any,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union[CfnExtension.ParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6930a24c04bd5aebe54f7a225f7ec08743e520b61a781973e88a4b6678524a5(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57070195544dc008ade09c677ffa495cf4120e6b1dc834d6ffa101c3cf189599(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f734d5e14d1ac32f7ec277282f23b1f2f7c0b8ce8e48d8df2b080f67d200577f(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__081c55af29bf24c3599cf24134be4ce60656f052c575f59ff68c2084fa523481(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__334508667f33fe5d26ff2e39e3bcbaaea618391e439f25094004fab0d75eb718(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b38bdb75b51870401d0b83754078af02e3e6886d97a64481c3733b63a5a4c814(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ad5fbf78cb34accb172520e561c08795fbca80280af2dcc78243ceb84841d07(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, CfnExtension.ParameterProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e6cc683bfd791a6ddfdc2295e58057279b3a19bc4adc7a11fbff993fe64fe37(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58317247cdf8a690d14849381527f22c6a038c04470bb6ed420b3ade323b7e43(
    *,
    name: builtins.str,
    uri: builtins.str,
    description: typing.Optional[builtins.str] = None,
    role_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__683bc731900456f8d594ddc90d3c7fc1fcdc884942410401537639fad3d02ed1(
    *,
    required: typing.Union[builtins.bool, _IResolvable_da3f097b],
    description: typing.Optional[builtins.str] = None,
    dynamic: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2e5a069dff64a93330fdfc39cee819956ed46cafa89dc1aee558b0c288de8af(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    extension_identifier: typing.Optional[builtins.str] = None,
    extension_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
    resource_identifier: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__209622600665bfa16663cc19d0b91c8caf5c5d29f4cc7cb09fd6fba67bcb1739(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0a9f34459bdf3e807e0362d7767352a597304250be35f36b98afb6b8d6ca733(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd635cb248fd501f641536d553e5645fb6dd03b8db84e4059ddc6af591a307e8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4aa600ead50aeb1f2d5f5f5fe334e3e11a16eccfa413e5de0742f763f7938a43(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc72677d37ba0fe5b56dcbee5b8705c9e4e30a75b5d3b051bc792305dfd3deda(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ff48a7c10c5007769564f0b18da5363288efbb9ca805f7bb5a7fd93e791ec3d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d31c336e3843162aab44371392cbb25a2b62fcd270c6fc472b3f2819a21b9ea1(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__658f796ad2928720e80bab1455b7c28527f38d13b4efe7780e0a592469829ce9(
    *,
    extension_identifier: typing.Optional[builtins.str] = None,
    extension_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
    resource_identifier: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a81148d01bee60e4140891afd5b9da3eab7a3dd5f81524eaa37f895ff781df1f(
    *,
    actions: typing.Any,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union[CfnExtension.ParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f2dc9ae7157f5223a79cf8ea4a7355ec285dbe0fda348428c6e0e6cdabbb60b(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    application_id: builtins.str,
    configuration_profile_id: builtins.str,
    content: builtins.str,
    content_type: builtins.str,
    description: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    version_label: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__287f244644cef79eb3704756fc9fd6f98e693a42df76727f726091d3190ab82c(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__694959938824dc357bd7ac9b60be653c213df7cdcc44905d59d6e7d7e1182171(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97e3d21e204bcf08a8dceb763729bfb70936f6d97ed550af3dfe101fac0f4331(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4193469efc98930e2e72ffffb47c40bb1631526d907d8eaab051ac721dce3631(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac0de9d6bf3585fb47f9ad3fbb1d23a9a11447de5c02a24b6971d67ab3a7fa70(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb880ec8c47eca7663501403482ddb505ffe759b4792fa0a7236d31e1313d7fe(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d43da3f82c30824ce1a2d29683403d6e68cb792341046055e7df42a980951259(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14797876de335768bb8254a37ba88bf3300df4a568a8174a333380741acaa4b8(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__384487882c55b43a28f4a742590e489e653df19c023a94fbfacb65cdf0cf00e2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2e12025d283b0b516fc7a346d00f20eff94d8259ba3fc82c8cb240aeb05264e(
    *,
    application_id: builtins.str,
    configuration_profile_id: builtins.str,
    content: builtins.str,
    content_type: builtins.str,
    description: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    version_label: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90a444a396ae95bf4dbe20a3cba4428b472f8dc18cddec786f4ed521d3ef8224(
    input_path: builtins.str,
    content_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3dc78a8c320c476850c109277461b0640bc3492938af15c32744671285117e99(
    content: builtins.str,
    content_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0be240b695740e98f6925d6eb7c6948c1cdff98558955885c2275a539fa4e5f0(
    content: builtins.str,
    content_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5d1c66ba91caf344acedcb9844b33debef555ae94702faf53abe298e612f662(
    content: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af127c28dd1d72bacc88a31e7606c4f0729ead8629d2aa39eca948c88e6a19f9(
    content: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d8aafff2e2f314c1c4bef6e213f0aaef56ff294051b33fee835ad5716a7e093(
    *,
    deployment_key: typing.Optional[_IKey_5f11635f] = None,
    deployment_strategy: typing.Optional[IDeploymentStrategy] = None,
    deploy_to: typing.Optional[typing.Sequence[IEnvironment]] = None,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    type: typing.Optional[ConfigurationType] = None,
    validators: typing.Optional[typing.Sequence[IValidator]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fde28a86ff967e860849eabd5d00b00f1f841ba2ded09e00655f2b7d433ef121(
    *,
    deployment_key: typing.Optional[_IKey_5f11635f] = None,
    deployment_strategy: typing.Optional[IDeploymentStrategy] = None,
    deploy_to: typing.Optional[typing.Sequence[IEnvironment]] = None,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    type: typing.Optional[ConfigurationType] = None,
    validators: typing.Optional[typing.Sequence[IValidator]] = None,
    application: IApplication,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e27dc717a0100d15b46f08976cbd9816d9234c98e20254c8d4090fd04187aa48(
    bucket: _IBucket_42e086fd,
    object_key: builtins.str,
    key: typing.Optional[_IKey_5f11635f] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f9f2ec1a2ab20cc29bcfe3f1d8216c56caff367e7c5fac53bb7e81cb5a4a385(
    document: _CfnDocument_8b177f00,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd6b66aaa0f14b1ceb91da8242ecc9bb0684df0b51abed7aa97919255659d04d(
    parameter: _IParameter_509a0f80,
    key: typing.Optional[_IKey_5f11635f] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7947957f92568ae27b5114957b81b662d25a30e2da5f3c76e8d1158c12566aca(
    pipeline: _IPipeline_0931f838,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a73d209b4025c3cdaf34909720e3249a1d3d4989e16aec9d748a6e59bb835675(
    secret: _ISecret_6e020e6a,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8463842034a8619eb54964cc08c28aa3cea9fcdbf4e58de63f128b5b5322da8(
    deployment_strategy_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b2751d6de1bb1e5195de3102d4fca0a566bedf6102d7bf2ce66a0d8291280f5(
    *,
    rollout_strategy: RolloutStrategy,
    deployment_strategy_name: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37c9050d36cf121416083b853e136100e069c334aadd707074579edb0620bf52(
    *,
    application: IApplication,
    environment_id: builtins.str,
    description: typing.Optional[builtins.str] = None,
    monitors: typing.Optional[typing.Sequence[Monitor]] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fbb7b0217b9bc7608bc896aa9827a29bb06de82b32c07cf8d98954734cdae547(
    *,
    description: typing.Optional[builtins.str] = None,
    environment_name: typing.Optional[builtins.str] = None,
    monitors: typing.Optional[typing.Sequence[Monitor]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70814b8db38d5e11a0b33e43663913fb290e190ace3191585fc4d0bd4c97bfff(
    *,
    description: typing.Optional[builtins.str] = None,
    environment_name: typing.Optional[builtins.str] = None,
    monitors: typing.Optional[typing.Sequence[Monitor]] = None,
    application: IApplication,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11f1d1fbf4b9190d06fa9b9ba49d1f42b2396559148c034133b90f93955b93cc(
    *,
    extension_id: builtins.str,
    extension_version_number: jsii.Number,
    actions: typing.Optional[typing.Sequence[Action]] = None,
    description: typing.Optional[builtins.str] = None,
    extension_arn: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e71eebf3abb67e3bfb63792c1df83d0e0e153e5e160fd92004f78031c885a39(
    *,
    description: typing.Optional[builtins.str] = None,
    extension_name: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Sequence[Parameter]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__003bfe5f4d042a69eceddde85ccfcfdb2e64aaea78e2842680880437998cd38f(
    *,
    description: typing.Optional[builtins.str] = None,
    extension_name: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Sequence[Parameter]] = None,
    actions: typing.Sequence[Action],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c4d8fda2e4860630073eda40d5a32347248e82c24127624ef93e735b071da8f(
    *,
    deployment_key: typing.Optional[_IKey_5f11635f] = None,
    deployment_strategy: typing.Optional[IDeploymentStrategy] = None,
    deploy_to: typing.Optional[typing.Sequence[IEnvironment]] = None,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    type: typing.Optional[ConfigurationType] = None,
    validators: typing.Optional[typing.Sequence[IValidator]] = None,
    content: ConfigurationContent,
    latest_version_number: typing.Optional[jsii.Number] = None,
    version_label: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7cba9d5464f3f4cbc208d892995245e5078fc2cc794651c71942035a9b151b2e(
    *,
    deployment_key: typing.Optional[_IKey_5f11635f] = None,
    deployment_strategy: typing.Optional[IDeploymentStrategy] = None,
    deploy_to: typing.Optional[typing.Sequence[IEnvironment]] = None,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    type: typing.Optional[ConfigurationType] = None,
    validators: typing.Optional[typing.Sequence[IValidator]] = None,
    application: IApplication,
    content: ConfigurationContent,
    latest_version_number: typing.Optional[jsii.Number] = None,
    version_label: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb165be70f31f79374053f908981a5e02c37cbdefd4d2123a7e32165fb887042(
    id: builtins.str,
    *,
    description: typing.Optional[builtins.str] = None,
    environment_name: typing.Optional[builtins.str] = None,
    monitors: typing.Optional[typing.Sequence[Monitor]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51863d25dd80b6b2aec3914f4049011443f202b08c7c800cd559c58ed15cc0d7(
    environment: IEnvironment,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3dfb6e70c8a97e61af9439d803dd44620f78eac39e160dc612cb32b98725d2a9(
    extension: IExtension,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3bd9df804b6975de3426c197a45965f129649a986f5cd9a03f0a4ee6f3cad84d(
    id: builtins.str,
    *,
    content: ConfigurationContent,
    latest_version_number: typing.Optional[jsii.Number] = None,
    version_label: typing.Optional[builtins.str] = None,
    deployment_key: typing.Optional[_IKey_5f11635f] = None,
    deployment_strategy: typing.Optional[IDeploymentStrategy] = None,
    deploy_to: typing.Optional[typing.Sequence[IEnvironment]] = None,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    type: typing.Optional[ConfigurationType] = None,
    validators: typing.Optional[typing.Sequence[IValidator]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__652068ebd01467de1bc3159a4c8fef165c1053fe6662fcbb6e0b8cb9fec285ff(
    id: builtins.str,
    *,
    location: ConfigurationSource,
    retrieval_role: typing.Optional[_IRole_235f5d8e] = None,
    version_number: typing.Optional[builtins.str] = None,
    deployment_key: typing.Optional[_IKey_5f11635f] = None,
    deployment_strategy: typing.Optional[IDeploymentStrategy] = None,
    deploy_to: typing.Optional[typing.Sequence[IEnvironment]] = None,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    type: typing.Optional[ConfigurationType] = None,
    validators: typing.Optional[typing.Sequence[IValidator]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d755f676cf64362ca69375955a2d00058210806c720c3245a961824cd5407ab(
    action_point: ActionPoint,
    event_destination: IEventDestination,
    *,
    description: typing.Optional[builtins.str] = None,
    extension_name: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Sequence[Parameter]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be554a7ff5cf6482e867ec00580dd9f3ee89ad10ddb4c5ec39a08250191f625c(
    event_destination: IEventDestination,
    *,
    description: typing.Optional[builtins.str] = None,
    extension_name: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Sequence[Parameter]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78526e82674bf1c4a84dd0a0c976f78629d8538ec16b9c7e91aba8ef23a2ebf7(
    event_destination: IEventDestination,
    *,
    description: typing.Optional[builtins.str] = None,
    extension_name: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Sequence[Parameter]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__034f622b91f25952ad7c4bab6456b57864c9e3bc626ae6eea947fe4d08915afd(
    event_destination: IEventDestination,
    *,
    description: typing.Optional[builtins.str] = None,
    extension_name: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Sequence[Parameter]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__016aa77ef2c908d64b76cf21200f5958ff7634df1b3d77a188a8e09c7a70bd56(
    event_destination: IEventDestination,
    *,
    description: typing.Optional[builtins.str] = None,
    extension_name: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Sequence[Parameter]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71b1982dcc7245c64b03552696f23c45795d967bafdd9dc9ab92802003c78d22(
    event_destination: IEventDestination,
    *,
    description: typing.Optional[builtins.str] = None,
    extension_name: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Sequence[Parameter]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58ebf4627ce889183b1c4f07bd2d0c79f4c30add9ad5c1e7916ab5d0565c0e71(
    event_destination: IEventDestination,
    *,
    description: typing.Optional[builtins.str] = None,
    extension_name: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Sequence[Parameter]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e94c708c7603af848bf6e13c31c0fc2a81ad1aa833b38ab455b5a4db91d0835(
    event_destination: IEventDestination,
    *,
    description: typing.Optional[builtins.str] = None,
    extension_name: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Sequence[Parameter]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f39f9fc38c2348c1cbb526adb681012a66d9e97575dc37ba0af87ab3bc3eddc(
    configuration: IConfiguration,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44b48a1bae27d9166bf28c62529963c2221d313260dbc1e9f5239536a54010d5(
    *configurations: IConfiguration,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21f3fd9d8706d2da33872e0f177690ef7904e1a5bffb8f09838105674dab79cf(
    extension: IExtension,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f223f0108afb5683d5788fc1fb9f93cbd4c76cb5698d6aae016951683e8148ee(
    grantee: _IGrantable_71c4f5de,
    *actions: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9980f2056195344785f7b36a405e0d1227ad963e409c454217caf9b0e4ab2c9d(
    grantee: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a99dab2b60d71d853252dc1cd4c58e0db20f0d3344869d8b3c0078d823053f47(
    action_point: ActionPoint,
    event_destination: IEventDestination,
    *,
    description: typing.Optional[builtins.str] = None,
    extension_name: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Sequence[Parameter]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bef62040c375bd2337f0d3e61b60a7c152f6460a98daef5742016059a14271a8(
    event_destination: IEventDestination,
    *,
    description: typing.Optional[builtins.str] = None,
    extension_name: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Sequence[Parameter]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d011fee22ec2026b2d30ec4752fd2b51dd4643c49774a9c6e595752709d9ce26(
    event_destination: IEventDestination,
    *,
    description: typing.Optional[builtins.str] = None,
    extension_name: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Sequence[Parameter]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80820f672394fd7f1353941a67dfc3c0f6661b448abcd5dbefa5d17e6beee7cf(
    event_destination: IEventDestination,
    *,
    description: typing.Optional[builtins.str] = None,
    extension_name: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Sequence[Parameter]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e495273d9b8cd07ab5fafbb39bb5f77a539112c335e202da5fc32fdf8a9e350a(
    event_destination: IEventDestination,
    *,
    description: typing.Optional[builtins.str] = None,
    extension_name: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Sequence[Parameter]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__934644fa645d264ebfb46e1fbc7a539792a455110f9ccc0c772308cb0cd2b3b2(
    event_destination: IEventDestination,
    *,
    description: typing.Optional[builtins.str] = None,
    extension_name: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Sequence[Parameter]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8730b489063898186752e5bbb505fc429ca40b3257aadac613dd158db05049ae(
    event_destination: IEventDestination,
    *,
    description: typing.Optional[builtins.str] = None,
    extension_name: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Sequence[Parameter]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11a5b9a15937937180da1889814f9b51e695b3dda7f18fad38f06693f0bf3bcd(
    event_destination: IEventDestination,
    *,
    description: typing.Optional[builtins.str] = None,
    extension_name: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Sequence[Parameter]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__636f478c5d08860b2bd38ade9249d6b6fb935a98206f256a2ce4651910bc75d2(
    extension: IExtension,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e51cabd347b530685c4f785d2c1fa5904d0191b12572fa1c83b4ee1b4e018cb4(
    action_point: ActionPoint,
    event_destination: IEventDestination,
    *,
    description: typing.Optional[builtins.str] = None,
    extension_name: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Sequence[Parameter]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6fa7ec332edec343e312eed71e77af42754053e46d5f53a5d9e9553a39b901bd(
    event_destination: IEventDestination,
    *,
    description: typing.Optional[builtins.str] = None,
    extension_name: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Sequence[Parameter]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81b022234ee1ebf91a3c01114a87d92835d32179a6a8002d81fd0d6bca9a56b5(
    event_destination: IEventDestination,
    *,
    description: typing.Optional[builtins.str] = None,
    extension_name: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Sequence[Parameter]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf6b6442be5cf3ca27f13266e178b6af166e7da8b09b6a4488c37c5d4f316321(
    event_destination: IEventDestination,
    *,
    description: typing.Optional[builtins.str] = None,
    extension_name: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Sequence[Parameter]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b18a5bb1eeef9a5b8cc629ae95374f939f48bc090b42485b360fb085c2325636(
    event_destination: IEventDestination,
    *,
    description: typing.Optional[builtins.str] = None,
    extension_name: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Sequence[Parameter]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b9f21b4a7c2b4d829a87f00606d3b497186ac272a0e388ed8b46a67d80e3b42(
    event_destination: IEventDestination,
    *,
    description: typing.Optional[builtins.str] = None,
    extension_name: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Sequence[Parameter]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d9383750894ef15ea5397fbe279df0dfa736eb00f19f0da10a9876cbafe3d26(
    event_destination: IEventDestination,
    *,
    description: typing.Optional[builtins.str] = None,
    extension_name: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Sequence[Parameter]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d882c483f3b7fe82114c8c7963525171dd0a2605c29b70221b2a01606bda297a(
    event_destination: IEventDestination,
    *,
    description: typing.Optional[builtins.str] = None,
    extension_name: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Sequence[Parameter]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78883cc72a23f294c8f7fa290505676f4a7bab645b06f048344b15590a97acae(
    input_path: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ac39b4aca41716a9c0c911538ffd870eaabc02b68632f8b0cee4708ca0935da(
    code: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c652c76ed075aa64f62bcabc7e6b60f2d86c05f769c17fb271ed8405259f68bb(
    func: _IFunction_6adb0ab8,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a245d9ad2d5a72963867d7f392bf31c9977c87f33b0ba8389f1024ee4eecad9e(
    func: _Function_244f85d8,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ccc59f1c5523364b8528526a5b6087774df2b905407caca37b7c685a5bfb76cb(
    alarm: _IAlarm_ff3eabc0,
    alarm_role: typing.Optional[_IRole_235f5d8e] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e86480f6d31f87043e7defee36f9e4716c05611a4f0372a521151cc2c7968eac(
    name: builtins.str,
    value: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c36eea0e8c419bcd42c01216c20d5a8f57657c660596cf07a801d4c269c0306(
    name: builtins.str,
    value: builtins.str,
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd34e38231115cf062a079b568bd536f7138f65ab8fb9db0b917b7c17c03e75b(
    *,
    deployment_duration: _Duration_4839e8c3,
    growth_factor: jsii.Number,
    final_bake_time: typing.Optional[_Duration_4839e8c3] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7717c5cbe1c0c49e9bad0179c39c84fc906b10056fbae28b785806ae0d939597(
    topic: _ITopic_9eca4852,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61200a738f2584e5d86190492c99ded9cebb5cc41d230eec1c74f7130b50cb6e(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    location: ConfigurationSource,
    retrieval_role: typing.Optional[_IRole_235f5d8e] = None,
    version_number: typing.Optional[builtins.str] = None,
    application: IApplication,
    deployment_key: typing.Optional[_IKey_5f11635f] = None,
    deployment_strategy: typing.Optional[IDeploymentStrategy] = None,
    deploy_to: typing.Optional[typing.Sequence[IEnvironment]] = None,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    type: typing.Optional[ConfigurationType] = None,
    validators: typing.Optional[typing.Sequence[IValidator]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__567a975af03924cb099dbb4e55da080a85101964698787ded85c7d42f63cd3b5(
    extension: IExtension,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63ed4552787e88def66e9a8b0abdb2cf11f84235e5089c5e232a1053e6059ecc(
    action_point: ActionPoint,
    event_destination: IEventDestination,
    *,
    description: typing.Optional[builtins.str] = None,
    extension_name: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Sequence[Parameter]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a145ea507639ac2b7073bd0f352974744e3821459664f412348146516ee16082(
    event_destination: IEventDestination,
    *,
    description: typing.Optional[builtins.str] = None,
    extension_name: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Sequence[Parameter]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0fe8f4ebcc7ac2ce0b33ab896176c13c0f82e5bd7bf4396cdfbb5e837e3ec16d(
    event_destination: IEventDestination,
    *,
    description: typing.Optional[builtins.str] = None,
    extension_name: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Sequence[Parameter]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64649b15b58a938933f677b7b099e3ead2b877aef924bed10aa8fd894977cb18(
    event_destination: IEventDestination,
    *,
    description: typing.Optional[builtins.str] = None,
    extension_name: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Sequence[Parameter]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a72a20510f9367a1ef380b113df52cc7b9a3191df20f658f8fafce65cf900ef(
    event_destination: IEventDestination,
    *,
    description: typing.Optional[builtins.str] = None,
    extension_name: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Sequence[Parameter]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__918c62fffe22d9133a92395bb9d8eb25cb55764c05a34180ae8212464e093e09(
    event_destination: IEventDestination,
    *,
    description: typing.Optional[builtins.str] = None,
    extension_name: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Sequence[Parameter]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71565cf401ee87c96ccfb60887b1f50eea8c2e04bc591d9804604fc7923acb19(
    event_destination: IEventDestination,
    *,
    description: typing.Optional[builtins.str] = None,
    extension_name: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Sequence[Parameter]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f65a8de4cec461bba4019fd73ca34ff5fcaf12f9911f7d1bea01ee3e18caf136(
    event_destination: IEventDestination,
    *,
    description: typing.Optional[builtins.str] = None,
    extension_name: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Sequence[Parameter]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0e9989f54c29397e556923d6dc5808d84cb6c3a5de0ea3c83ce4461584c451e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af782e66a589643c3273915140536d8c7931cca7f2adf6a0fc45e67b9228eebf(
    value: ExtensibleBase,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__115deabe7a02ce295c431e7d9a99bcbe112bc017436380d80181c5db491187a1(
    *,
    deployment_key: typing.Optional[_IKey_5f11635f] = None,
    deployment_strategy: typing.Optional[IDeploymentStrategy] = None,
    deploy_to: typing.Optional[typing.Sequence[IEnvironment]] = None,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    type: typing.Optional[ConfigurationType] = None,
    validators: typing.Optional[typing.Sequence[IValidator]] = None,
    location: ConfigurationSource,
    retrieval_role: typing.Optional[_IRole_235f5d8e] = None,
    version_number: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d41101d1b0f699a52d44a2b86fe3e9dcd0e6f1487f088908464eb49cb3e5e12c(
    *,
    deployment_key: typing.Optional[_IKey_5f11635f] = None,
    deployment_strategy: typing.Optional[IDeploymentStrategy] = None,
    deploy_to: typing.Optional[typing.Sequence[IEnvironment]] = None,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    type: typing.Optional[ConfigurationType] = None,
    validators: typing.Optional[typing.Sequence[IValidator]] = None,
    application: IApplication,
    location: ConfigurationSource,
    retrieval_role: typing.Optional[_IRole_235f5d8e] = None,
    version_number: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c28280d4c69ff29c8717c5fad93f2870bc55344bfbee733f6c2105ed3497ab5b(
    queue: _IQueue_7ed6f679,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1e564dd652de62b6550596a7830dbc1244bd584b24647a457f2e0424816f76e(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    application_name: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18d0bc0084bf434e4353d076c6c6a72311baedc58526dd0fcd93d827e77fc2d9(
    task_def: _TaskDefinition_a541a103,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76e4fec3d46016fd59c8bd0733b8dac8db60ebadadc4e94e6bfb10742e1d7435(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    application_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3cdd944facfa98bfbfbebc6eb2e937c4f847d03f65d52d4a9068926fe2c93f61(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    application_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f23af9ea4630280fc41549b208a41050e1d321a3300899bad1754e76fac80c00(
    region: builtins.str,
    platform: typing.Optional[Platform] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fbd38f9aba7df4d45f96d0029239a2f96f2fcad218a295b86c260e75cde6f20a(
    id: builtins.str,
    *,
    description: typing.Optional[builtins.str] = None,
    environment_name: typing.Optional[builtins.str] = None,
    monitors: typing.Optional[typing.Sequence[Monitor]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16233ddf7a1e42dc23f4bda96b70ec9417da6d3fedfafeec39f99b911d35656e(
    environment: IEnvironment,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97553b8fa0201fc58b21e96c914a619a1f6afeeb493a7ec1e67046be7d15a722(
    extension: IExtension,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b18310538532e3e3e53af99bb5da0c248186673a38a5175633a0149cf8ae0af(
    id: builtins.str,
    *,
    content: ConfigurationContent,
    latest_version_number: typing.Optional[jsii.Number] = None,
    version_label: typing.Optional[builtins.str] = None,
    deployment_key: typing.Optional[_IKey_5f11635f] = None,
    deployment_strategy: typing.Optional[IDeploymentStrategy] = None,
    deploy_to: typing.Optional[typing.Sequence[IEnvironment]] = None,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    type: typing.Optional[ConfigurationType] = None,
    validators: typing.Optional[typing.Sequence[IValidator]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c0399b30aac3a09a4a5e9f3f33f358c90afa60099a7dd6cfc1f1b40ff373215(
    id: builtins.str,
    *,
    location: ConfigurationSource,
    retrieval_role: typing.Optional[_IRole_235f5d8e] = None,
    version_number: typing.Optional[builtins.str] = None,
    deployment_key: typing.Optional[_IKey_5f11635f] = None,
    deployment_strategy: typing.Optional[IDeploymentStrategy] = None,
    deploy_to: typing.Optional[typing.Sequence[IEnvironment]] = None,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    type: typing.Optional[ConfigurationType] = None,
    validators: typing.Optional[typing.Sequence[IValidator]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__727774ca5ea7bba2fa87dc8ad6f91306047bf14b07d86949cc12510628c56ec2(
    action_point: ActionPoint,
    event_destination: IEventDestination,
    *,
    description: typing.Optional[builtins.str] = None,
    extension_name: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Sequence[Parameter]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__134b1acb6af5ac0c469c09cb9c572fc82e8a942398a4c09aa8f2c8b97953aa12(
    event_destination: IEventDestination,
    *,
    description: typing.Optional[builtins.str] = None,
    extension_name: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Sequence[Parameter]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43cf11a606f3bce0aaad5e1befddf0a9458ad3ff320049d375379fbbd55e106e(
    event_destination: IEventDestination,
    *,
    description: typing.Optional[builtins.str] = None,
    extension_name: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Sequence[Parameter]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e75df1a62410c2ab540f65a3a2294952a49aac8ea5def188ee109a52eb3d3ff(
    event_destination: IEventDestination,
    *,
    description: typing.Optional[builtins.str] = None,
    extension_name: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Sequence[Parameter]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af4fa8c37c6e1a14ec8b5a2243b1f62d1182e4551cd8d7247c737964514b946f(
    event_destination: IEventDestination,
    *,
    description: typing.Optional[builtins.str] = None,
    extension_name: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Sequence[Parameter]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20656d70f751052e70a657c2ab0b4d42341ae80f5507359b32d99b7e89e6b5a4(
    event_destination: IEventDestination,
    *,
    description: typing.Optional[builtins.str] = None,
    extension_name: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Sequence[Parameter]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__299d964c2aac2516ce8b1125bb695b718f5f425a8b70c26c082dff2413b12032(
    event_destination: IEventDestination,
    *,
    description: typing.Optional[builtins.str] = None,
    extension_name: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Sequence[Parameter]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af63cf64ce7c3fe83523222dceaef56e9447ce8f6a2afb5d2567c6c9792f3543(
    event_destination: IEventDestination,
    *,
    description: typing.Optional[builtins.str] = None,
    extension_name: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Sequence[Parameter]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82766fd65d19c222e55a3bd3d37a0ce2dbc32473446dfef2bbba053456f75dd9(
    value: ExtensibleBase,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__355f732c5b86477a8c74b5d90e398dea8eb36c47e6f7eb1df2958e42495a6598(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    rollout_strategy: RolloutStrategy,
    deployment_strategy_name: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b37d45983b2147369edbbbb7365fa518ba24fcce4bb42681de698092ccc6be4(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    deployment_strategy_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75327d45b26489bd7407fafc6ad0df26d223ce07225e44f5e5383facc04fcf58(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    deployment_strategy_id: DeploymentStrategyId,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09c6baa2088c107dc1834ea8f2a8c0f35612bf3782c77c3ef6879f99339a8ca7(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    application: IApplication,
    description: typing.Optional[builtins.str] = None,
    environment_name: typing.Optional[builtins.str] = None,
    monitors: typing.Optional[typing.Sequence[Monitor]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85f387eeef7a94f96ab485e8173f4b432330c3d2f02329d4f772d886d0070f5a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    environment_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d0acdd2bc2062b1e3a3bcead8b9d2670bef03c315b3aa44522a2099520a2b48(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    application: IApplication,
    environment_id: builtins.str,
    description: typing.Optional[builtins.str] = None,
    monitors: typing.Optional[typing.Sequence[Monitor]] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60a6cee655356c4a43230057c8909db67a6239e7701192ff39fda6b5549a6672(
    configuration: IConfiguration,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a87ca2c61c81bb433441138d696247c8865c67883b0937278f3b0aa320b5db0(
    *configurations: IConfiguration,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46eeb9c815b4c9f3f9ff6e64ae0bba20fa3057be7b74747b611ea672668a95cf(
    extension: IExtension,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c65f9ec077d5abb2638f74671e3f2d65ef4fed80c0e32561b7b807b917e7d53(
    grantee: _IGrantable_71c4f5de,
    *actions: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__790a777ba7325eb4b088cf4fe3be2b4fdcc0c100050d537316abc7125c7f326f(
    identity: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c5b20c6ba105fc862af761c49db56fe32fde770ccf217e82ae6d4ae54bada0f(
    action_point: ActionPoint,
    event_destination: IEventDestination,
    *,
    description: typing.Optional[builtins.str] = None,
    extension_name: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Sequence[Parameter]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f4454f449feb8e261a065afd7db0ca3cc40df93581582d67a92531c61da1458(
    event_destination: IEventDestination,
    *,
    description: typing.Optional[builtins.str] = None,
    extension_name: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Sequence[Parameter]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78f9cb6929bf857fb78f3e50ae777f7ad0b72a8340597d58727ccec6d8285614(
    event_destination: IEventDestination,
    *,
    description: typing.Optional[builtins.str] = None,
    extension_name: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Sequence[Parameter]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8127118f73782a3390b7d2b32acfd493beb5de7191565a608f9420135471066(
    event_destination: IEventDestination,
    *,
    description: typing.Optional[builtins.str] = None,
    extension_name: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Sequence[Parameter]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62b75fa8040428cb2e8eaedd119654e80a90641410e1e58a25ccf041128aeaf4(
    event_destination: IEventDestination,
    *,
    description: typing.Optional[builtins.str] = None,
    extension_name: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Sequence[Parameter]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3903e077af062c1b31f63d11710d11cc5807cb4fdd9694d38a86e3050f67a068(
    event_destination: IEventDestination,
    *,
    description: typing.Optional[builtins.str] = None,
    extension_name: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Sequence[Parameter]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f574c3024d31be00420b36fcfec7902de0226ae4a571a80f5e6502c34900f5fa(
    event_destination: IEventDestination,
    *,
    description: typing.Optional[builtins.str] = None,
    extension_name: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Sequence[Parameter]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22ccb2ca13f7df2815220f1d2cdda0fb9d20c17ac1fafb9dcc50064559b9a066(
    event_destination: IEventDestination,
    *,
    description: typing.Optional[builtins.str] = None,
    extension_name: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Sequence[Parameter]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd39d7b7b77c944582e5f7fabeb3e37717eaa470540d764633f9ce909058030a(
    value: typing.List[CfnDeployment],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f249899e37c9153afa9dc39542328ce1c247c1f209ac134fb2bc8a4ad1120946(
    value: ExtensibleBase,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80f21051c7734c306113ac626a6c5c630b229e3c1cb7444771ec9a9a993a7a3f(
    bus: _IEventBus_88d13111,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__859c379a4d03dea0c0fd17b7fd6acf3b7d65d43c3c4b856443463daca4ef489c(
    scope: _constructs_77d1e7e8.Construct,
    resource_arn: builtins.str,
    resource_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6a9c7f9aa42fa6ded0470d92dbcd83940a578472e76af9396bdbd356d3926fc(
    extension: IExtension,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a6722e71c8fd1cc15e9b19f2e0909d6bbb97c17169577f39de30b2d1260a131(
    action_point: ActionPoint,
    event_destination: IEventDestination,
    *,
    description: typing.Optional[builtins.str] = None,
    extension_name: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Sequence[Parameter]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec27ee4753650addf32b95b09fec2cb92d81a9c9171b0c84cf371c07727fbcb6(
    event_destination: IEventDestination,
    *,
    description: typing.Optional[builtins.str] = None,
    extension_name: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Sequence[Parameter]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b10722268778e5ad348b053b6dfa3088b7136433373392d19ffe8fa94f3e69cf(
    event_destination: IEventDestination,
    *,
    description: typing.Optional[builtins.str] = None,
    extension_name: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Sequence[Parameter]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4463425263eafb5ee62382d54de44afc2b669415871a836ff016494929fd805(
    event_destination: IEventDestination,
    *,
    description: typing.Optional[builtins.str] = None,
    extension_name: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Sequence[Parameter]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35795185ba628914eac8facd076158729a01914ea36274cabb0a1b1a7199fe79(
    event_destination: IEventDestination,
    *,
    description: typing.Optional[builtins.str] = None,
    extension_name: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Sequence[Parameter]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__040c76c87c97ded56b6f961a3f12386f7e3a3eae5691a332b2449e12945de1a3(
    event_destination: IEventDestination,
    *,
    description: typing.Optional[builtins.str] = None,
    extension_name: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Sequence[Parameter]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0876520af8e864feae7bfca8859c4660ea6a7c7ae48c3755fa69e58161cd6866(
    event_destination: IEventDestination,
    *,
    description: typing.Optional[builtins.str] = None,
    extension_name: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Sequence[Parameter]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a2539aa3c7790e56e2d710cf16d21806637a211078c85589485c38d18db2d34(
    event_destination: IEventDestination,
    *,
    description: typing.Optional[builtins.str] = None,
    extension_name: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Sequence[Parameter]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2651da7526c7d2966c70f3f4d4a570b1b30f5f6ee97508d27ddc0afdeffa5b68(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    actions: typing.Sequence[Action],
    description: typing.Optional[builtins.str] = None,
    extension_name: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Sequence[Parameter]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__675381e6515f056b4ecc6dca61eda68802c57de4687430e36e54e9b24d670c34(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    extension_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72f1e669cca59ef8756f1a767c7447e601a93a5765f9603a3f36fcc4077bf272(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    extension_id: builtins.str,
    extension_version_number: jsii.Number,
    actions: typing.Optional[typing.Sequence[Action]] = None,
    description: typing.Optional[builtins.str] = None,
    extension_arn: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e7eecc550d3d689f07534db869c7be67f00e08dcbf880bbb2656d01940aa8e8(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    content: ConfigurationContent,
    latest_version_number: typing.Optional[jsii.Number] = None,
    version_label: typing.Optional[builtins.str] = None,
    application: IApplication,
    deployment_key: typing.Optional[_IKey_5f11635f] = None,
    deployment_strategy: typing.Optional[IDeploymentStrategy] = None,
    deploy_to: typing.Optional[typing.Sequence[IEnvironment]] = None,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    type: typing.Optional[ConfigurationType] = None,
    validators: typing.Optional[typing.Sequence[IValidator]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dcffd5e999d1df96cb081e766c8016c4aa0123304ff23d455b57cbab7e0b7685(
    extension: IExtension,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2cdc0ffbe5a8630ebd90111a737ca2b967dee69b1b2b68149dd3251cce675208(
    action_point: ActionPoint,
    event_destination: IEventDestination,
    *,
    description: typing.Optional[builtins.str] = None,
    extension_name: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Sequence[Parameter]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ceda34dc0d119d50cc7ecc5a567ff2fc5c604fc1bb576ec935fb8335caf48c74(
    event_destination: IEventDestination,
    *,
    description: typing.Optional[builtins.str] = None,
    extension_name: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Sequence[Parameter]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95fca11df6f0876cf9825441d8ff70e095a2215e4eb6550fd49e603838afe3ca(
    event_destination: IEventDestination,
    *,
    description: typing.Optional[builtins.str] = None,
    extension_name: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Sequence[Parameter]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bac203b4ea30df38ac6f158d19b1afc4955e500a8830d6e3e75b448a1b98937b(
    event_destination: IEventDestination,
    *,
    description: typing.Optional[builtins.str] = None,
    extension_name: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Sequence[Parameter]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2fd8a68a1ddc7aca359954daa777db0d209ac14b7b24a6ba5b435bafd3b718bd(
    event_destination: IEventDestination,
    *,
    description: typing.Optional[builtins.str] = None,
    extension_name: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Sequence[Parameter]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7673b3ddc8b5478788c8347bb28dece31c205a8030ce432584227064e3e7dbd1(
    event_destination: IEventDestination,
    *,
    description: typing.Optional[builtins.str] = None,
    extension_name: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Sequence[Parameter]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3b0e26d65395b369b7b5023f0ce3b98d1c183d44f8cad8b1ec1a7ea1edc936b(
    event_destination: IEventDestination,
    *,
    description: typing.Optional[builtins.str] = None,
    extension_name: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Sequence[Parameter]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40083372633c70683c32dc01cf6546ae2759ee8aa8001f03ec550ad5578f1e4f(
    event_destination: IEventDestination,
    *,
    description: typing.Optional[builtins.str] = None,
    extension_name: typing.Optional[builtins.str] = None,
    latest_version_number: typing.Optional[jsii.Number] = None,
    parameters: typing.Optional[typing.Sequence[Parameter]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4058b9695ce055c514ee6b279cac6589d3ab9aa62414133fc4992ec610aa1d5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27c25acd80a9bdc9870365bad92556272569854dc957ad7cdf2b6e5a2c29c2ce(
    value: ExtensibleBase,
) -> None:
    """Type checking stubs"""
    pass
