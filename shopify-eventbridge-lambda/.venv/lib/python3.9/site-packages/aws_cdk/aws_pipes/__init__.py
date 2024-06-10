'''
# AWS::Pipes Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_pipes as pipes
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for Pipes construct libraries](https://constructs.dev/search?q=pipes)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::Pipes resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Pipes.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::Pipes](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Pipes.html).

(Read the [CDK Contributing Guide](https://github.com/aws/aws-cdk/blob/main/CONTRIBUTING.md) and submit an RFC if you are interested in contributing to this construct library.)

<!--END CFNONLY DISCLAIMER-->
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
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnPipe(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_pipes.CfnPipe",
):
    '''Specifies a pipe.

    Amazon EventBridge Pipes connect event sources to targets and reduces the need for specialized knowledge and integration code.
    .. epigraph::

       As an aid to help you jumpstart developing CloudFormation templates, the EventBridge console enables you to create templates from the existing pipes in your account. For more information, see `Generate an CloudFormation template from EventBridge Pipes <https://docs.aws.amazon.com/eventbridge/latest/userguide/pipes-generate-template.html>`_ in the *Amazon EventBridge User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pipes-pipe.html
    :cloudformationResource: AWS::Pipes::Pipe
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_pipes as pipes
        
        cfn_pipe = pipes.CfnPipe(self, "MyCfnPipe",
            role_arn="roleArn",
            source="source",
            target="target",
        
            # the properties below are optional
            description="description",
            desired_state="desiredState",
            enrichment="enrichment",
            enrichment_parameters=pipes.CfnPipe.PipeEnrichmentParametersProperty(
                http_parameters=pipes.CfnPipe.PipeEnrichmentHttpParametersProperty(
                    header_parameters={
                        "header_parameters_key": "headerParameters"
                    },
                    path_parameter_values=["pathParameterValues"],
                    query_string_parameters={
                        "query_string_parameters_key": "queryStringParameters"
                    }
                ),
                input_template="inputTemplate"
            ),
            log_configuration=pipes.CfnPipe.PipeLogConfigurationProperty(
                cloudwatch_logs_log_destination=pipes.CfnPipe.CloudwatchLogsLogDestinationProperty(
                    log_group_arn="logGroupArn"
                ),
                firehose_log_destination=pipes.CfnPipe.FirehoseLogDestinationProperty(
                    delivery_stream_arn="deliveryStreamArn"
                ),
                include_execution_data=["includeExecutionData"],
                level="level",
                s3_log_destination=pipes.CfnPipe.S3LogDestinationProperty(
                    bucket_name="bucketName",
                    bucket_owner="bucketOwner",
                    output_format="outputFormat",
                    prefix="prefix"
                )
            ),
            name="name",
            source_parameters=pipes.CfnPipe.PipeSourceParametersProperty(
                active_mq_broker_parameters=pipes.CfnPipe.PipeSourceActiveMQBrokerParametersProperty(
                    credentials=pipes.CfnPipe.MQBrokerAccessCredentialsProperty(
                        basic_auth="basicAuth"
                    ),
                    queue_name="queueName",
        
                    # the properties below are optional
                    batch_size=123,
                    maximum_batching_window_in_seconds=123
                ),
                dynamo_db_stream_parameters=pipes.CfnPipe.PipeSourceDynamoDBStreamParametersProperty(
                    starting_position="startingPosition",
        
                    # the properties below are optional
                    batch_size=123,
                    dead_letter_config=pipes.CfnPipe.DeadLetterConfigProperty(
                        arn="arn"
                    ),
                    maximum_batching_window_in_seconds=123,
                    maximum_record_age_in_seconds=123,
                    maximum_retry_attempts=123,
                    on_partial_batch_item_failure="onPartialBatchItemFailure",
                    parallelization_factor=123
                ),
                filter_criteria=pipes.CfnPipe.FilterCriteriaProperty(
                    filters=[pipes.CfnPipe.FilterProperty(
                        pattern="pattern"
                    )]
                ),
                kinesis_stream_parameters=pipes.CfnPipe.PipeSourceKinesisStreamParametersProperty(
                    starting_position="startingPosition",
        
                    # the properties below are optional
                    batch_size=123,
                    dead_letter_config=pipes.CfnPipe.DeadLetterConfigProperty(
                        arn="arn"
                    ),
                    maximum_batching_window_in_seconds=123,
                    maximum_record_age_in_seconds=123,
                    maximum_retry_attempts=123,
                    on_partial_batch_item_failure="onPartialBatchItemFailure",
                    parallelization_factor=123,
                    starting_position_timestamp="startingPositionTimestamp"
                ),
                managed_streaming_kafka_parameters=pipes.CfnPipe.PipeSourceManagedStreamingKafkaParametersProperty(
                    topic_name="topicName",
        
                    # the properties below are optional
                    batch_size=123,
                    consumer_group_id="consumerGroupId",
                    credentials=pipes.CfnPipe.MSKAccessCredentialsProperty(
                        client_certificate_tls_auth="clientCertificateTlsAuth",
                        sasl_scram512_auth="saslScram512Auth"
                    ),
                    maximum_batching_window_in_seconds=123,
                    starting_position="startingPosition"
                ),
                rabbit_mq_broker_parameters=pipes.CfnPipe.PipeSourceRabbitMQBrokerParametersProperty(
                    credentials=pipes.CfnPipe.MQBrokerAccessCredentialsProperty(
                        basic_auth="basicAuth"
                    ),
                    queue_name="queueName",
        
                    # the properties below are optional
                    batch_size=123,
                    maximum_batching_window_in_seconds=123,
                    virtual_host="virtualHost"
                ),
                self_managed_kafka_parameters=pipes.CfnPipe.PipeSourceSelfManagedKafkaParametersProperty(
                    topic_name="topicName",
        
                    # the properties below are optional
                    additional_bootstrap_servers=["additionalBootstrapServers"],
                    batch_size=123,
                    consumer_group_id="consumerGroupId",
                    credentials=pipes.CfnPipe.SelfManagedKafkaAccessConfigurationCredentialsProperty(
                        basic_auth="basicAuth",
                        client_certificate_tls_auth="clientCertificateTlsAuth",
                        sasl_scram256_auth="saslScram256Auth",
                        sasl_scram512_auth="saslScram512Auth"
                    ),
                    maximum_batching_window_in_seconds=123,
                    server_root_ca_certificate="serverRootCaCertificate",
                    starting_position="startingPosition",
                    vpc=pipes.CfnPipe.SelfManagedKafkaAccessConfigurationVpcProperty(
                        security_group=["securityGroup"],
                        subnets=["subnets"]
                    )
                ),
                sqs_queue_parameters=pipes.CfnPipe.PipeSourceSqsQueueParametersProperty(
                    batch_size=123,
                    maximum_batching_window_in_seconds=123
                )
            ),
            tags={
                "tags_key": "tags"
            },
            target_parameters=pipes.CfnPipe.PipeTargetParametersProperty(
                batch_job_parameters=pipes.CfnPipe.PipeTargetBatchJobParametersProperty(
                    job_definition="jobDefinition",
                    job_name="jobName",
        
                    # the properties below are optional
                    array_properties=pipes.CfnPipe.BatchArrayPropertiesProperty(
                        size=123
                    ),
                    container_overrides=pipes.CfnPipe.BatchContainerOverridesProperty(
                        command=["command"],
                        environment=[pipes.CfnPipe.BatchEnvironmentVariableProperty(
                            name="name",
                            value="value"
                        )],
                        instance_type="instanceType",
                        resource_requirements=[pipes.CfnPipe.BatchResourceRequirementProperty(
                            type="type",
                            value="value"
                        )]
                    ),
                    depends_on=[pipes.CfnPipe.BatchJobDependencyProperty(
                        job_id="jobId",
                        type="type"
                    )],
                    parameters={
                        "parameters_key": "parameters"
                    },
                    retry_strategy=pipes.CfnPipe.BatchRetryStrategyProperty(
                        attempts=123
                    )
                ),
                cloud_watch_logs_parameters=pipes.CfnPipe.PipeTargetCloudWatchLogsParametersProperty(
                    log_stream_name="logStreamName",
                    timestamp="timestamp"
                ),
                ecs_task_parameters=pipes.CfnPipe.PipeTargetEcsTaskParametersProperty(
                    task_definition_arn="taskDefinitionArn",
        
                    # the properties below are optional
                    capacity_provider_strategy=[pipes.CfnPipe.CapacityProviderStrategyItemProperty(
                        capacity_provider="capacityProvider",
        
                        # the properties below are optional
                        base=123,
                        weight=123
                    )],
                    enable_ecs_managed_tags=False,
                    enable_execute_command=False,
                    group="group",
                    launch_type="launchType",
                    network_configuration=pipes.CfnPipe.NetworkConfigurationProperty(
                        awsvpc_configuration=pipes.CfnPipe.AwsVpcConfigurationProperty(
                            subnets=["subnets"],
        
                            # the properties below are optional
                            assign_public_ip="assignPublicIp",
                            security_groups=["securityGroups"]
                        )
                    ),
                    overrides=pipes.CfnPipe.EcsTaskOverrideProperty(
                        container_overrides=[pipes.CfnPipe.EcsContainerOverrideProperty(
                            command=["command"],
                            cpu=123,
                            environment=[pipes.CfnPipe.EcsEnvironmentVariableProperty(
                                name="name",
                                value="value"
                            )],
                            environment_files=[pipes.CfnPipe.EcsEnvironmentFileProperty(
                                type="type",
                                value="value"
                            )],
                            memory=123,
                            memory_reservation=123,
                            name="name",
                            resource_requirements=[pipes.CfnPipe.EcsResourceRequirementProperty(
                                type="type",
                                value="value"
                            )]
                        )],
                        cpu="cpu",
                        ephemeral_storage=pipes.CfnPipe.EcsEphemeralStorageProperty(
                            size_in_gi_b=123
                        ),
                        execution_role_arn="executionRoleArn",
                        inference_accelerator_overrides=[pipes.CfnPipe.EcsInferenceAcceleratorOverrideProperty(
                            device_name="deviceName",
                            device_type="deviceType"
                        )],
                        memory="memory",
                        task_role_arn="taskRoleArn"
                    ),
                    placement_constraints=[pipes.CfnPipe.PlacementConstraintProperty(
                        expression="expression",
                        type="type"
                    )],
                    placement_strategy=[pipes.CfnPipe.PlacementStrategyProperty(
                        field="field",
                        type="type"
                    )],
                    platform_version="platformVersion",
                    propagate_tags="propagateTags",
                    reference_id="referenceId",
                    tags=[CfnTag(
                        key="key",
                        value="value"
                    )],
                    task_count=123
                ),
                event_bridge_event_bus_parameters=pipes.CfnPipe.PipeTargetEventBridgeEventBusParametersProperty(
                    detail_type="detailType",
                    endpoint_id="endpointId",
                    resources=["resources"],
                    source="source",
                    time="time"
                ),
                http_parameters=pipes.CfnPipe.PipeTargetHttpParametersProperty(
                    header_parameters={
                        "header_parameters_key": "headerParameters"
                    },
                    path_parameter_values=["pathParameterValues"],
                    query_string_parameters={
                        "query_string_parameters_key": "queryStringParameters"
                    }
                ),
                input_template="inputTemplate",
                kinesis_stream_parameters=pipes.CfnPipe.PipeTargetKinesisStreamParametersProperty(
                    partition_key="partitionKey"
                ),
                lambda_function_parameters=pipes.CfnPipe.PipeTargetLambdaFunctionParametersProperty(
                    invocation_type="invocationType"
                ),
                redshift_data_parameters=pipes.CfnPipe.PipeTargetRedshiftDataParametersProperty(
                    database="database",
                    sqls=["sqls"],
        
                    # the properties below are optional
                    db_user="dbUser",
                    secret_manager_arn="secretManagerArn",
                    statement_name="statementName",
                    with_event=False
                ),
                sage_maker_pipeline_parameters=pipes.CfnPipe.PipeTargetSageMakerPipelineParametersProperty(
                    pipeline_parameter_list=[pipes.CfnPipe.SageMakerPipelineParameterProperty(
                        name="name",
                        value="value"
                    )]
                ),
                sqs_queue_parameters=pipes.CfnPipe.PipeTargetSqsQueueParametersProperty(
                    message_deduplication_id="messageDeduplicationId",
                    message_group_id="messageGroupId"
                ),
                step_function_state_machine_parameters=pipes.CfnPipe.PipeTargetStateMachineParametersProperty(
                    invocation_type="invocationType"
                )
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        role_arn: builtins.str,
        source: builtins.str,
        target: builtins.str,
        description: typing.Optional[builtins.str] = None,
        desired_state: typing.Optional[builtins.str] = None,
        enrichment: typing.Optional[builtins.str] = None,
        enrichment_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPipe.PipeEnrichmentParametersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        log_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPipe.PipeLogConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        name: typing.Optional[builtins.str] = None,
        source_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPipe.PipeSourceParametersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        target_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPipe.PipeTargetParametersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param role_arn: The ARN of the role that allows the pipe to send data to the target.
        :param source: The ARN of the source resource.
        :param target: The ARN of the target resource.
        :param description: A description of the pipe.
        :param desired_state: The state the pipe should be in.
        :param enrichment: The ARN of the enrichment resource.
        :param enrichment_parameters: The parameters required to set up enrichment on your pipe.
        :param log_configuration: The logging configuration settings for the pipe.
        :param name: The name of the pipe.
        :param source_parameters: The parameters required to set up a source for your pipe.
        :param tags: The list of key-value pairs to associate with the pipe.
        :param target_parameters: The parameters required to set up a target for your pipe. For more information about pipe target parameters, including how to use dynamic path parameters, see `Target parameters <https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes-event-target.html>`_ in the *Amazon EventBridge User Guide* .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2590746a77e697feb25a71ec367eb957a7632f9fe5a46ae7e30476068534d683)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPipeProps(
            role_arn=role_arn,
            source=source,
            target=target,
            description=description,
            desired_state=desired_state,
            enrichment=enrichment,
            enrichment_parameters=enrichment_parameters,
            log_configuration=log_configuration,
            name=name,
            source_parameters=source_parameters,
            tags=tags,
            target_parameters=target_parameters,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__281eb4cd67e1ba036145aebcc10997c29984daadd10b66bef8033e25a39f3531)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c41a04b3c491b0925941962d0b7177857e979073f71bd9b6de38556def4efe12)
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
        '''The ARN of the pipe.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''The time the pipe was created.

        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrCurrentState")
    def attr_current_state(self) -> builtins.str:
        '''The state the pipe is in.

        :cloudformationAttribute: CurrentState
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCurrentState"))

    @builtins.property
    @jsii.member(jsii_name="attrLastModifiedTime")
    def attr_last_modified_time(self) -> builtins.str:
        '''When the pipe was last updated, in `ISO-8601 format <https://docs.aws.amazon.com/https://www.w3.org/TR/NOTE-datetime>`_ (YYYY-MM-DDThh:mm:ss.sTZD).

        :cloudformationAttribute: LastModifiedTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastModifiedTime"))

    @builtins.property
    @jsii.member(jsii_name="attrStateReason")
    def attr_state_reason(self) -> builtins.str:
        '''The reason the pipe is in its current state.

        :cloudformationAttribute: StateReason
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStateReason"))

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
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''The ARN of the role that allows the pipe to send data to the target.'''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__985ad2a14f580dd4275038980cbc387943f87211abf3e68fdb2f4755fdba5354)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(self) -> builtins.str:
        '''The ARN of the source resource.'''
        return typing.cast(builtins.str, jsii.get(self, "source"))

    @source.setter
    def source(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1fe18602cacd79eabcd3ef5565eda6cf280acd9362fd60e8a8059ed4ce59822)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "source", value)

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> builtins.str:
        '''The ARN of the target resource.'''
        return typing.cast(builtins.str, jsii.get(self, "target"))

    @target.setter
    def target(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__727f36b3af534d289c37e337ba67c6310e4420f9572ad6bbc62222fb26ecbb05)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the pipe.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25b696da604f323ac1a92ddfcc7ef102957b3d092e8137378e91cea16ea39501)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="desiredState")
    def desired_state(self) -> typing.Optional[builtins.str]:
        '''The state the pipe should be in.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "desiredState"))

    @desired_state.setter
    def desired_state(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ed87f6faacd73494b95f46c464263cf5f41d189f47daddc0b4607b7e1b5d9d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "desiredState", value)

    @builtins.property
    @jsii.member(jsii_name="enrichment")
    def enrichment(self) -> typing.Optional[builtins.str]:
        '''The ARN of the enrichment resource.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "enrichment"))

    @enrichment.setter
    def enrichment(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e73385dfe68409f0392cc314d936a945ec4656e8ef2f8c5b48def81168da23aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enrichment", value)

    @builtins.property
    @jsii.member(jsii_name="enrichmentParameters")
    def enrichment_parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.PipeEnrichmentParametersProperty"]]:
        '''The parameters required to set up enrichment on your pipe.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.PipeEnrichmentParametersProperty"]], jsii.get(self, "enrichmentParameters"))

    @enrichment_parameters.setter
    def enrichment_parameters(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.PipeEnrichmentParametersProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75aa67d8831c93b78f85f7319ad758289b207fec83baf9b92034cab4451f63d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enrichmentParameters", value)

    @builtins.property
    @jsii.member(jsii_name="logConfiguration")
    def log_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.PipeLogConfigurationProperty"]]:
        '''The logging configuration settings for the pipe.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.PipeLogConfigurationProperty"]], jsii.get(self, "logConfiguration"))

    @log_configuration.setter
    def log_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.PipeLogConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3975e792335934f36dcb66bc10ba0ab93afe079dae88c2011a2bacc35a8fe756)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the pipe.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e90ad70ab6477fe6112b4879f928b790cb38e40964bc2dde8bed7a3ba8008c71)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="sourceParameters")
    def source_parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.PipeSourceParametersProperty"]]:
        '''The parameters required to set up a source for your pipe.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.PipeSourceParametersProperty"]], jsii.get(self, "sourceParameters"))

    @source_parameters.setter
    def source_parameters(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.PipeSourceParametersProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef7a2d44f21af0c5ebeb25368be2b069abd76c8c64ba1cef587c3e219c88bec1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceParameters", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The list of key-value pairs to associate with the pipe.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4dba8d7cbad9d88d28d6a41b286be656a8aba98a10b5a338c7d175eab7061f25)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="targetParameters")
    def target_parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.PipeTargetParametersProperty"]]:
        '''The parameters required to set up a target for your pipe.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.PipeTargetParametersProperty"]], jsii.get(self, "targetParameters"))

    @target_parameters.setter
    def target_parameters(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.PipeTargetParametersProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6b5bbabe5f41fcd217d39a2fe0a41e5a7dcac510b412ddae1d12e74d71a1995)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetParameters", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pipes.CfnPipe.AwsVpcConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "subnets": "subnets",
            "assign_public_ip": "assignPublicIp",
            "security_groups": "securityGroups",
        },
    )
    class AwsVpcConfigurationProperty:
        def __init__(
            self,
            *,
            subnets: typing.Sequence[builtins.str],
            assign_public_ip: typing.Optional[builtins.str] = None,
            security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''This structure specifies the VPC subnets and security groups for the task, and whether a public IP address is to be used.

            This structure is relevant only for ECS tasks that use the ``awsvpc`` network mode.

            :param subnets: Specifies the subnets associated with the task. These subnets must all be in the same VPC. You can specify as many as 16 subnets.
            :param assign_public_ip: Specifies whether the task's elastic network interface receives a public IP address. You can specify ``ENABLED`` only when ``LaunchType`` in ``EcsParameters`` is set to ``FARGATE`` .
            :param security_groups: Specifies the security groups associated with the task. These security groups must all be in the same VPC. You can specify as many as five security groups. If you do not specify a security group, the default security group for the VPC is used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-awsvpcconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pipes as pipes
                
                aws_vpc_configuration_property = pipes.CfnPipe.AwsVpcConfigurationProperty(
                    subnets=["subnets"],
                
                    # the properties below are optional
                    assign_public_ip="assignPublicIp",
                    security_groups=["securityGroups"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5332578c4ac56ef4e1fdb629bb8be713eff47af3ee812e54c579d58784e9f78b)
                check_type(argname="argument subnets", value=subnets, expected_type=type_hints["subnets"])
                check_type(argname="argument assign_public_ip", value=assign_public_ip, expected_type=type_hints["assign_public_ip"])
                check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "subnets": subnets,
            }
            if assign_public_ip is not None:
                self._values["assign_public_ip"] = assign_public_ip
            if security_groups is not None:
                self._values["security_groups"] = security_groups

        @builtins.property
        def subnets(self) -> typing.List[builtins.str]:
            '''Specifies the subnets associated with the task.

            These subnets must all be in the same VPC. You can specify as many as 16 subnets.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-awsvpcconfiguration.html#cfn-pipes-pipe-awsvpcconfiguration-subnets
            '''
            result = self._values.get("subnets")
            assert result is not None, "Required property 'subnets' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def assign_public_ip(self) -> typing.Optional[builtins.str]:
            '''Specifies whether the task's elastic network interface receives a public IP address.

            You can specify ``ENABLED`` only when ``LaunchType`` in ``EcsParameters`` is set to ``FARGATE`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-awsvpcconfiguration.html#cfn-pipes-pipe-awsvpcconfiguration-assignpublicip
            '''
            result = self._values.get("assign_public_ip")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def security_groups(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Specifies the security groups associated with the task.

            These security groups must all be in the same VPC. You can specify as many as five security groups. If you do not specify a security group, the default security group for the VPC is used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-awsvpcconfiguration.html#cfn-pipes-pipe-awsvpcconfiguration-securitygroups
            '''
            result = self._values.get("security_groups")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AwsVpcConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pipes.CfnPipe.BatchArrayPropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={"size": "size"},
    )
    class BatchArrayPropertiesProperty:
        def __init__(self, *, size: typing.Optional[jsii.Number] = None) -> None:
            '''The array properties for the submitted job, such as the size of the array.

            The array size can be between 2 and 10,000. If you specify array properties for a job, it becomes an array job. This parameter is used only if the target is an AWS Batch job.

            :param size: The size of the array, if this is an array batch job. Default: - 0

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-batcharrayproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pipes as pipes
                
                batch_array_properties_property = pipes.CfnPipe.BatchArrayPropertiesProperty(
                    size=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__92192a261db9a36c55fcb7448e0173123454bca2fe715ba9d9aeb07eadf0530f)
                check_type(argname="argument size", value=size, expected_type=type_hints["size"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if size is not None:
                self._values["size"] = size

        @builtins.property
        def size(self) -> typing.Optional[jsii.Number]:
            '''The size of the array, if this is an array batch job.

            :default: - 0

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-batcharrayproperties.html#cfn-pipes-pipe-batcharrayproperties-size
            '''
            result = self._values.get("size")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BatchArrayPropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pipes.CfnPipe.BatchContainerOverridesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "command": "command",
            "environment": "environment",
            "instance_type": "instanceType",
            "resource_requirements": "resourceRequirements",
        },
    )
    class BatchContainerOverridesProperty:
        def __init__(
            self,
            *,
            command: typing.Optional[typing.Sequence[builtins.str]] = None,
            environment: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPipe.BatchEnvironmentVariableProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            instance_type: typing.Optional[builtins.str] = None,
            resource_requirements: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPipe.BatchResourceRequirementProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''The overrides that are sent to a container.

            :param command: The command to send to the container that overrides the default command from the Docker image or the task definition.
            :param environment: The environment variables to send to the container. You can add new environment variables, which are added to the container at launch, or you can override the existing environment variables from the Docker image or the task definition. .. epigraph:: Environment variables cannot start with " ``AWS Batch`` ". This naming convention is reserved for variables that AWS Batch sets.
            :param instance_type: The instance type to use for a multi-node parallel job. .. epigraph:: This parameter isn't applicable to single-node container jobs or jobs that run on Fargate resources, and shouldn't be provided.
            :param resource_requirements: The type and amount of resources to assign to a container. This overrides the settings in the job definition. The supported resources include ``GPU`` , ``MEMORY`` , and ``VCPU`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-batchcontaineroverrides.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pipes as pipes
                
                batch_container_overrides_property = pipes.CfnPipe.BatchContainerOverridesProperty(
                    command=["command"],
                    environment=[pipes.CfnPipe.BatchEnvironmentVariableProperty(
                        name="name",
                        value="value"
                    )],
                    instance_type="instanceType",
                    resource_requirements=[pipes.CfnPipe.BatchResourceRequirementProperty(
                        type="type",
                        value="value"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4e744d7df8a35e07450afdd20e33f3cfb5db1e9415e8c69615b236bf713417a3)
                check_type(argname="argument command", value=command, expected_type=type_hints["command"])
                check_type(argname="argument environment", value=environment, expected_type=type_hints["environment"])
                check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
                check_type(argname="argument resource_requirements", value=resource_requirements, expected_type=type_hints["resource_requirements"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if command is not None:
                self._values["command"] = command
            if environment is not None:
                self._values["environment"] = environment
            if instance_type is not None:
                self._values["instance_type"] = instance_type
            if resource_requirements is not None:
                self._values["resource_requirements"] = resource_requirements

        @builtins.property
        def command(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The command to send to the container that overrides the default command from the Docker image or the task definition.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-batchcontaineroverrides.html#cfn-pipes-pipe-batchcontaineroverrides-command
            '''
            result = self._values.get("command")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def environment(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPipe.BatchEnvironmentVariableProperty"]]]]:
            '''The environment variables to send to the container.

            You can add new environment variables, which are added to the container at launch, or you can override the existing environment variables from the Docker image or the task definition.
            .. epigraph::

               Environment variables cannot start with " ``AWS Batch`` ". This naming convention is reserved for variables that AWS Batch sets.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-batchcontaineroverrides.html#cfn-pipes-pipe-batchcontaineroverrides-environment
            '''
            result = self._values.get("environment")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPipe.BatchEnvironmentVariableProperty"]]]], result)

        @builtins.property
        def instance_type(self) -> typing.Optional[builtins.str]:
            '''The instance type to use for a multi-node parallel job.

            .. epigraph::

               This parameter isn't applicable to single-node container jobs or jobs that run on Fargate resources, and shouldn't be provided.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-batchcontaineroverrides.html#cfn-pipes-pipe-batchcontaineroverrides-instancetype
            '''
            result = self._values.get("instance_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def resource_requirements(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPipe.BatchResourceRequirementProperty"]]]]:
            '''The type and amount of resources to assign to a container.

            This overrides the settings in the job definition. The supported resources include ``GPU`` , ``MEMORY`` , and ``VCPU`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-batchcontaineroverrides.html#cfn-pipes-pipe-batchcontaineroverrides-resourcerequirements
            '''
            result = self._values.get("resource_requirements")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPipe.BatchResourceRequirementProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BatchContainerOverridesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pipes.CfnPipe.BatchEnvironmentVariableProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "value": "value"},
    )
    class BatchEnvironmentVariableProperty:
        def __init__(
            self,
            *,
            name: typing.Optional[builtins.str] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The environment variables to send to the container.

            You can add new environment variables, which are added to the container at launch, or you can override the existing environment variables from the Docker image or the task definition.
            .. epigraph::

               Environment variables cannot start with " ``AWS Batch`` ". This naming convention is reserved for variables that AWS Batch sets.

            :param name: The name of the key-value pair. For environment variables, this is the name of the environment variable.
            :param value: The value of the key-value pair. For environment variables, this is the value of the environment variable.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-batchenvironmentvariable.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pipes as pipes
                
                batch_environment_variable_property = pipes.CfnPipe.BatchEnvironmentVariableProperty(
                    name="name",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d6e3194d0527ccc74e30382a7dd1882664fde72ee15efb33743f945bf0a54b89)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if name is not None:
                self._values["name"] = name
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the key-value pair.

            For environment variables, this is the name of the environment variable.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-batchenvironmentvariable.html#cfn-pipes-pipe-batchenvironmentvariable-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''The value of the key-value pair.

            For environment variables, this is the value of the environment variable.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-batchenvironmentvariable.html#cfn-pipes-pipe-batchenvironmentvariable-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BatchEnvironmentVariableProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pipes.CfnPipe.BatchJobDependencyProperty",
        jsii_struct_bases=[],
        name_mapping={"job_id": "jobId", "type": "type"},
    )
    class BatchJobDependencyProperty:
        def __init__(
            self,
            *,
            job_id: typing.Optional[builtins.str] = None,
            type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''An object that represents an AWS Batch job dependency.

            :param job_id: The job ID of the AWS Batch job that's associated with this dependency.
            :param type: The type of the job dependency.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-batchjobdependency.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pipes as pipes
                
                batch_job_dependency_property = pipes.CfnPipe.BatchJobDependencyProperty(
                    job_id="jobId",
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2ea3de2ed5a4136d6fdec008bfc4898c56abd060a326a424ca01385c613d8a3b)
                check_type(argname="argument job_id", value=job_id, expected_type=type_hints["job_id"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if job_id is not None:
                self._values["job_id"] = job_id
            if type is not None:
                self._values["type"] = type

        @builtins.property
        def job_id(self) -> typing.Optional[builtins.str]:
            '''The job ID of the AWS Batch job that's associated with this dependency.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-batchjobdependency.html#cfn-pipes-pipe-batchjobdependency-jobid
            '''
            result = self._values.get("job_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''The type of the job dependency.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-batchjobdependency.html#cfn-pipes-pipe-batchjobdependency-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BatchJobDependencyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pipes.CfnPipe.BatchResourceRequirementProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type", "value": "value"},
    )
    class BatchResourceRequirementProperty:
        def __init__(self, *, type: builtins.str, value: builtins.str) -> None:
            '''The type and amount of a resource to assign to a container.

            The supported resources include ``GPU`` , ``MEMORY`` , and ``VCPU`` .

            :param type: The type of resource to assign to a container. The supported resources include ``GPU`` , ``MEMORY`` , and ``VCPU`` .
            :param value: The quantity of the specified resource to reserve for the container. The values vary based on the ``type`` specified. - **type="GPU"** - The number of physical GPUs to reserve for the container. Make sure that the number of GPUs reserved for all containers in a job doesn't exceed the number of available GPUs on the compute resource that the job is launched on. .. epigraph:: GPUs aren't available for jobs that are running on Fargate resources. - **type="MEMORY"** - The memory hard limit (in MiB) present to the container. This parameter is supported for jobs that are running on EC2 resources. If your container attempts to exceed the memory specified, the container is terminated. This parameter maps to ``Memory`` in the `Create a container <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/#create-a-container>`_ section of the `Docker Remote API <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/>`_ and the ``--memory`` option to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ . You must specify at least 4 MiB of memory for a job. This is required but can be specified in several places for multi-node parallel (MNP) jobs. It must be specified for each node at least once. This parameter maps to ``Memory`` in the `Create a container <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/#create-a-container>`_ section of the `Docker Remote API <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/>`_ and the ``--memory`` option to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ . .. epigraph:: If you're trying to maximize your resource utilization by providing your jobs as much memory as possible for a particular instance type, see `Memory management <https://docs.aws.amazon.com/batch/latest/userguide/memory-management.html>`_ in the *AWS Batch User Guide* . For jobs that are running on Fargate resources, then ``value`` is the hard limit (in MiB), and must match one of the supported values and the ``VCPU`` values must be one of the values supported for that memory value. - **value = 512** - ``VCPU`` = 0.25 - **value = 1024** - ``VCPU`` = 0.25 or 0.5 - **value = 2048** - ``VCPU`` = 0.25, 0.5, or 1 - **value = 3072** - ``VCPU`` = 0.5, or 1 - **value = 4096** - ``VCPU`` = 0.5, 1, or 2 - **value = 5120, 6144, or 7168** - ``VCPU`` = 1 or 2 - **value = 8192** - ``VCPU`` = 1, 2, 4, or 8 - **value = 9216, 10240, 11264, 12288, 13312, 14336, or 15360** - ``VCPU`` = 2 or 4 - **value = 16384** - ``VCPU`` = 2, 4, or 8 - **value = 17408, 18432, 19456, 21504, 22528, 23552, 25600, 26624, 27648, 29696, or 30720** - ``VCPU`` = 4 - **value = 20480, 24576, or 28672** - ``VCPU`` = 4 or 8 - **value = 36864, 45056, 53248, or 61440** - ``VCPU`` = 8 - **value = 32768, 40960, 49152, or 57344** - ``VCPU`` = 8 or 16 - **value = 65536, 73728, 81920, 90112, 98304, 106496, 114688, or 122880** - ``VCPU`` = 16 - **type="VCPU"** - The number of vCPUs reserved for the container. This parameter maps to ``CpuShares`` in the `Create a container <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/#create-a-container>`_ section of the `Docker Remote API <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/>`_ and the ``--cpu-shares`` option to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ . Each vCPU is equivalent to 1,024 CPU shares. For EC2 resources, you must specify at least one vCPU. This is required but can be specified in several places; it must be specified for each node at least once. The default for the Fargate On-Demand vCPU resource count quota is 6 vCPUs. For more information about Fargate quotas, see `AWS Fargate quotas <https://docs.aws.amazon.com/general/latest/gr/ecs-service.html#service-quotas-fargate>`_ in the *AWS General Reference* . For jobs that are running on Fargate resources, then ``value`` must match one of the supported values and the ``MEMORY`` values must be one of the values supported for that ``VCPU`` value. The supported values are 0.25, 0.5, 1, 2, 4, 8, and 16 - **value = 0.25** - ``MEMORY`` = 512, 1024, or 2048 - **value = 0.5** - ``MEMORY`` = 1024, 2048, 3072, or 4096 - **value = 1** - ``MEMORY`` = 2048, 3072, 4096, 5120, 6144, 7168, or 8192 - **value = 2** - ``MEMORY`` = 4096, 5120, 6144, 7168, 8192, 9216, 10240, 11264, 12288, 13312, 14336, 15360, or 16384 - **value = 4** - ``MEMORY`` = 8192, 9216, 10240, 11264, 12288, 13312, 14336, 15360, 16384, 17408, 18432, 19456, 20480, 21504, 22528, 23552, 24576, 25600, 26624, 27648, 28672, 29696, or 30720 - **value = 8** - ``MEMORY`` = 16384, 20480, 24576, 28672, 32768, 36864, 40960, 45056, 49152, 53248, 57344, or 61440 - **value = 16** - ``MEMORY`` = 32768, 40960, 49152, 57344, 65536, 73728, 81920, 90112, 98304, 106496, 114688, or 122880

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-batchresourcerequirement.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pipes as pipes
                
                batch_resource_requirement_property = pipes.CfnPipe.BatchResourceRequirementProperty(
                    type="type",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ff7ddf004d2156fbb4d6695cf8b70ebe68fd7dbeaa600ae631bdfb7cc39c9f7c)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "type": type,
                "value": value,
            }

        @builtins.property
        def type(self) -> builtins.str:
            '''The type of resource to assign to a container.

            The supported resources include ``GPU`` , ``MEMORY`` , and ``VCPU`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-batchresourcerequirement.html#cfn-pipes-pipe-batchresourcerequirement-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''The quantity of the specified resource to reserve for the container. The values vary based on the ``type`` specified.

            - **type="GPU"** - The number of physical GPUs to reserve for the container. Make sure that the number of GPUs reserved for all containers in a job doesn't exceed the number of available GPUs on the compute resource that the job is launched on.

            .. epigraph::

               GPUs aren't available for jobs that are running on Fargate resources.

            - **type="MEMORY"** - The memory hard limit (in MiB) present to the container. This parameter is supported for jobs that are running on EC2 resources. If your container attempts to exceed the memory specified, the container is terminated. This parameter maps to ``Memory`` in the `Create a container <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/#create-a-container>`_ section of the `Docker Remote API <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/>`_ and the ``--memory`` option to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ . You must specify at least 4 MiB of memory for a job. This is required but can be specified in several places for multi-node parallel (MNP) jobs. It must be specified for each node at least once. This parameter maps to ``Memory`` in the `Create a container <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/#create-a-container>`_ section of the `Docker Remote API <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/>`_ and the ``--memory`` option to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ .

            .. epigraph::

               If you're trying to maximize your resource utilization by providing your jobs as much memory as possible for a particular instance type, see `Memory management <https://docs.aws.amazon.com/batch/latest/userguide/memory-management.html>`_ in the *AWS Batch User Guide* .

            For jobs that are running on Fargate resources, then ``value`` is the hard limit (in MiB), and must match one of the supported values and the ``VCPU`` values must be one of the values supported for that memory value.

            - **value = 512** - ``VCPU`` = 0.25
            - **value = 1024** - ``VCPU`` = 0.25 or 0.5
            - **value = 2048** - ``VCPU`` = 0.25, 0.5, or 1
            - **value = 3072** - ``VCPU`` = 0.5, or 1
            - **value = 4096** - ``VCPU`` = 0.5, 1, or 2
            - **value = 5120, 6144, or 7168** - ``VCPU`` = 1 or 2
            - **value = 8192** - ``VCPU`` = 1, 2, 4, or 8
            - **value = 9216, 10240, 11264, 12288, 13312, 14336, or 15360** - ``VCPU`` = 2 or 4
            - **value = 16384** - ``VCPU`` = 2, 4, or 8
            - **value = 17408, 18432, 19456, 21504, 22528, 23552, 25600, 26624, 27648, 29696, or 30720** - ``VCPU`` = 4
            - **value = 20480, 24576, or 28672** - ``VCPU`` = 4 or 8
            - **value = 36864, 45056, 53248, or 61440** - ``VCPU`` = 8
            - **value = 32768, 40960, 49152, or 57344** - ``VCPU`` = 8 or 16
            - **value = 65536, 73728, 81920, 90112, 98304, 106496, 114688, or 122880** - ``VCPU`` = 16
            - **type="VCPU"** - The number of vCPUs reserved for the container. This parameter maps to ``CpuShares`` in the `Create a container <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/#create-a-container>`_ section of the `Docker Remote API <https://docs.aws.amazon.com/https://docs.docker.com/engine/api/v1.23/>`_ and the ``--cpu-shares`` option to `docker run <https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/>`_ . Each vCPU is equivalent to 1,024 CPU shares. For EC2 resources, you must specify at least one vCPU. This is required but can be specified in several places; it must be specified for each node at least once.

            The default for the Fargate On-Demand vCPU resource count quota is 6 vCPUs. For more information about Fargate quotas, see `AWS Fargate quotas <https://docs.aws.amazon.com/general/latest/gr/ecs-service.html#service-quotas-fargate>`_ in the *AWS General Reference* .

            For jobs that are running on Fargate resources, then ``value`` must match one of the supported values and the ``MEMORY`` values must be one of the values supported for that ``VCPU`` value. The supported values are 0.25, 0.5, 1, 2, 4, 8, and 16

            - **value = 0.25** - ``MEMORY`` = 512, 1024, or 2048
            - **value = 0.5** - ``MEMORY`` = 1024, 2048, 3072, or 4096
            - **value = 1** - ``MEMORY`` = 2048, 3072, 4096, 5120, 6144, 7168, or 8192
            - **value = 2** - ``MEMORY`` = 4096, 5120, 6144, 7168, 8192, 9216, 10240, 11264, 12288, 13312, 14336, 15360, or 16384
            - **value = 4** - ``MEMORY`` = 8192, 9216, 10240, 11264, 12288, 13312, 14336, 15360, 16384, 17408, 18432, 19456, 20480, 21504, 22528, 23552, 24576, 25600, 26624, 27648, 28672, 29696, or 30720
            - **value = 8** - ``MEMORY`` = 16384, 20480, 24576, 28672, 32768, 36864, 40960, 45056, 49152, 53248, 57344, or 61440
            - **value = 16** - ``MEMORY`` = 32768, 40960, 49152, 57344, 65536, 73728, 81920, 90112, 98304, 106496, 114688, or 122880

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-batchresourcerequirement.html#cfn-pipes-pipe-batchresourcerequirement-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BatchResourceRequirementProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pipes.CfnPipe.BatchRetryStrategyProperty",
        jsii_struct_bases=[],
        name_mapping={"attempts": "attempts"},
    )
    class BatchRetryStrategyProperty:
        def __init__(self, *, attempts: typing.Optional[jsii.Number] = None) -> None:
            '''The retry strategy that's associated with a job.

            For more information, see `Automated job retries <https://docs.aws.amazon.com/batch/latest/userguide/job_retries.html>`_ in the *AWS Batch User Guide* .

            :param attempts: The number of times to move a job to the ``RUNNABLE`` status. If the value of ``attempts`` is greater than one, the job is retried on failure the same number of attempts as the value. Default: - 0

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-batchretrystrategy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pipes as pipes
                
                batch_retry_strategy_property = pipes.CfnPipe.BatchRetryStrategyProperty(
                    attempts=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6d623eb197750cfc3e70926318810b6905af52604196157974285f7aa990f4bd)
                check_type(argname="argument attempts", value=attempts, expected_type=type_hints["attempts"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if attempts is not None:
                self._values["attempts"] = attempts

        @builtins.property
        def attempts(self) -> typing.Optional[jsii.Number]:
            '''The number of times to move a job to the ``RUNNABLE`` status.

            If the value of ``attempts`` is greater than one, the job is retried on failure the same number of attempts as the value.

            :default: - 0

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-batchretrystrategy.html#cfn-pipes-pipe-batchretrystrategy-attempts
            '''
            result = self._values.get("attempts")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BatchRetryStrategyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pipes.CfnPipe.CapacityProviderStrategyItemProperty",
        jsii_struct_bases=[],
        name_mapping={
            "capacity_provider": "capacityProvider",
            "base": "base",
            "weight": "weight",
        },
    )
    class CapacityProviderStrategyItemProperty:
        def __init__(
            self,
            *,
            capacity_provider: builtins.str,
            base: typing.Optional[jsii.Number] = None,
            weight: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''The details of a capacity provider strategy.

            To learn more, see `CapacityProviderStrategyItem <https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CapacityProviderStrategyItem.html>`_ in the Amazon ECS API Reference.

            :param capacity_provider: The short name of the capacity provider.
            :param base: The base value designates how many tasks, at a minimum, to run on the specified capacity provider. Only one capacity provider in a capacity provider strategy can have a base defined. If no value is specified, the default value of 0 is used. Default: - 0
            :param weight: The weight value designates the relative percentage of the total number of tasks launched that should use the specified capacity provider. The weight value is taken into consideration after the base value, if defined, is satisfied. Default: - 0

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-capacityproviderstrategyitem.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pipes as pipes
                
                capacity_provider_strategy_item_property = pipes.CfnPipe.CapacityProviderStrategyItemProperty(
                    capacity_provider="capacityProvider",
                
                    # the properties below are optional
                    base=123,
                    weight=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7a0a6c552a3434ea82161f20199d02513f09432e81ead4005d7f813754024e4b)
                check_type(argname="argument capacity_provider", value=capacity_provider, expected_type=type_hints["capacity_provider"])
                check_type(argname="argument base", value=base, expected_type=type_hints["base"])
                check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "capacity_provider": capacity_provider,
            }
            if base is not None:
                self._values["base"] = base
            if weight is not None:
                self._values["weight"] = weight

        @builtins.property
        def capacity_provider(self) -> builtins.str:
            '''The short name of the capacity provider.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-capacityproviderstrategyitem.html#cfn-pipes-pipe-capacityproviderstrategyitem-capacityprovider
            '''
            result = self._values.get("capacity_provider")
            assert result is not None, "Required property 'capacity_provider' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def base(self) -> typing.Optional[jsii.Number]:
            '''The base value designates how many tasks, at a minimum, to run on the specified capacity provider.

            Only one capacity provider in a capacity provider strategy can have a base defined. If no value is specified, the default value of 0 is used.

            :default: - 0

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-capacityproviderstrategyitem.html#cfn-pipes-pipe-capacityproviderstrategyitem-base
            '''
            result = self._values.get("base")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def weight(self) -> typing.Optional[jsii.Number]:
            '''The weight value designates the relative percentage of the total number of tasks launched that should use the specified capacity provider.

            The weight value is taken into consideration after the base value, if defined, is satisfied.

            :default: - 0

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-capacityproviderstrategyitem.html#cfn-pipes-pipe-capacityproviderstrategyitem-weight
            '''
            result = self._values.get("weight")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CapacityProviderStrategyItemProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pipes.CfnPipe.CloudwatchLogsLogDestinationProperty",
        jsii_struct_bases=[],
        name_mapping={"log_group_arn": "logGroupArn"},
    )
    class CloudwatchLogsLogDestinationProperty:
        def __init__(
            self,
            *,
            log_group_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Represents the Amazon CloudWatch Logs logging configuration settings for the pipe.

            :param log_group_arn: The AWS Resource Name (ARN) for the CloudWatch log group to which EventBridge sends the log records.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-cloudwatchlogslogdestination.html
            :exampleMetadata: infused

            Example::

                # source_queue: sqs.Queue
                # target_queue: sqs.Queue
                
                
                source_filter = pipes.Filter([
                    pipes.FilterPattern.from_object({
                        "body": {
                            # only forward events with customerType B2B or B2C
                            "customer_type": ["B2B", "B2C"]
                        }
                    })
                ])
                
                pipe = pipes.Pipe(self, "Pipe",
                    source=SqsSource(source_queue),
                    target=SqsTarget(target_queue),
                    filter=source_filter
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e7fcaf667064eeae949a2b411c39d860bfd847c21fbdaaffccb0267266f85864)
                check_type(argname="argument log_group_arn", value=log_group_arn, expected_type=type_hints["log_group_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if log_group_arn is not None:
                self._values["log_group_arn"] = log_group_arn

        @builtins.property
        def log_group_arn(self) -> typing.Optional[builtins.str]:
            '''The AWS Resource Name (ARN) for the CloudWatch log group to which EventBridge sends the log records.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-cloudwatchlogslogdestination.html#cfn-pipes-pipe-cloudwatchlogslogdestination-loggrouparn
            '''
            result = self._values.get("log_group_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CloudwatchLogsLogDestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pipes.CfnPipe.DeadLetterConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"arn": "arn"},
    )
    class DeadLetterConfigProperty:
        def __init__(self, *, arn: typing.Optional[builtins.str] = None) -> None:
            '''A ``DeadLetterConfig`` object that contains information about a dead-letter queue configuration.

            :param arn: The ARN of the specified target for the dead-letter queue. For Amazon Kinesis stream and Amazon DynamoDB stream sources, specify either an Amazon SNS topic or Amazon SQS queue ARN.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-deadletterconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pipes as pipes
                
                dead_letter_config_property = pipes.CfnPipe.DeadLetterConfigProperty(
                    arn="arn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c77be0d58acf260e66916991ed848b46a2c0c50751145a9186710668a20838df)
                check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if arn is not None:
                self._values["arn"] = arn

        @builtins.property
        def arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the specified target for the dead-letter queue.

            For Amazon Kinesis stream and Amazon DynamoDB stream sources, specify either an Amazon SNS topic or Amazon SQS queue ARN.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-deadletterconfig.html#cfn-pipes-pipe-deadletterconfig-arn
            '''
            result = self._values.get("arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DeadLetterConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pipes.CfnPipe.EcsContainerOverrideProperty",
        jsii_struct_bases=[],
        name_mapping={
            "command": "command",
            "cpu": "cpu",
            "environment": "environment",
            "environment_files": "environmentFiles",
            "memory": "memory",
            "memory_reservation": "memoryReservation",
            "name": "name",
            "resource_requirements": "resourceRequirements",
        },
    )
    class EcsContainerOverrideProperty:
        def __init__(
            self,
            *,
            command: typing.Optional[typing.Sequence[builtins.str]] = None,
            cpu: typing.Optional[jsii.Number] = None,
            environment: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPipe.EcsEnvironmentVariableProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            environment_files: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPipe.EcsEnvironmentFileProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            memory: typing.Optional[jsii.Number] = None,
            memory_reservation: typing.Optional[jsii.Number] = None,
            name: typing.Optional[builtins.str] = None,
            resource_requirements: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPipe.EcsResourceRequirementProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''The overrides that are sent to a container.

            An empty container override can be passed in. An example of an empty container override is ``{"containerOverrides": [ ] }`` . If a non-empty container override is specified, the ``name`` parameter must be included.

            :param command: The command to send to the container that overrides the default command from the Docker image or the task definition. You must also specify a container name.
            :param cpu: The number of ``cpu`` units reserved for the container, instead of the default value from the task definition. You must also specify a container name.
            :param environment: The environment variables to send to the container. You can add new environment variables, which are added to the container at launch, or you can override the existing environment variables from the Docker image or the task definition. You must also specify a container name.
            :param environment_files: A list of files containing the environment variables to pass to a container, instead of the value from the container definition.
            :param memory: The hard limit (in MiB) of memory to present to the container, instead of the default value from the task definition. If your container attempts to exceed the memory specified here, the container is killed. You must also specify a container name.
            :param memory_reservation: The soft limit (in MiB) of memory to reserve for the container, instead of the default value from the task definition. You must also specify a container name.
            :param name: The name of the container that receives the override. This parameter is required if any override is specified.
            :param resource_requirements: The type and amount of a resource to assign to a container, instead of the default value from the task definition. The only supported resource is a GPU.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-ecscontaineroverride.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pipes as pipes
                
                ecs_container_override_property = pipes.CfnPipe.EcsContainerOverrideProperty(
                    command=["command"],
                    cpu=123,
                    environment=[pipes.CfnPipe.EcsEnvironmentVariableProperty(
                        name="name",
                        value="value"
                    )],
                    environment_files=[pipes.CfnPipe.EcsEnvironmentFileProperty(
                        type="type",
                        value="value"
                    )],
                    memory=123,
                    memory_reservation=123,
                    name="name",
                    resource_requirements=[pipes.CfnPipe.EcsResourceRequirementProperty(
                        type="type",
                        value="value"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2aa9c9e99af21330a73d690bfbb31c0ded547e5a62886d6682815f5910e00e65)
                check_type(argname="argument command", value=command, expected_type=type_hints["command"])
                check_type(argname="argument cpu", value=cpu, expected_type=type_hints["cpu"])
                check_type(argname="argument environment", value=environment, expected_type=type_hints["environment"])
                check_type(argname="argument environment_files", value=environment_files, expected_type=type_hints["environment_files"])
                check_type(argname="argument memory", value=memory, expected_type=type_hints["memory"])
                check_type(argname="argument memory_reservation", value=memory_reservation, expected_type=type_hints["memory_reservation"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument resource_requirements", value=resource_requirements, expected_type=type_hints["resource_requirements"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if command is not None:
                self._values["command"] = command
            if cpu is not None:
                self._values["cpu"] = cpu
            if environment is not None:
                self._values["environment"] = environment
            if environment_files is not None:
                self._values["environment_files"] = environment_files
            if memory is not None:
                self._values["memory"] = memory
            if memory_reservation is not None:
                self._values["memory_reservation"] = memory_reservation
            if name is not None:
                self._values["name"] = name
            if resource_requirements is not None:
                self._values["resource_requirements"] = resource_requirements

        @builtins.property
        def command(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The command to send to the container that overrides the default command from the Docker image or the task definition.

            You must also specify a container name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-ecscontaineroverride.html#cfn-pipes-pipe-ecscontaineroverride-command
            '''
            result = self._values.get("command")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def cpu(self) -> typing.Optional[jsii.Number]:
            '''The number of ``cpu`` units reserved for the container, instead of the default value from the task definition.

            You must also specify a container name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-ecscontaineroverride.html#cfn-pipes-pipe-ecscontaineroverride-cpu
            '''
            result = self._values.get("cpu")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def environment(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPipe.EcsEnvironmentVariableProperty"]]]]:
            '''The environment variables to send to the container.

            You can add new environment variables, which are added to the container at launch, or you can override the existing environment variables from the Docker image or the task definition. You must also specify a container name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-ecscontaineroverride.html#cfn-pipes-pipe-ecscontaineroverride-environment
            '''
            result = self._values.get("environment")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPipe.EcsEnvironmentVariableProperty"]]]], result)

        @builtins.property
        def environment_files(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPipe.EcsEnvironmentFileProperty"]]]]:
            '''A list of files containing the environment variables to pass to a container, instead of the value from the container definition.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-ecscontaineroverride.html#cfn-pipes-pipe-ecscontaineroverride-environmentfiles
            '''
            result = self._values.get("environment_files")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPipe.EcsEnvironmentFileProperty"]]]], result)

        @builtins.property
        def memory(self) -> typing.Optional[jsii.Number]:
            '''The hard limit (in MiB) of memory to present to the container, instead of the default value from the task definition.

            If your container attempts to exceed the memory specified here, the container is killed. You must also specify a container name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-ecscontaineroverride.html#cfn-pipes-pipe-ecscontaineroverride-memory
            '''
            result = self._values.get("memory")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def memory_reservation(self) -> typing.Optional[jsii.Number]:
            '''The soft limit (in MiB) of memory to reserve for the container, instead of the default value from the task definition.

            You must also specify a container name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-ecscontaineroverride.html#cfn-pipes-pipe-ecscontaineroverride-memoryreservation
            '''
            result = self._values.get("memory_reservation")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the container that receives the override.

            This parameter is required if any override is specified.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-ecscontaineroverride.html#cfn-pipes-pipe-ecscontaineroverride-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def resource_requirements(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPipe.EcsResourceRequirementProperty"]]]]:
            '''The type and amount of a resource to assign to a container, instead of the default value from the task definition.

            The only supported resource is a GPU.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-ecscontaineroverride.html#cfn-pipes-pipe-ecscontaineroverride-resourcerequirements
            '''
            result = self._values.get("resource_requirements")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPipe.EcsResourceRequirementProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EcsContainerOverrideProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pipes.CfnPipe.EcsEnvironmentFileProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type", "value": "value"},
    )
    class EcsEnvironmentFileProperty:
        def __init__(self, *, type: builtins.str, value: builtins.str) -> None:
            '''A list of files containing the environment variables to pass to a container.

            You can specify up to ten environment files. The file must have a ``.env`` file extension. Each line in an environment file should contain an environment variable in ``VARIABLE=VALUE`` format. Lines beginning with ``#`` are treated as comments and are ignored. For more information about the environment variable file syntax, see `Declare default environment variables in file <https://docs.aws.amazon.com/https://docs.docker.com/compose/env-file/>`_ .

            If there are environment variables specified using the ``environment`` parameter in a container definition, they take precedence over the variables contained within an environment file. If multiple environment files are specified that contain the same variable, they're processed from the top down. We recommend that you use unique variable names. For more information, see `Specifying environment variables <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/taskdef-envfiles.html>`_ in the *Amazon Elastic Container Service Developer Guide* .

            This parameter is only supported for tasks hosted on Fargate using the following platform versions:

            - Linux platform version ``1.4.0`` or later.
            - Windows platform version ``1.0.0`` or later.

            :param type: The file type to use. The only supported value is ``s3`` .
            :param value: The Amazon Resource Name (ARN) of the Amazon S3 object containing the environment variable file.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-ecsenvironmentfile.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pipes as pipes
                
                ecs_environment_file_property = pipes.CfnPipe.EcsEnvironmentFileProperty(
                    type="type",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__01bada1fe04905f47a26a5965d040f55b22a98d3ef168a973e3a38a0c3937836)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "type": type,
                "value": value,
            }

        @builtins.property
        def type(self) -> builtins.str:
            '''The file type to use.

            The only supported value is ``s3`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-ecsenvironmentfile.html#cfn-pipes-pipe-ecsenvironmentfile-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the Amazon S3 object containing the environment variable file.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-ecsenvironmentfile.html#cfn-pipes-pipe-ecsenvironmentfile-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EcsEnvironmentFileProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pipes.CfnPipe.EcsEnvironmentVariableProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "value": "value"},
    )
    class EcsEnvironmentVariableProperty:
        def __init__(
            self,
            *,
            name: typing.Optional[builtins.str] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The environment variables to send to the container.

            You can add new environment variables, which are added to the container at launch, or you can override the existing environment variables from the Docker image or the task definition. You must also specify a container name.

            :param name: The name of the key-value pair. For environment variables, this is the name of the environment variable.
            :param value: The value of the key-value pair. For environment variables, this is the value of the environment variable.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-ecsenvironmentvariable.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pipes as pipes
                
                ecs_environment_variable_property = pipes.CfnPipe.EcsEnvironmentVariableProperty(
                    name="name",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5916c016388a7f5303579d1368d4dcbda171aeb41921023cbc0b22b49997fb59)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if name is not None:
                self._values["name"] = name
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the key-value pair.

            For environment variables, this is the name of the environment variable.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-ecsenvironmentvariable.html#cfn-pipes-pipe-ecsenvironmentvariable-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''The value of the key-value pair.

            For environment variables, this is the value of the environment variable.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-ecsenvironmentvariable.html#cfn-pipes-pipe-ecsenvironmentvariable-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EcsEnvironmentVariableProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pipes.CfnPipe.EcsEphemeralStorageProperty",
        jsii_struct_bases=[],
        name_mapping={"size_in_gib": "sizeInGiB"},
    )
    class EcsEphemeralStorageProperty:
        def __init__(self, *, size_in_gib: jsii.Number) -> None:
            '''The amount of ephemeral storage to allocate for the task.

            This parameter is used to expand the total amount of ephemeral storage available, beyond the default amount, for tasks hosted on Fargate. For more information, see `Fargate task storage <https://docs.aws.amazon.com/AmazonECS/latest/userguide/using_data_volumes.html>`_ in the *Amazon ECS User Guide for Fargate* .
            .. epigraph::

               This parameter is only supported for tasks hosted on Fargate using Linux platform version ``1.4.0`` or later. This parameter is not supported for Windows containers on Fargate.

            :param size_in_gib: The total amount, in GiB, of ephemeral storage to set for the task. The minimum supported value is ``21`` GiB and the maximum supported value is ``200`` GiB. Default: - 0

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-ecsephemeralstorage.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pipes as pipes
                
                ecs_ephemeral_storage_property = pipes.CfnPipe.EcsEphemeralStorageProperty(
                    size_in_gi_b=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__caa763e1eb6274b4829763db1a11d6c4d69679f0c1c56e86833c464b209d7d2b)
                check_type(argname="argument size_in_gib", value=size_in_gib, expected_type=type_hints["size_in_gib"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "size_in_gib": size_in_gib,
            }

        @builtins.property
        def size_in_gib(self) -> jsii.Number:
            '''The total amount, in GiB, of ephemeral storage to set for the task.

            The minimum supported value is ``21`` GiB and the maximum supported value is ``200`` GiB.

            :default: - 0

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-ecsephemeralstorage.html#cfn-pipes-pipe-ecsephemeralstorage-sizeingib
            '''
            result = self._values.get("size_in_gib")
            assert result is not None, "Required property 'size_in_gib' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EcsEphemeralStorageProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pipes.CfnPipe.EcsInferenceAcceleratorOverrideProperty",
        jsii_struct_bases=[],
        name_mapping={"device_name": "deviceName", "device_type": "deviceType"},
    )
    class EcsInferenceAcceleratorOverrideProperty:
        def __init__(
            self,
            *,
            device_name: typing.Optional[builtins.str] = None,
            device_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Details on an Elastic Inference accelerator task override.

            This parameter is used to override the Elastic Inference accelerator specified in the task definition. For more information, see `Working with Amazon Elastic Inference on Amazon ECS <https://docs.aws.amazon.com/AmazonECS/latest/userguide/ecs-inference.html>`_ in the *Amazon Elastic Container Service Developer Guide* .

            :param device_name: The Elastic Inference accelerator device name to override for the task. This parameter must match a ``deviceName`` specified in the task definition.
            :param device_type: The Elastic Inference accelerator type to use.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-ecsinferenceacceleratoroverride.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pipes as pipes
                
                ecs_inference_accelerator_override_property = pipes.CfnPipe.EcsInferenceAcceleratorOverrideProperty(
                    device_name="deviceName",
                    device_type="deviceType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9920d06ed2da3a222b25b6b174db7eb43e6983e29183224a1b0d86f3ae79a3fc)
                check_type(argname="argument device_name", value=device_name, expected_type=type_hints["device_name"])
                check_type(argname="argument device_type", value=device_type, expected_type=type_hints["device_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if device_name is not None:
                self._values["device_name"] = device_name
            if device_type is not None:
                self._values["device_type"] = device_type

        @builtins.property
        def device_name(self) -> typing.Optional[builtins.str]:
            '''The Elastic Inference accelerator device name to override for the task.

            This parameter must match a ``deviceName`` specified in the task definition.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-ecsinferenceacceleratoroverride.html#cfn-pipes-pipe-ecsinferenceacceleratoroverride-devicename
            '''
            result = self._values.get("device_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def device_type(self) -> typing.Optional[builtins.str]:
            '''The Elastic Inference accelerator type to use.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-ecsinferenceacceleratoroverride.html#cfn-pipes-pipe-ecsinferenceacceleratoroverride-devicetype
            '''
            result = self._values.get("device_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EcsInferenceAcceleratorOverrideProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pipes.CfnPipe.EcsResourceRequirementProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type", "value": "value"},
    )
    class EcsResourceRequirementProperty:
        def __init__(self, *, type: builtins.str, value: builtins.str) -> None:
            '''The type and amount of a resource to assign to a container.

            The supported resource types are GPUs and Elastic Inference accelerators. For more information, see `Working with GPUs on Amazon ECS <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-gpu.html>`_ or `Working with Amazon Elastic Inference on Amazon ECS <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-inference.html>`_ in the *Amazon Elastic Container Service Developer Guide*

            :param type: The type of resource to assign to a container. The supported values are ``GPU`` or ``InferenceAccelerator`` .
            :param value: The value for the specified resource type. If the ``GPU`` type is used, the value is the number of physical ``GPUs`` the Amazon ECS container agent reserves for the container. The number of GPUs that's reserved for all containers in a task can't exceed the number of available GPUs on the container instance that the task is launched on. If the ``InferenceAccelerator`` type is used, the ``value`` matches the ``deviceName`` for an InferenceAccelerator specified in a task definition.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-ecsresourcerequirement.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pipes as pipes
                
                ecs_resource_requirement_property = pipes.CfnPipe.EcsResourceRequirementProperty(
                    type="type",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0b2bd11ae2d133e2ae4a3b3bbf1130a6396a05fe6a948341ca3d1fbe22cfb752)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "type": type,
                "value": value,
            }

        @builtins.property
        def type(self) -> builtins.str:
            '''The type of resource to assign to a container.

            The supported values are ``GPU`` or ``InferenceAccelerator`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-ecsresourcerequirement.html#cfn-pipes-pipe-ecsresourcerequirement-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''The value for the specified resource type.

            If the ``GPU`` type is used, the value is the number of physical ``GPUs`` the Amazon ECS container agent reserves for the container. The number of GPUs that's reserved for all containers in a task can't exceed the number of available GPUs on the container instance that the task is launched on.

            If the ``InferenceAccelerator`` type is used, the ``value`` matches the ``deviceName`` for an InferenceAccelerator specified in a task definition.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-ecsresourcerequirement.html#cfn-pipes-pipe-ecsresourcerequirement-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EcsResourceRequirementProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pipes.CfnPipe.EcsTaskOverrideProperty",
        jsii_struct_bases=[],
        name_mapping={
            "container_overrides": "containerOverrides",
            "cpu": "cpu",
            "ephemeral_storage": "ephemeralStorage",
            "execution_role_arn": "executionRoleArn",
            "inference_accelerator_overrides": "inferenceAcceleratorOverrides",
            "memory": "memory",
            "task_role_arn": "taskRoleArn",
        },
    )
    class EcsTaskOverrideProperty:
        def __init__(
            self,
            *,
            container_overrides: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPipe.EcsContainerOverrideProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            cpu: typing.Optional[builtins.str] = None,
            ephemeral_storage: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPipe.EcsEphemeralStorageProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            execution_role_arn: typing.Optional[builtins.str] = None,
            inference_accelerator_overrides: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPipe.EcsInferenceAcceleratorOverrideProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            memory: typing.Optional[builtins.str] = None,
            task_role_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The overrides that are associated with a task.

            :param container_overrides: One or more container overrides that are sent to a task.
            :param cpu: The cpu override for the task.
            :param ephemeral_storage: The ephemeral storage setting override for the task. .. epigraph:: This parameter is only supported for tasks hosted on Fargate that use the following platform versions: - Linux platform version ``1.4.0`` or later. - Windows platform version ``1.0.0`` or later.
            :param execution_role_arn: The Amazon Resource Name (ARN) of the task execution IAM role override for the task. For more information, see `Amazon ECS task execution IAM role <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_execution_IAM_role.html>`_ in the *Amazon Elastic Container Service Developer Guide* .
            :param inference_accelerator_overrides: The Elastic Inference accelerator override for the task.
            :param memory: The memory override for the task.
            :param task_role_arn: The Amazon Resource Name (ARN) of the IAM role that containers in this task can assume. All containers in this task are granted the permissions that are specified in this role. For more information, see `IAM Role for Tasks <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html>`_ in the *Amazon Elastic Container Service Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-ecstaskoverride.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pipes as pipes
                
                ecs_task_override_property = pipes.CfnPipe.EcsTaskOverrideProperty(
                    container_overrides=[pipes.CfnPipe.EcsContainerOverrideProperty(
                        command=["command"],
                        cpu=123,
                        environment=[pipes.CfnPipe.EcsEnvironmentVariableProperty(
                            name="name",
                            value="value"
                        )],
                        environment_files=[pipes.CfnPipe.EcsEnvironmentFileProperty(
                            type="type",
                            value="value"
                        )],
                        memory=123,
                        memory_reservation=123,
                        name="name",
                        resource_requirements=[pipes.CfnPipe.EcsResourceRequirementProperty(
                            type="type",
                            value="value"
                        )]
                    )],
                    cpu="cpu",
                    ephemeral_storage=pipes.CfnPipe.EcsEphemeralStorageProperty(
                        size_in_gi_b=123
                    ),
                    execution_role_arn="executionRoleArn",
                    inference_accelerator_overrides=[pipes.CfnPipe.EcsInferenceAcceleratorOverrideProperty(
                        device_name="deviceName",
                        device_type="deviceType"
                    )],
                    memory="memory",
                    task_role_arn="taskRoleArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ac29bac5fb5186aee7c9d8a3a767986fee27a65cfa4b10cb45878a777a141ee5)
                check_type(argname="argument container_overrides", value=container_overrides, expected_type=type_hints["container_overrides"])
                check_type(argname="argument cpu", value=cpu, expected_type=type_hints["cpu"])
                check_type(argname="argument ephemeral_storage", value=ephemeral_storage, expected_type=type_hints["ephemeral_storage"])
                check_type(argname="argument execution_role_arn", value=execution_role_arn, expected_type=type_hints["execution_role_arn"])
                check_type(argname="argument inference_accelerator_overrides", value=inference_accelerator_overrides, expected_type=type_hints["inference_accelerator_overrides"])
                check_type(argname="argument memory", value=memory, expected_type=type_hints["memory"])
                check_type(argname="argument task_role_arn", value=task_role_arn, expected_type=type_hints["task_role_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if container_overrides is not None:
                self._values["container_overrides"] = container_overrides
            if cpu is not None:
                self._values["cpu"] = cpu
            if ephemeral_storage is not None:
                self._values["ephemeral_storage"] = ephemeral_storage
            if execution_role_arn is not None:
                self._values["execution_role_arn"] = execution_role_arn
            if inference_accelerator_overrides is not None:
                self._values["inference_accelerator_overrides"] = inference_accelerator_overrides
            if memory is not None:
                self._values["memory"] = memory
            if task_role_arn is not None:
                self._values["task_role_arn"] = task_role_arn

        @builtins.property
        def container_overrides(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPipe.EcsContainerOverrideProperty"]]]]:
            '''One or more container overrides that are sent to a task.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-ecstaskoverride.html#cfn-pipes-pipe-ecstaskoverride-containeroverrides
            '''
            result = self._values.get("container_overrides")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPipe.EcsContainerOverrideProperty"]]]], result)

        @builtins.property
        def cpu(self) -> typing.Optional[builtins.str]:
            '''The cpu override for the task.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-ecstaskoverride.html#cfn-pipes-pipe-ecstaskoverride-cpu
            '''
            result = self._values.get("cpu")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def ephemeral_storage(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.EcsEphemeralStorageProperty"]]:
            '''The ephemeral storage setting override for the task.

            .. epigraph::

               This parameter is only supported for tasks hosted on Fargate that use the following platform versions:

               - Linux platform version ``1.4.0`` or later.
               - Windows platform version ``1.0.0`` or later.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-ecstaskoverride.html#cfn-pipes-pipe-ecstaskoverride-ephemeralstorage
            '''
            result = self._values.get("ephemeral_storage")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.EcsEphemeralStorageProperty"]], result)

        @builtins.property
        def execution_role_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the task execution IAM role override for the task.

            For more information, see `Amazon ECS task execution IAM role <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_execution_IAM_role.html>`_ in the *Amazon Elastic Container Service Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-ecstaskoverride.html#cfn-pipes-pipe-ecstaskoverride-executionrolearn
            '''
            result = self._values.get("execution_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def inference_accelerator_overrides(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPipe.EcsInferenceAcceleratorOverrideProperty"]]]]:
            '''The Elastic Inference accelerator override for the task.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-ecstaskoverride.html#cfn-pipes-pipe-ecstaskoverride-inferenceacceleratoroverrides
            '''
            result = self._values.get("inference_accelerator_overrides")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPipe.EcsInferenceAcceleratorOverrideProperty"]]]], result)

        @builtins.property
        def memory(self) -> typing.Optional[builtins.str]:
            '''The memory override for the task.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-ecstaskoverride.html#cfn-pipes-pipe-ecstaskoverride-memory
            '''
            result = self._values.get("memory")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def task_role_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the IAM role that containers in this task can assume.

            All containers in this task are granted the permissions that are specified in this role. For more information, see `IAM Role for Tasks <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html>`_ in the *Amazon Elastic Container Service Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-ecstaskoverride.html#cfn-pipes-pipe-ecstaskoverride-taskrolearn
            '''
            result = self._values.get("task_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EcsTaskOverrideProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pipes.CfnPipe.FilterCriteriaProperty",
        jsii_struct_bases=[],
        name_mapping={"filters": "filters"},
    )
    class FilterCriteriaProperty:
        def __init__(
            self,
            *,
            filters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPipe.FilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''The collection of event patterns used to filter events.

            To remove a filter, specify a ``FilterCriteria`` object with an empty array of ``Filter`` objects.

            For more information, see `Events and Event Patterns <https://docs.aws.amazon.com/eventbridge/latest/userguide/eventbridge-and-event-patterns.html>`_ in the *Amazon EventBridge User Guide* .

            :param filters: The event patterns.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-filtercriteria.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pipes as pipes
                
                filter_criteria_property = pipes.CfnPipe.FilterCriteriaProperty(
                    filters=[pipes.CfnPipe.FilterProperty(
                        pattern="pattern"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__004b9f76dd8a2c227817a517c0d05d104afc0af72ef6cb0c3c89fbc4b6c922a5)
                check_type(argname="argument filters", value=filters, expected_type=type_hints["filters"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if filters is not None:
                self._values["filters"] = filters

        @builtins.property
        def filters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPipe.FilterProperty"]]]]:
            '''The event patterns.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-filtercriteria.html#cfn-pipes-pipe-filtercriteria-filters
            '''
            result = self._values.get("filters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPipe.FilterProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FilterCriteriaProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pipes.CfnPipe.FilterProperty",
        jsii_struct_bases=[],
        name_mapping={"pattern": "pattern"},
    )
    class FilterProperty:
        def __init__(self, *, pattern: typing.Optional[builtins.str] = None) -> None:
            '''Filter events using an event pattern.

            For more information, see `Events and Event Patterns <https://docs.aws.amazon.com/eventbridge/latest/userguide/eventbridge-and-event-patterns.html>`_ in the *Amazon EventBridge User Guide* .

            :param pattern: The event pattern.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-filter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pipes as pipes
                
                filter_property = pipes.CfnPipe.FilterProperty(
                    pattern="pattern"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9f00591753ff21d2f36f1936733014c6b5ee6e0461229e20051346fba671bc2b)
                check_type(argname="argument pattern", value=pattern, expected_type=type_hints["pattern"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if pattern is not None:
                self._values["pattern"] = pattern

        @builtins.property
        def pattern(self) -> typing.Optional[builtins.str]:
            '''The event pattern.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-filter.html#cfn-pipes-pipe-filter-pattern
            '''
            result = self._values.get("pattern")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pipes.CfnPipe.FirehoseLogDestinationProperty",
        jsii_struct_bases=[],
        name_mapping={"delivery_stream_arn": "deliveryStreamArn"},
    )
    class FirehoseLogDestinationProperty:
        def __init__(
            self,
            *,
            delivery_stream_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Represents the Amazon Data Firehose logging configuration settings for the pipe.

            :param delivery_stream_arn: The Amazon Resource Name (ARN) of the Firehose delivery stream to which EventBridge delivers the pipe log records.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-firehoselogdestination.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pipes as pipes
                
                firehose_log_destination_property = pipes.CfnPipe.FirehoseLogDestinationProperty(
                    delivery_stream_arn="deliveryStreamArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__debe1fd10d907031fe99a3f76db2e5a127e103de0cfb29f11bf57a42822b27b1)
                check_type(argname="argument delivery_stream_arn", value=delivery_stream_arn, expected_type=type_hints["delivery_stream_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if delivery_stream_arn is not None:
                self._values["delivery_stream_arn"] = delivery_stream_arn

        @builtins.property
        def delivery_stream_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the Firehose delivery stream to which EventBridge delivers the pipe log records.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-firehoselogdestination.html#cfn-pipes-pipe-firehoselogdestination-deliverystreamarn
            '''
            result = self._values.get("delivery_stream_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FirehoseLogDestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pipes.CfnPipe.MQBrokerAccessCredentialsProperty",
        jsii_struct_bases=[],
        name_mapping={"basic_auth": "basicAuth"},
    )
    class MQBrokerAccessCredentialsProperty:
        def __init__(self, *, basic_auth: builtins.str) -> None:
            '''The AWS Secrets Manager secret that stores your broker credentials.

            :param basic_auth: The ARN of the Secrets Manager secret.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-mqbrokeraccesscredentials.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pipes as pipes
                
                m_qBroker_access_credentials_property = pipes.CfnPipe.MQBrokerAccessCredentialsProperty(
                    basic_auth="basicAuth"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1cb1a557465a40a3893ac95a9d03f8e5ebb12253739b129caf5e762c94e574c8)
                check_type(argname="argument basic_auth", value=basic_auth, expected_type=type_hints["basic_auth"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "basic_auth": basic_auth,
            }

        @builtins.property
        def basic_auth(self) -> builtins.str:
            '''The ARN of the Secrets Manager secret.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-mqbrokeraccesscredentials.html#cfn-pipes-pipe-mqbrokeraccesscredentials-basicauth
            '''
            result = self._values.get("basic_auth")
            assert result is not None, "Required property 'basic_auth' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MQBrokerAccessCredentialsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pipes.CfnPipe.MSKAccessCredentialsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "client_certificate_tls_auth": "clientCertificateTlsAuth",
            "sasl_scram512_auth": "saslScram512Auth",
        },
    )
    class MSKAccessCredentialsProperty:
        def __init__(
            self,
            *,
            client_certificate_tls_auth: typing.Optional[builtins.str] = None,
            sasl_scram512_auth: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The AWS Secrets Manager secret that stores your stream credentials.

            :param client_certificate_tls_auth: The ARN of the Secrets Manager secret.
            :param sasl_scram512_auth: The ARN of the Secrets Manager secret.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-mskaccesscredentials.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pipes as pipes
                
                m_sKAccess_credentials_property = pipes.CfnPipe.MSKAccessCredentialsProperty(
                    client_certificate_tls_auth="clientCertificateTlsAuth",
                    sasl_scram512_auth="saslScram512Auth"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__46261e68c3c1fb4bc41f7b2debe372659b86c5d9845e6857c0ad7b9046c0c987)
                check_type(argname="argument client_certificate_tls_auth", value=client_certificate_tls_auth, expected_type=type_hints["client_certificate_tls_auth"])
                check_type(argname="argument sasl_scram512_auth", value=sasl_scram512_auth, expected_type=type_hints["sasl_scram512_auth"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if client_certificate_tls_auth is not None:
                self._values["client_certificate_tls_auth"] = client_certificate_tls_auth
            if sasl_scram512_auth is not None:
                self._values["sasl_scram512_auth"] = sasl_scram512_auth

        @builtins.property
        def client_certificate_tls_auth(self) -> typing.Optional[builtins.str]:
            '''The ARN of the Secrets Manager secret.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-mskaccesscredentials.html#cfn-pipes-pipe-mskaccesscredentials-clientcertificatetlsauth
            '''
            result = self._values.get("client_certificate_tls_auth")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def sasl_scram512_auth(self) -> typing.Optional[builtins.str]:
            '''The ARN of the Secrets Manager secret.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-mskaccesscredentials.html#cfn-pipes-pipe-mskaccesscredentials-saslscram512auth
            '''
            result = self._values.get("sasl_scram512_auth")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MSKAccessCredentialsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pipes.CfnPipe.NetworkConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"awsvpc_configuration": "awsvpcConfiguration"},
    )
    class NetworkConfigurationProperty:
        def __init__(
            self,
            *,
            awsvpc_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPipe.AwsVpcConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''This structure specifies the network configuration for an Amazon ECS task.

            :param awsvpc_configuration: Use this structure to specify the VPC subnets and security groups for the task, and whether a public IP address is to be used. This structure is relevant only for ECS tasks that use the ``awsvpc`` network mode.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-networkconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pipes as pipes
                
                network_configuration_property = pipes.CfnPipe.NetworkConfigurationProperty(
                    awsvpc_configuration=pipes.CfnPipe.AwsVpcConfigurationProperty(
                        subnets=["subnets"],
                
                        # the properties below are optional
                        assign_public_ip="assignPublicIp",
                        security_groups=["securityGroups"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d27b7177804b8a4677a880ec362095763e2c62871f3c70d4aadd38189dedd0ac)
                check_type(argname="argument awsvpc_configuration", value=awsvpc_configuration, expected_type=type_hints["awsvpc_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if awsvpc_configuration is not None:
                self._values["awsvpc_configuration"] = awsvpc_configuration

        @builtins.property
        def awsvpc_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.AwsVpcConfigurationProperty"]]:
            '''Use this structure to specify the VPC subnets and security groups for the task, and whether a public IP address is to be used.

            This structure is relevant only for ECS tasks that use the ``awsvpc`` network mode.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-networkconfiguration.html#cfn-pipes-pipe-networkconfiguration-awsvpcconfiguration
            '''
            result = self._values.get("awsvpc_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.AwsVpcConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NetworkConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pipes.CfnPipe.PipeEnrichmentHttpParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "header_parameters": "headerParameters",
            "path_parameter_values": "pathParameterValues",
            "query_string_parameters": "queryStringParameters",
        },
    )
    class PipeEnrichmentHttpParametersProperty:
        def __init__(
            self,
            *,
            header_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
            path_parameter_values: typing.Optional[typing.Sequence[builtins.str]] = None,
            query_string_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
        ) -> None:
            '''These are custom parameter to be used when the target is an API Gateway REST APIs or EventBridge ApiDestinations.

            In the latter case, these are merged with any InvocationParameters specified on the Connection, with any values from the Connection taking precedence.

            :param header_parameters: The headers that need to be sent as part of request invoking the API Gateway REST API or EventBridge ApiDestination.
            :param path_parameter_values: The path parameter values to be used to populate API Gateway REST API or EventBridge ApiDestination path wildcards ("*").
            :param query_string_parameters: The query string keys/values that need to be sent as part of request invoking the API Gateway REST API or EventBridge ApiDestination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipeenrichmenthttpparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pipes as pipes
                
                pipe_enrichment_http_parameters_property = pipes.CfnPipe.PipeEnrichmentHttpParametersProperty(
                    header_parameters={
                        "header_parameters_key": "headerParameters"
                    },
                    path_parameter_values=["pathParameterValues"],
                    query_string_parameters={
                        "query_string_parameters_key": "queryStringParameters"
                    }
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1c0ef57785475dd0f00d9483a37fb4e2993490bc25effa27f975d3eb152d45a0)
                check_type(argname="argument header_parameters", value=header_parameters, expected_type=type_hints["header_parameters"])
                check_type(argname="argument path_parameter_values", value=path_parameter_values, expected_type=type_hints["path_parameter_values"])
                check_type(argname="argument query_string_parameters", value=query_string_parameters, expected_type=type_hints["query_string_parameters"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if header_parameters is not None:
                self._values["header_parameters"] = header_parameters
            if path_parameter_values is not None:
                self._values["path_parameter_values"] = path_parameter_values
            if query_string_parameters is not None:
                self._values["query_string_parameters"] = query_string_parameters

        @builtins.property
        def header_parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
            '''The headers that need to be sent as part of request invoking the API Gateway REST API or EventBridge ApiDestination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipeenrichmenthttpparameters.html#cfn-pipes-pipe-pipeenrichmenthttpparameters-headerparameters
            '''
            result = self._values.get("header_parameters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], result)

        @builtins.property
        def path_parameter_values(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The path parameter values to be used to populate API Gateway REST API or EventBridge ApiDestination path wildcards ("*").

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipeenrichmenthttpparameters.html#cfn-pipes-pipe-pipeenrichmenthttpparameters-pathparametervalues
            '''
            result = self._values.get("path_parameter_values")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def query_string_parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
            '''The query string keys/values that need to be sent as part of request invoking the API Gateway REST API or EventBridge ApiDestination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipeenrichmenthttpparameters.html#cfn-pipes-pipe-pipeenrichmenthttpparameters-querystringparameters
            '''
            result = self._values.get("query_string_parameters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PipeEnrichmentHttpParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pipes.CfnPipe.PipeEnrichmentParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "http_parameters": "httpParameters",
            "input_template": "inputTemplate",
        },
    )
    class PipeEnrichmentParametersProperty:
        def __init__(
            self,
            *,
            http_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPipe.PipeEnrichmentHttpParametersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            input_template: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The parameters required to set up enrichment on your pipe.

            :param http_parameters: Contains the HTTP parameters to use when the target is a API Gateway REST endpoint or EventBridge ApiDestination. If you specify an API Gateway REST API or EventBridge ApiDestination as a target, you can use this parameter to specify headers, path parameters, and query string keys/values as part of your target invoking request. If you're using ApiDestinations, the corresponding Connection can also have these values configured. In case of any conflicting keys, values from the Connection take precedence.
            :param input_template: Valid JSON text passed to the enrichment. In this case, nothing from the event itself is passed to the enrichment. For more information, see `The JavaScript Object Notation (JSON) Data Interchange Format <https://docs.aws.amazon.com/http://www.rfc-editor.org/rfc/rfc7159.txt>`_ . To remove an input template, specify an empty string.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipeenrichmentparameters.html
            :exampleMetadata: infused

            Example::

                # source_queue: sqs.Queue
                # target_queue: sqs.Queue
                # loggroup: logs.LogGroup
                
                
                pipe = pipes.Pipe(self, "Pipe",
                    source=SqsSource(source_queue),
                    target=SqsTarget(target_queue),
                
                    log_level=pipes.LogLevel.TRACE,
                    log_include_execution_data=[pipes.IncludeExecutionData.ALL],
                
                    log_destinations=[
                        CloudwatchDestination(loggroup)
                    ]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0c41c854101e445a9a64950cf1ae31f47633329bb0e1d2188fc8a4013b114b09)
                check_type(argname="argument http_parameters", value=http_parameters, expected_type=type_hints["http_parameters"])
                check_type(argname="argument input_template", value=input_template, expected_type=type_hints["input_template"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if http_parameters is not None:
                self._values["http_parameters"] = http_parameters
            if input_template is not None:
                self._values["input_template"] = input_template

        @builtins.property
        def http_parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.PipeEnrichmentHttpParametersProperty"]]:
            '''Contains the HTTP parameters to use when the target is a API Gateway REST endpoint or EventBridge ApiDestination.

            If you specify an API Gateway REST API or EventBridge ApiDestination as a target, you can use this parameter to specify headers, path parameters, and query string keys/values as part of your target invoking request. If you're using ApiDestinations, the corresponding Connection can also have these values configured. In case of any conflicting keys, values from the Connection take precedence.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipeenrichmentparameters.html#cfn-pipes-pipe-pipeenrichmentparameters-httpparameters
            '''
            result = self._values.get("http_parameters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.PipeEnrichmentHttpParametersProperty"]], result)

        @builtins.property
        def input_template(self) -> typing.Optional[builtins.str]:
            '''Valid JSON text passed to the enrichment.

            In this case, nothing from the event itself is passed to the enrichment. For more information, see `The JavaScript Object Notation (JSON) Data Interchange Format <https://docs.aws.amazon.com/http://www.rfc-editor.org/rfc/rfc7159.txt>`_ .

            To remove an input template, specify an empty string.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipeenrichmentparameters.html#cfn-pipes-pipe-pipeenrichmentparameters-inputtemplate
            '''
            result = self._values.get("input_template")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PipeEnrichmentParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pipes.CfnPipe.PipeLogConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cloudwatch_logs_log_destination": "cloudwatchLogsLogDestination",
            "firehose_log_destination": "firehoseLogDestination",
            "include_execution_data": "includeExecutionData",
            "level": "level",
            "s3_log_destination": "s3LogDestination",
        },
    )
    class PipeLogConfigurationProperty:
        def __init__(
            self,
            *,
            cloudwatch_logs_log_destination: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPipe.CloudwatchLogsLogDestinationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            firehose_log_destination: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPipe.FirehoseLogDestinationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            include_execution_data: typing.Optional[typing.Sequence[builtins.str]] = None,
            level: typing.Optional[builtins.str] = None,
            s3_log_destination: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPipe.S3LogDestinationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Represents the configuration settings for the logs to which this pipe should report events.

            :param cloudwatch_logs_log_destination: The logging configuration settings for the pipe.
            :param firehose_log_destination: The Amazon Data Firehose logging configuration settings for the pipe.
            :param include_execution_data: Whether the execution data (specifically, the ``payload`` , ``awsRequest`` , and ``awsResponse`` fields) is included in the log messages for this pipe. This applies to all log destinations for the pipe. For more information, see `Including execution data in logs <https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes-logs.html#eb-pipes-logs-execution-data>`_ in the *Amazon EventBridge User Guide* . *Allowed values:* ``ALL``
            :param level: The level of logging detail to include. This applies to all log destinations for the pipe.
            :param s3_log_destination: The Amazon S3 logging configuration settings for the pipe.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipelogconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pipes as pipes
                
                pipe_log_configuration_property = pipes.CfnPipe.PipeLogConfigurationProperty(
                    cloudwatch_logs_log_destination=pipes.CfnPipe.CloudwatchLogsLogDestinationProperty(
                        log_group_arn="logGroupArn"
                    ),
                    firehose_log_destination=pipes.CfnPipe.FirehoseLogDestinationProperty(
                        delivery_stream_arn="deliveryStreamArn"
                    ),
                    include_execution_data=["includeExecutionData"],
                    level="level",
                    s3_log_destination=pipes.CfnPipe.S3LogDestinationProperty(
                        bucket_name="bucketName",
                        bucket_owner="bucketOwner",
                        output_format="outputFormat",
                        prefix="prefix"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__306252f91f65dd02a7e0e602af22016c4fe25b4159b0ed1f2ec374f280216abd)
                check_type(argname="argument cloudwatch_logs_log_destination", value=cloudwatch_logs_log_destination, expected_type=type_hints["cloudwatch_logs_log_destination"])
                check_type(argname="argument firehose_log_destination", value=firehose_log_destination, expected_type=type_hints["firehose_log_destination"])
                check_type(argname="argument include_execution_data", value=include_execution_data, expected_type=type_hints["include_execution_data"])
                check_type(argname="argument level", value=level, expected_type=type_hints["level"])
                check_type(argname="argument s3_log_destination", value=s3_log_destination, expected_type=type_hints["s3_log_destination"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if cloudwatch_logs_log_destination is not None:
                self._values["cloudwatch_logs_log_destination"] = cloudwatch_logs_log_destination
            if firehose_log_destination is not None:
                self._values["firehose_log_destination"] = firehose_log_destination
            if include_execution_data is not None:
                self._values["include_execution_data"] = include_execution_data
            if level is not None:
                self._values["level"] = level
            if s3_log_destination is not None:
                self._values["s3_log_destination"] = s3_log_destination

        @builtins.property
        def cloudwatch_logs_log_destination(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.CloudwatchLogsLogDestinationProperty"]]:
            '''The logging configuration settings for the pipe.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipelogconfiguration.html#cfn-pipes-pipe-pipelogconfiguration-cloudwatchlogslogdestination
            '''
            result = self._values.get("cloudwatch_logs_log_destination")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.CloudwatchLogsLogDestinationProperty"]], result)

        @builtins.property
        def firehose_log_destination(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.FirehoseLogDestinationProperty"]]:
            '''The Amazon Data Firehose logging configuration settings for the pipe.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipelogconfiguration.html#cfn-pipes-pipe-pipelogconfiguration-firehoselogdestination
            '''
            result = self._values.get("firehose_log_destination")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.FirehoseLogDestinationProperty"]], result)

        @builtins.property
        def include_execution_data(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Whether the execution data (specifically, the ``payload`` , ``awsRequest`` , and ``awsResponse`` fields) is included in the log messages for this pipe.

            This applies to all log destinations for the pipe.

            For more information, see `Including execution data in logs <https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes-logs.html#eb-pipes-logs-execution-data>`_ in the *Amazon EventBridge User Guide* .

            *Allowed values:* ``ALL``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipelogconfiguration.html#cfn-pipes-pipe-pipelogconfiguration-includeexecutiondata
            '''
            result = self._values.get("include_execution_data")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def level(self) -> typing.Optional[builtins.str]:
            '''The level of logging detail to include.

            This applies to all log destinations for the pipe.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipelogconfiguration.html#cfn-pipes-pipe-pipelogconfiguration-level
            '''
            result = self._values.get("level")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3_log_destination(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.S3LogDestinationProperty"]]:
            '''The Amazon S3 logging configuration settings for the pipe.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipelogconfiguration.html#cfn-pipes-pipe-pipelogconfiguration-s3logdestination
            '''
            result = self._values.get("s3_log_destination")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.S3LogDestinationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PipeLogConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pipes.CfnPipe.PipeSourceActiveMQBrokerParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "credentials": "credentials",
            "queue_name": "queueName",
            "batch_size": "batchSize",
            "maximum_batching_window_in_seconds": "maximumBatchingWindowInSeconds",
        },
    )
    class PipeSourceActiveMQBrokerParametersProperty:
        def __init__(
            self,
            *,
            credentials: typing.Union[_IResolvable_da3f097b, typing.Union["CfnPipe.MQBrokerAccessCredentialsProperty", typing.Dict[builtins.str, typing.Any]]],
            queue_name: builtins.str,
            batch_size: typing.Optional[jsii.Number] = None,
            maximum_batching_window_in_seconds: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''The parameters for using an Active MQ broker as a source.

            :param credentials: The credentials needed to access the resource.
            :param queue_name: The name of the destination queue to consume.
            :param batch_size: The maximum number of records to include in each batch.
            :param maximum_batching_window_in_seconds: The maximum length of a time to wait for events.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourceactivemqbrokerparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pipes as pipes
                
                pipe_source_active_mQBroker_parameters_property = pipes.CfnPipe.PipeSourceActiveMQBrokerParametersProperty(
                    credentials=pipes.CfnPipe.MQBrokerAccessCredentialsProperty(
                        basic_auth="basicAuth"
                    ),
                    queue_name="queueName",
                
                    # the properties below are optional
                    batch_size=123,
                    maximum_batching_window_in_seconds=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0146fc05725151ab0272065e74d8b279e41669f4c12c21bf5b654dc4ea4e0db3)
                check_type(argname="argument credentials", value=credentials, expected_type=type_hints["credentials"])
                check_type(argname="argument queue_name", value=queue_name, expected_type=type_hints["queue_name"])
                check_type(argname="argument batch_size", value=batch_size, expected_type=type_hints["batch_size"])
                check_type(argname="argument maximum_batching_window_in_seconds", value=maximum_batching_window_in_seconds, expected_type=type_hints["maximum_batching_window_in_seconds"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "credentials": credentials,
                "queue_name": queue_name,
            }
            if batch_size is not None:
                self._values["batch_size"] = batch_size
            if maximum_batching_window_in_seconds is not None:
                self._values["maximum_batching_window_in_seconds"] = maximum_batching_window_in_seconds

        @builtins.property
        def credentials(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnPipe.MQBrokerAccessCredentialsProperty"]:
            '''The credentials needed to access the resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourceactivemqbrokerparameters.html#cfn-pipes-pipe-pipesourceactivemqbrokerparameters-credentials
            '''
            result = self._values.get("credentials")
            assert result is not None, "Required property 'credentials' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnPipe.MQBrokerAccessCredentialsProperty"], result)

        @builtins.property
        def queue_name(self) -> builtins.str:
            '''The name of the destination queue to consume.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourceactivemqbrokerparameters.html#cfn-pipes-pipe-pipesourceactivemqbrokerparameters-queuename
            '''
            result = self._values.get("queue_name")
            assert result is not None, "Required property 'queue_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def batch_size(self) -> typing.Optional[jsii.Number]:
            '''The maximum number of records to include in each batch.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourceactivemqbrokerparameters.html#cfn-pipes-pipe-pipesourceactivemqbrokerparameters-batchsize
            '''
            result = self._values.get("batch_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def maximum_batching_window_in_seconds(self) -> typing.Optional[jsii.Number]:
            '''The maximum length of a time to wait for events.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourceactivemqbrokerparameters.html#cfn-pipes-pipe-pipesourceactivemqbrokerparameters-maximumbatchingwindowinseconds
            '''
            result = self._values.get("maximum_batching_window_in_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PipeSourceActiveMQBrokerParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pipes.CfnPipe.PipeSourceDynamoDBStreamParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "starting_position": "startingPosition",
            "batch_size": "batchSize",
            "dead_letter_config": "deadLetterConfig",
            "maximum_batching_window_in_seconds": "maximumBatchingWindowInSeconds",
            "maximum_record_age_in_seconds": "maximumRecordAgeInSeconds",
            "maximum_retry_attempts": "maximumRetryAttempts",
            "on_partial_batch_item_failure": "onPartialBatchItemFailure",
            "parallelization_factor": "parallelizationFactor",
        },
    )
    class PipeSourceDynamoDBStreamParametersProperty:
        def __init__(
            self,
            *,
            starting_position: builtins.str,
            batch_size: typing.Optional[jsii.Number] = None,
            dead_letter_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPipe.DeadLetterConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            maximum_batching_window_in_seconds: typing.Optional[jsii.Number] = None,
            maximum_record_age_in_seconds: typing.Optional[jsii.Number] = None,
            maximum_retry_attempts: typing.Optional[jsii.Number] = None,
            on_partial_batch_item_failure: typing.Optional[builtins.str] = None,
            parallelization_factor: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''The parameters for using a DynamoDB stream as a source.

            :param starting_position: (Streams only) The position in a stream from which to start reading. *Valid values* : ``TRIM_HORIZON | LATEST``
            :param batch_size: The maximum number of records to include in each batch.
            :param dead_letter_config: Define the target queue to send dead-letter queue events to.
            :param maximum_batching_window_in_seconds: The maximum length of a time to wait for events.
            :param maximum_record_age_in_seconds: (Streams only) Discard records older than the specified age. The default value is -1, which sets the maximum age to infinite. When the value is set to infinite, EventBridge never discards old records.
            :param maximum_retry_attempts: (Streams only) Discard records after the specified number of retries. The default value is -1, which sets the maximum number of retries to infinite. When MaximumRetryAttempts is infinite, EventBridge retries failed records until the record expires in the event source.
            :param on_partial_batch_item_failure: (Streams only) Define how to handle item process failures. ``AUTOMATIC_BISECT`` halves each batch and retry each half until all the records are processed or there is one failed message left in the batch.
            :param parallelization_factor: (Streams only) The number of batches to process concurrently from each shard. The default value is 1.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcedynamodbstreamparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pipes as pipes
                
                pipe_source_dynamo_dBStream_parameters_property = pipes.CfnPipe.PipeSourceDynamoDBStreamParametersProperty(
                    starting_position="startingPosition",
                
                    # the properties below are optional
                    batch_size=123,
                    dead_letter_config=pipes.CfnPipe.DeadLetterConfigProperty(
                        arn="arn"
                    ),
                    maximum_batching_window_in_seconds=123,
                    maximum_record_age_in_seconds=123,
                    maximum_retry_attempts=123,
                    on_partial_batch_item_failure="onPartialBatchItemFailure",
                    parallelization_factor=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c3914232e5e779f01bede413661456f0566bb16bbb4b0a9f9e7c7abf0a20b55f)
                check_type(argname="argument starting_position", value=starting_position, expected_type=type_hints["starting_position"])
                check_type(argname="argument batch_size", value=batch_size, expected_type=type_hints["batch_size"])
                check_type(argname="argument dead_letter_config", value=dead_letter_config, expected_type=type_hints["dead_letter_config"])
                check_type(argname="argument maximum_batching_window_in_seconds", value=maximum_batching_window_in_seconds, expected_type=type_hints["maximum_batching_window_in_seconds"])
                check_type(argname="argument maximum_record_age_in_seconds", value=maximum_record_age_in_seconds, expected_type=type_hints["maximum_record_age_in_seconds"])
                check_type(argname="argument maximum_retry_attempts", value=maximum_retry_attempts, expected_type=type_hints["maximum_retry_attempts"])
                check_type(argname="argument on_partial_batch_item_failure", value=on_partial_batch_item_failure, expected_type=type_hints["on_partial_batch_item_failure"])
                check_type(argname="argument parallelization_factor", value=parallelization_factor, expected_type=type_hints["parallelization_factor"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "starting_position": starting_position,
            }
            if batch_size is not None:
                self._values["batch_size"] = batch_size
            if dead_letter_config is not None:
                self._values["dead_letter_config"] = dead_letter_config
            if maximum_batching_window_in_seconds is not None:
                self._values["maximum_batching_window_in_seconds"] = maximum_batching_window_in_seconds
            if maximum_record_age_in_seconds is not None:
                self._values["maximum_record_age_in_seconds"] = maximum_record_age_in_seconds
            if maximum_retry_attempts is not None:
                self._values["maximum_retry_attempts"] = maximum_retry_attempts
            if on_partial_batch_item_failure is not None:
                self._values["on_partial_batch_item_failure"] = on_partial_batch_item_failure
            if parallelization_factor is not None:
                self._values["parallelization_factor"] = parallelization_factor

        @builtins.property
        def starting_position(self) -> builtins.str:
            '''(Streams only) The position in a stream from which to start reading.

            *Valid values* : ``TRIM_HORIZON | LATEST``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcedynamodbstreamparameters.html#cfn-pipes-pipe-pipesourcedynamodbstreamparameters-startingposition
            '''
            result = self._values.get("starting_position")
            assert result is not None, "Required property 'starting_position' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def batch_size(self) -> typing.Optional[jsii.Number]:
            '''The maximum number of records to include in each batch.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcedynamodbstreamparameters.html#cfn-pipes-pipe-pipesourcedynamodbstreamparameters-batchsize
            '''
            result = self._values.get("batch_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def dead_letter_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.DeadLetterConfigProperty"]]:
            '''Define the target queue to send dead-letter queue events to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcedynamodbstreamparameters.html#cfn-pipes-pipe-pipesourcedynamodbstreamparameters-deadletterconfig
            '''
            result = self._values.get("dead_letter_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.DeadLetterConfigProperty"]], result)

        @builtins.property
        def maximum_batching_window_in_seconds(self) -> typing.Optional[jsii.Number]:
            '''The maximum length of a time to wait for events.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcedynamodbstreamparameters.html#cfn-pipes-pipe-pipesourcedynamodbstreamparameters-maximumbatchingwindowinseconds
            '''
            result = self._values.get("maximum_batching_window_in_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def maximum_record_age_in_seconds(self) -> typing.Optional[jsii.Number]:
            '''(Streams only) Discard records older than the specified age.

            The default value is -1, which sets the maximum age to infinite. When the value is set to infinite, EventBridge never discards old records.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcedynamodbstreamparameters.html#cfn-pipes-pipe-pipesourcedynamodbstreamparameters-maximumrecordageinseconds
            '''
            result = self._values.get("maximum_record_age_in_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def maximum_retry_attempts(self) -> typing.Optional[jsii.Number]:
            '''(Streams only) Discard records after the specified number of retries.

            The default value is -1, which sets the maximum number of retries to infinite. When MaximumRetryAttempts is infinite, EventBridge retries failed records until the record expires in the event source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcedynamodbstreamparameters.html#cfn-pipes-pipe-pipesourcedynamodbstreamparameters-maximumretryattempts
            '''
            result = self._values.get("maximum_retry_attempts")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def on_partial_batch_item_failure(self) -> typing.Optional[builtins.str]:
            '''(Streams only) Define how to handle item process failures.

            ``AUTOMATIC_BISECT`` halves each batch and retry each half until all the records are processed or there is one failed message left in the batch.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcedynamodbstreamparameters.html#cfn-pipes-pipe-pipesourcedynamodbstreamparameters-onpartialbatchitemfailure
            '''
            result = self._values.get("on_partial_batch_item_failure")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def parallelization_factor(self) -> typing.Optional[jsii.Number]:
            '''(Streams only) The number of batches to process concurrently from each shard.

            The default value is 1.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcedynamodbstreamparameters.html#cfn-pipes-pipe-pipesourcedynamodbstreamparameters-parallelizationfactor
            '''
            result = self._values.get("parallelization_factor")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PipeSourceDynamoDBStreamParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pipes.CfnPipe.PipeSourceKinesisStreamParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "starting_position": "startingPosition",
            "batch_size": "batchSize",
            "dead_letter_config": "deadLetterConfig",
            "maximum_batching_window_in_seconds": "maximumBatchingWindowInSeconds",
            "maximum_record_age_in_seconds": "maximumRecordAgeInSeconds",
            "maximum_retry_attempts": "maximumRetryAttempts",
            "on_partial_batch_item_failure": "onPartialBatchItemFailure",
            "parallelization_factor": "parallelizationFactor",
            "starting_position_timestamp": "startingPositionTimestamp",
        },
    )
    class PipeSourceKinesisStreamParametersProperty:
        def __init__(
            self,
            *,
            starting_position: builtins.str,
            batch_size: typing.Optional[jsii.Number] = None,
            dead_letter_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPipe.DeadLetterConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            maximum_batching_window_in_seconds: typing.Optional[jsii.Number] = None,
            maximum_record_age_in_seconds: typing.Optional[jsii.Number] = None,
            maximum_retry_attempts: typing.Optional[jsii.Number] = None,
            on_partial_batch_item_failure: typing.Optional[builtins.str] = None,
            parallelization_factor: typing.Optional[jsii.Number] = None,
            starting_position_timestamp: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The parameters for using a Kinesis stream as a source.

            :param starting_position: (Streams only) The position in a stream from which to start reading.
            :param batch_size: The maximum number of records to include in each batch.
            :param dead_letter_config: Define the target queue to send dead-letter queue events to.
            :param maximum_batching_window_in_seconds: The maximum length of a time to wait for events.
            :param maximum_record_age_in_seconds: (Streams only) Discard records older than the specified age. The default value is -1, which sets the maximum age to infinite. When the value is set to infinite, EventBridge never discards old records.
            :param maximum_retry_attempts: (Streams only) Discard records after the specified number of retries. The default value is -1, which sets the maximum number of retries to infinite. When MaximumRetryAttempts is infinite, EventBridge retries failed records until the record expires in the event source.
            :param on_partial_batch_item_failure: (Streams only) Define how to handle item process failures. ``AUTOMATIC_BISECT`` halves each batch and retry each half until all the records are processed or there is one failed message left in the batch.
            :param parallelization_factor: (Streams only) The number of batches to process concurrently from each shard. The default value is 1.
            :param starting_position_timestamp: With ``StartingPosition`` set to ``AT_TIMESTAMP`` , the time from which to start reading, in Unix time seconds.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcekinesisstreamparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pipes as pipes
                
                pipe_source_kinesis_stream_parameters_property = pipes.CfnPipe.PipeSourceKinesisStreamParametersProperty(
                    starting_position="startingPosition",
                
                    # the properties below are optional
                    batch_size=123,
                    dead_letter_config=pipes.CfnPipe.DeadLetterConfigProperty(
                        arn="arn"
                    ),
                    maximum_batching_window_in_seconds=123,
                    maximum_record_age_in_seconds=123,
                    maximum_retry_attempts=123,
                    on_partial_batch_item_failure="onPartialBatchItemFailure",
                    parallelization_factor=123,
                    starting_position_timestamp="startingPositionTimestamp"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6b24786dafb795146de150a5ba8bedca4b5929c018392ddade565e7bf6a2a819)
                check_type(argname="argument starting_position", value=starting_position, expected_type=type_hints["starting_position"])
                check_type(argname="argument batch_size", value=batch_size, expected_type=type_hints["batch_size"])
                check_type(argname="argument dead_letter_config", value=dead_letter_config, expected_type=type_hints["dead_letter_config"])
                check_type(argname="argument maximum_batching_window_in_seconds", value=maximum_batching_window_in_seconds, expected_type=type_hints["maximum_batching_window_in_seconds"])
                check_type(argname="argument maximum_record_age_in_seconds", value=maximum_record_age_in_seconds, expected_type=type_hints["maximum_record_age_in_seconds"])
                check_type(argname="argument maximum_retry_attempts", value=maximum_retry_attempts, expected_type=type_hints["maximum_retry_attempts"])
                check_type(argname="argument on_partial_batch_item_failure", value=on_partial_batch_item_failure, expected_type=type_hints["on_partial_batch_item_failure"])
                check_type(argname="argument parallelization_factor", value=parallelization_factor, expected_type=type_hints["parallelization_factor"])
                check_type(argname="argument starting_position_timestamp", value=starting_position_timestamp, expected_type=type_hints["starting_position_timestamp"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "starting_position": starting_position,
            }
            if batch_size is not None:
                self._values["batch_size"] = batch_size
            if dead_letter_config is not None:
                self._values["dead_letter_config"] = dead_letter_config
            if maximum_batching_window_in_seconds is not None:
                self._values["maximum_batching_window_in_seconds"] = maximum_batching_window_in_seconds
            if maximum_record_age_in_seconds is not None:
                self._values["maximum_record_age_in_seconds"] = maximum_record_age_in_seconds
            if maximum_retry_attempts is not None:
                self._values["maximum_retry_attempts"] = maximum_retry_attempts
            if on_partial_batch_item_failure is not None:
                self._values["on_partial_batch_item_failure"] = on_partial_batch_item_failure
            if parallelization_factor is not None:
                self._values["parallelization_factor"] = parallelization_factor
            if starting_position_timestamp is not None:
                self._values["starting_position_timestamp"] = starting_position_timestamp

        @builtins.property
        def starting_position(self) -> builtins.str:
            '''(Streams only) The position in a stream from which to start reading.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcekinesisstreamparameters.html#cfn-pipes-pipe-pipesourcekinesisstreamparameters-startingposition
            '''
            result = self._values.get("starting_position")
            assert result is not None, "Required property 'starting_position' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def batch_size(self) -> typing.Optional[jsii.Number]:
            '''The maximum number of records to include in each batch.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcekinesisstreamparameters.html#cfn-pipes-pipe-pipesourcekinesisstreamparameters-batchsize
            '''
            result = self._values.get("batch_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def dead_letter_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.DeadLetterConfigProperty"]]:
            '''Define the target queue to send dead-letter queue events to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcekinesisstreamparameters.html#cfn-pipes-pipe-pipesourcekinesisstreamparameters-deadletterconfig
            '''
            result = self._values.get("dead_letter_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.DeadLetterConfigProperty"]], result)

        @builtins.property
        def maximum_batching_window_in_seconds(self) -> typing.Optional[jsii.Number]:
            '''The maximum length of a time to wait for events.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcekinesisstreamparameters.html#cfn-pipes-pipe-pipesourcekinesisstreamparameters-maximumbatchingwindowinseconds
            '''
            result = self._values.get("maximum_batching_window_in_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def maximum_record_age_in_seconds(self) -> typing.Optional[jsii.Number]:
            '''(Streams only) Discard records older than the specified age.

            The default value is -1, which sets the maximum age to infinite. When the value is set to infinite, EventBridge never discards old records.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcekinesisstreamparameters.html#cfn-pipes-pipe-pipesourcekinesisstreamparameters-maximumrecordageinseconds
            '''
            result = self._values.get("maximum_record_age_in_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def maximum_retry_attempts(self) -> typing.Optional[jsii.Number]:
            '''(Streams only) Discard records after the specified number of retries.

            The default value is -1, which sets the maximum number of retries to infinite. When MaximumRetryAttempts is infinite, EventBridge retries failed records until the record expires in the event source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcekinesisstreamparameters.html#cfn-pipes-pipe-pipesourcekinesisstreamparameters-maximumretryattempts
            '''
            result = self._values.get("maximum_retry_attempts")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def on_partial_batch_item_failure(self) -> typing.Optional[builtins.str]:
            '''(Streams only) Define how to handle item process failures.

            ``AUTOMATIC_BISECT`` halves each batch and retry each half until all the records are processed or there is one failed message left in the batch.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcekinesisstreamparameters.html#cfn-pipes-pipe-pipesourcekinesisstreamparameters-onpartialbatchitemfailure
            '''
            result = self._values.get("on_partial_batch_item_failure")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def parallelization_factor(self) -> typing.Optional[jsii.Number]:
            '''(Streams only) The number of batches to process concurrently from each shard.

            The default value is 1.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcekinesisstreamparameters.html#cfn-pipes-pipe-pipesourcekinesisstreamparameters-parallelizationfactor
            '''
            result = self._values.get("parallelization_factor")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def starting_position_timestamp(self) -> typing.Optional[builtins.str]:
            '''With ``StartingPosition`` set to ``AT_TIMESTAMP`` , the time from which to start reading, in Unix time seconds.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcekinesisstreamparameters.html#cfn-pipes-pipe-pipesourcekinesisstreamparameters-startingpositiontimestamp
            '''
            result = self._values.get("starting_position_timestamp")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PipeSourceKinesisStreamParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pipes.CfnPipe.PipeSourceManagedStreamingKafkaParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "topic_name": "topicName",
            "batch_size": "batchSize",
            "consumer_group_id": "consumerGroupId",
            "credentials": "credentials",
            "maximum_batching_window_in_seconds": "maximumBatchingWindowInSeconds",
            "starting_position": "startingPosition",
        },
    )
    class PipeSourceManagedStreamingKafkaParametersProperty:
        def __init__(
            self,
            *,
            topic_name: builtins.str,
            batch_size: typing.Optional[jsii.Number] = None,
            consumer_group_id: typing.Optional[builtins.str] = None,
            credentials: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPipe.MSKAccessCredentialsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            maximum_batching_window_in_seconds: typing.Optional[jsii.Number] = None,
            starting_position: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The parameters for using an MSK stream as a source.

            :param topic_name: The name of the topic that the pipe will read from.
            :param batch_size: The maximum number of records to include in each batch.
            :param consumer_group_id: The name of the destination queue to consume.
            :param credentials: The credentials needed to access the resource.
            :param maximum_batching_window_in_seconds: The maximum length of a time to wait for events.
            :param starting_position: (Streams only) The position in a stream from which to start reading.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcemanagedstreamingkafkaparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pipes as pipes
                
                pipe_source_managed_streaming_kafka_parameters_property = pipes.CfnPipe.PipeSourceManagedStreamingKafkaParametersProperty(
                    topic_name="topicName",
                
                    # the properties below are optional
                    batch_size=123,
                    consumer_group_id="consumerGroupId",
                    credentials=pipes.CfnPipe.MSKAccessCredentialsProperty(
                        client_certificate_tls_auth="clientCertificateTlsAuth",
                        sasl_scram512_auth="saslScram512Auth"
                    ),
                    maximum_batching_window_in_seconds=123,
                    starting_position="startingPosition"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8fa065b1f4c1a49a0c34029f20edbcee0895067597c39e79f08e5cb70c545116)
                check_type(argname="argument topic_name", value=topic_name, expected_type=type_hints["topic_name"])
                check_type(argname="argument batch_size", value=batch_size, expected_type=type_hints["batch_size"])
                check_type(argname="argument consumer_group_id", value=consumer_group_id, expected_type=type_hints["consumer_group_id"])
                check_type(argname="argument credentials", value=credentials, expected_type=type_hints["credentials"])
                check_type(argname="argument maximum_batching_window_in_seconds", value=maximum_batching_window_in_seconds, expected_type=type_hints["maximum_batching_window_in_seconds"])
                check_type(argname="argument starting_position", value=starting_position, expected_type=type_hints["starting_position"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "topic_name": topic_name,
            }
            if batch_size is not None:
                self._values["batch_size"] = batch_size
            if consumer_group_id is not None:
                self._values["consumer_group_id"] = consumer_group_id
            if credentials is not None:
                self._values["credentials"] = credentials
            if maximum_batching_window_in_seconds is not None:
                self._values["maximum_batching_window_in_seconds"] = maximum_batching_window_in_seconds
            if starting_position is not None:
                self._values["starting_position"] = starting_position

        @builtins.property
        def topic_name(self) -> builtins.str:
            '''The name of the topic that the pipe will read from.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcemanagedstreamingkafkaparameters.html#cfn-pipes-pipe-pipesourcemanagedstreamingkafkaparameters-topicname
            '''
            result = self._values.get("topic_name")
            assert result is not None, "Required property 'topic_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def batch_size(self) -> typing.Optional[jsii.Number]:
            '''The maximum number of records to include in each batch.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcemanagedstreamingkafkaparameters.html#cfn-pipes-pipe-pipesourcemanagedstreamingkafkaparameters-batchsize
            '''
            result = self._values.get("batch_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def consumer_group_id(self) -> typing.Optional[builtins.str]:
            '''The name of the destination queue to consume.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcemanagedstreamingkafkaparameters.html#cfn-pipes-pipe-pipesourcemanagedstreamingkafkaparameters-consumergroupid
            '''
            result = self._values.get("consumer_group_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def credentials(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.MSKAccessCredentialsProperty"]]:
            '''The credentials needed to access the resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcemanagedstreamingkafkaparameters.html#cfn-pipes-pipe-pipesourcemanagedstreamingkafkaparameters-credentials
            '''
            result = self._values.get("credentials")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.MSKAccessCredentialsProperty"]], result)

        @builtins.property
        def maximum_batching_window_in_seconds(self) -> typing.Optional[jsii.Number]:
            '''The maximum length of a time to wait for events.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcemanagedstreamingkafkaparameters.html#cfn-pipes-pipe-pipesourcemanagedstreamingkafkaparameters-maximumbatchingwindowinseconds
            '''
            result = self._values.get("maximum_batching_window_in_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def starting_position(self) -> typing.Optional[builtins.str]:
            '''(Streams only) The position in a stream from which to start reading.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcemanagedstreamingkafkaparameters.html#cfn-pipes-pipe-pipesourcemanagedstreamingkafkaparameters-startingposition
            '''
            result = self._values.get("starting_position")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PipeSourceManagedStreamingKafkaParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pipes.CfnPipe.PipeSourceParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "active_mq_broker_parameters": "activeMqBrokerParameters",
            "dynamo_db_stream_parameters": "dynamoDbStreamParameters",
            "filter_criteria": "filterCriteria",
            "kinesis_stream_parameters": "kinesisStreamParameters",
            "managed_streaming_kafka_parameters": "managedStreamingKafkaParameters",
            "rabbit_mq_broker_parameters": "rabbitMqBrokerParameters",
            "self_managed_kafka_parameters": "selfManagedKafkaParameters",
            "sqs_queue_parameters": "sqsQueueParameters",
        },
    )
    class PipeSourceParametersProperty:
        def __init__(
            self,
            *,
            active_mq_broker_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPipe.PipeSourceActiveMQBrokerParametersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            dynamo_db_stream_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPipe.PipeSourceDynamoDBStreamParametersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            filter_criteria: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPipe.FilterCriteriaProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            kinesis_stream_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPipe.PipeSourceKinesisStreamParametersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            managed_streaming_kafka_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPipe.PipeSourceManagedStreamingKafkaParametersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            rabbit_mq_broker_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPipe.PipeSourceRabbitMQBrokerParametersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            self_managed_kafka_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPipe.PipeSourceSelfManagedKafkaParametersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            sqs_queue_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPipe.PipeSourceSqsQueueParametersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The parameters required to set up a source for your pipe.

            :param active_mq_broker_parameters: The parameters for using an Active MQ broker as a source.
            :param dynamo_db_stream_parameters: The parameters for using a DynamoDB stream as a source.
            :param filter_criteria: The collection of event patterns used to filter events. To remove a filter, specify a ``FilterCriteria`` object with an empty array of ``Filter`` objects. For more information, see `Events and Event Patterns <https://docs.aws.amazon.com/eventbridge/latest/userguide/eventbridge-and-event-patterns.html>`_ in the *Amazon EventBridge User Guide* .
            :param kinesis_stream_parameters: The parameters for using a Kinesis stream as a source.
            :param managed_streaming_kafka_parameters: The parameters for using an MSK stream as a source.
            :param rabbit_mq_broker_parameters: The parameters for using a Rabbit MQ broker as a source.
            :param self_managed_kafka_parameters: The parameters for using a self-managed Apache Kafka stream as a source. A *self managed* cluster refers to any Apache Kafka cluster not hosted by AWS . This includes both clusters you manage yourself, as well as those hosted by a third-party provider, such as `Confluent Cloud <https://docs.aws.amazon.com/https://www.confluent.io/>`_ , `CloudKarafka <https://docs.aws.amazon.com/https://www.cloudkarafka.com/>`_ , or `Redpanda <https://docs.aws.amazon.com/https://redpanda.com/>`_ . For more information, see `Apache Kafka streams as a source <https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes-kafka.html>`_ in the *Amazon EventBridge User Guide* .
            :param sqs_queue_parameters: The parameters for using a Amazon SQS stream as a source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourceparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pipes as pipes
                
                pipe_source_parameters_property = pipes.CfnPipe.PipeSourceParametersProperty(
                    active_mq_broker_parameters=pipes.CfnPipe.PipeSourceActiveMQBrokerParametersProperty(
                        credentials=pipes.CfnPipe.MQBrokerAccessCredentialsProperty(
                            basic_auth="basicAuth"
                        ),
                        queue_name="queueName",
                
                        # the properties below are optional
                        batch_size=123,
                        maximum_batching_window_in_seconds=123
                    ),
                    dynamo_db_stream_parameters=pipes.CfnPipe.PipeSourceDynamoDBStreamParametersProperty(
                        starting_position="startingPosition",
                
                        # the properties below are optional
                        batch_size=123,
                        dead_letter_config=pipes.CfnPipe.DeadLetterConfigProperty(
                            arn="arn"
                        ),
                        maximum_batching_window_in_seconds=123,
                        maximum_record_age_in_seconds=123,
                        maximum_retry_attempts=123,
                        on_partial_batch_item_failure="onPartialBatchItemFailure",
                        parallelization_factor=123
                    ),
                    filter_criteria=pipes.CfnPipe.FilterCriteriaProperty(
                        filters=[pipes.CfnPipe.FilterProperty(
                            pattern="pattern"
                        )]
                    ),
                    kinesis_stream_parameters=pipes.CfnPipe.PipeSourceKinesisStreamParametersProperty(
                        starting_position="startingPosition",
                
                        # the properties below are optional
                        batch_size=123,
                        dead_letter_config=pipes.CfnPipe.DeadLetterConfigProperty(
                            arn="arn"
                        ),
                        maximum_batching_window_in_seconds=123,
                        maximum_record_age_in_seconds=123,
                        maximum_retry_attempts=123,
                        on_partial_batch_item_failure="onPartialBatchItemFailure",
                        parallelization_factor=123,
                        starting_position_timestamp="startingPositionTimestamp"
                    ),
                    managed_streaming_kafka_parameters=pipes.CfnPipe.PipeSourceManagedStreamingKafkaParametersProperty(
                        topic_name="topicName",
                
                        # the properties below are optional
                        batch_size=123,
                        consumer_group_id="consumerGroupId",
                        credentials=pipes.CfnPipe.MSKAccessCredentialsProperty(
                            client_certificate_tls_auth="clientCertificateTlsAuth",
                            sasl_scram512_auth="saslScram512Auth"
                        ),
                        maximum_batching_window_in_seconds=123,
                        starting_position="startingPosition"
                    ),
                    rabbit_mq_broker_parameters=pipes.CfnPipe.PipeSourceRabbitMQBrokerParametersProperty(
                        credentials=pipes.CfnPipe.MQBrokerAccessCredentialsProperty(
                            basic_auth="basicAuth"
                        ),
                        queue_name="queueName",
                
                        # the properties below are optional
                        batch_size=123,
                        maximum_batching_window_in_seconds=123,
                        virtual_host="virtualHost"
                    ),
                    self_managed_kafka_parameters=pipes.CfnPipe.PipeSourceSelfManagedKafkaParametersProperty(
                        topic_name="topicName",
                
                        # the properties below are optional
                        additional_bootstrap_servers=["additionalBootstrapServers"],
                        batch_size=123,
                        consumer_group_id="consumerGroupId",
                        credentials=pipes.CfnPipe.SelfManagedKafkaAccessConfigurationCredentialsProperty(
                            basic_auth="basicAuth",
                            client_certificate_tls_auth="clientCertificateTlsAuth",
                            sasl_scram256_auth="saslScram256Auth",
                            sasl_scram512_auth="saslScram512Auth"
                        ),
                        maximum_batching_window_in_seconds=123,
                        server_root_ca_certificate="serverRootCaCertificate",
                        starting_position="startingPosition",
                        vpc=pipes.CfnPipe.SelfManagedKafkaAccessConfigurationVpcProperty(
                            security_group=["securityGroup"],
                            subnets=["subnets"]
                        )
                    ),
                    sqs_queue_parameters=pipes.CfnPipe.PipeSourceSqsQueueParametersProperty(
                        batch_size=123,
                        maximum_batching_window_in_seconds=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f69eae8cb9c31c50f3f84207511653ea968efd2ef99df30157d160dff080c77f)
                check_type(argname="argument active_mq_broker_parameters", value=active_mq_broker_parameters, expected_type=type_hints["active_mq_broker_parameters"])
                check_type(argname="argument dynamo_db_stream_parameters", value=dynamo_db_stream_parameters, expected_type=type_hints["dynamo_db_stream_parameters"])
                check_type(argname="argument filter_criteria", value=filter_criteria, expected_type=type_hints["filter_criteria"])
                check_type(argname="argument kinesis_stream_parameters", value=kinesis_stream_parameters, expected_type=type_hints["kinesis_stream_parameters"])
                check_type(argname="argument managed_streaming_kafka_parameters", value=managed_streaming_kafka_parameters, expected_type=type_hints["managed_streaming_kafka_parameters"])
                check_type(argname="argument rabbit_mq_broker_parameters", value=rabbit_mq_broker_parameters, expected_type=type_hints["rabbit_mq_broker_parameters"])
                check_type(argname="argument self_managed_kafka_parameters", value=self_managed_kafka_parameters, expected_type=type_hints["self_managed_kafka_parameters"])
                check_type(argname="argument sqs_queue_parameters", value=sqs_queue_parameters, expected_type=type_hints["sqs_queue_parameters"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if active_mq_broker_parameters is not None:
                self._values["active_mq_broker_parameters"] = active_mq_broker_parameters
            if dynamo_db_stream_parameters is not None:
                self._values["dynamo_db_stream_parameters"] = dynamo_db_stream_parameters
            if filter_criteria is not None:
                self._values["filter_criteria"] = filter_criteria
            if kinesis_stream_parameters is not None:
                self._values["kinesis_stream_parameters"] = kinesis_stream_parameters
            if managed_streaming_kafka_parameters is not None:
                self._values["managed_streaming_kafka_parameters"] = managed_streaming_kafka_parameters
            if rabbit_mq_broker_parameters is not None:
                self._values["rabbit_mq_broker_parameters"] = rabbit_mq_broker_parameters
            if self_managed_kafka_parameters is not None:
                self._values["self_managed_kafka_parameters"] = self_managed_kafka_parameters
            if sqs_queue_parameters is not None:
                self._values["sqs_queue_parameters"] = sqs_queue_parameters

        @builtins.property
        def active_mq_broker_parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.PipeSourceActiveMQBrokerParametersProperty"]]:
            '''The parameters for using an Active MQ broker as a source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourceparameters.html#cfn-pipes-pipe-pipesourceparameters-activemqbrokerparameters
            '''
            result = self._values.get("active_mq_broker_parameters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.PipeSourceActiveMQBrokerParametersProperty"]], result)

        @builtins.property
        def dynamo_db_stream_parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.PipeSourceDynamoDBStreamParametersProperty"]]:
            '''The parameters for using a DynamoDB stream as a source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourceparameters.html#cfn-pipes-pipe-pipesourceparameters-dynamodbstreamparameters
            '''
            result = self._values.get("dynamo_db_stream_parameters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.PipeSourceDynamoDBStreamParametersProperty"]], result)

        @builtins.property
        def filter_criteria(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.FilterCriteriaProperty"]]:
            '''The collection of event patterns used to filter events.

            To remove a filter, specify a ``FilterCriteria`` object with an empty array of ``Filter`` objects.

            For more information, see `Events and Event Patterns <https://docs.aws.amazon.com/eventbridge/latest/userguide/eventbridge-and-event-patterns.html>`_ in the *Amazon EventBridge User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourceparameters.html#cfn-pipes-pipe-pipesourceparameters-filtercriteria
            '''
            result = self._values.get("filter_criteria")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.FilterCriteriaProperty"]], result)

        @builtins.property
        def kinesis_stream_parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.PipeSourceKinesisStreamParametersProperty"]]:
            '''The parameters for using a Kinesis stream as a source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourceparameters.html#cfn-pipes-pipe-pipesourceparameters-kinesisstreamparameters
            '''
            result = self._values.get("kinesis_stream_parameters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.PipeSourceKinesisStreamParametersProperty"]], result)

        @builtins.property
        def managed_streaming_kafka_parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.PipeSourceManagedStreamingKafkaParametersProperty"]]:
            '''The parameters for using an MSK stream as a source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourceparameters.html#cfn-pipes-pipe-pipesourceparameters-managedstreamingkafkaparameters
            '''
            result = self._values.get("managed_streaming_kafka_parameters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.PipeSourceManagedStreamingKafkaParametersProperty"]], result)

        @builtins.property
        def rabbit_mq_broker_parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.PipeSourceRabbitMQBrokerParametersProperty"]]:
            '''The parameters for using a Rabbit MQ broker as a source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourceparameters.html#cfn-pipes-pipe-pipesourceparameters-rabbitmqbrokerparameters
            '''
            result = self._values.get("rabbit_mq_broker_parameters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.PipeSourceRabbitMQBrokerParametersProperty"]], result)

        @builtins.property
        def self_managed_kafka_parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.PipeSourceSelfManagedKafkaParametersProperty"]]:
            '''The parameters for using a self-managed Apache Kafka stream as a source.

            A *self managed* cluster refers to any Apache Kafka cluster not hosted by AWS . This includes both clusters you manage yourself, as well as those hosted by a third-party provider, such as `Confluent Cloud <https://docs.aws.amazon.com/https://www.confluent.io/>`_ , `CloudKarafka <https://docs.aws.amazon.com/https://www.cloudkarafka.com/>`_ , or `Redpanda <https://docs.aws.amazon.com/https://redpanda.com/>`_ . For more information, see `Apache Kafka streams as a source <https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes-kafka.html>`_ in the *Amazon EventBridge User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourceparameters.html#cfn-pipes-pipe-pipesourceparameters-selfmanagedkafkaparameters
            '''
            result = self._values.get("self_managed_kafka_parameters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.PipeSourceSelfManagedKafkaParametersProperty"]], result)

        @builtins.property
        def sqs_queue_parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.PipeSourceSqsQueueParametersProperty"]]:
            '''The parameters for using a Amazon SQS stream as a source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourceparameters.html#cfn-pipes-pipe-pipesourceparameters-sqsqueueparameters
            '''
            result = self._values.get("sqs_queue_parameters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.PipeSourceSqsQueueParametersProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PipeSourceParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pipes.CfnPipe.PipeSourceRabbitMQBrokerParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "credentials": "credentials",
            "queue_name": "queueName",
            "batch_size": "batchSize",
            "maximum_batching_window_in_seconds": "maximumBatchingWindowInSeconds",
            "virtual_host": "virtualHost",
        },
    )
    class PipeSourceRabbitMQBrokerParametersProperty:
        def __init__(
            self,
            *,
            credentials: typing.Union[_IResolvable_da3f097b, typing.Union["CfnPipe.MQBrokerAccessCredentialsProperty", typing.Dict[builtins.str, typing.Any]]],
            queue_name: builtins.str,
            batch_size: typing.Optional[jsii.Number] = None,
            maximum_batching_window_in_seconds: typing.Optional[jsii.Number] = None,
            virtual_host: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The parameters for using a Rabbit MQ broker as a source.

            :param credentials: The credentials needed to access the resource.
            :param queue_name: The name of the destination queue to consume.
            :param batch_size: The maximum number of records to include in each batch.
            :param maximum_batching_window_in_seconds: The maximum length of a time to wait for events.
            :param virtual_host: The name of the virtual host associated with the source broker.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcerabbitmqbrokerparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pipes as pipes
                
                pipe_source_rabbit_mQBroker_parameters_property = pipes.CfnPipe.PipeSourceRabbitMQBrokerParametersProperty(
                    credentials=pipes.CfnPipe.MQBrokerAccessCredentialsProperty(
                        basic_auth="basicAuth"
                    ),
                    queue_name="queueName",
                
                    # the properties below are optional
                    batch_size=123,
                    maximum_batching_window_in_seconds=123,
                    virtual_host="virtualHost"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c74f43f119c84e728ccfcb7abb732d38519873fb7ec729b9fdf249f2c0e5bddd)
                check_type(argname="argument credentials", value=credentials, expected_type=type_hints["credentials"])
                check_type(argname="argument queue_name", value=queue_name, expected_type=type_hints["queue_name"])
                check_type(argname="argument batch_size", value=batch_size, expected_type=type_hints["batch_size"])
                check_type(argname="argument maximum_batching_window_in_seconds", value=maximum_batching_window_in_seconds, expected_type=type_hints["maximum_batching_window_in_seconds"])
                check_type(argname="argument virtual_host", value=virtual_host, expected_type=type_hints["virtual_host"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "credentials": credentials,
                "queue_name": queue_name,
            }
            if batch_size is not None:
                self._values["batch_size"] = batch_size
            if maximum_batching_window_in_seconds is not None:
                self._values["maximum_batching_window_in_seconds"] = maximum_batching_window_in_seconds
            if virtual_host is not None:
                self._values["virtual_host"] = virtual_host

        @builtins.property
        def credentials(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnPipe.MQBrokerAccessCredentialsProperty"]:
            '''The credentials needed to access the resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcerabbitmqbrokerparameters.html#cfn-pipes-pipe-pipesourcerabbitmqbrokerparameters-credentials
            '''
            result = self._values.get("credentials")
            assert result is not None, "Required property 'credentials' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnPipe.MQBrokerAccessCredentialsProperty"], result)

        @builtins.property
        def queue_name(self) -> builtins.str:
            '''The name of the destination queue to consume.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcerabbitmqbrokerparameters.html#cfn-pipes-pipe-pipesourcerabbitmqbrokerparameters-queuename
            '''
            result = self._values.get("queue_name")
            assert result is not None, "Required property 'queue_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def batch_size(self) -> typing.Optional[jsii.Number]:
            '''The maximum number of records to include in each batch.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcerabbitmqbrokerparameters.html#cfn-pipes-pipe-pipesourcerabbitmqbrokerparameters-batchsize
            '''
            result = self._values.get("batch_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def maximum_batching_window_in_seconds(self) -> typing.Optional[jsii.Number]:
            '''The maximum length of a time to wait for events.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcerabbitmqbrokerparameters.html#cfn-pipes-pipe-pipesourcerabbitmqbrokerparameters-maximumbatchingwindowinseconds
            '''
            result = self._values.get("maximum_batching_window_in_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def virtual_host(self) -> typing.Optional[builtins.str]:
            '''The name of the virtual host associated with the source broker.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcerabbitmqbrokerparameters.html#cfn-pipes-pipe-pipesourcerabbitmqbrokerparameters-virtualhost
            '''
            result = self._values.get("virtual_host")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PipeSourceRabbitMQBrokerParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pipes.CfnPipe.PipeSourceSelfManagedKafkaParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "topic_name": "topicName",
            "additional_bootstrap_servers": "additionalBootstrapServers",
            "batch_size": "batchSize",
            "consumer_group_id": "consumerGroupId",
            "credentials": "credentials",
            "maximum_batching_window_in_seconds": "maximumBatchingWindowInSeconds",
            "server_root_ca_certificate": "serverRootCaCertificate",
            "starting_position": "startingPosition",
            "vpc": "vpc",
        },
    )
    class PipeSourceSelfManagedKafkaParametersProperty:
        def __init__(
            self,
            *,
            topic_name: builtins.str,
            additional_bootstrap_servers: typing.Optional[typing.Sequence[builtins.str]] = None,
            batch_size: typing.Optional[jsii.Number] = None,
            consumer_group_id: typing.Optional[builtins.str] = None,
            credentials: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPipe.SelfManagedKafkaAccessConfigurationCredentialsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            maximum_batching_window_in_seconds: typing.Optional[jsii.Number] = None,
            server_root_ca_certificate: typing.Optional[builtins.str] = None,
            starting_position: typing.Optional[builtins.str] = None,
            vpc: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPipe.SelfManagedKafkaAccessConfigurationVpcProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The parameters for using a self-managed Apache Kafka stream as a source.

            A *self managed* cluster refers to any Apache Kafka cluster not hosted by AWS . This includes both clusters you manage yourself, as well as those hosted by a third-party provider, such as `Confluent Cloud <https://docs.aws.amazon.com/https://www.confluent.io/>`_ , `CloudKarafka <https://docs.aws.amazon.com/https://www.cloudkarafka.com/>`_ , or `Redpanda <https://docs.aws.amazon.com/https://redpanda.com/>`_ . For more information, see `Apache Kafka streams as a source <https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes-kafka.html>`_ in the *Amazon EventBridge User Guide* .

            :param topic_name: The name of the topic that the pipe will read from.
            :param additional_bootstrap_servers: An array of server URLs.
            :param batch_size: The maximum number of records to include in each batch.
            :param consumer_group_id: The name of the destination queue to consume.
            :param credentials: The credentials needed to access the resource.
            :param maximum_batching_window_in_seconds: The maximum length of a time to wait for events.
            :param server_root_ca_certificate: The ARN of the Secrets Manager secret used for certification.
            :param starting_position: (Streams only) The position in a stream from which to start reading.
            :param vpc: This structure specifies the VPC subnets and security groups for the stream, and whether a public IP address is to be used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourceselfmanagedkafkaparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pipes as pipes
                
                pipe_source_self_managed_kafka_parameters_property = pipes.CfnPipe.PipeSourceSelfManagedKafkaParametersProperty(
                    topic_name="topicName",
                
                    # the properties below are optional
                    additional_bootstrap_servers=["additionalBootstrapServers"],
                    batch_size=123,
                    consumer_group_id="consumerGroupId",
                    credentials=pipes.CfnPipe.SelfManagedKafkaAccessConfigurationCredentialsProperty(
                        basic_auth="basicAuth",
                        client_certificate_tls_auth="clientCertificateTlsAuth",
                        sasl_scram256_auth="saslScram256Auth",
                        sasl_scram512_auth="saslScram512Auth"
                    ),
                    maximum_batching_window_in_seconds=123,
                    server_root_ca_certificate="serverRootCaCertificate",
                    starting_position="startingPosition",
                    vpc=pipes.CfnPipe.SelfManagedKafkaAccessConfigurationVpcProperty(
                        security_group=["securityGroup"],
                        subnets=["subnets"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__66a0aa3e5511ea04d388f45c3036c4936d03c059f1ffad52b097b33a19a33603)
                check_type(argname="argument topic_name", value=topic_name, expected_type=type_hints["topic_name"])
                check_type(argname="argument additional_bootstrap_servers", value=additional_bootstrap_servers, expected_type=type_hints["additional_bootstrap_servers"])
                check_type(argname="argument batch_size", value=batch_size, expected_type=type_hints["batch_size"])
                check_type(argname="argument consumer_group_id", value=consumer_group_id, expected_type=type_hints["consumer_group_id"])
                check_type(argname="argument credentials", value=credentials, expected_type=type_hints["credentials"])
                check_type(argname="argument maximum_batching_window_in_seconds", value=maximum_batching_window_in_seconds, expected_type=type_hints["maximum_batching_window_in_seconds"])
                check_type(argname="argument server_root_ca_certificate", value=server_root_ca_certificate, expected_type=type_hints["server_root_ca_certificate"])
                check_type(argname="argument starting_position", value=starting_position, expected_type=type_hints["starting_position"])
                check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "topic_name": topic_name,
            }
            if additional_bootstrap_servers is not None:
                self._values["additional_bootstrap_servers"] = additional_bootstrap_servers
            if batch_size is not None:
                self._values["batch_size"] = batch_size
            if consumer_group_id is not None:
                self._values["consumer_group_id"] = consumer_group_id
            if credentials is not None:
                self._values["credentials"] = credentials
            if maximum_batching_window_in_seconds is not None:
                self._values["maximum_batching_window_in_seconds"] = maximum_batching_window_in_seconds
            if server_root_ca_certificate is not None:
                self._values["server_root_ca_certificate"] = server_root_ca_certificate
            if starting_position is not None:
                self._values["starting_position"] = starting_position
            if vpc is not None:
                self._values["vpc"] = vpc

        @builtins.property
        def topic_name(self) -> builtins.str:
            '''The name of the topic that the pipe will read from.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourceselfmanagedkafkaparameters.html#cfn-pipes-pipe-pipesourceselfmanagedkafkaparameters-topicname
            '''
            result = self._values.get("topic_name")
            assert result is not None, "Required property 'topic_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def additional_bootstrap_servers(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''An array of server URLs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourceselfmanagedkafkaparameters.html#cfn-pipes-pipe-pipesourceselfmanagedkafkaparameters-additionalbootstrapservers
            '''
            result = self._values.get("additional_bootstrap_servers")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def batch_size(self) -> typing.Optional[jsii.Number]:
            '''The maximum number of records to include in each batch.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourceselfmanagedkafkaparameters.html#cfn-pipes-pipe-pipesourceselfmanagedkafkaparameters-batchsize
            '''
            result = self._values.get("batch_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def consumer_group_id(self) -> typing.Optional[builtins.str]:
            '''The name of the destination queue to consume.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourceselfmanagedkafkaparameters.html#cfn-pipes-pipe-pipesourceselfmanagedkafkaparameters-consumergroupid
            '''
            result = self._values.get("consumer_group_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def credentials(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.SelfManagedKafkaAccessConfigurationCredentialsProperty"]]:
            '''The credentials needed to access the resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourceselfmanagedkafkaparameters.html#cfn-pipes-pipe-pipesourceselfmanagedkafkaparameters-credentials
            '''
            result = self._values.get("credentials")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.SelfManagedKafkaAccessConfigurationCredentialsProperty"]], result)

        @builtins.property
        def maximum_batching_window_in_seconds(self) -> typing.Optional[jsii.Number]:
            '''The maximum length of a time to wait for events.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourceselfmanagedkafkaparameters.html#cfn-pipes-pipe-pipesourceselfmanagedkafkaparameters-maximumbatchingwindowinseconds
            '''
            result = self._values.get("maximum_batching_window_in_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def server_root_ca_certificate(self) -> typing.Optional[builtins.str]:
            '''The ARN of the Secrets Manager secret used for certification.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourceselfmanagedkafkaparameters.html#cfn-pipes-pipe-pipesourceselfmanagedkafkaparameters-serverrootcacertificate
            '''
            result = self._values.get("server_root_ca_certificate")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def starting_position(self) -> typing.Optional[builtins.str]:
            '''(Streams only) The position in a stream from which to start reading.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourceselfmanagedkafkaparameters.html#cfn-pipes-pipe-pipesourceselfmanagedkafkaparameters-startingposition
            '''
            result = self._values.get("starting_position")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def vpc(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.SelfManagedKafkaAccessConfigurationVpcProperty"]]:
            '''This structure specifies the VPC subnets and security groups for the stream, and whether a public IP address is to be used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourceselfmanagedkafkaparameters.html#cfn-pipes-pipe-pipesourceselfmanagedkafkaparameters-vpc
            '''
            result = self._values.get("vpc")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.SelfManagedKafkaAccessConfigurationVpcProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PipeSourceSelfManagedKafkaParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pipes.CfnPipe.PipeSourceSqsQueueParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "batch_size": "batchSize",
            "maximum_batching_window_in_seconds": "maximumBatchingWindowInSeconds",
        },
    )
    class PipeSourceSqsQueueParametersProperty:
        def __init__(
            self,
            *,
            batch_size: typing.Optional[jsii.Number] = None,
            maximum_batching_window_in_seconds: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''The parameters for using a Amazon SQS stream as a source.

            :param batch_size: The maximum number of records to include in each batch.
            :param maximum_batching_window_in_seconds: The maximum length of a time to wait for events.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcesqsqueueparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pipes as pipes
                
                pipe_source_sqs_queue_parameters_property = pipes.CfnPipe.PipeSourceSqsQueueParametersProperty(
                    batch_size=123,
                    maximum_batching_window_in_seconds=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__67e4be2db1ed30e406fb7818b3884b7726611e447c0cbe62b206747477440cf9)
                check_type(argname="argument batch_size", value=batch_size, expected_type=type_hints["batch_size"])
                check_type(argname="argument maximum_batching_window_in_seconds", value=maximum_batching_window_in_seconds, expected_type=type_hints["maximum_batching_window_in_seconds"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if batch_size is not None:
                self._values["batch_size"] = batch_size
            if maximum_batching_window_in_seconds is not None:
                self._values["maximum_batching_window_in_seconds"] = maximum_batching_window_in_seconds

        @builtins.property
        def batch_size(self) -> typing.Optional[jsii.Number]:
            '''The maximum number of records to include in each batch.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcesqsqueueparameters.html#cfn-pipes-pipe-pipesourcesqsqueueparameters-batchsize
            '''
            result = self._values.get("batch_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def maximum_batching_window_in_seconds(self) -> typing.Optional[jsii.Number]:
            '''The maximum length of a time to wait for events.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipesourcesqsqueueparameters.html#cfn-pipes-pipe-pipesourcesqsqueueparameters-maximumbatchingwindowinseconds
            '''
            result = self._values.get("maximum_batching_window_in_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PipeSourceSqsQueueParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pipes.CfnPipe.PipeTargetBatchJobParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "job_definition": "jobDefinition",
            "job_name": "jobName",
            "array_properties": "arrayProperties",
            "container_overrides": "containerOverrides",
            "depends_on": "dependsOn",
            "parameters": "parameters",
            "retry_strategy": "retryStrategy",
        },
    )
    class PipeTargetBatchJobParametersProperty:
        def __init__(
            self,
            *,
            job_definition: builtins.str,
            job_name: builtins.str,
            array_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPipe.BatchArrayPropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            container_overrides: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPipe.BatchContainerOverridesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            depends_on: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPipe.BatchJobDependencyProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
            retry_strategy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPipe.BatchRetryStrategyProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The parameters for using an AWS Batch job as a target.

            :param job_definition: The job definition used by this job. This value can be one of ``name`` , ``name:revision`` , or the Amazon Resource Name (ARN) for the job definition. If name is specified without a revision then the latest active revision is used.
            :param job_name: The name of the job. It can be up to 128 letters long. The first character must be alphanumeric, can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (_).
            :param array_properties: The array properties for the submitted job, such as the size of the array. The array size can be between 2 and 10,000. If you specify array properties for a job, it becomes an array job. This parameter is used only if the target is an AWS Batch job.
            :param container_overrides: The overrides that are sent to a container.
            :param depends_on: A list of dependencies for the job. A job can depend upon a maximum of 20 jobs. You can specify a ``SEQUENTIAL`` type dependency without specifying a job ID for array jobs so that each child array job completes sequentially, starting at index 0. You can also specify an ``N_TO_N`` type dependency with a job ID for array jobs. In that case, each index child of this job must wait for the corresponding index child of each dependency to complete before it can begin.
            :param parameters: Additional parameters passed to the job that replace parameter substitution placeholders that are set in the job definition. Parameters are specified as a key and value pair mapping. Parameters included here override any corresponding parameter defaults from the job definition.
            :param retry_strategy: The retry strategy to use for failed jobs. When a retry strategy is specified here, it overrides the retry strategy defined in the job definition.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetbatchjobparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pipes as pipes
                
                pipe_target_batch_job_parameters_property = pipes.CfnPipe.PipeTargetBatchJobParametersProperty(
                    job_definition="jobDefinition",
                    job_name="jobName",
                
                    # the properties below are optional
                    array_properties=pipes.CfnPipe.BatchArrayPropertiesProperty(
                        size=123
                    ),
                    container_overrides=pipes.CfnPipe.BatchContainerOverridesProperty(
                        command=["command"],
                        environment=[pipes.CfnPipe.BatchEnvironmentVariableProperty(
                            name="name",
                            value="value"
                        )],
                        instance_type="instanceType",
                        resource_requirements=[pipes.CfnPipe.BatchResourceRequirementProperty(
                            type="type",
                            value="value"
                        )]
                    ),
                    depends_on=[pipes.CfnPipe.BatchJobDependencyProperty(
                        job_id="jobId",
                        type="type"
                    )],
                    parameters={
                        "parameters_key": "parameters"
                    },
                    retry_strategy=pipes.CfnPipe.BatchRetryStrategyProperty(
                        attempts=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a1cb92272e9e571b199ec86e09734d9a3e51183f8515940ff8f8fb18edb8487c)
                check_type(argname="argument job_definition", value=job_definition, expected_type=type_hints["job_definition"])
                check_type(argname="argument job_name", value=job_name, expected_type=type_hints["job_name"])
                check_type(argname="argument array_properties", value=array_properties, expected_type=type_hints["array_properties"])
                check_type(argname="argument container_overrides", value=container_overrides, expected_type=type_hints["container_overrides"])
                check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
                check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
                check_type(argname="argument retry_strategy", value=retry_strategy, expected_type=type_hints["retry_strategy"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "job_definition": job_definition,
                "job_name": job_name,
            }
            if array_properties is not None:
                self._values["array_properties"] = array_properties
            if container_overrides is not None:
                self._values["container_overrides"] = container_overrides
            if depends_on is not None:
                self._values["depends_on"] = depends_on
            if parameters is not None:
                self._values["parameters"] = parameters
            if retry_strategy is not None:
                self._values["retry_strategy"] = retry_strategy

        @builtins.property
        def job_definition(self) -> builtins.str:
            '''The job definition used by this job.

            This value can be one of ``name`` , ``name:revision`` , or the Amazon Resource Name (ARN) for the job definition. If name is specified without a revision then the latest active revision is used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetbatchjobparameters.html#cfn-pipes-pipe-pipetargetbatchjobparameters-jobdefinition
            '''
            result = self._values.get("job_definition")
            assert result is not None, "Required property 'job_definition' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def job_name(self) -> builtins.str:
            '''The name of the job.

            It can be up to 128 letters long. The first character must be alphanumeric, can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (_).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetbatchjobparameters.html#cfn-pipes-pipe-pipetargetbatchjobparameters-jobname
            '''
            result = self._values.get("job_name")
            assert result is not None, "Required property 'job_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def array_properties(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.BatchArrayPropertiesProperty"]]:
            '''The array properties for the submitted job, such as the size of the array.

            The array size can be between 2 and 10,000. If you specify array properties for a job, it becomes an array job. This parameter is used only if the target is an AWS Batch job.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetbatchjobparameters.html#cfn-pipes-pipe-pipetargetbatchjobparameters-arrayproperties
            '''
            result = self._values.get("array_properties")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.BatchArrayPropertiesProperty"]], result)

        @builtins.property
        def container_overrides(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.BatchContainerOverridesProperty"]]:
            '''The overrides that are sent to a container.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetbatchjobparameters.html#cfn-pipes-pipe-pipetargetbatchjobparameters-containeroverrides
            '''
            result = self._values.get("container_overrides")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.BatchContainerOverridesProperty"]], result)

        @builtins.property
        def depends_on(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPipe.BatchJobDependencyProperty"]]]]:
            '''A list of dependencies for the job.

            A job can depend upon a maximum of 20 jobs. You can specify a ``SEQUENTIAL`` type dependency without specifying a job ID for array jobs so that each child array job completes sequentially, starting at index 0. You can also specify an ``N_TO_N`` type dependency with a job ID for array jobs. In that case, each index child of this job must wait for the corresponding index child of each dependency to complete before it can begin.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetbatchjobparameters.html#cfn-pipes-pipe-pipetargetbatchjobparameters-dependson
            '''
            result = self._values.get("depends_on")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPipe.BatchJobDependencyProperty"]]]], result)

        @builtins.property
        def parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
            '''Additional parameters passed to the job that replace parameter substitution placeholders that are set in the job definition.

            Parameters are specified as a key and value pair mapping. Parameters included here override any corresponding parameter defaults from the job definition.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetbatchjobparameters.html#cfn-pipes-pipe-pipetargetbatchjobparameters-parameters
            '''
            result = self._values.get("parameters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], result)

        @builtins.property
        def retry_strategy(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.BatchRetryStrategyProperty"]]:
            '''The retry strategy to use for failed jobs.

            When a retry strategy is specified here, it overrides the retry strategy defined in the job definition.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetbatchjobparameters.html#cfn-pipes-pipe-pipetargetbatchjobparameters-retrystrategy
            '''
            result = self._values.get("retry_strategy")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.BatchRetryStrategyProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PipeTargetBatchJobParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pipes.CfnPipe.PipeTargetCloudWatchLogsParametersProperty",
        jsii_struct_bases=[],
        name_mapping={"log_stream_name": "logStreamName", "timestamp": "timestamp"},
    )
    class PipeTargetCloudWatchLogsParametersProperty:
        def __init__(
            self,
            *,
            log_stream_name: typing.Optional[builtins.str] = None,
            timestamp: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The parameters for using an CloudWatch Logs log stream as a target.

            :param log_stream_name: The name of the log stream.
            :param timestamp: The time the event occurred, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetcloudwatchlogsparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pipes as pipes
                
                pipe_target_cloud_watch_logs_parameters_property = pipes.CfnPipe.PipeTargetCloudWatchLogsParametersProperty(
                    log_stream_name="logStreamName",
                    timestamp="timestamp"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9be904989c92536dbb91aa23e3469c4c06a8919cf641a798da1e9c78b51b2156)
                check_type(argname="argument log_stream_name", value=log_stream_name, expected_type=type_hints["log_stream_name"])
                check_type(argname="argument timestamp", value=timestamp, expected_type=type_hints["timestamp"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if log_stream_name is not None:
                self._values["log_stream_name"] = log_stream_name
            if timestamp is not None:
                self._values["timestamp"] = timestamp

        @builtins.property
        def log_stream_name(self) -> typing.Optional[builtins.str]:
            '''The name of the log stream.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetcloudwatchlogsparameters.html#cfn-pipes-pipe-pipetargetcloudwatchlogsparameters-logstreamname
            '''
            result = self._values.get("log_stream_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def timestamp(self) -> typing.Optional[builtins.str]:
            '''The time the event occurred, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetcloudwatchlogsparameters.html#cfn-pipes-pipe-pipetargetcloudwatchlogsparameters-timestamp
            '''
            result = self._values.get("timestamp")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PipeTargetCloudWatchLogsParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pipes.CfnPipe.PipeTargetEcsTaskParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "task_definition_arn": "taskDefinitionArn",
            "capacity_provider_strategy": "capacityProviderStrategy",
            "enable_ecs_managed_tags": "enableEcsManagedTags",
            "enable_execute_command": "enableExecuteCommand",
            "group": "group",
            "launch_type": "launchType",
            "network_configuration": "networkConfiguration",
            "overrides": "overrides",
            "placement_constraints": "placementConstraints",
            "placement_strategy": "placementStrategy",
            "platform_version": "platformVersion",
            "propagate_tags": "propagateTags",
            "reference_id": "referenceId",
            "tags": "tags",
            "task_count": "taskCount",
        },
    )
    class PipeTargetEcsTaskParametersProperty:
        def __init__(
            self,
            *,
            task_definition_arn: builtins.str,
            capacity_provider_strategy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPipe.CapacityProviderStrategyItemProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            enable_ecs_managed_tags: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            enable_execute_command: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            group: typing.Optional[builtins.str] = None,
            launch_type: typing.Optional[builtins.str] = None,
            network_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPipe.NetworkConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            overrides: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPipe.EcsTaskOverrideProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            placement_constraints: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPipe.PlacementConstraintProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            placement_strategy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPipe.PlacementStrategyProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            platform_version: typing.Optional[builtins.str] = None,
            propagate_tags: typing.Optional[builtins.str] = None,
            reference_id: typing.Optional[builtins.str] = None,
            tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
            task_count: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''The parameters for using an Amazon ECS task as a target.

            :param task_definition_arn: The ARN of the task definition to use if the event target is an Amazon ECS task.
            :param capacity_provider_strategy: The capacity provider strategy to use for the task. If a ``capacityProviderStrategy`` is specified, the ``launchType`` parameter must be omitted. If no ``capacityProviderStrategy`` or launchType is specified, the ``defaultCapacityProviderStrategy`` for the cluster is used.
            :param enable_ecs_managed_tags: Specifies whether to enable Amazon ECS managed tags for the task. For more information, see `Tagging Your Amazon ECS Resources <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-using-tags.html>`_ in the Amazon Elastic Container Service Developer Guide. Default: - false
            :param enable_execute_command: Whether or not to enable the execute command functionality for the containers in this task. If true, this enables execute command functionality on all containers in the task. Default: - false
            :param group: Specifies an Amazon ECS task group for the task. The maximum length is 255 characters.
            :param launch_type: Specifies the launch type on which your task is running. The launch type that you specify here must match one of the launch type (compatibilities) of the target task. The ``FARGATE`` value is supported only in the Regions where AWS Fargate with Amazon ECS is supported. For more information, see `AWS Fargate on Amazon ECS <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS-Fargate.html>`_ in the *Amazon Elastic Container Service Developer Guide* .
            :param network_configuration: Use this structure if the Amazon ECS task uses the ``awsvpc`` network mode. This structure specifies the VPC subnets and security groups associated with the task, and whether a public IP address is to be used. This structure is required if ``LaunchType`` is ``FARGATE`` because the ``awsvpc`` mode is required for Fargate tasks. If you specify ``NetworkConfiguration`` when the target ECS task does not use the ``awsvpc`` network mode, the task fails.
            :param overrides: The overrides that are associated with a task.
            :param placement_constraints: An array of placement constraint objects to use for the task. You can specify up to 10 constraints per task (including constraints in the task definition and those specified at runtime).
            :param placement_strategy: The placement strategy objects to use for the task. You can specify a maximum of five strategy rules per task.
            :param platform_version: Specifies the platform version for the task. Specify only the numeric portion of the platform version, such as ``1.1.0`` . This structure is used only if ``LaunchType`` is ``FARGATE`` . For more information about valid platform versions, see `AWS Fargate Platform Versions <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html>`_ in the *Amazon Elastic Container Service Developer Guide* .
            :param propagate_tags: Specifies whether to propagate the tags from the task definition to the task. If no value is specified, the tags are not propagated. Tags can only be propagated to the task during task creation. To add tags to a task after task creation, use the ``TagResource`` API action.
            :param reference_id: The reference ID to use for the task.
            :param tags: The metadata that you apply to the task to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. To learn more, see `RunTask <https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_RunTask.html#ECS-RunTask-request-tags>`_ in the Amazon ECS API Reference.
            :param task_count: The number of tasks to create based on ``TaskDefinition`` . The default is 1.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetecstaskparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pipes as pipes
                
                pipe_target_ecs_task_parameters_property = pipes.CfnPipe.PipeTargetEcsTaskParametersProperty(
                    task_definition_arn="taskDefinitionArn",
                
                    # the properties below are optional
                    capacity_provider_strategy=[pipes.CfnPipe.CapacityProviderStrategyItemProperty(
                        capacity_provider="capacityProvider",
                
                        # the properties below are optional
                        base=123,
                        weight=123
                    )],
                    enable_ecs_managed_tags=False,
                    enable_execute_command=False,
                    group="group",
                    launch_type="launchType",
                    network_configuration=pipes.CfnPipe.NetworkConfigurationProperty(
                        awsvpc_configuration=pipes.CfnPipe.AwsVpcConfigurationProperty(
                            subnets=["subnets"],
                
                            # the properties below are optional
                            assign_public_ip="assignPublicIp",
                            security_groups=["securityGroups"]
                        )
                    ),
                    overrides=pipes.CfnPipe.EcsTaskOverrideProperty(
                        container_overrides=[pipes.CfnPipe.EcsContainerOverrideProperty(
                            command=["command"],
                            cpu=123,
                            environment=[pipes.CfnPipe.EcsEnvironmentVariableProperty(
                                name="name",
                                value="value"
                            )],
                            environment_files=[pipes.CfnPipe.EcsEnvironmentFileProperty(
                                type="type",
                                value="value"
                            )],
                            memory=123,
                            memory_reservation=123,
                            name="name",
                            resource_requirements=[pipes.CfnPipe.EcsResourceRequirementProperty(
                                type="type",
                                value="value"
                            )]
                        )],
                        cpu="cpu",
                        ephemeral_storage=pipes.CfnPipe.EcsEphemeralStorageProperty(
                            size_in_gi_b=123
                        ),
                        execution_role_arn="executionRoleArn",
                        inference_accelerator_overrides=[pipes.CfnPipe.EcsInferenceAcceleratorOverrideProperty(
                            device_name="deviceName",
                            device_type="deviceType"
                        )],
                        memory="memory",
                        task_role_arn="taskRoleArn"
                    ),
                    placement_constraints=[pipes.CfnPipe.PlacementConstraintProperty(
                        expression="expression",
                        type="type"
                    )],
                    placement_strategy=[pipes.CfnPipe.PlacementStrategyProperty(
                        field="field",
                        type="type"
                    )],
                    platform_version="platformVersion",
                    propagate_tags="propagateTags",
                    reference_id="referenceId",
                    tags=[CfnTag(
                        key="key",
                        value="value"
                    )],
                    task_count=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__da21f6b180d5c707968fc953abf6c9b6a20c14a97bb988159e2bff9f1252dc07)
                check_type(argname="argument task_definition_arn", value=task_definition_arn, expected_type=type_hints["task_definition_arn"])
                check_type(argname="argument capacity_provider_strategy", value=capacity_provider_strategy, expected_type=type_hints["capacity_provider_strategy"])
                check_type(argname="argument enable_ecs_managed_tags", value=enable_ecs_managed_tags, expected_type=type_hints["enable_ecs_managed_tags"])
                check_type(argname="argument enable_execute_command", value=enable_execute_command, expected_type=type_hints["enable_execute_command"])
                check_type(argname="argument group", value=group, expected_type=type_hints["group"])
                check_type(argname="argument launch_type", value=launch_type, expected_type=type_hints["launch_type"])
                check_type(argname="argument network_configuration", value=network_configuration, expected_type=type_hints["network_configuration"])
                check_type(argname="argument overrides", value=overrides, expected_type=type_hints["overrides"])
                check_type(argname="argument placement_constraints", value=placement_constraints, expected_type=type_hints["placement_constraints"])
                check_type(argname="argument placement_strategy", value=placement_strategy, expected_type=type_hints["placement_strategy"])
                check_type(argname="argument platform_version", value=platform_version, expected_type=type_hints["platform_version"])
                check_type(argname="argument propagate_tags", value=propagate_tags, expected_type=type_hints["propagate_tags"])
                check_type(argname="argument reference_id", value=reference_id, expected_type=type_hints["reference_id"])
                check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
                check_type(argname="argument task_count", value=task_count, expected_type=type_hints["task_count"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "task_definition_arn": task_definition_arn,
            }
            if capacity_provider_strategy is not None:
                self._values["capacity_provider_strategy"] = capacity_provider_strategy
            if enable_ecs_managed_tags is not None:
                self._values["enable_ecs_managed_tags"] = enable_ecs_managed_tags
            if enable_execute_command is not None:
                self._values["enable_execute_command"] = enable_execute_command
            if group is not None:
                self._values["group"] = group
            if launch_type is not None:
                self._values["launch_type"] = launch_type
            if network_configuration is not None:
                self._values["network_configuration"] = network_configuration
            if overrides is not None:
                self._values["overrides"] = overrides
            if placement_constraints is not None:
                self._values["placement_constraints"] = placement_constraints
            if placement_strategy is not None:
                self._values["placement_strategy"] = placement_strategy
            if platform_version is not None:
                self._values["platform_version"] = platform_version
            if propagate_tags is not None:
                self._values["propagate_tags"] = propagate_tags
            if reference_id is not None:
                self._values["reference_id"] = reference_id
            if tags is not None:
                self._values["tags"] = tags
            if task_count is not None:
                self._values["task_count"] = task_count

        @builtins.property
        def task_definition_arn(self) -> builtins.str:
            '''The ARN of the task definition to use if the event target is an Amazon ECS task.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetecstaskparameters.html#cfn-pipes-pipe-pipetargetecstaskparameters-taskdefinitionarn
            '''
            result = self._values.get("task_definition_arn")
            assert result is not None, "Required property 'task_definition_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def capacity_provider_strategy(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPipe.CapacityProviderStrategyItemProperty"]]]]:
            '''The capacity provider strategy to use for the task.

            If a ``capacityProviderStrategy`` is specified, the ``launchType`` parameter must be omitted. If no ``capacityProviderStrategy`` or launchType is specified, the ``defaultCapacityProviderStrategy`` for the cluster is used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetecstaskparameters.html#cfn-pipes-pipe-pipetargetecstaskparameters-capacityproviderstrategy
            '''
            result = self._values.get("capacity_provider_strategy")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPipe.CapacityProviderStrategyItemProperty"]]]], result)

        @builtins.property
        def enable_ecs_managed_tags(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies whether to enable Amazon ECS managed tags for the task.

            For more information, see `Tagging Your Amazon ECS Resources <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-using-tags.html>`_ in the Amazon Elastic Container Service Developer Guide.

            :default: - false

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetecstaskparameters.html#cfn-pipes-pipe-pipetargetecstaskparameters-enableecsmanagedtags
            '''
            result = self._values.get("enable_ecs_managed_tags")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def enable_execute_command(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Whether or not to enable the execute command functionality for the containers in this task.

            If true, this enables execute command functionality on all containers in the task.

            :default: - false

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetecstaskparameters.html#cfn-pipes-pipe-pipetargetecstaskparameters-enableexecutecommand
            '''
            result = self._values.get("enable_execute_command")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def group(self) -> typing.Optional[builtins.str]:
            '''Specifies an Amazon ECS task group for the task.

            The maximum length is 255 characters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetecstaskparameters.html#cfn-pipes-pipe-pipetargetecstaskparameters-group
            '''
            result = self._values.get("group")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def launch_type(self) -> typing.Optional[builtins.str]:
            '''Specifies the launch type on which your task is running.

            The launch type that you specify here must match one of the launch type (compatibilities) of the target task. The ``FARGATE`` value is supported only in the Regions where AWS Fargate with Amazon ECS is supported. For more information, see `AWS Fargate on Amazon ECS <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS-Fargate.html>`_ in the *Amazon Elastic Container Service Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetecstaskparameters.html#cfn-pipes-pipe-pipetargetecstaskparameters-launchtype
            '''
            result = self._values.get("launch_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def network_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.NetworkConfigurationProperty"]]:
            '''Use this structure if the Amazon ECS task uses the ``awsvpc`` network mode.

            This structure specifies the VPC subnets and security groups associated with the task, and whether a public IP address is to be used. This structure is required if ``LaunchType`` is ``FARGATE`` because the ``awsvpc`` mode is required for Fargate tasks.

            If you specify ``NetworkConfiguration`` when the target ECS task does not use the ``awsvpc`` network mode, the task fails.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetecstaskparameters.html#cfn-pipes-pipe-pipetargetecstaskparameters-networkconfiguration
            '''
            result = self._values.get("network_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.NetworkConfigurationProperty"]], result)

        @builtins.property
        def overrides(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.EcsTaskOverrideProperty"]]:
            '''The overrides that are associated with a task.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetecstaskparameters.html#cfn-pipes-pipe-pipetargetecstaskparameters-overrides
            '''
            result = self._values.get("overrides")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.EcsTaskOverrideProperty"]], result)

        @builtins.property
        def placement_constraints(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPipe.PlacementConstraintProperty"]]]]:
            '''An array of placement constraint objects to use for the task.

            You can specify up to 10 constraints per task (including constraints in the task definition and those specified at runtime).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetecstaskparameters.html#cfn-pipes-pipe-pipetargetecstaskparameters-placementconstraints
            '''
            result = self._values.get("placement_constraints")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPipe.PlacementConstraintProperty"]]]], result)

        @builtins.property
        def placement_strategy(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPipe.PlacementStrategyProperty"]]]]:
            '''The placement strategy objects to use for the task.

            You can specify a maximum of five strategy rules per task.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetecstaskparameters.html#cfn-pipes-pipe-pipetargetecstaskparameters-placementstrategy
            '''
            result = self._values.get("placement_strategy")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPipe.PlacementStrategyProperty"]]]], result)

        @builtins.property
        def platform_version(self) -> typing.Optional[builtins.str]:
            '''Specifies the platform version for the task.

            Specify only the numeric portion of the platform version, such as ``1.1.0`` .

            This structure is used only if ``LaunchType`` is ``FARGATE`` . For more information about valid platform versions, see `AWS Fargate Platform Versions <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html>`_ in the *Amazon Elastic Container Service Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetecstaskparameters.html#cfn-pipes-pipe-pipetargetecstaskparameters-platformversion
            '''
            result = self._values.get("platform_version")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def propagate_tags(self) -> typing.Optional[builtins.str]:
            '''Specifies whether to propagate the tags from the task definition to the task.

            If no value is specified, the tags are not propagated. Tags can only be propagated to the task during task creation. To add tags to a task after task creation, use the ``TagResource`` API action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetecstaskparameters.html#cfn-pipes-pipe-pipetargetecstaskparameters-propagatetags
            '''
            result = self._values.get("propagate_tags")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def reference_id(self) -> typing.Optional[builtins.str]:
            '''The reference ID to use for the task.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetecstaskparameters.html#cfn-pipes-pipe-pipetargetecstaskparameters-referenceid
            '''
            result = self._values.get("reference_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
            '''The metadata that you apply to the task to help you categorize and organize them.

            Each tag consists of a key and an optional value, both of which you define. To learn more, see `RunTask <https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_RunTask.html#ECS-RunTask-request-tags>`_ in the Amazon ECS API Reference.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetecstaskparameters.html#cfn-pipes-pipe-pipetargetecstaskparameters-tags
            '''
            result = self._values.get("tags")
            return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

        @builtins.property
        def task_count(self) -> typing.Optional[jsii.Number]:
            '''The number of tasks to create based on ``TaskDefinition`` .

            The default is 1.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetecstaskparameters.html#cfn-pipes-pipe-pipetargetecstaskparameters-taskcount
            '''
            result = self._values.get("task_count")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PipeTargetEcsTaskParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pipes.CfnPipe.PipeTargetEventBridgeEventBusParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "detail_type": "detailType",
            "endpoint_id": "endpointId",
            "resources": "resources",
            "source": "source",
            "time": "time",
        },
    )
    class PipeTargetEventBridgeEventBusParametersProperty:
        def __init__(
            self,
            *,
            detail_type: typing.Optional[builtins.str] = None,
            endpoint_id: typing.Optional[builtins.str] = None,
            resources: typing.Optional[typing.Sequence[builtins.str]] = None,
            source: typing.Optional[builtins.str] = None,
            time: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The parameters for using an EventBridge event bus as a target.

            :param detail_type: A free-form string, with a maximum of 128 characters, used to decide what fields to expect in the event detail.
            :param endpoint_id: The URL subdomain of the endpoint. For example, if the URL for Endpoint is https://abcde.veo.endpoints.event.amazonaws.com, then the EndpointId is ``abcde.veo`` .
            :param resources: AWS resources, identified by Amazon Resource Name (ARN), which the event primarily concerns. Any number, including zero, may be present.
            :param source: The source of the event.
            :param time: The time stamp of the event, per `RFC3339 <https://docs.aws.amazon.com/https://www.rfc-editor.org/rfc/rfc3339.txt>`_ . If no time stamp is provided, the time stamp of the `PutEvents <https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutEvents.html>`_ call is used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargeteventbridgeeventbusparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pipes as pipes
                
                pipe_target_event_bridge_event_bus_parameters_property = pipes.CfnPipe.PipeTargetEventBridgeEventBusParametersProperty(
                    detail_type="detailType",
                    endpoint_id="endpointId",
                    resources=["resources"],
                    source="source",
                    time="time"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e4ff5c800b247e08d889440f1b30d658847593d507da887052e6a07cd035a3a8)
                check_type(argname="argument detail_type", value=detail_type, expected_type=type_hints["detail_type"])
                check_type(argname="argument endpoint_id", value=endpoint_id, expected_type=type_hints["endpoint_id"])
                check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
                check_type(argname="argument source", value=source, expected_type=type_hints["source"])
                check_type(argname="argument time", value=time, expected_type=type_hints["time"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if detail_type is not None:
                self._values["detail_type"] = detail_type
            if endpoint_id is not None:
                self._values["endpoint_id"] = endpoint_id
            if resources is not None:
                self._values["resources"] = resources
            if source is not None:
                self._values["source"] = source
            if time is not None:
                self._values["time"] = time

        @builtins.property
        def detail_type(self) -> typing.Optional[builtins.str]:
            '''A free-form string, with a maximum of 128 characters, used to decide what fields to expect in the event detail.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargeteventbridgeeventbusparameters.html#cfn-pipes-pipe-pipetargeteventbridgeeventbusparameters-detailtype
            '''
            result = self._values.get("detail_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def endpoint_id(self) -> typing.Optional[builtins.str]:
            '''The URL subdomain of the endpoint.

            For example, if the URL for Endpoint is https://abcde.veo.endpoints.event.amazonaws.com, then the EndpointId is ``abcde.veo`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargeteventbridgeeventbusparameters.html#cfn-pipes-pipe-pipetargeteventbridgeeventbusparameters-endpointid
            '''
            result = self._values.get("endpoint_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def resources(self) -> typing.Optional[typing.List[builtins.str]]:
            '''AWS resources, identified by Amazon Resource Name (ARN), which the event primarily concerns.

            Any number, including zero, may be present.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargeteventbridgeeventbusparameters.html#cfn-pipes-pipe-pipetargeteventbridgeeventbusparameters-resources
            '''
            result = self._values.get("resources")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def source(self) -> typing.Optional[builtins.str]:
            '''The source of the event.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargeteventbridgeeventbusparameters.html#cfn-pipes-pipe-pipetargeteventbridgeeventbusparameters-source
            '''
            result = self._values.get("source")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def time(self) -> typing.Optional[builtins.str]:
            '''The time stamp of the event, per `RFC3339 <https://docs.aws.amazon.com/https://www.rfc-editor.org/rfc/rfc3339.txt>`_ . If no time stamp is provided, the time stamp of the `PutEvents <https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutEvents.html>`_ call is used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargeteventbridgeeventbusparameters.html#cfn-pipes-pipe-pipetargeteventbridgeeventbusparameters-time
            '''
            result = self._values.get("time")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PipeTargetEventBridgeEventBusParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pipes.CfnPipe.PipeTargetHttpParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "header_parameters": "headerParameters",
            "path_parameter_values": "pathParameterValues",
            "query_string_parameters": "queryStringParameters",
        },
    )
    class PipeTargetHttpParametersProperty:
        def __init__(
            self,
            *,
            header_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
            path_parameter_values: typing.Optional[typing.Sequence[builtins.str]] = None,
            query_string_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
        ) -> None:
            '''These are custom parameter to be used when the target is an API Gateway REST APIs or EventBridge ApiDestinations.

            :param header_parameters: The headers that need to be sent as part of request invoking the API Gateway REST API or EventBridge ApiDestination.
            :param path_parameter_values: The path parameter values to be used to populate API Gateway REST API or EventBridge ApiDestination path wildcards ("*").
            :param query_string_parameters: The query string keys/values that need to be sent as part of request invoking the API Gateway REST API or EventBridge ApiDestination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargethttpparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pipes as pipes
                
                pipe_target_http_parameters_property = pipes.CfnPipe.PipeTargetHttpParametersProperty(
                    header_parameters={
                        "header_parameters_key": "headerParameters"
                    },
                    path_parameter_values=["pathParameterValues"],
                    query_string_parameters={
                        "query_string_parameters_key": "queryStringParameters"
                    }
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7188f5bfc90d5dba8acd880f5c8ab24cadd75972f9cc901fb933192887a73e08)
                check_type(argname="argument header_parameters", value=header_parameters, expected_type=type_hints["header_parameters"])
                check_type(argname="argument path_parameter_values", value=path_parameter_values, expected_type=type_hints["path_parameter_values"])
                check_type(argname="argument query_string_parameters", value=query_string_parameters, expected_type=type_hints["query_string_parameters"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if header_parameters is not None:
                self._values["header_parameters"] = header_parameters
            if path_parameter_values is not None:
                self._values["path_parameter_values"] = path_parameter_values
            if query_string_parameters is not None:
                self._values["query_string_parameters"] = query_string_parameters

        @builtins.property
        def header_parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
            '''The headers that need to be sent as part of request invoking the API Gateway REST API or EventBridge ApiDestination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargethttpparameters.html#cfn-pipes-pipe-pipetargethttpparameters-headerparameters
            '''
            result = self._values.get("header_parameters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], result)

        @builtins.property
        def path_parameter_values(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The path parameter values to be used to populate API Gateway REST API or EventBridge ApiDestination path wildcards ("*").

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargethttpparameters.html#cfn-pipes-pipe-pipetargethttpparameters-pathparametervalues
            '''
            result = self._values.get("path_parameter_values")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def query_string_parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
            '''The query string keys/values that need to be sent as part of request invoking the API Gateway REST API or EventBridge ApiDestination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargethttpparameters.html#cfn-pipes-pipe-pipetargethttpparameters-querystringparameters
            '''
            result = self._values.get("query_string_parameters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PipeTargetHttpParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pipes.CfnPipe.PipeTargetKinesisStreamParametersProperty",
        jsii_struct_bases=[],
        name_mapping={"partition_key": "partitionKey"},
    )
    class PipeTargetKinesisStreamParametersProperty:
        def __init__(self, *, partition_key: builtins.str) -> None:
            '''The parameters for using a Kinesis stream as a target.

            :param partition_key: Determines which shard in the stream the data record is assigned to. Partition keys are Unicode strings with a maximum length limit of 256 characters for each key. Amazon Kinesis Data Streams uses the partition key as input to a hash function that maps the partition key and associated data to a specific shard. Specifically, an MD5 hash function is used to map partition keys to 128-bit integer values and to map associated data records to shards. As a result of this hashing mechanism, all data records with the same partition key map to the same shard within the stream.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetkinesisstreamparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pipes as pipes
                
                pipe_target_kinesis_stream_parameters_property = pipes.CfnPipe.PipeTargetKinesisStreamParametersProperty(
                    partition_key="partitionKey"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1f6573d105d52fd2f7280462dfe30eaedfc28e7d968c7cfb9b734b2d7b3df87d)
                check_type(argname="argument partition_key", value=partition_key, expected_type=type_hints["partition_key"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "partition_key": partition_key,
            }

        @builtins.property
        def partition_key(self) -> builtins.str:
            '''Determines which shard in the stream the data record is assigned to.

            Partition keys are Unicode strings with a maximum length limit of 256 characters for each key. Amazon Kinesis Data Streams uses the partition key as input to a hash function that maps the partition key and associated data to a specific shard. Specifically, an MD5 hash function is used to map partition keys to 128-bit integer values and to map associated data records to shards. As a result of this hashing mechanism, all data records with the same partition key map to the same shard within the stream.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetkinesisstreamparameters.html#cfn-pipes-pipe-pipetargetkinesisstreamparameters-partitionkey
            '''
            result = self._values.get("partition_key")
            assert result is not None, "Required property 'partition_key' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PipeTargetKinesisStreamParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pipes.CfnPipe.PipeTargetLambdaFunctionParametersProperty",
        jsii_struct_bases=[],
        name_mapping={"invocation_type": "invocationType"},
    )
    class PipeTargetLambdaFunctionParametersProperty:
        def __init__(
            self,
            *,
            invocation_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The parameters for using a Lambda function as a target.

            :param invocation_type: Specify whether to invoke the function synchronously or asynchronously. - ``REQUEST_RESPONSE`` (default) - Invoke synchronously. This corresponds to the ``RequestResponse`` option in the ``InvocationType`` parameter for the Lambda `Invoke <https://docs.aws.amazon.com/lambda/latest/dg/API_Invoke.html#API_Invoke_RequestSyntax>`_ API. - ``FIRE_AND_FORGET`` - Invoke asynchronously. This corresponds to the ``Event`` option in the ``InvocationType`` parameter for the Lambda `Invoke <https://docs.aws.amazon.com/lambda/latest/dg/API_Invoke.html#API_Invoke_RequestSyntax>`_ API. For more information, see `Invocation types <https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes.html#pipes-invocation>`_ in the *Amazon EventBridge User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetlambdafunctionparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pipes as pipes
                
                pipe_target_lambda_function_parameters_property = pipes.CfnPipe.PipeTargetLambdaFunctionParametersProperty(
                    invocation_type="invocationType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bb748756b23b0347b9022c2e96a5ec829bfa9e34d4d712d757794e89d1cb2d37)
                check_type(argname="argument invocation_type", value=invocation_type, expected_type=type_hints["invocation_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if invocation_type is not None:
                self._values["invocation_type"] = invocation_type

        @builtins.property
        def invocation_type(self) -> typing.Optional[builtins.str]:
            '''Specify whether to invoke the function synchronously or asynchronously.

            - ``REQUEST_RESPONSE`` (default) - Invoke synchronously. This corresponds to the ``RequestResponse`` option in the ``InvocationType`` parameter for the Lambda `Invoke <https://docs.aws.amazon.com/lambda/latest/dg/API_Invoke.html#API_Invoke_RequestSyntax>`_ API.
            - ``FIRE_AND_FORGET`` - Invoke asynchronously. This corresponds to the ``Event`` option in the ``InvocationType`` parameter for the Lambda `Invoke <https://docs.aws.amazon.com/lambda/latest/dg/API_Invoke.html#API_Invoke_RequestSyntax>`_ API.

            For more information, see `Invocation types <https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes.html#pipes-invocation>`_ in the *Amazon EventBridge User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetlambdafunctionparameters.html#cfn-pipes-pipe-pipetargetlambdafunctionparameters-invocationtype
            '''
            result = self._values.get("invocation_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PipeTargetLambdaFunctionParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pipes.CfnPipe.PipeTargetParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "batch_job_parameters": "batchJobParameters",
            "cloud_watch_logs_parameters": "cloudWatchLogsParameters",
            "ecs_task_parameters": "ecsTaskParameters",
            "event_bridge_event_bus_parameters": "eventBridgeEventBusParameters",
            "http_parameters": "httpParameters",
            "input_template": "inputTemplate",
            "kinesis_stream_parameters": "kinesisStreamParameters",
            "lambda_function_parameters": "lambdaFunctionParameters",
            "redshift_data_parameters": "redshiftDataParameters",
            "sage_maker_pipeline_parameters": "sageMakerPipelineParameters",
            "sqs_queue_parameters": "sqsQueueParameters",
            "step_function_state_machine_parameters": "stepFunctionStateMachineParameters",
        },
    )
    class PipeTargetParametersProperty:
        def __init__(
            self,
            *,
            batch_job_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPipe.PipeTargetBatchJobParametersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            cloud_watch_logs_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPipe.PipeTargetCloudWatchLogsParametersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            ecs_task_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPipe.PipeTargetEcsTaskParametersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            event_bridge_event_bus_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPipe.PipeTargetEventBridgeEventBusParametersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            http_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPipe.PipeTargetHttpParametersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            input_template: typing.Optional[builtins.str] = None,
            kinesis_stream_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPipe.PipeTargetKinesisStreamParametersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            lambda_function_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPipe.PipeTargetLambdaFunctionParametersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            redshift_data_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPipe.PipeTargetRedshiftDataParametersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            sage_maker_pipeline_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPipe.PipeTargetSageMakerPipelineParametersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            sqs_queue_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPipe.PipeTargetSqsQueueParametersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            step_function_state_machine_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPipe.PipeTargetStateMachineParametersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The parameters required to set up a target for your pipe.

            For more information about pipe target parameters, including how to use dynamic path parameters, see `Target parameters <https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes-event-target.html>`_ in the *Amazon EventBridge User Guide* .

            :param batch_job_parameters: The parameters for using an AWS Batch job as a target.
            :param cloud_watch_logs_parameters: The parameters for using an CloudWatch Logs log stream as a target.
            :param ecs_task_parameters: The parameters for using an Amazon ECS task as a target.
            :param event_bridge_event_bus_parameters: The parameters for using an EventBridge event bus as a target.
            :param http_parameters: These are custom parameter to be used when the target is an API Gateway REST APIs or EventBridge ApiDestinations.
            :param input_template: Valid JSON text passed to the target. In this case, nothing from the event itself is passed to the target. For more information, see `The JavaScript Object Notation (JSON) Data Interchange Format <https://docs.aws.amazon.com/http://www.rfc-editor.org/rfc/rfc7159.txt>`_ . To remove an input template, specify an empty string.
            :param kinesis_stream_parameters: The parameters for using a Kinesis stream as a target.
            :param lambda_function_parameters: The parameters for using a Lambda function as a target.
            :param redshift_data_parameters: These are custom parameters to be used when the target is a Amazon Redshift cluster to invoke the Amazon Redshift Data API BatchExecuteStatement.
            :param sage_maker_pipeline_parameters: The parameters for using a SageMaker pipeline as a target.
            :param sqs_queue_parameters: The parameters for using a Amazon SQS stream as a target.
            :param step_function_state_machine_parameters: The parameters for using a Step Functions state machine as a target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetparameters.html
            :exampleMetadata: infused

            Example::

                # source_queue: sqs.Queue
                # target_queue: sqs.Queue
                
                
                pipe_source = sources.SqsSource(source_queue,
                    batch_size=10,
                    maximum_batching_window=cdk.Duration.seconds(10)
                )
                
                pipe = pipes.Pipe(self, "Pipe",
                    source=pipe_source,
                    target=SomeTarget(target_queue)
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__165d2153d77ee319562b47678485053dec4a8dbcb94c274abe1d78488c0de760)
                check_type(argname="argument batch_job_parameters", value=batch_job_parameters, expected_type=type_hints["batch_job_parameters"])
                check_type(argname="argument cloud_watch_logs_parameters", value=cloud_watch_logs_parameters, expected_type=type_hints["cloud_watch_logs_parameters"])
                check_type(argname="argument ecs_task_parameters", value=ecs_task_parameters, expected_type=type_hints["ecs_task_parameters"])
                check_type(argname="argument event_bridge_event_bus_parameters", value=event_bridge_event_bus_parameters, expected_type=type_hints["event_bridge_event_bus_parameters"])
                check_type(argname="argument http_parameters", value=http_parameters, expected_type=type_hints["http_parameters"])
                check_type(argname="argument input_template", value=input_template, expected_type=type_hints["input_template"])
                check_type(argname="argument kinesis_stream_parameters", value=kinesis_stream_parameters, expected_type=type_hints["kinesis_stream_parameters"])
                check_type(argname="argument lambda_function_parameters", value=lambda_function_parameters, expected_type=type_hints["lambda_function_parameters"])
                check_type(argname="argument redshift_data_parameters", value=redshift_data_parameters, expected_type=type_hints["redshift_data_parameters"])
                check_type(argname="argument sage_maker_pipeline_parameters", value=sage_maker_pipeline_parameters, expected_type=type_hints["sage_maker_pipeline_parameters"])
                check_type(argname="argument sqs_queue_parameters", value=sqs_queue_parameters, expected_type=type_hints["sqs_queue_parameters"])
                check_type(argname="argument step_function_state_machine_parameters", value=step_function_state_machine_parameters, expected_type=type_hints["step_function_state_machine_parameters"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if batch_job_parameters is not None:
                self._values["batch_job_parameters"] = batch_job_parameters
            if cloud_watch_logs_parameters is not None:
                self._values["cloud_watch_logs_parameters"] = cloud_watch_logs_parameters
            if ecs_task_parameters is not None:
                self._values["ecs_task_parameters"] = ecs_task_parameters
            if event_bridge_event_bus_parameters is not None:
                self._values["event_bridge_event_bus_parameters"] = event_bridge_event_bus_parameters
            if http_parameters is not None:
                self._values["http_parameters"] = http_parameters
            if input_template is not None:
                self._values["input_template"] = input_template
            if kinesis_stream_parameters is not None:
                self._values["kinesis_stream_parameters"] = kinesis_stream_parameters
            if lambda_function_parameters is not None:
                self._values["lambda_function_parameters"] = lambda_function_parameters
            if redshift_data_parameters is not None:
                self._values["redshift_data_parameters"] = redshift_data_parameters
            if sage_maker_pipeline_parameters is not None:
                self._values["sage_maker_pipeline_parameters"] = sage_maker_pipeline_parameters
            if sqs_queue_parameters is not None:
                self._values["sqs_queue_parameters"] = sqs_queue_parameters
            if step_function_state_machine_parameters is not None:
                self._values["step_function_state_machine_parameters"] = step_function_state_machine_parameters

        @builtins.property
        def batch_job_parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.PipeTargetBatchJobParametersProperty"]]:
            '''The parameters for using an AWS Batch job as a target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetparameters.html#cfn-pipes-pipe-pipetargetparameters-batchjobparameters
            '''
            result = self._values.get("batch_job_parameters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.PipeTargetBatchJobParametersProperty"]], result)

        @builtins.property
        def cloud_watch_logs_parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.PipeTargetCloudWatchLogsParametersProperty"]]:
            '''The parameters for using an CloudWatch Logs log stream as a target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetparameters.html#cfn-pipes-pipe-pipetargetparameters-cloudwatchlogsparameters
            '''
            result = self._values.get("cloud_watch_logs_parameters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.PipeTargetCloudWatchLogsParametersProperty"]], result)

        @builtins.property
        def ecs_task_parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.PipeTargetEcsTaskParametersProperty"]]:
            '''The parameters for using an Amazon ECS task as a target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetparameters.html#cfn-pipes-pipe-pipetargetparameters-ecstaskparameters
            '''
            result = self._values.get("ecs_task_parameters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.PipeTargetEcsTaskParametersProperty"]], result)

        @builtins.property
        def event_bridge_event_bus_parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.PipeTargetEventBridgeEventBusParametersProperty"]]:
            '''The parameters for using an EventBridge event bus as a target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetparameters.html#cfn-pipes-pipe-pipetargetparameters-eventbridgeeventbusparameters
            '''
            result = self._values.get("event_bridge_event_bus_parameters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.PipeTargetEventBridgeEventBusParametersProperty"]], result)

        @builtins.property
        def http_parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.PipeTargetHttpParametersProperty"]]:
            '''These are custom parameter to be used when the target is an API Gateway REST APIs or EventBridge ApiDestinations.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetparameters.html#cfn-pipes-pipe-pipetargetparameters-httpparameters
            '''
            result = self._values.get("http_parameters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.PipeTargetHttpParametersProperty"]], result)

        @builtins.property
        def input_template(self) -> typing.Optional[builtins.str]:
            '''Valid JSON text passed to the target.

            In this case, nothing from the event itself is passed to the target. For more information, see `The JavaScript Object Notation (JSON) Data Interchange Format <https://docs.aws.amazon.com/http://www.rfc-editor.org/rfc/rfc7159.txt>`_ .

            To remove an input template, specify an empty string.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetparameters.html#cfn-pipes-pipe-pipetargetparameters-inputtemplate
            '''
            result = self._values.get("input_template")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def kinesis_stream_parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.PipeTargetKinesisStreamParametersProperty"]]:
            '''The parameters for using a Kinesis stream as a target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetparameters.html#cfn-pipes-pipe-pipetargetparameters-kinesisstreamparameters
            '''
            result = self._values.get("kinesis_stream_parameters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.PipeTargetKinesisStreamParametersProperty"]], result)

        @builtins.property
        def lambda_function_parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.PipeTargetLambdaFunctionParametersProperty"]]:
            '''The parameters for using a Lambda function as a target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetparameters.html#cfn-pipes-pipe-pipetargetparameters-lambdafunctionparameters
            '''
            result = self._values.get("lambda_function_parameters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.PipeTargetLambdaFunctionParametersProperty"]], result)

        @builtins.property
        def redshift_data_parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.PipeTargetRedshiftDataParametersProperty"]]:
            '''These are custom parameters to be used when the target is a Amazon Redshift cluster to invoke the Amazon Redshift Data API BatchExecuteStatement.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetparameters.html#cfn-pipes-pipe-pipetargetparameters-redshiftdataparameters
            '''
            result = self._values.get("redshift_data_parameters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.PipeTargetRedshiftDataParametersProperty"]], result)

        @builtins.property
        def sage_maker_pipeline_parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.PipeTargetSageMakerPipelineParametersProperty"]]:
            '''The parameters for using a SageMaker pipeline as a target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetparameters.html#cfn-pipes-pipe-pipetargetparameters-sagemakerpipelineparameters
            '''
            result = self._values.get("sage_maker_pipeline_parameters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.PipeTargetSageMakerPipelineParametersProperty"]], result)

        @builtins.property
        def sqs_queue_parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.PipeTargetSqsQueueParametersProperty"]]:
            '''The parameters for using a Amazon SQS stream as a target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetparameters.html#cfn-pipes-pipe-pipetargetparameters-sqsqueueparameters
            '''
            result = self._values.get("sqs_queue_parameters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.PipeTargetSqsQueueParametersProperty"]], result)

        @builtins.property
        def step_function_state_machine_parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.PipeTargetStateMachineParametersProperty"]]:
            '''The parameters for using a Step Functions state machine as a target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetparameters.html#cfn-pipes-pipe-pipetargetparameters-stepfunctionstatemachineparameters
            '''
            result = self._values.get("step_function_state_machine_parameters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipe.PipeTargetStateMachineParametersProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PipeTargetParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pipes.CfnPipe.PipeTargetRedshiftDataParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "database": "database",
            "sqls": "sqls",
            "db_user": "dbUser",
            "secret_manager_arn": "secretManagerArn",
            "statement_name": "statementName",
            "with_event": "withEvent",
        },
    )
    class PipeTargetRedshiftDataParametersProperty:
        def __init__(
            self,
            *,
            database: builtins.str,
            sqls: typing.Sequence[builtins.str],
            db_user: typing.Optional[builtins.str] = None,
            secret_manager_arn: typing.Optional[builtins.str] = None,
            statement_name: typing.Optional[builtins.str] = None,
            with_event: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''These are custom parameters to be used when the target is a Amazon Redshift cluster to invoke the Amazon Redshift Data API BatchExecuteStatement.

            :param database: The name of the database. Required when authenticating using temporary credentials.
            :param sqls: The SQL statement text to run.
            :param db_user: The database user name. Required when authenticating using temporary credentials.
            :param secret_manager_arn: The name or ARN of the secret that enables access to the database. Required when authenticating using Secrets Manager.
            :param statement_name: The name of the SQL statement. You can name the SQL statement when you create it to identify the query.
            :param with_event: Indicates whether to send an event back to EventBridge after the SQL statement runs. Default: - false

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetredshiftdataparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pipes as pipes
                
                pipe_target_redshift_data_parameters_property = pipes.CfnPipe.PipeTargetRedshiftDataParametersProperty(
                    database="database",
                    sqls=["sqls"],
                
                    # the properties below are optional
                    db_user="dbUser",
                    secret_manager_arn="secretManagerArn",
                    statement_name="statementName",
                    with_event=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b7ea6dedf4af0c373d420ab7d2ec651a184123217d353843d2015cd78c2e412a)
                check_type(argname="argument database", value=database, expected_type=type_hints["database"])
                check_type(argname="argument sqls", value=sqls, expected_type=type_hints["sqls"])
                check_type(argname="argument db_user", value=db_user, expected_type=type_hints["db_user"])
                check_type(argname="argument secret_manager_arn", value=secret_manager_arn, expected_type=type_hints["secret_manager_arn"])
                check_type(argname="argument statement_name", value=statement_name, expected_type=type_hints["statement_name"])
                check_type(argname="argument with_event", value=with_event, expected_type=type_hints["with_event"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "database": database,
                "sqls": sqls,
            }
            if db_user is not None:
                self._values["db_user"] = db_user
            if secret_manager_arn is not None:
                self._values["secret_manager_arn"] = secret_manager_arn
            if statement_name is not None:
                self._values["statement_name"] = statement_name
            if with_event is not None:
                self._values["with_event"] = with_event

        @builtins.property
        def database(self) -> builtins.str:
            '''The name of the database.

            Required when authenticating using temporary credentials.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetredshiftdataparameters.html#cfn-pipes-pipe-pipetargetredshiftdataparameters-database
            '''
            result = self._values.get("database")
            assert result is not None, "Required property 'database' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def sqls(self) -> typing.List[builtins.str]:
            '''The SQL statement text to run.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetredshiftdataparameters.html#cfn-pipes-pipe-pipetargetredshiftdataparameters-sqls
            '''
            result = self._values.get("sqls")
            assert result is not None, "Required property 'sqls' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def db_user(self) -> typing.Optional[builtins.str]:
            '''The database user name.

            Required when authenticating using temporary credentials.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetredshiftdataparameters.html#cfn-pipes-pipe-pipetargetredshiftdataparameters-dbuser
            '''
            result = self._values.get("db_user")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def secret_manager_arn(self) -> typing.Optional[builtins.str]:
            '''The name or ARN of the secret that enables access to the database.

            Required when authenticating using Secrets Manager.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetredshiftdataparameters.html#cfn-pipes-pipe-pipetargetredshiftdataparameters-secretmanagerarn
            '''
            result = self._values.get("secret_manager_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def statement_name(self) -> typing.Optional[builtins.str]:
            '''The name of the SQL statement.

            You can name the SQL statement when you create it to identify the query.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetredshiftdataparameters.html#cfn-pipes-pipe-pipetargetredshiftdataparameters-statementname
            '''
            result = self._values.get("statement_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def with_event(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates whether to send an event back to EventBridge after the SQL statement runs.

            :default: - false

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetredshiftdataparameters.html#cfn-pipes-pipe-pipetargetredshiftdataparameters-withevent
            '''
            result = self._values.get("with_event")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PipeTargetRedshiftDataParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pipes.CfnPipe.PipeTargetSageMakerPipelineParametersProperty",
        jsii_struct_bases=[],
        name_mapping={"pipeline_parameter_list": "pipelineParameterList"},
    )
    class PipeTargetSageMakerPipelineParametersProperty:
        def __init__(
            self,
            *,
            pipeline_parameter_list: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPipe.SageMakerPipelineParameterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''The parameters for using a SageMaker pipeline as a target.

            :param pipeline_parameter_list: List of Parameter names and values for SageMaker Model Building Pipeline execution.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetsagemakerpipelineparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pipes as pipes
                
                pipe_target_sage_maker_pipeline_parameters_property = pipes.CfnPipe.PipeTargetSageMakerPipelineParametersProperty(
                    pipeline_parameter_list=[pipes.CfnPipe.SageMakerPipelineParameterProperty(
                        name="name",
                        value="value"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a0605c1a90997b245e51ad3fb0e2d8178d3a57cc7250323bcd66289779b8c17b)
                check_type(argname="argument pipeline_parameter_list", value=pipeline_parameter_list, expected_type=type_hints["pipeline_parameter_list"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if pipeline_parameter_list is not None:
                self._values["pipeline_parameter_list"] = pipeline_parameter_list

        @builtins.property
        def pipeline_parameter_list(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPipe.SageMakerPipelineParameterProperty"]]]]:
            '''List of Parameter names and values for SageMaker Model Building Pipeline execution.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetsagemakerpipelineparameters.html#cfn-pipes-pipe-pipetargetsagemakerpipelineparameters-pipelineparameterlist
            '''
            result = self._values.get("pipeline_parameter_list")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPipe.SageMakerPipelineParameterProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PipeTargetSageMakerPipelineParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pipes.CfnPipe.PipeTargetSqsQueueParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "message_deduplication_id": "messageDeduplicationId",
            "message_group_id": "messageGroupId",
        },
    )
    class PipeTargetSqsQueueParametersProperty:
        def __init__(
            self,
            *,
            message_deduplication_id: typing.Optional[builtins.str] = None,
            message_group_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The parameters for using a Amazon SQS stream as a target.

            :param message_deduplication_id: This parameter applies only to FIFO (first-in-first-out) queues. The token used for deduplication of sent messages.
            :param message_group_id: The FIFO message group ID to use as the target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetsqsqueueparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pipes as pipes
                
                pipe_target_sqs_queue_parameters_property = pipes.CfnPipe.PipeTargetSqsQueueParametersProperty(
                    message_deduplication_id="messageDeduplicationId",
                    message_group_id="messageGroupId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3a65dfb99d32c62fab8dad285f75fc0a48cf44d2b3a47fdc95ccf3a2120c2817)
                check_type(argname="argument message_deduplication_id", value=message_deduplication_id, expected_type=type_hints["message_deduplication_id"])
                check_type(argname="argument message_group_id", value=message_group_id, expected_type=type_hints["message_group_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if message_deduplication_id is not None:
                self._values["message_deduplication_id"] = message_deduplication_id
            if message_group_id is not None:
                self._values["message_group_id"] = message_group_id

        @builtins.property
        def message_deduplication_id(self) -> typing.Optional[builtins.str]:
            '''This parameter applies only to FIFO (first-in-first-out) queues.

            The token used for deduplication of sent messages.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetsqsqueueparameters.html#cfn-pipes-pipe-pipetargetsqsqueueparameters-messagededuplicationid
            '''
            result = self._values.get("message_deduplication_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def message_group_id(self) -> typing.Optional[builtins.str]:
            '''The FIFO message group ID to use as the target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetsqsqueueparameters.html#cfn-pipes-pipe-pipetargetsqsqueueparameters-messagegroupid
            '''
            result = self._values.get("message_group_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PipeTargetSqsQueueParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pipes.CfnPipe.PipeTargetStateMachineParametersProperty",
        jsii_struct_bases=[],
        name_mapping={"invocation_type": "invocationType"},
    )
    class PipeTargetStateMachineParametersProperty:
        def __init__(
            self,
            *,
            invocation_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The parameters for using a Step Functions state machine as a target.

            :param invocation_type: Specify whether to invoke the Step Functions state machine synchronously or asynchronously. - ``REQUEST_RESPONSE`` (default) - Invoke synchronously. For more information, see `StartSyncExecution <https://docs.aws.amazon.com/step-functions/latest/apireference/API_StartSyncExecution.html>`_ in the *AWS Step Functions API Reference* . .. epigraph:: ``REQUEST_RESPONSE`` is not supported for ``STANDARD`` state machine workflows. - ``FIRE_AND_FORGET`` - Invoke asynchronously. For more information, see `StartExecution <https://docs.aws.amazon.com/step-functions/latest/apireference/API_StartExecution.html>`_ in the *AWS Step Functions API Reference* . For more information, see `Invocation types <https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes.html#pipes-invocation>`_ in the *Amazon EventBridge User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetstatemachineparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pipes as pipes
                
                pipe_target_state_machine_parameters_property = pipes.CfnPipe.PipeTargetStateMachineParametersProperty(
                    invocation_type="invocationType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9ec503fded11cbbc4dab0b1613c3577e5cd2103bb82744fbf161f720dcc71eea)
                check_type(argname="argument invocation_type", value=invocation_type, expected_type=type_hints["invocation_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if invocation_type is not None:
                self._values["invocation_type"] = invocation_type

        @builtins.property
        def invocation_type(self) -> typing.Optional[builtins.str]:
            '''Specify whether to invoke the Step Functions state machine synchronously or asynchronously.

            - ``REQUEST_RESPONSE`` (default) - Invoke synchronously. For more information, see `StartSyncExecution <https://docs.aws.amazon.com/step-functions/latest/apireference/API_StartSyncExecution.html>`_ in the *AWS Step Functions API Reference* .

            .. epigraph::

               ``REQUEST_RESPONSE`` is not supported for ``STANDARD`` state machine workflows.

            - ``FIRE_AND_FORGET`` - Invoke asynchronously. For more information, see `StartExecution <https://docs.aws.amazon.com/step-functions/latest/apireference/API_StartExecution.html>`_ in the *AWS Step Functions API Reference* .

            For more information, see `Invocation types <https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes.html#pipes-invocation>`_ in the *Amazon EventBridge User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-pipetargetstatemachineparameters.html#cfn-pipes-pipe-pipetargetstatemachineparameters-invocationtype
            '''
            result = self._values.get("invocation_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PipeTargetStateMachineParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pipes.CfnPipe.PlacementConstraintProperty",
        jsii_struct_bases=[],
        name_mapping={"expression": "expression", "type": "type"},
    )
    class PlacementConstraintProperty:
        def __init__(
            self,
            *,
            expression: typing.Optional[builtins.str] = None,
            type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''An object representing a constraint on task placement.

            To learn more, see `Task Placement Constraints <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html>`_ in the Amazon Elastic Container Service Developer Guide.

            :param expression: A cluster query language expression to apply to the constraint. You cannot specify an expression if the constraint type is ``distinctInstance`` . To learn more, see `Cluster Query Language <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-query-language.html>`_ in the Amazon Elastic Container Service Developer Guide.
            :param type: The type of constraint. Use distinctInstance to ensure that each task in a particular group is running on a different container instance. Use memberOf to restrict the selection to a group of valid candidates.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-placementconstraint.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pipes as pipes
                
                placement_constraint_property = pipes.CfnPipe.PlacementConstraintProperty(
                    expression="expression",
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__29749098783763739ea7f446fdc50033c069cafa812e55482d1793fc10995a4b)
                check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if expression is not None:
                self._values["expression"] = expression
            if type is not None:
                self._values["type"] = type

        @builtins.property
        def expression(self) -> typing.Optional[builtins.str]:
            '''A cluster query language expression to apply to the constraint.

            You cannot specify an expression if the constraint type is ``distinctInstance`` . To learn more, see `Cluster Query Language <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-query-language.html>`_ in the Amazon Elastic Container Service Developer Guide.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-placementconstraint.html#cfn-pipes-pipe-placementconstraint-expression
            '''
            result = self._values.get("expression")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''The type of constraint.

            Use distinctInstance to ensure that each task in a particular group is running on a different container instance. Use memberOf to restrict the selection to a group of valid candidates.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-placementconstraint.html#cfn-pipes-pipe-placementconstraint-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PlacementConstraintProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pipes.CfnPipe.PlacementStrategyProperty",
        jsii_struct_bases=[],
        name_mapping={"field": "field", "type": "type"},
    )
    class PlacementStrategyProperty:
        def __init__(
            self,
            *,
            field: typing.Optional[builtins.str] = None,
            type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The task placement strategy for a task or service.

            To learn more, see `Task Placement Strategies <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-strategies.html>`_ in the Amazon Elastic Container Service Service Developer Guide.

            :param field: The field to apply the placement strategy against. For the spread placement strategy, valid values are instanceId (or host, which has the same effect), or any platform or custom attribute that is applied to a container instance, such as attribute:ecs.availability-zone. For the binpack placement strategy, valid values are cpu and memory. For the random placement strategy, this field is not used.
            :param type: The type of placement strategy. The random placement strategy randomly places tasks on available candidates. The spread placement strategy spreads placement across available candidates evenly based on the field parameter. The binpack strategy places tasks on available candidates that have the least available amount of the resource that is specified with the field parameter. For example, if you binpack on memory, a task is placed on the instance with the least amount of remaining memory (but still enough to run the task).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-placementstrategy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pipes as pipes
                
                placement_strategy_property = pipes.CfnPipe.PlacementStrategyProperty(
                    field="field",
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__41016c173f52ab604960ddef7dd10ba081bf43fe6b79a3449b991c6e580a6b31)
                check_type(argname="argument field", value=field, expected_type=type_hints["field"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if field is not None:
                self._values["field"] = field
            if type is not None:
                self._values["type"] = type

        @builtins.property
        def field(self) -> typing.Optional[builtins.str]:
            '''The field to apply the placement strategy against.

            For the spread placement strategy, valid values are instanceId (or host, which has the same effect), or any platform or custom attribute that is applied to a container instance, such as attribute:ecs.availability-zone. For the binpack placement strategy, valid values are cpu and memory. For the random placement strategy, this field is not used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-placementstrategy.html#cfn-pipes-pipe-placementstrategy-field
            '''
            result = self._values.get("field")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''The type of placement strategy.

            The random placement strategy randomly places tasks on available candidates. The spread placement strategy spreads placement across available candidates evenly based on the field parameter. The binpack strategy places tasks on available candidates that have the least available amount of the resource that is specified with the field parameter. For example, if you binpack on memory, a task is placed on the instance with the least amount of remaining memory (but still enough to run the task).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-placementstrategy.html#cfn-pipes-pipe-placementstrategy-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PlacementStrategyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pipes.CfnPipe.S3LogDestinationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bucket_name": "bucketName",
            "bucket_owner": "bucketOwner",
            "output_format": "outputFormat",
            "prefix": "prefix",
        },
    )
    class S3LogDestinationProperty:
        def __init__(
            self,
            *,
            bucket_name: typing.Optional[builtins.str] = None,
            bucket_owner: typing.Optional[builtins.str] = None,
            output_format: typing.Optional[builtins.str] = None,
            prefix: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Represents the Amazon S3 logging configuration settings for the pipe.

            :param bucket_name: The name of the Amazon S3 bucket to which EventBridge delivers the log records for the pipe.
            :param bucket_owner: The AWS account that owns the Amazon S3 bucket to which EventBridge delivers the log records for the pipe.
            :param output_format: The format EventBridge uses for the log records. - ``json`` : JSON - ``plain`` : Plain text - ``w3c`` : `W3C extended logging file format <https://docs.aws.amazon.com/https://www.w3.org/TR/WD-logfile>`_
            :param prefix: The prefix text with which to begin Amazon S3 log object names. For more information, see `Organizing objects using prefixes <https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-prefixes.html>`_ in the *Amazon Simple Storage Service User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-s3logdestination.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pipes as pipes
                
                s3_log_destination_property = pipes.CfnPipe.S3LogDestinationProperty(
                    bucket_name="bucketName",
                    bucket_owner="bucketOwner",
                    output_format="outputFormat",
                    prefix="prefix"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7c319ecbfef3f3f4f0396c9f93fb73d31e31de12dc99872261356def9a66887b)
                check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
                check_type(argname="argument bucket_owner", value=bucket_owner, expected_type=type_hints["bucket_owner"])
                check_type(argname="argument output_format", value=output_format, expected_type=type_hints["output_format"])
                check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if bucket_name is not None:
                self._values["bucket_name"] = bucket_name
            if bucket_owner is not None:
                self._values["bucket_owner"] = bucket_owner
            if output_format is not None:
                self._values["output_format"] = output_format
            if prefix is not None:
                self._values["prefix"] = prefix

        @builtins.property
        def bucket_name(self) -> typing.Optional[builtins.str]:
            '''The name of the Amazon S3 bucket to which EventBridge delivers the log records for the pipe.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-s3logdestination.html#cfn-pipes-pipe-s3logdestination-bucketname
            '''
            result = self._values.get("bucket_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def bucket_owner(self) -> typing.Optional[builtins.str]:
            '''The AWS account that owns the Amazon S3 bucket to which EventBridge delivers the log records for the pipe.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-s3logdestination.html#cfn-pipes-pipe-s3logdestination-bucketowner
            '''
            result = self._values.get("bucket_owner")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def output_format(self) -> typing.Optional[builtins.str]:
            '''The format EventBridge uses for the log records.

            - ``json`` : JSON
            - ``plain`` : Plain text
            - ``w3c`` : `W3C extended logging file format <https://docs.aws.amazon.com/https://www.w3.org/TR/WD-logfile>`_

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-s3logdestination.html#cfn-pipes-pipe-s3logdestination-outputformat
            '''
            result = self._values.get("output_format")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def prefix(self) -> typing.Optional[builtins.str]:
            '''The prefix text with which to begin Amazon S3 log object names.

            For more information, see `Organizing objects using prefixes <https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-prefixes.html>`_ in the *Amazon Simple Storage Service User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-s3logdestination.html#cfn-pipes-pipe-s3logdestination-prefix
            '''
            result = self._values.get("prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3LogDestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pipes.CfnPipe.SageMakerPipelineParameterProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "value": "value"},
    )
    class SageMakerPipelineParameterProperty:
        def __init__(self, *, name: builtins.str, value: builtins.str) -> None:
            '''Name/Value pair of a parameter to start execution of a SageMaker Model Building Pipeline.

            :param name: Name of parameter to start execution of a SageMaker Model Building Pipeline.
            :param value: Value of parameter to start execution of a SageMaker Model Building Pipeline.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-sagemakerpipelineparameter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pipes as pipes
                
                sage_maker_pipeline_parameter_property = pipes.CfnPipe.SageMakerPipelineParameterProperty(
                    name="name",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2b7219cb450fe6061989c0273d80ba8ae6685a3c905f3de4c65a3b25e44d886a)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
                "value": value,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''Name of parameter to start execution of a SageMaker Model Building Pipeline.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-sagemakerpipelineparameter.html#cfn-pipes-pipe-sagemakerpipelineparameter-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''Value of parameter to start execution of a SageMaker Model Building Pipeline.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-sagemakerpipelineparameter.html#cfn-pipes-pipe-sagemakerpipelineparameter-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SageMakerPipelineParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pipes.CfnPipe.SelfManagedKafkaAccessConfigurationCredentialsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "basic_auth": "basicAuth",
            "client_certificate_tls_auth": "clientCertificateTlsAuth",
            "sasl_scram256_auth": "saslScram256Auth",
            "sasl_scram512_auth": "saslScram512Auth",
        },
    )
    class SelfManagedKafkaAccessConfigurationCredentialsProperty:
        def __init__(
            self,
            *,
            basic_auth: typing.Optional[builtins.str] = None,
            client_certificate_tls_auth: typing.Optional[builtins.str] = None,
            sasl_scram256_auth: typing.Optional[builtins.str] = None,
            sasl_scram512_auth: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The AWS Secrets Manager secret that stores your stream credentials.

            :param basic_auth: The ARN of the Secrets Manager secret.
            :param client_certificate_tls_auth: The ARN of the Secrets Manager secret.
            :param sasl_scram256_auth: The ARN of the Secrets Manager secret.
            :param sasl_scram512_auth: The ARN of the Secrets Manager secret.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-selfmanagedkafkaaccessconfigurationcredentials.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pipes as pipes
                
                self_managed_kafka_access_configuration_credentials_property = pipes.CfnPipe.SelfManagedKafkaAccessConfigurationCredentialsProperty(
                    basic_auth="basicAuth",
                    client_certificate_tls_auth="clientCertificateTlsAuth",
                    sasl_scram256_auth="saslScram256Auth",
                    sasl_scram512_auth="saslScram512Auth"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fbe8d3d5ef589741952141cbe10471b8f44008a53170ba93ec8d8a3945e4dcd7)
                check_type(argname="argument basic_auth", value=basic_auth, expected_type=type_hints["basic_auth"])
                check_type(argname="argument client_certificate_tls_auth", value=client_certificate_tls_auth, expected_type=type_hints["client_certificate_tls_auth"])
                check_type(argname="argument sasl_scram256_auth", value=sasl_scram256_auth, expected_type=type_hints["sasl_scram256_auth"])
                check_type(argname="argument sasl_scram512_auth", value=sasl_scram512_auth, expected_type=type_hints["sasl_scram512_auth"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if basic_auth is not None:
                self._values["basic_auth"] = basic_auth
            if client_certificate_tls_auth is not None:
                self._values["client_certificate_tls_auth"] = client_certificate_tls_auth
            if sasl_scram256_auth is not None:
                self._values["sasl_scram256_auth"] = sasl_scram256_auth
            if sasl_scram512_auth is not None:
                self._values["sasl_scram512_auth"] = sasl_scram512_auth

        @builtins.property
        def basic_auth(self) -> typing.Optional[builtins.str]:
            '''The ARN of the Secrets Manager secret.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-selfmanagedkafkaaccessconfigurationcredentials.html#cfn-pipes-pipe-selfmanagedkafkaaccessconfigurationcredentials-basicauth
            '''
            result = self._values.get("basic_auth")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def client_certificate_tls_auth(self) -> typing.Optional[builtins.str]:
            '''The ARN of the Secrets Manager secret.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-selfmanagedkafkaaccessconfigurationcredentials.html#cfn-pipes-pipe-selfmanagedkafkaaccessconfigurationcredentials-clientcertificatetlsauth
            '''
            result = self._values.get("client_certificate_tls_auth")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def sasl_scram256_auth(self) -> typing.Optional[builtins.str]:
            '''The ARN of the Secrets Manager secret.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-selfmanagedkafkaaccessconfigurationcredentials.html#cfn-pipes-pipe-selfmanagedkafkaaccessconfigurationcredentials-saslscram256auth
            '''
            result = self._values.get("sasl_scram256_auth")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def sasl_scram512_auth(self) -> typing.Optional[builtins.str]:
            '''The ARN of the Secrets Manager secret.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-selfmanagedkafkaaccessconfigurationcredentials.html#cfn-pipes-pipe-selfmanagedkafkaaccessconfigurationcredentials-saslscram512auth
            '''
            result = self._values.get("sasl_scram512_auth")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SelfManagedKafkaAccessConfigurationCredentialsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pipes.CfnPipe.SelfManagedKafkaAccessConfigurationVpcProperty",
        jsii_struct_bases=[],
        name_mapping={"security_group": "securityGroup", "subnets": "subnets"},
    )
    class SelfManagedKafkaAccessConfigurationVpcProperty:
        def __init__(
            self,
            *,
            security_group: typing.Optional[typing.Sequence[builtins.str]] = None,
            subnets: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''This structure specifies the VPC subnets and security groups for the stream, and whether a public IP address is to be used.

            :param security_group: Specifies the security groups associated with the stream. These security groups must all be in the same VPC. You can specify as many as five security groups. If you do not specify a security group, the default security group for the VPC is used.
            :param subnets: Specifies the subnets associated with the stream. These subnets must all be in the same VPC. You can specify as many as 16 subnets.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-selfmanagedkafkaaccessconfigurationvpc.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pipes as pipes
                
                self_managed_kafka_access_configuration_vpc_property = pipes.CfnPipe.SelfManagedKafkaAccessConfigurationVpcProperty(
                    security_group=["securityGroup"],
                    subnets=["subnets"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__93a7c0e9afe409ba0c90cb07ebece11a8dbddefa4be80b9479ca7514bb7dd61f)
                check_type(argname="argument security_group", value=security_group, expected_type=type_hints["security_group"])
                check_type(argname="argument subnets", value=subnets, expected_type=type_hints["subnets"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if security_group is not None:
                self._values["security_group"] = security_group
            if subnets is not None:
                self._values["subnets"] = subnets

        @builtins.property
        def security_group(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Specifies the security groups associated with the stream.

            These security groups must all be in the same VPC. You can specify as many as five security groups. If you do not specify a security group, the default security group for the VPC is used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-selfmanagedkafkaaccessconfigurationvpc.html#cfn-pipes-pipe-selfmanagedkafkaaccessconfigurationvpc-securitygroup
            '''
            result = self._values.get("security_group")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def subnets(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Specifies the subnets associated with the stream.

            These subnets must all be in the same VPC. You can specify as many as 16 subnets.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pipes-pipe-selfmanagedkafkaaccessconfigurationvpc.html#cfn-pipes-pipe-selfmanagedkafkaaccessconfigurationvpc-subnets
            '''
            result = self._values.get("subnets")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SelfManagedKafkaAccessConfigurationVpcProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_pipes.CfnPipeProps",
    jsii_struct_bases=[],
    name_mapping={
        "role_arn": "roleArn",
        "source": "source",
        "target": "target",
        "description": "description",
        "desired_state": "desiredState",
        "enrichment": "enrichment",
        "enrichment_parameters": "enrichmentParameters",
        "log_configuration": "logConfiguration",
        "name": "name",
        "source_parameters": "sourceParameters",
        "tags": "tags",
        "target_parameters": "targetParameters",
    },
)
class CfnPipeProps:
    def __init__(
        self,
        *,
        role_arn: builtins.str,
        source: builtins.str,
        target: builtins.str,
        description: typing.Optional[builtins.str] = None,
        desired_state: typing.Optional[builtins.str] = None,
        enrichment: typing.Optional[builtins.str] = None,
        enrichment_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipe.PipeEnrichmentParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        log_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipe.PipeLogConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        name: typing.Optional[builtins.str] = None,
        source_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipe.PipeSourceParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        target_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipe.PipeTargetParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnPipe``.

        :param role_arn: The ARN of the role that allows the pipe to send data to the target.
        :param source: The ARN of the source resource.
        :param target: The ARN of the target resource.
        :param description: A description of the pipe.
        :param desired_state: The state the pipe should be in.
        :param enrichment: The ARN of the enrichment resource.
        :param enrichment_parameters: The parameters required to set up enrichment on your pipe.
        :param log_configuration: The logging configuration settings for the pipe.
        :param name: The name of the pipe.
        :param source_parameters: The parameters required to set up a source for your pipe.
        :param tags: The list of key-value pairs to associate with the pipe.
        :param target_parameters: The parameters required to set up a target for your pipe. For more information about pipe target parameters, including how to use dynamic path parameters, see `Target parameters <https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes-event-target.html>`_ in the *Amazon EventBridge User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pipes-pipe.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_pipes as pipes
            
            cfn_pipe_props = pipes.CfnPipeProps(
                role_arn="roleArn",
                source="source",
                target="target",
            
                # the properties below are optional
                description="description",
                desired_state="desiredState",
                enrichment="enrichment",
                enrichment_parameters=pipes.CfnPipe.PipeEnrichmentParametersProperty(
                    http_parameters=pipes.CfnPipe.PipeEnrichmentHttpParametersProperty(
                        header_parameters={
                            "header_parameters_key": "headerParameters"
                        },
                        path_parameter_values=["pathParameterValues"],
                        query_string_parameters={
                            "query_string_parameters_key": "queryStringParameters"
                        }
                    ),
                    input_template="inputTemplate"
                ),
                log_configuration=pipes.CfnPipe.PipeLogConfigurationProperty(
                    cloudwatch_logs_log_destination=pipes.CfnPipe.CloudwatchLogsLogDestinationProperty(
                        log_group_arn="logGroupArn"
                    ),
                    firehose_log_destination=pipes.CfnPipe.FirehoseLogDestinationProperty(
                        delivery_stream_arn="deliveryStreamArn"
                    ),
                    include_execution_data=["includeExecutionData"],
                    level="level",
                    s3_log_destination=pipes.CfnPipe.S3LogDestinationProperty(
                        bucket_name="bucketName",
                        bucket_owner="bucketOwner",
                        output_format="outputFormat",
                        prefix="prefix"
                    )
                ),
                name="name",
                source_parameters=pipes.CfnPipe.PipeSourceParametersProperty(
                    active_mq_broker_parameters=pipes.CfnPipe.PipeSourceActiveMQBrokerParametersProperty(
                        credentials=pipes.CfnPipe.MQBrokerAccessCredentialsProperty(
                            basic_auth="basicAuth"
                        ),
                        queue_name="queueName",
            
                        # the properties below are optional
                        batch_size=123,
                        maximum_batching_window_in_seconds=123
                    ),
                    dynamo_db_stream_parameters=pipes.CfnPipe.PipeSourceDynamoDBStreamParametersProperty(
                        starting_position="startingPosition",
            
                        # the properties below are optional
                        batch_size=123,
                        dead_letter_config=pipes.CfnPipe.DeadLetterConfigProperty(
                            arn="arn"
                        ),
                        maximum_batching_window_in_seconds=123,
                        maximum_record_age_in_seconds=123,
                        maximum_retry_attempts=123,
                        on_partial_batch_item_failure="onPartialBatchItemFailure",
                        parallelization_factor=123
                    ),
                    filter_criteria=pipes.CfnPipe.FilterCriteriaProperty(
                        filters=[pipes.CfnPipe.FilterProperty(
                            pattern="pattern"
                        )]
                    ),
                    kinesis_stream_parameters=pipes.CfnPipe.PipeSourceKinesisStreamParametersProperty(
                        starting_position="startingPosition",
            
                        # the properties below are optional
                        batch_size=123,
                        dead_letter_config=pipes.CfnPipe.DeadLetterConfigProperty(
                            arn="arn"
                        ),
                        maximum_batching_window_in_seconds=123,
                        maximum_record_age_in_seconds=123,
                        maximum_retry_attempts=123,
                        on_partial_batch_item_failure="onPartialBatchItemFailure",
                        parallelization_factor=123,
                        starting_position_timestamp="startingPositionTimestamp"
                    ),
                    managed_streaming_kafka_parameters=pipes.CfnPipe.PipeSourceManagedStreamingKafkaParametersProperty(
                        topic_name="topicName",
            
                        # the properties below are optional
                        batch_size=123,
                        consumer_group_id="consumerGroupId",
                        credentials=pipes.CfnPipe.MSKAccessCredentialsProperty(
                            client_certificate_tls_auth="clientCertificateTlsAuth",
                            sasl_scram512_auth="saslScram512Auth"
                        ),
                        maximum_batching_window_in_seconds=123,
                        starting_position="startingPosition"
                    ),
                    rabbit_mq_broker_parameters=pipes.CfnPipe.PipeSourceRabbitMQBrokerParametersProperty(
                        credentials=pipes.CfnPipe.MQBrokerAccessCredentialsProperty(
                            basic_auth="basicAuth"
                        ),
                        queue_name="queueName",
            
                        # the properties below are optional
                        batch_size=123,
                        maximum_batching_window_in_seconds=123,
                        virtual_host="virtualHost"
                    ),
                    self_managed_kafka_parameters=pipes.CfnPipe.PipeSourceSelfManagedKafkaParametersProperty(
                        topic_name="topicName",
            
                        # the properties below are optional
                        additional_bootstrap_servers=["additionalBootstrapServers"],
                        batch_size=123,
                        consumer_group_id="consumerGroupId",
                        credentials=pipes.CfnPipe.SelfManagedKafkaAccessConfigurationCredentialsProperty(
                            basic_auth="basicAuth",
                            client_certificate_tls_auth="clientCertificateTlsAuth",
                            sasl_scram256_auth="saslScram256Auth",
                            sasl_scram512_auth="saslScram512Auth"
                        ),
                        maximum_batching_window_in_seconds=123,
                        server_root_ca_certificate="serverRootCaCertificate",
                        starting_position="startingPosition",
                        vpc=pipes.CfnPipe.SelfManagedKafkaAccessConfigurationVpcProperty(
                            security_group=["securityGroup"],
                            subnets=["subnets"]
                        )
                    ),
                    sqs_queue_parameters=pipes.CfnPipe.PipeSourceSqsQueueParametersProperty(
                        batch_size=123,
                        maximum_batching_window_in_seconds=123
                    )
                ),
                tags={
                    "tags_key": "tags"
                },
                target_parameters=pipes.CfnPipe.PipeTargetParametersProperty(
                    batch_job_parameters=pipes.CfnPipe.PipeTargetBatchJobParametersProperty(
                        job_definition="jobDefinition",
                        job_name="jobName",
            
                        # the properties below are optional
                        array_properties=pipes.CfnPipe.BatchArrayPropertiesProperty(
                            size=123
                        ),
                        container_overrides=pipes.CfnPipe.BatchContainerOverridesProperty(
                            command=["command"],
                            environment=[pipes.CfnPipe.BatchEnvironmentVariableProperty(
                                name="name",
                                value="value"
                            )],
                            instance_type="instanceType",
                            resource_requirements=[pipes.CfnPipe.BatchResourceRequirementProperty(
                                type="type",
                                value="value"
                            )]
                        ),
                        depends_on=[pipes.CfnPipe.BatchJobDependencyProperty(
                            job_id="jobId",
                            type="type"
                        )],
                        parameters={
                            "parameters_key": "parameters"
                        },
                        retry_strategy=pipes.CfnPipe.BatchRetryStrategyProperty(
                            attempts=123
                        )
                    ),
                    cloud_watch_logs_parameters=pipes.CfnPipe.PipeTargetCloudWatchLogsParametersProperty(
                        log_stream_name="logStreamName",
                        timestamp="timestamp"
                    ),
                    ecs_task_parameters=pipes.CfnPipe.PipeTargetEcsTaskParametersProperty(
                        task_definition_arn="taskDefinitionArn",
            
                        # the properties below are optional
                        capacity_provider_strategy=[pipes.CfnPipe.CapacityProviderStrategyItemProperty(
                            capacity_provider="capacityProvider",
            
                            # the properties below are optional
                            base=123,
                            weight=123
                        )],
                        enable_ecs_managed_tags=False,
                        enable_execute_command=False,
                        group="group",
                        launch_type="launchType",
                        network_configuration=pipes.CfnPipe.NetworkConfigurationProperty(
                            awsvpc_configuration=pipes.CfnPipe.AwsVpcConfigurationProperty(
                                subnets=["subnets"],
            
                                # the properties below are optional
                                assign_public_ip="assignPublicIp",
                                security_groups=["securityGroups"]
                            )
                        ),
                        overrides=pipes.CfnPipe.EcsTaskOverrideProperty(
                            container_overrides=[pipes.CfnPipe.EcsContainerOverrideProperty(
                                command=["command"],
                                cpu=123,
                                environment=[pipes.CfnPipe.EcsEnvironmentVariableProperty(
                                    name="name",
                                    value="value"
                                )],
                                environment_files=[pipes.CfnPipe.EcsEnvironmentFileProperty(
                                    type="type",
                                    value="value"
                                )],
                                memory=123,
                                memory_reservation=123,
                                name="name",
                                resource_requirements=[pipes.CfnPipe.EcsResourceRequirementProperty(
                                    type="type",
                                    value="value"
                                )]
                            )],
                            cpu="cpu",
                            ephemeral_storage=pipes.CfnPipe.EcsEphemeralStorageProperty(
                                size_in_gi_b=123
                            ),
                            execution_role_arn="executionRoleArn",
                            inference_accelerator_overrides=[pipes.CfnPipe.EcsInferenceAcceleratorOverrideProperty(
                                device_name="deviceName",
                                device_type="deviceType"
                            )],
                            memory="memory",
                            task_role_arn="taskRoleArn"
                        ),
                        placement_constraints=[pipes.CfnPipe.PlacementConstraintProperty(
                            expression="expression",
                            type="type"
                        )],
                        placement_strategy=[pipes.CfnPipe.PlacementStrategyProperty(
                            field="field",
                            type="type"
                        )],
                        platform_version="platformVersion",
                        propagate_tags="propagateTags",
                        reference_id="referenceId",
                        tags=[CfnTag(
                            key="key",
                            value="value"
                        )],
                        task_count=123
                    ),
                    event_bridge_event_bus_parameters=pipes.CfnPipe.PipeTargetEventBridgeEventBusParametersProperty(
                        detail_type="detailType",
                        endpoint_id="endpointId",
                        resources=["resources"],
                        source="source",
                        time="time"
                    ),
                    http_parameters=pipes.CfnPipe.PipeTargetHttpParametersProperty(
                        header_parameters={
                            "header_parameters_key": "headerParameters"
                        },
                        path_parameter_values=["pathParameterValues"],
                        query_string_parameters={
                            "query_string_parameters_key": "queryStringParameters"
                        }
                    ),
                    input_template="inputTemplate",
                    kinesis_stream_parameters=pipes.CfnPipe.PipeTargetKinesisStreamParametersProperty(
                        partition_key="partitionKey"
                    ),
                    lambda_function_parameters=pipes.CfnPipe.PipeTargetLambdaFunctionParametersProperty(
                        invocation_type="invocationType"
                    ),
                    redshift_data_parameters=pipes.CfnPipe.PipeTargetRedshiftDataParametersProperty(
                        database="database",
                        sqls=["sqls"],
            
                        # the properties below are optional
                        db_user="dbUser",
                        secret_manager_arn="secretManagerArn",
                        statement_name="statementName",
                        with_event=False
                    ),
                    sage_maker_pipeline_parameters=pipes.CfnPipe.PipeTargetSageMakerPipelineParametersProperty(
                        pipeline_parameter_list=[pipes.CfnPipe.SageMakerPipelineParameterProperty(
                            name="name",
                            value="value"
                        )]
                    ),
                    sqs_queue_parameters=pipes.CfnPipe.PipeTargetSqsQueueParametersProperty(
                        message_deduplication_id="messageDeduplicationId",
                        message_group_id="messageGroupId"
                    ),
                    step_function_state_machine_parameters=pipes.CfnPipe.PipeTargetStateMachineParametersProperty(
                        invocation_type="invocationType"
                    )
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6a6720db1bd2e7acc178f6bd481fd8e3e740405a24c01b669c4c4595318b8c0)
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument desired_state", value=desired_state, expected_type=type_hints["desired_state"])
            check_type(argname="argument enrichment", value=enrichment, expected_type=type_hints["enrichment"])
            check_type(argname="argument enrichment_parameters", value=enrichment_parameters, expected_type=type_hints["enrichment_parameters"])
            check_type(argname="argument log_configuration", value=log_configuration, expected_type=type_hints["log_configuration"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument source_parameters", value=source_parameters, expected_type=type_hints["source_parameters"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument target_parameters", value=target_parameters, expected_type=type_hints["target_parameters"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "role_arn": role_arn,
            "source": source,
            "target": target,
        }
        if description is not None:
            self._values["description"] = description
        if desired_state is not None:
            self._values["desired_state"] = desired_state
        if enrichment is not None:
            self._values["enrichment"] = enrichment
        if enrichment_parameters is not None:
            self._values["enrichment_parameters"] = enrichment_parameters
        if log_configuration is not None:
            self._values["log_configuration"] = log_configuration
        if name is not None:
            self._values["name"] = name
        if source_parameters is not None:
            self._values["source_parameters"] = source_parameters
        if tags is not None:
            self._values["tags"] = tags
        if target_parameters is not None:
            self._values["target_parameters"] = target_parameters

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''The ARN of the role that allows the pipe to send data to the target.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pipes-pipe.html#cfn-pipes-pipe-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source(self) -> builtins.str:
        '''The ARN of the source resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pipes-pipe.html#cfn-pipes-pipe-source
        '''
        result = self._values.get("source")
        assert result is not None, "Required property 'source' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target(self) -> builtins.str:
        '''The ARN of the target resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pipes-pipe.html#cfn-pipes-pipe-target
        '''
        result = self._values.get("target")
        assert result is not None, "Required property 'target' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the pipe.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pipes-pipe.html#cfn-pipes-pipe-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def desired_state(self) -> typing.Optional[builtins.str]:
        '''The state the pipe should be in.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pipes-pipe.html#cfn-pipes-pipe-desiredstate
        '''
        result = self._values.get("desired_state")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enrichment(self) -> typing.Optional[builtins.str]:
        '''The ARN of the enrichment resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pipes-pipe.html#cfn-pipes-pipe-enrichment
        '''
        result = self._values.get("enrichment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enrichment_parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPipe.PipeEnrichmentParametersProperty]]:
        '''The parameters required to set up enrichment on your pipe.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pipes-pipe.html#cfn-pipes-pipe-enrichmentparameters
        '''
        result = self._values.get("enrichment_parameters")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPipe.PipeEnrichmentParametersProperty]], result)

    @builtins.property
    def log_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPipe.PipeLogConfigurationProperty]]:
        '''The logging configuration settings for the pipe.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pipes-pipe.html#cfn-pipes-pipe-logconfiguration
        '''
        result = self._values.get("log_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPipe.PipeLogConfigurationProperty]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the pipe.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pipes-pipe.html#cfn-pipes-pipe-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPipe.PipeSourceParametersProperty]]:
        '''The parameters required to set up a source for your pipe.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pipes-pipe.html#cfn-pipes-pipe-sourceparameters
        '''
        result = self._values.get("source_parameters")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPipe.PipeSourceParametersProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The list of key-value pairs to associate with the pipe.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pipes-pipe.html#cfn-pipes-pipe-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def target_parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPipe.PipeTargetParametersProperty]]:
        '''The parameters required to set up a target for your pipe.

        For more information about pipe target parameters, including how to use dynamic path parameters, see `Target parameters <https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes-event-target.html>`_ in the *Amazon EventBridge User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pipes-pipe.html#cfn-pipes-pipe-targetparameters
        '''
        result = self._values.get("target_parameters")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPipe.PipeTargetParametersProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPipeProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnPipe",
    "CfnPipeProps",
]

publication.publish()

def _typecheckingstub__2590746a77e697feb25a71ec367eb957a7632f9fe5a46ae7e30476068534d683(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    role_arn: builtins.str,
    source: builtins.str,
    target: builtins.str,
    description: typing.Optional[builtins.str] = None,
    desired_state: typing.Optional[builtins.str] = None,
    enrichment: typing.Optional[builtins.str] = None,
    enrichment_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipe.PipeEnrichmentParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    log_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipe.PipeLogConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    source_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipe.PipeSourceParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    target_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipe.PipeTargetParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__281eb4cd67e1ba036145aebcc10997c29984daadd10b66bef8033e25a39f3531(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c41a04b3c491b0925941962d0b7177857e979073f71bd9b6de38556def4efe12(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__985ad2a14f580dd4275038980cbc387943f87211abf3e68fdb2f4755fdba5354(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1fe18602cacd79eabcd3ef5565eda6cf280acd9362fd60e8a8059ed4ce59822(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__727f36b3af534d289c37e337ba67c6310e4420f9572ad6bbc62222fb26ecbb05(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25b696da604f323ac1a92ddfcc7ef102957b3d092e8137378e91cea16ea39501(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ed87f6faacd73494b95f46c464263cf5f41d189f47daddc0b4607b7e1b5d9d0(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e73385dfe68409f0392cc314d936a945ec4656e8ef2f8c5b48def81168da23aa(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75aa67d8831c93b78f85f7319ad758289b207fec83baf9b92034cab4451f63d2(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPipe.PipeEnrichmentParametersProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3975e792335934f36dcb66bc10ba0ab93afe079dae88c2011a2bacc35a8fe756(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPipe.PipeLogConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e90ad70ab6477fe6112b4879f928b790cb38e40964bc2dde8bed7a3ba8008c71(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef7a2d44f21af0c5ebeb25368be2b069abd76c8c64ba1cef587c3e219c88bec1(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPipe.PipeSourceParametersProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4dba8d7cbad9d88d28d6a41b286be656a8aba98a10b5a338c7d175eab7061f25(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6b5bbabe5f41fcd217d39a2fe0a41e5a7dcac510b412ddae1d12e74d71a1995(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPipe.PipeTargetParametersProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5332578c4ac56ef4e1fdb629bb8be713eff47af3ee812e54c579d58784e9f78b(
    *,
    subnets: typing.Sequence[builtins.str],
    assign_public_ip: typing.Optional[builtins.str] = None,
    security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92192a261db9a36c55fcb7448e0173123454bca2fe715ba9d9aeb07eadf0530f(
    *,
    size: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e744d7df8a35e07450afdd20e33f3cfb5db1e9415e8c69615b236bf713417a3(
    *,
    command: typing.Optional[typing.Sequence[builtins.str]] = None,
    environment: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipe.BatchEnvironmentVariableProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    instance_type: typing.Optional[builtins.str] = None,
    resource_requirements: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipe.BatchResourceRequirementProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6e3194d0527ccc74e30382a7dd1882664fde72ee15efb33743f945bf0a54b89(
    *,
    name: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ea3de2ed5a4136d6fdec008bfc4898c56abd060a326a424ca01385c613d8a3b(
    *,
    job_id: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff7ddf004d2156fbb4d6695cf8b70ebe68fd7dbeaa600ae631bdfb7cc39c9f7c(
    *,
    type: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d623eb197750cfc3e70926318810b6905af52604196157974285f7aa990f4bd(
    *,
    attempts: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a0a6c552a3434ea82161f20199d02513f09432e81ead4005d7f813754024e4b(
    *,
    capacity_provider: builtins.str,
    base: typing.Optional[jsii.Number] = None,
    weight: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7fcaf667064eeae949a2b411c39d860bfd847c21fbdaaffccb0267266f85864(
    *,
    log_group_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c77be0d58acf260e66916991ed848b46a2c0c50751145a9186710668a20838df(
    *,
    arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2aa9c9e99af21330a73d690bfbb31c0ded547e5a62886d6682815f5910e00e65(
    *,
    command: typing.Optional[typing.Sequence[builtins.str]] = None,
    cpu: typing.Optional[jsii.Number] = None,
    environment: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipe.EcsEnvironmentVariableProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    environment_files: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipe.EcsEnvironmentFileProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    memory: typing.Optional[jsii.Number] = None,
    memory_reservation: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
    resource_requirements: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipe.EcsResourceRequirementProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01bada1fe04905f47a26a5965d040f55b22a98d3ef168a973e3a38a0c3937836(
    *,
    type: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5916c016388a7f5303579d1368d4dcbda171aeb41921023cbc0b22b49997fb59(
    *,
    name: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__caa763e1eb6274b4829763db1a11d6c4d69679f0c1c56e86833c464b209d7d2b(
    *,
    size_in_gib: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9920d06ed2da3a222b25b6b174db7eb43e6983e29183224a1b0d86f3ae79a3fc(
    *,
    device_name: typing.Optional[builtins.str] = None,
    device_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b2bd11ae2d133e2ae4a3b3bbf1130a6396a05fe6a948341ca3d1fbe22cfb752(
    *,
    type: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac29bac5fb5186aee7c9d8a3a767986fee27a65cfa4b10cb45878a777a141ee5(
    *,
    container_overrides: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipe.EcsContainerOverrideProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    cpu: typing.Optional[builtins.str] = None,
    ephemeral_storage: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipe.EcsEphemeralStorageProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    execution_role_arn: typing.Optional[builtins.str] = None,
    inference_accelerator_overrides: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipe.EcsInferenceAcceleratorOverrideProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    memory: typing.Optional[builtins.str] = None,
    task_role_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__004b9f76dd8a2c227817a517c0d05d104afc0af72ef6cb0c3c89fbc4b6c922a5(
    *,
    filters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipe.FilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f00591753ff21d2f36f1936733014c6b5ee6e0461229e20051346fba671bc2b(
    *,
    pattern: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__debe1fd10d907031fe99a3f76db2e5a127e103de0cfb29f11bf57a42822b27b1(
    *,
    delivery_stream_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1cb1a557465a40a3893ac95a9d03f8e5ebb12253739b129caf5e762c94e574c8(
    *,
    basic_auth: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46261e68c3c1fb4bc41f7b2debe372659b86c5d9845e6857c0ad7b9046c0c987(
    *,
    client_certificate_tls_auth: typing.Optional[builtins.str] = None,
    sasl_scram512_auth: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d27b7177804b8a4677a880ec362095763e2c62871f3c70d4aadd38189dedd0ac(
    *,
    awsvpc_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipe.AwsVpcConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c0ef57785475dd0f00d9483a37fb4e2993490bc25effa27f975d3eb152d45a0(
    *,
    header_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
    path_parameter_values: typing.Optional[typing.Sequence[builtins.str]] = None,
    query_string_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c41c854101e445a9a64950cf1ae31f47633329bb0e1d2188fc8a4013b114b09(
    *,
    http_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipe.PipeEnrichmentHttpParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    input_template: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__306252f91f65dd02a7e0e602af22016c4fe25b4159b0ed1f2ec374f280216abd(
    *,
    cloudwatch_logs_log_destination: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipe.CloudwatchLogsLogDestinationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    firehose_log_destination: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipe.FirehoseLogDestinationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    include_execution_data: typing.Optional[typing.Sequence[builtins.str]] = None,
    level: typing.Optional[builtins.str] = None,
    s3_log_destination: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipe.S3LogDestinationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0146fc05725151ab0272065e74d8b279e41669f4c12c21bf5b654dc4ea4e0db3(
    *,
    credentials: typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipe.MQBrokerAccessCredentialsProperty, typing.Dict[builtins.str, typing.Any]]],
    queue_name: builtins.str,
    batch_size: typing.Optional[jsii.Number] = None,
    maximum_batching_window_in_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3914232e5e779f01bede413661456f0566bb16bbb4b0a9f9e7c7abf0a20b55f(
    *,
    starting_position: builtins.str,
    batch_size: typing.Optional[jsii.Number] = None,
    dead_letter_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipe.DeadLetterConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    maximum_batching_window_in_seconds: typing.Optional[jsii.Number] = None,
    maximum_record_age_in_seconds: typing.Optional[jsii.Number] = None,
    maximum_retry_attempts: typing.Optional[jsii.Number] = None,
    on_partial_batch_item_failure: typing.Optional[builtins.str] = None,
    parallelization_factor: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b24786dafb795146de150a5ba8bedca4b5929c018392ddade565e7bf6a2a819(
    *,
    starting_position: builtins.str,
    batch_size: typing.Optional[jsii.Number] = None,
    dead_letter_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipe.DeadLetterConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    maximum_batching_window_in_seconds: typing.Optional[jsii.Number] = None,
    maximum_record_age_in_seconds: typing.Optional[jsii.Number] = None,
    maximum_retry_attempts: typing.Optional[jsii.Number] = None,
    on_partial_batch_item_failure: typing.Optional[builtins.str] = None,
    parallelization_factor: typing.Optional[jsii.Number] = None,
    starting_position_timestamp: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8fa065b1f4c1a49a0c34029f20edbcee0895067597c39e79f08e5cb70c545116(
    *,
    topic_name: builtins.str,
    batch_size: typing.Optional[jsii.Number] = None,
    consumer_group_id: typing.Optional[builtins.str] = None,
    credentials: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipe.MSKAccessCredentialsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    maximum_batching_window_in_seconds: typing.Optional[jsii.Number] = None,
    starting_position: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f69eae8cb9c31c50f3f84207511653ea968efd2ef99df30157d160dff080c77f(
    *,
    active_mq_broker_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipe.PipeSourceActiveMQBrokerParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    dynamo_db_stream_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipe.PipeSourceDynamoDBStreamParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    filter_criteria: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipe.FilterCriteriaProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    kinesis_stream_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipe.PipeSourceKinesisStreamParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    managed_streaming_kafka_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipe.PipeSourceManagedStreamingKafkaParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    rabbit_mq_broker_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipe.PipeSourceRabbitMQBrokerParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    self_managed_kafka_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipe.PipeSourceSelfManagedKafkaParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sqs_queue_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipe.PipeSourceSqsQueueParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c74f43f119c84e728ccfcb7abb732d38519873fb7ec729b9fdf249f2c0e5bddd(
    *,
    credentials: typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipe.MQBrokerAccessCredentialsProperty, typing.Dict[builtins.str, typing.Any]]],
    queue_name: builtins.str,
    batch_size: typing.Optional[jsii.Number] = None,
    maximum_batching_window_in_seconds: typing.Optional[jsii.Number] = None,
    virtual_host: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66a0aa3e5511ea04d388f45c3036c4936d03c059f1ffad52b097b33a19a33603(
    *,
    topic_name: builtins.str,
    additional_bootstrap_servers: typing.Optional[typing.Sequence[builtins.str]] = None,
    batch_size: typing.Optional[jsii.Number] = None,
    consumer_group_id: typing.Optional[builtins.str] = None,
    credentials: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipe.SelfManagedKafkaAccessConfigurationCredentialsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    maximum_batching_window_in_seconds: typing.Optional[jsii.Number] = None,
    server_root_ca_certificate: typing.Optional[builtins.str] = None,
    starting_position: typing.Optional[builtins.str] = None,
    vpc: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipe.SelfManagedKafkaAccessConfigurationVpcProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67e4be2db1ed30e406fb7818b3884b7726611e447c0cbe62b206747477440cf9(
    *,
    batch_size: typing.Optional[jsii.Number] = None,
    maximum_batching_window_in_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1cb92272e9e571b199ec86e09734d9a3e51183f8515940ff8f8fb18edb8487c(
    *,
    job_definition: builtins.str,
    job_name: builtins.str,
    array_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipe.BatchArrayPropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    container_overrides: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipe.BatchContainerOverridesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    depends_on: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipe.BatchJobDependencyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
    retry_strategy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipe.BatchRetryStrategyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9be904989c92536dbb91aa23e3469c4c06a8919cf641a798da1e9c78b51b2156(
    *,
    log_stream_name: typing.Optional[builtins.str] = None,
    timestamp: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da21f6b180d5c707968fc953abf6c9b6a20c14a97bb988159e2bff9f1252dc07(
    *,
    task_definition_arn: builtins.str,
    capacity_provider_strategy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipe.CapacityProviderStrategyItemProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    enable_ecs_managed_tags: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    enable_execute_command: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    group: typing.Optional[builtins.str] = None,
    launch_type: typing.Optional[builtins.str] = None,
    network_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipe.NetworkConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    overrides: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipe.EcsTaskOverrideProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    placement_constraints: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipe.PlacementConstraintProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    placement_strategy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipe.PlacementStrategyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    platform_version: typing.Optional[builtins.str] = None,
    propagate_tags: typing.Optional[builtins.str] = None,
    reference_id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    task_count: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4ff5c800b247e08d889440f1b30d658847593d507da887052e6a07cd035a3a8(
    *,
    detail_type: typing.Optional[builtins.str] = None,
    endpoint_id: typing.Optional[builtins.str] = None,
    resources: typing.Optional[typing.Sequence[builtins.str]] = None,
    source: typing.Optional[builtins.str] = None,
    time: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7188f5bfc90d5dba8acd880f5c8ab24cadd75972f9cc901fb933192887a73e08(
    *,
    header_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
    path_parameter_values: typing.Optional[typing.Sequence[builtins.str]] = None,
    query_string_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f6573d105d52fd2f7280462dfe30eaedfc28e7d968c7cfb9b734b2d7b3df87d(
    *,
    partition_key: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb748756b23b0347b9022c2e96a5ec829bfa9e34d4d712d757794e89d1cb2d37(
    *,
    invocation_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__165d2153d77ee319562b47678485053dec4a8dbcb94c274abe1d78488c0de760(
    *,
    batch_job_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipe.PipeTargetBatchJobParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    cloud_watch_logs_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipe.PipeTargetCloudWatchLogsParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ecs_task_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipe.PipeTargetEcsTaskParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    event_bridge_event_bus_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipe.PipeTargetEventBridgeEventBusParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    http_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipe.PipeTargetHttpParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    input_template: typing.Optional[builtins.str] = None,
    kinesis_stream_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipe.PipeTargetKinesisStreamParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    lambda_function_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipe.PipeTargetLambdaFunctionParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    redshift_data_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipe.PipeTargetRedshiftDataParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sage_maker_pipeline_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipe.PipeTargetSageMakerPipelineParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sqs_queue_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipe.PipeTargetSqsQueueParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    step_function_state_machine_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipe.PipeTargetStateMachineParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7ea6dedf4af0c373d420ab7d2ec651a184123217d353843d2015cd78c2e412a(
    *,
    database: builtins.str,
    sqls: typing.Sequence[builtins.str],
    db_user: typing.Optional[builtins.str] = None,
    secret_manager_arn: typing.Optional[builtins.str] = None,
    statement_name: typing.Optional[builtins.str] = None,
    with_event: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0605c1a90997b245e51ad3fb0e2d8178d3a57cc7250323bcd66289779b8c17b(
    *,
    pipeline_parameter_list: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipe.SageMakerPipelineParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a65dfb99d32c62fab8dad285f75fc0a48cf44d2b3a47fdc95ccf3a2120c2817(
    *,
    message_deduplication_id: typing.Optional[builtins.str] = None,
    message_group_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ec503fded11cbbc4dab0b1613c3577e5cd2103bb82744fbf161f720dcc71eea(
    *,
    invocation_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29749098783763739ea7f446fdc50033c069cafa812e55482d1793fc10995a4b(
    *,
    expression: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41016c173f52ab604960ddef7dd10ba081bf43fe6b79a3449b991c6e580a6b31(
    *,
    field: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c319ecbfef3f3f4f0396c9f93fb73d31e31de12dc99872261356def9a66887b(
    *,
    bucket_name: typing.Optional[builtins.str] = None,
    bucket_owner: typing.Optional[builtins.str] = None,
    output_format: typing.Optional[builtins.str] = None,
    prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b7219cb450fe6061989c0273d80ba8ae6685a3c905f3de4c65a3b25e44d886a(
    *,
    name: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fbe8d3d5ef589741952141cbe10471b8f44008a53170ba93ec8d8a3945e4dcd7(
    *,
    basic_auth: typing.Optional[builtins.str] = None,
    client_certificate_tls_auth: typing.Optional[builtins.str] = None,
    sasl_scram256_auth: typing.Optional[builtins.str] = None,
    sasl_scram512_auth: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93a7c0e9afe409ba0c90cb07ebece11a8dbddefa4be80b9479ca7514bb7dd61f(
    *,
    security_group: typing.Optional[typing.Sequence[builtins.str]] = None,
    subnets: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6a6720db1bd2e7acc178f6bd481fd8e3e740405a24c01b669c4c4595318b8c0(
    *,
    role_arn: builtins.str,
    source: builtins.str,
    target: builtins.str,
    description: typing.Optional[builtins.str] = None,
    desired_state: typing.Optional[builtins.str] = None,
    enrichment: typing.Optional[builtins.str] = None,
    enrichment_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipe.PipeEnrichmentParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    log_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipe.PipeLogConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    source_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipe.PipeSourceParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    target_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipe.PipeTargetParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
