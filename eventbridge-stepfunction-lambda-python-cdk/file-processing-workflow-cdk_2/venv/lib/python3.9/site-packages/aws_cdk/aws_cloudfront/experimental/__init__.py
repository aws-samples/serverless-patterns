import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from ..._jsii import *

import constructs as _constructs_77d1e7e8
from ... import (
    Duration as _Duration_4839e8c3,
    Resource as _Resource_45bc6135,
    Size as _Size_7b441c34,
)
from ...aws_cloudwatch import (
    Metric as _Metric_e396a4dc,
    MetricOptions as _MetricOptions_1788b62f,
    Unit as _Unit_61bc6f70,
)
from ...aws_codeguruprofiler import IProfilingGroup as _IProfilingGroup_0bba72c4
from ...aws_ec2 import (
    Connections as _Connections_0f31fce8,
    ISecurityGroup as _ISecurityGroup_acf8a799,
    IVpc as _IVpc_f30d5663,
    SubnetSelection as _SubnetSelection_e57d76df,
)
from ...aws_iam import (
    Grant as _Grant_a7ae64f8,
    IGrantable as _IGrantable_71c4f5de,
    IPrincipal as _IPrincipal_539bb2fd,
    IRole as _IRole_235f5d8e,
    PolicyStatement as _PolicyStatement_0fe33853,
)
from ...aws_kms import IKey as _IKey_5f11635f
from ...aws_lambda import (
    AdotInstrumentationConfig as _AdotInstrumentationConfig_7c38d65d,
    Alias as _Alias_55be8873,
    AliasOptions as _AliasOptions_61fd38e4,
    Architecture as _Architecture_12d5a53f,
    Code as _Code_7848f942,
    EventInvokeConfigOptions as _EventInvokeConfigOptions_42b67f17,
    EventSourceMapping as _EventSourceMapping_556828d7,
    EventSourceMappingOptions as _EventSourceMappingOptions_b3f2bb85,
    FileSystem as _FileSystem_a5fa005d,
    FunctionProps as _FunctionProps_a308e854,
    FunctionUrl as _FunctionUrl_aff26443,
    FunctionUrlAuthType as _FunctionUrlAuthType_9c7b2c86,
    FunctionUrlCorsOptions as _FunctionUrlCorsOptions_ca855cc0,
    FunctionUrlOptions as _FunctionUrlOptions_84d38c38,
    ICodeSigningConfig as _ICodeSigningConfig_edb41d1f,
    IDestination as _IDestination_40f19de4,
    IEventSource as _IEventSource_3686b3f8,
    IEventSourceDlq as _IEventSourceDlq_5e2c6ad9,
    IFunction as _IFunction_6adb0ab8,
    ILayerVersion as _ILayerVersion_5ac127c8,
    IVersion as _IVersion_faf7234e,
    InvokeMode as _InvokeMode_e7b50559,
    LambdaInsightsVersion as _LambdaInsightsVersion_9dfbfef9,
    LogRetentionRetryOptions as _LogRetentionRetryOptions_ad797a7a,
    ParamsAndSecretsLayerVersion as _ParamsAndSecretsLayerVersion_dce97f06,
    Permission as _Permission_9def3964,
    Runtime as _Runtime_b4eaa844,
    RuntimeManagementMode as _RuntimeManagementMode_688c173b,
    SourceAccessConfiguration as _SourceAccessConfiguration_1926ff89,
    StartingPosition as _StartingPosition_c0a4852c,
    Tracing as _Tracing_9fe8e2bb,
    VersionOptions as _VersionOptions_981bb3c0,
    VersionWeight as _VersionWeight_64df085b,
)
from ...aws_logs import RetentionDays as _RetentionDays_070f99f0
from ...aws_sns import ITopic as _ITopic_9eca4852
from ...aws_sqs import IQueue as _IQueue_7ed6f679


@jsii.implements(_IVersion_faf7234e)
class EdgeFunction(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudfront.experimental.EdgeFunction",
):
    '''A Lambda@Edge function.

    Convenience resource for requesting a Lambda function in the 'us-east-1' region for use with Lambda@Edge.
    Implements several restrictions enforced by Lambda@Edge.

    Note that this construct requires that the 'us-east-1' region has been bootstrapped.
    See https://docs.aws.amazon.com/cdk/latest/guide/bootstrapping.html or 'cdk bootstrap --help' for options.

    :resource: AWS::Lambda::Function
    :exampleMetadata: infused

    Example::

        # my_bucket: s3.Bucket
        # A Lambda@Edge function added to default behavior of a Distribution
        # and triggered on every request
        my_func = cloudfront.experimental.EdgeFunction(self, "MyFunction",
            runtime=lambda_.Runtime.NODEJS_14_X,
            handler="index.handler",
            code=lambda_.Code.from_asset(path.join(__dirname, "lambda-handler"))
        )
        cloudfront.Distribution(self, "myDist",
            default_behavior=cloudfront.BehaviorOptions(
                origin=origins.S3Origin(my_bucket),
                edge_lambdas=[cloudfront.EdgeLambda(
                    function_version=my_func.current_version,
                    event_type=cloudfront.LambdaEdgeEventType.VIEWER_REQUEST
                )
                ]
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        stack_id: typing.Optional[builtins.str] = None,
        code: _Code_7848f942,
        handler: builtins.str,
        runtime: _Runtime_b4eaa844,
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
        :param stack_id: The stack ID of Lambda@Edge function. Default: - ``edge-lambda-stack-${region}``
        :param code: The source code of your Lambda function. You can point to a file in an Amazon Simple Storage Service (Amazon S3) bucket or specify your source code as inline text.
        :param handler: The name of the method within your code that Lambda calls to execute your function. The format includes the file name. It can also include namespaces and other qualifiers, depending on the runtime. For more information, see https://docs.aws.amazon.com/lambda/latest/dg/foundation-progmodel.html. Use ``Handler.FROM_IMAGE`` when defining a function from a Docker image. NOTE: If you specify your source code as inline text by specifying the ZipFile property within the Code property, specify index.function_name as the handler.
        :param runtime: The runtime environment for the Lambda function that you are uploading. For valid values, see the Runtime property in the AWS Lambda Developer Guide. Use ``Runtime.FROM_IMAGE`` when defining a function from a Docker image.
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
            type_hints = typing.get_type_hints(_typecheckingstub__b2f96e5632f259adb036f7aba2bbc7c19fd9840c647d67a10a8135cb35edd4fd)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = EdgeFunctionProps(
            stack_id=stack_id,
            code=code,
            handler=handler,
            runtime=runtime,
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

    @jsii.member(jsii_name="addAlias")
    def add_alias(
        self,
        alias_name: builtins.str,
        *,
        additional_versions: typing.Optional[typing.Sequence[typing.Union[_VersionWeight_64df085b, typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        provisioned_concurrent_executions: typing.Optional[jsii.Number] = None,
        max_event_age: typing.Optional[_Duration_4839e8c3] = None,
        on_failure: typing.Optional[_IDestination_40f19de4] = None,
        on_success: typing.Optional[_IDestination_40f19de4] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
    ) -> _Alias_55be8873:
        '''Defines an alias for this version.

        :param alias_name: -
        :param additional_versions: Additional versions with individual weights this alias points to. Individual additional version weights specified here should add up to (less than) one. All remaining weight is routed to the default version. For example, the config is version: "1" additionalVersions: [{ version: "2", weight: 0.05 }] Then 5% of traffic will be routed to function version 2, while the remaining 95% of traffic will be routed to function version 1. Default: No additional versions
        :param description: Description for the alias. Default: No description
        :param provisioned_concurrent_executions: Specifies a provisioned concurrency configuration for a function's alias. Default: No provisioned concurrency
        :param max_event_age: The maximum age of a request that Lambda sends to a function for processing. Minimum: 60 seconds Maximum: 6 hours Default: Duration.hours(6)
        :param on_failure: The destination for failed invocations. Default: - no destination
        :param on_success: The destination for successful invocations. Default: - no destination
        :param retry_attempts: The maximum number of times to retry when the function returns an error. Minimum: 0 Maximum: 2 Default: 2
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71584facfd686f7aa59df4ac72c76bd89b4c7702ed892615c35a6928eead9b01)
            check_type(argname="argument alias_name", value=alias_name, expected_type=type_hints["alias_name"])
        options = _AliasOptions_61fd38e4(
            additional_versions=additional_versions,
            description=description,
            provisioned_concurrent_executions=provisioned_concurrent_executions,
            max_event_age=max_event_age,
            on_failure=on_failure,
            on_success=on_success,
            retry_attempts=retry_attempts,
        )

        return typing.cast(_Alias_55be8873, jsii.invoke(self, "addAlias", [alias_name, options]))

    @jsii.member(jsii_name="addEventSource")
    def add_event_source(self, source: _IEventSource_3686b3f8) -> None:
        '''Adds an event source to this function.

        :param source: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__55f33cdcdd9ce575affd43f849b278eaf1db3da08d4ae8ba312f375918646a1b)
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
        return typing.cast(None, jsii.invoke(self, "addEventSource", [source]))

    @jsii.member(jsii_name="addEventSourceMapping")
    def add_event_source_mapping(
        self,
        id: builtins.str,
        *,
        batch_size: typing.Optional[jsii.Number] = None,
        bisect_batch_on_error: typing.Optional[builtins.bool] = None,
        enabled: typing.Optional[builtins.bool] = None,
        event_source_arn: typing.Optional[builtins.str] = None,
        filters: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, typing.Any]]] = None,
        kafka_bootstrap_servers: typing.Optional[typing.Sequence[builtins.str]] = None,
        kafka_consumer_group_id: typing.Optional[builtins.str] = None,
        kafka_topic: typing.Optional[builtins.str] = None,
        max_batching_window: typing.Optional[_Duration_4839e8c3] = None,
        max_concurrency: typing.Optional[jsii.Number] = None,
        max_record_age: typing.Optional[_Duration_4839e8c3] = None,
        on_failure: typing.Optional[_IEventSourceDlq_5e2c6ad9] = None,
        parallelization_factor: typing.Optional[jsii.Number] = None,
        report_batch_item_failures: typing.Optional[builtins.bool] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
        source_access_configurations: typing.Optional[typing.Sequence[typing.Union[_SourceAccessConfiguration_1926ff89, typing.Dict[builtins.str, typing.Any]]]] = None,
        starting_position: typing.Optional[_StartingPosition_c0a4852c] = None,
        starting_position_timestamp: typing.Optional[jsii.Number] = None,
        tumbling_window: typing.Optional[_Duration_4839e8c3] = None,
    ) -> _EventSourceMapping_556828d7:
        '''Adds an event source that maps to this AWS Lambda function.

        :param id: -
        :param batch_size: The largest number of records that AWS Lambda will retrieve from your event source at the time of invoking your function. Your function receives an event with all the retrieved records. Valid Range: Minimum value of 1. Maximum value of 10000. Default: - Amazon Kinesis, Amazon DynamoDB, and Amazon MSK is 100 records. The default for Amazon SQS is 10 messages. For standard SQS queues, the maximum is 10,000. For FIFO SQS queues, the maximum is 10.
        :param bisect_batch_on_error: If the function returns an error, split the batch in two and retry. Default: false
        :param enabled: Set to false to disable the event source upon creation. Default: true
        :param event_source_arn: The Amazon Resource Name (ARN) of the event source. Any record added to this stream can invoke the Lambda function. Default: - not set if using a self managed Kafka cluster, throws an error otherwise
        :param filters: Add filter criteria to Event Source. Default: - none
        :param kafka_bootstrap_servers: A list of host and port pairs that are the addresses of the Kafka brokers in a self managed "bootstrap" Kafka cluster that a Kafka client connects to initially to bootstrap itself. They are in the format ``abc.example.com:9096``. Default: - none
        :param kafka_consumer_group_id: The identifier for the Kafka consumer group to join. The consumer group ID must be unique among all your Kafka event sources. After creating a Kafka event source mapping with the consumer group ID specified, you cannot update this value. The value must have a lenght between 1 and 200 and full the pattern '[a-zA-Z0-9-/*:_+=.@-]*'. For more information, see `Customizable consumer group ID <https://docs.aws.amazon.com/lambda/latest/dg/with-msk.html#services-msk-consumer-group-id>`_. Default: - none
        :param kafka_topic: The name of the Kafka topic. Default: - no topic
        :param max_batching_window: The maximum amount of time to gather records before invoking the function. Maximum of Duration.minutes(5) Default: Duration.seconds(0)
        :param max_concurrency: The maximum concurrency setting limits the number of concurrent instances of the function that an Amazon SQS event source can invoke. Default: - No specific limit.
        :param max_record_age: The maximum age of a record that Lambda sends to a function for processing. Valid Range: - Minimum value of 60 seconds - Maximum value of 7 days Default: - infinite or until the record expires.
        :param on_failure: An Amazon SQS queue or Amazon SNS topic destination for discarded records. Default: discarded records are ignored
        :param parallelization_factor: The number of batches to process from each shard concurrently. Valid Range: - Minimum value of 1 - Maximum value of 10 Default: 1
        :param report_batch_item_failures: Allow functions to return partially successful responses for a batch of records. Default: false
        :param retry_attempts: The maximum number of times to retry when the function returns an error. Set to ``undefined`` if you want lambda to keep retrying infinitely or until the record expires. Valid Range: - Minimum value of 0 - Maximum value of 10000 Default: - infinite or until the record expires.
        :param source_access_configurations: Specific settings like the authentication protocol or the VPC components to secure access to your event source. Default: - none
        :param starting_position: The position in the DynamoDB, Kinesis or MSK stream where AWS Lambda should start reading. Default: - no starting position
        :param starting_position_timestamp: The time from which to start reading, in Unix time seconds. Default: - no timestamp
        :param tumbling_window: The size of the tumbling windows to group records sent to DynamoDB or Kinesis. Default: - None
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3a2f6769309cd3c52da869813738e2d4a94d233e574ada7ebba1654d2c4a3db)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = _EventSourceMappingOptions_b3f2bb85(
            batch_size=batch_size,
            bisect_batch_on_error=bisect_batch_on_error,
            enabled=enabled,
            event_source_arn=event_source_arn,
            filters=filters,
            kafka_bootstrap_servers=kafka_bootstrap_servers,
            kafka_consumer_group_id=kafka_consumer_group_id,
            kafka_topic=kafka_topic,
            max_batching_window=max_batching_window,
            max_concurrency=max_concurrency,
            max_record_age=max_record_age,
            on_failure=on_failure,
            parallelization_factor=parallelization_factor,
            report_batch_item_failures=report_batch_item_failures,
            retry_attempts=retry_attempts,
            source_access_configurations=source_access_configurations,
            starting_position=starting_position,
            starting_position_timestamp=starting_position_timestamp,
            tumbling_window=tumbling_window,
        )

        return typing.cast(_EventSourceMapping_556828d7, jsii.invoke(self, "addEventSourceMapping", [id, options]))

    @jsii.member(jsii_name="addFunctionUrl")
    def add_function_url(
        self,
        *,
        auth_type: typing.Optional[_FunctionUrlAuthType_9c7b2c86] = None,
        cors: typing.Optional[typing.Union[_FunctionUrlCorsOptions_ca855cc0, typing.Dict[builtins.str, typing.Any]]] = None,
        invoke_mode: typing.Optional[_InvokeMode_e7b50559] = None,
    ) -> _FunctionUrl_aff26443:
        '''Adds a url to this lambda function.

        :param auth_type: The type of authentication that your function URL uses. Default: FunctionUrlAuthType.AWS_IAM
        :param cors: The cross-origin resource sharing (CORS) settings for your function URL. Default: - No CORS configuration.
        :param invoke_mode: The type of invocation mode that your Lambda function uses. Default: InvokeMode.BUFFERED
        '''
        options = _FunctionUrlOptions_84d38c38(
            auth_type=auth_type, cors=cors, invoke_mode=invoke_mode
        )

        return typing.cast(_FunctionUrl_aff26443, jsii.invoke(self, "addFunctionUrl", [options]))

    @jsii.member(jsii_name="addPermission")
    def add_permission(
        self,
        id: builtins.str,
        *,
        principal: _IPrincipal_539bb2fd,
        action: typing.Optional[builtins.str] = None,
        event_source_token: typing.Optional[builtins.str] = None,
        function_url_auth_type: typing.Optional[_FunctionUrlAuthType_9c7b2c86] = None,
        organization_id: typing.Optional[builtins.str] = None,
        scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
        source_account: typing.Optional[builtins.str] = None,
        source_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Adds a permission to the Lambda resource policy.

        :param id: -
        :param principal: The entity for which you are granting permission to invoke the Lambda function. This entity can be any of the following: - a valid AWS service principal, such as ``s3.amazonaws.com`` or ``sns.amazonaws.com`` - an AWS account ID for cross-account permissions. For example, you might want to allow a custom application in another AWS account to push events to Lambda by invoking your function. - an AWS organization principal to grant permissions to an entire organization. The principal can be an AccountPrincipal, an ArnPrincipal, a ServicePrincipal, or an OrganizationPrincipal.
        :param action: The Lambda actions that you want to allow in this statement. For example, you can specify lambda:CreateFunction to specify a certain action, or use a wildcard (``lambda:*``) to grant permission to all Lambda actions. For a list of actions, see Actions and Condition Context Keys for AWS Lambda in the IAM User Guide. Default: 'lambda:InvokeFunction'
        :param event_source_token: A unique token that must be supplied by the principal invoking the function. Default: - The caller would not need to present a token.
        :param function_url_auth_type: The authType for the function URL that you are granting permissions for. Default: - No functionUrlAuthType
        :param organization_id: The organization you want to grant permissions to. Use this ONLY if you need to grant permissions to a subset of the organization. If you want to grant permissions to the entire organization, sending the organization principal through the ``principal`` property will suffice. You can use this property to ensure that all source principals are owned by a specific organization. Default: - No organizationId
        :param scope: The scope to which the permission constructs be attached. The default is the Lambda function construct itself, but this would need to be different in cases such as cross-stack references where the Permissions would need to sit closer to the consumer of this permission (i.e., the caller). Default: - The instance of lambda.IFunction
        :param source_account: The AWS account ID (without hyphens) of the source owner. For example, if you specify an S3 bucket in the SourceArn property, this value is the bucket owner's account ID. You can use this property to ensure that all source principals are owned by a specific account.
        :param source_arn: The ARN of a resource that is invoking your function. When granting Amazon Simple Storage Service (Amazon S3) permission to invoke your function, specify this property with the bucket ARN as its value. This ensures that events generated only from the specified bucket, not just any bucket from any AWS account that creates a mapping to your function, can invoke the function.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2eb22d84593be3f12d95da9b201a03a4c5bc3b744aa1e4ce7f555d5cdea7c4b9)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        permission = _Permission_9def3964(
            principal=principal,
            action=action,
            event_source_token=event_source_token,
            function_url_auth_type=function_url_auth_type,
            organization_id=organization_id,
            scope=scope,
            source_account=source_account,
            source_arn=source_arn,
        )

        return typing.cast(None, jsii.invoke(self, "addPermission", [id, permission]))

    @jsii.member(jsii_name="addToRolePolicy")
    def add_to_role_policy(self, statement: _PolicyStatement_0fe33853) -> None:
        '''Adds a statement to the IAM role assumed by the instance.

        :param statement: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__550534039580f7851495238ac3fb5cddb093d2dad5e39241df18f9f5b42a85f5)
            check_type(argname="argument statement", value=statement, expected_type=type_hints["statement"])
        return typing.cast(None, jsii.invoke(self, "addToRolePolicy", [statement]))

    @jsii.member(jsii_name="configureAsyncInvoke")
    def configure_async_invoke(
        self,
        *,
        max_event_age: typing.Optional[_Duration_4839e8c3] = None,
        on_failure: typing.Optional[_IDestination_40f19de4] = None,
        on_success: typing.Optional[_IDestination_40f19de4] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Configures options for asynchronous invocation.

        :param max_event_age: The maximum age of a request that Lambda sends to a function for processing. Minimum: 60 seconds Maximum: 6 hours Default: Duration.hours(6)
        :param on_failure: The destination for failed invocations. Default: - no destination
        :param on_success: The destination for successful invocations. Default: - no destination
        :param retry_attempts: The maximum number of times to retry when the function returns an error. Minimum: 0 Maximum: 2 Default: 2
        '''
        options = _EventInvokeConfigOptions_42b67f17(
            max_event_age=max_event_age,
            on_failure=on_failure,
            on_success=on_success,
            retry_attempts=retry_attempts,
        )

        return typing.cast(None, jsii.invoke(self, "configureAsyncInvoke", [options]))

    @jsii.member(jsii_name="grantInvoke")
    def grant_invoke(self, identity: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant the given identity permissions to invoke this Lambda.

        :param identity: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81021b991bbfca05164e4a606b5779ba5971abb7854ae9893435653d6d5421e0)
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantInvoke", [identity]))

    @jsii.member(jsii_name="grantInvokeUrl")
    def grant_invoke_url(self, identity: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant the given identity permissions to invoke this Lambda Function URL.

        :param identity: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d96b6feda81e352ac9cf655dd7c949f0071932768ea9b423e4bcc49841ebce16)
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantInvokeUrl", [identity]))

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
        '''Return the given named metric for this Lambda Return the given named metric for this Function.

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
            type_hints = typing.get_type_hints(_typecheckingstub__e35fb51736b3036c83dc4af9104a7ec11601ff54bef98bdf17e2325a3a1d9f89)
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
        '''Metric for the Duration of this Lambda How long execution of this Lambda takes.

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

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricDuration", [props]))

    @jsii.member(jsii_name="metricErrors")
    def metric_errors(
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
        '''How many invocations of this Lambda fail.

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

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricErrors", [props]))

    @jsii.member(jsii_name="metricInvocations")
    def metric_invocations(
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
        '''Metric for the number of invocations of this Lambda How often this Lambda is invoked.

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

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricInvocations", [props]))

    @jsii.member(jsii_name="metricThrottles")
    def metric_throttles(
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
        '''Metric for the number of throttled invocations of this Lambda How often this Lambda is throttled.

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

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricThrottles", [props]))

    @builtins.property
    @jsii.member(jsii_name="architecture")
    def architecture(self) -> _Architecture_12d5a53f:
        '''The system architectures compatible with this lambda function.'''
        return typing.cast(_Architecture_12d5a53f, jsii.get(self, "architecture"))

    @builtins.property
    @jsii.member(jsii_name="connections")
    def connections(self) -> _Connections_0f31fce8:
        '''Not supported.

        Connections are only applicable to VPC-enabled functions.
        '''
        return typing.cast(_Connections_0f31fce8, jsii.get(self, "connections"))

    @builtins.property
    @jsii.member(jsii_name="currentVersion")
    def current_version(self) -> _IVersion_faf7234e:
        '''Convenience method to make ``EdgeFunction`` conform to the same interface as ``Function``.'''
        return typing.cast(_IVersion_faf7234e, jsii.get(self, "currentVersion"))

    @builtins.property
    @jsii.member(jsii_name="edgeArn")
    def edge_arn(self) -> builtins.str:
        '''The ARN of the version for Lambda@Edge.'''
        return typing.cast(builtins.str, jsii.get(self, "edgeArn"))

    @builtins.property
    @jsii.member(jsii_name="functionArn")
    def function_arn(self) -> builtins.str:
        '''The ARN of the function.'''
        return typing.cast(builtins.str, jsii.get(self, "functionArn"))

    @builtins.property
    @jsii.member(jsii_name="functionName")
    def function_name(self) -> builtins.str:
        '''The name of the function.'''
        return typing.cast(builtins.str, jsii.get(self, "functionName"))

    @builtins.property
    @jsii.member(jsii_name="grantPrincipal")
    def grant_principal(self) -> _IPrincipal_539bb2fd:
        '''The principal to grant permissions to.'''
        return typing.cast(_IPrincipal_539bb2fd, jsii.get(self, "grantPrincipal"))

    @builtins.property
    @jsii.member(jsii_name="isBoundToVpc")
    def is_bound_to_vpc(self) -> builtins.bool:
        '''Whether or not this Lambda function was bound to a VPC.

        If this is is ``false``, trying to access the ``connections`` object will fail.
        '''
        return typing.cast(builtins.bool, jsii.get(self, "isBoundToVpc"))

    @builtins.property
    @jsii.member(jsii_name="lambda")
    def lambda_(self) -> _IFunction_6adb0ab8:
        '''The underlying AWS Lambda function.'''
        return typing.cast(_IFunction_6adb0ab8, jsii.get(self, "lambda"))

    @builtins.property
    @jsii.member(jsii_name="latestVersion")
    def latest_version(self) -> _IVersion_faf7234e:
        '''The ``$LATEST`` version of this function.

        Note that this is reference to a non-specific AWS Lambda version, which
        means the function this version refers to can return different results in
        different invocations.

        To obtain a reference to an explicit version which references the current
        function configuration, use ``lambdaFunction.currentVersion`` instead.
        '''
        return typing.cast(_IVersion_faf7234e, jsii.get(self, "latestVersion"))

    @builtins.property
    @jsii.member(jsii_name="permissionsNode")
    def permissions_node(self) -> _constructs_77d1e7e8.Node:
        '''The construct node where permissions are attached.'''
        return typing.cast(_constructs_77d1e7e8.Node, jsii.get(self, "permissionsNode"))

    @builtins.property
    @jsii.member(jsii_name="resourceArnsForGrantInvoke")
    def resource_arns_for_grant_invoke(self) -> typing.List[builtins.str]:
        '''The ARN(s) to put into the resource field of the generated IAM policy for grantInvoke().

        This property is for cdk modules to consume only. You should not need to use this property.
        Instead, use grantInvoke() directly.
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "resourceArnsForGrantInvoke"))

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        '''The most recently deployed version of this function.'''
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''The IAM role associated with this function.'''
        return typing.cast(typing.Optional[_IRole_235f5d8e], jsii.get(self, "role"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudfront.experimental.EdgeFunctionProps",
    jsii_struct_bases=[_FunctionProps_a308e854],
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
        "stack_id": "stackId",
    },
)
class EdgeFunctionProps(_FunctionProps_a308e854):
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
        stack_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for creating a Lambda@Edge function.

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
        :param stack_id: The stack ID of Lambda@Edge function. Default: - ``edge-lambda-stack-${region}``

        :exampleMetadata: infused

        Example::

            # my_bucket: s3.Bucket
            # A Lambda@Edge function added to default behavior of a Distribution
            # and triggered on every request
            my_func = cloudfront.experimental.EdgeFunction(self, "MyFunction",
                runtime=lambda_.Runtime.NODEJS_14_X,
                handler="index.handler",
                code=lambda_.Code.from_asset(path.join(__dirname, "lambda-handler"))
            )
            cloudfront.Distribution(self, "myDist",
                default_behavior=cloudfront.BehaviorOptions(
                    origin=origins.S3Origin(my_bucket),
                    edge_lambdas=[cloudfront.EdgeLambda(
                        function_version=my_func.current_version,
                        event_type=cloudfront.LambdaEdgeEventType.VIEWER_REQUEST
                    )
                    ]
                )
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
            type_hints = typing.get_type_hints(_typecheckingstub__709cdcb05c7a5fc7f7bcd1d72557097c39c5c534076a00b6b8db807bd38db33d)
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
            check_type(argname="argument stack_id", value=stack_id, expected_type=type_hints["stack_id"])
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
        if stack_id is not None:
            self._values["stack_id"] = stack_id

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
    def stack_id(self) -> typing.Optional[builtins.str]:
        '''The stack ID of Lambda@Edge function.

        :default: - ``edge-lambda-stack-${region}``
        '''
        result = self._values.get("stack_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EdgeFunctionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "EdgeFunction",
    "EdgeFunctionProps",
]

publication.publish()

def _typecheckingstub__b2f96e5632f259adb036f7aba2bbc7c19fd9840c647d67a10a8135cb35edd4fd(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    stack_id: typing.Optional[builtins.str] = None,
    code: _Code_7848f942,
    handler: builtins.str,
    runtime: _Runtime_b4eaa844,
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

def _typecheckingstub__71584facfd686f7aa59df4ac72c76bd89b4c7702ed892615c35a6928eead9b01(
    alias_name: builtins.str,
    *,
    additional_versions: typing.Optional[typing.Sequence[typing.Union[_VersionWeight_64df085b, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    provisioned_concurrent_executions: typing.Optional[jsii.Number] = None,
    max_event_age: typing.Optional[_Duration_4839e8c3] = None,
    on_failure: typing.Optional[_IDestination_40f19de4] = None,
    on_success: typing.Optional[_IDestination_40f19de4] = None,
    retry_attempts: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55f33cdcdd9ce575affd43f849b278eaf1db3da08d4ae8ba312f375918646a1b(
    source: _IEventSource_3686b3f8,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3a2f6769309cd3c52da869813738e2d4a94d233e574ada7ebba1654d2c4a3db(
    id: builtins.str,
    *,
    batch_size: typing.Optional[jsii.Number] = None,
    bisect_batch_on_error: typing.Optional[builtins.bool] = None,
    enabled: typing.Optional[builtins.bool] = None,
    event_source_arn: typing.Optional[builtins.str] = None,
    filters: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, typing.Any]]] = None,
    kafka_bootstrap_servers: typing.Optional[typing.Sequence[builtins.str]] = None,
    kafka_consumer_group_id: typing.Optional[builtins.str] = None,
    kafka_topic: typing.Optional[builtins.str] = None,
    max_batching_window: typing.Optional[_Duration_4839e8c3] = None,
    max_concurrency: typing.Optional[jsii.Number] = None,
    max_record_age: typing.Optional[_Duration_4839e8c3] = None,
    on_failure: typing.Optional[_IEventSourceDlq_5e2c6ad9] = None,
    parallelization_factor: typing.Optional[jsii.Number] = None,
    report_batch_item_failures: typing.Optional[builtins.bool] = None,
    retry_attempts: typing.Optional[jsii.Number] = None,
    source_access_configurations: typing.Optional[typing.Sequence[typing.Union[_SourceAccessConfiguration_1926ff89, typing.Dict[builtins.str, typing.Any]]]] = None,
    starting_position: typing.Optional[_StartingPosition_c0a4852c] = None,
    starting_position_timestamp: typing.Optional[jsii.Number] = None,
    tumbling_window: typing.Optional[_Duration_4839e8c3] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2eb22d84593be3f12d95da9b201a03a4c5bc3b744aa1e4ce7f555d5cdea7c4b9(
    id: builtins.str,
    *,
    principal: _IPrincipal_539bb2fd,
    action: typing.Optional[builtins.str] = None,
    event_source_token: typing.Optional[builtins.str] = None,
    function_url_auth_type: typing.Optional[_FunctionUrlAuthType_9c7b2c86] = None,
    organization_id: typing.Optional[builtins.str] = None,
    scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
    source_account: typing.Optional[builtins.str] = None,
    source_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__550534039580f7851495238ac3fb5cddb093d2dad5e39241df18f9f5b42a85f5(
    statement: _PolicyStatement_0fe33853,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81021b991bbfca05164e4a606b5779ba5971abb7854ae9893435653d6d5421e0(
    identity: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d96b6feda81e352ac9cf655dd7c949f0071932768ea9b423e4bcc49841ebce16(
    identity: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e35fb51736b3036c83dc4af9104a7ec11601ff54bef98bdf17e2325a3a1d9f89(
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

def _typecheckingstub__709cdcb05c7a5fc7f7bcd1d72557097c39c5c534076a00b6b8db807bd38db33d(
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
    stack_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
