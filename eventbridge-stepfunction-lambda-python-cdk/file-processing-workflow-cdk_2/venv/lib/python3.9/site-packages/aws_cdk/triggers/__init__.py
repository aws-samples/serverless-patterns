'''
# Triggers

Triggers allows you to execute code during deployments. This can be used for a
variety of use cases such as:

* Self tests: validate something after a resource/construct been provisioned
* Data priming: add initial data to resources after they are created
* Preconditions: check things such as account limits or external dependencies
  before deployment.

## Usage

The `TriggerFunction` construct will define an AWS Lambda function which is
triggered *during* deployment:

```python
import aws_cdk.triggers as triggers


triggers.TriggerFunction(self, "MyTrigger",
    runtime=lambda_.Runtime.NODEJS_14_X,
    handler="index.handler",
    code=lambda_.Code.from_asset(__dirname + "/my-trigger")
)
```

In the above example, the AWS Lambda function defined in `MyTrigger` will
be invoked when the stack is deployed.

It is also possible to trigger a predefined Lambda function by using the `Trigger` construct:

```python
import aws_cdk.triggers as triggers


func = lambda_.Function(self, "MyFunction",
    handler="index.handler",
    runtime=lambda_.Runtime.NODEJS_14_X,
    code=lambda_.Code.from_inline("foo")
)

triggers.Trigger(self, "MyTrigger",
    handler=func,
    timeout=Duration.minutes(10),
    invocation_type=triggers.InvocationType.EVENT
)
```

Addition properties can be used to fine-tune the behaviour of the trigger.
The `timeout` property can be used to determine how long the invocation of the function should take.
The `invocationType` property can be used to change the invocation type of the function.
This might be useful in scenarios where a fire-and-forget strategy for invoking the function is sufficient.

## Trigger Failures

If the trigger handler fails (e.g. an exception is raised), the CloudFormation
deployment will fail, as if a resource failed to provision. This makes it easy
to implement "self tests" via triggers by simply making a set of assertions on
some provisioned infrastructure.

Note that this behavior is only applied when invocationType is `REQUEST_RESPONSE`. When invocationType is `EVENT`, Lambda function is invoked asynchronously.
In that case, if Lambda function is invoked successfully, the trigger will success regardless of the result for the function execution.

## Order of Execution

By default, a trigger will be executed by CloudFormation after the associated
handler is provisioned. This means that if the handler takes an implicit
dependency on other resources (e.g. via environment variables), those resources
will be provisioned *before* the trigger is executed.

In most cases, implicit ordering should be sufficient, but you can also use
`executeAfter` and `executeBefore` to control the order of execution.

The following example defines the following order: `(hello, world) => myTrigger => goodbye`.
The resources under `hello` and `world` will be provisioned in
parallel, and then the trigger `myTrigger` will be executed. Only then the
resources under `goodbye` will be provisioned:

```python
import aws_cdk.triggers as triggers

# my_trigger: triggers.Trigger
# hello: Construct
# world: Construct
# goodbye: Construct


my_trigger.execute_after(hello, world)
my_trigger.execute_before(goodbye)
```

Note that `hello` and `world` are construct *scopes*. This means that they can
be specific resources (such as an `s3.Bucket` object) or groups of resources
composed together into constructs.

## Re-execution of Triggers

By default, `executeOnHandlerChange` is enabled. This implies that the trigger
is re-executed every time the handler function code or configuration changes. If
this option is disabled, the trigger will be executed only once upon first
deployment.

In the future we will consider adding support for additional re-execution modes:

* `executeOnEveryDeployment: boolean` - re-executes every time the stack is
  deployed (add random "salt" during synthesis).
* `executeOnResourceChange: Construct[]` - re-executes when one of the resources
  under the specified scopes has changed (add the hash the CloudFormation
  resource specs).
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
from .. import Duration as _Duration_4839e8c3, Size as _Size_7b441c34
from ..aws_codeguruprofiler import IProfilingGroup as _IProfilingGroup_0bba72c4
from ..aws_ec2 import (
    ISecurityGroup as _ISecurityGroup_acf8a799,
    IVpc as _IVpc_f30d5663,
    SubnetSelection as _SubnetSelection_e57d76df,
)
from ..aws_iam import (
    IRole as _IRole_235f5d8e, PolicyStatement as _PolicyStatement_0fe33853
)
from ..aws_kms import IKey as _IKey_5f11635f
from ..aws_lambda import (
    AdotInstrumentationConfig as _AdotInstrumentationConfig_7c38d65d,
    Architecture as _Architecture_12d5a53f,
    Code as _Code_7848f942,
    FileSystem as _FileSystem_a5fa005d,
    Function as _Function_244f85d8,
    FunctionProps as _FunctionProps_a308e854,
    ICodeSigningConfig as _ICodeSigningConfig_edb41d1f,
    IDestination as _IDestination_40f19de4,
    IEventSource as _IEventSource_3686b3f8,
    ILayerVersion as _ILayerVersion_5ac127c8,
    LambdaInsightsVersion as _LambdaInsightsVersion_9dfbfef9,
    LogRetentionRetryOptions as _LogRetentionRetryOptions_ad797a7a,
    ParamsAndSecretsLayerVersion as _ParamsAndSecretsLayerVersion_dce97f06,
    Runtime as _Runtime_b4eaa844,
    RuntimeManagementMode as _RuntimeManagementMode_688c173b,
    Tracing as _Tracing_9fe8e2bb,
    VersionOptions as _VersionOptions_981bb3c0,
)
from ..aws_logs import RetentionDays as _RetentionDays_070f99f0
from ..aws_sns import ITopic as _ITopic_9eca4852
from ..aws_sqs import IQueue as _IQueue_7ed6f679


@jsii.interface(jsii_type="aws-cdk-lib.triggers.ITrigger")
class ITrigger(_constructs_77d1e7e8.IConstruct, typing_extensions.Protocol):
    '''Interface for triggers.'''

    @jsii.member(jsii_name="executeAfter")
    def execute_after(self, *scopes: _constructs_77d1e7e8.Construct) -> None:
        '''Adds trigger dependencies.

        Execute this trigger only after these construct
        scopes have been provisioned.

        :param scopes: A list of construct scopes which this trigger will depend on.
        '''
        ...

    @jsii.member(jsii_name="executeBefore")
    def execute_before(self, *scopes: _constructs_77d1e7e8.Construct) -> None:
        '''Adds this trigger as a dependency on other constructs.

        This means that this
        trigger will get executed *before* the given construct(s).

        :param scopes: A list of construct scopes which will take a dependency on this trigger.
        '''
        ...


class _ITriggerProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
):
    '''Interface for triggers.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.triggers.ITrigger"

    @jsii.member(jsii_name="executeAfter")
    def execute_after(self, *scopes: _constructs_77d1e7e8.Construct) -> None:
        '''Adds trigger dependencies.

        Execute this trigger only after these construct
        scopes have been provisioned.

        :param scopes: A list of construct scopes which this trigger will depend on.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1440952b0ad66bce206afd39f8df5d3131d1aec936e757ff45565c33d8e743de)
            check_type(argname="argument scopes", value=scopes, expected_type=typing.Tuple[type_hints["scopes"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "executeAfter", [*scopes]))

    @jsii.member(jsii_name="executeBefore")
    def execute_before(self, *scopes: _constructs_77d1e7e8.Construct) -> None:
        '''Adds this trigger as a dependency on other constructs.

        This means that this
        trigger will get executed *before* the given construct(s).

        :param scopes: A list of construct scopes which will take a dependency on this trigger.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83c288d084243ca76dbe90e11a2ed762e4f9ff4be79125b9325e2b639f9bf225)
            check_type(argname="argument scopes", value=scopes, expected_type=typing.Tuple[type_hints["scopes"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "executeBefore", [*scopes]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITrigger).__jsii_proxy_class__ = lambda : _ITriggerProxy


@jsii.enum(jsii_type="aws-cdk-lib.triggers.InvocationType")
class InvocationType(enum.Enum):
    '''The invocation type to apply to a trigger.

    This determines whether the trigger function should await the result of the to be triggered function or not.

    :exampleMetadata: infused

    Example::

        import aws_cdk.triggers as triggers
        
        
        func = lambda_.Function(self, "MyFunction",
            handler="index.handler",
            runtime=lambda_.Runtime.NODEJS_14_X,
            code=lambda_.Code.from_inline("foo")
        )
        
        triggers.Trigger(self, "MyTrigger",
            handler=func,
            timeout=Duration.minutes(10),
            invocation_type=triggers.InvocationType.EVENT
        )
    '''

    EVENT = "EVENT"
    '''Invoke the function asynchronously.

    Send events that fail multiple times to the function's dead-letter queue (if one is configured).
    The API response only includes a status code.
    '''
    REQUEST_RESPONSE = "REQUEST_RESPONSE"
    '''Invoke the function synchronously.

    Keep the connection open until the function returns a response or times out.
    The API response includes the function response and additional data.
    '''
    DRY_RUN = "DRY_RUN"
    '''Validate parameter values and verify that the user or role has permission to invoke the function.'''


@jsii.implements(ITrigger)
class Trigger(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.triggers.Trigger",
):
    '''Triggers an AWS Lambda function during deployment.

    :exampleMetadata: infused

    Example::

        import aws_cdk.triggers as triggers
        
        
        func = lambda_.Function(self, "MyFunction",
            handler="index.handler",
            runtime=lambda_.Runtime.NODEJS_14_X,
            code=lambda_.Code.from_inline("foo")
        )
        
        triggers.Trigger(self, "MyTrigger",
            handler=func,
            timeout=Duration.minutes(10),
            invocation_type=triggers.InvocationType.EVENT
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        handler: _Function_244f85d8,
        invocation_type: typing.Optional[InvocationType] = None,
        timeout: typing.Optional[_Duration_4839e8c3] = None,
        execute_after: typing.Optional[typing.Sequence[_constructs_77d1e7e8.Construct]] = None,
        execute_before: typing.Optional[typing.Sequence[_constructs_77d1e7e8.Construct]] = None,
        execute_on_handler_change: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param handler: The AWS Lambda function of the handler to execute.
        :param invocation_type: The invocation type to invoke the Lambda function with. Default: RequestResponse
        :param timeout: The timeout of the invocation call of the Lambda function to be triggered. Default: Duration.minutes(2)
        :param execute_after: Adds trigger dependencies. Execute this trigger only after these construct scopes have been provisioned. You can also use ``trigger.executeAfter()`` to add additional dependencies. Default: []
        :param execute_before: Adds this trigger as a dependency on other constructs. This means that this trigger will get executed *before* the given construct(s). You can also use ``trigger.executeBefore()`` to add additional dependants. Default: []
        :param execute_on_handler_change: Re-executes the trigger every time the handler changes. This implies that the trigger is associated with the ``currentVersion`` of the handler, which gets recreated every time the handler or its configuration is updated. Default: true
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b7d2333ea709a924a3374ea45391de202dd23ab9ad7b9dc22d6b36d95aab023)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = TriggerProps(
            handler=handler,
            invocation_type=invocation_type,
            timeout=timeout,
            execute_after=execute_after,
            execute_before=execute_before,
            execute_on_handler_change=execute_on_handler_change,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="executeAfter")
    def execute_after(self, *scopes: _constructs_77d1e7e8.Construct) -> None:
        '''Adds trigger dependencies.

        Execute this trigger only after these construct
        scopes have been provisioned.

        :param scopes: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60d0e9556ead797bb961db69cb5121040091279632390d475d4c2209fb0ffc70)
            check_type(argname="argument scopes", value=scopes, expected_type=typing.Tuple[type_hints["scopes"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "executeAfter", [*scopes]))

    @jsii.member(jsii_name="executeBefore")
    def execute_before(self, *scopes: _constructs_77d1e7e8.Construct) -> None:
        '''Adds this trigger as a dependency on other constructs.

        This means that this
        trigger will get executed *before* the given construct(s).

        :param scopes: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53346c2d06fbc7c3a1bbe51e2105eef0d748c9336faeb91d2007168d162b5fe5)
            check_type(argname="argument scopes", value=scopes, expected_type=typing.Tuple[type_hints["scopes"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "executeBefore", [*scopes]))


@jsii.implements(ITrigger)
class TriggerFunction(
    _Function_244f85d8,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.triggers.TriggerFunction",
):
    '''Invokes an AWS Lambda function during deployment.

    :exampleMetadata: infused

    Example::

        import aws_cdk.triggers as triggers
        
        
        triggers.TriggerFunction(self, "MyTrigger",
            runtime=lambda_.Runtime.NODEJS_14_X,
            handler="index.handler",
            code=lambda_.Code.from_asset(__dirname + "/my-trigger")
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        code: _Code_7848f942,
        handler: builtins.str,
        runtime: _Runtime_b4eaa844,
        execute_after: typing.Optional[typing.Sequence[_constructs_77d1e7e8.Construct]] = None,
        execute_before: typing.Optional[typing.Sequence[_constructs_77d1e7e8.Construct]] = None,
        execute_on_handler_change: typing.Optional[builtins.bool] = None,
        adot_instrumentation: typing.Optional[typing.Union[_AdotInstrumentationConfig_7c38d65d, typing.Dict[builtins.str, typing.Any]]] = None,
        allow_all_outbound: typing.Optional[builtins.bool] = None,
        allow_public_subnet: typing.Optional[builtins.bool] = None,
        architecture: typing.Optional[_Architecture_12d5a53f] = None,
        code_signing_config: typing.Optional[_ICodeSigningConfig_edb41d1f] = None,
        current_version_options: typing.Optional[typing.Union[_VersionOptions_981bb3c0, typing.Dict[builtins.str, typing.Any]]] = None,
        dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
        dead_letter_queue_enabled: typing.Optional[builtins.bool] = None,
        dead_letter_topic: typing.Optional[_ITopic_9eca4852] = None,
        description: typing.Optional[builtins.str] = None,
        environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        environment_encryption: typing.Optional[_IKey_5f11635f] = None,
        ephemeral_storage_size: typing.Optional[_Size_7b441c34] = None,
        events: typing.Optional[typing.Sequence[_IEventSource_3686b3f8]] = None,
        filesystem: typing.Optional[_FileSystem_a5fa005d] = None,
        function_name: typing.Optional[builtins.str] = None,
        initial_policy: typing.Optional[typing.Sequence[_PolicyStatement_0fe33853]] = None,
        insights_version: typing.Optional[_LambdaInsightsVersion_9dfbfef9] = None,
        layers: typing.Optional[typing.Sequence[_ILayerVersion_5ac127c8]] = None,
        log_retention: typing.Optional[_RetentionDays_070f99f0] = None,
        log_retention_retry_options: typing.Optional[typing.Union[_LogRetentionRetryOptions_ad797a7a, typing.Dict[builtins.str, typing.Any]]] = None,
        log_retention_role: typing.Optional[_IRole_235f5d8e] = None,
        memory_size: typing.Optional[jsii.Number] = None,
        params_and_secrets: typing.Optional[_ParamsAndSecretsLayerVersion_dce97f06] = None,
        profiling: typing.Optional[builtins.bool] = None,
        profiling_group: typing.Optional[_IProfilingGroup_0bba72c4] = None,
        reserved_concurrent_executions: typing.Optional[jsii.Number] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
        runtime_management_mode: typing.Optional[_RuntimeManagementMode_688c173b] = None,
        security_groups: typing.Optional[typing.Sequence[_ISecurityGroup_acf8a799]] = None,
        timeout: typing.Optional[_Duration_4839e8c3] = None,
        tracing: typing.Optional[_Tracing_9fe8e2bb] = None,
        vpc: typing.Optional[_IVpc_f30d5663] = None,
        vpc_subnets: typing.Optional[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]] = None,
        max_event_age: typing.Optional[_Duration_4839e8c3] = None,
        on_failure: typing.Optional[_IDestination_40f19de4] = None,
        on_success: typing.Optional[_IDestination_40f19de4] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param code: The source code of your Lambda function. You can point to a file in an Amazon Simple Storage Service (Amazon S3) bucket or specify your source code as inline text.
        :param handler: The name of the method within your code that Lambda calls to execute your function. The format includes the file name. It can also include namespaces and other qualifiers, depending on the runtime. For more information, see https://docs.aws.amazon.com/lambda/latest/dg/foundation-progmodel.html. Use ``Handler.FROM_IMAGE`` when defining a function from a Docker image. NOTE: If you specify your source code as inline text by specifying the ZipFile property within the Code property, specify index.function_name as the handler.
        :param runtime: The runtime environment for the Lambda function that you are uploading. For valid values, see the Runtime property in the AWS Lambda Developer Guide. Use ``Runtime.FROM_IMAGE`` when defining a function from a Docker image.
        :param execute_after: Adds trigger dependencies. Execute this trigger only after these construct scopes have been provisioned. You can also use ``trigger.executeAfter()`` to add additional dependencies. Default: []
        :param execute_before: Adds this trigger as a dependency on other constructs. This means that this trigger will get executed *before* the given construct(s). You can also use ``trigger.executeBefore()`` to add additional dependants. Default: []
        :param execute_on_handler_change: Re-executes the trigger every time the handler changes. This implies that the trigger is associated with the ``currentVersion`` of the handler, which gets recreated every time the handler or its configuration is updated. Default: true
        :param adot_instrumentation: Specify the configuration of AWS Distro for OpenTelemetry (ADOT) instrumentation. Default: - No ADOT instrumentation
        :param allow_all_outbound: Whether to allow the Lambda to send all network traffic. If set to false, you must individually add traffic rules to allow the Lambda to connect to network targets. Default: true
        :param allow_public_subnet: Lambda Functions in a public subnet can NOT access the internet. Use this property to acknowledge this limitation and still place the function in a public subnet. Default: false
        :param architecture: The system architectures compatible with this lambda function. Default: Architecture.X86_64
        :param code_signing_config: Code signing config associated with this function. Default: - Not Sign the Code
        :param current_version_options: Options for the ``lambda.Version`` resource automatically created by the ``fn.currentVersion`` method. Default: - default options as described in ``VersionOptions``
        :param dead_letter_queue: The SQS queue to use if DLQ is enabled. If SNS topic is desired, specify ``deadLetterTopic`` property instead. Default: - SQS queue with 14 day retention period if ``deadLetterQueueEnabled`` is ``true``
        :param dead_letter_queue_enabled: Enabled DLQ. If ``deadLetterQueue`` is undefined, an SQS queue with default options will be defined for your Function. Default: - false unless ``deadLetterQueue`` is set, which implies DLQ is enabled.
        :param dead_letter_topic: The SNS topic to use as a DLQ. Note that if ``deadLetterQueueEnabled`` is set to ``true``, an SQS queue will be created rather than an SNS topic. Using an SNS topic as a DLQ requires this property to be set explicitly. Default: - no SNS topic
        :param description: A description of the function. Default: - No description.
        :param environment: Key-value pairs that Lambda caches and makes available for your Lambda functions. Use environment variables to apply configuration changes, such as test and production environment configurations, without changing your Lambda function source code. Default: - No environment variables.
        :param environment_encryption: The AWS KMS key that's used to encrypt your function's environment variables. Default: - AWS Lambda creates and uses an AWS managed customer master key (CMK).
        :param ephemeral_storage_size: The size of the function’s /tmp directory in MiB. Default: 512 MiB
        :param events: Event sources for this function. You can also add event sources using ``addEventSource``. Default: - No event sources.
        :param filesystem: The filesystem configuration for the lambda function. Default: - will not mount any filesystem
        :param function_name: A name for the function. Default: - AWS CloudFormation generates a unique physical ID and uses that ID for the function's name. For more information, see Name Type.
        :param initial_policy: Initial policy statements to add to the created Lambda Role. You can call ``addToRolePolicy`` to the created lambda to add statements post creation. Default: - No policy statements are added to the created Lambda role.
        :param insights_version: Specify the version of CloudWatch Lambda insights to use for monitoring. Default: - No Lambda Insights
        :param layers: A list of layers to add to the function's execution environment. You can configure your Lambda function to pull in additional code during initialization in the form of layers. Layers are packages of libraries or other dependencies that can be used by multiple functions. Default: - No layers.
        :param log_retention: The number of days log events are kept in CloudWatch Logs. When updating this property, unsetting it doesn't remove the log retention policy. To remove the retention policy, set the value to ``INFINITE``. Default: logs.RetentionDays.INFINITE
        :param log_retention_retry_options: When log retention is specified, a custom resource attempts to create the CloudWatch log group. These options control the retry policy when interacting with CloudWatch APIs. Default: - Default AWS SDK retry options.
        :param log_retention_role: The IAM role for the Lambda function associated with the custom resource that sets the retention policy. Default: - A new role is created.
        :param memory_size: The amount of memory, in MB, that is allocated to your Lambda function. Lambda uses this value to proportionally allocate the amount of CPU power. For more information, see Resource Model in the AWS Lambda Developer Guide. Default: 128
        :param params_and_secrets: Specify the configuration of Parameters and Secrets Extension. Default: - No Parameters and Secrets Extension
        :param profiling: Enable profiling. Default: - No profiling.
        :param profiling_group: Profiling Group. Default: - A new profiling group will be created if ``profiling`` is set.
        :param reserved_concurrent_executions: The maximum of concurrent executions you want to reserve for the function. Default: - No specific limit - account limit.
        :param role: Lambda execution role. This is the role that will be assumed by the function upon execution. It controls the permissions that the function will have. The Role must be assumable by the 'lambda.amazonaws.com' service principal. The default Role automatically has permissions granted for Lambda execution. If you provide a Role, you must add the relevant AWS managed policies yourself. The relevant managed policies are "service-role/AWSLambdaBasicExecutionRole" and "service-role/AWSLambdaVPCAccessExecutionRole". Default: - A unique role will be generated for this lambda function. Both supplied and generated roles can always be changed by calling ``addToRolePolicy``.
        :param runtime_management_mode: Sets the runtime management configuration for a function's version. Default: Auto
        :param security_groups: The list of security groups to associate with the Lambda's network interfaces. Only used if 'vpc' is supplied. Default: - If the function is placed within a VPC and a security group is not specified, either by this or securityGroup prop, a dedicated security group will be created for this function.
        :param timeout: The function execution time (in seconds) after which Lambda terminates the function. Because the execution time affects cost, set this value based on the function's expected execution time. Default: Duration.seconds(3)
        :param tracing: Enable AWS X-Ray Tracing for Lambda Function. Default: Tracing.Disabled
        :param vpc: VPC network to place Lambda network interfaces. Specify this if the Lambda function needs to access resources in a VPC. This is required when ``vpcSubnets`` is specified. Default: - Function is not placed within a VPC.
        :param vpc_subnets: Where to place the network interfaces within the VPC. This requires ``vpc`` to be specified in order for interfaces to actually be placed in the subnets. If ``vpc`` is not specify, this will raise an error. Note: Internet access for Lambda Functions requires a NAT Gateway, so picking public subnets is not allowed (unless ``allowPublicSubnet`` is set to ``true``). Default: - the Vpc default strategy if not specified
        :param max_event_age: The maximum age of a request that Lambda sends to a function for processing. Minimum: 60 seconds Maximum: 6 hours Default: Duration.hours(6)
        :param on_failure: The destination for failed invocations. Default: - no destination
        :param on_success: The destination for successful invocations. Default: - no destination
        :param retry_attempts: The maximum number of times to retry when the function returns an error. Minimum: 0 Maximum: 2 Default: 2
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f34c5ba084706d20d6ef37a7f59673b20ed3425ffc7035fc8ea888e9f68bdd9)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = TriggerFunctionProps(
            code=code,
            handler=handler,
            runtime=runtime,
            execute_after=execute_after,
            execute_before=execute_before,
            execute_on_handler_change=execute_on_handler_change,
            adot_instrumentation=adot_instrumentation,
            allow_all_outbound=allow_all_outbound,
            allow_public_subnet=allow_public_subnet,
            architecture=architecture,
            code_signing_config=code_signing_config,
            current_version_options=current_version_options,
            dead_letter_queue=dead_letter_queue,
            dead_letter_queue_enabled=dead_letter_queue_enabled,
            dead_letter_topic=dead_letter_topic,
            description=description,
            environment=environment,
            environment_encryption=environment_encryption,
            ephemeral_storage_size=ephemeral_storage_size,
            events=events,
            filesystem=filesystem,
            function_name=function_name,
            initial_policy=initial_policy,
            insights_version=insights_version,
            layers=layers,
            log_retention=log_retention,
            log_retention_retry_options=log_retention_retry_options,
            log_retention_role=log_retention_role,
            memory_size=memory_size,
            params_and_secrets=params_and_secrets,
            profiling=profiling,
            profiling_group=profiling_group,
            reserved_concurrent_executions=reserved_concurrent_executions,
            role=role,
            runtime_management_mode=runtime_management_mode,
            security_groups=security_groups,
            timeout=timeout,
            tracing=tracing,
            vpc=vpc,
            vpc_subnets=vpc_subnets,
            max_event_age=max_event_age,
            on_failure=on_failure,
            on_success=on_success,
            retry_attempts=retry_attempts,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="executeAfter")
    def execute_after(self, *scopes: _constructs_77d1e7e8.Construct) -> None:
        '''Adds trigger dependencies.

        Execute this trigger only after these construct
        scopes have been provisioned.

        :param scopes: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90250696d445460d02b427f820f1d5da99cca60cf5bd9e0352e63062c8f24bc9)
            check_type(argname="argument scopes", value=scopes, expected_type=typing.Tuple[type_hints["scopes"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "executeAfter", [*scopes]))

    @jsii.member(jsii_name="executeBefore")
    def execute_before(self, *scopes: _constructs_77d1e7e8.Construct) -> None:
        '''Adds this trigger as a dependency on other constructs.

        This means that this
        trigger will get executed *before* the given construct(s).

        :param scopes: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3a39b559574edf1b66218b9829d7f7cb9718777ead4c37c75db4b04ce680f72)
            check_type(argname="argument scopes", value=scopes, expected_type=typing.Tuple[type_hints["scopes"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "executeBefore", [*scopes]))

    @builtins.property
    @jsii.member(jsii_name="trigger")
    def trigger(self) -> Trigger:
        '''The underlying trigger resource.'''
        return typing.cast(Trigger, jsii.get(self, "trigger"))


@jsii.enum(jsii_type="aws-cdk-lib.triggers.TriggerInvalidation")
class TriggerInvalidation(enum.Enum):
    '''Determines.'''

    HANDLER_CHANGE = "HANDLER_CHANGE"
    '''The trigger will be executed every time the handler (or its configuration) changes.

    This is implemented by associated the trigger with the ``currentVersion``
    of the AWS Lambda function, which gets recreated every time the handler changes.
    '''


@jsii.data_type(
    jsii_type="aws-cdk-lib.triggers.TriggerOptions",
    jsii_struct_bases=[],
    name_mapping={
        "execute_after": "executeAfter",
        "execute_before": "executeBefore",
        "execute_on_handler_change": "executeOnHandlerChange",
    },
)
class TriggerOptions:
    def __init__(
        self,
        *,
        execute_after: typing.Optional[typing.Sequence[_constructs_77d1e7e8.Construct]] = None,
        execute_before: typing.Optional[typing.Sequence[_constructs_77d1e7e8.Construct]] = None,
        execute_on_handler_change: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Options for ``Trigger``.

        :param execute_after: Adds trigger dependencies. Execute this trigger only after these construct scopes have been provisioned. You can also use ``trigger.executeAfter()`` to add additional dependencies. Default: []
        :param execute_before: Adds this trigger as a dependency on other constructs. This means that this trigger will get executed *before* the given construct(s). You can also use ``trigger.executeBefore()`` to add additional dependants. Default: []
        :param execute_on_handler_change: Re-executes the trigger every time the handler changes. This implies that the trigger is associated with the ``currentVersion`` of the handler, which gets recreated every time the handler or its configuration is updated. Default: true

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import triggers
            import constructs as constructs
            
            # construct: constructs.Construct
            
            trigger_options = triggers.TriggerOptions(
                execute_after=[construct],
                execute_before=[construct],
                execute_on_handler_change=False
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5a182040d846d549ba242a7734148186c69e4de0d60c879b2b64ef1229e176d)
            check_type(argname="argument execute_after", value=execute_after, expected_type=type_hints["execute_after"])
            check_type(argname="argument execute_before", value=execute_before, expected_type=type_hints["execute_before"])
            check_type(argname="argument execute_on_handler_change", value=execute_on_handler_change, expected_type=type_hints["execute_on_handler_change"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if execute_after is not None:
            self._values["execute_after"] = execute_after
        if execute_before is not None:
            self._values["execute_before"] = execute_before
        if execute_on_handler_change is not None:
            self._values["execute_on_handler_change"] = execute_on_handler_change

    @builtins.property
    def execute_after(
        self,
    ) -> typing.Optional[typing.List[_constructs_77d1e7e8.Construct]]:
        '''Adds trigger dependencies. Execute this trigger only after these construct scopes have been provisioned.

        You can also use ``trigger.executeAfter()`` to add additional dependencies.

        :default: []
        '''
        result = self._values.get("execute_after")
        return typing.cast(typing.Optional[typing.List[_constructs_77d1e7e8.Construct]], result)

    @builtins.property
    def execute_before(
        self,
    ) -> typing.Optional[typing.List[_constructs_77d1e7e8.Construct]]:
        '''Adds this trigger as a dependency on other constructs.

        This means that this
        trigger will get executed *before* the given construct(s).

        You can also use ``trigger.executeBefore()`` to add additional dependants.

        :default: []
        '''
        result = self._values.get("execute_before")
        return typing.cast(typing.Optional[typing.List[_constructs_77d1e7e8.Construct]], result)

    @builtins.property
    def execute_on_handler_change(self) -> typing.Optional[builtins.bool]:
        '''Re-executes the trigger every time the handler changes.

        This implies that the trigger is associated with the ``currentVersion`` of
        the handler, which gets recreated every time the handler or its
        configuration is updated.

        :default: true
        '''
        result = self._values.get("execute_on_handler_change")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TriggerOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.triggers.TriggerProps",
    jsii_struct_bases=[TriggerOptions],
    name_mapping={
        "execute_after": "executeAfter",
        "execute_before": "executeBefore",
        "execute_on_handler_change": "executeOnHandlerChange",
        "handler": "handler",
        "invocation_type": "invocationType",
        "timeout": "timeout",
    },
)
class TriggerProps(TriggerOptions):
    def __init__(
        self,
        *,
        execute_after: typing.Optional[typing.Sequence[_constructs_77d1e7e8.Construct]] = None,
        execute_before: typing.Optional[typing.Sequence[_constructs_77d1e7e8.Construct]] = None,
        execute_on_handler_change: typing.Optional[builtins.bool] = None,
        handler: _Function_244f85d8,
        invocation_type: typing.Optional[InvocationType] = None,
        timeout: typing.Optional[_Duration_4839e8c3] = None,
    ) -> None:
        '''Props for ``Trigger``.

        :param execute_after: Adds trigger dependencies. Execute this trigger only after these construct scopes have been provisioned. You can also use ``trigger.executeAfter()`` to add additional dependencies. Default: []
        :param execute_before: Adds this trigger as a dependency on other constructs. This means that this trigger will get executed *before* the given construct(s). You can also use ``trigger.executeBefore()`` to add additional dependants. Default: []
        :param execute_on_handler_change: Re-executes the trigger every time the handler changes. This implies that the trigger is associated with the ``currentVersion`` of the handler, which gets recreated every time the handler or its configuration is updated. Default: true
        :param handler: The AWS Lambda function of the handler to execute.
        :param invocation_type: The invocation type to invoke the Lambda function with. Default: RequestResponse
        :param timeout: The timeout of the invocation call of the Lambda function to be triggered. Default: Duration.minutes(2)

        :exampleMetadata: infused

        Example::

            import aws_cdk.triggers as triggers
            
            
            func = lambda_.Function(self, "MyFunction",
                handler="index.handler",
                runtime=lambda_.Runtime.NODEJS_14_X,
                code=lambda_.Code.from_inline("foo")
            )
            
            triggers.Trigger(self, "MyTrigger",
                handler=func,
                timeout=Duration.minutes(10),
                invocation_type=triggers.InvocationType.EVENT
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59427805740f705ff9572f1711767f2e394b5cfe9e0d4149bd301d8a94bf4ae0)
            check_type(argname="argument execute_after", value=execute_after, expected_type=type_hints["execute_after"])
            check_type(argname="argument execute_before", value=execute_before, expected_type=type_hints["execute_before"])
            check_type(argname="argument execute_on_handler_change", value=execute_on_handler_change, expected_type=type_hints["execute_on_handler_change"])
            check_type(argname="argument handler", value=handler, expected_type=type_hints["handler"])
            check_type(argname="argument invocation_type", value=invocation_type, expected_type=type_hints["invocation_type"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "handler": handler,
        }
        if execute_after is not None:
            self._values["execute_after"] = execute_after
        if execute_before is not None:
            self._values["execute_before"] = execute_before
        if execute_on_handler_change is not None:
            self._values["execute_on_handler_change"] = execute_on_handler_change
        if invocation_type is not None:
            self._values["invocation_type"] = invocation_type
        if timeout is not None:
            self._values["timeout"] = timeout

    @builtins.property
    def execute_after(
        self,
    ) -> typing.Optional[typing.List[_constructs_77d1e7e8.Construct]]:
        '''Adds trigger dependencies. Execute this trigger only after these construct scopes have been provisioned.

        You can also use ``trigger.executeAfter()`` to add additional dependencies.

        :default: []
        '''
        result = self._values.get("execute_after")
        return typing.cast(typing.Optional[typing.List[_constructs_77d1e7e8.Construct]], result)

    @builtins.property
    def execute_before(
        self,
    ) -> typing.Optional[typing.List[_constructs_77d1e7e8.Construct]]:
        '''Adds this trigger as a dependency on other constructs.

        This means that this
        trigger will get executed *before* the given construct(s).

        You can also use ``trigger.executeBefore()`` to add additional dependants.

        :default: []
        '''
        result = self._values.get("execute_before")
        return typing.cast(typing.Optional[typing.List[_constructs_77d1e7e8.Construct]], result)

    @builtins.property
    def execute_on_handler_change(self) -> typing.Optional[builtins.bool]:
        '''Re-executes the trigger every time the handler changes.

        This implies that the trigger is associated with the ``currentVersion`` of
        the handler, which gets recreated every time the handler or its
        configuration is updated.

        :default: true
        '''
        result = self._values.get("execute_on_handler_change")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def handler(self) -> _Function_244f85d8:
        '''The AWS Lambda function of the handler to execute.'''
        result = self._values.get("handler")
        assert result is not None, "Required property 'handler' is missing"
        return typing.cast(_Function_244f85d8, result)

    @builtins.property
    def invocation_type(self) -> typing.Optional[InvocationType]:
        '''The invocation type to invoke the Lambda function with.

        :default: RequestResponse
        '''
        result = self._values.get("invocation_type")
        return typing.cast(typing.Optional[InvocationType], result)

    @builtins.property
    def timeout(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The timeout of the invocation call of the Lambda function to be triggered.

        :default: Duration.minutes(2)
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TriggerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.triggers.TriggerFunctionProps",
    jsii_struct_bases=[_FunctionProps_a308e854, TriggerOptions],
    name_mapping={
        "max_event_age": "maxEventAge",
        "on_failure": "onFailure",
        "on_success": "onSuccess",
        "retry_attempts": "retryAttempts",
        "adot_instrumentation": "adotInstrumentation",
        "allow_all_outbound": "allowAllOutbound",
        "allow_public_subnet": "allowPublicSubnet",
        "architecture": "architecture",
        "code_signing_config": "codeSigningConfig",
        "current_version_options": "currentVersionOptions",
        "dead_letter_queue": "deadLetterQueue",
        "dead_letter_queue_enabled": "deadLetterQueueEnabled",
        "dead_letter_topic": "deadLetterTopic",
        "description": "description",
        "environment": "environment",
        "environment_encryption": "environmentEncryption",
        "ephemeral_storage_size": "ephemeralStorageSize",
        "events": "events",
        "filesystem": "filesystem",
        "function_name": "functionName",
        "initial_policy": "initialPolicy",
        "insights_version": "insightsVersion",
        "layers": "layers",
        "log_retention": "logRetention",
        "log_retention_retry_options": "logRetentionRetryOptions",
        "log_retention_role": "logRetentionRole",
        "memory_size": "memorySize",
        "params_and_secrets": "paramsAndSecrets",
        "profiling": "profiling",
        "profiling_group": "profilingGroup",
        "reserved_concurrent_executions": "reservedConcurrentExecutions",
        "role": "role",
        "runtime_management_mode": "runtimeManagementMode",
        "security_groups": "securityGroups",
        "timeout": "timeout",
        "tracing": "tracing",
        "vpc": "vpc",
        "vpc_subnets": "vpcSubnets",
        "code": "code",
        "handler": "handler",
        "runtime": "runtime",
        "execute_after": "executeAfter",
        "execute_before": "executeBefore",
        "execute_on_handler_change": "executeOnHandlerChange",
    },
)
class TriggerFunctionProps(_FunctionProps_a308e854, TriggerOptions):
    def __init__(
        self,
        *,
        max_event_age: typing.Optional[_Duration_4839e8c3] = None,
        on_failure: typing.Optional[_IDestination_40f19de4] = None,
        on_success: typing.Optional[_IDestination_40f19de4] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
        adot_instrumentation: typing.Optional[typing.Union[_AdotInstrumentationConfig_7c38d65d, typing.Dict[builtins.str, typing.Any]]] = None,
        allow_all_outbound: typing.Optional[builtins.bool] = None,
        allow_public_subnet: typing.Optional[builtins.bool] = None,
        architecture: typing.Optional[_Architecture_12d5a53f] = None,
        code_signing_config: typing.Optional[_ICodeSigningConfig_edb41d1f] = None,
        current_version_options: typing.Optional[typing.Union[_VersionOptions_981bb3c0, typing.Dict[builtins.str, typing.Any]]] = None,
        dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
        dead_letter_queue_enabled: typing.Optional[builtins.bool] = None,
        dead_letter_topic: typing.Optional[_ITopic_9eca4852] = None,
        description: typing.Optional[builtins.str] = None,
        environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        environment_encryption: typing.Optional[_IKey_5f11635f] = None,
        ephemeral_storage_size: typing.Optional[_Size_7b441c34] = None,
        events: typing.Optional[typing.Sequence[_IEventSource_3686b3f8]] = None,
        filesystem: typing.Optional[_FileSystem_a5fa005d] = None,
        function_name: typing.Optional[builtins.str] = None,
        initial_policy: typing.Optional[typing.Sequence[_PolicyStatement_0fe33853]] = None,
        insights_version: typing.Optional[_LambdaInsightsVersion_9dfbfef9] = None,
        layers: typing.Optional[typing.Sequence[_ILayerVersion_5ac127c8]] = None,
        log_retention: typing.Optional[_RetentionDays_070f99f0] = None,
        log_retention_retry_options: typing.Optional[typing.Union[_LogRetentionRetryOptions_ad797a7a, typing.Dict[builtins.str, typing.Any]]] = None,
        log_retention_role: typing.Optional[_IRole_235f5d8e] = None,
        memory_size: typing.Optional[jsii.Number] = None,
        params_and_secrets: typing.Optional[_ParamsAndSecretsLayerVersion_dce97f06] = None,
        profiling: typing.Optional[builtins.bool] = None,
        profiling_group: typing.Optional[_IProfilingGroup_0bba72c4] = None,
        reserved_concurrent_executions: typing.Optional[jsii.Number] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
        runtime_management_mode: typing.Optional[_RuntimeManagementMode_688c173b] = None,
        security_groups: typing.Optional[typing.Sequence[_ISecurityGroup_acf8a799]] = None,
        timeout: typing.Optional[_Duration_4839e8c3] = None,
        tracing: typing.Optional[_Tracing_9fe8e2bb] = None,
        vpc: typing.Optional[_IVpc_f30d5663] = None,
        vpc_subnets: typing.Optional[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]] = None,
        code: _Code_7848f942,
        handler: builtins.str,
        runtime: _Runtime_b4eaa844,
        execute_after: typing.Optional[typing.Sequence[_constructs_77d1e7e8.Construct]] = None,
        execute_before: typing.Optional[typing.Sequence[_constructs_77d1e7e8.Construct]] = None,
        execute_on_handler_change: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Props for ``InvokeFunction``.

        :param max_event_age: The maximum age of a request that Lambda sends to a function for processing. Minimum: 60 seconds Maximum: 6 hours Default: Duration.hours(6)
        :param on_failure: The destination for failed invocations. Default: - no destination
        :param on_success: The destination for successful invocations. Default: - no destination
        :param retry_attempts: The maximum number of times to retry when the function returns an error. Minimum: 0 Maximum: 2 Default: 2
        :param adot_instrumentation: Specify the configuration of AWS Distro for OpenTelemetry (ADOT) instrumentation. Default: - No ADOT instrumentation
        :param allow_all_outbound: Whether to allow the Lambda to send all network traffic. If set to false, you must individually add traffic rules to allow the Lambda to connect to network targets. Default: true
        :param allow_public_subnet: Lambda Functions in a public subnet can NOT access the internet. Use this property to acknowledge this limitation and still place the function in a public subnet. Default: false
        :param architecture: The system architectures compatible with this lambda function. Default: Architecture.X86_64
        :param code_signing_config: Code signing config associated with this function. Default: - Not Sign the Code
        :param current_version_options: Options for the ``lambda.Version`` resource automatically created by the ``fn.currentVersion`` method. Default: - default options as described in ``VersionOptions``
        :param dead_letter_queue: The SQS queue to use if DLQ is enabled. If SNS topic is desired, specify ``deadLetterTopic`` property instead. Default: - SQS queue with 14 day retention period if ``deadLetterQueueEnabled`` is ``true``
        :param dead_letter_queue_enabled: Enabled DLQ. If ``deadLetterQueue`` is undefined, an SQS queue with default options will be defined for your Function. Default: - false unless ``deadLetterQueue`` is set, which implies DLQ is enabled.
        :param dead_letter_topic: The SNS topic to use as a DLQ. Note that if ``deadLetterQueueEnabled`` is set to ``true``, an SQS queue will be created rather than an SNS topic. Using an SNS topic as a DLQ requires this property to be set explicitly. Default: - no SNS topic
        :param description: A description of the function. Default: - No description.
        :param environment: Key-value pairs that Lambda caches and makes available for your Lambda functions. Use environment variables to apply configuration changes, such as test and production environment configurations, without changing your Lambda function source code. Default: - No environment variables.
        :param environment_encryption: The AWS KMS key that's used to encrypt your function's environment variables. Default: - AWS Lambda creates and uses an AWS managed customer master key (CMK).
        :param ephemeral_storage_size: The size of the function’s /tmp directory in MiB. Default: 512 MiB
        :param events: Event sources for this function. You can also add event sources using ``addEventSource``. Default: - No event sources.
        :param filesystem: The filesystem configuration for the lambda function. Default: - will not mount any filesystem
        :param function_name: A name for the function. Default: - AWS CloudFormation generates a unique physical ID and uses that ID for the function's name. For more information, see Name Type.
        :param initial_policy: Initial policy statements to add to the created Lambda Role. You can call ``addToRolePolicy`` to the created lambda to add statements post creation. Default: - No policy statements are added to the created Lambda role.
        :param insights_version: Specify the version of CloudWatch Lambda insights to use for monitoring. Default: - No Lambda Insights
        :param layers: A list of layers to add to the function's execution environment. You can configure your Lambda function to pull in additional code during initialization in the form of layers. Layers are packages of libraries or other dependencies that can be used by multiple functions. Default: - No layers.
        :param log_retention: The number of days log events are kept in CloudWatch Logs. When updating this property, unsetting it doesn't remove the log retention policy. To remove the retention policy, set the value to ``INFINITE``. Default: logs.RetentionDays.INFINITE
        :param log_retention_retry_options: When log retention is specified, a custom resource attempts to create the CloudWatch log group. These options control the retry policy when interacting with CloudWatch APIs. Default: - Default AWS SDK retry options.
        :param log_retention_role: The IAM role for the Lambda function associated with the custom resource that sets the retention policy. Default: - A new role is created.
        :param memory_size: The amount of memory, in MB, that is allocated to your Lambda function. Lambda uses this value to proportionally allocate the amount of CPU power. For more information, see Resource Model in the AWS Lambda Developer Guide. Default: 128
        :param params_and_secrets: Specify the configuration of Parameters and Secrets Extension. Default: - No Parameters and Secrets Extension
        :param profiling: Enable profiling. Default: - No profiling.
        :param profiling_group: Profiling Group. Default: - A new profiling group will be created if ``profiling`` is set.
        :param reserved_concurrent_executions: The maximum of concurrent executions you want to reserve for the function. Default: - No specific limit - account limit.
        :param role: Lambda execution role. This is the role that will be assumed by the function upon execution. It controls the permissions that the function will have. The Role must be assumable by the 'lambda.amazonaws.com' service principal. The default Role automatically has permissions granted for Lambda execution. If you provide a Role, you must add the relevant AWS managed policies yourself. The relevant managed policies are "service-role/AWSLambdaBasicExecutionRole" and "service-role/AWSLambdaVPCAccessExecutionRole". Default: - A unique role will be generated for this lambda function. Both supplied and generated roles can always be changed by calling ``addToRolePolicy``.
        :param runtime_management_mode: Sets the runtime management configuration for a function's version. Default: Auto
        :param security_groups: The list of security groups to associate with the Lambda's network interfaces. Only used if 'vpc' is supplied. Default: - If the function is placed within a VPC and a security group is not specified, either by this or securityGroup prop, a dedicated security group will be created for this function.
        :param timeout: The function execution time (in seconds) after which Lambda terminates the function. Because the execution time affects cost, set this value based on the function's expected execution time. Default: Duration.seconds(3)
        :param tracing: Enable AWS X-Ray Tracing for Lambda Function. Default: Tracing.Disabled
        :param vpc: VPC network to place Lambda network interfaces. Specify this if the Lambda function needs to access resources in a VPC. This is required when ``vpcSubnets`` is specified. Default: - Function is not placed within a VPC.
        :param vpc_subnets: Where to place the network interfaces within the VPC. This requires ``vpc`` to be specified in order for interfaces to actually be placed in the subnets. If ``vpc`` is not specify, this will raise an error. Note: Internet access for Lambda Functions requires a NAT Gateway, so picking public subnets is not allowed (unless ``allowPublicSubnet`` is set to ``true``). Default: - the Vpc default strategy if not specified
        :param code: The source code of your Lambda function. You can point to a file in an Amazon Simple Storage Service (Amazon S3) bucket or specify your source code as inline text.
        :param handler: The name of the method within your code that Lambda calls to execute your function. The format includes the file name. It can also include namespaces and other qualifiers, depending on the runtime. For more information, see https://docs.aws.amazon.com/lambda/latest/dg/foundation-progmodel.html. Use ``Handler.FROM_IMAGE`` when defining a function from a Docker image. NOTE: If you specify your source code as inline text by specifying the ZipFile property within the Code property, specify index.function_name as the handler.
        :param runtime: The runtime environment for the Lambda function that you are uploading. For valid values, see the Runtime property in the AWS Lambda Developer Guide. Use ``Runtime.FROM_IMAGE`` when defining a function from a Docker image.
        :param execute_after: Adds trigger dependencies. Execute this trigger only after these construct scopes have been provisioned. You can also use ``trigger.executeAfter()`` to add additional dependencies. Default: []
        :param execute_before: Adds this trigger as a dependency on other constructs. This means that this trigger will get executed *before* the given construct(s). You can also use ``trigger.executeBefore()`` to add additional dependants. Default: []
        :param execute_on_handler_change: Re-executes the trigger every time the handler changes. This implies that the trigger is associated with the ``currentVersion`` of the handler, which gets recreated every time the handler or its configuration is updated. Default: true

        :exampleMetadata: infused

        Example::

            import aws_cdk.triggers as triggers
            
            
            triggers.TriggerFunction(self, "MyTrigger",
                runtime=lambda_.Runtime.NODEJS_14_X,
                handler="index.handler",
                code=lambda_.Code.from_asset(__dirname + "/my-trigger")
            )
        '''
        if isinstance(adot_instrumentation, dict):
            adot_instrumentation = _AdotInstrumentationConfig_7c38d65d(**adot_instrumentation)
        if isinstance(current_version_options, dict):
            current_version_options = _VersionOptions_981bb3c0(**current_version_options)
        if isinstance(log_retention_retry_options, dict):
            log_retention_retry_options = _LogRetentionRetryOptions_ad797a7a(**log_retention_retry_options)
        if isinstance(vpc_subnets, dict):
            vpc_subnets = _SubnetSelection_e57d76df(**vpc_subnets)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2f4b009b0160d566d798bfa6d813ccc8440e1a9e0f75c99449184a2fc126f91)
            check_type(argname="argument max_event_age", value=max_event_age, expected_type=type_hints["max_event_age"])
            check_type(argname="argument on_failure", value=on_failure, expected_type=type_hints["on_failure"])
            check_type(argname="argument on_success", value=on_success, expected_type=type_hints["on_success"])
            check_type(argname="argument retry_attempts", value=retry_attempts, expected_type=type_hints["retry_attempts"])
            check_type(argname="argument adot_instrumentation", value=adot_instrumentation, expected_type=type_hints["adot_instrumentation"])
            check_type(argname="argument allow_all_outbound", value=allow_all_outbound, expected_type=type_hints["allow_all_outbound"])
            check_type(argname="argument allow_public_subnet", value=allow_public_subnet, expected_type=type_hints["allow_public_subnet"])
            check_type(argname="argument architecture", value=architecture, expected_type=type_hints["architecture"])
            check_type(argname="argument code_signing_config", value=code_signing_config, expected_type=type_hints["code_signing_config"])
            check_type(argname="argument current_version_options", value=current_version_options, expected_type=type_hints["current_version_options"])
            check_type(argname="argument dead_letter_queue", value=dead_letter_queue, expected_type=type_hints["dead_letter_queue"])
            check_type(argname="argument dead_letter_queue_enabled", value=dead_letter_queue_enabled, expected_type=type_hints["dead_letter_queue_enabled"])
            check_type(argname="argument dead_letter_topic", value=dead_letter_topic, expected_type=type_hints["dead_letter_topic"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument environment", value=environment, expected_type=type_hints["environment"])
            check_type(argname="argument environment_encryption", value=environment_encryption, expected_type=type_hints["environment_encryption"])
            check_type(argname="argument ephemeral_storage_size", value=ephemeral_storage_size, expected_type=type_hints["ephemeral_storage_size"])
            check_type(argname="argument events", value=events, expected_type=type_hints["events"])
            check_type(argname="argument filesystem", value=filesystem, expected_type=type_hints["filesystem"])
            check_type(argname="argument function_name", value=function_name, expected_type=type_hints["function_name"])
            check_type(argname="argument initial_policy", value=initial_policy, expected_type=type_hints["initial_policy"])
            check_type(argname="argument insights_version", value=insights_version, expected_type=type_hints["insights_version"])
            check_type(argname="argument layers", value=layers, expected_type=type_hints["layers"])
            check_type(argname="argument log_retention", value=log_retention, expected_type=type_hints["log_retention"])
            check_type(argname="argument log_retention_retry_options", value=log_retention_retry_options, expected_type=type_hints["log_retention_retry_options"])
            check_type(argname="argument log_retention_role", value=log_retention_role, expected_type=type_hints["log_retention_role"])
            check_type(argname="argument memory_size", value=memory_size, expected_type=type_hints["memory_size"])
            check_type(argname="argument params_and_secrets", value=params_and_secrets, expected_type=type_hints["params_and_secrets"])
            check_type(argname="argument profiling", value=profiling, expected_type=type_hints["profiling"])
            check_type(argname="argument profiling_group", value=profiling_group, expected_type=type_hints["profiling_group"])
            check_type(argname="argument reserved_concurrent_executions", value=reserved_concurrent_executions, expected_type=type_hints["reserved_concurrent_executions"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument runtime_management_mode", value=runtime_management_mode, expected_type=type_hints["runtime_management_mode"])
            check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
            check_type(argname="argument tracing", value=tracing, expected_type=type_hints["tracing"])
            check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
            check_type(argname="argument vpc_subnets", value=vpc_subnets, expected_type=type_hints["vpc_subnets"])
            check_type(argname="argument code", value=code, expected_type=type_hints["code"])
            check_type(argname="argument handler", value=handler, expected_type=type_hints["handler"])
            check_type(argname="argument runtime", value=runtime, expected_type=type_hints["runtime"])
            check_type(argname="argument execute_after", value=execute_after, expected_type=type_hints["execute_after"])
            check_type(argname="argument execute_before", value=execute_before, expected_type=type_hints["execute_before"])
            check_type(argname="argument execute_on_handler_change", value=execute_on_handler_change, expected_type=type_hints["execute_on_handler_change"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "code": code,
            "handler": handler,
            "runtime": runtime,
        }
        if max_event_age is not None:
            self._values["max_event_age"] = max_event_age
        if on_failure is not None:
            self._values["on_failure"] = on_failure
        if on_success is not None:
            self._values["on_success"] = on_success
        if retry_attempts is not None:
            self._values["retry_attempts"] = retry_attempts
        if adot_instrumentation is not None:
            self._values["adot_instrumentation"] = adot_instrumentation
        if allow_all_outbound is not None:
            self._values["allow_all_outbound"] = allow_all_outbound
        if allow_public_subnet is not None:
            self._values["allow_public_subnet"] = allow_public_subnet
        if architecture is not None:
            self._values["architecture"] = architecture
        if code_signing_config is not None:
            self._values["code_signing_config"] = code_signing_config
        if current_version_options is not None:
            self._values["current_version_options"] = current_version_options
        if dead_letter_queue is not None:
            self._values["dead_letter_queue"] = dead_letter_queue
        if dead_letter_queue_enabled is not None:
            self._values["dead_letter_queue_enabled"] = dead_letter_queue_enabled
        if dead_letter_topic is not None:
            self._values["dead_letter_topic"] = dead_letter_topic
        if description is not None:
            self._values["description"] = description
        if environment is not None:
            self._values["environment"] = environment
        if environment_encryption is not None:
            self._values["environment_encryption"] = environment_encryption
        if ephemeral_storage_size is not None:
            self._values["ephemeral_storage_size"] = ephemeral_storage_size
        if events is not None:
            self._values["events"] = events
        if filesystem is not None:
            self._values["filesystem"] = filesystem
        if function_name is not None:
            self._values["function_name"] = function_name
        if initial_policy is not None:
            self._values["initial_policy"] = initial_policy
        if insights_version is not None:
            self._values["insights_version"] = insights_version
        if layers is not None:
            self._values["layers"] = layers
        if log_retention is not None:
            self._values["log_retention"] = log_retention
        if log_retention_retry_options is not None:
            self._values["log_retention_retry_options"] = log_retention_retry_options
        if log_retention_role is not None:
            self._values["log_retention_role"] = log_retention_role
        if memory_size is not None:
            self._values["memory_size"] = memory_size
        if params_and_secrets is not None:
            self._values["params_and_secrets"] = params_and_secrets
        if profiling is not None:
            self._values["profiling"] = profiling
        if profiling_group is not None:
            self._values["profiling_group"] = profiling_group
        if reserved_concurrent_executions is not None:
            self._values["reserved_concurrent_executions"] = reserved_concurrent_executions
        if role is not None:
            self._values["role"] = role
        if runtime_management_mode is not None:
            self._values["runtime_management_mode"] = runtime_management_mode
        if security_groups is not None:
            self._values["security_groups"] = security_groups
        if timeout is not None:
            self._values["timeout"] = timeout
        if tracing is not None:
            self._values["tracing"] = tracing
        if vpc is not None:
            self._values["vpc"] = vpc
        if vpc_subnets is not None:
            self._values["vpc_subnets"] = vpc_subnets
        if execute_after is not None:
            self._values["execute_after"] = execute_after
        if execute_before is not None:
            self._values["execute_before"] = execute_before
        if execute_on_handler_change is not None:
            self._values["execute_on_handler_change"] = execute_on_handler_change

    @builtins.property
    def max_event_age(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The maximum age of a request that Lambda sends to a function for processing.

        Minimum: 60 seconds
        Maximum: 6 hours

        :default: Duration.hours(6)
        '''
        result = self._values.get("max_event_age")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def on_failure(self) -> typing.Optional[_IDestination_40f19de4]:
        '''The destination for failed invocations.

        :default: - no destination
        '''
        result = self._values.get("on_failure")
        return typing.cast(typing.Optional[_IDestination_40f19de4], result)

    @builtins.property
    def on_success(self) -> typing.Optional[_IDestination_40f19de4]:
        '''The destination for successful invocations.

        :default: - no destination
        '''
        result = self._values.get("on_success")
        return typing.cast(typing.Optional[_IDestination_40f19de4], result)

    @builtins.property
    def retry_attempts(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of times to retry when the function returns an error.

        Minimum: 0
        Maximum: 2

        :default: 2
        '''
        result = self._values.get("retry_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def adot_instrumentation(
        self,
    ) -> typing.Optional[_AdotInstrumentationConfig_7c38d65d]:
        '''Specify the configuration of AWS Distro for OpenTelemetry (ADOT) instrumentation.

        :default: - No ADOT instrumentation

        :see: https://aws-otel.github.io/docs/getting-started/lambda
        '''
        result = self._values.get("adot_instrumentation")
        return typing.cast(typing.Optional[_AdotInstrumentationConfig_7c38d65d], result)

    @builtins.property
    def allow_all_outbound(self) -> typing.Optional[builtins.bool]:
        '''Whether to allow the Lambda to send all network traffic.

        If set to false, you must individually add traffic rules to allow the
        Lambda to connect to network targets.

        :default: true
        '''
        result = self._values.get("allow_all_outbound")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def allow_public_subnet(self) -> typing.Optional[builtins.bool]:
        '''Lambda Functions in a public subnet can NOT access the internet.

        Use this property to acknowledge this limitation and still place the function in a public subnet.

        :default: false

        :see: https://stackoverflow.com/questions/52992085/why-cant-an-aws-lambda-function-inside-a-public-subnet-in-a-vpc-connect-to-the/52994841#52994841
        '''
        result = self._values.get("allow_public_subnet")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def architecture(self) -> typing.Optional[_Architecture_12d5a53f]:
        '''The system architectures compatible with this lambda function.

        :default: Architecture.X86_64
        '''
        result = self._values.get("architecture")
        return typing.cast(typing.Optional[_Architecture_12d5a53f], result)

    @builtins.property
    def code_signing_config(self) -> typing.Optional[_ICodeSigningConfig_edb41d1f]:
        '''Code signing config associated with this function.

        :default: - Not Sign the Code
        '''
        result = self._values.get("code_signing_config")
        return typing.cast(typing.Optional[_ICodeSigningConfig_edb41d1f], result)

    @builtins.property
    def current_version_options(self) -> typing.Optional[_VersionOptions_981bb3c0]:
        '''Options for the ``lambda.Version`` resource automatically created by the ``fn.currentVersion`` method.

        :default: - default options as described in ``VersionOptions``
        '''
        result = self._values.get("current_version_options")
        return typing.cast(typing.Optional[_VersionOptions_981bb3c0], result)

    @builtins.property
    def dead_letter_queue(self) -> typing.Optional[_IQueue_7ed6f679]:
        '''The SQS queue to use if DLQ is enabled.

        If SNS topic is desired, specify ``deadLetterTopic`` property instead.

        :default: - SQS queue with 14 day retention period if ``deadLetterQueueEnabled`` is ``true``
        '''
        result = self._values.get("dead_letter_queue")
        return typing.cast(typing.Optional[_IQueue_7ed6f679], result)

    @builtins.property
    def dead_letter_queue_enabled(self) -> typing.Optional[builtins.bool]:
        '''Enabled DLQ.

        If ``deadLetterQueue`` is undefined,
        an SQS queue with default options will be defined for your Function.

        :default: - false unless ``deadLetterQueue`` is set, which implies DLQ is enabled.
        '''
        result = self._values.get("dead_letter_queue_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def dead_letter_topic(self) -> typing.Optional[_ITopic_9eca4852]:
        '''The SNS topic to use as a DLQ.

        Note that if ``deadLetterQueueEnabled`` is set to ``true``, an SQS queue will be created
        rather than an SNS topic. Using an SNS topic as a DLQ requires this property to be set explicitly.

        :default: - no SNS topic
        '''
        result = self._values.get("dead_letter_topic")
        return typing.cast(typing.Optional[_ITopic_9eca4852], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the function.

        :default: - No description.
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def environment(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Key-value pairs that Lambda caches and makes available for your Lambda functions.

        Use environment variables to apply configuration changes, such
        as test and production environment configurations, without changing your
        Lambda function source code.

        :default: - No environment variables.
        '''
        result = self._values.get("environment")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def environment_encryption(self) -> typing.Optional[_IKey_5f11635f]:
        '''The AWS KMS key that's used to encrypt your function's environment variables.

        :default: - AWS Lambda creates and uses an AWS managed customer master key (CMK).
        '''
        result = self._values.get("environment_encryption")
        return typing.cast(typing.Optional[_IKey_5f11635f], result)

    @builtins.property
    def ephemeral_storage_size(self) -> typing.Optional[_Size_7b441c34]:
        '''The size of the function’s /tmp directory in MiB.

        :default: 512 MiB
        '''
        result = self._values.get("ephemeral_storage_size")
        return typing.cast(typing.Optional[_Size_7b441c34], result)

    @builtins.property
    def events(self) -> typing.Optional[typing.List[_IEventSource_3686b3f8]]:
        '''Event sources for this function.

        You can also add event sources using ``addEventSource``.

        :default: - No event sources.
        '''
        result = self._values.get("events")
        return typing.cast(typing.Optional[typing.List[_IEventSource_3686b3f8]], result)

    @builtins.property
    def filesystem(self) -> typing.Optional[_FileSystem_a5fa005d]:
        '''The filesystem configuration for the lambda function.

        :default: - will not mount any filesystem
        '''
        result = self._values.get("filesystem")
        return typing.cast(typing.Optional[_FileSystem_a5fa005d], result)

    @builtins.property
    def function_name(self) -> typing.Optional[builtins.str]:
        '''A name for the function.

        :default:

        - AWS CloudFormation generates a unique physical ID and uses that
        ID for the function's name. For more information, see Name Type.
        '''
        result = self._values.get("function_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def initial_policy(self) -> typing.Optional[typing.List[_PolicyStatement_0fe33853]]:
        '''Initial policy statements to add to the created Lambda Role.

        You can call ``addToRolePolicy`` to the created lambda to add statements post creation.

        :default: - No policy statements are added to the created Lambda role.
        '''
        result = self._values.get("initial_policy")
        return typing.cast(typing.Optional[typing.List[_PolicyStatement_0fe33853]], result)

    @builtins.property
    def insights_version(self) -> typing.Optional[_LambdaInsightsVersion_9dfbfef9]:
        '''Specify the version of CloudWatch Lambda insights to use for monitoring.

        :default: - No Lambda Insights

        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Lambda-Insights-Getting-Started-docker.html
        '''
        result = self._values.get("insights_version")
        return typing.cast(typing.Optional[_LambdaInsightsVersion_9dfbfef9], result)

    @builtins.property
    def layers(self) -> typing.Optional[typing.List[_ILayerVersion_5ac127c8]]:
        '''A list of layers to add to the function's execution environment.

        You can configure your Lambda function to pull in
        additional code during initialization in the form of layers. Layers are packages of libraries or other dependencies
        that can be used by multiple functions.

        :default: - No layers.
        '''
        result = self._values.get("layers")
        return typing.cast(typing.Optional[typing.List[_ILayerVersion_5ac127c8]], result)

    @builtins.property
    def log_retention(self) -> typing.Optional[_RetentionDays_070f99f0]:
        '''The number of days log events are kept in CloudWatch Logs.

        When updating
        this property, unsetting it doesn't remove the log retention policy. To
        remove the retention policy, set the value to ``INFINITE``.

        :default: logs.RetentionDays.INFINITE
        '''
        result = self._values.get("log_retention")
        return typing.cast(typing.Optional[_RetentionDays_070f99f0], result)

    @builtins.property
    def log_retention_retry_options(
        self,
    ) -> typing.Optional[_LogRetentionRetryOptions_ad797a7a]:
        '''When log retention is specified, a custom resource attempts to create the CloudWatch log group.

        These options control the retry policy when interacting with CloudWatch APIs.

        :default: - Default AWS SDK retry options.
        '''
        result = self._values.get("log_retention_retry_options")
        return typing.cast(typing.Optional[_LogRetentionRetryOptions_ad797a7a], result)

    @builtins.property
    def log_retention_role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''The IAM role for the Lambda function associated with the custom resource that sets the retention policy.

        :default: - A new role is created.
        '''
        result = self._values.get("log_retention_role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    @builtins.property
    def memory_size(self) -> typing.Optional[jsii.Number]:
        '''The amount of memory, in MB, that is allocated to your Lambda function.

        Lambda uses this value to proportionally allocate the amount of CPU
        power. For more information, see Resource Model in the AWS Lambda
        Developer Guide.

        :default: 128
        '''
        result = self._values.get("memory_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def params_and_secrets(
        self,
    ) -> typing.Optional[_ParamsAndSecretsLayerVersion_dce97f06]:
        '''Specify the configuration of Parameters and Secrets Extension.

        :default: - No Parameters and Secrets Extension

        :see: https://docs.aws.amazon.com/systems-manager/latest/userguide/ps-integration-lambda-extensions.html
        '''
        result = self._values.get("params_and_secrets")
        return typing.cast(typing.Optional[_ParamsAndSecretsLayerVersion_dce97f06], result)

    @builtins.property
    def profiling(self) -> typing.Optional[builtins.bool]:
        '''Enable profiling.

        :default: - No profiling.

        :see: https://docs.aws.amazon.com/codeguru/latest/profiler-ug/setting-up-lambda.html
        '''
        result = self._values.get("profiling")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def profiling_group(self) -> typing.Optional[_IProfilingGroup_0bba72c4]:
        '''Profiling Group.

        :default: - A new profiling group will be created if ``profiling`` is set.

        :see: https://docs.aws.amazon.com/codeguru/latest/profiler-ug/setting-up-lambda.html
        '''
        result = self._values.get("profiling_group")
        return typing.cast(typing.Optional[_IProfilingGroup_0bba72c4], result)

    @builtins.property
    def reserved_concurrent_executions(self) -> typing.Optional[jsii.Number]:
        '''The maximum of concurrent executions you want to reserve for the function.

        :default: - No specific limit - account limit.

        :see: https://docs.aws.amazon.com/lambda/latest/dg/concurrent-executions.html
        '''
        result = self._values.get("reserved_concurrent_executions")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''Lambda execution role.

        This is the role that will be assumed by the function upon execution.
        It controls the permissions that the function will have. The Role must
        be assumable by the 'lambda.amazonaws.com' service principal.

        The default Role automatically has permissions granted for Lambda execution. If you
        provide a Role, you must add the relevant AWS managed policies yourself.

        The relevant managed policies are "service-role/AWSLambdaBasicExecutionRole" and
        "service-role/AWSLambdaVPCAccessExecutionRole".

        :default:

        - A unique role will be generated for this lambda function.
        Both supplied and generated roles can always be changed by calling ``addToRolePolicy``.
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    @builtins.property
    def runtime_management_mode(
        self,
    ) -> typing.Optional[_RuntimeManagementMode_688c173b]:
        '''Sets the runtime management configuration for a function's version.

        :default: Auto
        '''
        result = self._values.get("runtime_management_mode")
        return typing.cast(typing.Optional[_RuntimeManagementMode_688c173b], result)

    @builtins.property
    def security_groups(self) -> typing.Optional[typing.List[_ISecurityGroup_acf8a799]]:
        '''The list of security groups to associate with the Lambda's network interfaces.

        Only used if 'vpc' is supplied.

        :default:

        - If the function is placed within a VPC and a security group is
        not specified, either by this or securityGroup prop, a dedicated security
        group will be created for this function.
        '''
        result = self._values.get("security_groups")
        return typing.cast(typing.Optional[typing.List[_ISecurityGroup_acf8a799]], result)

    @builtins.property
    def timeout(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The function execution time (in seconds) after which Lambda terminates the function.

        Because the execution time affects cost, set this value
        based on the function's expected execution time.

        :default: Duration.seconds(3)
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def tracing(self) -> typing.Optional[_Tracing_9fe8e2bb]:
        '''Enable AWS X-Ray Tracing for Lambda Function.

        :default: Tracing.Disabled
        '''
        result = self._values.get("tracing")
        return typing.cast(typing.Optional[_Tracing_9fe8e2bb], result)

    @builtins.property
    def vpc(self) -> typing.Optional[_IVpc_f30d5663]:
        '''VPC network to place Lambda network interfaces.

        Specify this if the Lambda function needs to access resources in a VPC.
        This is required when ``vpcSubnets`` is specified.

        :default: - Function is not placed within a VPC.
        '''
        result = self._values.get("vpc")
        return typing.cast(typing.Optional[_IVpc_f30d5663], result)

    @builtins.property
    def vpc_subnets(self) -> typing.Optional[_SubnetSelection_e57d76df]:
        '''Where to place the network interfaces within the VPC.

        This requires ``vpc`` to be specified in order for interfaces to actually be
        placed in the subnets. If ``vpc`` is not specify, this will raise an error.

        Note: Internet access for Lambda Functions requires a NAT Gateway, so picking
        public subnets is not allowed (unless ``allowPublicSubnet`` is set to ``true``).

        :default: - the Vpc default strategy if not specified
        '''
        result = self._values.get("vpc_subnets")
        return typing.cast(typing.Optional[_SubnetSelection_e57d76df], result)

    @builtins.property
    def code(self) -> _Code_7848f942:
        '''The source code of your Lambda function.

        You can point to a file in an
        Amazon Simple Storage Service (Amazon S3) bucket or specify your source
        code as inline text.
        '''
        result = self._values.get("code")
        assert result is not None, "Required property 'code' is missing"
        return typing.cast(_Code_7848f942, result)

    @builtins.property
    def handler(self) -> builtins.str:
        '''The name of the method within your code that Lambda calls to execute your function.

        The format includes the file name. It can also include
        namespaces and other qualifiers, depending on the runtime.
        For more information, see https://docs.aws.amazon.com/lambda/latest/dg/foundation-progmodel.html.

        Use ``Handler.FROM_IMAGE`` when defining a function from a Docker image.

        NOTE: If you specify your source code as inline text by specifying the
        ZipFile property within the Code property, specify index.function_name as
        the handler.
        '''
        result = self._values.get("handler")
        assert result is not None, "Required property 'handler' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def runtime(self) -> _Runtime_b4eaa844:
        '''The runtime environment for the Lambda function that you are uploading.

        For valid values, see the Runtime property in the AWS Lambda Developer
        Guide.

        Use ``Runtime.FROM_IMAGE`` when defining a function from a Docker image.
        '''
        result = self._values.get("runtime")
        assert result is not None, "Required property 'runtime' is missing"
        return typing.cast(_Runtime_b4eaa844, result)

    @builtins.property
    def execute_after(
        self,
    ) -> typing.Optional[typing.List[_constructs_77d1e7e8.Construct]]:
        '''Adds trigger dependencies. Execute this trigger only after these construct scopes have been provisioned.

        You can also use ``trigger.executeAfter()`` to add additional dependencies.

        :default: []
        '''
        result = self._values.get("execute_after")
        return typing.cast(typing.Optional[typing.List[_constructs_77d1e7e8.Construct]], result)

    @builtins.property
    def execute_before(
        self,
    ) -> typing.Optional[typing.List[_constructs_77d1e7e8.Construct]]:
        '''Adds this trigger as a dependency on other constructs.

        This means that this
        trigger will get executed *before* the given construct(s).

        You can also use ``trigger.executeBefore()`` to add additional dependants.

        :default: []
        '''
        result = self._values.get("execute_before")
        return typing.cast(typing.Optional[typing.List[_constructs_77d1e7e8.Construct]], result)

    @builtins.property
    def execute_on_handler_change(self) -> typing.Optional[builtins.bool]:
        '''Re-executes the trigger every time the handler changes.

        This implies that the trigger is associated with the ``currentVersion`` of
        the handler, which gets recreated every time the handler or its
        configuration is updated.

        :default: true
        '''
        result = self._values.get("execute_on_handler_change")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TriggerFunctionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ITrigger",
    "InvocationType",
    "Trigger",
    "TriggerFunction",
    "TriggerFunctionProps",
    "TriggerInvalidation",
    "TriggerOptions",
    "TriggerProps",
]

publication.publish()

def _typecheckingstub__1440952b0ad66bce206afd39f8df5d3131d1aec936e757ff45565c33d8e743de(
    *scopes: _constructs_77d1e7e8.Construct,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83c288d084243ca76dbe90e11a2ed762e4f9ff4be79125b9325e2b639f9bf225(
    *scopes: _constructs_77d1e7e8.Construct,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b7d2333ea709a924a3374ea45391de202dd23ab9ad7b9dc22d6b36d95aab023(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    handler: _Function_244f85d8,
    invocation_type: typing.Optional[InvocationType] = None,
    timeout: typing.Optional[_Duration_4839e8c3] = None,
    execute_after: typing.Optional[typing.Sequence[_constructs_77d1e7e8.Construct]] = None,
    execute_before: typing.Optional[typing.Sequence[_constructs_77d1e7e8.Construct]] = None,
    execute_on_handler_change: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60d0e9556ead797bb961db69cb5121040091279632390d475d4c2209fb0ffc70(
    *scopes: _constructs_77d1e7e8.Construct,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53346c2d06fbc7c3a1bbe51e2105eef0d748c9336faeb91d2007168d162b5fe5(
    *scopes: _constructs_77d1e7e8.Construct,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f34c5ba084706d20d6ef37a7f59673b20ed3425ffc7035fc8ea888e9f68bdd9(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    code: _Code_7848f942,
    handler: builtins.str,
    runtime: _Runtime_b4eaa844,
    execute_after: typing.Optional[typing.Sequence[_constructs_77d1e7e8.Construct]] = None,
    execute_before: typing.Optional[typing.Sequence[_constructs_77d1e7e8.Construct]] = None,
    execute_on_handler_change: typing.Optional[builtins.bool] = None,
    adot_instrumentation: typing.Optional[typing.Union[_AdotInstrumentationConfig_7c38d65d, typing.Dict[builtins.str, typing.Any]]] = None,
    allow_all_outbound: typing.Optional[builtins.bool] = None,
    allow_public_subnet: typing.Optional[builtins.bool] = None,
    architecture: typing.Optional[_Architecture_12d5a53f] = None,
    code_signing_config: typing.Optional[_ICodeSigningConfig_edb41d1f] = None,
    current_version_options: typing.Optional[typing.Union[_VersionOptions_981bb3c0, typing.Dict[builtins.str, typing.Any]]] = None,
    dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
    dead_letter_queue_enabled: typing.Optional[builtins.bool] = None,
    dead_letter_topic: typing.Optional[_ITopic_9eca4852] = None,
    description: typing.Optional[builtins.str] = None,
    environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    environment_encryption: typing.Optional[_IKey_5f11635f] = None,
    ephemeral_storage_size: typing.Optional[_Size_7b441c34] = None,
    events: typing.Optional[typing.Sequence[_IEventSource_3686b3f8]] = None,
    filesystem: typing.Optional[_FileSystem_a5fa005d] = None,
    function_name: typing.Optional[builtins.str] = None,
    initial_policy: typing.Optional[typing.Sequence[_PolicyStatement_0fe33853]] = None,
    insights_version: typing.Optional[_LambdaInsightsVersion_9dfbfef9] = None,
    layers: typing.Optional[typing.Sequence[_ILayerVersion_5ac127c8]] = None,
    log_retention: typing.Optional[_RetentionDays_070f99f0] = None,
    log_retention_retry_options: typing.Optional[typing.Union[_LogRetentionRetryOptions_ad797a7a, typing.Dict[builtins.str, typing.Any]]] = None,
    log_retention_role: typing.Optional[_IRole_235f5d8e] = None,
    memory_size: typing.Optional[jsii.Number] = None,
    params_and_secrets: typing.Optional[_ParamsAndSecretsLayerVersion_dce97f06] = None,
    profiling: typing.Optional[builtins.bool] = None,
    profiling_group: typing.Optional[_IProfilingGroup_0bba72c4] = None,
    reserved_concurrent_executions: typing.Optional[jsii.Number] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
    runtime_management_mode: typing.Optional[_RuntimeManagementMode_688c173b] = None,
    security_groups: typing.Optional[typing.Sequence[_ISecurityGroup_acf8a799]] = None,
    timeout: typing.Optional[_Duration_4839e8c3] = None,
    tracing: typing.Optional[_Tracing_9fe8e2bb] = None,
    vpc: typing.Optional[_IVpc_f30d5663] = None,
    vpc_subnets: typing.Optional[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]] = None,
    max_event_age: typing.Optional[_Duration_4839e8c3] = None,
    on_failure: typing.Optional[_IDestination_40f19de4] = None,
    on_success: typing.Optional[_IDestination_40f19de4] = None,
    retry_attempts: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90250696d445460d02b427f820f1d5da99cca60cf5bd9e0352e63062c8f24bc9(
    *scopes: _constructs_77d1e7e8.Construct,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3a39b559574edf1b66218b9829d7f7cb9718777ead4c37c75db4b04ce680f72(
    *scopes: _constructs_77d1e7e8.Construct,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5a182040d846d549ba242a7734148186c69e4de0d60c879b2b64ef1229e176d(
    *,
    execute_after: typing.Optional[typing.Sequence[_constructs_77d1e7e8.Construct]] = None,
    execute_before: typing.Optional[typing.Sequence[_constructs_77d1e7e8.Construct]] = None,
    execute_on_handler_change: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59427805740f705ff9572f1711767f2e394b5cfe9e0d4149bd301d8a94bf4ae0(
    *,
    execute_after: typing.Optional[typing.Sequence[_constructs_77d1e7e8.Construct]] = None,
    execute_before: typing.Optional[typing.Sequence[_constructs_77d1e7e8.Construct]] = None,
    execute_on_handler_change: typing.Optional[builtins.bool] = None,
    handler: _Function_244f85d8,
    invocation_type: typing.Optional[InvocationType] = None,
    timeout: typing.Optional[_Duration_4839e8c3] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2f4b009b0160d566d798bfa6d813ccc8440e1a9e0f75c99449184a2fc126f91(
    *,
    max_event_age: typing.Optional[_Duration_4839e8c3] = None,
    on_failure: typing.Optional[_IDestination_40f19de4] = None,
    on_success: typing.Optional[_IDestination_40f19de4] = None,
    retry_attempts: typing.Optional[jsii.Number] = None,
    adot_instrumentation: typing.Optional[typing.Union[_AdotInstrumentationConfig_7c38d65d, typing.Dict[builtins.str, typing.Any]]] = None,
    allow_all_outbound: typing.Optional[builtins.bool] = None,
    allow_public_subnet: typing.Optional[builtins.bool] = None,
    architecture: typing.Optional[_Architecture_12d5a53f] = None,
    code_signing_config: typing.Optional[_ICodeSigningConfig_edb41d1f] = None,
    current_version_options: typing.Optional[typing.Union[_VersionOptions_981bb3c0, typing.Dict[builtins.str, typing.Any]]] = None,
    dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
    dead_letter_queue_enabled: typing.Optional[builtins.bool] = None,
    dead_letter_topic: typing.Optional[_ITopic_9eca4852] = None,
    description: typing.Optional[builtins.str] = None,
    environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    environment_encryption: typing.Optional[_IKey_5f11635f] = None,
    ephemeral_storage_size: typing.Optional[_Size_7b441c34] = None,
    events: typing.Optional[typing.Sequence[_IEventSource_3686b3f8]] = None,
    filesystem: typing.Optional[_FileSystem_a5fa005d] = None,
    function_name: typing.Optional[builtins.str] = None,
    initial_policy: typing.Optional[typing.Sequence[_PolicyStatement_0fe33853]] = None,
    insights_version: typing.Optional[_LambdaInsightsVersion_9dfbfef9] = None,
    layers: typing.Optional[typing.Sequence[_ILayerVersion_5ac127c8]] = None,
    log_retention: typing.Optional[_RetentionDays_070f99f0] = None,
    log_retention_retry_options: typing.Optional[typing.Union[_LogRetentionRetryOptions_ad797a7a, typing.Dict[builtins.str, typing.Any]]] = None,
    log_retention_role: typing.Optional[_IRole_235f5d8e] = None,
    memory_size: typing.Optional[jsii.Number] = None,
    params_and_secrets: typing.Optional[_ParamsAndSecretsLayerVersion_dce97f06] = None,
    profiling: typing.Optional[builtins.bool] = None,
    profiling_group: typing.Optional[_IProfilingGroup_0bba72c4] = None,
    reserved_concurrent_executions: typing.Optional[jsii.Number] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
    runtime_management_mode: typing.Optional[_RuntimeManagementMode_688c173b] = None,
    security_groups: typing.Optional[typing.Sequence[_ISecurityGroup_acf8a799]] = None,
    timeout: typing.Optional[_Duration_4839e8c3] = None,
    tracing: typing.Optional[_Tracing_9fe8e2bb] = None,
    vpc: typing.Optional[_IVpc_f30d5663] = None,
    vpc_subnets: typing.Optional[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]] = None,
    code: _Code_7848f942,
    handler: builtins.str,
    runtime: _Runtime_b4eaa844,
    execute_after: typing.Optional[typing.Sequence[_constructs_77d1e7e8.Construct]] = None,
    execute_before: typing.Optional[typing.Sequence[_constructs_77d1e7e8.Construct]] = None,
    execute_on_handler_change: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass
