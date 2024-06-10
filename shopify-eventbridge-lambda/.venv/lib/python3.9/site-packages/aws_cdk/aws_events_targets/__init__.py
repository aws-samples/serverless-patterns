'''
# Event Targets for Amazon EventBridge

This library contains integration classes to send Amazon EventBridge to any
number of supported AWS Services. Instances of these classes should be passed
to the `rule.addTarget()` method.

Currently supported are:

* [Event Targets for Amazon EventBridge](#event-targets-for-amazon-eventbridge)

  * [Event retry policy and using dead-letter queues](#event-retry-policy-and-using-dead-letter-queues)
  * [Invoke a Lambda function](#invoke-a-lambda-function)
  * [Log an event into a LogGroup](#log-an-event-into-a-loggroup)
  * [Start a CodeBuild build](#start-a-codebuild-build)
  * [Start a CodePipeline pipeline](#start-a-codepipeline-pipeline)
  * [Start a StepFunctions state machine](#start-a-stepfunctions-state-machine)
  * [Queue a Batch job](#queue-a-batch-job)
  * [Invoke an API Gateway REST API](#invoke-an-api-gateway-rest-api)
  * [Invoke an API Destination](#invoke-an-api-destination)
  * [Invoke an AppSync GraphQL API](#invoke-an-appsync-graphql-api)
  * [Put an event on an EventBridge bus](#put-an-event-on-an-eventbridge-bus)
  * [Run an ECS Task](#run-an-ecs-task)

    * [Tagging Tasks](#tagging-tasks)
    * [Launch type for ECS Task](#launch-type-for-ecs-task)
    * [Assign public IP addresses to tasks](#assign-public-ip-addresses-to-tasks)
    * [Enable Amazon ECS Exec for ECS Task](#enable-amazon-ecs-exec-for-ecs-task)

See the README of the `aws-cdk-lib/aws-events` library for more information on
EventBridge.

## Event retry policy and using dead-letter queues

The Codebuild, CodePipeline, Lambda, StepFunctions, LogGroup, SQSQueue, SNSTopic and ECSTask targets support attaching a [dead letter queue and setting retry policies](https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html). See the [lambda example](#invoke-a-lambda-function).
Use [escape hatches](https://docs.aws.amazon.com/cdk/latest/guide/cfn_layer.html) for the other target types.

## Invoke a Lambda function

Use the `LambdaFunction` target to invoke a lambda function.

The code snippet below creates an event rule with a Lambda function as a target
triggered for every events from `aws.ec2` source. You can optionally attach a
[dead letter queue](https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html).

```python
import aws_cdk.aws_lambda as lambda_


fn = lambda_.Function(self, "MyFunc",
    runtime=lambda_.Runtime.NODEJS_LATEST,
    handler="index.handler",
    code=lambda_.Code.from_inline("exports.handler = handler.toString()")
)

rule = events.Rule(self, "rule",
    event_pattern=events.EventPattern(
        source=["aws.ec2"]
    )
)

queue = sqs.Queue(self, "Queue")

rule.add_target(targets.LambdaFunction(fn,
    dead_letter_queue=queue,  # Optional: add a dead letter queue
    max_event_age=Duration.hours(2),  # Optional: set the maxEventAge retry policy
    retry_attempts=2
))
```

## Log an event into a LogGroup

Use the `LogGroup` target to log your events in a CloudWatch LogGroup.

For example, the following code snippet creates an event rule with a CloudWatch LogGroup as a target.
Every events sent from the `aws.ec2` source will be sent to the CloudWatch LogGroup.

```python
import aws_cdk.aws_logs as logs


log_group = logs.LogGroup(self, "MyLogGroup",
    log_group_name="MyLogGroup"
)

rule = events.Rule(self, "rule",
    event_pattern=events.EventPattern(
        source=["aws.ec2"]
    )
)

rule.add_target(targets.CloudWatchLogGroup(log_group))
```

A rule target input can also be specified to modify the event that is sent to the log group.
Unlike other event targets, CloudWatchLogs requires a specific input template format.

```python
import aws_cdk.aws_logs as logs
# log_group: logs.LogGroup
# rule: events.Rule


rule.add_target(targets.CloudWatchLogGroup(log_group,
    log_event=targets.LogGroupTargetInput.from_object(
        timestamp=events.EventField.from_path("$.time"),
        message=events.EventField.from_path("$.detail-type")
    )
))
```

If you want to use static values to overwrite the `message` make sure that you provide a `string`
value.

```python
import aws_cdk.aws_logs as logs
# log_group: logs.LogGroup
# rule: events.Rule


rule.add_target(targets.CloudWatchLogGroup(log_group,
    log_event=targets.LogGroupTargetInput.from_object(
        message=JSON.stringify({
            "CustomField": "CustomValue"
        })
    )
))
```

The cloudwatch log event target will create an AWS custom resource internally which will default
to set `installLatestAwsSdk` to `true`. This may be problematic for CN partition deployment. To
workaround this issue, set `installLatestAwsSdk` to `false`.

```python
import aws_cdk.aws_logs as logs
# log_group: logs.LogGroup
# rule: events.Rule


rule.add_target(targets.CloudWatchLogGroup(log_group,
    install_latest_aws_sdk=False
))
```

## Start a CodeBuild build

Use the `CodeBuildProject` target to trigger a CodeBuild project.

The code snippet below creates a CodeCommit repository that triggers a CodeBuild project
on commit to the master branch. You can optionally attach a
[dead letter queue](https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html).

```python
import aws_cdk.aws_codebuild as codebuild
import aws_cdk.aws_codecommit as codecommit


repo = codecommit.Repository(self, "MyRepo",
    repository_name="aws-cdk-codebuild-events"
)

project = codebuild.Project(self, "MyProject",
    source=codebuild.Source.code_commit(repository=repo)
)

dead_letter_queue = sqs.Queue(self, "DeadLetterQueue")

# trigger a build when a commit is pushed to the repo
on_commit_rule = repo.on_commit("OnCommit",
    target=targets.CodeBuildProject(project,
        dead_letter_queue=dead_letter_queue
    ),
    branches=["master"]
)
```

## Start a CodePipeline pipeline

Use the `CodePipeline` target to trigger a CodePipeline pipeline.

The code snippet below creates a CodePipeline pipeline that is triggered every hour

```python
import aws_cdk.aws_codepipeline as codepipeline


pipeline = codepipeline.Pipeline(self, "Pipeline")

rule = events.Rule(self, "Rule",
    schedule=events.Schedule.expression("rate(1 hour)")
)

rule.add_target(targets.CodePipeline(pipeline))
```

## Start a StepFunctions state machine

Use the `SfnStateMachine` target to trigger a State Machine.

The code snippet below creates a Simple StateMachine that is triggered every minute with a
dummy object as input.
You can optionally attach a
[dead letter queue](https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html)
to the target.

```python
import aws_cdk.aws_iam as iam
import aws_cdk.aws_stepfunctions as sfn


rule = events.Rule(self, "Rule",
    schedule=events.Schedule.rate(Duration.minutes(1))
)

dlq = sqs.Queue(self, "DeadLetterQueue")

role = iam.Role(self, "Role",
    assumed_by=iam.ServicePrincipal("events.amazonaws.com")
)
state_machine = sfn.StateMachine(self, "SM",
    definition=sfn.Wait(self, "Hello", time=sfn.WaitTime.duration(Duration.seconds(10)))
)

rule.add_target(targets.SfnStateMachine(state_machine,
    input=events.RuleTargetInput.from_object({"SomeParam": "SomeValue"}),
    dead_letter_queue=dlq,
    role=role
))
```

## Queue a Batch job

Use the `BatchJob` target to queue a Batch job.

The code snippet below creates a Simple JobQueue that is triggered every hour with a
dummy object as input.
You can optionally attach a
[dead letter queue](https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html)
to the target.

```python
import aws_cdk.aws_ec2 as ec2
import aws_cdk.aws_ecs as ecs
import aws_cdk.aws_batch as batch
from aws_cdk.aws_ecs import ContainerImage

# vpc: ec2.Vpc


compute_environment = batch.FargateComputeEnvironment(self, "ComputeEnv",
    vpc=vpc
)

job_queue = batch.JobQueue(self, "JobQueue",
    priority=1,
    compute_environments=[batch.OrderedComputeEnvironment(
        compute_environment=compute_environment,
        order=1
    )
    ]
)

job_definition = batch.EcsJobDefinition(self, "MyJob",
    container=batch.EcsEc2ContainerDefinition(self, "Container",
        image=ecs.ContainerImage.from_registry("test-repo"),
        memory=cdk.Size.mebibytes(2048),
        cpu=256
    )
)

queue = sqs.Queue(self, "Queue")

rule = events.Rule(self, "Rule",
    schedule=events.Schedule.rate(Duration.hours(1))
)

rule.add_target(targets.BatchJob(job_queue.job_queue_arn, job_queue, job_definition.job_definition_arn, job_definition,
    dead_letter_queue=queue,
    event=events.RuleTargetInput.from_object({"SomeParam": "SomeValue"}),
    retry_attempts=2,
    max_event_age=Duration.hours(2)
))
```

## Invoke an API Gateway REST API

Use the `ApiGateway` target to trigger a REST API.

The code snippet below creates a Api Gateway REST API that is invoked every hour.

```python
import aws_cdk.aws_apigateway as api
import aws_cdk.aws_lambda as lambda_


rule = events.Rule(self, "Rule",
    schedule=events.Schedule.rate(Duration.minutes(1))
)

fn = lambda_.Function(self, "MyFunc",
    handler="index.handler",
    runtime=lambda_.Runtime.NODEJS_LATEST,
    code=lambda_.Code.from_inline("exports.handler = e => {}")
)

rest_api = api.LambdaRestApi(self, "MyRestAPI", handler=fn)

dlq = sqs.Queue(self, "DeadLetterQueue")

rule.add_target(
    targets.ApiGateway(rest_api,
        path="/*/test",
        method="GET",
        stage="prod",
        path_parameter_values=["path-value"],
        header_parameters={
            "Header1": "header1"
        },
        query_string_parameters={
            "QueryParam1": "query-param-1"
        },
        dead_letter_queue=dlq
    ))
```

## Invoke an API Destination

Use the `targets.ApiDestination` target to trigger an external API. You need to
create an `events.Connection` and `events.ApiDestination` as well.

The code snippet below creates an external destination that is invoked every hour.

```python
connection = events.Connection(self, "Connection",
    authorization=events.Authorization.api_key("x-api-key", SecretValue.secrets_manager("ApiSecretName")),
    description="Connection with API Key x-api-key"
)

destination = events.ApiDestination(self, "Destination",
    connection=connection,
    endpoint="https://example.com",
    description="Calling example.com with API key x-api-key"
)

rule = events.Rule(self, "Rule",
    schedule=events.Schedule.rate(Duration.minutes(1)),
    targets=[targets.ApiDestination(destination)]
)
```

You can also import an existing connection and destination
to create additional rules:

```python
connection = events.Connection.from_event_bus_arn(self, "Connection", "arn:aws:events:us-east-1:123456789012:event-bus/EventBusName", "arn:aws:secretsmanager:us-east-1:123456789012:secret:SecretName-f3gDy9")

api_destination_arn = "arn:aws:events:us-east-1:123456789012:api-destination/DestinationName"
destination = events.ApiDestination.from_api_destination_attributes(self, "Destination", api_destination_arn=api_destination_arn, connection=connection)

rule = events.Rule(self, "OtherRule",
    schedule=events.Schedule.rate(Duration.minutes(10)),
    targets=[targets.ApiDestination(destination)]
)
```

## Invoke an AppSync GraphQL API

Use the `AppSync` target to trigger an AppSync GraphQL API. You need to
create an `AppSync.GraphqlApi` configured with `AWS_IAM` authorization mode.

The code snippet below creates an AppSync GraphQL API target that is invoked every hour, calling the `publish` mutation.

```python
import aws_cdk.aws_appsync as appsync


api = appsync.GraphqlApi(self, "api",
    name="api",
    definition=appsync.Definition.from_file("schema.graphql"),
    authorization_config=appsync.AuthorizationConfig(
        default_authorization=appsync.AuthorizationMode(authorization_type=appsync.AuthorizationType.IAM)
    )
)

rule = events.Rule(self, "Rule",
    schedule=events.Schedule.rate(cdk.Duration.hours(1))
)

rule.add_target(targets.AppSync(api,
    graph_qLOperation="mutation Publish($message: String!){ publish(message: $message) { message } }",
    variables=events.RuleTargetInput.from_object({
        "message": "hello world"
    })
))
```

You can pass an existing role with the proper permissions to be used for the target when the rule is triggered. The code snippet below uses an existing role and grants permissions to use the publish Mutation on the GraphQL API.

```python
import aws_cdk.aws_iam as iam
import aws_cdk.aws_appsync as appsync


api = appsync.GraphqlApi.from_graphql_api_attributes(self, "ImportedAPI",
    graphql_api_id="<api-id>",
    graphql_api_arn="<api-arn>",
    graph_qLEndpoint_arn="<api-endpoint-arn>",
    visibility=appsync.Visibility.GLOBAL,
    modes=[appsync.AuthorizationType.IAM]
)

rule = events.Rule(self, "Rule", schedule=events.Schedule.rate(cdk.Duration.minutes(1)))
role = iam.Role(self, "Role", assumed_by=iam.ServicePrincipal("events.amazonaws.com"))

# allow EventBridge to use the `publish` mutation
api.grant_mutation(role, "publish")

rule.add_target(targets.AppSync(api,
    graph_qLOperation="mutation Publish($message: String!){ publish(message: $message) { message } }",
    variables=events.RuleTargetInput.from_object({
        "message": "hello world"
    }),
    event_role=role
))
```

## Put an event on an EventBridge bus

Use the `EventBus` target to route event to a different EventBus.

The code snippet below creates the scheduled event rule that route events to an imported event bus.

```python
rule = events.Rule(self, "Rule",
    schedule=events.Schedule.expression("rate(1 minute)")
)

rule.add_target(targets.EventBus(
    events.EventBus.from_event_bus_arn(self, "External", "arn:aws:events:eu-west-1:999999999999:event-bus/test-bus")))
```

## Run an ECS Task

Use the `EcsTask` target to run an ECS Task.

The code snippet below creates a scheduled event rule that will run the task described in `taskDefinition` every hour.

### Tagging Tasks

By default, ECS tasks run from EventBridge targets will not have tags applied to
them. You can set the `propagateTags` field to propagate the tags set on the task
definition to the task initialized by the event trigger.

If you want to set tags independent of those applied to the TaskDefinition, you
can use the `tags` array. Both of these fields can be used together or separately
to set tags on the triggered task.

```python
import aws_cdk.aws_ecs as ecs

# cluster: ecs.ICluster
# task_definition: ecs.TaskDefinition


rule = events.Rule(self, "Rule",
    schedule=events.Schedule.rate(cdk.Duration.hours(1))
)

rule.add_target(
    targets.EcsTask(
        cluster=cluster,
        task_definition=task_definition,
        propagate_tags=ecs.PropagatedTagSource.TASK_DEFINITION,
        tags=[targets.Tag(
            key="my-tag",
            value="my-tag-value"
        )
        ]
    ))
```

### Launch type for ECS Task

By default, if `isEc2Compatible` for the `taskDefinition` is true, the EC2 type is used as
the launch type for the task, otherwise the FARGATE type.
If you want to override the default launch type, you can set the `launchType` property.

```python
import aws_cdk.aws_ecs as ecs

# cluster: ecs.ICluster
# task_definition: ecs.TaskDefinition


rule = events.Rule(self, "Rule",
    schedule=events.Schedule.rate(cdk.Duration.hours(1))
)

rule.add_target(targets.EcsTask(
    cluster=cluster,
    task_definition=task_definition,
    launch_type=ecs.LaunchType.FARGATE
))
```

### Assign public IP addresses to tasks

You can set the `assignPublicIp` flag to assign public IP addresses to tasks.
If you want to detach the public IP address from the task, you have to set the flag `false`.
You can specify the flag `true` only when the launch type is set to FARGATE.

```python
import aws_cdk.aws_ecs as ecs
import aws_cdk.aws_ec2 as ec2

# cluster: ecs.ICluster
# task_definition: ecs.TaskDefinition


rule = events.Rule(self, "Rule",
    schedule=events.Schedule.rate(cdk.Duration.hours(1))
)

rule.add_target(
    targets.EcsTask(
        cluster=cluster,
        task_definition=task_definition,
        assign_public_ip=True,
        subnet_selection=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC)
    ))
```

### Enable Amazon ECS Exec for ECS Task

If you use Amazon ECS Exec, you can run commands in or get a shell to a container running on an Amazon EC2 instance or on AWS Fargate.

```python
import aws_cdk.aws_ecs as ecs

# cluster: ecs.ICluster
# task_definition: ecs.TaskDefinition


rule = events.Rule(self, "Rule",
    schedule=events.Schedule.rate(cdk.Duration.hours(1))
)

rule.add_target(targets.EcsTask(
    cluster=cluster,
    task_definition=task_definition,
    task_count=1,
    container_overrides=[targets.ContainerOverride(
        container_name="TheContainer",
        command=["echo", events.EventField.from_path("$.detail.event")]
    )],
    enable_execute_command=True
))
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
from .. import Duration as _Duration_4839e8c3, IResource as _IResource_c80c4260
from ..aws_apigateway import (
    IRestApi as _IRestApi_1f02523d, RestApi as _RestApi_777c8238
)
from ..aws_appsync import IGraphqlApi as _IGraphqlApi_ed8270f3
from ..aws_codebuild import IProject as _IProject_aafae30a
from ..aws_codepipeline import IPipeline as _IPipeline_0931f838
from ..aws_ec2 import (
    ISecurityGroup as _ISecurityGroup_acf8a799,
    SubnetSelection as _SubnetSelection_e57d76df,
)
from ..aws_ecs import (
    FargatePlatformVersion as _FargatePlatformVersion_55d8be5c,
    ICluster as _ICluster_16cddd09,
    ITaskDefinition as _ITaskDefinition_889ba4d8,
    LaunchType as _LaunchType_6894135d,
    PropagatedTagSource as _PropagatedTagSource_ad4e874a,
)
from ..aws_events import (
    IApiDestination as _IApiDestination_44cdeedd,
    IEventBus as _IEventBus_88d13111,
    IRule as _IRule_af9e3d28,
    IRuleTarget as _IRuleTarget_7a91f454,
    RuleTargetConfig as _RuleTargetConfig_4e70fe03,
    RuleTargetInput as _RuleTargetInput_6beca786,
    RuleTargetInputProperties as _RuleTargetInputProperties_38e7b0db,
)
from ..aws_iam import (
    IRole as _IRole_235f5d8e, PolicyStatement as _PolicyStatement_0fe33853
)
from ..aws_kinesis import IStream as _IStream_4e2457d2
from ..aws_kinesisfirehose import CfnDeliveryStream as _CfnDeliveryStream_8f3b1735
from ..aws_lambda import IFunction as _IFunction_6adb0ab8
from ..aws_logs import ILogGroup as _ILogGroup_3c4fa718
from ..aws_sns import ITopic as _ITopic_9eca4852
from ..aws_sqs import IQueue as _IQueue_7ed6f679
from ..aws_stepfunctions import IStateMachine as _IStateMachine_73e8d2b0


@jsii.implements(_IRuleTarget_7a91f454)
class ApiDestination(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_events_targets.ApiDestination",
):
    '''Use an API Destination rule target.

    :exampleMetadata: infused

    Example::

        connection = events.Connection(self, "Connection",
            authorization=events.Authorization.api_key("x-api-key", SecretValue.secrets_manager("ApiSecretName")),
            description="Connection with API Key x-api-key"
        )
        
        destination = events.ApiDestination(self, "Destination",
            connection=connection,
            endpoint="https://example.com",
            description="Calling example.com with API key x-api-key"
        )
        
        rule = events.Rule(self, "Rule",
            schedule=events.Schedule.rate(Duration.minutes(1)),
            targets=[targets.ApiDestination(destination)]
        )
    '''

    def __init__(
        self,
        api_destination: _IApiDestination_44cdeedd,
        *,
        event: typing.Optional[_RuleTargetInput_6beca786] = None,
        event_role: typing.Optional[_IRole_235f5d8e] = None,
        header_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        path_parameter_values: typing.Optional[typing.Sequence[builtins.str]] = None,
        query_string_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
        max_event_age: typing.Optional[_Duration_4839e8c3] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param api_destination: -
        :param event: The event to send. Default: - the entire EventBridge event
        :param event_role: The role to assume before invoking the target. Default: - a new role will be created
        :param header_parameters: Additional headers sent to the API Destination. These are merged with headers specified on the Connection, with the headers on the Connection taking precedence. You can only specify secret values on the Connection. Default: - none
        :param path_parameter_values: Path parameters to insert in place of path wildcards (``*``). If the API destination has a wilcard in the path, these path parts will be inserted in that place. Default: - none
        :param query_string_parameters: Additional query string parameters sent to the API Destination. These are merged with headers specified on the Connection, with the headers on the Connection taking precedence. You can only specify secret values on the Connection. Default: - none
        :param dead_letter_queue: The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_. The events not successfully delivered are automatically retried for a specified period of time, depending on the retry policy of the target. If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue. Default: - no dead-letter queue
        :param max_event_age: The maximum age of a request that Lambda sends to a function for processing. Minimum value of 60. Maximum value of 86400. Default: Duration.hours(24)
        :param retry_attempts: The maximum number of times to retry when the function returns an error. Minimum value of 0. Maximum value of 185. Default: 185
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d106eb32ee82e64ee59c0904873ef15fb598d1b5613440afd038509ccbb15ea)
            check_type(argname="argument api_destination", value=api_destination, expected_type=type_hints["api_destination"])
        props = ApiDestinationProps(
            event=event,
            event_role=event_role,
            header_parameters=header_parameters,
            path_parameter_values=path_parameter_values,
            query_string_parameters=query_string_parameters,
            dead_letter_queue=dead_letter_queue,
            max_event_age=max_event_age,
            retry_attempts=retry_attempts,
        )

        jsii.create(self.__class__, self, [api_destination, props])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _rule: _IRule_af9e3d28,
        _id: typing.Optional[builtins.str] = None,
    ) -> _RuleTargetConfig_4e70fe03:
        '''Returns a RuleTarget that can be used to trigger API destinations from an EventBridge event.

        :param _rule: -
        :param _id: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7fc3c1c0cf00ea5f22f33bc5b97cb9290363f2ca57adb35a3ef3345ba3c4ee26)
            check_type(argname="argument _rule", value=_rule, expected_type=type_hints["_rule"])
            check_type(argname="argument _id", value=_id, expected_type=type_hints["_id"])
        return typing.cast(_RuleTargetConfig_4e70fe03, jsii.invoke(self, "bind", [_rule, _id]))


@jsii.implements(_IRuleTarget_7a91f454)
class ApiGateway(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_events_targets.ApiGateway",
):
    '''Use an API Gateway REST APIs as a target for Amazon EventBridge rules.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_apigateway as api
        import aws_cdk.aws_lambda as lambda_
        
        
        rule = events.Rule(self, "Rule",
            schedule=events.Schedule.rate(Duration.minutes(1))
        )
        
        fn = lambda_.Function(self, "MyFunc",
            handler="index.handler",
            runtime=lambda_.Runtime.NODEJS_LATEST,
            code=lambda_.Code.from_inline("exports.handler = e => {}")
        )
        
        rest_api = api.LambdaRestApi(self, "MyRestAPI", handler=fn)
        
        dlq = sqs.Queue(self, "DeadLetterQueue")
        
        rule.add_target(
            targets.ApiGateway(rest_api,
                path="/*/test",
                method="GET",
                stage="prod",
                path_parameter_values=["path-value"],
                header_parameters={
                    "Header1": "header1"
                },
                query_string_parameters={
                    "QueryParam1": "query-param-1"
                },
                dead_letter_queue=dlq
            ))
    '''

    def __init__(
        self,
        rest_api: _IRestApi_1f02523d,
        *,
        event_role: typing.Optional[_IRole_235f5d8e] = None,
        header_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        method: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
        path_parameter_values: typing.Optional[typing.Sequence[builtins.str]] = None,
        post_body: typing.Optional[_RuleTargetInput_6beca786] = None,
        query_string_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        stage: typing.Optional[builtins.str] = None,
        dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
        max_event_age: typing.Optional[_Duration_4839e8c3] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param rest_api: - IRestApi implementation to use as event target.
        :param event_role: The role to assume before invoking the target (i.e., the pipeline) when the given rule is triggered. Default: - a new role will be created
        :param header_parameters: The headers to be set when requesting API. Default: no header parameters
        :param method: The method for api resource invoked by the rule. Default: '*' that treated as ANY
        :param path: The api resource invoked by the rule. We can use wildcards('*') to specify the path. In that case, an equal number of real values must be specified for pathParameterValues. Default: '/'
        :param path_parameter_values: The path parameter values to be used to populate to wildcards("*") of requesting api path. Default: no path parameters
        :param post_body: This will be the post request body send to the API. Default: the entire EventBridge event
        :param query_string_parameters: The query parameters to be set when requesting API. Default: no querystring parameters
        :param stage: The deploy stage of api gateway invoked by the rule. Default: the value of deploymentStage.stageName of target api gateway.
        :param dead_letter_queue: The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_. The events not successfully delivered are automatically retried for a specified period of time, depending on the retry policy of the target. If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue. Default: - no dead-letter queue
        :param max_event_age: The maximum age of a request that Lambda sends to a function for processing. Minimum value of 60. Maximum value of 86400. Default: Duration.hours(24)
        :param retry_attempts: The maximum number of times to retry when the function returns an error. Minimum value of 0. Maximum value of 185. Default: 185
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4351ee68d84b56105dfaf7566e76bf0350931a4945a4f9e2599f6310ff34c1f4)
            check_type(argname="argument rest_api", value=rest_api, expected_type=type_hints["rest_api"])
        props = ApiGatewayProps(
            event_role=event_role,
            header_parameters=header_parameters,
            method=method,
            path=path,
            path_parameter_values=path_parameter_values,
            post_body=post_body,
            query_string_parameters=query_string_parameters,
            stage=stage,
            dead_letter_queue=dead_letter_queue,
            max_event_age=max_event_age,
            retry_attempts=retry_attempts,
        )

        jsii.create(self.__class__, self, [rest_api, props])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        rule: _IRule_af9e3d28,
        _id: typing.Optional[builtins.str] = None,
    ) -> _RuleTargetConfig_4e70fe03:
        '''Returns a RuleTarget that can be used to trigger this API Gateway REST APIs as a result from an EventBridge event.

        :param rule: -
        :param _id: -

        :see: https://docs.aws.amazon.com/eventbridge/latest/userguide/resource-based-policies-eventbridge.html#sqs-permissions
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f34d8ba93048cf243454dc97d2236199033c050fc0bbc6ff84e18fa6033ee8b0)
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
            check_type(argname="argument _id", value=_id, expected_type=type_hints["_id"])
        return typing.cast(_RuleTargetConfig_4e70fe03, jsii.invoke(self, "bind", [rule, _id]))

    @builtins.property
    @jsii.member(jsii_name="iRestApi")
    def i_rest_api(self) -> _IRestApi_1f02523d:
        '''Returns the target IRestApi.'''
        return typing.cast(_IRestApi_1f02523d, jsii.get(self, "iRestApi"))

    @builtins.property
    @jsii.member(jsii_name="restApi")
    def rest_api(self) -> _RestApi_777c8238:
        '''
        :deprecated: Use the ``iRestApi`` getter instead

        :stability: deprecated
        '''
        return typing.cast(_RestApi_777c8238, jsii.get(self, "restApi"))


@jsii.implements(_IRuleTarget_7a91f454)
class AppSync(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_events_targets.AppSync",
):
    '''Use an AppSync GraphQL API as a target for Amazon EventBridge rules.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_appsync as appsync
        
        
        api = appsync.GraphqlApi(self, "api",
            name="api",
            definition=appsync.Definition.from_file("schema.graphql"),
            authorization_config=appsync.AuthorizationConfig(
                default_authorization=appsync.AuthorizationMode(authorization_type=appsync.AuthorizationType.IAM)
            )
        )
        
        rule = events.Rule(self, "Rule",
            schedule=events.Schedule.rate(cdk.Duration.hours(1))
        )
        
        rule.add_target(targets.AppSync(api,
            graph_qLOperation="mutation Publish($message: String!){ publish(message: $message) { message } }",
            variables=events.RuleTargetInput.from_object({
                "message": "hello world"
            })
        ))
    '''

    def __init__(
        self,
        appsync_api: _IGraphqlApi_ed8270f3,
        *,
        graph_ql_operation: builtins.str,
        event_role: typing.Optional[_IRole_235f5d8e] = None,
        variables: typing.Optional[_RuleTargetInput_6beca786] = None,
        dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
        max_event_age: typing.Optional[_Duration_4839e8c3] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param appsync_api: -
        :param graph_ql_operation: The GraphQL operation; that is, the query, mutation, or subscription to be parsed and executed by the GraphQL service.
        :param event_role: The role to assume before invoking the target (i.e., the pipeline) when the given rule is triggered. Default: - a new role with permissions to access mutations will be created
        :param variables: The variables that are include in the GraphQL operation. Default: - The entire event is used
        :param dead_letter_queue: The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_. The events not successfully delivered are automatically retried for a specified period of time, depending on the retry policy of the target. If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue. Default: - no dead-letter queue
        :param max_event_age: The maximum age of a request that Lambda sends to a function for processing. Minimum value of 60. Maximum value of 86400. Default: Duration.hours(24)
        :param retry_attempts: The maximum number of times to retry when the function returns an error. Minimum value of 0. Maximum value of 185. Default: 185
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56a99cbd83a0d7a956b68eb6ee5cedd89a2b1c37754c2dc7f5a5ea2ccffb1c7f)
            check_type(argname="argument appsync_api", value=appsync_api, expected_type=type_hints["appsync_api"])
        props = AppSyncGraphQLApiProps(
            graph_ql_operation=graph_ql_operation,
            event_role=event_role,
            variables=variables,
            dead_letter_queue=dead_letter_queue,
            max_event_age=max_event_age,
            retry_attempts=retry_attempts,
        )

        jsii.create(self.__class__, self, [appsync_api, props])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        rule: _IRule_af9e3d28,
        _id: typing.Optional[builtins.str] = None,
    ) -> _RuleTargetConfig_4e70fe03:
        '''Returns a RuleTarget that can be used to trigger this AppSync GraphQL API as a result from an EventBridge event.

        :param rule: -
        :param _id: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b1999a517525e35ef54e6129e3396c11b46ecb394388d3f908c6d627c051c4f)
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
            check_type(argname="argument _id", value=_id, expected_type=type_hints["_id"])
        return typing.cast(_RuleTargetConfig_4e70fe03, jsii.invoke(self, "bind", [rule, _id]))


@jsii.implements(_IRuleTarget_7a91f454)
class AwsApi(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_events_targets.AwsApi",
):
    '''Use an AWS Lambda function that makes API calls as an event rule target.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_events_targets as events_targets
        from aws_cdk import aws_iam as iam
        
        # parameters: Any
        # policy_statement: iam.PolicyStatement
        
        aws_api = events_targets.AwsApi(
            action="action",
            service="service",
        
            # the properties below are optional
            api_version="apiVersion",
            catch_error_pattern="catchErrorPattern",
            parameters=parameters,
            policy_statement=policy_statement
        )
    '''

    def __init__(
        self,
        *,
        policy_statement: typing.Optional[_PolicyStatement_0fe33853] = None,
        action: builtins.str,
        service: builtins.str,
        api_version: typing.Optional[builtins.str] = None,
        catch_error_pattern: typing.Optional[builtins.str] = None,
        parameters: typing.Any = None,
    ) -> None:
        '''
        :param policy_statement: The IAM policy statement to allow the API call. Use only if resource restriction is needed. Default: - extract the permission from the API call
        :param action: The service action to call.
        :param service: The service to call.
        :param api_version: (deprecated) API version to use for the service.
        :param catch_error_pattern: The regex pattern to use to catch API errors. The ``code`` property of the ``Error`` object will be tested against this pattern. If there is a match an error will not be thrown. Default: - do not catch errors
        :param parameters: The parameters for the service action. Default: - no parameters
        '''
        props = AwsApiProps(
            policy_statement=policy_statement,
            action=action,
            service=service,
            api_version=api_version,
            catch_error_pattern=catch_error_pattern,
            parameters=parameters,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        rule: _IRule_af9e3d28,
        id: typing.Optional[builtins.str] = None,
    ) -> _RuleTargetConfig_4e70fe03:
        '''Returns a RuleTarget that can be used to trigger this AwsApi as a result from an EventBridge event.

        :param rule: -
        :param id: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a41bcbfd7e37d2d2cf83a8f636d325a2a328da0a83ef4d994f0be12782f7d357)
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        return typing.cast(_RuleTargetConfig_4e70fe03, jsii.invoke(self, "bind", [rule, id]))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_events_targets.AwsApiInput",
    jsii_struct_bases=[],
    name_mapping={
        "action": "action",
        "service": "service",
        "api_version": "apiVersion",
        "catch_error_pattern": "catchErrorPattern",
        "parameters": "parameters",
    },
)
class AwsApiInput:
    def __init__(
        self,
        *,
        action: builtins.str,
        service: builtins.str,
        api_version: typing.Optional[builtins.str] = None,
        catch_error_pattern: typing.Optional[builtins.str] = None,
        parameters: typing.Any = None,
    ) -> None:
        '''Rule target input for an AwsApi target.

        :param action: The service action to call.
        :param service: The service to call.
        :param api_version: (deprecated) API version to use for the service.
        :param catch_error_pattern: The regex pattern to use to catch API errors. The ``code`` property of the ``Error`` object will be tested against this pattern. If there is a match an error will not be thrown. Default: - do not catch errors
        :param parameters: The parameters for the service action. Default: - no parameters

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_events_targets as events_targets
            
            # parameters: Any
            
            aws_api_input = events_targets.AwsApiInput(
                action="action",
                service="service",
            
                # the properties below are optional
                api_version="apiVersion",
                catch_error_pattern="catchErrorPattern",
                parameters=parameters
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2fe69d44df432ded25b817ab8882c534b11b4e6a93f032091c7ab9ea0763f88)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
            check_type(argname="argument api_version", value=api_version, expected_type=type_hints["api_version"])
            check_type(argname="argument catch_error_pattern", value=catch_error_pattern, expected_type=type_hints["catch_error_pattern"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "action": action,
            "service": service,
        }
        if api_version is not None:
            self._values["api_version"] = api_version
        if catch_error_pattern is not None:
            self._values["catch_error_pattern"] = catch_error_pattern
        if parameters is not None:
            self._values["parameters"] = parameters

    @builtins.property
    def action(self) -> builtins.str:
        '''The service action to call.

        :see: https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/index.html
        '''
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service(self) -> builtins.str:
        '''The service to call.

        :see: https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/index.html
        '''
        result = self._values.get("service")
        assert result is not None, "Required property 'service' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def api_version(self) -> typing.Optional[builtins.str]:
        '''(deprecated) API version to use for the service.

        :deprecated: the handler code was migrated to AWS SDK for JavaScript v3, which does not support this feature anymore

        :stability: deprecated
        '''
        result = self._values.get("api_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def catch_error_pattern(self) -> typing.Optional[builtins.str]:
        '''The regex pattern to use to catch API errors.

        The ``code`` property of the
        ``Error`` object will be tested against this pattern. If there is a match an
        error will not be thrown.

        :default: - do not catch errors
        '''
        result = self._values.get("catch_error_pattern")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameters(self) -> typing.Any:
        '''The parameters for the service action.

        :default: - no parameters

        :see: https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/index.html
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AwsApiInput(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_events_targets.AwsApiProps",
    jsii_struct_bases=[AwsApiInput],
    name_mapping={
        "action": "action",
        "service": "service",
        "api_version": "apiVersion",
        "catch_error_pattern": "catchErrorPattern",
        "parameters": "parameters",
        "policy_statement": "policyStatement",
    },
)
class AwsApiProps(AwsApiInput):
    def __init__(
        self,
        *,
        action: builtins.str,
        service: builtins.str,
        api_version: typing.Optional[builtins.str] = None,
        catch_error_pattern: typing.Optional[builtins.str] = None,
        parameters: typing.Any = None,
        policy_statement: typing.Optional[_PolicyStatement_0fe33853] = None,
    ) -> None:
        '''Properties for an AwsApi target.

        :param action: The service action to call.
        :param service: The service to call.
        :param api_version: (deprecated) API version to use for the service.
        :param catch_error_pattern: The regex pattern to use to catch API errors. The ``code`` property of the ``Error`` object will be tested against this pattern. If there is a match an error will not be thrown. Default: - do not catch errors
        :param parameters: The parameters for the service action. Default: - no parameters
        :param policy_statement: The IAM policy statement to allow the API call. Use only if resource restriction is needed. Default: - extract the permission from the API call

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_events_targets as events_targets
            from aws_cdk import aws_iam as iam
            
            # parameters: Any
            # policy_statement: iam.PolicyStatement
            
            aws_api_props = events_targets.AwsApiProps(
                action="action",
                service="service",
            
                # the properties below are optional
                api_version="apiVersion",
                catch_error_pattern="catchErrorPattern",
                parameters=parameters,
                policy_statement=policy_statement
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0959cf5a09d52d03f2591de3b911528bd507126b7e2027cd7c4585de25301ad)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
            check_type(argname="argument api_version", value=api_version, expected_type=type_hints["api_version"])
            check_type(argname="argument catch_error_pattern", value=catch_error_pattern, expected_type=type_hints["catch_error_pattern"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument policy_statement", value=policy_statement, expected_type=type_hints["policy_statement"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "action": action,
            "service": service,
        }
        if api_version is not None:
            self._values["api_version"] = api_version
        if catch_error_pattern is not None:
            self._values["catch_error_pattern"] = catch_error_pattern
        if parameters is not None:
            self._values["parameters"] = parameters
        if policy_statement is not None:
            self._values["policy_statement"] = policy_statement

    @builtins.property
    def action(self) -> builtins.str:
        '''The service action to call.

        :see: https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/index.html
        '''
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service(self) -> builtins.str:
        '''The service to call.

        :see: https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/index.html
        '''
        result = self._values.get("service")
        assert result is not None, "Required property 'service' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def api_version(self) -> typing.Optional[builtins.str]:
        '''(deprecated) API version to use for the service.

        :deprecated: the handler code was migrated to AWS SDK for JavaScript v3, which does not support this feature anymore

        :stability: deprecated
        '''
        result = self._values.get("api_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def catch_error_pattern(self) -> typing.Optional[builtins.str]:
        '''The regex pattern to use to catch API errors.

        The ``code`` property of the
        ``Error`` object will be tested against this pattern. If there is a match an
        error will not be thrown.

        :default: - do not catch errors
        '''
        result = self._values.get("catch_error_pattern")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameters(self) -> typing.Any:
        '''The parameters for the service action.

        :default: - no parameters

        :see: https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/index.html
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Any, result)

    @builtins.property
    def policy_statement(self) -> typing.Optional[_PolicyStatement_0fe33853]:
        '''The IAM policy statement to allow the API call.

        Use only if
        resource restriction is needed.

        :default: - extract the permission from the API call
        '''
        result = self._values.get("policy_statement")
        return typing.cast(typing.Optional[_PolicyStatement_0fe33853], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AwsApiProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IRuleTarget_7a91f454)
class BatchJob(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_events_targets.BatchJob",
):
    '''Use an AWS Batch Job / Queue as an event rule target.

    Most likely the code will look something like this:
    ``new BatchJob(jobQueue.jobQueueArn, jobQueue, jobDefinition.jobDefinitionArn, jobDefinition)``

    In the future this API will be improved to be fully typed

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_ec2 as ec2
        import aws_cdk.aws_ecs as ecs
        import aws_cdk.aws_batch as batch
        from aws_cdk.aws_ecs import ContainerImage
        
        # vpc: ec2.Vpc
        
        
        compute_environment = batch.FargateComputeEnvironment(self, "ComputeEnv",
            vpc=vpc
        )
        
        job_queue = batch.JobQueue(self, "JobQueue",
            priority=1,
            compute_environments=[batch.OrderedComputeEnvironment(
                compute_environment=compute_environment,
                order=1
            )
            ]
        )
        
        job_definition = batch.EcsJobDefinition(self, "MyJob",
            container=batch.EcsEc2ContainerDefinition(self, "Container",
                image=ecs.ContainerImage.from_registry("test-repo"),
                memory=cdk.Size.mebibytes(2048),
                cpu=256
            )
        )
        
        queue = sqs.Queue(self, "Queue")
        
        rule = events.Rule(self, "Rule",
            schedule=events.Schedule.rate(Duration.hours(1))
        )
        
        rule.add_target(targets.BatchJob(job_queue.job_queue_arn, job_queue, job_definition.job_definition_arn, job_definition,
            dead_letter_queue=queue,
            event=events.RuleTargetInput.from_object({"SomeParam": "SomeValue"}),
            retry_attempts=2,
            max_event_age=Duration.hours(2)
        ))
    '''

    def __init__(
        self,
        job_queue_arn: builtins.str,
        job_queue_scope: _constructs_77d1e7e8.IConstruct,
        job_definition_arn: builtins.str,
        job_definition_scope: _constructs_77d1e7e8.IConstruct,
        *,
        attempts: typing.Optional[jsii.Number] = None,
        event: typing.Optional[_RuleTargetInput_6beca786] = None,
        job_name: typing.Optional[builtins.str] = None,
        size: typing.Optional[jsii.Number] = None,
        dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
        max_event_age: typing.Optional[_Duration_4839e8c3] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param job_queue_arn: The JobQueue arn.
        :param job_queue_scope: The JobQueue Resource.
        :param job_definition_arn: The jobDefinition arn.
        :param job_definition_scope: The JobQueue Resource.
        :param attempts: The number of times to attempt to retry, if the job fails. Valid values are 1–10. Default: no retryStrategy is set
        :param event: The event to send to the Lambda. This will be the payload sent to the Lambda Function. Default: the entire EventBridge event
        :param job_name: The name of the submitted job. Default: - Automatically generated
        :param size: The size of the array, if this is an array batch job. Valid values are integers between 2 and 10,000. Default: no arrayProperties are set
        :param dead_letter_queue: The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_. The events not successfully delivered are automatically retried for a specified period of time, depending on the retry policy of the target. If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue. Default: - no dead-letter queue
        :param max_event_age: The maximum age of a request that Lambda sends to a function for processing. Minimum value of 60. Maximum value of 86400. Default: Duration.hours(24)
        :param retry_attempts: The maximum number of times to retry when the function returns an error. Minimum value of 0. Maximum value of 185. Default: 185
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__47158c034f7c0f0c69db5367db77245ba70cbcc56ed81ec05ad80116fa6238e6)
            check_type(argname="argument job_queue_arn", value=job_queue_arn, expected_type=type_hints["job_queue_arn"])
            check_type(argname="argument job_queue_scope", value=job_queue_scope, expected_type=type_hints["job_queue_scope"])
            check_type(argname="argument job_definition_arn", value=job_definition_arn, expected_type=type_hints["job_definition_arn"])
            check_type(argname="argument job_definition_scope", value=job_definition_scope, expected_type=type_hints["job_definition_scope"])
        props = BatchJobProps(
            attempts=attempts,
            event=event,
            job_name=job_name,
            size=size,
            dead_letter_queue=dead_letter_queue,
            max_event_age=max_event_age,
            retry_attempts=retry_attempts,
        )

        jsii.create(self.__class__, self, [job_queue_arn, job_queue_scope, job_definition_arn, job_definition_scope, props])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        rule: _IRule_af9e3d28,
        _id: typing.Optional[builtins.str] = None,
    ) -> _RuleTargetConfig_4e70fe03:
        '''Returns a RuleTarget that can be used to trigger queue this batch job as a result from an EventBridge event.

        :param rule: -
        :param _id: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__154b5229eec4b919f6367b1ffec428480b40785475052bfd94fade237bd22597)
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
            check_type(argname="argument _id", value=_id, expected_type=type_hints["_id"])
        return typing.cast(_RuleTargetConfig_4e70fe03, jsii.invoke(self, "bind", [rule, _id]))


@jsii.implements(_IRuleTarget_7a91f454)
class CloudWatchLogGroup(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_events_targets.CloudWatchLogGroup",
):
    '''Use an AWS CloudWatch LogGroup as an event rule target.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_logs as logs
        # log_group: logs.LogGroup
        # rule: events.Rule
        
        
        rule.add_target(targets.CloudWatchLogGroup(log_group,
            log_event=targets.LogGroupTargetInput.from_object(
                message=JSON.stringify({
                    "CustomField": "CustomValue"
                })
            )
        ))
    '''

    def __init__(
        self,
        log_group: _ILogGroup_3c4fa718,
        *,
        event: typing.Optional[_RuleTargetInput_6beca786] = None,
        install_latest_aws_sdk: typing.Optional[builtins.bool] = None,
        log_event: typing.Optional["LogGroupTargetInput"] = None,
        dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
        max_event_age: typing.Optional[_Duration_4839e8c3] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param log_group: -
        :param event: (deprecated) The event to send to the CloudWatch LogGroup. This will be the event logged into the CloudWatch LogGroup Default: - the entire EventBridge event
        :param install_latest_aws_sdk: Whether the custom resource created wll default to install latest AWS SDK. Default: - install latest AWS SDK
        :param log_event: The event to send to the CloudWatch LogGroup. This will be the event logged into the CloudWatch LogGroup Default: - the entire EventBridge event
        :param dead_letter_queue: The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_. The events not successfully delivered are automatically retried for a specified period of time, depending on the retry policy of the target. If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue. Default: - no dead-letter queue
        :param max_event_age: The maximum age of a request that Lambda sends to a function for processing. Minimum value of 60. Maximum value of 86400. Default: Duration.hours(24)
        :param retry_attempts: The maximum number of times to retry when the function returns an error. Minimum value of 0. Maximum value of 185. Default: 185
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7cd04d50c1c36eb2be36abb3fbdf553a534c7ae5d60f1c9cac6b5cf6428d284)
            check_type(argname="argument log_group", value=log_group, expected_type=type_hints["log_group"])
        props = LogGroupProps(
            event=event,
            install_latest_aws_sdk=install_latest_aws_sdk,
            log_event=log_event,
            dead_letter_queue=dead_letter_queue,
            max_event_age=max_event_age,
            retry_attempts=retry_attempts,
        )

        jsii.create(self.__class__, self, [log_group, props])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _rule: _IRule_af9e3d28,
        _id: typing.Optional[builtins.str] = None,
    ) -> _RuleTargetConfig_4e70fe03:
        '''Returns a RuleTarget that can be used to log an event into a CloudWatch LogGroup.

        :param _rule: -
        :param _id: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5583066efc6b7b2980bfbfbf33e6491271f5faf3b97e5d2ae998d1fe4189d1d4)
            check_type(argname="argument _rule", value=_rule, expected_type=type_hints["_rule"])
            check_type(argname="argument _id", value=_id, expected_type=type_hints["_id"])
        return typing.cast(_RuleTargetConfig_4e70fe03, jsii.invoke(self, "bind", [_rule, _id]))


@jsii.implements(_IRuleTarget_7a91f454)
class CodeBuildProject(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_events_targets.CodeBuildProject",
):
    '''Start a CodeBuild build when an Amazon EventBridge rule is triggered.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_sns as sns
        import aws_cdk.aws_events_targets as targets
        
        # repo: codecommit.Repository
        # project: codebuild.PipelineProject
        # my_topic: sns.Topic
        
        
        # starts a CodeBuild project when a commit is pushed to the "main" branch of the repo
        repo.on_commit("CommitToMain",
            target=targets.CodeBuildProject(project),
            branches=["main"]
        )
        
        # publishes a message to an Amazon SNS topic when a comment is made on a pull request
        rule = repo.on_comment_on_pull_request("CommentOnPullRequest",
            target=targets.SnsTopic(my_topic)
        )
    '''

    def __init__(
        self,
        project: _IProject_aafae30a,
        *,
        event: typing.Optional[_RuleTargetInput_6beca786] = None,
        event_role: typing.Optional[_IRole_235f5d8e] = None,
        dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
        max_event_age: typing.Optional[_Duration_4839e8c3] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param project: -
        :param event: The event to send to CodeBuild. This will be the payload for the StartBuild API. Default: - the entire EventBridge event
        :param event_role: The role to assume before invoking the target (i.e., the codebuild) when the given rule is triggered. Default: - a new role will be created
        :param dead_letter_queue: The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_. The events not successfully delivered are automatically retried for a specified period of time, depending on the retry policy of the target. If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue. Default: - no dead-letter queue
        :param max_event_age: The maximum age of a request that Lambda sends to a function for processing. Minimum value of 60. Maximum value of 86400. Default: Duration.hours(24)
        :param retry_attempts: The maximum number of times to retry when the function returns an error. Minimum value of 0. Maximum value of 185. Default: 185
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a8679d207265b7ec6863cf63c5b8aaaa8577dce8b9b2c6ec8d9a52c6bde44f1)
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
        props = CodeBuildProjectProps(
            event=event,
            event_role=event_role,
            dead_letter_queue=dead_letter_queue,
            max_event_age=max_event_age,
            retry_attempts=retry_attempts,
        )

        jsii.create(self.__class__, self, [project, props])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _rule: _IRule_af9e3d28,
        _id: typing.Optional[builtins.str] = None,
    ) -> _RuleTargetConfig_4e70fe03:
        '''Allows using build projects as event rule targets.

        :param _rule: -
        :param _id: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c864909db0683c496942d72c9b834b03e1082bec9e20c368a204df37449c6e48)
            check_type(argname="argument _rule", value=_rule, expected_type=type_hints["_rule"])
            check_type(argname="argument _id", value=_id, expected_type=type_hints["_id"])
        return typing.cast(_RuleTargetConfig_4e70fe03, jsii.invoke(self, "bind", [_rule, _id]))


@jsii.implements(_IRuleTarget_7a91f454)
class CodePipeline(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_events_targets.CodePipeline",
):
    '''Allows the pipeline to be used as an EventBridge rule target.

    :exampleMetadata: infused

    Example::

        # A pipeline being used as a target for a CloudWatch event rule.
        import aws_cdk.aws_events_targets as targets
        import aws_cdk.aws_events as events
        
        # pipeline: codepipeline.Pipeline
        
        
        # kick off the pipeline every day
        rule = events.Rule(self, "Daily",
            schedule=events.Schedule.rate(Duration.days(1))
        )
        rule.add_target(targets.CodePipeline(pipeline))
    '''

    def __init__(
        self,
        pipeline: _IPipeline_0931f838,
        *,
        event_role: typing.Optional[_IRole_235f5d8e] = None,
        dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
        max_event_age: typing.Optional[_Duration_4839e8c3] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param pipeline: -
        :param event_role: The role to assume before invoking the target (i.e., the pipeline) when the given rule is triggered. Default: - a new role will be created
        :param dead_letter_queue: The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_. The events not successfully delivered are automatically retried for a specified period of time, depending on the retry policy of the target. If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue. Default: - no dead-letter queue
        :param max_event_age: The maximum age of a request that Lambda sends to a function for processing. Minimum value of 60. Maximum value of 86400. Default: Duration.hours(24)
        :param retry_attempts: The maximum number of times to retry when the function returns an error. Minimum value of 0. Maximum value of 185. Default: 185
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__daa7b4e77a0ef964ea3cdb54ce57cc8f475d7342b57d85f348e63fff7e5ecc14)
            check_type(argname="argument pipeline", value=pipeline, expected_type=type_hints["pipeline"])
        options = CodePipelineTargetOptions(
            event_role=event_role,
            dead_letter_queue=dead_letter_queue,
            max_event_age=max_event_age,
            retry_attempts=retry_attempts,
        )

        jsii.create(self.__class__, self, [pipeline, options])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _rule: _IRule_af9e3d28,
        _id: typing.Optional[builtins.str] = None,
    ) -> _RuleTargetConfig_4e70fe03:
        '''Returns the rule target specification.

        NOTE: Do not use the various ``inputXxx`` options. They can be set in a call to ``addTarget``.

        :param _rule: -
        :param _id: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__add42f3c28d5f6651e451885b955fd84ad865300b4e6606be36174db4f3d8c73)
            check_type(argname="argument _rule", value=_rule, expected_type=type_hints["_rule"])
            check_type(argname="argument _id", value=_id, expected_type=type_hints["_id"])
        return typing.cast(_RuleTargetConfig_4e70fe03, jsii.invoke(self, "bind", [_rule, _id]))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_events_targets.ContainerOverride",
    jsii_struct_bases=[],
    name_mapping={
        "container_name": "containerName",
        "command": "command",
        "cpu": "cpu",
        "environment": "environment",
        "memory_limit": "memoryLimit",
        "memory_reservation": "memoryReservation",
    },
)
class ContainerOverride:
    def __init__(
        self,
        *,
        container_name: builtins.str,
        command: typing.Optional[typing.Sequence[builtins.str]] = None,
        cpu: typing.Optional[jsii.Number] = None,
        environment: typing.Optional[typing.Sequence[typing.Union["TaskEnvironmentVariable", typing.Dict[builtins.str, typing.Any]]]] = None,
        memory_limit: typing.Optional[jsii.Number] = None,
        memory_reservation: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param container_name: Name of the container inside the task definition.
        :param command: Command to run inside the container. Default: Default command
        :param cpu: The number of cpu units reserved for the container. Default: The default value from the task definition.
        :param environment: Variables to set in the container's environment.
        :param memory_limit: Hard memory limit on the container. Default: The default value from the task definition.
        :param memory_reservation: Soft memory limit on the container. Default: The default value from the task definition.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_events_targets as events_targets
            
            container_override = events_targets.ContainerOverride(
                container_name="containerName",
            
                # the properties below are optional
                command=["command"],
                cpu=123,
                environment=[events_targets.TaskEnvironmentVariable(
                    name="name",
                    value="value"
                )],
                memory_limit=123,
                memory_reservation=123
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c13bb1641d81a866856c7cdeae6fa612e09bb941bc83053a19b901e3040ba066)
            check_type(argname="argument container_name", value=container_name, expected_type=type_hints["container_name"])
            check_type(argname="argument command", value=command, expected_type=type_hints["command"])
            check_type(argname="argument cpu", value=cpu, expected_type=type_hints["cpu"])
            check_type(argname="argument environment", value=environment, expected_type=type_hints["environment"])
            check_type(argname="argument memory_limit", value=memory_limit, expected_type=type_hints["memory_limit"])
            check_type(argname="argument memory_reservation", value=memory_reservation, expected_type=type_hints["memory_reservation"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "container_name": container_name,
        }
        if command is not None:
            self._values["command"] = command
        if cpu is not None:
            self._values["cpu"] = cpu
        if environment is not None:
            self._values["environment"] = environment
        if memory_limit is not None:
            self._values["memory_limit"] = memory_limit
        if memory_reservation is not None:
            self._values["memory_reservation"] = memory_reservation

    @builtins.property
    def container_name(self) -> builtins.str:
        '''Name of the container inside the task definition.'''
        result = self._values.get("container_name")
        assert result is not None, "Required property 'container_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def command(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Command to run inside the container.

        :default: Default command
        '''
        result = self._values.get("command")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def cpu(self) -> typing.Optional[jsii.Number]:
        '''The number of cpu units reserved for the container.

        :default: The default value from the task definition.
        '''
        result = self._values.get("cpu")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def environment(self) -> typing.Optional[typing.List["TaskEnvironmentVariable"]]:
        '''Variables to set in the container's environment.'''
        result = self._values.get("environment")
        return typing.cast(typing.Optional[typing.List["TaskEnvironmentVariable"]], result)

    @builtins.property
    def memory_limit(self) -> typing.Optional[jsii.Number]:
        '''Hard memory limit on the container.

        :default: The default value from the task definition.
        '''
        result = self._values.get("memory_limit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def memory_reservation(self) -> typing.Optional[jsii.Number]:
        '''Soft memory limit on the container.

        :default: The default value from the task definition.
        '''
        result = self._values.get("memory_reservation")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerOverride(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IRuleTarget_7a91f454)
class EcsTask(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_events_targets.EcsTask",
):
    '''Start a task on an ECS cluster.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_ecs as ecs
        import aws_cdk.aws_ec2 as ec2
        
        # cluster: ecs.ICluster
        # task_definition: ecs.TaskDefinition
        
        
        rule = events.Rule(self, "Rule",
            schedule=events.Schedule.rate(cdk.Duration.hours(1))
        )
        
        rule.add_target(
            targets.EcsTask(
                cluster=cluster,
                task_definition=task_definition,
                assign_public_ip=True,
                subnet_selection=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC)
            ))
    '''

    def __init__(
        self,
        *,
        cluster: _ICluster_16cddd09,
        task_definition: _ITaskDefinition_889ba4d8,
        assign_public_ip: typing.Optional[builtins.bool] = None,
        container_overrides: typing.Optional[typing.Sequence[typing.Union[ContainerOverride, typing.Dict[builtins.str, typing.Any]]]] = None,
        enable_execute_command: typing.Optional[builtins.bool] = None,
        launch_type: typing.Optional[_LaunchType_6894135d] = None,
        platform_version: typing.Optional[_FargatePlatformVersion_55d8be5c] = None,
        propagate_tags: typing.Optional[_PropagatedTagSource_ad4e874a] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
        security_groups: typing.Optional[typing.Sequence[_ISecurityGroup_acf8a799]] = None,
        subnet_selection: typing.Optional[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["Tag", typing.Dict[builtins.str, typing.Any]]]] = None,
        task_count: typing.Optional[jsii.Number] = None,
        dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
        max_event_age: typing.Optional[_Duration_4839e8c3] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param cluster: Cluster where service will be deployed.
        :param task_definition: Task Definition of the task that should be started.
        :param assign_public_ip: Specifies whether the task's elastic network interface receives a public IP address. You can specify true only when LaunchType is set to FARGATE. Default: - true if the subnet type is PUBLIC, otherwise false
        :param container_overrides: Container setting overrides. Key is the name of the container to override, value is the values you want to override.
        :param enable_execute_command: Whether or not to enable the execute command functionality for the containers in this task. If true, this enables execute command functionality on all containers in the task. Default: - false
        :param launch_type: Specifies the launch type on which your task is running. The launch type that you specify here must match one of the launch type (compatibilities) of the target task. Default: - 'EC2' if ``isEc2Compatible`` for the ``taskDefinition`` is true, otherwise 'FARGATE'
        :param platform_version: The platform version on which to run your task. Unless you have specific compatibility requirements, you don't need to specify this. Default: - ECS will set the Fargate platform version to 'LATEST'
        :param propagate_tags: Specifies whether to propagate the tags from the task definition to the task. If no value is specified, the tags are not propagated. Default: - Tags will not be propagated
        :param role: Existing IAM role to run the ECS task. Default: A new IAM role is created
        :param security_groups: Existing security groups to use for the task's ENIs. (Only applicable in case the TaskDefinition is configured for AwsVpc networking) Default: A new security group is created
        :param subnet_selection: In what subnets to place the task's ENIs. (Only applicable in case the TaskDefinition is configured for AwsVpc networking) Default: Private subnets
        :param tags: The metadata that you apply to the task to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Default: - No additional tags are applied to the task
        :param task_count: How many tasks should be started when this event is triggered. Default: 1
        :param dead_letter_queue: The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_. The events not successfully delivered are automatically retried for a specified period of time, depending on the retry policy of the target. If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue. Default: - no dead-letter queue
        :param max_event_age: The maximum age of a request that Lambda sends to a function for processing. Minimum value of 60. Maximum value of 86400. Default: Duration.hours(24)
        :param retry_attempts: The maximum number of times to retry when the function returns an error. Minimum value of 0. Maximum value of 185. Default: 185
        '''
        props = EcsTaskProps(
            cluster=cluster,
            task_definition=task_definition,
            assign_public_ip=assign_public_ip,
            container_overrides=container_overrides,
            enable_execute_command=enable_execute_command,
            launch_type=launch_type,
            platform_version=platform_version,
            propagate_tags=propagate_tags,
            role=role,
            security_groups=security_groups,
            subnet_selection=subnet_selection,
            tags=tags,
            task_count=task_count,
            dead_letter_queue=dead_letter_queue,
            max_event_age=max_event_age,
            retry_attempts=retry_attempts,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _rule: _IRule_af9e3d28,
        _id: typing.Optional[builtins.str] = None,
    ) -> _RuleTargetConfig_4e70fe03:
        '''Allows using tasks as target of EventBridge events.

        :param _rule: -
        :param _id: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ad199a8641f171a0447e974756bbddd91b00aaa9bcf33d231826916b85b8166)
            check_type(argname="argument _rule", value=_rule, expected_type=type_hints["_rule"])
            check_type(argname="argument _id", value=_id, expected_type=type_hints["_id"])
        return typing.cast(_RuleTargetConfig_4e70fe03, jsii.invoke(self, "bind", [_rule, _id]))

    @builtins.property
    @jsii.member(jsii_name="securityGroups")
    def security_groups(self) -> typing.Optional[typing.List[_ISecurityGroup_acf8a799]]:
        '''The security groups associated with the task.

        Only applicable with awsvpc network mode.

        :default: - A new security group is created.
        '''
        return typing.cast(typing.Optional[typing.List[_ISecurityGroup_acf8a799]], jsii.get(self, "securityGroups"))


@jsii.implements(_IRuleTarget_7a91f454)
class EventBus(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_events_targets.EventBus",
):
    '''Notify an existing Event Bus of an event.

    :exampleMetadata: infused

    Example::

        rule = events.Rule(self, "Rule",
            schedule=events.Schedule.expression("rate(1 minute)")
        )
        
        rule.add_target(targets.EventBus(
            events.EventBus.from_event_bus_arn(self, "External", "arn:aws:events:eu-west-1:999999999999:event-bus/test-bus")))
    '''

    def __init__(
        self,
        event_bus: _IEventBus_88d13111,
        *,
        dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
    ) -> None:
        '''
        :param event_bus: -
        :param dead_letter_queue: The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_. The events not successfully delivered are automatically retried for a specified period of time, depending on the retry policy of the target. If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue. Default: - no dead-letter queue
        :param role: Role to be used to publish the event. Default: a new role is created.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6012a31db9ac91c35876daca0265cba4fbb81bfdf8acd148b62786503371d52)
            check_type(argname="argument event_bus", value=event_bus, expected_type=type_hints["event_bus"])
        props = EventBusProps(dead_letter_queue=dead_letter_queue, role=role)

        jsii.create(self.__class__, self, [event_bus, props])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        rule: _IRule_af9e3d28,
        _id: typing.Optional[builtins.str] = None,
    ) -> _RuleTargetConfig_4e70fe03:
        '''Returns the rule target specification.

        NOTE: Do not use the various ``inputXxx`` options. They can be set in a call to ``addTarget``.

        :param rule: -
        :param _id: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00d16e4ddfa6305196a715a56432c551f3ba5a905dead2e6a85f30bad692c31f)
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
            check_type(argname="argument _id", value=_id, expected_type=type_hints["_id"])
        return typing.cast(_RuleTargetConfig_4e70fe03, jsii.invoke(self, "bind", [rule, _id]))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_events_targets.EventBusProps",
    jsii_struct_bases=[],
    name_mapping={"dead_letter_queue": "deadLetterQueue", "role": "role"},
)
class EventBusProps:
    def __init__(
        self,
        *,
        dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
    ) -> None:
        '''Configuration properties of an Event Bus event.

        Cannot extend TargetBaseProps. Retry policy is not supported for Event bus targets.

        :param dead_letter_queue: The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_. The events not successfully delivered are automatically retried for a specified period of time, depending on the retry policy of the target. If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue. Default: - no dead-letter queue
        :param role: Role to be used to publish the event. Default: a new role is created.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_events_targets as events_targets
            from aws_cdk import aws_iam as iam
            from aws_cdk import aws_sqs as sqs
            
            # queue: sqs.Queue
            # role: iam.Role
            
            event_bus_props = events_targets.EventBusProps(
                dead_letter_queue=queue,
                role=role
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5af20e134873490c1ac4788761972ccd53cd625edbd9b75c1c1f0b1a334b56ba)
            check_type(argname="argument dead_letter_queue", value=dead_letter_queue, expected_type=type_hints["dead_letter_queue"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if dead_letter_queue is not None:
            self._values["dead_letter_queue"] = dead_letter_queue
        if role is not None:
            self._values["role"] = role

    @builtins.property
    def dead_letter_queue(self) -> typing.Optional[_IQueue_7ed6f679]:
        '''The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_.

        The events not successfully delivered are automatically retried for a specified period of time,
        depending on the retry policy of the target.
        If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue.

        :default: - no dead-letter queue
        '''
        result = self._values.get("dead_letter_queue")
        return typing.cast(typing.Optional[_IQueue_7ed6f679], result)

    @builtins.property
    def role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''Role to be used to publish the event.

        :default: a new role is created.
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventBusProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.aws_events_targets.IDeliveryStream")
class IDeliveryStream(_IResource_c80c4260, typing_extensions.Protocol):
    '''Represents a Kinesis Data Firehose delivery stream.'''

    @builtins.property
    @jsii.member(jsii_name="deliveryStreamArn")
    def delivery_stream_arn(self) -> builtins.str:
        '''The ARN of the delivery stream.

        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="deliveryStreamName")
    def delivery_stream_name(self) -> builtins.str:
        '''The name of the delivery stream.

        :attribute: true
        '''
        ...


class _IDeliveryStreamProxy(
    jsii.proxy_for(_IResource_c80c4260), # type: ignore[misc]
):
    '''Represents a Kinesis Data Firehose delivery stream.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_events_targets.IDeliveryStream"

    @builtins.property
    @jsii.member(jsii_name="deliveryStreamArn")
    def delivery_stream_arn(self) -> builtins.str:
        '''The ARN of the delivery stream.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "deliveryStreamArn"))

    @builtins.property
    @jsii.member(jsii_name="deliveryStreamName")
    def delivery_stream_name(self) -> builtins.str:
        '''The name of the delivery stream.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "deliveryStreamName"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDeliveryStream).__jsii_proxy_class__ = lambda : _IDeliveryStreamProxy


@jsii.implements(_IRuleTarget_7a91f454)
class KinesisFirehoseStream(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_events_targets.KinesisFirehoseStream",
):
    '''(deprecated) Customize the Firehose Stream Event Target.

    :deprecated: Use KinesisFirehoseStreamV2

    :stability: deprecated
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_events as events
        from aws_cdk import aws_events_targets as events_targets
        from aws_cdk import aws_kinesisfirehose as kinesisfirehose
        
        # cfn_delivery_stream: kinesisfirehose.CfnDeliveryStream
        # rule_target_input: events.RuleTargetInput
        
        kinesis_firehose_stream = events_targets.KinesisFirehoseStream(cfn_delivery_stream,
            message=rule_target_input
        )
    '''

    def __init__(
        self,
        stream: _CfnDeliveryStream_8f3b1735,
        *,
        message: typing.Optional[_RuleTargetInput_6beca786] = None,
    ) -> None:
        '''
        :param stream: -
        :param message: The message to send to the stream. Must be a valid JSON text passed to the target stream. Default: - the entire Event Bridge event

        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6dba8ed5e351380147a927ce30f4c9095bc69a54a2de45039c2a1d8275dc88c)
            check_type(argname="argument stream", value=stream, expected_type=type_hints["stream"])
        props = KinesisFirehoseStreamProps(message=message)

        jsii.create(self.__class__, self, [stream, props])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _rule: _IRule_af9e3d28,
        _id: typing.Optional[builtins.str] = None,
    ) -> _RuleTargetConfig_4e70fe03:
        '''(deprecated) Returns a RuleTarget that can be used to trigger this Firehose Stream as a result from a Event Bridge event.

        :param _rule: -
        :param _id: -

        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b38a65da97645536b57df6537ab7a5b06cf8910d4235008699171e7ced62c584)
            check_type(argname="argument _rule", value=_rule, expected_type=type_hints["_rule"])
            check_type(argname="argument _id", value=_id, expected_type=type_hints["_id"])
        return typing.cast(_RuleTargetConfig_4e70fe03, jsii.invoke(self, "bind", [_rule, _id]))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_events_targets.KinesisFirehoseStreamProps",
    jsii_struct_bases=[],
    name_mapping={"message": "message"},
)
class KinesisFirehoseStreamProps:
    def __init__(
        self,
        *,
        message: typing.Optional[_RuleTargetInput_6beca786] = None,
    ) -> None:
        '''Customize the Firehose Stream Event Target.

        :param message: The message to send to the stream. Must be a valid JSON text passed to the target stream. Default: - the entire Event Bridge event

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_events as events
            from aws_cdk import aws_events_targets as events_targets
            
            # rule_target_input: events.RuleTargetInput
            
            kinesis_firehose_stream_props = events_targets.KinesisFirehoseStreamProps(
                message=rule_target_input
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81d5bbf50681705e8fea422823feb918a4c9bd4be7914a6acf6200ac65c3aa81)
            check_type(argname="argument message", value=message, expected_type=type_hints["message"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if message is not None:
            self._values["message"] = message

    @builtins.property
    def message(self) -> typing.Optional[_RuleTargetInput_6beca786]:
        '''The message to send to the stream.

        Must be a valid JSON text passed to the target stream.

        :default: - the entire Event Bridge event
        '''
        result = self._values.get("message")
        return typing.cast(typing.Optional[_RuleTargetInput_6beca786], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseStreamProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IRuleTarget_7a91f454)
class KinesisFirehoseStreamV2(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_events_targets.KinesisFirehoseStreamV2",
):
    '''Customize the Firehose Stream Event Target V2 to support L2 Kinesis Delivery Stream instead of L1 Cfn Kinesis Delivery Stream.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_events as events
        from aws_cdk import aws_events_targets as events_targets
        
        # delivery_stream: events_targets.IDeliveryStream
        # rule_target_input: events.RuleTargetInput
        
        kinesis_firehose_stream_v2 = events_targets.KinesisFirehoseStreamV2(delivery_stream,
            message=rule_target_input
        )
    '''

    def __init__(
        self,
        stream: IDeliveryStream,
        *,
        message: typing.Optional[_RuleTargetInput_6beca786] = None,
    ) -> None:
        '''
        :param stream: -
        :param message: The message to send to the stream. Must be a valid JSON text passed to the target stream. Default: - the entire Event Bridge event
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8230487c5e79599a4ad63af004c2c8350c2b25e209491350274d38019afa418)
            check_type(argname="argument stream", value=stream, expected_type=type_hints["stream"])
        props = KinesisFirehoseStreamProps(message=message)

        jsii.create(self.__class__, self, [stream, props])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _rule: _IRule_af9e3d28,
        _id: typing.Optional[builtins.str] = None,
    ) -> _RuleTargetConfig_4e70fe03:
        '''Returns a RuleTarget that can be used to trigger this Firehose Stream as a result from a Event Bridge event.

        :param _rule: -
        :param _id: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3467ab0e593ed64d775dafc3b3fc1b1835fa2853c7ee8685668bf081dd189e44)
            check_type(argname="argument _rule", value=_rule, expected_type=type_hints["_rule"])
            check_type(argname="argument _id", value=_id, expected_type=type_hints["_id"])
        return typing.cast(_RuleTargetConfig_4e70fe03, jsii.invoke(self, "bind", [_rule, _id]))


@jsii.implements(_IRuleTarget_7a91f454)
class KinesisStream(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_events_targets.KinesisStream",
):
    '''Use a Kinesis Stream as a target for AWS CloudWatch event rules.

    Example::

        # put to a Kinesis stream every time code is committed
        # to a CodeCommit repository
        repository.on_commit("onCommit", target=targets.KinesisStream(stream))
    '''

    def __init__(
        self,
        stream: _IStream_4e2457d2,
        *,
        message: typing.Optional[_RuleTargetInput_6beca786] = None,
        partition_key_path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param stream: -
        :param message: The message to send to the stream. Must be a valid JSON text passed to the target stream. Default: - the entire CloudWatch event
        :param partition_key_path: Partition Key Path for records sent to this stream. Default: - eventId as the partition key
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__47a9d917a1971c5aa11b68bf823d9f34a57a7b1e7653b0f82809c06309cac1a6)
            check_type(argname="argument stream", value=stream, expected_type=type_hints["stream"])
        props = KinesisStreamProps(
            message=message, partition_key_path=partition_key_path
        )

        jsii.create(self.__class__, self, [stream, props])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _rule: _IRule_af9e3d28,
        _id: typing.Optional[builtins.str] = None,
    ) -> _RuleTargetConfig_4e70fe03:
        '''Returns a RuleTarget that can be used to trigger this Kinesis Stream as a result from a CloudWatch event.

        :param _rule: -
        :param _id: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae222f596f043d31f56819c2cb64c58ef12e8e3d35bce41fa6f0cd929c2db58a)
            check_type(argname="argument _rule", value=_rule, expected_type=type_hints["_rule"])
            check_type(argname="argument _id", value=_id, expected_type=type_hints["_id"])
        return typing.cast(_RuleTargetConfig_4e70fe03, jsii.invoke(self, "bind", [_rule, _id]))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_events_targets.KinesisStreamProps",
    jsii_struct_bases=[],
    name_mapping={"message": "message", "partition_key_path": "partitionKeyPath"},
)
class KinesisStreamProps:
    def __init__(
        self,
        *,
        message: typing.Optional[_RuleTargetInput_6beca786] = None,
        partition_key_path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Customize the Kinesis Stream Event Target.

        :param message: The message to send to the stream. Must be a valid JSON text passed to the target stream. Default: - the entire CloudWatch event
        :param partition_key_path: Partition Key Path for records sent to this stream. Default: - eventId as the partition key

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_events as events
            from aws_cdk import aws_events_targets as events_targets
            
            # rule_target_input: events.RuleTargetInput
            
            kinesis_stream_props = events_targets.KinesisStreamProps(
                message=rule_target_input,
                partition_key_path="partitionKeyPath"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__971b6fc6dc302be6b6401547a0731521d858936fe589a0d096ef25e81e707b46)
            check_type(argname="argument message", value=message, expected_type=type_hints["message"])
            check_type(argname="argument partition_key_path", value=partition_key_path, expected_type=type_hints["partition_key_path"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if message is not None:
            self._values["message"] = message
        if partition_key_path is not None:
            self._values["partition_key_path"] = partition_key_path

    @builtins.property
    def message(self) -> typing.Optional[_RuleTargetInput_6beca786]:
        '''The message to send to the stream.

        Must be a valid JSON text passed to the target stream.

        :default: - the entire CloudWatch event
        '''
        result = self._values.get("message")
        return typing.cast(typing.Optional[_RuleTargetInput_6beca786], result)

    @builtins.property
    def partition_key_path(self) -> typing.Optional[builtins.str]:
        '''Partition Key Path for records sent to this stream.

        :default: - eventId as the partition key
        '''
        result = self._values.get("partition_key_path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisStreamProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IRuleTarget_7a91f454)
class LambdaFunction(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_events_targets.LambdaFunction",
):
    '''Use an AWS Lambda function as an event rule target.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_lambda as lambda_
        
        
        fn = lambda_.Function(self, "MyFunc",
            runtime=lambda_.Runtime.NODEJS_LATEST,
            handler="index.handler",
            code=lambda_.Code.from_inline("exports.handler = handler.toString()")
        )
        
        rule = events.Rule(self, "rule",
            event_pattern=events.EventPattern(
                source=["aws.ec2"]
            )
        )
        
        queue = sqs.Queue(self, "Queue")
        
        rule.add_target(targets.LambdaFunction(fn,
            dead_letter_queue=queue,  # Optional: add a dead letter queue
            max_event_age=Duration.hours(2),  # Optional: set the maxEventAge retry policy
            retry_attempts=2
        ))
    '''

    def __init__(
        self,
        handler: _IFunction_6adb0ab8,
        *,
        event: typing.Optional[_RuleTargetInput_6beca786] = None,
        dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
        max_event_age: typing.Optional[_Duration_4839e8c3] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param handler: -
        :param event: The event to send to the Lambda. This will be the payload sent to the Lambda Function. Default: the entire EventBridge event
        :param dead_letter_queue: The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_. The events not successfully delivered are automatically retried for a specified period of time, depending on the retry policy of the target. If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue. Default: - no dead-letter queue
        :param max_event_age: The maximum age of a request that Lambda sends to a function for processing. Minimum value of 60. Maximum value of 86400. Default: Duration.hours(24)
        :param retry_attempts: The maximum number of times to retry when the function returns an error. Minimum value of 0. Maximum value of 185. Default: 185
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ed39c6222adc3f41ac8913ef4f7e22134443e2aa19c19114f6650e1d987c3c4)
            check_type(argname="argument handler", value=handler, expected_type=type_hints["handler"])
        props = LambdaFunctionProps(
            event=event,
            dead_letter_queue=dead_letter_queue,
            max_event_age=max_event_age,
            retry_attempts=retry_attempts,
        )

        jsii.create(self.__class__, self, [handler, props])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        rule: _IRule_af9e3d28,
        _id: typing.Optional[builtins.str] = None,
    ) -> _RuleTargetConfig_4e70fe03:
        '''Returns a RuleTarget that can be used to trigger this Lambda as a result from an EventBridge event.

        :param rule: -
        :param _id: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__906b4fb6301e027a5cc5111944bf8d3844e211a5f528e71002c42bebd068aad6)
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
            check_type(argname="argument _id", value=_id, expected_type=type_hints["_id"])
        return typing.cast(_RuleTargetConfig_4e70fe03, jsii.invoke(self, "bind", [rule, _id]))


class LogGroupTargetInput(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="aws-cdk-lib.aws_events_targets.LogGroupTargetInput",
):
    '''The input to send to the CloudWatch LogGroup target.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_logs as logs
        # log_group: logs.LogGroup
        # rule: events.Rule
        
        
        rule.add_target(targets.CloudWatchLogGroup(log_group,
            log_event=targets.LogGroupTargetInput.from_object(
                timestamp=events.EventField.from_path("$.time"),
                message=events.EventField.from_path("$.detail-type")
            )
        ))
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="fromObject")
    @builtins.classmethod
    def from_object(
        cls,
        *,
        message: typing.Any = None,
        timestamp: typing.Any = None,
    ) -> _RuleTargetInput_6beca786:
        '''Pass a JSON object to the the log group event target.

        May contain strings returned by ``EventField.from()`` to substitute in parts of the
        matched event.

        :param message: The value provided here will be used in the Log "message" field. This field must be a string. If an object is passed (e.g. JSON data) it will not throw an error, but the message that makes it to CloudWatch logs will be incorrect. This is a likely scenario if doing something like: EventField.fromPath('$.detail') since in most cases the ``detail`` field contains JSON data. Default: EventField.detailType
        :param timestamp: The timestamp that will appear in the CloudWatch Logs record. Default: EventField.time
        '''
        options = LogGroupTargetInputOptions(message=message, timestamp=timestamp)

        return typing.cast(_RuleTargetInput_6beca786, jsii.sinvoke(cls, "fromObject", [options]))

    @jsii.member(jsii_name="bind")
    @abc.abstractmethod
    def bind(self, rule: _IRule_af9e3d28) -> _RuleTargetInputProperties_38e7b0db:
        '''Return the input properties for this input object.

        :param rule: -
        '''
        ...


class _LogGroupTargetInputProxy(LogGroupTargetInput):
    @jsii.member(jsii_name="bind")
    def bind(self, rule: _IRule_af9e3d28) -> _RuleTargetInputProperties_38e7b0db:
        '''Return the input properties for this input object.

        :param rule: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__758083b81fe2898a867779bb9918a1aaa26f0291624b27f0e1637860027d86a5)
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
        return typing.cast(_RuleTargetInputProperties_38e7b0db, jsii.invoke(self, "bind", [rule]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, LogGroupTargetInput).__jsii_proxy_class__ = lambda : _LogGroupTargetInputProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_events_targets.LogGroupTargetInputOptions",
    jsii_struct_bases=[],
    name_mapping={"message": "message", "timestamp": "timestamp"},
)
class LogGroupTargetInputOptions:
    def __init__(
        self,
        *,
        message: typing.Any = None,
        timestamp: typing.Any = None,
    ) -> None:
        '''Options used when creating a target input template.

        :param message: The value provided here will be used in the Log "message" field. This field must be a string. If an object is passed (e.g. JSON data) it will not throw an error, but the message that makes it to CloudWatch logs will be incorrect. This is a likely scenario if doing something like: EventField.fromPath('$.detail') since in most cases the ``detail`` field contains JSON data. Default: EventField.detailType
        :param timestamp: The timestamp that will appear in the CloudWatch Logs record. Default: EventField.time

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_logs as logs
            # log_group: logs.LogGroup
            # rule: events.Rule
            
            
            rule.add_target(targets.CloudWatchLogGroup(log_group,
                log_event=targets.LogGroupTargetInput.from_object(
                    timestamp=events.EventField.from_path("$.time"),
                    message=events.EventField.from_path("$.detail-type")
                )
            ))
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12b2a1770edaa7f8ba5d731e85339d65d757aa25fd54d6c6be4746c6a4f4a070)
            check_type(argname="argument message", value=message, expected_type=type_hints["message"])
            check_type(argname="argument timestamp", value=timestamp, expected_type=type_hints["timestamp"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if message is not None:
            self._values["message"] = message
        if timestamp is not None:
            self._values["timestamp"] = timestamp

    @builtins.property
    def message(self) -> typing.Any:
        '''The value provided here will be used in the Log "message" field.

        This field must be a string. If an object is passed (e.g. JSON data)
        it will not throw an error, but the message that makes it to
        CloudWatch logs will be incorrect. This is a likely scenario if
        doing something like: EventField.fromPath('$.detail') since in most cases
        the ``detail`` field contains JSON data.

        :default: EventField.detailType
        '''
        result = self._values.get("message")
        return typing.cast(typing.Any, result)

    @builtins.property
    def timestamp(self) -> typing.Any:
        '''The timestamp that will appear in the CloudWatch Logs record.

        :default: EventField.time
        '''
        result = self._values.get("timestamp")
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogGroupTargetInputOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IRuleTarget_7a91f454)
class SfnStateMachine(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_events_targets.SfnStateMachine",
):
    '''Use a StepFunctions state machine as a target for Amazon EventBridge rules.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_iam as iam
        import aws_cdk.aws_stepfunctions as sfn
        
        
        rule = events.Rule(self, "Rule",
            schedule=events.Schedule.rate(Duration.minutes(1))
        )
        
        dlq = sqs.Queue(self, "DeadLetterQueue")
        
        role = iam.Role(self, "Role",
            assumed_by=iam.ServicePrincipal("events.amazonaws.com")
        )
        state_machine = sfn.StateMachine(self, "SM",
            definition=sfn.Wait(self, "Hello", time=sfn.WaitTime.duration(Duration.seconds(10)))
        )
        
        rule.add_target(targets.SfnStateMachine(state_machine,
            input=events.RuleTargetInput.from_object({"SomeParam": "SomeValue"}),
            dead_letter_queue=dlq,
            role=role
        ))
    '''

    def __init__(
        self,
        machine: _IStateMachine_73e8d2b0,
        *,
        input: typing.Optional[_RuleTargetInput_6beca786] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
        dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
        max_event_age: typing.Optional[_Duration_4839e8c3] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param machine: -
        :param input: The input to the state machine execution. Default: the entire EventBridge event
        :param role: The IAM role to be assumed to execute the State Machine. Default: - a new role will be created
        :param dead_letter_queue: The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_. The events not successfully delivered are automatically retried for a specified period of time, depending on the retry policy of the target. If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue. Default: - no dead-letter queue
        :param max_event_age: The maximum age of a request that Lambda sends to a function for processing. Minimum value of 60. Maximum value of 86400. Default: Duration.hours(24)
        :param retry_attempts: The maximum number of times to retry when the function returns an error. Minimum value of 0. Maximum value of 185. Default: 185
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__257316eeebae5ef658a5b570361035fdfb5ab37e96962b24c2e814b0702cba68)
            check_type(argname="argument machine", value=machine, expected_type=type_hints["machine"])
        props = SfnStateMachineProps(
            input=input,
            role=role,
            dead_letter_queue=dead_letter_queue,
            max_event_age=max_event_age,
            retry_attempts=retry_attempts,
        )

        jsii.create(self.__class__, self, [machine, props])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _rule: _IRule_af9e3d28,
        _id: typing.Optional[builtins.str] = None,
    ) -> _RuleTargetConfig_4e70fe03:
        '''Returns a properties that are used in an Rule to trigger this State Machine.

        :param _rule: -
        :param _id: -

        :see: https://docs.aws.amazon.com/eventbridge/latest/userguide/resource-based-policies-eventbridge.html#sns-permissions
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e0733fbe09a8310edfc7237ca759e925b3db6d25ad43627fcf4f165c2efe942)
            check_type(argname="argument _rule", value=_rule, expected_type=type_hints["_rule"])
            check_type(argname="argument _id", value=_id, expected_type=type_hints["_id"])
        return typing.cast(_RuleTargetConfig_4e70fe03, jsii.invoke(self, "bind", [_rule, _id]))

    @builtins.property
    @jsii.member(jsii_name="machine")
    def machine(self) -> _IStateMachine_73e8d2b0:
        return typing.cast(_IStateMachine_73e8d2b0, jsii.get(self, "machine"))


@jsii.implements(_IRuleTarget_7a91f454)
class SnsTopic(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_events_targets.SnsTopic",
):
    '''Use an SNS topic as a target for Amazon EventBridge rules.

    If the topic is imported the required permissions to publish to that topic need to be set manually.

    Example::

        # publish to an SNS topic every time code is committed
        # to a CodeCommit repository
        repository.on_commit("onCommit", target=targets.SnsTopic(topic))
    '''

    def __init__(
        self,
        topic: _ITopic_9eca4852,
        *,
        message: typing.Optional[_RuleTargetInput_6beca786] = None,
        dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
        max_event_age: typing.Optional[_Duration_4839e8c3] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param topic: -
        :param message: The message to send to the topic. Default: the entire EventBridge event
        :param dead_letter_queue: The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_. The events not successfully delivered are automatically retried for a specified period of time, depending on the retry policy of the target. If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue. Default: - no dead-letter queue
        :param max_event_age: The maximum age of a request that Lambda sends to a function for processing. Minimum value of 60. Maximum value of 86400. Default: Duration.hours(24)
        :param retry_attempts: The maximum number of times to retry when the function returns an error. Minimum value of 0. Maximum value of 185. Default: 185
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b58aa74b2a717b90ef291556746b786df8882b8158b4b3255bf88691dbd8fd07)
            check_type(argname="argument topic", value=topic, expected_type=type_hints["topic"])
        props = SnsTopicProps(
            message=message,
            dead_letter_queue=dead_letter_queue,
            max_event_age=max_event_age,
            retry_attempts=retry_attempts,
        )

        jsii.create(self.__class__, self, [topic, props])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _rule: _IRule_af9e3d28,
        _id: typing.Optional[builtins.str] = None,
    ) -> _RuleTargetConfig_4e70fe03:
        '''Returns a RuleTarget that can be used to trigger this SNS topic as a result from an EventBridge event.

        :param _rule: -
        :param _id: -

        :see: https://docs.aws.amazon.com/eventbridge/latest/userguide/resource-based-policies-eventbridge.html#sns-permissions
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6de2339b649dec356056a716737bfe488b0873abee2d224f4a18f7ad162d83f6)
            check_type(argname="argument _rule", value=_rule, expected_type=type_hints["_rule"])
            check_type(argname="argument _id", value=_id, expected_type=type_hints["_id"])
        return typing.cast(_RuleTargetConfig_4e70fe03, jsii.invoke(self, "bind", [_rule, _id]))

    @builtins.property
    @jsii.member(jsii_name="topic")
    def topic(self) -> _ITopic_9eca4852:
        return typing.cast(_ITopic_9eca4852, jsii.get(self, "topic"))


@jsii.implements(_IRuleTarget_7a91f454)
class SqsQueue(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_events_targets.SqsQueue",
):
    '''Use an SQS Queue as a target for Amazon EventBridge rules.

    Example::

        # publish to an SQS queue every time code is committed
        # to a CodeCommit repository
        repository.on_commit("onCommit", target=targets.SqsQueue(queue))
    '''

    def __init__(
        self,
        queue: _IQueue_7ed6f679,
        *,
        message: typing.Optional[_RuleTargetInput_6beca786] = None,
        message_group_id: typing.Optional[builtins.str] = None,
        dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
        max_event_age: typing.Optional[_Duration_4839e8c3] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param queue: -
        :param message: The message to send to the queue. Must be a valid JSON text passed to the target queue. Default: the entire EventBridge event
        :param message_group_id: Message Group ID for messages sent to this queue. Required for FIFO queues, leave empty for regular queues. Default: - no message group ID (regular queue)
        :param dead_letter_queue: The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_. The events not successfully delivered are automatically retried for a specified period of time, depending on the retry policy of the target. If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue. Default: - no dead-letter queue
        :param max_event_age: The maximum age of a request that Lambda sends to a function for processing. Minimum value of 60. Maximum value of 86400. Default: Duration.hours(24)
        :param retry_attempts: The maximum number of times to retry when the function returns an error. Minimum value of 0. Maximum value of 185. Default: 185
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26484816bdcb2fef6d100370a28b06c1fd038591b98fcbe847383a51245c79f9)
            check_type(argname="argument queue", value=queue, expected_type=type_hints["queue"])
        props = SqsQueueProps(
            message=message,
            message_group_id=message_group_id,
            dead_letter_queue=dead_letter_queue,
            max_event_age=max_event_age,
            retry_attempts=retry_attempts,
        )

        jsii.create(self.__class__, self, [queue, props])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        rule: _IRule_af9e3d28,
        _id: typing.Optional[builtins.str] = None,
    ) -> _RuleTargetConfig_4e70fe03:
        '''Returns a RuleTarget that can be used to trigger this SQS queue as a result from an EventBridge event.

        :param rule: -
        :param _id: -

        :see: https://docs.aws.amazon.com/eventbridge/latest/userguide/resource-based-policies-eventbridge.html#sqs-permissions
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7bbb7c546d67f5f999da3b2a71dc36c03ae5d8723a592b50de5b0193d62ebe6)
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
            check_type(argname="argument _id", value=_id, expected_type=type_hints["_id"])
        return typing.cast(_RuleTargetConfig_4e70fe03, jsii.invoke(self, "bind", [rule, _id]))

    @builtins.property
    @jsii.member(jsii_name="queue")
    def queue(self) -> _IQueue_7ed6f679:
        return typing.cast(_IQueue_7ed6f679, jsii.get(self, "queue"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_events_targets.Tag",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "value": "value"},
)
class Tag:
    def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
        '''Metadata that you apply to a resource to help categorize and organize the resource.

        Each tag consists of a key and an optional value, both of which you define.

        :param key: Key is the name of the tag.
        :param value: Value is the metadata contents of the tag.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_events_targets as events_targets
            
            tag = events_targets.Tag(
                key="key",
                value="value"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a813f48d70b31d8149568e4c733eee0b3ddf93c3d8ee22172032406da2f91b10)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
            "value": value,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Key is the name of the tag.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Value is the metadata contents of the tag.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Tag(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_events_targets.TargetBaseProps",
    jsii_struct_bases=[],
    name_mapping={
        "dead_letter_queue": "deadLetterQueue",
        "max_event_age": "maxEventAge",
        "retry_attempts": "retryAttempts",
    },
)
class TargetBaseProps:
    def __init__(
        self,
        *,
        dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
        max_event_age: typing.Optional[_Duration_4839e8c3] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''The generic properties for an RuleTarget.

        :param dead_letter_queue: The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_. The events not successfully delivered are automatically retried for a specified period of time, depending on the retry policy of the target. If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue. Default: - no dead-letter queue
        :param max_event_age: The maximum age of a request that Lambda sends to a function for processing. Minimum value of 60. Maximum value of 86400. Default: Duration.hours(24)
        :param retry_attempts: The maximum number of times to retry when the function returns an error. Minimum value of 0. Maximum value of 185. Default: 185

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk as cdk
            from aws_cdk import aws_events_targets as events_targets
            from aws_cdk import aws_sqs as sqs
            
            # queue: sqs.Queue
            
            target_base_props = events_targets.TargetBaseProps(
                dead_letter_queue=queue,
                max_event_age=cdk.Duration.minutes(30),
                retry_attempts=123
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c149bf0de902d492c0a50daf03a233ef8286c2fb8799f305c9e4b91ffc8d577)
            check_type(argname="argument dead_letter_queue", value=dead_letter_queue, expected_type=type_hints["dead_letter_queue"])
            check_type(argname="argument max_event_age", value=max_event_age, expected_type=type_hints["max_event_age"])
            check_type(argname="argument retry_attempts", value=retry_attempts, expected_type=type_hints["retry_attempts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if dead_letter_queue is not None:
            self._values["dead_letter_queue"] = dead_letter_queue
        if max_event_age is not None:
            self._values["max_event_age"] = max_event_age
        if retry_attempts is not None:
            self._values["retry_attempts"] = retry_attempts

    @builtins.property
    def dead_letter_queue(self) -> typing.Optional[_IQueue_7ed6f679]:
        '''The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_.

        The events not successfully delivered are automatically retried for a specified period of time,
        depending on the retry policy of the target.
        If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue.

        :default: - no dead-letter queue
        '''
        result = self._values.get("dead_letter_queue")
        return typing.cast(typing.Optional[_IQueue_7ed6f679], result)

    @builtins.property
    def max_event_age(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The maximum age of a request that Lambda sends to a function for processing.

        Minimum value of 60.
        Maximum value of 86400.

        :default: Duration.hours(24)
        '''
        result = self._values.get("max_event_age")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def retry_attempts(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of times to retry when the function returns an error.

        Minimum value of 0.
        Maximum value of 185.

        :default: 185
        '''
        result = self._values.get("retry_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TargetBaseProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_events_targets.TaskEnvironmentVariable",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "value": "value"},
)
class TaskEnvironmentVariable:
    def __init__(self, *, name: builtins.str, value: builtins.str) -> None:
        '''An environment variable to be set in the container run as a task.

        :param name: Name for the environment variable. Exactly one of ``name`` and ``namePath`` must be specified.
        :param value: Value of the environment variable. Exactly one of ``value`` and ``valuePath`` must be specified.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_events_targets as events_targets
            
            task_environment_variable = events_targets.TaskEnvironmentVariable(
                name="name",
                value="value"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad8ad9cb08b1d9914f8ba21360b8735e425827635478e4e057a6f1dc9f660930)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "value": value,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Name for the environment variable.

        Exactly one of ``name`` and ``namePath`` must be specified.
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Value of the environment variable.

        Exactly one of ``value`` and ``valuePath`` must be specified.
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TaskEnvironmentVariable(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_events_targets.ApiDestinationProps",
    jsii_struct_bases=[TargetBaseProps],
    name_mapping={
        "dead_letter_queue": "deadLetterQueue",
        "max_event_age": "maxEventAge",
        "retry_attempts": "retryAttempts",
        "event": "event",
        "event_role": "eventRole",
        "header_parameters": "headerParameters",
        "path_parameter_values": "pathParameterValues",
        "query_string_parameters": "queryStringParameters",
    },
)
class ApiDestinationProps(TargetBaseProps):
    def __init__(
        self,
        *,
        dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
        max_event_age: typing.Optional[_Duration_4839e8c3] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
        event: typing.Optional[_RuleTargetInput_6beca786] = None,
        event_role: typing.Optional[_IRole_235f5d8e] = None,
        header_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        path_parameter_values: typing.Optional[typing.Sequence[builtins.str]] = None,
        query_string_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Customize the EventBridge Api Destinations Target.

        :param dead_letter_queue: The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_. The events not successfully delivered are automatically retried for a specified period of time, depending on the retry policy of the target. If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue. Default: - no dead-letter queue
        :param max_event_age: The maximum age of a request that Lambda sends to a function for processing. Minimum value of 60. Maximum value of 86400. Default: Duration.hours(24)
        :param retry_attempts: The maximum number of times to retry when the function returns an error. Minimum value of 0. Maximum value of 185. Default: 185
        :param event: The event to send. Default: - the entire EventBridge event
        :param event_role: The role to assume before invoking the target. Default: - a new role will be created
        :param header_parameters: Additional headers sent to the API Destination. These are merged with headers specified on the Connection, with the headers on the Connection taking precedence. You can only specify secret values on the Connection. Default: - none
        :param path_parameter_values: Path parameters to insert in place of path wildcards (``*``). If the API destination has a wilcard in the path, these path parts will be inserted in that place. Default: - none
        :param query_string_parameters: Additional query string parameters sent to the API Destination. These are merged with headers specified on the Connection, with the headers on the Connection taking precedence. You can only specify secret values on the Connection. Default: - none

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk as cdk
            from aws_cdk import aws_events as events
            from aws_cdk import aws_events_targets as events_targets
            from aws_cdk import aws_iam as iam
            from aws_cdk import aws_sqs as sqs
            
            # queue: sqs.Queue
            # role: iam.Role
            # rule_target_input: events.RuleTargetInput
            
            api_destination_props = events_targets.ApiDestinationProps(
                dead_letter_queue=queue,
                event=rule_target_input,
                event_role=role,
                header_parameters={
                    "header_parameters_key": "headerParameters"
                },
                max_event_age=cdk.Duration.minutes(30),
                path_parameter_values=["pathParameterValues"],
                query_string_parameters={
                    "query_string_parameters_key": "queryStringParameters"
                },
                retry_attempts=123
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a7e2f14909f24e23bf0efd9e767b25ab4257897a69dccc79351ad4456fe857a)
            check_type(argname="argument dead_letter_queue", value=dead_letter_queue, expected_type=type_hints["dead_letter_queue"])
            check_type(argname="argument max_event_age", value=max_event_age, expected_type=type_hints["max_event_age"])
            check_type(argname="argument retry_attempts", value=retry_attempts, expected_type=type_hints["retry_attempts"])
            check_type(argname="argument event", value=event, expected_type=type_hints["event"])
            check_type(argname="argument event_role", value=event_role, expected_type=type_hints["event_role"])
            check_type(argname="argument header_parameters", value=header_parameters, expected_type=type_hints["header_parameters"])
            check_type(argname="argument path_parameter_values", value=path_parameter_values, expected_type=type_hints["path_parameter_values"])
            check_type(argname="argument query_string_parameters", value=query_string_parameters, expected_type=type_hints["query_string_parameters"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if dead_letter_queue is not None:
            self._values["dead_letter_queue"] = dead_letter_queue
        if max_event_age is not None:
            self._values["max_event_age"] = max_event_age
        if retry_attempts is not None:
            self._values["retry_attempts"] = retry_attempts
        if event is not None:
            self._values["event"] = event
        if event_role is not None:
            self._values["event_role"] = event_role
        if header_parameters is not None:
            self._values["header_parameters"] = header_parameters
        if path_parameter_values is not None:
            self._values["path_parameter_values"] = path_parameter_values
        if query_string_parameters is not None:
            self._values["query_string_parameters"] = query_string_parameters

    @builtins.property
    def dead_letter_queue(self) -> typing.Optional[_IQueue_7ed6f679]:
        '''The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_.

        The events not successfully delivered are automatically retried for a specified period of time,
        depending on the retry policy of the target.
        If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue.

        :default: - no dead-letter queue
        '''
        result = self._values.get("dead_letter_queue")
        return typing.cast(typing.Optional[_IQueue_7ed6f679], result)

    @builtins.property
    def max_event_age(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The maximum age of a request that Lambda sends to a function for processing.

        Minimum value of 60.
        Maximum value of 86400.

        :default: Duration.hours(24)
        '''
        result = self._values.get("max_event_age")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def retry_attempts(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of times to retry when the function returns an error.

        Minimum value of 0.
        Maximum value of 185.

        :default: 185
        '''
        result = self._values.get("retry_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def event(self) -> typing.Optional[_RuleTargetInput_6beca786]:
        '''The event to send.

        :default: - the entire EventBridge event
        '''
        result = self._values.get("event")
        return typing.cast(typing.Optional[_RuleTargetInput_6beca786], result)

    @builtins.property
    def event_role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''The role to assume before invoking the target.

        :default: - a new role will be created
        '''
        result = self._values.get("event_role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    @builtins.property
    def header_parameters(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional headers sent to the API Destination.

        These are merged with headers specified on the Connection, with
        the headers on the Connection taking precedence.

        You can only specify secret values on the Connection.

        :default: - none
        '''
        result = self._values.get("header_parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def path_parameter_values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Path parameters to insert in place of path wildcards (``*``).

        If the API destination has a wilcard in the path, these path parts
        will be inserted in that place.

        :default: - none
        '''
        result = self._values.get("path_parameter_values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def query_string_parameters(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional query string parameters sent to the API Destination.

        These are merged with headers specified on the Connection, with
        the headers on the Connection taking precedence.

        You can only specify secret values on the Connection.

        :default: - none
        '''
        result = self._values.get("query_string_parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiDestinationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_events_targets.ApiGatewayProps",
    jsii_struct_bases=[TargetBaseProps],
    name_mapping={
        "dead_letter_queue": "deadLetterQueue",
        "max_event_age": "maxEventAge",
        "retry_attempts": "retryAttempts",
        "event_role": "eventRole",
        "header_parameters": "headerParameters",
        "method": "method",
        "path": "path",
        "path_parameter_values": "pathParameterValues",
        "post_body": "postBody",
        "query_string_parameters": "queryStringParameters",
        "stage": "stage",
    },
)
class ApiGatewayProps(TargetBaseProps):
    def __init__(
        self,
        *,
        dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
        max_event_age: typing.Optional[_Duration_4839e8c3] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
        event_role: typing.Optional[_IRole_235f5d8e] = None,
        header_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        method: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
        path_parameter_values: typing.Optional[typing.Sequence[builtins.str]] = None,
        post_body: typing.Optional[_RuleTargetInput_6beca786] = None,
        query_string_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        stage: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Customize the API Gateway Event Target.

        :param dead_letter_queue: The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_. The events not successfully delivered are automatically retried for a specified period of time, depending on the retry policy of the target. If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue. Default: - no dead-letter queue
        :param max_event_age: The maximum age of a request that Lambda sends to a function for processing. Minimum value of 60. Maximum value of 86400. Default: Duration.hours(24)
        :param retry_attempts: The maximum number of times to retry when the function returns an error. Minimum value of 0. Maximum value of 185. Default: 185
        :param event_role: The role to assume before invoking the target (i.e., the pipeline) when the given rule is triggered. Default: - a new role will be created
        :param header_parameters: The headers to be set when requesting API. Default: no header parameters
        :param method: The method for api resource invoked by the rule. Default: '*' that treated as ANY
        :param path: The api resource invoked by the rule. We can use wildcards('*') to specify the path. In that case, an equal number of real values must be specified for pathParameterValues. Default: '/'
        :param path_parameter_values: The path parameter values to be used to populate to wildcards("*") of requesting api path. Default: no path parameters
        :param post_body: This will be the post request body send to the API. Default: the entire EventBridge event
        :param query_string_parameters: The query parameters to be set when requesting API. Default: no querystring parameters
        :param stage: The deploy stage of api gateway invoked by the rule. Default: the value of deploymentStage.stageName of target api gateway.

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_apigateway as api
            import aws_cdk.aws_lambda as lambda_
            
            
            rule = events.Rule(self, "Rule",
                schedule=events.Schedule.rate(Duration.minutes(1))
            )
            
            fn = lambda_.Function(self, "MyFunc",
                handler="index.handler",
                runtime=lambda_.Runtime.NODEJS_LATEST,
                code=lambda_.Code.from_inline("exports.handler = e => {}")
            )
            
            rest_api = api.LambdaRestApi(self, "MyRestAPI", handler=fn)
            
            dlq = sqs.Queue(self, "DeadLetterQueue")
            
            rule.add_target(
                targets.ApiGateway(rest_api,
                    path="/*/test",
                    method="GET",
                    stage="prod",
                    path_parameter_values=["path-value"],
                    header_parameters={
                        "Header1": "header1"
                    },
                    query_string_parameters={
                        "QueryParam1": "query-param-1"
                    },
                    dead_letter_queue=dlq
                ))
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed5e368611ecca03be97333615df4f6727992e87138462a27cc1f9a4cdf3a511)
            check_type(argname="argument dead_letter_queue", value=dead_letter_queue, expected_type=type_hints["dead_letter_queue"])
            check_type(argname="argument max_event_age", value=max_event_age, expected_type=type_hints["max_event_age"])
            check_type(argname="argument retry_attempts", value=retry_attempts, expected_type=type_hints["retry_attempts"])
            check_type(argname="argument event_role", value=event_role, expected_type=type_hints["event_role"])
            check_type(argname="argument header_parameters", value=header_parameters, expected_type=type_hints["header_parameters"])
            check_type(argname="argument method", value=method, expected_type=type_hints["method"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument path_parameter_values", value=path_parameter_values, expected_type=type_hints["path_parameter_values"])
            check_type(argname="argument post_body", value=post_body, expected_type=type_hints["post_body"])
            check_type(argname="argument query_string_parameters", value=query_string_parameters, expected_type=type_hints["query_string_parameters"])
            check_type(argname="argument stage", value=stage, expected_type=type_hints["stage"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if dead_letter_queue is not None:
            self._values["dead_letter_queue"] = dead_letter_queue
        if max_event_age is not None:
            self._values["max_event_age"] = max_event_age
        if retry_attempts is not None:
            self._values["retry_attempts"] = retry_attempts
        if event_role is not None:
            self._values["event_role"] = event_role
        if header_parameters is not None:
            self._values["header_parameters"] = header_parameters
        if method is not None:
            self._values["method"] = method
        if path is not None:
            self._values["path"] = path
        if path_parameter_values is not None:
            self._values["path_parameter_values"] = path_parameter_values
        if post_body is not None:
            self._values["post_body"] = post_body
        if query_string_parameters is not None:
            self._values["query_string_parameters"] = query_string_parameters
        if stage is not None:
            self._values["stage"] = stage

    @builtins.property
    def dead_letter_queue(self) -> typing.Optional[_IQueue_7ed6f679]:
        '''The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_.

        The events not successfully delivered are automatically retried for a specified period of time,
        depending on the retry policy of the target.
        If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue.

        :default: - no dead-letter queue
        '''
        result = self._values.get("dead_letter_queue")
        return typing.cast(typing.Optional[_IQueue_7ed6f679], result)

    @builtins.property
    def max_event_age(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The maximum age of a request that Lambda sends to a function for processing.

        Minimum value of 60.
        Maximum value of 86400.

        :default: Duration.hours(24)
        '''
        result = self._values.get("max_event_age")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def retry_attempts(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of times to retry when the function returns an error.

        Minimum value of 0.
        Maximum value of 185.

        :default: 185
        '''
        result = self._values.get("retry_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def event_role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''The role to assume before invoking the target (i.e., the pipeline) when the given rule is triggered.

        :default: - a new role will be created
        '''
        result = self._values.get("event_role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    @builtins.property
    def header_parameters(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The headers to be set when requesting API.

        :default: no header parameters
        '''
        result = self._values.get("header_parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def method(self) -> typing.Optional[builtins.str]:
        '''The method for api resource invoked by the rule.

        :default: '*' that treated as ANY
        '''
        result = self._values.get("method")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''The api resource invoked by the rule.

        We can use wildcards('*') to specify the path. In that case,
        an equal number of real values must be specified for pathParameterValues.

        :default: '/'
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def path_parameter_values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The path parameter values to be used to populate to wildcards("*") of requesting api path.

        :default: no path parameters
        '''
        result = self._values.get("path_parameter_values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def post_body(self) -> typing.Optional[_RuleTargetInput_6beca786]:
        '''This will be the post request body send to the API.

        :default: the entire EventBridge event
        '''
        result = self._values.get("post_body")
        return typing.cast(typing.Optional[_RuleTargetInput_6beca786], result)

    @builtins.property
    def query_string_parameters(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The query parameters to be set when requesting API.

        :default: no querystring parameters
        '''
        result = self._values.get("query_string_parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def stage(self) -> typing.Optional[builtins.str]:
        '''The deploy stage of api gateway invoked by the rule.

        :default: the value of deploymentStage.stageName of target api gateway.
        '''
        result = self._values.get("stage")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiGatewayProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_events_targets.AppSyncGraphQLApiProps",
    jsii_struct_bases=[TargetBaseProps],
    name_mapping={
        "dead_letter_queue": "deadLetterQueue",
        "max_event_age": "maxEventAge",
        "retry_attempts": "retryAttempts",
        "graph_ql_operation": "graphQLOperation",
        "event_role": "eventRole",
        "variables": "variables",
    },
)
class AppSyncGraphQLApiProps(TargetBaseProps):
    def __init__(
        self,
        *,
        dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
        max_event_age: typing.Optional[_Duration_4839e8c3] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
        graph_ql_operation: builtins.str,
        event_role: typing.Optional[_IRole_235f5d8e] = None,
        variables: typing.Optional[_RuleTargetInput_6beca786] = None,
    ) -> None:
        '''Customize the AppSync GraphQL API target.

        :param dead_letter_queue: The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_. The events not successfully delivered are automatically retried for a specified period of time, depending on the retry policy of the target. If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue. Default: - no dead-letter queue
        :param max_event_age: The maximum age of a request that Lambda sends to a function for processing. Minimum value of 60. Maximum value of 86400. Default: Duration.hours(24)
        :param retry_attempts: The maximum number of times to retry when the function returns an error. Minimum value of 0. Maximum value of 185. Default: 185
        :param graph_ql_operation: The GraphQL operation; that is, the query, mutation, or subscription to be parsed and executed by the GraphQL service.
        :param event_role: The role to assume before invoking the target (i.e., the pipeline) when the given rule is triggered. Default: - a new role with permissions to access mutations will be created
        :param variables: The variables that are include in the GraphQL operation. Default: - The entire event is used

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_appsync as appsync
            
            
            api = appsync.GraphqlApi(self, "api",
                name="api",
                definition=appsync.Definition.from_file("schema.graphql"),
                authorization_config=appsync.AuthorizationConfig(
                    default_authorization=appsync.AuthorizationMode(authorization_type=appsync.AuthorizationType.IAM)
                )
            )
            
            rule = events.Rule(self, "Rule",
                schedule=events.Schedule.rate(cdk.Duration.hours(1))
            )
            
            rule.add_target(targets.AppSync(api,
                graph_qLOperation="mutation Publish($message: String!){ publish(message: $message) { message } }",
                variables=events.RuleTargetInput.from_object({
                    "message": "hello world"
                })
            ))
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aea6c33be1be64052595742c1fdd00fb0f53185ebe3c9f93ceacd92d82655d1d)
            check_type(argname="argument dead_letter_queue", value=dead_letter_queue, expected_type=type_hints["dead_letter_queue"])
            check_type(argname="argument max_event_age", value=max_event_age, expected_type=type_hints["max_event_age"])
            check_type(argname="argument retry_attempts", value=retry_attempts, expected_type=type_hints["retry_attempts"])
            check_type(argname="argument graph_ql_operation", value=graph_ql_operation, expected_type=type_hints["graph_ql_operation"])
            check_type(argname="argument event_role", value=event_role, expected_type=type_hints["event_role"])
            check_type(argname="argument variables", value=variables, expected_type=type_hints["variables"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "graph_ql_operation": graph_ql_operation,
        }
        if dead_letter_queue is not None:
            self._values["dead_letter_queue"] = dead_letter_queue
        if max_event_age is not None:
            self._values["max_event_age"] = max_event_age
        if retry_attempts is not None:
            self._values["retry_attempts"] = retry_attempts
        if event_role is not None:
            self._values["event_role"] = event_role
        if variables is not None:
            self._values["variables"] = variables

    @builtins.property
    def dead_letter_queue(self) -> typing.Optional[_IQueue_7ed6f679]:
        '''The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_.

        The events not successfully delivered are automatically retried for a specified period of time,
        depending on the retry policy of the target.
        If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue.

        :default: - no dead-letter queue
        '''
        result = self._values.get("dead_letter_queue")
        return typing.cast(typing.Optional[_IQueue_7ed6f679], result)

    @builtins.property
    def max_event_age(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The maximum age of a request that Lambda sends to a function for processing.

        Minimum value of 60.
        Maximum value of 86400.

        :default: Duration.hours(24)
        '''
        result = self._values.get("max_event_age")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def retry_attempts(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of times to retry when the function returns an error.

        Minimum value of 0.
        Maximum value of 185.

        :default: 185
        '''
        result = self._values.get("retry_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def graph_ql_operation(self) -> builtins.str:
        '''The GraphQL operation;

        that is, the query, mutation, or subscription
        to be parsed and executed by the GraphQL service.
        '''
        result = self._values.get("graph_ql_operation")
        assert result is not None, "Required property 'graph_ql_operation' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def event_role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''The role to assume before invoking the target (i.e., the pipeline) when the given rule is triggered.

        :default: - a new role with permissions to access mutations will be created
        '''
        result = self._values.get("event_role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    @builtins.property
    def variables(self) -> typing.Optional[_RuleTargetInput_6beca786]:
        '''The variables that are include in the GraphQL operation.

        :default: - The entire event is used
        '''
        result = self._values.get("variables")
        return typing.cast(typing.Optional[_RuleTargetInput_6beca786], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppSyncGraphQLApiProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_events_targets.BatchJobProps",
    jsii_struct_bases=[TargetBaseProps],
    name_mapping={
        "dead_letter_queue": "deadLetterQueue",
        "max_event_age": "maxEventAge",
        "retry_attempts": "retryAttempts",
        "attempts": "attempts",
        "event": "event",
        "job_name": "jobName",
        "size": "size",
    },
)
class BatchJobProps(TargetBaseProps):
    def __init__(
        self,
        *,
        dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
        max_event_age: typing.Optional[_Duration_4839e8c3] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
        attempts: typing.Optional[jsii.Number] = None,
        event: typing.Optional[_RuleTargetInput_6beca786] = None,
        job_name: typing.Optional[builtins.str] = None,
        size: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Customize the Batch Job Event Target.

        :param dead_letter_queue: The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_. The events not successfully delivered are automatically retried for a specified period of time, depending on the retry policy of the target. If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue. Default: - no dead-letter queue
        :param max_event_age: The maximum age of a request that Lambda sends to a function for processing. Minimum value of 60. Maximum value of 86400. Default: Duration.hours(24)
        :param retry_attempts: The maximum number of times to retry when the function returns an error. Minimum value of 0. Maximum value of 185. Default: 185
        :param attempts: The number of times to attempt to retry, if the job fails. Valid values are 1–10. Default: no retryStrategy is set
        :param event: The event to send to the Lambda. This will be the payload sent to the Lambda Function. Default: the entire EventBridge event
        :param job_name: The name of the submitted job. Default: - Automatically generated
        :param size: The size of the array, if this is an array batch job. Valid values are integers between 2 and 10,000. Default: no arrayProperties are set

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_ec2 as ec2
            import aws_cdk.aws_ecs as ecs
            import aws_cdk.aws_batch as batch
            from aws_cdk.aws_ecs import ContainerImage
            
            # vpc: ec2.Vpc
            
            
            compute_environment = batch.FargateComputeEnvironment(self, "ComputeEnv",
                vpc=vpc
            )
            
            job_queue = batch.JobQueue(self, "JobQueue",
                priority=1,
                compute_environments=[batch.OrderedComputeEnvironment(
                    compute_environment=compute_environment,
                    order=1
                )
                ]
            )
            
            job_definition = batch.EcsJobDefinition(self, "MyJob",
                container=batch.EcsEc2ContainerDefinition(self, "Container",
                    image=ecs.ContainerImage.from_registry("test-repo"),
                    memory=cdk.Size.mebibytes(2048),
                    cpu=256
                )
            )
            
            queue = sqs.Queue(self, "Queue")
            
            rule = events.Rule(self, "Rule",
                schedule=events.Schedule.rate(Duration.hours(1))
            )
            
            rule.add_target(targets.BatchJob(job_queue.job_queue_arn, job_queue, job_definition.job_definition_arn, job_definition,
                dead_letter_queue=queue,
                event=events.RuleTargetInput.from_object({"SomeParam": "SomeValue"}),
                retry_attempts=2,
                max_event_age=Duration.hours(2)
            ))
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91b263189af78d46fd5bf421034197688036a7347fbaee9bef843d928f9bb43f)
            check_type(argname="argument dead_letter_queue", value=dead_letter_queue, expected_type=type_hints["dead_letter_queue"])
            check_type(argname="argument max_event_age", value=max_event_age, expected_type=type_hints["max_event_age"])
            check_type(argname="argument retry_attempts", value=retry_attempts, expected_type=type_hints["retry_attempts"])
            check_type(argname="argument attempts", value=attempts, expected_type=type_hints["attempts"])
            check_type(argname="argument event", value=event, expected_type=type_hints["event"])
            check_type(argname="argument job_name", value=job_name, expected_type=type_hints["job_name"])
            check_type(argname="argument size", value=size, expected_type=type_hints["size"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if dead_letter_queue is not None:
            self._values["dead_letter_queue"] = dead_letter_queue
        if max_event_age is not None:
            self._values["max_event_age"] = max_event_age
        if retry_attempts is not None:
            self._values["retry_attempts"] = retry_attempts
        if attempts is not None:
            self._values["attempts"] = attempts
        if event is not None:
            self._values["event"] = event
        if job_name is not None:
            self._values["job_name"] = job_name
        if size is not None:
            self._values["size"] = size

    @builtins.property
    def dead_letter_queue(self) -> typing.Optional[_IQueue_7ed6f679]:
        '''The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_.

        The events not successfully delivered are automatically retried for a specified period of time,
        depending on the retry policy of the target.
        If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue.

        :default: - no dead-letter queue
        '''
        result = self._values.get("dead_letter_queue")
        return typing.cast(typing.Optional[_IQueue_7ed6f679], result)

    @builtins.property
    def max_event_age(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The maximum age of a request that Lambda sends to a function for processing.

        Minimum value of 60.
        Maximum value of 86400.

        :default: Duration.hours(24)
        '''
        result = self._values.get("max_event_age")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def retry_attempts(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of times to retry when the function returns an error.

        Minimum value of 0.
        Maximum value of 185.

        :default: 185
        '''
        result = self._values.get("retry_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def attempts(self) -> typing.Optional[jsii.Number]:
        '''The number of times to attempt to retry, if the job fails.

        Valid values are 1–10.

        :default: no retryStrategy is set
        '''
        result = self._values.get("attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def event(self) -> typing.Optional[_RuleTargetInput_6beca786]:
        '''The event to send to the Lambda.

        This will be the payload sent to the Lambda Function.

        :default: the entire EventBridge event
        '''
        result = self._values.get("event")
        return typing.cast(typing.Optional[_RuleTargetInput_6beca786], result)

    @builtins.property
    def job_name(self) -> typing.Optional[builtins.str]:
        '''The name of the submitted job.

        :default: - Automatically generated
        '''
        result = self._values.get("job_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def size(self) -> typing.Optional[jsii.Number]:
        '''The size of the array, if this is an array batch job.

        Valid values are integers between 2 and 10,000.

        :default: no arrayProperties are set
        '''
        result = self._values.get("size")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BatchJobProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_events_targets.CodeBuildProjectProps",
    jsii_struct_bases=[TargetBaseProps],
    name_mapping={
        "dead_letter_queue": "deadLetterQueue",
        "max_event_age": "maxEventAge",
        "retry_attempts": "retryAttempts",
        "event": "event",
        "event_role": "eventRole",
    },
)
class CodeBuildProjectProps(TargetBaseProps):
    def __init__(
        self,
        *,
        dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
        max_event_age: typing.Optional[_Duration_4839e8c3] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
        event: typing.Optional[_RuleTargetInput_6beca786] = None,
        event_role: typing.Optional[_IRole_235f5d8e] = None,
    ) -> None:
        '''Customize the CodeBuild Event Target.

        :param dead_letter_queue: The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_. The events not successfully delivered are automatically retried for a specified period of time, depending on the retry policy of the target. If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue. Default: - no dead-letter queue
        :param max_event_age: The maximum age of a request that Lambda sends to a function for processing. Minimum value of 60. Maximum value of 86400. Default: Duration.hours(24)
        :param retry_attempts: The maximum number of times to retry when the function returns an error. Minimum value of 0. Maximum value of 185. Default: 185
        :param event: The event to send to CodeBuild. This will be the payload for the StartBuild API. Default: - the entire EventBridge event
        :param event_role: The role to assume before invoking the target (i.e., the codebuild) when the given rule is triggered. Default: - a new role will be created

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_codebuild as codebuild
            import aws_cdk.aws_codecommit as codecommit
            
            
            repo = codecommit.Repository(self, "MyRepo",
                repository_name="aws-cdk-codebuild-events"
            )
            
            project = codebuild.Project(self, "MyProject",
                source=codebuild.Source.code_commit(repository=repo)
            )
            
            dead_letter_queue = sqs.Queue(self, "DeadLetterQueue")
            
            # trigger a build when a commit is pushed to the repo
            on_commit_rule = repo.on_commit("OnCommit",
                target=targets.CodeBuildProject(project,
                    dead_letter_queue=dead_letter_queue
                ),
                branches=["master"]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0aa7b3ccb4774f7e12d466bbcb6662ffc40cea68d16ffd9b2fff0a4a8ff49b72)
            check_type(argname="argument dead_letter_queue", value=dead_letter_queue, expected_type=type_hints["dead_letter_queue"])
            check_type(argname="argument max_event_age", value=max_event_age, expected_type=type_hints["max_event_age"])
            check_type(argname="argument retry_attempts", value=retry_attempts, expected_type=type_hints["retry_attempts"])
            check_type(argname="argument event", value=event, expected_type=type_hints["event"])
            check_type(argname="argument event_role", value=event_role, expected_type=type_hints["event_role"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if dead_letter_queue is not None:
            self._values["dead_letter_queue"] = dead_letter_queue
        if max_event_age is not None:
            self._values["max_event_age"] = max_event_age
        if retry_attempts is not None:
            self._values["retry_attempts"] = retry_attempts
        if event is not None:
            self._values["event"] = event
        if event_role is not None:
            self._values["event_role"] = event_role

    @builtins.property
    def dead_letter_queue(self) -> typing.Optional[_IQueue_7ed6f679]:
        '''The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_.

        The events not successfully delivered are automatically retried for a specified period of time,
        depending on the retry policy of the target.
        If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue.

        :default: - no dead-letter queue
        '''
        result = self._values.get("dead_letter_queue")
        return typing.cast(typing.Optional[_IQueue_7ed6f679], result)

    @builtins.property
    def max_event_age(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The maximum age of a request that Lambda sends to a function for processing.

        Minimum value of 60.
        Maximum value of 86400.

        :default: Duration.hours(24)
        '''
        result = self._values.get("max_event_age")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def retry_attempts(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of times to retry when the function returns an error.

        Minimum value of 0.
        Maximum value of 185.

        :default: 185
        '''
        result = self._values.get("retry_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def event(self) -> typing.Optional[_RuleTargetInput_6beca786]:
        '''The event to send to CodeBuild.

        This will be the payload for the StartBuild API.

        :default: - the entire EventBridge event
        '''
        result = self._values.get("event")
        return typing.cast(typing.Optional[_RuleTargetInput_6beca786], result)

    @builtins.property
    def event_role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''The role to assume before invoking the target (i.e., the codebuild) when the given rule is triggered.

        :default: - a new role will be created
        '''
        result = self._values.get("event_role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodeBuildProjectProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_events_targets.CodePipelineTargetOptions",
    jsii_struct_bases=[TargetBaseProps],
    name_mapping={
        "dead_letter_queue": "deadLetterQueue",
        "max_event_age": "maxEventAge",
        "retry_attempts": "retryAttempts",
        "event_role": "eventRole",
    },
)
class CodePipelineTargetOptions(TargetBaseProps):
    def __init__(
        self,
        *,
        dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
        max_event_age: typing.Optional[_Duration_4839e8c3] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
        event_role: typing.Optional[_IRole_235f5d8e] = None,
    ) -> None:
        '''Customization options when creating a ``CodePipeline`` event target.

        :param dead_letter_queue: The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_. The events not successfully delivered are automatically retried for a specified period of time, depending on the retry policy of the target. If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue. Default: - no dead-letter queue
        :param max_event_age: The maximum age of a request that Lambda sends to a function for processing. Minimum value of 60. Maximum value of 86400. Default: Duration.hours(24)
        :param retry_attempts: The maximum number of times to retry when the function returns an error. Minimum value of 0. Maximum value of 185. Default: 185
        :param event_role: The role to assume before invoking the target (i.e., the pipeline) when the given rule is triggered. Default: - a new role will be created

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk as cdk
            from aws_cdk import aws_events_targets as events_targets
            from aws_cdk import aws_iam as iam
            from aws_cdk import aws_sqs as sqs
            
            # queue: sqs.Queue
            # role: iam.Role
            
            code_pipeline_target_options = events_targets.CodePipelineTargetOptions(
                dead_letter_queue=queue,
                event_role=role,
                max_event_age=cdk.Duration.minutes(30),
                retry_attempts=123
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c1acf9f087ecbbaf384c1beceee58dbb3a425d691a10d8da9317706e37e3dfe)
            check_type(argname="argument dead_letter_queue", value=dead_letter_queue, expected_type=type_hints["dead_letter_queue"])
            check_type(argname="argument max_event_age", value=max_event_age, expected_type=type_hints["max_event_age"])
            check_type(argname="argument retry_attempts", value=retry_attempts, expected_type=type_hints["retry_attempts"])
            check_type(argname="argument event_role", value=event_role, expected_type=type_hints["event_role"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if dead_letter_queue is not None:
            self._values["dead_letter_queue"] = dead_letter_queue
        if max_event_age is not None:
            self._values["max_event_age"] = max_event_age
        if retry_attempts is not None:
            self._values["retry_attempts"] = retry_attempts
        if event_role is not None:
            self._values["event_role"] = event_role

    @builtins.property
    def dead_letter_queue(self) -> typing.Optional[_IQueue_7ed6f679]:
        '''The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_.

        The events not successfully delivered are automatically retried for a specified period of time,
        depending on the retry policy of the target.
        If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue.

        :default: - no dead-letter queue
        '''
        result = self._values.get("dead_letter_queue")
        return typing.cast(typing.Optional[_IQueue_7ed6f679], result)

    @builtins.property
    def max_event_age(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The maximum age of a request that Lambda sends to a function for processing.

        Minimum value of 60.
        Maximum value of 86400.

        :default: Duration.hours(24)
        '''
        result = self._values.get("max_event_age")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def retry_attempts(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of times to retry when the function returns an error.

        Minimum value of 0.
        Maximum value of 185.

        :default: 185
        '''
        result = self._values.get("retry_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def event_role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''The role to assume before invoking the target (i.e., the pipeline) when the given rule is triggered.

        :default: - a new role will be created
        '''
        result = self._values.get("event_role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodePipelineTargetOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_events_targets.EcsTaskProps",
    jsii_struct_bases=[TargetBaseProps],
    name_mapping={
        "dead_letter_queue": "deadLetterQueue",
        "max_event_age": "maxEventAge",
        "retry_attempts": "retryAttempts",
        "cluster": "cluster",
        "task_definition": "taskDefinition",
        "assign_public_ip": "assignPublicIp",
        "container_overrides": "containerOverrides",
        "enable_execute_command": "enableExecuteCommand",
        "launch_type": "launchType",
        "platform_version": "platformVersion",
        "propagate_tags": "propagateTags",
        "role": "role",
        "security_groups": "securityGroups",
        "subnet_selection": "subnetSelection",
        "tags": "tags",
        "task_count": "taskCount",
    },
)
class EcsTaskProps(TargetBaseProps):
    def __init__(
        self,
        *,
        dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
        max_event_age: typing.Optional[_Duration_4839e8c3] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
        cluster: _ICluster_16cddd09,
        task_definition: _ITaskDefinition_889ba4d8,
        assign_public_ip: typing.Optional[builtins.bool] = None,
        container_overrides: typing.Optional[typing.Sequence[typing.Union[ContainerOverride, typing.Dict[builtins.str, typing.Any]]]] = None,
        enable_execute_command: typing.Optional[builtins.bool] = None,
        launch_type: typing.Optional[_LaunchType_6894135d] = None,
        platform_version: typing.Optional[_FargatePlatformVersion_55d8be5c] = None,
        propagate_tags: typing.Optional[_PropagatedTagSource_ad4e874a] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
        security_groups: typing.Optional[typing.Sequence[_ISecurityGroup_acf8a799]] = None,
        subnet_selection: typing.Optional[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[Tag, typing.Dict[builtins.str, typing.Any]]]] = None,
        task_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Properties to define an ECS Event Task.

        :param dead_letter_queue: The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_. The events not successfully delivered are automatically retried for a specified period of time, depending on the retry policy of the target. If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue. Default: - no dead-letter queue
        :param max_event_age: The maximum age of a request that Lambda sends to a function for processing. Minimum value of 60. Maximum value of 86400. Default: Duration.hours(24)
        :param retry_attempts: The maximum number of times to retry when the function returns an error. Minimum value of 0. Maximum value of 185. Default: 185
        :param cluster: Cluster where service will be deployed.
        :param task_definition: Task Definition of the task that should be started.
        :param assign_public_ip: Specifies whether the task's elastic network interface receives a public IP address. You can specify true only when LaunchType is set to FARGATE. Default: - true if the subnet type is PUBLIC, otherwise false
        :param container_overrides: Container setting overrides. Key is the name of the container to override, value is the values you want to override.
        :param enable_execute_command: Whether or not to enable the execute command functionality for the containers in this task. If true, this enables execute command functionality on all containers in the task. Default: - false
        :param launch_type: Specifies the launch type on which your task is running. The launch type that you specify here must match one of the launch type (compatibilities) of the target task. Default: - 'EC2' if ``isEc2Compatible`` for the ``taskDefinition`` is true, otherwise 'FARGATE'
        :param platform_version: The platform version on which to run your task. Unless you have specific compatibility requirements, you don't need to specify this. Default: - ECS will set the Fargate platform version to 'LATEST'
        :param propagate_tags: Specifies whether to propagate the tags from the task definition to the task. If no value is specified, the tags are not propagated. Default: - Tags will not be propagated
        :param role: Existing IAM role to run the ECS task. Default: A new IAM role is created
        :param security_groups: Existing security groups to use for the task's ENIs. (Only applicable in case the TaskDefinition is configured for AwsVpc networking) Default: A new security group is created
        :param subnet_selection: In what subnets to place the task's ENIs. (Only applicable in case the TaskDefinition is configured for AwsVpc networking) Default: Private subnets
        :param tags: The metadata that you apply to the task to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Default: - No additional tags are applied to the task
        :param task_count: How many tasks should be started when this event is triggered. Default: 1

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_ecs as ecs
            import aws_cdk.aws_ec2 as ec2
            
            # cluster: ecs.ICluster
            # task_definition: ecs.TaskDefinition
            
            
            rule = events.Rule(self, "Rule",
                schedule=events.Schedule.rate(cdk.Duration.hours(1))
            )
            
            rule.add_target(
                targets.EcsTask(
                    cluster=cluster,
                    task_definition=task_definition,
                    assign_public_ip=True,
                    subnet_selection=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC)
                ))
        '''
        if isinstance(subnet_selection, dict):
            subnet_selection = _SubnetSelection_e57d76df(**subnet_selection)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3624031da4f9372e2ccdb3e422123cc459d01922cc36bab5b96caa98fc41c5b1)
            check_type(argname="argument dead_letter_queue", value=dead_letter_queue, expected_type=type_hints["dead_letter_queue"])
            check_type(argname="argument max_event_age", value=max_event_age, expected_type=type_hints["max_event_age"])
            check_type(argname="argument retry_attempts", value=retry_attempts, expected_type=type_hints["retry_attempts"])
            check_type(argname="argument cluster", value=cluster, expected_type=type_hints["cluster"])
            check_type(argname="argument task_definition", value=task_definition, expected_type=type_hints["task_definition"])
            check_type(argname="argument assign_public_ip", value=assign_public_ip, expected_type=type_hints["assign_public_ip"])
            check_type(argname="argument container_overrides", value=container_overrides, expected_type=type_hints["container_overrides"])
            check_type(argname="argument enable_execute_command", value=enable_execute_command, expected_type=type_hints["enable_execute_command"])
            check_type(argname="argument launch_type", value=launch_type, expected_type=type_hints["launch_type"])
            check_type(argname="argument platform_version", value=platform_version, expected_type=type_hints["platform_version"])
            check_type(argname="argument propagate_tags", value=propagate_tags, expected_type=type_hints["propagate_tags"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
            check_type(argname="argument subnet_selection", value=subnet_selection, expected_type=type_hints["subnet_selection"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument task_count", value=task_count, expected_type=type_hints["task_count"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cluster": cluster,
            "task_definition": task_definition,
        }
        if dead_letter_queue is not None:
            self._values["dead_letter_queue"] = dead_letter_queue
        if max_event_age is not None:
            self._values["max_event_age"] = max_event_age
        if retry_attempts is not None:
            self._values["retry_attempts"] = retry_attempts
        if assign_public_ip is not None:
            self._values["assign_public_ip"] = assign_public_ip
        if container_overrides is not None:
            self._values["container_overrides"] = container_overrides
        if enable_execute_command is not None:
            self._values["enable_execute_command"] = enable_execute_command
        if launch_type is not None:
            self._values["launch_type"] = launch_type
        if platform_version is not None:
            self._values["platform_version"] = platform_version
        if propagate_tags is not None:
            self._values["propagate_tags"] = propagate_tags
        if role is not None:
            self._values["role"] = role
        if security_groups is not None:
            self._values["security_groups"] = security_groups
        if subnet_selection is not None:
            self._values["subnet_selection"] = subnet_selection
        if tags is not None:
            self._values["tags"] = tags
        if task_count is not None:
            self._values["task_count"] = task_count

    @builtins.property
    def dead_letter_queue(self) -> typing.Optional[_IQueue_7ed6f679]:
        '''The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_.

        The events not successfully delivered are automatically retried for a specified period of time,
        depending on the retry policy of the target.
        If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue.

        :default: - no dead-letter queue
        '''
        result = self._values.get("dead_letter_queue")
        return typing.cast(typing.Optional[_IQueue_7ed6f679], result)

    @builtins.property
    def max_event_age(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The maximum age of a request that Lambda sends to a function for processing.

        Minimum value of 60.
        Maximum value of 86400.

        :default: Duration.hours(24)
        '''
        result = self._values.get("max_event_age")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def retry_attempts(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of times to retry when the function returns an error.

        Minimum value of 0.
        Maximum value of 185.

        :default: 185
        '''
        result = self._values.get("retry_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def cluster(self) -> _ICluster_16cddd09:
        '''Cluster where service will be deployed.'''
        result = self._values.get("cluster")
        assert result is not None, "Required property 'cluster' is missing"
        return typing.cast(_ICluster_16cddd09, result)

    @builtins.property
    def task_definition(self) -> _ITaskDefinition_889ba4d8:
        '''Task Definition of the task that should be started.'''
        result = self._values.get("task_definition")
        assert result is not None, "Required property 'task_definition' is missing"
        return typing.cast(_ITaskDefinition_889ba4d8, result)

    @builtins.property
    def assign_public_ip(self) -> typing.Optional[builtins.bool]:
        '''Specifies whether the task's elastic network interface receives a public IP address.

        You can specify true only when LaunchType is set to FARGATE.

        :default: - true if the subnet type is PUBLIC, otherwise false
        '''
        result = self._values.get("assign_public_ip")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def container_overrides(self) -> typing.Optional[typing.List[ContainerOverride]]:
        '''Container setting overrides.

        Key is the name of the container to override, value is the
        values you want to override.
        '''
        result = self._values.get("container_overrides")
        return typing.cast(typing.Optional[typing.List[ContainerOverride]], result)

    @builtins.property
    def enable_execute_command(self) -> typing.Optional[builtins.bool]:
        '''Whether or not to enable the execute command functionality for the containers in this task.

        If true, this enables execute command functionality on all containers in the task.

        :default: - false
        '''
        result = self._values.get("enable_execute_command")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def launch_type(self) -> typing.Optional[_LaunchType_6894135d]:
        '''Specifies the launch type on which your task is running.

        The launch type that you specify here
        must match one of the launch type (compatibilities) of the target task.

        :default: - 'EC2' if ``isEc2Compatible`` for the ``taskDefinition`` is true, otherwise 'FARGATE'
        '''
        result = self._values.get("launch_type")
        return typing.cast(typing.Optional[_LaunchType_6894135d], result)

    @builtins.property
    def platform_version(self) -> typing.Optional[_FargatePlatformVersion_55d8be5c]:
        '''The platform version on which to run your task.

        Unless you have specific compatibility requirements, you don't need to specify this.

        :default: - ECS will set the Fargate platform version to 'LATEST'

        :see: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html
        '''
        result = self._values.get("platform_version")
        return typing.cast(typing.Optional[_FargatePlatformVersion_55d8be5c], result)

    @builtins.property
    def propagate_tags(self) -> typing.Optional[_PropagatedTagSource_ad4e874a]:
        '''Specifies whether to propagate the tags from the task definition to the task.

        If no value is specified, the tags are not propagated.

        :default: - Tags will not be propagated
        '''
        result = self._values.get("propagate_tags")
        return typing.cast(typing.Optional[_PropagatedTagSource_ad4e874a], result)

    @builtins.property
    def role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''Existing IAM role to run the ECS task.

        :default: A new IAM role is created
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    @builtins.property
    def security_groups(self) -> typing.Optional[typing.List[_ISecurityGroup_acf8a799]]:
        '''Existing security groups to use for the task's ENIs.

        (Only applicable in case the TaskDefinition is configured for AwsVpc networking)

        :default: A new security group is created
        '''
        result = self._values.get("security_groups")
        return typing.cast(typing.Optional[typing.List[_ISecurityGroup_acf8a799]], result)

    @builtins.property
    def subnet_selection(self) -> typing.Optional[_SubnetSelection_e57d76df]:
        '''In what subnets to place the task's ENIs.

        (Only applicable in case the TaskDefinition is configured for AwsVpc networking)

        :default: Private subnets
        '''
        result = self._values.get("subnet_selection")
        return typing.cast(typing.Optional[_SubnetSelection_e57d76df], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[Tag]]:
        '''The metadata that you apply to the task to help you categorize and organize them.

        Each tag consists of a key and an optional value, both of which you define.

        :default: - No additional tags are applied to the task
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[Tag]], result)

    @builtins.property
    def task_count(self) -> typing.Optional[jsii.Number]:
        '''How many tasks should be started when this event is triggered.

        :default: 1
        '''
        result = self._values.get("task_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsTaskProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_events_targets.LambdaFunctionProps",
    jsii_struct_bases=[TargetBaseProps],
    name_mapping={
        "dead_letter_queue": "deadLetterQueue",
        "max_event_age": "maxEventAge",
        "retry_attempts": "retryAttempts",
        "event": "event",
    },
)
class LambdaFunctionProps(TargetBaseProps):
    def __init__(
        self,
        *,
        dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
        max_event_age: typing.Optional[_Duration_4839e8c3] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
        event: typing.Optional[_RuleTargetInput_6beca786] = None,
    ) -> None:
        '''Customize the Lambda Event Target.

        :param dead_letter_queue: The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_. The events not successfully delivered are automatically retried for a specified period of time, depending on the retry policy of the target. If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue. Default: - no dead-letter queue
        :param max_event_age: The maximum age of a request that Lambda sends to a function for processing. Minimum value of 60. Maximum value of 86400. Default: Duration.hours(24)
        :param retry_attempts: The maximum number of times to retry when the function returns an error. Minimum value of 0. Maximum value of 185. Default: 185
        :param event: The event to send to the Lambda. This will be the payload sent to the Lambda Function. Default: the entire EventBridge event

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_lambda as lambda_
            
            
            fn = lambda_.Function(self, "MyFunc",
                runtime=lambda_.Runtime.NODEJS_LATEST,
                handler="index.handler",
                code=lambda_.Code.from_inline("exports.handler = handler.toString()")
            )
            
            rule = events.Rule(self, "rule",
                event_pattern=events.EventPattern(
                    source=["aws.ec2"]
                )
            )
            
            queue = sqs.Queue(self, "Queue")
            
            rule.add_target(targets.LambdaFunction(fn,
                dead_letter_queue=queue,  # Optional: add a dead letter queue
                max_event_age=Duration.hours(2),  # Optional: set the maxEventAge retry policy
                retry_attempts=2
            ))
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e34dd9ce66add58b9a28d19d7823e686db2c0d099525e77c896c992c0318854)
            check_type(argname="argument dead_letter_queue", value=dead_letter_queue, expected_type=type_hints["dead_letter_queue"])
            check_type(argname="argument max_event_age", value=max_event_age, expected_type=type_hints["max_event_age"])
            check_type(argname="argument retry_attempts", value=retry_attempts, expected_type=type_hints["retry_attempts"])
            check_type(argname="argument event", value=event, expected_type=type_hints["event"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if dead_letter_queue is not None:
            self._values["dead_letter_queue"] = dead_letter_queue
        if max_event_age is not None:
            self._values["max_event_age"] = max_event_age
        if retry_attempts is not None:
            self._values["retry_attempts"] = retry_attempts
        if event is not None:
            self._values["event"] = event

    @builtins.property
    def dead_letter_queue(self) -> typing.Optional[_IQueue_7ed6f679]:
        '''The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_.

        The events not successfully delivered are automatically retried for a specified period of time,
        depending on the retry policy of the target.
        If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue.

        :default: - no dead-letter queue
        '''
        result = self._values.get("dead_letter_queue")
        return typing.cast(typing.Optional[_IQueue_7ed6f679], result)

    @builtins.property
    def max_event_age(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The maximum age of a request that Lambda sends to a function for processing.

        Minimum value of 60.
        Maximum value of 86400.

        :default: Duration.hours(24)
        '''
        result = self._values.get("max_event_age")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def retry_attempts(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of times to retry when the function returns an error.

        Minimum value of 0.
        Maximum value of 185.

        :default: 185
        '''
        result = self._values.get("retry_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def event(self) -> typing.Optional[_RuleTargetInput_6beca786]:
        '''The event to send to the Lambda.

        This will be the payload sent to the Lambda Function.

        :default: the entire EventBridge event
        '''
        result = self._values.get("event")
        return typing.cast(typing.Optional[_RuleTargetInput_6beca786], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LambdaFunctionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_events_targets.LogGroupProps",
    jsii_struct_bases=[TargetBaseProps],
    name_mapping={
        "dead_letter_queue": "deadLetterQueue",
        "max_event_age": "maxEventAge",
        "retry_attempts": "retryAttempts",
        "event": "event",
        "install_latest_aws_sdk": "installLatestAwsSdk",
        "log_event": "logEvent",
    },
)
class LogGroupProps(TargetBaseProps):
    def __init__(
        self,
        *,
        dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
        max_event_age: typing.Optional[_Duration_4839e8c3] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
        event: typing.Optional[_RuleTargetInput_6beca786] = None,
        install_latest_aws_sdk: typing.Optional[builtins.bool] = None,
        log_event: typing.Optional[LogGroupTargetInput] = None,
    ) -> None:
        '''Customize the CloudWatch LogGroup Event Target.

        :param dead_letter_queue: The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_. The events not successfully delivered are automatically retried for a specified period of time, depending on the retry policy of the target. If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue. Default: - no dead-letter queue
        :param max_event_age: The maximum age of a request that Lambda sends to a function for processing. Minimum value of 60. Maximum value of 86400. Default: Duration.hours(24)
        :param retry_attempts: The maximum number of times to retry when the function returns an error. Minimum value of 0. Maximum value of 185. Default: 185
        :param event: (deprecated) The event to send to the CloudWatch LogGroup. This will be the event logged into the CloudWatch LogGroup Default: - the entire EventBridge event
        :param install_latest_aws_sdk: Whether the custom resource created wll default to install latest AWS SDK. Default: - install latest AWS SDK
        :param log_event: The event to send to the CloudWatch LogGroup. This will be the event logged into the CloudWatch LogGroup Default: - the entire EventBridge event

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_logs as logs
            # log_group: logs.LogGroup
            # rule: events.Rule
            
            
            rule.add_target(targets.CloudWatchLogGroup(log_group,
                log_event=targets.LogGroupTargetInput.from_object(
                    message=JSON.stringify({
                        "CustomField": "CustomValue"
                    })
                )
            ))
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__955ae13452482b1f3001946153d6bfa138fb7c7e8a5c482a52178f35142a7c9c)
            check_type(argname="argument dead_letter_queue", value=dead_letter_queue, expected_type=type_hints["dead_letter_queue"])
            check_type(argname="argument max_event_age", value=max_event_age, expected_type=type_hints["max_event_age"])
            check_type(argname="argument retry_attempts", value=retry_attempts, expected_type=type_hints["retry_attempts"])
            check_type(argname="argument event", value=event, expected_type=type_hints["event"])
            check_type(argname="argument install_latest_aws_sdk", value=install_latest_aws_sdk, expected_type=type_hints["install_latest_aws_sdk"])
            check_type(argname="argument log_event", value=log_event, expected_type=type_hints["log_event"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if dead_letter_queue is not None:
            self._values["dead_letter_queue"] = dead_letter_queue
        if max_event_age is not None:
            self._values["max_event_age"] = max_event_age
        if retry_attempts is not None:
            self._values["retry_attempts"] = retry_attempts
        if event is not None:
            self._values["event"] = event
        if install_latest_aws_sdk is not None:
            self._values["install_latest_aws_sdk"] = install_latest_aws_sdk
        if log_event is not None:
            self._values["log_event"] = log_event

    @builtins.property
    def dead_letter_queue(self) -> typing.Optional[_IQueue_7ed6f679]:
        '''The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_.

        The events not successfully delivered are automatically retried for a specified period of time,
        depending on the retry policy of the target.
        If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue.

        :default: - no dead-letter queue
        '''
        result = self._values.get("dead_letter_queue")
        return typing.cast(typing.Optional[_IQueue_7ed6f679], result)

    @builtins.property
    def max_event_age(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The maximum age of a request that Lambda sends to a function for processing.

        Minimum value of 60.
        Maximum value of 86400.

        :default: Duration.hours(24)
        '''
        result = self._values.get("max_event_age")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def retry_attempts(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of times to retry when the function returns an error.

        Minimum value of 0.
        Maximum value of 185.

        :default: 185
        '''
        result = self._values.get("retry_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def event(self) -> typing.Optional[_RuleTargetInput_6beca786]:
        '''(deprecated) The event to send to the CloudWatch LogGroup.

        This will be the event logged into the CloudWatch LogGroup

        :default: - the entire EventBridge event

        :deprecated: use logEvent instead

        :stability: deprecated
        '''
        result = self._values.get("event")
        return typing.cast(typing.Optional[_RuleTargetInput_6beca786], result)

    @builtins.property
    def install_latest_aws_sdk(self) -> typing.Optional[builtins.bool]:
        '''Whether the custom resource created wll default to install latest AWS SDK.

        :default: - install latest AWS SDK
        '''
        result = self._values.get("install_latest_aws_sdk")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def log_event(self) -> typing.Optional[LogGroupTargetInput]:
        '''The event to send to the CloudWatch LogGroup.

        This will be the event logged into the CloudWatch LogGroup

        :default: - the entire EventBridge event
        '''
        result = self._values.get("log_event")
        return typing.cast(typing.Optional[LogGroupTargetInput], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_events_targets.SfnStateMachineProps",
    jsii_struct_bases=[TargetBaseProps],
    name_mapping={
        "dead_letter_queue": "deadLetterQueue",
        "max_event_age": "maxEventAge",
        "retry_attempts": "retryAttempts",
        "input": "input",
        "role": "role",
    },
)
class SfnStateMachineProps(TargetBaseProps):
    def __init__(
        self,
        *,
        dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
        max_event_age: typing.Optional[_Duration_4839e8c3] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
        input: typing.Optional[_RuleTargetInput_6beca786] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
    ) -> None:
        '''Customize the Step Functions State Machine target.

        :param dead_letter_queue: The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_. The events not successfully delivered are automatically retried for a specified period of time, depending on the retry policy of the target. If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue. Default: - no dead-letter queue
        :param max_event_age: The maximum age of a request that Lambda sends to a function for processing. Minimum value of 60. Maximum value of 86400. Default: Duration.hours(24)
        :param retry_attempts: The maximum number of times to retry when the function returns an error. Minimum value of 0. Maximum value of 185. Default: 185
        :param input: The input to the state machine execution. Default: the entire EventBridge event
        :param role: The IAM role to be assumed to execute the State Machine. Default: - a new role will be created

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_iam as iam
            import aws_cdk.aws_stepfunctions as sfn
            
            
            rule = events.Rule(self, "Rule",
                schedule=events.Schedule.rate(Duration.minutes(1))
            )
            
            dlq = sqs.Queue(self, "DeadLetterQueue")
            
            role = iam.Role(self, "Role",
                assumed_by=iam.ServicePrincipal("events.amazonaws.com")
            )
            state_machine = sfn.StateMachine(self, "SM",
                definition=sfn.Wait(self, "Hello", time=sfn.WaitTime.duration(Duration.seconds(10)))
            )
            
            rule.add_target(targets.SfnStateMachine(state_machine,
                input=events.RuleTargetInput.from_object({"SomeParam": "SomeValue"}),
                dead_letter_queue=dlq,
                role=role
            ))
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e7617cf19a253c5e65116870d86237c3f90f88155a00afbdd412e561c617258)
            check_type(argname="argument dead_letter_queue", value=dead_letter_queue, expected_type=type_hints["dead_letter_queue"])
            check_type(argname="argument max_event_age", value=max_event_age, expected_type=type_hints["max_event_age"])
            check_type(argname="argument retry_attempts", value=retry_attempts, expected_type=type_hints["retry_attempts"])
            check_type(argname="argument input", value=input, expected_type=type_hints["input"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if dead_letter_queue is not None:
            self._values["dead_letter_queue"] = dead_letter_queue
        if max_event_age is not None:
            self._values["max_event_age"] = max_event_age
        if retry_attempts is not None:
            self._values["retry_attempts"] = retry_attempts
        if input is not None:
            self._values["input"] = input
        if role is not None:
            self._values["role"] = role

    @builtins.property
    def dead_letter_queue(self) -> typing.Optional[_IQueue_7ed6f679]:
        '''The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_.

        The events not successfully delivered are automatically retried for a specified period of time,
        depending on the retry policy of the target.
        If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue.

        :default: - no dead-letter queue
        '''
        result = self._values.get("dead_letter_queue")
        return typing.cast(typing.Optional[_IQueue_7ed6f679], result)

    @builtins.property
    def max_event_age(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The maximum age of a request that Lambda sends to a function for processing.

        Minimum value of 60.
        Maximum value of 86400.

        :default: Duration.hours(24)
        '''
        result = self._values.get("max_event_age")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def retry_attempts(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of times to retry when the function returns an error.

        Minimum value of 0.
        Maximum value of 185.

        :default: 185
        '''
        result = self._values.get("retry_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def input(self) -> typing.Optional[_RuleTargetInput_6beca786]:
        '''The input to the state machine execution.

        :default: the entire EventBridge event
        '''
        result = self._values.get("input")
        return typing.cast(typing.Optional[_RuleTargetInput_6beca786], result)

    @builtins.property
    def role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''The IAM role to be assumed to execute the State Machine.

        :default: - a new role will be created
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SfnStateMachineProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_events_targets.SnsTopicProps",
    jsii_struct_bases=[TargetBaseProps],
    name_mapping={
        "dead_letter_queue": "deadLetterQueue",
        "max_event_age": "maxEventAge",
        "retry_attempts": "retryAttempts",
        "message": "message",
    },
)
class SnsTopicProps(TargetBaseProps):
    def __init__(
        self,
        *,
        dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
        max_event_age: typing.Optional[_Duration_4839e8c3] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
        message: typing.Optional[_RuleTargetInput_6beca786] = None,
    ) -> None:
        '''Customize the SNS Topic Event Target.

        :param dead_letter_queue: The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_. The events not successfully delivered are automatically retried for a specified period of time, depending on the retry policy of the target. If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue. Default: - no dead-letter queue
        :param max_event_age: The maximum age of a request that Lambda sends to a function for processing. Minimum value of 60. Maximum value of 86400. Default: Duration.hours(24)
        :param retry_attempts: The maximum number of times to retry when the function returns an error. Minimum value of 0. Maximum value of 185. Default: 185
        :param message: The message to send to the topic. Default: the entire EventBridge event

        :exampleMetadata: infused

        Example::

            # on_commit_rule: events.Rule
            # topic: sns.Topic
            
            
            on_commit_rule.add_target(targets.SnsTopic(topic,
                message=events.RuleTargetInput.from_text(f"A commit was pushed to the repository {codecommit.ReferenceEvent.repositoryName} on branch {codecommit.ReferenceEvent.referenceName}")
            ))
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29b5b095e8884167f8f78e4ccfc6cd844ecb24d73c2e229d24c0a7a18ce7485f)
            check_type(argname="argument dead_letter_queue", value=dead_letter_queue, expected_type=type_hints["dead_letter_queue"])
            check_type(argname="argument max_event_age", value=max_event_age, expected_type=type_hints["max_event_age"])
            check_type(argname="argument retry_attempts", value=retry_attempts, expected_type=type_hints["retry_attempts"])
            check_type(argname="argument message", value=message, expected_type=type_hints["message"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if dead_letter_queue is not None:
            self._values["dead_letter_queue"] = dead_letter_queue
        if max_event_age is not None:
            self._values["max_event_age"] = max_event_age
        if retry_attempts is not None:
            self._values["retry_attempts"] = retry_attempts
        if message is not None:
            self._values["message"] = message

    @builtins.property
    def dead_letter_queue(self) -> typing.Optional[_IQueue_7ed6f679]:
        '''The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_.

        The events not successfully delivered are automatically retried for a specified period of time,
        depending on the retry policy of the target.
        If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue.

        :default: - no dead-letter queue
        '''
        result = self._values.get("dead_letter_queue")
        return typing.cast(typing.Optional[_IQueue_7ed6f679], result)

    @builtins.property
    def max_event_age(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The maximum age of a request that Lambda sends to a function for processing.

        Minimum value of 60.
        Maximum value of 86400.

        :default: Duration.hours(24)
        '''
        result = self._values.get("max_event_age")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def retry_attempts(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of times to retry when the function returns an error.

        Minimum value of 0.
        Maximum value of 185.

        :default: 185
        '''
        result = self._values.get("retry_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def message(self) -> typing.Optional[_RuleTargetInput_6beca786]:
        '''The message to send to the topic.

        :default: the entire EventBridge event
        '''
        result = self._values.get("message")
        return typing.cast(typing.Optional[_RuleTargetInput_6beca786], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SnsTopicProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_events_targets.SqsQueueProps",
    jsii_struct_bases=[TargetBaseProps],
    name_mapping={
        "dead_letter_queue": "deadLetterQueue",
        "max_event_age": "maxEventAge",
        "retry_attempts": "retryAttempts",
        "message": "message",
        "message_group_id": "messageGroupId",
    },
)
class SqsQueueProps(TargetBaseProps):
    def __init__(
        self,
        *,
        dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
        max_event_age: typing.Optional[_Duration_4839e8c3] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
        message: typing.Optional[_RuleTargetInput_6beca786] = None,
        message_group_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Customize the SQS Queue Event Target.

        :param dead_letter_queue: The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_. The events not successfully delivered are automatically retried for a specified period of time, depending on the retry policy of the target. If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue. Default: - no dead-letter queue
        :param max_event_age: The maximum age of a request that Lambda sends to a function for processing. Minimum value of 60. Maximum value of 86400. Default: Duration.hours(24)
        :param retry_attempts: The maximum number of times to retry when the function returns an error. Minimum value of 0. Maximum value of 185. Default: 185
        :param message: The message to send to the queue. Must be a valid JSON text passed to the target queue. Default: the entire EventBridge event
        :param message_group_id: Message Group ID for messages sent to this queue. Required for FIFO queues, leave empty for regular queues. Default: - no message group ID (regular queue)

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk as cdk
            from aws_cdk import aws_events as events
            from aws_cdk import aws_events_targets as events_targets
            from aws_cdk import aws_sqs as sqs
            
            # queue: sqs.Queue
            # rule_target_input: events.RuleTargetInput
            
            sqs_queue_props = events_targets.SqsQueueProps(
                dead_letter_queue=queue,
                max_event_age=cdk.Duration.minutes(30),
                message=rule_target_input,
                message_group_id="messageGroupId",
                retry_attempts=123
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6472cea5f7d90ec67bd493d4b2ba6bc083b2c915d8dc1da40193693c2eb79cc7)
            check_type(argname="argument dead_letter_queue", value=dead_letter_queue, expected_type=type_hints["dead_letter_queue"])
            check_type(argname="argument max_event_age", value=max_event_age, expected_type=type_hints["max_event_age"])
            check_type(argname="argument retry_attempts", value=retry_attempts, expected_type=type_hints["retry_attempts"])
            check_type(argname="argument message", value=message, expected_type=type_hints["message"])
            check_type(argname="argument message_group_id", value=message_group_id, expected_type=type_hints["message_group_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if dead_letter_queue is not None:
            self._values["dead_letter_queue"] = dead_letter_queue
        if max_event_age is not None:
            self._values["max_event_age"] = max_event_age
        if retry_attempts is not None:
            self._values["retry_attempts"] = retry_attempts
        if message is not None:
            self._values["message"] = message
        if message_group_id is not None:
            self._values["message_group_id"] = message_group_id

    @builtins.property
    def dead_letter_queue(self) -> typing.Optional[_IQueue_7ed6f679]:
        '''The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_.

        The events not successfully delivered are automatically retried for a specified period of time,
        depending on the retry policy of the target.
        If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue.

        :default: - no dead-letter queue
        '''
        result = self._values.get("dead_letter_queue")
        return typing.cast(typing.Optional[_IQueue_7ed6f679], result)

    @builtins.property
    def max_event_age(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The maximum age of a request that Lambda sends to a function for processing.

        Minimum value of 60.
        Maximum value of 86400.

        :default: Duration.hours(24)
        '''
        result = self._values.get("max_event_age")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def retry_attempts(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of times to retry when the function returns an error.

        Minimum value of 0.
        Maximum value of 185.

        :default: 185
        '''
        result = self._values.get("retry_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def message(self) -> typing.Optional[_RuleTargetInput_6beca786]:
        '''The message to send to the queue.

        Must be a valid JSON text passed to the target queue.

        :default: the entire EventBridge event
        '''
        result = self._values.get("message")
        return typing.cast(typing.Optional[_RuleTargetInput_6beca786], result)

    @builtins.property
    def message_group_id(self) -> typing.Optional[builtins.str]:
        '''Message Group ID for messages sent to this queue.

        Required for FIFO queues, leave empty for regular queues.

        :default: - no message group ID (regular queue)
        '''
        result = self._values.get("message_group_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SqsQueueProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ApiDestination",
    "ApiDestinationProps",
    "ApiGateway",
    "ApiGatewayProps",
    "AppSync",
    "AppSyncGraphQLApiProps",
    "AwsApi",
    "AwsApiInput",
    "AwsApiProps",
    "BatchJob",
    "BatchJobProps",
    "CloudWatchLogGroup",
    "CodeBuildProject",
    "CodeBuildProjectProps",
    "CodePipeline",
    "CodePipelineTargetOptions",
    "ContainerOverride",
    "EcsTask",
    "EcsTaskProps",
    "EventBus",
    "EventBusProps",
    "IDeliveryStream",
    "KinesisFirehoseStream",
    "KinesisFirehoseStreamProps",
    "KinesisFirehoseStreamV2",
    "KinesisStream",
    "KinesisStreamProps",
    "LambdaFunction",
    "LambdaFunctionProps",
    "LogGroupProps",
    "LogGroupTargetInput",
    "LogGroupTargetInputOptions",
    "SfnStateMachine",
    "SfnStateMachineProps",
    "SnsTopic",
    "SnsTopicProps",
    "SqsQueue",
    "SqsQueueProps",
    "Tag",
    "TargetBaseProps",
    "TaskEnvironmentVariable",
]

publication.publish()

def _typecheckingstub__1d106eb32ee82e64ee59c0904873ef15fb598d1b5613440afd038509ccbb15ea(
    api_destination: _IApiDestination_44cdeedd,
    *,
    event: typing.Optional[_RuleTargetInput_6beca786] = None,
    event_role: typing.Optional[_IRole_235f5d8e] = None,
    header_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    path_parameter_values: typing.Optional[typing.Sequence[builtins.str]] = None,
    query_string_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
    max_event_age: typing.Optional[_Duration_4839e8c3] = None,
    retry_attempts: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7fc3c1c0cf00ea5f22f33bc5b97cb9290363f2ca57adb35a3ef3345ba3c4ee26(
    _rule: _IRule_af9e3d28,
    _id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4351ee68d84b56105dfaf7566e76bf0350931a4945a4f9e2599f6310ff34c1f4(
    rest_api: _IRestApi_1f02523d,
    *,
    event_role: typing.Optional[_IRole_235f5d8e] = None,
    header_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    method: typing.Optional[builtins.str] = None,
    path: typing.Optional[builtins.str] = None,
    path_parameter_values: typing.Optional[typing.Sequence[builtins.str]] = None,
    post_body: typing.Optional[_RuleTargetInput_6beca786] = None,
    query_string_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    stage: typing.Optional[builtins.str] = None,
    dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
    max_event_age: typing.Optional[_Duration_4839e8c3] = None,
    retry_attempts: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f34d8ba93048cf243454dc97d2236199033c050fc0bbc6ff84e18fa6033ee8b0(
    rule: _IRule_af9e3d28,
    _id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56a99cbd83a0d7a956b68eb6ee5cedd89a2b1c37754c2dc7f5a5ea2ccffb1c7f(
    appsync_api: _IGraphqlApi_ed8270f3,
    *,
    graph_ql_operation: builtins.str,
    event_role: typing.Optional[_IRole_235f5d8e] = None,
    variables: typing.Optional[_RuleTargetInput_6beca786] = None,
    dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
    max_event_age: typing.Optional[_Duration_4839e8c3] = None,
    retry_attempts: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b1999a517525e35ef54e6129e3396c11b46ecb394388d3f908c6d627c051c4f(
    rule: _IRule_af9e3d28,
    _id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a41bcbfd7e37d2d2cf83a8f636d325a2a328da0a83ef4d994f0be12782f7d357(
    rule: _IRule_af9e3d28,
    id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2fe69d44df432ded25b817ab8882c534b11b4e6a93f032091c7ab9ea0763f88(
    *,
    action: builtins.str,
    service: builtins.str,
    api_version: typing.Optional[builtins.str] = None,
    catch_error_pattern: typing.Optional[builtins.str] = None,
    parameters: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0959cf5a09d52d03f2591de3b911528bd507126b7e2027cd7c4585de25301ad(
    *,
    action: builtins.str,
    service: builtins.str,
    api_version: typing.Optional[builtins.str] = None,
    catch_error_pattern: typing.Optional[builtins.str] = None,
    parameters: typing.Any = None,
    policy_statement: typing.Optional[_PolicyStatement_0fe33853] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47158c034f7c0f0c69db5367db77245ba70cbcc56ed81ec05ad80116fa6238e6(
    job_queue_arn: builtins.str,
    job_queue_scope: _constructs_77d1e7e8.IConstruct,
    job_definition_arn: builtins.str,
    job_definition_scope: _constructs_77d1e7e8.IConstruct,
    *,
    attempts: typing.Optional[jsii.Number] = None,
    event: typing.Optional[_RuleTargetInput_6beca786] = None,
    job_name: typing.Optional[builtins.str] = None,
    size: typing.Optional[jsii.Number] = None,
    dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
    max_event_age: typing.Optional[_Duration_4839e8c3] = None,
    retry_attempts: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__154b5229eec4b919f6367b1ffec428480b40785475052bfd94fade237bd22597(
    rule: _IRule_af9e3d28,
    _id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7cd04d50c1c36eb2be36abb3fbdf553a534c7ae5d60f1c9cac6b5cf6428d284(
    log_group: _ILogGroup_3c4fa718,
    *,
    event: typing.Optional[_RuleTargetInput_6beca786] = None,
    install_latest_aws_sdk: typing.Optional[builtins.bool] = None,
    log_event: typing.Optional[LogGroupTargetInput] = None,
    dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
    max_event_age: typing.Optional[_Duration_4839e8c3] = None,
    retry_attempts: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5583066efc6b7b2980bfbfbf33e6491271f5faf3b97e5d2ae998d1fe4189d1d4(
    _rule: _IRule_af9e3d28,
    _id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a8679d207265b7ec6863cf63c5b8aaaa8577dce8b9b2c6ec8d9a52c6bde44f1(
    project: _IProject_aafae30a,
    *,
    event: typing.Optional[_RuleTargetInput_6beca786] = None,
    event_role: typing.Optional[_IRole_235f5d8e] = None,
    dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
    max_event_age: typing.Optional[_Duration_4839e8c3] = None,
    retry_attempts: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c864909db0683c496942d72c9b834b03e1082bec9e20c368a204df37449c6e48(
    _rule: _IRule_af9e3d28,
    _id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__daa7b4e77a0ef964ea3cdb54ce57cc8f475d7342b57d85f348e63fff7e5ecc14(
    pipeline: _IPipeline_0931f838,
    *,
    event_role: typing.Optional[_IRole_235f5d8e] = None,
    dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
    max_event_age: typing.Optional[_Duration_4839e8c3] = None,
    retry_attempts: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__add42f3c28d5f6651e451885b955fd84ad865300b4e6606be36174db4f3d8c73(
    _rule: _IRule_af9e3d28,
    _id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c13bb1641d81a866856c7cdeae6fa612e09bb941bc83053a19b901e3040ba066(
    *,
    container_name: builtins.str,
    command: typing.Optional[typing.Sequence[builtins.str]] = None,
    cpu: typing.Optional[jsii.Number] = None,
    environment: typing.Optional[typing.Sequence[typing.Union[TaskEnvironmentVariable, typing.Dict[builtins.str, typing.Any]]]] = None,
    memory_limit: typing.Optional[jsii.Number] = None,
    memory_reservation: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ad199a8641f171a0447e974756bbddd91b00aaa9bcf33d231826916b85b8166(
    _rule: _IRule_af9e3d28,
    _id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6012a31db9ac91c35876daca0265cba4fbb81bfdf8acd148b62786503371d52(
    event_bus: _IEventBus_88d13111,
    *,
    dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00d16e4ddfa6305196a715a56432c551f3ba5a905dead2e6a85f30bad692c31f(
    rule: _IRule_af9e3d28,
    _id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5af20e134873490c1ac4788761972ccd53cd625edbd9b75c1c1f0b1a334b56ba(
    *,
    dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6dba8ed5e351380147a927ce30f4c9095bc69a54a2de45039c2a1d8275dc88c(
    stream: _CfnDeliveryStream_8f3b1735,
    *,
    message: typing.Optional[_RuleTargetInput_6beca786] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b38a65da97645536b57df6537ab7a5b06cf8910d4235008699171e7ced62c584(
    _rule: _IRule_af9e3d28,
    _id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81d5bbf50681705e8fea422823feb918a4c9bd4be7914a6acf6200ac65c3aa81(
    *,
    message: typing.Optional[_RuleTargetInput_6beca786] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8230487c5e79599a4ad63af004c2c8350c2b25e209491350274d38019afa418(
    stream: IDeliveryStream,
    *,
    message: typing.Optional[_RuleTargetInput_6beca786] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3467ab0e593ed64d775dafc3b3fc1b1835fa2853c7ee8685668bf081dd189e44(
    _rule: _IRule_af9e3d28,
    _id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47a9d917a1971c5aa11b68bf823d9f34a57a7b1e7653b0f82809c06309cac1a6(
    stream: _IStream_4e2457d2,
    *,
    message: typing.Optional[_RuleTargetInput_6beca786] = None,
    partition_key_path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae222f596f043d31f56819c2cb64c58ef12e8e3d35bce41fa6f0cd929c2db58a(
    _rule: _IRule_af9e3d28,
    _id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__971b6fc6dc302be6b6401547a0731521d858936fe589a0d096ef25e81e707b46(
    *,
    message: typing.Optional[_RuleTargetInput_6beca786] = None,
    partition_key_path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ed39c6222adc3f41ac8913ef4f7e22134443e2aa19c19114f6650e1d987c3c4(
    handler: _IFunction_6adb0ab8,
    *,
    event: typing.Optional[_RuleTargetInput_6beca786] = None,
    dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
    max_event_age: typing.Optional[_Duration_4839e8c3] = None,
    retry_attempts: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__906b4fb6301e027a5cc5111944bf8d3844e211a5f528e71002c42bebd068aad6(
    rule: _IRule_af9e3d28,
    _id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__758083b81fe2898a867779bb9918a1aaa26f0291624b27f0e1637860027d86a5(
    rule: _IRule_af9e3d28,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12b2a1770edaa7f8ba5d731e85339d65d757aa25fd54d6c6be4746c6a4f4a070(
    *,
    message: typing.Any = None,
    timestamp: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__257316eeebae5ef658a5b570361035fdfb5ab37e96962b24c2e814b0702cba68(
    machine: _IStateMachine_73e8d2b0,
    *,
    input: typing.Optional[_RuleTargetInput_6beca786] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
    dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
    max_event_age: typing.Optional[_Duration_4839e8c3] = None,
    retry_attempts: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e0733fbe09a8310edfc7237ca759e925b3db6d25ad43627fcf4f165c2efe942(
    _rule: _IRule_af9e3d28,
    _id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b58aa74b2a717b90ef291556746b786df8882b8158b4b3255bf88691dbd8fd07(
    topic: _ITopic_9eca4852,
    *,
    message: typing.Optional[_RuleTargetInput_6beca786] = None,
    dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
    max_event_age: typing.Optional[_Duration_4839e8c3] = None,
    retry_attempts: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6de2339b649dec356056a716737bfe488b0873abee2d224f4a18f7ad162d83f6(
    _rule: _IRule_af9e3d28,
    _id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26484816bdcb2fef6d100370a28b06c1fd038591b98fcbe847383a51245c79f9(
    queue: _IQueue_7ed6f679,
    *,
    message: typing.Optional[_RuleTargetInput_6beca786] = None,
    message_group_id: typing.Optional[builtins.str] = None,
    dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
    max_event_age: typing.Optional[_Duration_4839e8c3] = None,
    retry_attempts: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7bbb7c546d67f5f999da3b2a71dc36c03ae5d8723a592b50de5b0193d62ebe6(
    rule: _IRule_af9e3d28,
    _id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a813f48d70b31d8149568e4c733eee0b3ddf93c3d8ee22172032406da2f91b10(
    *,
    key: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c149bf0de902d492c0a50daf03a233ef8286c2fb8799f305c9e4b91ffc8d577(
    *,
    dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
    max_event_age: typing.Optional[_Duration_4839e8c3] = None,
    retry_attempts: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad8ad9cb08b1d9914f8ba21360b8735e425827635478e4e057a6f1dc9f660930(
    *,
    name: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a7e2f14909f24e23bf0efd9e767b25ab4257897a69dccc79351ad4456fe857a(
    *,
    dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
    max_event_age: typing.Optional[_Duration_4839e8c3] = None,
    retry_attempts: typing.Optional[jsii.Number] = None,
    event: typing.Optional[_RuleTargetInput_6beca786] = None,
    event_role: typing.Optional[_IRole_235f5d8e] = None,
    header_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    path_parameter_values: typing.Optional[typing.Sequence[builtins.str]] = None,
    query_string_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed5e368611ecca03be97333615df4f6727992e87138462a27cc1f9a4cdf3a511(
    *,
    dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
    max_event_age: typing.Optional[_Duration_4839e8c3] = None,
    retry_attempts: typing.Optional[jsii.Number] = None,
    event_role: typing.Optional[_IRole_235f5d8e] = None,
    header_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    method: typing.Optional[builtins.str] = None,
    path: typing.Optional[builtins.str] = None,
    path_parameter_values: typing.Optional[typing.Sequence[builtins.str]] = None,
    post_body: typing.Optional[_RuleTargetInput_6beca786] = None,
    query_string_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    stage: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aea6c33be1be64052595742c1fdd00fb0f53185ebe3c9f93ceacd92d82655d1d(
    *,
    dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
    max_event_age: typing.Optional[_Duration_4839e8c3] = None,
    retry_attempts: typing.Optional[jsii.Number] = None,
    graph_ql_operation: builtins.str,
    event_role: typing.Optional[_IRole_235f5d8e] = None,
    variables: typing.Optional[_RuleTargetInput_6beca786] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91b263189af78d46fd5bf421034197688036a7347fbaee9bef843d928f9bb43f(
    *,
    dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
    max_event_age: typing.Optional[_Duration_4839e8c3] = None,
    retry_attempts: typing.Optional[jsii.Number] = None,
    attempts: typing.Optional[jsii.Number] = None,
    event: typing.Optional[_RuleTargetInput_6beca786] = None,
    job_name: typing.Optional[builtins.str] = None,
    size: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0aa7b3ccb4774f7e12d466bbcb6662ffc40cea68d16ffd9b2fff0a4a8ff49b72(
    *,
    dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
    max_event_age: typing.Optional[_Duration_4839e8c3] = None,
    retry_attempts: typing.Optional[jsii.Number] = None,
    event: typing.Optional[_RuleTargetInput_6beca786] = None,
    event_role: typing.Optional[_IRole_235f5d8e] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c1acf9f087ecbbaf384c1beceee58dbb3a425d691a10d8da9317706e37e3dfe(
    *,
    dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
    max_event_age: typing.Optional[_Duration_4839e8c3] = None,
    retry_attempts: typing.Optional[jsii.Number] = None,
    event_role: typing.Optional[_IRole_235f5d8e] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3624031da4f9372e2ccdb3e422123cc459d01922cc36bab5b96caa98fc41c5b1(
    *,
    dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
    max_event_age: typing.Optional[_Duration_4839e8c3] = None,
    retry_attempts: typing.Optional[jsii.Number] = None,
    cluster: _ICluster_16cddd09,
    task_definition: _ITaskDefinition_889ba4d8,
    assign_public_ip: typing.Optional[builtins.bool] = None,
    container_overrides: typing.Optional[typing.Sequence[typing.Union[ContainerOverride, typing.Dict[builtins.str, typing.Any]]]] = None,
    enable_execute_command: typing.Optional[builtins.bool] = None,
    launch_type: typing.Optional[_LaunchType_6894135d] = None,
    platform_version: typing.Optional[_FargatePlatformVersion_55d8be5c] = None,
    propagate_tags: typing.Optional[_PropagatedTagSource_ad4e874a] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
    security_groups: typing.Optional[typing.Sequence[_ISecurityGroup_acf8a799]] = None,
    subnet_selection: typing.Optional[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[Tag, typing.Dict[builtins.str, typing.Any]]]] = None,
    task_count: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e34dd9ce66add58b9a28d19d7823e686db2c0d099525e77c896c992c0318854(
    *,
    dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
    max_event_age: typing.Optional[_Duration_4839e8c3] = None,
    retry_attempts: typing.Optional[jsii.Number] = None,
    event: typing.Optional[_RuleTargetInput_6beca786] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__955ae13452482b1f3001946153d6bfa138fb7c7e8a5c482a52178f35142a7c9c(
    *,
    dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
    max_event_age: typing.Optional[_Duration_4839e8c3] = None,
    retry_attempts: typing.Optional[jsii.Number] = None,
    event: typing.Optional[_RuleTargetInput_6beca786] = None,
    install_latest_aws_sdk: typing.Optional[builtins.bool] = None,
    log_event: typing.Optional[LogGroupTargetInput] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e7617cf19a253c5e65116870d86237c3f90f88155a00afbdd412e561c617258(
    *,
    dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
    max_event_age: typing.Optional[_Duration_4839e8c3] = None,
    retry_attempts: typing.Optional[jsii.Number] = None,
    input: typing.Optional[_RuleTargetInput_6beca786] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29b5b095e8884167f8f78e4ccfc6cd844ecb24d73c2e229d24c0a7a18ce7485f(
    *,
    dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
    max_event_age: typing.Optional[_Duration_4839e8c3] = None,
    retry_attempts: typing.Optional[jsii.Number] = None,
    message: typing.Optional[_RuleTargetInput_6beca786] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6472cea5f7d90ec67bd493d4b2ba6bc083b2c915d8dc1da40193693c2eb79cc7(
    *,
    dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
    max_event_age: typing.Optional[_Duration_4839e8c3] = None,
    retry_attempts: typing.Optional[jsii.Number] = None,
    message: typing.Optional[_RuleTargetInput_6beca786] = None,
    message_group_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
